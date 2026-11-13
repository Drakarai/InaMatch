import Phaser from 'phaser';
import { music } from '../audio/music';
import { sfx } from '../audio/sfx';
import { loadClub, saveClub } from '../club/club';
import { GAME_H, GAME_W, PORTRAIT } from '../config';
import { getTeam, TEAMS } from '../data';
import { SEASONS } from '../data/seasons';
import type { TeamData } from '../data/types';
import { defaultLineup } from '../engine/lineup';
import { teamRating } from '../engine/rating';
import { ensureSprites } from '../gfx/pack';
import { texKey } from '../gfx/placeholders';
import { DIFFICULTIES, getSettings } from '../settings';
import {
  createCup,
  createLeague,
  CUP_SIZE,
  finishWithoutUser,
  LEAGUE_SIZE,
  loadTourney,
  pickOpponents,
  recordUserResult,
  roundName,
  saveTourney,
  standings,
  TOURNEY_COINS,
  TOURNEY_REGISTRY,
  TOURNEY_RESULT,
  tourneyCoins,
  userMatch,
  userPlace,
  winnerOf,
  type MatchResult,
  type Tourney,
  type TourneyKind,
  type TourneyMatchResult,
} from '../tournament/tournament';
import { THEME, cardPanel, coinChip, confirmDialog, fitCamera, glow, inkOn, stadiumBackdrop, topBar } from '../ui/theme';
import { Button, display, fitWidth, label } from '../ui/widgets';

/** Temporadas para elegir equipo (Mi club incluido si existe). */
const PICK_SEASONS = SEASONS.filter((s) => s.id !== 'otros');

const exists = (id: string) => TEAMS.some((t) => t.id === id);
const rating = (id: string) => {
  try {
    return teamRating(getTeam(id));
  } catch {
    return 50;
  }
};
const teamName = (id: string) => {
  try {
    return getTeam(id).name;
  } catch {
    return id;
  }
};

/**
 * Modo torneo: copa de 8 equipos (eliminatorias; los empates, a penaltis) o liga de 6 (todos contra todos).
 * Se elige el formato, el equipo propio y de dónde salen los rivales; luego, ronda a ronda, se juega el partido
 * propio y el resto se simula. El torneo en curso se guarda: se puede salir y seguir más tarde.
 */
export class TournamentScene extends Phaser.Scene {
  private view!: Phaser.GameObjects.Container;
  private tourney: Tourney | null = null;
  private kind: TourneyKind = 'cup';
  private season = 'ie1';
  private busy = false;
  private modal: Phaser.GameObjects.Container | null = null;

  constructor() {
    super('tournament');
  }

  create(): void {
    fitCamera(this);
    music.play('menu');
    this.busy = false;
    this.modal = null;
    stadiumBackdrop(this, THEME.home, THEME.yellow);
    this.view = this.add.container(0, 0);
    this.tourney = loadTourney(exists);
    // vuelta de un partido del torneo
    const res = this.registry.get(TOURNEY_RESULT) as TourneyMatchResult | undefined;
    this.registry.remove(TOURNEY_RESULT);
    this.registry.remove(TOURNEY_REGISTRY);
    if (res && this.tourney && userMatch(this.tourney)) {
      const before = this.tourney;
      this.tourney = recordUserResult(before, res.goalsFor, res.goalsAgainst, rating, Math.random);
      saveTourney(this.tourney);
      this.showTourney();
      this.afterRound(before, res);
      return;
    }
    if (this.tourney) this.showTourney();
    else this.showKind();
    this.input.keyboard?.on('keydown-ESC', () => !this.busy && this.scene.start('title'));
  }

  private back(): Phaser.GameObjects.Container {
    return topBar(this, {
      title: 'Torneo',
      subtitle: 'Copa o liga contra equipos de la saga',
      back: { label: 'Inicio', onClick: () => this.scene.start('title') },
    });
  }

  // ------------------------------------------------------------- crear

