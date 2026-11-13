import Phaser from 'phaser';
import { music } from '../audio/music';
import { THEME, cardPanel, chip, coinChip, dim, fitCamera, glow, inkOn, pt, starRow, topBar } from '../ui/theme';
import { soundButton, soundPanel } from '../ui/soundPanel';
import { FONT, GAME_H, GAME_W, PORTRAIT, hex } from '../config';
import { TEAMS } from '../data';
import { getFormation } from '../data/formations';
import { SEASONS, getSeason, seasonOf } from '../data/seasons';
import type { TeamData } from '../data/types';
import { defaultLineup } from '../engine/lineup';
import { lineRatings, playerOverall, ratingStars, teamRating } from '../engine/rating';
import { Button, display, fitWidth, label, meter, text } from '../ui/widgets';
import { loadClub } from '../club/club';
import { makeEmblem, texKey } from '../gfx/placeholders';
import { ensureSprites } from '../gfx/pack';

type Side = 'home' | 'away';

interface Selection {
  home: string;
  away: string;
  /** Lado que se está eligiendo desde la estantería de escudos. */
  focus: Side;
}

// Pantalla de "versus": una tarjeta por equipo, el VS en medio y abajo la estantería de escudos.
const CARD = { y: 80, w: 520, h: 332 };
const CARD_X: Record<Side, number> = { home: 28, away: GAME_W - 28 - CARD.w };
const CTA_Y = 450;
const SHELF = { x: 20, y: 488, w: GAME_W - 40, h: GAME_H - 488 - 8 };
const SIDE = {
  home: { label: 'TÚ', color: THEME.home, css: THEME.homeCss },
  away: { label: 'RIVAL', color: THEME.away, css: THEME.awayCss },
} as const;

const seasonsWithTeams = () => SEASONS.filter((s) => TEAMS.some((t) => seasonOf(t) === s.id));
const teamsOf = (season: string) => TEAMS.filter((t) => seasonOf(t) === season).sort((a, b) => a.name.localeCompare(b.name, 'es'));
const teamById = (id: string) => TEAMS.find((t) => t.id === id)!;

export class MenuScene extends Phaser.Scene {
  private sel!: Selection;
  private shelfSeason!: string;
  private bg!: Phaser.GameObjects.Graphics;
  private sides!: Record<Side, Phaser.GameObjects.Container>;
  private shelf!: Phaser.GameObjects.Container;
  private ctaRow!: Phaser.GameObjects.Container;
  /** Móvil: página de la cuadrícula de escudos. */
  private page = 0;

  constructor() {
    super('menu');
  }

  create(): void {
    this.starting = false;
    fitCamera(this);
    music.play('menu');
    const club = TEAMS.find((t) => t.id === 'club');
    if (club) makeEmblem(this, club);
    const saved = this.registry.get('menuSelection') as Selection | undefined;
    this.sel = saved && TEAMS.some((t) => t.id === saved.home) && TEAMS.some((t) => t.id === saved.away) && saved.home !== saved.away ? { ...saved } : this.defaults();
    this.shelfSeason = seasonOf(teamById(this.sel[this.sel.focus]));
    this.page = this.pageOf(this.sel[this.sel.focus]);

    if (PORTRAIT) {
      this.createPortrait();
      return;
    }
    this.bg = this.add.graphics();
    this.drawBackground();
    this.sides = { home: this.add.container(0, 0), away: this.add.container(0, 0) };
    this.ctaRow = this.add.container(0, 0);
    this.shelf = this.add.container(0, 0);
    this.drawCenter();
    this.renderSide('home');
    this.renderSide('away');
    this.renderCta();
    this.renderShelf();
    this.bindKeys();
    this.drawTopBar();
  }

  private defaults(): Selection {
    const home = TEAMS.find((t) => t.id === 'ie3-inazuma-japan') ?? TEAMS[0];
    const away = TEAMS.find((t) => t.id === 'ie3-desert-lion') ?? TEAMS.find((t) => t !== home) ?? home;
    return { home: home.id, away: away.id, focus: 'away' };
  }

  // ----------------------------------------------------------------- fondo

  private drawBackground(): void {
    const g = this.bg.clear();
    const home = teamById(this.sel.home);
    const away = teamById(this.sel.away);
    g.fillGradientStyle(THEME.deep, THEME.deep, THEME.night, THEME.night, 1, 1, 1, 1).fillRect(0, 0, GAME_W, GAME_H);
    // cada mitad con un foco del color de su equipo, partidas en diagonal
    g.fillStyle(dim(home.colors.shirt, 0.8)).fillPoints([pt(0, 0), pt(700, 0), pt(580, SHELF.y), pt(0, SHELF.y)], true);
    g.fillStyle(dim(away.colors.shirt, 0.8)).fillPoints([pt(700, 0), pt(GAME_W, 0), pt(GAME_W, SHELF.y), pt(580, SHELF.y)], true);
    glow(g, 200, 120, 520, hex(home.colors.accent), 0.16);
    glow(g, GAME_W - 200, 120, 520, hex(away.colors.accent), 0.16);
    g.fillStyle(0xffffff, 0.025);
    for (let i = 0; i < 6; i++) {
      const bx = 60 + i * 220;
      g.fillPoints([pt(bx - 20, 0), pt(bx + 20, 0), pt(bx + 200, SHELF.y), pt(bx + 90, SHELF.y)], true);
    }
    g.lineStyle(1, 0xffffff, 0.025);
    for (let gx = 0; gx <= GAME_W; gx += 40) g.lineBetween(gx, 0, gx, SHELF.y);
    for (let gy = 0; gy <= SHELF.y; gy += 40) g.lineBetween(0, gy, GAME_W, gy);
    g.lineStyle(2, THEME.yellow, 0.5).lineBetween(700, 0, 580, SHELF.y);
    g.fillGradientStyle(0x000000, 0x000000, 0x000000, 0x000000, 0, 0, 0.45, 0.45).fillRect(0, SHELF.y - 120, GAME_W, 120);
  }

