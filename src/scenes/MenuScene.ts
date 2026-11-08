import Phaser from 'phaser';
import { music } from '../audio/music';
import { THEME, cardPanel, chip, coinChip, dim, fitCamera, glow, inkOn, pt, starRow, topBar } from '../ui/theme';
import { soundButton } from '../ui/soundPanel';
import { FONT, GAME_H, GAME_W, hex } from '../config';
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
    topBar(this, { title: 'InaMatch', subtitle: 'Elige los equipos y ¡a jugar!' });
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
    this.refresh();
  }

  /** Arriba/abajo: cambia la temporada de la estantería y elige su primer equipo para el lado activo. */
  private stepSeason(dir: number): void {
    const seasons = seasonsWithTeams();
    const i = seasons.findIndex((s) => s.id === this.shelfSeason);
    this.shelfSeason = seasons[(i + dir + seasons.length) % seasons.length].id;
    const list = teamsOf(this.shelfSeason).filter((t) => t.id !== this.sel[this.other(this.sel.focus)]);
    if (list.length) this.sel[this.sel.focus] = list[0].id;
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
      .text(GAME_W / 2, GAME_H - 30, 'Cargando jugadores…', { fontFamily: FONT, fontSize: '15px', color: '#ffffff', backgroundColor: '#0b1a2ecc', padding: { x: 10, y: 4 } })
      .setOrigin(0.5)
      .setDepth(700);
    ensureSprites(this.textures, [home, away])
      .catch((err) => console.warn('[pack] no se pudieron cargar los sprites dibujados', err))
      .then(() => {
        wait.destroy();
        this.scene.start('formation', { home: defaultLineup(home), away: defaultLineup(away) });
      });
  }
}