  /** Paso 1: copa o liga. */
  private showKind(): void {
    const c = this.view.removeAll(true);
    c.add(this.back());
    c.add(label(this, GAME_W / 2, PORTRAIT ? 120 : 112, 'Elige el formato', PORTRAIT ? 22 : 24, '#ffffff', { fontStyle: 'bold italic' }).setOrigin(0.5));
    const opts: { kind: TourneyKind; title: string; lines: string[]; icon: string }[] = [
      { kind: 'cup', title: 'COPA', icon: '🏆', lines: [`${CUP_SIZE} equipos, eliminatorias`, 'Cuartos, semifinales y final', 'Si hay empate: penaltis'] },
      { kind: 'league', title: 'LIGA', icon: '📋', lines: [`${LEAGUE_SIZE} equipos, todos contra todos`, `${LEAGUE_SIZE - 1} jornadas a una vuelta`, 'Victoria 3 puntos, empate 1'] },
    ];
    const w = PORTRAIT ? GAME_W - 60 : 400;
    const h = PORTRAIT ? 250 : 320;
    opts.forEach((o, i) => {
      const x = PORTRAIT ? GAME_W / 2 : GAME_W / 2 + (i - 0.5) * (w + 40);
      const y = PORTRAIT ? 300 + i * (h + 30) : 360;
      const g = this.add.graphics();
      cardPanel(g, x - w / 2, y - h / 2, w, h, { accent: i ? THEME.cyan : THEME.yellow, alpha: 0.95 });
      glow(g, x, y - h * 0.18, w * 0.4, i ? THEME.cyan : THEME.yellow, 0.18);
      c.add(g);
      c.add(label(this, x, y - h / 2 + (PORTRAIT ? 50 : 70), o.icon, PORTRAIT ? 44 : 60, '#ffffff').setOrigin(0.5));
      c.add(display(this, x, y - h / 2 + (PORTRAIT ? 110 : 150), o.title, PORTRAIT ? 44 : 54, i ? THEME.cyanCss : THEME.yellowCss).setOrigin(0.5));
      o.lines.forEach((l, k) => c.add(label(this, x, y - h / 2 + (PORTRAIT ? 150 : 200) + k * 24, l, PORTRAIT ? 15 : 16, '#dce6f5').setOrigin(0.5)));
      const hit = this.add.zone(x, y, w, h).setInteractive({ useHandCursor: true });
      hit.on('pointerover', () => g.setAlpha(1));
      hit.on('pointerup', () => {
        sfx.click();
        this.kind = o.kind;
        this.showTeams();
      });
      c.add(hit);
    });
    const d = DIFFICULTIES[getSettings().difficulty];
    c.add(label(this, GAME_W / 2, GAME_H - (PORTRAIT ? 40 : 34), `Dificultad: ${d.label}  ·  se cambia en los ajustes de la pantalla de inicio (⚙)`, PORTRAIT ? 12 : 13, THEME.muted, { fontStyle: 'italic', align: 'center', wordWrap: { width: GAME_W - 40 } }).setOrigin(0.5));
  }