  private drawTopBar(): void {
    topBar(this, { title: 'InaMatch', subtitle: 'Elige los equipos y ¡a jugar!', back: { label: 'Inicio', onClick: () => this.scene.start('title') } });
    const save = loadClub();
    soundButton(this, GAME_W - 30, 32, GAME_W - 350, 76);
    if (!save) return;
    coinChip(this, GAME_W - 64, 32, save.coins).setDepth(101);
    new Button(this, GAME_W - 222, 32, 'Fichajes', () => this.scene.start('gacha', { from: 'menu' }), { w: 120, h: 38, variant: 'secondary', size: 15 }).setDepth(101);
    new Button(this, GAME_W - 366, 32, 'Mi club', () => this.scene.start('club'), { w: 140, h: 38, color: THEME.orange, size: 15, icon: '⚡' }).setDepth(101);
  }

  // ------------------------------------------------------------------ lados

  private renderSide(side: Side): void {
    const c = this.sides[side];
    this.tweens.killTweensOf(c.list);
    c.removeAll(true);
    const team = teamById(this.sel[side]);
    const s = SIDE[side];
    const choosing = this.sel.focus === side;
    const x0 = CARD_X[side];
    const y0 = CARD.y;
    const accent = hex(team.colors.accent);

    const g = this.add.graphics();
    cardPanel(g, x0, y0, CARD.w, CARD.h, { accent: s.color, fill: dim(team.colors.shirt, 0.78), alpha: 0.96, radius: 18 });
    if (choosing) g.lineStyle(2, THEME.cyan, 0.9).strokeRoundedRect(x0, y0, CARD.w, CARD.h, 18);
    // destello detrás del escudo
    const ex = x0 + 118;
    const ey = y0 + 168;
    glow(g, ex, ey, 110, accent, 0.5, 8);
    g.fillStyle(0x000000, 0.3).fillCircle(ex, ey, 88);
    g.lineStyle(choosing ? 3 : 2, choosing ? THEME.cyan : 0xffffff, choosing ? 0.9 : 0.25).strokeCircle(ex, ey, 88);
    c.add(g);
    const rays = this.add.graphics({ x: ex, y: ey });
    for (let i = 0; i < 12; i++) {
      const a = (i / 12) * Math.PI * 2;
      rays.fillStyle(0xffffff, 0.05).fillTriangle(0, 0, Math.cos(a - 0.1) * 86, Math.sin(a - 0.1) * 86, Math.cos(a + 0.1) * 86, Math.sin(a + 0.1) * 86);
    }
    this.tweens.add({ targets: rays, angle: side === 'home' ? 360 : -360, duration: 50000, repeat: -1 });
    c.add(rays);
    c.add(this.add.image(ex, ey, texKey.emblem(team.id)).setDisplaySize(136, 136));

    // etiqueta TÚ / RIVAL y la pista de qué lado se elige
    c.add(chip(this, x0 + 18, y0 + 24, s.label, s.color, { size: 12, h: 24, padX: 12, textColor: '#ffffff' }));
    if (choosing) c.add(label(this, x0 + (side === 'home' ? 86 : 104), y0 + 24, 'eligiendo en la estantería ▾', 11, THEME.cyanCss, { fontStyle: 'italic' }).setOrigin(0, 0.5));

    // flechas a los lados del escudo
    for (const dir of [-1, 1]) {
      const ax = ex + dir * 106;
      const arrow = this.add.graphics();
      const draw = (hover: boolean) => {
        arrow.clear().fillStyle(hover ? THEME.yellow : 0xffffff, hover ? 1 : 0.7);
        arrow.fillPoints([pt(ax + dir * 9, ey), pt(ax - dir * 7, ey - 14), pt(ax - dir * 7, ey + 14)], true);
      };
      draw(false);
      const zone = this.add.zone(ax - 16, ey - 26, 32, 52).setOrigin(0).setInteractive({ useHandCursor: true });
      zone.on('pointerover', () => draw(true)).on('pointerout', () => draw(false));
      zone.on('pointerdown', () => this.cycle(side, dir));
      c.add([arrow, zone]);
    }

    // nombre, temporada y posición en la lista
    const tx = x0 + 236;
    const name = display(this, tx, y0 + 50, team.name, 36, '#ffffff').setOrigin(0, 0.5);
    fitWidth(name, CARD.w - 252, 18);
    c.add(name);
    const list = teamsOf(seasonOf(team));
    const season = getSeason(seasonOf(team));
    const icon = season.icon && this.textures.exists(`series:${season.icon}`) ? `series:${season.icon}` : undefined;
    const sc = chip(this, tx, y0 + 86, `${season.name}  ·  ${list.indexOf(team) + 1}/${list.length}`, THEME.panelLight, { size: 11, h: 22, textColor: THEME.text, icon });
    c.add(sc);

    // media grande con estrellas
    const rating = teamRating(team);
    c.add(display(this, tx, y0 + 132, String(rating), 58, THEME.yellowCss, { strokeThickness: 0, shadow: { offsetX: 0, offsetY: 3, color: '#000', blur: 0, fill: true } }).setOrigin(0, 0.5));
    c.add(label(this, tx + 2, y0 + 165, 'MEDIA', 10, THEME.muted, { fontStyle: 'bold' }));
    c.add(starRow(this, tx + 82, y0 + 124, ratingStars(rating), 9));
    const f = getFormation(team.formation);
    const layout = ['DF', 'MF', 'FW'].map((pos) => f.slots.filter((sl) => sl.pos === pos).length).join('-');
    c.add(label(this, tx + 84, y0 + 146, `${f.name}  ·  ${layout}`, 12, THEME.text, { fontStyle: 'italic' }).setOrigin(0, 0.5));

    // líneas
    const lines = lineRatings(team);
    const rows = [
      ['Ataque', lines.att, THEME.orange],
      ['Medio', lines.mid, THEME.green],
      ['Defensa', lines.def, 0x4fa3ff],
    ] as const;
    rows.forEach(([cap, value, color], i) => c.add(meter(this, tx + 70, y0 + 198 + i * 24, 160, value - 30, 60, color, cap, String(value))));

    // la estrella del equipo
    const best = [...team.players.slice(0, 11)].sort((a, b) => playerOverall(b) - playerOverall(a))[0];
    if (best) {
      const by = y0 + CARD.h - 34;
      c.add(label(this, tx, by, 'ESTRELLA', 10, THEME.muted, { fontStyle: 'bold' }).setOrigin(0, 0.5));
      c.add(label(this, tx + 62, by, `${best.name}  ·  ${best.position}  ·  ${playerOverall(best)}`, 13, THEME.text, { fontStyle: 'italic bold' }).setOrigin(0, 0.5));
    }

    // pulsar en cualquier parte de la tarjeta la elige para la estantería
    const hit = this.add.zone(x0, y0, CARD.w, CARD.h).setOrigin(0).setInteractive({ useHandCursor: !choosing });
    hit.on('pointerdown', () => this.setFocus(side));
    hit.on('wheel', (_p: Phaser.Input.Pointer, _dx: number, dy: number) => this.cycle(side, dy > 0 ? 1 : -1));
    c.add(hit);
    c.sendToBack(hit);
  }