  /** Paso 2: el equipo propio, por temporadas. */
  private showTeams(): void {
    const c = this.view.removeAll(true);
    c.add(
      topBar(this, {
        title: this.kind === 'cup' ? 'Copa: tu equipo' : 'Liga: tu equipo',
        subtitle: 'Elige con qué equipo juegas',
        back: { label: 'Formato', onClick: () => this.showKind() },
      }),
    );
    const seasons = PICK_SEASONS.filter((s) => TEAMS.some((t) => t.season === s.id));
    if (!seasons.some((s) => s.id === this.season)) this.season = seasons[0]?.id ?? 'ie1';
    const tabY = PORTRAIT ? 104 : 100;
    const tw = Math.min(PORTRAIT ? 50 : 110, (GAME_W - 24) / seasons.length);
    seasons.forEach((s, i) => {
      const x = GAME_W / 2 + (i - (seasons.length - 1) / 2) * tw;
      const on = s.id === this.season;
      const g = this.add.graphics();
      g.fillStyle(on ? THEME.yellow : 0x10203a, on ? 1 : 0.85).fillRoundedRect(x - tw / 2 + 3, tabY - 26, tw - 6, 52, 10);
      c.add(g);
      const key = `series:${s.icon}`;
      if (s.icon && this.textures.exists(key)) {
        const img = this.add.image(x, tabY, key);
        img.setScale(Math.min(40 / img.height, (tw - 12) / img.width));
        c.add(img);
      } else c.add(fitWidth(label(this, x, tabY, s.short, 13, on ? '#0b1a2e' : '#ffffff', { fontStyle: 'bold' }).setOrigin(0.5), tw - 10, 8));
      const hit = this.add.zone(x, tabY, tw - 6, 52).setInteractive({ useHandCursor: true });
      hit.on('pointerup', () => {
        this.season = s.id;
        this.showTeams();
      });
      c.add(hit);
    });
    const season = seasons.find((s) => s.id === this.season);
    c.add(label(this, GAME_W / 2, tabY + 44, season?.name ?? '', PORTRAIT ? 16 : 18, '#ffd23f', { fontStyle: 'bold italic' }).setOrigin(0.5));
    const teams = TEAMS.filter((t) => t.season === this.season);
    const cols = PORTRAIT ? 3 : 6;
    const top = tabY + 70;
    const cw = (GAME_W - 40) / cols;
    const rows = Math.ceil(teams.length / cols);
    const ch = Math.min(PORTRAIT ? 150 : 132, (GAME_H - top - 20) / Math.max(1, rows));
    teams.forEach((t, i) => {
      const x = 20 + (i % cols) * cw + cw / 2;
      const y = top + Math.floor(i / cols) * ch + ch / 2;
      const g = this.add.graphics();
      g.fillStyle(0x10203a, 0.92).fillRoundedRect(x - cw / 2 + 5, y - ch / 2 + 4, cw - 10, ch - 8, 12);
      g.lineStyle(2, 0xffffff, 0.15).strokeRoundedRect(x - cw / 2 + 5, y - ch / 2 + 4, cw - 10, ch - 8, 12);
      c.add(g);
      const es = Math.min(ch * 0.46, 64);
      if (this.textures.exists(texKey.emblem(t.id))) c.add(this.add.image(x, y - ch * 0.14, texKey.emblem(t.id)).setDisplaySize(es, es));
      c.add(fitWidth(label(this, x, y + ch * 0.2, t.name, 12, '#ffffff', { fontStyle: 'bold', align: 'center' }).setOrigin(0.5), cw - 18, 8));
      c.add(fitWidth(label(this, x, y + ch * 0.36, `Media ${teamRating(t)}`, 10, '#9fb3d1', { fontStyle: 'italic' }).setOrigin(0.5), cw - 18, 8));
      const hit = this.add.zone(x, y, cw - 10, ch - 8).setInteractive({ useHandCursor: true });
      hit.on('pointerup', () => this.showRivals(t));
      c.add(hit);
    });
  }

  /** Paso 3: de dónde salen los rivales, y a empezar. */
  private showRivals(team: TeamData): void {
    sfx.click();
    const need = (this.kind === 'cup' ? CUP_SIZE : LEAGUE_SIZE) - 1;
    const pool = (filter: (t: TeamData) => boolean) => TEAMS.filter((t) => t.id !== team.id && t.id !== 'club' && filter(t)).map((t) => t.id);
    const r = rating(team.id);
    const options: { title: string; sub: string; ids: string[] }[] = [
      { title: 'Toda la saga', sub: 'Rivales al azar de todas las temporadas', ids: pool(() => true) },
      { title: 'Misma temporada', sub: 'Solo equipos de su juego', ids: team.season === 'club' ? [] : pool((t) => t.season === team.season) },
      { title: 'De su nivel', sub: 'Equipos con una media parecida', ids: pool((t) => Math.abs(teamRating(t) - r) <= 4) },
      { title: 'Los mejores', sub: 'Solo equipos de media alta', ids: pool((t) => teamRating(t) >= 66) },
    ];
    this.modal?.destroy();
    const c = this.add.container(0, 0).setDepth(300);
    this.modal = c;
    c.add(this.add.rectangle(0, 0, GAME_W, GAME_H, 0x000000, 0.7).setOrigin(0).setInteractive());
    const W = PORTRAIT ? GAME_W - 32 : 560;
    const H = PORTRAIT ? 600 : 520;
    const x = (GAME_W - W) / 2;
    const y = (GAME_H - H) / 2;
    const g = this.add.graphics();
    cardPanel(g, x, y, W, H, { accent: THEME.yellow, alpha: 0.98 });
    c.add(g);
    if (this.textures.exists(texKey.emblem(team.id))) c.add(this.add.image(x + 56, y + 56, texKey.emblem(team.id)).setDisplaySize(72, 72));
    c.add(fitWidth(display(this, x + 104, y + 44, team.name, 30, '#ffd23f').setOrigin(0, 0.5), W - 130, 16));
    c.add(label(this, x + 106, y + 74, `${this.kind === 'cup' ? 'Copa' : 'Liga'}  ·  ¿contra quién?`, 15, '#dce6f5', { fontStyle: 'italic' }).setOrigin(0, 0.5));
    const bh = PORTRAIT ? 92 : 78;
    options.forEach((o, i) => {
      const enough = o.ids.length >= need;
      const by = y + 140 + i * (bh + 10);
      const b = new Button(this, GAME_W / 2, by, o.title, () => this.start(team.id, o.ids), { w: W - 48, h: bh - 18, size: 20, variant: i ? 'secondary' : 'primary' });
      b.setEnabled(enough);
      c.add(b);
      c.add(label(this, GAME_W / 2, by + bh / 2 - 6, enough ? o.sub : 'No hay bastantes equipos', 12, enough ? THEME.muted : THEME.coralCss, { fontStyle: 'italic' }).setOrigin(0.5));
    });
    c.add(new Button(this, GAME_W / 2, y + H - 40, 'Cancelar', () => c.destroy(), { w: 180, h: 44, variant: 'ghost', size: 16 }));
  }

  private start(user: string, candidates: string[]): void {
    const need = (this.kind === 'cup' ? CUP_SIZE : LEAGUE_SIZE) - 1;
    const rivals = pickOpponents(user, candidates, need, Math.random);
    this.tourney = this.kind === 'cup' ? createCup(user, rivals, Math.random) : createLeague(user, rivals, Math.random);
    saveTourney(this.tourney);
    sfx.whistle();
    this.modal?.destroy();
    this.modal = null;
    this.showTourney();
  }

  // ------------------------------------------------------------- en juego

  private showTourney(): void {
    const t = this.tourney!;
    const c = this.view.removeAll(true);
    const title = t.kind === 'cup' ? 'Copa' : 'Liga';
    const sub = t.champion ? `Campeón: ${teamName(t.champion)}` : t.out ? 'Eliminado' : roundName(t);
    c.add(topBar(this, { title: `${title} · ${teamName(t.user)}`, subtitle: sub, back: { label: 'Inicio', onClick: () => this.scene.start('title') }, icon: texKey.emblem(t.user) }));
    const save = loadClub();
    if (save && !PORTRAIT) c.add(coinChip(this, GAME_W - 24, 32, save.coins));
    if (t.kind === 'cup') this.drawBracket(c, t);
    else this.drawLeague(c, t);
    this.drawActions(c, t);
  }

  /** Casilla de un partido: los dos equipos con su escudo y su resultado. */
  private matchBox(c: Phaser.GameObjects.Container, m: MatchResult | null, x: number, y: number, w: number, user: string, highlight = false): void {
    const h = 64;
    const g = this.add.graphics();
    const mine = !!m && (m.home === user || m.away === user);
    g.fillStyle(0x0b1a2e, 0.94).fillRoundedRect(x, y, w, h, 10);
    g.lineStyle(2, highlight ? THEME.yellow : mine ? THEME.cyan : 0xffffff, highlight ? 1 : mine ? 0.8 : 0.15).strokeRoundedRect(x, y, w, h, 10);
    g.lineStyle(1, 0xffffff, 0.08).lineBetween(x + 8, y + h / 2, x + w - 8, y + h / 2);
    c.add(g);
    if (!m) {
      c.add(label(this, x + w / 2, y + h / 2, '—', 14, THEME.muted).setOrigin(0.5));
      return;
    }
    const win = winnerOf(m);
    const row = (team: string, goals: number | null, pens: number | undefined, ry: number) => {
      const lost = win !== null && win !== team;
      if (this.textures.exists(texKey.emblem(team))) c.add(this.add.image(x + 18, ry, texKey.emblem(team)).setDisplaySize(22, 22).setAlpha(lost ? 0.5 : 1));
      c.add(fitWidth(label(this, x + 34, ry, teamName(team), 13, team === user ? THEME.cyanCss : lost ? THEME.muted : '#ffffff', { fontStyle: 'bold' }).setOrigin(0, 0.5), w - 34 - 50, 9));
      if (goals !== null) c.add(label(this, x + w - 12, ry, pens !== undefined ? `${goals} (${pens})` : String(goals), 15, lost ? THEME.muted : '#ffd23f', { fontStyle: 'bold' }).setOrigin(1, 0.5));
    };
    row(m.home, m.hg, m.pens?.home, y + h / 4 + 1);
    row(m.away, m.ag, m.pens?.away, y + (h * 3) / 4 - 1);
  }