  // ----------------------------------------------------------------- centro

  private drawCenter(): void {
    const vs = display(this, 640, 200, 'VS', 96, THEME.yellowCss, { strokeThickness: 10 }).setOrigin(0.5);
    this.tweens.add({ targets: vs, scale: 1.05, duration: 800, yoyo: true, repeat: -1, ease: 'Sine.inOut' });

    const round = (x: number, y: number, icon: string, hint: string, onClick: () => void) => {
      const g = this.add.graphics();
      const draw = (hover: boolean) => {
        g.clear().fillStyle(hover ? THEME.yellow : THEME.panel, 0.95).fillCircle(x, y, 24);
        g.lineStyle(2, hover ? THEME.yellow : 0xffffff, hover ? 1 : 0.3).strokeCircle(x, y, 24);
      };
      draw(false);
      const lbl = text(this, x, y, icon, 20, '#ffffff', { strokeThickness: 0 }).setOrigin(0.5);
      const tip = label(this, x, y + 38, hint, 12, THEME.text, { fontStyle: 'italic bold' }).setOrigin(0.5).setAlpha(0);
      this.add
        .zone(x - 26, y - 26, 52, 52)
        .setOrigin(0)
        .setInteractive({ useHandCursor: true })
        .on('pointerover', () => (draw(true), lbl.setColor(THEME.ink), tip.setAlpha(1)))
        .on('pointerout', () => (draw(false), lbl.setColor('#ffffff'), tip.setAlpha(0)))
        .on('pointerdown', onClick);
    };
    round(606, 290, '⇄', 'Cambiar lados', () => this.swap());
    round(674, 290, '⚄', 'Rival al azar', () => this.randomRival());
  }

  /** Fila entre las tarjetas y la estantería: el botón de seguir, las teclas y para qué lado se elige. */
  private renderCta(): void {
    const c = this.ctaRow;
    c.removeAll(true);
    c.add(new Button(this, 640, CTA_Y, '¡A la formación!', () => this.next(), { w: 300, h: 54, variant: 'primary', size: 22, hint: '⏎' }));
    c.add(label(this, 28, CTA_Y, '← →  equipo     ↑ ↓  temporada     Tab  lado     Rueda del ratón sobre una tarjeta', 11, THEME.muted).setOrigin(0, 0.5));
    // para qué lado se elige en la estantería
    const sx = GAME_W - 28;
    const g = this.add.graphics();
    const segW = 78;
    const x0 = sx - segW * 2 - 2;
    g.fillStyle(THEME.panel, 0.95).fillRoundedRect(x0 - 2, CTA_Y - 16, segW * 2 + 4, 32, 16);
    (['home', 'away'] as const).forEach((side, i) => {
      const on = this.sel.focus === side;
      const x = x0 + i * segW;
      if (on) g.fillStyle(SIDE[side].color).fillRoundedRect(x, CTA_Y - 14, segW, 28, 14);
      const t = label(this, x + segW / 2, CTA_Y, SIDE[side].label, 12, on ? '#ffffff' : THEME.muted, { fontStyle: 'bold' }).setOrigin(0.5);
      const z = this.add.zone(x, CTA_Y - 16, segW, 32).setOrigin(0).setInteractive({ useHandCursor: true });
      z.on('pointerdown', () => this.setFocus(side));
      c.add([t, z]);
    });
    c.add(label(this, x0 - 12, CTA_Y, 'eligiendo para', 12, THEME.muted, { fontStyle: 'italic' }).setOrigin(1, 0.5));
    c.add(g);
    c.sendToBack(g);
  }

  // ------------------------------------------------------------- estantería