  private drawBracket(c: Phaser.GameObjects.Container, t: Tourney): void {
    const rounds = [4, 2, 1];
    const names = ['Cuartos', 'Semifinales', 'Final'];
    const top = PORTRAIT ? 84 : 92;
    if (PORTRAIT) {
      // en el móvil: las rondas una debajo de otra, en dos columnas
      let y = top;
      rounds.forEach((n, r) => {
        c.add(label(this, 20, y + 10, names[r], 15, r === t.round && !t.champion ? '#ffd23f' : '#ffffff', { fontStyle: 'bold italic' }).setOrigin(0, 0.5));
        y += 24;
        const w = n === 1 ? GAME_W - 40 : (GAME_W - 50) / 2;
        for (let i = 0; i < n; i++) {
          const mx = n === 1 ? 20 : 20 + (i % 2) * (w + 10);
          const my = y + Math.floor(i / 2) * 72;
          this.matchBox(c, t.rounds[r]?.[i] ?? null, mx, my, w, t.user, r === t.round && !t.champion && !t.out && !!t.rounds[r]?.[i] && [t.rounds[r][i].home, t.rounds[r][i].away].includes(t.user));
        }
        y += Math.ceil(n / 2) * 72 + 8;
      });
      if (t.champion) this.championBadge(c, GAME_W / 2, y + 40, t.champion, 70);
      return;
    }
    const colW = 250;
    const gapX = 60;
    const x0 = (GAME_W - (colW * 3 + gapX * 2 + 220)) / 2;
    const areaTop = top + 40;
    const areaH = GAME_H - areaTop - 120;
    const lines = this.add.graphics();
    c.add(lines);
    rounds.forEach((n, r) => {
      const x = x0 + r * (colW + gapX);
      c.add(label(this, x + colW / 2, top + 12, names[r], 17, r === t.round && !t.champion ? '#ffd23f' : '#ffffff', { fontStyle: 'bold italic' }).setOrigin(0.5));
      for (let i = 0; i < n; i++) {
        const slot = areaH / n;
        const y = areaTop + slot * i + slot / 2 - 32;
        const m = t.rounds[r]?.[i] ?? null;
        const live = r === t.round && !t.champion && !t.out && !!m && (m.home === t.user || m.away === t.user);
        this.matchBox(c, m, x, y, colW, t.user, live);
        // líneas hacia el siguiente partido
        if (r < 2) {
          const nx = x + colW + gapX;
          const ny = areaTop + (areaH / (n / 2)) * Math.floor(i / 2) + areaH / (n / 2) / 2;
          lines.lineStyle(2, 0xffffff, 0.18).beginPath().moveTo(x + colW, y + 32).lineTo(x + colW + gapX / 2, y + 32).lineTo(x + colW + gapX / 2, ny).lineTo(nx, ny).strokePath();
        }
      }
    });
    const fx = x0 + 3 * (colW + gapX) - gapX + 40;
    lines.lineStyle(2, 0xffffff, 0.18).lineBetween(x0 + 2 * (colW + gapX) + colW, areaTop + areaH / 2, fx, areaTop + areaH / 2);
    if (t.champion) this.championBadge(c, fx + 90, areaTop + areaH / 2, t.champion, 110);
    else {
      c.add(label(this, fx + 90, areaTop + areaH / 2 - 70, '🏆', 64, '#ffffff').setOrigin(0.5).setAlpha(0.35));
      c.add(label(this, fx + 90, areaTop + areaH / 2 + 10, 'Campeón', 16, THEME.muted, { fontStyle: 'italic' }).setOrigin(0.5));
    }
  }

  private championBadge(c: Phaser.GameObjects.Container, x: number, y: number, team: string, size: number): void {
    const g = this.add.graphics();
    glow(g, x, y, size * 1.3, THEME.yellow, 0.3);
    c.add(g);
    if (this.textures.exists(texKey.emblem(team))) c.add(this.add.image(x, y - 10, texKey.emblem(team)).setDisplaySize(size, size));
    c.add(label(this, x, y - size / 2 - 26, '🏆 CAMPEÓN', 16, '#ffd23f', { fontStyle: 'bold' }).setOrigin(0.5));
    c.add(fitWidth(label(this, x, y + size / 2 + 6, teamName(team), 15, '#ffffff', { fontStyle: 'bold', align: 'center' }).setOrigin(0.5), 200, 10));
  }

  private drawLeague(c: Phaser.GameObjects.Container, t: Tourney): void {
    const table = standings(t);
    const top = PORTRAIT ? 92 : 96;
    const tx = PORTRAIT ? 16 : 40;
    const tw = PORTRAIT ? GAME_W - 32 : 640;
    const rowH = PORTRAIT ? 44 : 50;
    const g = this.add.graphics();
    cardPanel(g, tx, top, tw, 46 + rowH * table.length + 10, { accent: THEME.cyan, alpha: 0.94 });
    c.add(g);
    const cols = PORTRAIT
      ? [
          { k: 'PJ', x: tw - 220 },
          { k: 'G', x: tw - 182 },
          { k: 'E', x: tw - 150 },
          { k: 'P', x: tw - 118 },
          { k: 'DG', x: tw - 76 },
          { k: 'Pts', x: tw - 28 },
        ]
      : [
          { k: 'PJ', x: tw - 330 },
          { k: 'G', x: tw - 280 },
          { k: 'E', x: tw - 240 },
          { k: 'P', x: tw - 200 },
          { k: 'GF', x: tw - 160 },
          { k: 'GC', x: tw - 120 },
          { k: 'Pts', x: tw - 50 },
        ];
    cols.forEach((col) => c.add(label(this, tx + col.x, top + 26, col.k, 13, THEME.muted, { fontStyle: 'bold' }).setOrigin(0.5)));
    table.forEach((s, i) => {
      const y = top + 46 + i * rowH + rowH / 2;
      const mine = s.team === t.user;
      if (mine) {
        const hg = this.add.graphics().fillStyle(THEME.cyan, 0.14).fillRoundedRect(tx + 8, y - rowH / 2 + 3, tw - 16, rowH - 6, 8);
        c.add(hg);
      }
      if (i === 0 && t.champion) c.add(label(this, tx + 22, y, '🏆', 16, '#ffffff').setOrigin(0.5));
      else c.add(label(this, tx + 22, y, String(i + 1), 16, i === 0 ? '#ffd23f' : '#ffffff', { fontStyle: 'bold' }).setOrigin(0.5));
      if (this.textures.exists(texKey.emblem(s.team))) c.add(this.add.image(tx + 52, y, texKey.emblem(s.team)).setDisplaySize(30, 30));
      c.add(fitWidth(label(this, tx + 74, y, teamName(s.team), PORTRAIT ? 13 : 15, mine ? THEME.cyanCss : '#ffffff', { fontStyle: 'bold' }).setOrigin(0, 0.5), cols[0].x - 90, 9));
      const vals: Record<string, string> = { PJ: `${s.played}`, G: `${s.won}`, E: `${s.drawn}`, P: `${s.lost}`, GF: `${s.gf}`, GC: `${s.ga}`, DG: `${s.gf - s.ga > 0 ? '+' : ''}${s.gf - s.ga}`, Pts: `${s.points}` };
      cols.forEach((col) => c.add(label(this, tx + col.x, y, vals[col.k], col.k === 'Pts' ? 17 : 14, col.k === 'Pts' ? '#ffd23f' : '#dce6f5', { fontStyle: col.k === 'Pts' ? 'bold' : 'normal' }).setOrigin(0.5)));
    });
    // partidos de la jornada (la actual o, al acabar, la última)
    const r = Math.min(t.round, t.rounds.length - 1);
    const fx = PORTRAIT ? 16 : tx + tw + 30;
    const fy = PORTRAIT ? top + 46 + rowH * table.length + 30 : top;
    const fw = PORTRAIT ? GAME_W - 32 : GAME_W - fx - 40;
    c.add(label(this, fx + 4, fy + 12, roundName(t, r), 16, '#ffd23f', { fontStyle: 'bold italic' }).setOrigin(0, 0.5));
    t.rounds[r].forEach((m, i) => {
      const live = !t.champion && (m.home === t.user || m.away === t.user);
      this.matchBox(c, m, fx, fy + 30 + i * (PORTRAIT ? 70 : 74), fw, t.user, live);
    });
    // la jornada anterior, con sus resultados
    if (!PORTRAIT && r > 0 && !t.champion) {
      const py = fy + 30 + t.rounds[r].length * 74 + 20;
      c.add(label(this, fx + 4, py, `${roundName(t, r - 1)}: resultados`, 13, THEME.muted, { fontStyle: 'bold italic' }).setOrigin(0, 0.5));
      t.rounds[r - 1].forEach((m, i) => {
        c.add(fitWidth(label(this, fx + 4, py + 22 + i * 20, `${teamName(m.home)} ${m.hg} - ${m.ag} ${teamName(m.away)}`, 12, '#c9d6ec').setOrigin(0, 0.5), fw - 8, 9));
      });
    }
  }