  /**
   * Abajo: pestañas con el logo de cada juego de la saga (los de la enciclopedia oficial) y, debajo, todos los
   * escudos del juego elegido, en hasta tres filas, para elegir de un vistazo.
   */
  private renderShelf(): void {
    const c = this.shelf;
    this.tweens.killTweensOf(c.list);
    c.removeAll(true);
    const g = this.add.graphics();
    cardPanel(g, SHELF.x, SHELF.y, SHELF.w, SHELF.h, { plain: true, alpha: 0.9, radius: 16 });
    c.add(g);

    // pestañas de los juegos
    const seasons = seasonsWithTeams();
    const tabW = 96;
    const tabH = 36;
    const ty = SHELF.y + 30;
    let tx = SHELF.x + 16;
    const tip = text(this, 0, 0, '', 13, '#ffffff', { fontStyle: 'italic bold', strokeThickness: 5 }).setOrigin(0.5).setVisible(false);
    seasons.forEach((s) => {
      const on = s.id === this.shelfSeason;
      const x = tx;
      const tab = this.add.graphics();
      const color = on ? THEME.yellow : s.id === 'club' ? THEME.orange : THEME.panelLight;
      const draw = (hover: boolean) => {
        tab.clear().fillStyle(color, 1).fillRoundedRect(x, ty - tabH / 2, tabW - 6, tabH, 10);
        if (hover && !on) tab.lineStyle(1, 0xffffff, 0.6).strokeRoundedRect(x, ty - tabH / 2, tabW - 6, tabH, 10);
        else if (!on) tab.lineStyle(1, 0xffffff, 0.1).strokeRoundedRect(x, ty - tabH / 2, tabW - 6, tabH, 10);
      };
      draw(false);
      c.add(tab);
      let lx = x + 12;
      if (s.icon && this.textures.exists(`series:${s.icon}`)) {
        const icon = this.add.image(x + 22, ty, `series:${s.icon}`).setDisplaySize(24, 26);
        if (on) icon.setTint(0x0b1a2e);
        c.add(icon);
        lx = x + 40;
      } else if (s.id === 'club') {
        c.add(this.add.image(x + 22, ty, texKey.emblem('club')).setDisplaySize(24, 24));
        lx = x + 40;
      }
      c.add(label(this, lx, ty, s.short, 13, inkOn(color), { fontStyle: 'bold' }).setOrigin(0, 0.5));
      const zone = this.add.zone(x, ty - tabH / 2, tabW - 6, tabH).setOrigin(0).setInteractive({ useHandCursor: true });
      zone.on('pointerover', () => {
        draw(true);
        tip.setText(`${s.name} · ${teamsOf(s.id).length} equipos`).setPosition(Phaser.Math.Clamp(x + 45, 120, GAME_W - 140), ty - 30).setVisible(true);
        c.bringToTop(tip);
      });
      zone.on('pointerout', () => (draw(false), tip.setVisible(false)));
      zone.on('pointerdown', () => {
        this.shelfSeason = s.id;
        this.renderShelf();
      });
      c.add(zone);
      tx += tabW;
    });
    const season = getSeason(this.shelfSeason);
    const teams = teamsOf(this.shelfSeason);
    const who = SIDE[this.sel.focus];
    c.add(label(this, SHELF.x + SHELF.w - 18, ty - 8, season.name, 15, THEME.text, { fontStyle: 'italic bold' }).setOrigin(1, 0.5));
    c.add(label(this, SHELF.x + SHELF.w - 18, ty + 10, `${teams.length} ${teams.length === 1 ? 'equipo' : 'equipos'}  ·  pulsa uno para ponerlo como `, 11, THEME.muted).setOrigin(1, 0.5));
    const whoT = label(this, SHELF.x + SHELF.w - 18, ty + 10, who.label, 11, who.css, { fontStyle: 'bold' }).setOrigin(1, 0.5);
    c.add(whoT);
    (c.list[c.list.length - 2] as Phaser.GameObjects.Text).setX(SHELF.x + SHELF.w - 18 - whoT.width - 2);

    // escudos del juego: hasta tres filas, centradas
    const rows = teams.length > 30 ? 3 : teams.length > 15 ? 2 : 1;
    const perRow = Math.ceil(teams.length / rows);
    const size = rows === 3 ? 42 : rows === 2 ? 52 : 60;
    const stepX = Math.min(size + 26, (SHELF.w - 40) / perRow);
    const area = { top: SHELF.y + 56, bottom: SHELF.y + SHELF.h - 6 };
    const stepY = (area.bottom - area.top) / rows;
    teams.forEach((team, i) => {
      const row = Math.floor(i / perRow);
      const inRow = row === rows - 1 ? teams.length - perRow * row : perRow;
      const x = GAME_W / 2 - ((inRow - 1) * stepX) / 2 + (i - perRow * row) * stepX;
      const y = area.top + stepY * (row + 0.5);
      const ring = this.add.graphics();
      const mark = team.id === this.sel.home ? SIDE.home : team.id === this.sel.away ? SIDE.away : null;
      const r = size / 2 + 5;
      if (mark) {
        ring.fillStyle(mark.color, 0.3).fillCircle(x, y, r).lineStyle(2.5, mark.color).strokeCircle(x, y, r);
        const tag = chip(this, x, y + r - 6, mark.label, mark.color, { size: 8, h: 13, padX: 5, textColor: '#ffffff' });
        tag.setX(x - tag.width / 2);
        c.add(tag);
      }
      const img = this.add.image(x, y, texKey.emblem(team.id)).setDisplaySize(size, size);
      img.setInteractive({ useHandCursor: true });
      img.on('pointerover', () => {
        c.bringToTop(img);
        this.tweens.add({ targets: img, displayWidth: size + 14, displayHeight: size + 14, duration: 100 });
        tip.setText(`${team.name}  ·  ${teamRating(team)}`).setPosition(Phaser.Math.Clamp(x, 120, GAME_W - 120), y - size / 2 - 16).setVisible(true);
        c.bringToTop(tip);
      });
      img.on('pointerout', () => {
        this.tweens.add({ targets: img, displayWidth: size, displayHeight: size, duration: 100 });
        tip.setVisible(false);
      });
      img.on('pointerdown', () => this.choose(team));
      c.add([ring, img]);
      c.bringToTop(ring);
      c.bringToTop(img);
    });
    c.add(tip);
  }

  // --------------------------------------------------------------- acciones

  private bindKeys(): void {
    const kb = this.input.keyboard;
    if (!kb) return;
    kb.on('keydown-LEFT', () => this.cycle(this.sel.focus, -1));
    kb.on('keydown-RIGHT', () => this.cycle(this.sel.focus, 1));
    kb.on('keydown-UP', () => this.stepSeason(-1));
    kb.on('keydown-DOWN', () => this.stepSeason(1));
    kb.on('keydown-TAB', (e: KeyboardEvent) => {
      e.preventDefault();
      this.setFocus(this.sel.focus === 'home' ? 'away' : 'home');
    });
    kb.on('keydown-ENTER', () => this.next());
    kb.on('keydown-R', () => this.randomRival());
  }