  /** Botones de abajo: jugar el siguiente partido, ver el final si te eliminan, cobrar el premio o empezar otro. */
  private drawActions(c: Phaser.GameObjects.Container, t: Tourney): void {
    const by = GAME_H - (PORTRAIT ? 56 : 46);
    const bh = PORTRAIT ? 64 : 52;
    const abandon = () =>
      confirmDialog(this, {
        title: '¿Abandonar el torneo?',
        body: 'Se pierde el torneo en curso (sin premio).',
        ok: 'Abandonar',
        danger: true,
        onOk: () => {
          saveTourney(null);
          this.tourney = null;
          this.showKind();
        },
      });
    if (t.champion) {
      this.payOnce(t);
      const place = userPlace(t);
      const msg = place === 1 ? '¡Campeones!' : place === 2 ? (t.kind === 'cup' ? 'Subcampeones' : '2.º puesto') : t.kind === 'cup' ? 'Eliminados' : `${place}.º puesto`;
      c.add(label(this, GAME_W / 2, by - bh / 2 - 20, `${msg}  ·  +${tourneyCoins(t)} monedas para Mi club`, PORTRAIT ? 15 : 16, place === 1 ? '#ffd23f' : '#ffffff', { fontStyle: 'bold' }).setOrigin(0.5));
      c.add(
        new Button(this, GAME_W / 2, by, 'Nuevo torneo', () => {
          saveTourney(null);
          this.tourney = null;
          this.showKind();
        }, { variant: 'primary', w: PORTRAIT ? GAME_W - 40 : 300, h: bh, size: 22 }),
      );
      return;
    }
    if (t.out) {
      c.add(label(this, GAME_W / 2, by - bh / 2 - 20, 'Tu equipo ha caído. El torneo sigue sin ti.', PORTRAIT ? 15 : 16, THEME.coralCss, { fontStyle: 'bold italic' }).setOrigin(0.5));
      c.add(
        new Button(this, GAME_W / 2, by, 'Ver cómo acaba', () => {
          this.tourney = finishWithoutUser(t, rating, Math.random);
          saveTourney(this.tourney);
          this.showTourney();
        }, { variant: 'primary', w: PORTRAIT ? GAME_W - 40 : 300, h: bh, size: 22 }),
      );
      return;
    }
    const m = userMatch(t);
    if (!m) return;
    const rival = m.home === t.user ? m.away : m.home;
    const pw = PORTRAIT ? GAME_W - 40 - 130 : 340;
    c.add(new Button(this, PORTRAIT ? 20 + 60 : GAME_W / 2 - pw / 2 - 100, by, 'Abandonar', abandon, { variant: 'ghost', w: PORTRAIT ? 120 : 160, h: bh, size: 15 }));
    c.add(
      new Button(this, PORTRAIT ? GAME_W - 20 - pw / 2 : GAME_W / 2 + 90, by, `Jugar contra ${teamName(rival)}`, () => void this.play(), {
        variant: 'primary',
        w: pw,
        h: bh,
        size: PORTRAIT ? 17 : 19,
        hint: PORTRAIT ? undefined : '⏎',
      }),
    );
    this.input.keyboard?.removeAllListeners('keydown-ENTER');
    this.input.keyboard?.on('keydown-ENTER', () => !this.busy && this.tourney && userMatch(this.tourney) && void this.play());
  }

  private payOnce(t: Tourney): void {
    if (t.paid) return;
    const coins = tourneyCoins(t);
    const save = loadClub();
    if (save) saveClub({ ...save, coins: save.coins + coins });
    t.paid = true;
    saveTourney(t);
    if (userPlace(t) === 1) {
      sfx.win();
      this.celebrate(t);
    }
  }

  private celebrate(t: Tourney): void {
    const c = this.add.container(0, 0).setDepth(800);
    c.add(this.add.rectangle(0, 0, GAME_W, GAME_H, 0x000000, 0.75).setOrigin(0).setInteractive());
    const g = this.add.graphics();
    glow(g, GAME_W / 2, GAME_H / 2 - 40, 300, THEME.yellow, 0.25);
    c.add(g);
    if (this.textures.exists(texKey.emblem(t.user))) c.add(this.add.image(GAME_W / 2, GAME_H / 2 - 170, texKey.emblem(t.user)).setDisplaySize(120, 120));
    c.add(fitWidth(display(this, GAME_W / 2, GAME_H / 2 - 60, t.kind === 'cup' ? '¡CAMPEONES DE LA COPA!' : '¡CAMPEONES DE LIGA!', PORTRAIT ? 44 : 60, '#ffd23f').setOrigin(0.5), GAME_W - 40, 24));
    c.add(label(this, GAME_W / 2, GAME_H / 2 + 6, teamName(t.user), 22, '#ffffff', { fontStyle: 'bold italic' }).setOrigin(0.5));
    c.add(label(this, GAME_W / 2, GAME_H / 2 + 50, `+${TOURNEY_COINS.champion} monedas para Mi club`, 18, '#0b1a2e', { backgroundColor: '#ffd23f', padding: { x: 12, y: 5 }, fontStyle: 'bold' }).setOrigin(0.5));
    c.add(new Button(this, GAME_W / 2, GAME_H / 2 + 130, '¡Genial!', () => c.destroy(), { variant: 'primary', w: 220, h: 56, size: 22 }));
    c.setAlpha(0);
    this.tweens.add({ targets: c, alpha: 1, duration: 300 });
  }

  /** Aviso de cómo ha ido la ronda (tu resultado y, en copa, si pasas). */
  private afterRound(before: Tourney, res: TourneyMatchResult): void {
    const t = this.tourney!;
    const m = before.rounds[before.round].find((x) => x.home === t.user || x.away === t.user);
    const after = t.rounds[before.round].find((x) => x.home === t.user || x.away === t.user);
    if (!m || !after) return;
    const won = res.goalsFor > res.goalsAgainst || (!!after.pens && winnerOf(after) === t.user);
    const draw = res.goalsFor === res.goalsAgainst && !after.pens;
    let msg = res.quit ? 'Partido abandonado: cuenta como derrota 0-3' : `${res.goalsFor}-${res.goalsAgainst}`;
    if (!res.quit && after.pens) {
      const userHome = after.home === t.user;
      msg += `, penaltis ${userHome ? after.pens.home : after.pens.away}-${userHome ? after.pens.away : after.pens.home}`;
    }
    if (t.kind === 'cup') msg += won ? (t.champion ? ' · ¡Campeones!' : ' · ¡Pasáis de ronda!') : ' · Eliminados';
    else msg += won ? ' · ¡Victoria! +3' : draw ? ' · Empate +1' : ' · Derrota';
    // encima de los botones de abajo (el aviso normal los taparía)
    const color = won ? THEME.green : draw ? THEME.yellow : THEME.coral;
    const y = GAME_H - (PORTRAIT ? 56 : 46) - (PORTRAIT ? 64 : 52) / 2 - (t.champion || t.out ? 60 : 30);
    const tx = label(this, 0, 0, msg, PORTRAIT ? 16 : 16, inkOn(color), { fontStyle: 'bold', align: 'center', wordWrap: { width: GAME_W - 80 } }).setOrigin(0.5);
    const w = tx.width + 36;
    const h = Math.max(34, tx.height + 14);
    const banner = this.add.container(GAME_W / 2, y).setDepth(600).setAlpha(0);
    banner.add([this.add.graphics().fillStyle(color).fillRoundedRect(-w / 2, -h / 2, w, h, h / 2), tx]);
    this.tweens.add({ targets: banner, alpha: 1, y: y - 8, duration: 200 });
    this.time.delayedCall(3600, () => this.tweens.add({ targets: banner, alpha: 0, duration: 300, onComplete: () => banner.destroy() }));
  }

  private async play(): Promise<void> {
    const t = this.tourney;
    const m = t && userMatch(t);
    if (!t || !m || this.busy) return;
    this.busy = true;
    sfx.click();
    const home = getTeam(t.user);
    const away = getTeam(m.home === t.user ? m.away : m.home);
    const wait = label(this, GAME_W / 2, GAME_H / 2, 'Cargando jugadores…', 18, '#ffffff', { backgroundColor: '#0b1a2ecc', padding: { x: 10, y: 4 } }).setOrigin(0.5).setDepth(900);
    await ensureSprites(this.textures, [home, away]).catch(() => {});
    wait.destroy();
    this.registry.remove('storyMatch');
    this.registry.set(TOURNEY_REGISTRY, true);
    this.scene.start('formation', { home: defaultLineup(home), away: defaultLineup(away) });
  }
}