  private refresh(): void {
    if (PORTRAIT) {
      this.refreshPortrait();
      return;
    }
    this.drawBackground();
    this.renderSide('home');
    this.renderSide('away');
    this.renderCta();
    this.renderShelf();
  }

  private setFocus(side: Side): void {
    if (this.sel.focus === side) return;
    this.sel.focus = side;
    this.shelfSeason = seasonOf(teamById(this.sel[side]));
    this.page = this.pageOf(this.sel[side]);
    this.refresh();
  }

  private other(side: Side): Side {
    return side === 'home' ? 'away' : 'home';
  }

  /** Pone el equipo en el lado activo; si ya estaba en el otro lado, los intercambia (nunca los dos iguales). */
  private choose(team: TeamData): void {
    const side = this.sel.focus;
    if (this.sel[this.other(side)] === team.id) this.sel[this.other(side)] = this.sel[side];
    this.sel[side] = team.id;
    this.refresh();
  }

  private cycle(side: Side, dir: number): void {
    const team = teamById(this.sel[side]);
    const list = teamsOf(seasonOf(team));
    let i = list.indexOf(team);
    let next = team;
    for (let n = 0; n < list.length; n++) {
      i = (i + dir + list.length) % list.length;
      next = list[i];
      if (next.id !== this.sel[this.other(side)]) break;
    }
    this.sel[side] = next.id;
    this.sel.focus = side;
    this.shelfSeason = seasonOf(team);
    this.page = this.pageOf(next.id);
    this.refresh();
  }

  /** Arriba/abajo: cambia la temporada de la estantería y elige su primer equipo para el lado activo. */
  private stepSeason(dir: number): void {
    const seasons = seasonsWithTeams();
    const i = seasons.findIndex((s) => s.id === this.shelfSeason);
    this.shelfSeason = seasons[(i + dir + seasons.length) % seasons.length].id;
    const list = teamsOf(this.shelfSeason).filter((t) => t.id !== this.sel[this.other(this.sel.focus)]);
    if (list.length) this.sel[this.sel.focus] = list[0].id;
    this.page = 0;
    this.refresh();
  }

  private swap(): void {
    [this.sel.home, this.sel.away] = [this.sel.away, this.sel.home];
    this.refresh();
  }

  private randomRival(): void {
    const pool = TEAMS.filter((t) => t.id !== this.sel.home && t.id !== this.sel.away);
    const pick: TeamData | undefined = pool[Math.floor(Math.random() * pool.length)];
    if (!pick) return;
    this.sel.away = pick.id;
    this.sel.focus = 'away';
    this.shelfSeason = seasonOf(pick);
    this.page = this.pageOf(pick.id);
    this.refresh();
  }

  private starting = false;

  private next(): void {
    if (this.starting) return;
    this.starting = true;
    this.registry.set('menuSelection', { ...this.sel });
    const home = teamById(this.sel.home);
    const away = teamById(this.sel.away);
    // los sprites dibujados de los dos equipos se piden ahora (no se cargan al arrancar)
    const wait = this.add
      .text(GAME_W / 2, PORTRAIT ? GAME_H - 96 : GAME_H - 30, 'Cargando jugadores…', { fontFamily: FONT, fontSize: PORTRAIT ? '18px' : '15px', color: '#ffffff', backgroundColor: '#0b1a2ecc', padding: { x: 10, y: 4 } })
      .setOrigin(0.5)
      .setDepth(700);
    ensureSprites(this.textures, [home, away])
      .catch((err) => console.warn('[pack] no se pudieron cargar los sprites dibujados', err))
      .then(() => {
        wait.destroy();
        // partido normal: que no vuelva a la historia ni al torneo
        for (const k of ['storyMatch', 'tourneyMatch']) this.registry.remove(k);
        this.scene.start('formation', { home: defaultLineup(home), away: defaultLineup(away) });
      });
  }

  // =================================================================== móvil (vertical, 540x960)
  //
  // Arriba la barra (InaMatch, monedas, sonido) y los botones de Mi club y Fichajes; luego las dos tarjetas TÚ y
  // RIVAL lado a lado con el VS en medio; debajo, la estantería: una pestaña por juego (solo el logo) y una
  // cuadrícula de escudos por páginas (flechas o deslizar); y abajo del todo, el botón grande de jugar.

  private pageOf(teamId: string): number {
    const list = teamsOf(this.shelfSeason);
    const i = list.findIndex((t) => t.id === teamId);
    return i < 0 ? 0 : Math.floor(i / P_GRID.per);
  }

  private createPortrait(): void {
    this.bg = this.add.graphics();
    this.sides = { home: this.add.container(0, 0), away: this.add.container(0, 0) };
    this.ctaRow = this.add.container(0, 0);
    this.shelf = this.add.container(0, 0);
    this.drawBackgroundP();
    this.renderSideP('home');
    this.renderSideP('away');
    const vsG = this.add.graphics().setDepth(5);
    vsG.fillStyle(THEME.night, 0.95).fillCircle(GAME_W / 2, P_CARD.y + 100, 27).lineStyle(2, THEME.yellow, 0.9).strokeCircle(GAME_W / 2, P_CARD.y + 100, 27);
    const vs = display(this, GAME_W / 2, P_CARD.y + 102, 'VS', 32, THEME.yellowCss, { strokeThickness: 5 }).setOrigin(0.5).setDepth(5);
    this.tweens.add({ targets: vs, scale: 1.06, duration: 800, yoyo: true, repeat: -1, ease: 'Sine.inOut' });
    this.renderCtaP();
    this.renderShelfP();
    this.bindKeys();
    this.drawTopBarP();
    // deslizar sobre la cuadrícula cambia de página
    let down: { x: number; y: number } | null = null;
    this.input.on('pointerdown', (p: Phaser.Input.Pointer) => {
      const w = this.cameras.main.getWorldPoint(p.x, p.y);
      down = w.y > P_GRID.top - 10 && w.y < P_GRID.top + P_GRID.rows * P_GRID.cellH + 10 ? { x: w.x, y: w.y } : null;
      this.swipeStart = { x: w.x, y: w.y };
    });
    this.input.on('pointerup', (p: Phaser.Input.Pointer) => {
      if (!down) return;
      const w = this.cameras.main.getWorldPoint(p.x, p.y);
      const dx = w.x - down.x;
      down = null;
      if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(w.y - this.swipeStart.y)) this.turnPage(dx < 0 ? 1 : -1);
    });
  }

  private swipeStart = { x: 0, y: 0 };

  private refreshPortrait(): void {
    this.drawBackgroundP();
    this.renderSideP('home');
    this.renderSideP('away');
    this.renderCtaP();
    this.renderShelfP();
  }

  private drawBackgroundP(): void {
    const g = this.bg.clear();
    const home = teamById(this.sel.home);
    const away = teamById(this.sel.away);
    g.fillGradientStyle(THEME.deep, THEME.deep, THEME.night, THEME.night, 1, 1, 1, 1).fillRect(0, 0, GAME_W, GAME_H);
    const bottom = P_CARD.y + P_CARD.h + 20;
    g.fillStyle(dim(home.colors.shirt, 0.8)).fillPoints([pt(0, 0), pt(300, 0), pt(240, bottom), pt(0, bottom)], true);
    g.fillStyle(dim(away.colors.shirt, 0.8)).fillPoints([pt(300, 0), pt(GAME_W, 0), pt(GAME_W, bottom), pt(240, bottom)], true);
    glow(g, 90, 160, 300, hex(home.colors.accent), 0.16);
    glow(g, GAME_W - 90, 160, 300, hex(away.colors.accent), 0.16);
    g.lineStyle(1, 0xffffff, 0.025);
    for (let gx = 0; gx <= GAME_W; gx += 40) g.lineBetween(gx, 0, gx, bottom);
    for (let gy = 0; gy <= bottom; gy += 40) g.lineBetween(0, gy, GAME_W, gy);
    g.lineStyle(2, THEME.yellow, 0.5).lineBetween(300, 0, 240, bottom);
    g.fillGradientStyle(0x000000, 0x000000, 0x000000, 0x000000, 0, 0, 0.5, 0.5).fillRect(0, bottom - 90, GAME_W, 90);
  }

  private drawTopBarP(): void {
    topBar(this, { title: 'InaMatch', subtitle: 'Elige los equipos y ¡a jugar!', back: { label: 'Inicio', onClick: () => this.scene.start('title') } });
    const save = loadClub();
    // botón de sonido propio, con área táctil grande (el panel se abre centrado)
    let panel: Phaser.GameObjects.Container | null = null;
    const sx = GAME_W - 34;
    const g = this.add.graphics().setDepth(199);
    g.fillStyle(THEME.night, 0.92).fillCircle(sx, 32, 22).lineStyle(2, THEME.yellow).strokeCircle(sx, 32, 22);
    text(this, sx, 32, '♪', 22, '#ffffff').setOrigin(0.5).setDepth(199);
    this.add
      .zone(sx - 30, 2, 60, 60)
      .setOrigin(0)
      .setDepth(199)
      .setInteractive({ useHandCursor: true })
      .on('pointerdown', () => {
        if (panel?.active) {
          panel.destroy();
          panel = null;
        } else panel = soundPanel(this, (GAME_W - 320) / 2, 120, () => (panel = null)).setDepth(300);
      });
    if (!save) return;
    coinChip(this, GAME_W - 66, 32, save.coins).setDepth(101);
    const bw = (GAME_W - 48) / 2;
    new Button(this, 16 + bw / 2, 104, 'Mi club', () => this.scene.start('club'), { w: bw, h: 56, color: THEME.orange, size: 20, icon: '⚡' }).setDepth(101);
    new Button(this, GAME_W - 16 - bw / 2, 104, 'Fichajes', () => this.scene.start('gacha', { from: 'menu' }), { w: bw, h: 56, variant: 'secondary', size: 20 }).setDepth(101);
  }

  private renderSideP(side: Side): void {
    const c = this.sides[side];
    this.tweens.killTweensOf(c.list);
    c.removeAll(true);
    const team = teamById(this.sel[side]);
    const s = SIDE[side];
    const choosing = this.sel.focus === side;
    const x0 = side === 'home' ? 12 : GAME_W - 12 - P_CARD.w;
    const y0 = P_CARD.y;
    const W = P_CARD.w;
    const cx = x0 + W / 2;
    const accent = hex(team.colors.accent);

    const g = this.add.graphics();
    cardPanel(g, x0, y0, W, P_CARD.h, { accent: s.color, fill: dim(team.colors.shirt, 0.78), alpha: 0.96, radius: 16 });
    if (choosing) g.lineStyle(3, THEME.cyan, 0.95).strokeRoundedRect(x0, y0, W, P_CARD.h, 16);
    const ey = y0 + 100;
    glow(g, cx, ey, 78, accent, 0.5, 8);
    g.fillStyle(0x000000, 0.3).fillCircle(cx, ey, 60);
    g.lineStyle(choosing ? 3 : 2, choosing ? THEME.cyan : 0xffffff, choosing ? 0.9 : 0.25).strokeCircle(cx, ey, 60);
    c.add(g);
    // pulsar en la tarjeta la elige para la estantería (detrás de todo lo demás)
    const hit = this.add.zone(x0, y0, W, P_CARD.h).setOrigin(0).setInteractive({ useHandCursor: !choosing });
    hit.on('pointerdown', () => this.setFocus(side));
    c.add(hit);
    c.add(this.add.image(cx, ey, texKey.emblem(team.id)).setDisplaySize(96, 96));

    c.add(chip(this, x0 + 12, y0 + 22, s.label, s.color, { size: 14, h: 26, padX: 12, textColor: '#ffffff' }));
    if (choosing) {
      const tag = chip(this, 0, y0 + 22, 'ELIGIENDO', THEME.cyan, { size: 11, h: 20, padX: 7 });
      tag.setX(x0 + W - 12 - tag.width);
      c.add(tag);
    }

    // flechas grandes a los lados del escudo: equipo anterior / siguiente del mismo juego
    for (const dir of [-1, 1]) {
      const ax = cx + dir * 84;
      const arrow = this.add.graphics();
      arrow.fillStyle(0xffffff, 0.85).fillPoints([pt(ax + dir * 9, ey), pt(ax - dir * 7, ey - 15), pt(ax - dir * 7, ey + 15)], true);
      const zone = this.add.zone(ax - 22, ey - 40, 44, 80).setOrigin(0).setInteractive({ useHandCursor: true });
      zone.on('pointerdown', () => this.cycle(side, dir));
      c.add([arrow, zone]);
    }

    const name = display(this, cx, y0 + 184, team.name, 26, '#ffffff').setOrigin(0.5);
    fitWidth(name, W - 20, 15);
    c.add(name);
    const list = teamsOf(seasonOf(team));
    const season = getSeason(seasonOf(team));
    const icon = season.icon && this.textures.exists(`series:${season.icon}`) ? `series:${season.icon}` : undefined;
    const sc = chip(this, 0, y0 + 214, `${season.short}  ·  ${list.indexOf(team) + 1}/${list.length}`, THEME.panelLight, { size: 13, h: 24, textColor: THEME.text, icon });
    sc.setX(cx - sc.width / 2);
    c.add(sc);

    const rating = teamRating(team);
    const rt = display(this, x0 + 16, y0 + 254, String(rating), 44, THEME.yellowCss, { strokeThickness: 0, shadow: { offsetX: 0, offsetY: 3, color: '#000', blur: 0, fill: true } }).setOrigin(0, 0.5);
    c.add(rt);
    c.add(starRow(this, x0 + 24 + rt.width, y0 + 246, ratingStars(rating), 8));
    const f = getFormation(team.formation);
    const layout = ['DF', 'MF', 'FW'].map((pos) => f.slots.filter((sl) => sl.pos === pos).length).join('-');
    c.add(label(this, x0 + 26 + rt.width, y0 + 266, layout, 15, THEME.text, { fontStyle: 'italic bold' }).setOrigin(0, 0.5));
    const lines = lineRatings(team);
    const cols = [
      ['ATQ', lines.att, '#ffb27a'],
      ['MED', lines.mid, '#8fe8b4'],
      ['DEF', lines.def, '#9fc9ff'],
    ] as const;
    cols.forEach(([cap, v, css], i) => {
      const lx = x0 + 16 + i * ((W - 32) / 3) + (W - 32) / 6;
      c.add(label(this, lx, y0 + 296, String(v), 18, css, { fontStyle: 'bold' }).setOrigin(0.5));
      c.add(label(this, lx, y0 + 315, cap, 11, THEME.muted, { fontStyle: 'bold' }).setOrigin(0.5));
    });
  }

  /** Fila bajo las tarjetas: cambiar lados y rival al azar. */
  private renderCtaP(): void {
    const c = this.ctaRow;
    c.removeAll(true);
    const y = P_CARD.y + P_CARD.h + 40;
    const bw = (GAME_W - 48) / 2;
    c.add(new Button(this, 16 + bw / 2, y, 'Cambiar lados', () => this.swap(), { w: bw, h: 52, variant: 'secondary', size: 18, icon: '⇄' }));
    c.add(new Button(this, GAME_W - 16 - bw / 2, y, 'Rival al azar', () => this.randomRival(), { w: bw, h: 52, variant: 'secondary', size: 18, icon: '⚄' }));
    // el botón de jugar, fijo abajo
    const cy = GAME_H - 46;
    const sh = this.add.graphics();
    sh.fillGradientStyle(THEME.night, THEME.night, THEME.night, THEME.night, 0, 0, 0.95, 0.95).fillRect(0, cy - 60, GAME_W, 106);
    c.add(sh);
    c.add(new Button(this, GAME_W / 2, cy, '¡A la formación!', () => this.next(), { w: GAME_W - 32, h: 68, variant: 'primary', size: 26 }));
  }

  private turnPage(dir: number): void {
    const pages = Math.max(1, Math.ceil(teamsOf(this.shelfSeason).length / P_GRID.per));
    const next = Phaser.Math.Clamp(this.page + dir, 0, pages - 1);
    if (next === this.page) return;
    this.page = next;
    this.renderShelfP();
  }

  /** Estantería del móvil: pestañas con el logo de cada juego y cuadrícula de escudos por páginas. */
  private renderShelfP(): void {
    const c = this.shelf;
    this.tweens.killTweensOf(c.list);
    c.removeAll(true);
    const top = P_SHELF.y;
    const g = this.add.graphics();
    cardPanel(g, 8, top, GAME_W - 16, P_SHELF.h, { plain: true, alpha: 0.92, radius: 16 });
    c.add(g);

    // pestañas: solo el logo de cada juego, todas en una fila
    const seasons = seasonsWithTeams();
    const tabH = 50;
    const tabW = Math.min(64, (GAME_W - 32) / seasons.length);
    const tx0 = GAME_W / 2 - (tabW * seasons.length) / 2;
    const ty = top + 12 + tabH / 2;
    seasons.forEach((s, i) => {
      const on = s.id === this.shelfSeason;
      const x = tx0 + i * tabW;
      const color = on ? THEME.yellow : s.id === 'club' ? THEME.orange : THEME.panelLight;
      const tab = this.add.graphics();
      tab.fillStyle(color, 1).fillRoundedRect(x + 2, ty - tabH / 2, tabW - 4, tabH, 10);
      if (!on) tab.lineStyle(1, 0xffffff, 0.12).strokeRoundedRect(x + 2, ty - tabH / 2, tabW - 4, tabH, 10);
      c.add(tab);
      const isz = Math.min(34, tabW - 14);
      if (s.icon && this.textures.exists(`series:${s.icon}`)) {
        const img = this.add.image(x + tabW / 2, ty, `series:${s.icon}`).setDisplaySize(isz, isz * 1.08);
        if (on) img.setTint(0x0b1a2e);
        c.add(img);
      } else if (s.id === 'club') c.add(this.add.image(x + tabW / 2, ty, texKey.emblem('club')).setDisplaySize(isz, isz));
      else c.add(label(this, x + tabW / 2, ty, s.short, 13, inkOn(color), { fontStyle: 'bold' }).setOrigin(0.5));
      const zone = this.add.zone(x, ty - tabH / 2 - 4, tabW, tabH + 8).setOrigin(0).setInteractive({ useHandCursor: true });
      zone.on('pointerdown', () => {
        if (this.shelfSeason === s.id) return;
        this.shelfSeason = s.id;
        this.page = this.pageOf(this.sel[this.sel.focus]);
        this.renderShelfP();
      });
      c.add(zone);
    });

    // nombre del juego y para qué lado se elige
    const season = getSeason(this.shelfSeason);
    const teams = teamsOf(this.shelfSeason);
    const who = SIDE[this.sel.focus];
    const hy = ty + tabH / 2 + 22;
    const title = label(this, 22, hy, season.name, 19, THEME.text, { fontStyle: 'italic bold' }).setOrigin(0, 0.5);
    fitWidth(title, GAME_W - 210, 14);
    c.add(title);
    const tag = chip(this, 0, hy, `Elige ${who.label === 'TÚ' ? 'el tuyo' : 'el RIVAL'}`, who.color, { size: 14, h: 28, padX: 12, textColor: '#ffffff' });
    tag.setX(GAME_W - 22 - tag.width);
    c.add(tag);

    // cuadrícula de la página
    const pages = Math.max(1, Math.ceil(teams.length / P_GRID.per));
    this.page = Phaser.Math.Clamp(this.page, 0, pages - 1);
    const slice = teams.slice(this.page * P_GRID.per, (this.page + 1) * P_GRID.per);
    const gw = GAME_W - 104; // deja sitio a las flechas
    const cellW = gw / P_GRID.cols;
    const size = 62;
    slice.forEach((team, i) => {
      const col = i % P_GRID.cols;
      const row = Math.floor(i / P_GRID.cols);
      const x = 52 + cellW * (col + 0.5);
      const y = P_GRID.top + P_GRID.cellH * (row + 0.5) - 6;
      const mark = team.id === this.sel.home ? SIDE.home : team.id === this.sel.away ? SIDE.away : null;
      const ring = this.add.graphics();
      if (mark) ring.fillStyle(mark.color, 0.3).fillCircle(x, y, size / 2 + 6).lineStyle(3, mark.color).strokeCircle(x, y, size / 2 + 6);
      c.add(ring);
      const img = this.add.image(x, y, texKey.emblem(team.id)).setDisplaySize(size, size);
      c.add(img);
      const nm = label(this, x, y + size / 2 + 10, team.name, 12, mark ? mark.css : THEME.muted, { fontStyle: 'bold' }).setOrigin(0.5);
      fitWidth(nm, cellW - 4, 9);
      if (nm.width > cellW - 4) nm.setText(team.name.slice(0, 11) + '…');
      c.add(nm);
      if (mark) {
        const t = chip(this, x, y - size / 2 - 2, mark.label, mark.color, { size: 10, h: 16, padX: 6, textColor: '#ffffff' });
        t.setX(x - t.width / 2);
        c.add(t);
      }
      // se elige al soltar, si no se ha deslizado (para poder pasar página arrastrando)
      const zone = this.add.zone(x - cellW / 2, y - P_GRID.cellH / 2, cellW, P_GRID.cellH).setOrigin(0).setInteractive({ useHandCursor: true });
      zone.on('pointerup', (p: Phaser.Input.Pointer) => {
        const w = this.cameras.main.getWorldPoint(p.x, p.y);
        if (Math.abs(w.x - this.swipeStart.x) < 20 && Math.abs(w.y - this.swipeStart.y) < 20) this.choose(team);
      });
      c.add(zone);
    });

    // flechas de página y puntos
    const midY = P_GRID.top + (P_GRID.rows * P_GRID.cellH) / 2 - 6;
    for (const dir of [-1, 1]) {
      const ax = dir < 0 ? 28 : GAME_W - 28;
      const can = dir < 0 ? this.page > 0 : this.page < pages - 1;
      const a = this.add.graphics();
      a.fillStyle(can ? THEME.panelLight : THEME.panel, 1).fillRoundedRect(ax - 20, midY - 40, 40, 80, 12);
      a.fillStyle(can ? 0xffffff : 0x55606f, can ? 0.95 : 0.6).fillPoints([pt(ax + dir * 8, midY), pt(ax - dir * 6, midY - 13), pt(ax - dir * 6, midY + 13)], true);
      c.add(a);
      if (can) {
        const z = this.add.zone(ax - 26, midY - 50, 52, 100).setOrigin(0).setInteractive({ useHandCursor: true });
        z.on('pointerdown', () => this.turnPage(dir));
        c.add(z);
      }
    }
    if (pages > 1) {
      const dy = P_SHELF.y + P_SHELF.h - 16;
      const dots = this.add.graphics();
      for (let i = 0; i < pages; i++) {
        const dx = GAME_W / 2 + (i - (pages - 1) / 2) * 20;
        dots.fillStyle(i === this.page ? THEME.yellow : 0xffffff, i === this.page ? 1 : 0.25).fillCircle(dx, dy, i === this.page ? 6 : 4.5);
      }
      c.add(dots);
    }
    c.add(label(this, GAME_W - 22, P_SHELF.y + P_SHELF.h - 16, `${teams.length} equipos`, 13, THEME.muted).setOrigin(1, 0.5));
  }
}

// medidas del diseño de móvil
const P_CARD = { y: 140, w: 252, h: 330 };
const P_SHELF = { y: 540, h: 316 };
const P_GRID = { top: 652, cols: 4, rows: 2, cellH: 92, per: 8 };
