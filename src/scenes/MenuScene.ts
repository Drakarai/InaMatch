import Phaser from 'phaser';
import { COLORS, GAME_H, GAME_W, hex } from '../config';
import { TEAMS } from '../data';
import { SEASONS, getSeason, seasonOf } from '../data/seasons';
import type { TeamData } from '../data/types';
import { defaultLineup } from '../engine/lineup';
import { ratingStars, teamRating } from '../engine/rating';
import { texKey } from '../gfx/placeholders';
import { Button, panelFrame, text } from '../ui/widgets';

export function drawBackdrop(scene: Phaser.Scene): void {
  const g = scene.add.graphics();
  g.fillGradientStyle(0x1d4f8f, 0x1d4f8f, 0x0d2547, 0x0d2547).fillRect(0, 0, GAME_W, GAME_H);
  g.fillStyle(0xffffff, 0.04);
  for (let i = -GAME_H; i < GAME_W; i += 80) g.fillTriangle(i, GAME_H, i + 40, GAME_H, i + 40 + GAME_H, 0).fillTriangle(i, GAME_H, i + GAME_H, 0, i + 40 + GAME_H, 0);
}

/** Estrellas de valoración (con medias estrellas), al estilo FIFA. `bg` es el color de fondo, para tapar la mitad vacía. */
export function drawStars(g: Phaser.GameObjects.Graphics, x: number, y: number, value: number, size: number, bg: number): void {
  const pts = (cx: number, cy: number, r: number) =>
    Array.from({ length: 10 }, (_, i) => {
      const a = -Math.PI / 2 + (i * Math.PI) / 5;
      const rr = i % 2 ? r * 0.45 : r;
      return new Phaser.Geom.Point(cx + Math.cos(a) * rr, cy + Math.sin(a) * rr);
    });
  for (let i = 0; i < 5; i++) {
    const cx = x + i * size * 1.15 + size / 2;
    const fill = Math.min(1, Math.max(0, value - i));
    g.fillStyle(0x3a4a5e).fillPoints(pts(cx, y, size / 2), true);
    if (fill > 0) {
      g.fillStyle(0xffd23f).fillPoints(pts(cx, y, size / 2), true);
      if (fill < 1) {
        // media estrella: se tapa la mitad derecha y se vuelve a pintar vacía
        g.fillStyle(bg).fillRect(cx, y - size / 2 - 1, size / 2 + 1, size + 2);
        g.fillStyle(0x3a4a5e).fillPoints(pts(cx, y, size / 2), true);
        g.fillStyle(0xffd23f).fillPoints(
          pts(cx, y, size / 2).map((p) => new Phaser.Geom.Point(Math.min(p.x, cx), p.y)),
          true,
        );
      }
    }
  }
}

type Slot = 'home' | 'away';

interface Selection {
  season: string;
  home: string;
  away: string;
  active: Slot;
}

const GRID = { x: 248, y: 96, cols: 5, w: 144, h: 104, gap: 8 };
const CARD_BG = 0x24466f;

export class MenuScene extends Phaser.Scene {
  private sel!: Selection;
  private grid!: Phaser.GameObjects.Container;
  private seasonButtons: { id: string; bg: Phaser.GameObjects.Graphics; draw: (on: boolean) => void }[] = [];
  private slots!: Record<Slot, Phaser.GameObjects.Container>;

  constructor() {
    super('menu');
  }

  create(): void {
    drawBackdrop(this);
    const saved = this.registry.get('menuSelection') as Selection | undefined;
    this.sel = saved && TEAMS.some((t) => t.id === saved.home) && TEAMS.some((t) => t.id === saved.away) ? { ...saved } : this.defaults();

    text(this, 28, 22, 'InaMatch', 40, '#ffd23f', { strokeThickness: 8 });
    text(this, 220, 40, 'Elige temporada y equipos', 18, '#d8e8ff');
    text(this, GAME_W - 24, 40, 'Proyecto de fans sin ánimo de lucro · Inazuma Eleven es una marca de LEVEL-5', 11, '#9fb8d8').setOrigin(1, 0.5);

    this.buildSeasons();
    this.grid = this.add.container(0, 0);
    this.slots = { home: this.add.container(1018, 96), away: this.add.container(1018, 336) };
    this.renderGrid();
    this.renderSlots();

    new Button(this, 1138, 600, 'Rival aleatorio', () => this.randomRival(), { w: 220, h: 40, size: 16, color: 0x51647d });
    new Button(this, 1138, 664, 'Formación  ▶', () => this.next(), { w: 220, h: 56, size: 24, color: 0xe2552c });
  }

  private defaults(): Selection {
    const home = TEAMS.find((t) => t.id === 'ie3-inazuma-japan') ?? TEAMS[0];
    const away = TEAMS.find((t) => t.id === 'ie3-desert-lion') ?? TEAMS.find((t) => t !== home) ?? home;
    return { season: seasonOf(home), home: home.id, away: away.id, active: 'home' };
  }

  // ------------------------------------------------------------ temporadas

  private buildSeasons(): void {
    const g = this.add.graphics();
    panelFrame(g, 20, 96, 210, 560, COLORS.panelDark);
    text(this, 36, 108, 'Temporadas', 18, '#ffe28a');
    const seasons = SEASONS.filter((s) => TEAMS.some((t) => seasonOf(t) === s.id));
    seasons.forEach((s, i) => {
      const y = 146 + i * 82;
      const count = TEAMS.filter((t) => seasonOf(t) === s.id).length;
      const bg = this.add.graphics();
      const draw = (on: boolean) => {
        bg.clear();
        bg.fillStyle(on ? 0xe2552c : 0x2c4f7a).fillRoundedRect(32, y, 186, 70, 10);
        bg.lineStyle(2, on ? 0xffffff : COLORS.panelLine, on ? 1 : 0.6).strokeRoundedRect(32, y, 186, 70, 10);
      };
      text(this, 46, y + 10, s.short, 26, '#ffffff', { strokeThickness: 5 });
      text(this, 104, y + 14, s.name.replace('Inazuma Eleven', 'Inazuma\nEleven'), 13, '#ffffff', { lineSpacing: 0 });
      text(this, 46, y + 48, `${count} equipos`, 12, '#d8e8ff');
      const zone = this.add.zone(32, y, 186, 70).setOrigin(0).setInteractive({ useHandCursor: true });
      zone.on('pointerdown', () => {
        this.sel.season = s.id;
        this.renderGrid();
      });
      this.seasonButtons.push({ id: s.id, bg, draw });
      draw(s.id === this.sel.season);
    });
  }

  // --------------------------------------------------------------- equipos

  private renderGrid(): void {
    for (const b of this.seasonButtons) b.draw(b.id === this.sel.season);
    this.grid.removeAll(true);
    const g = this.add.graphics();
    panelFrame(g, GRID.x - 10, GRID.y - 10, GRID.cols * (GRID.w + GRID.gap) + 12, 572, COLORS.panelDark);
    this.grid.add(g);
    const teams = TEAMS.filter((t) => seasonOf(t) === this.sel.season);
    teams.forEach((team, i) => {
      const x = GRID.x + (i % GRID.cols) * (GRID.w + GRID.gap);
      const y = GRID.y + Math.floor(i / GRID.cols) * (GRID.h + GRID.gap);
      this.grid.add(this.card(team, x, y));
    });
    if (teams.length === 0) this.grid.add(text(this, GRID.x + 380, GRID.y + 260, 'Sin equipos', 20).setOrigin(0.5));
  }

  private card(team: TeamData, x: number, y: number): Phaser.GameObjects.Container {
    const c = this.add.container(x, y);
    const bg = this.add.graphics();
    const isHome = this.sel.home === team.id;
    const isAway = this.sel.away === team.id;
    const draw = (hover: boolean) => {
      bg.clear();
      bg.fillStyle(hover ? 0x2f5a8c : CARD_BG).fillRoundedRect(0, 0, GRID.w, GRID.h, 8);
      bg.fillStyle(hex(team.colors.accent)).fillRect(0, GRID.h - 5, GRID.w, 5);
      const border = isHome ? 0x4fa3ff : isAway ? 0xff5a6a : 0x6f9fd6;
      bg.lineStyle(isHome || isAway ? 3 : 1, border, isHome || isAway ? 1 : 0.5).strokeRoundedRect(0, 0, GRID.w, GRID.h, 8);
    };
    draw(false);
    const emblem = this.add.image(GRID.w / 2, 28, texKey.emblem(team.id)).setDisplaySize(44, 44);
    const name = text(this, GRID.w / 2, 54, team.name, 12, '#ffffff', { align: 'center', wordWrap: { width: GRID.w - 10 } }).setOrigin(0.5, 0);
    if (name.height > 20) name.setFontSize(10).setY(51);
    const stars = this.add.graphics();
    drawStars(stars, GRID.w / 2 - 38, GRID.h - 14, ratingStars(teamRating(team)), 13, CARD_BG);
    c.add([bg, emblem, name, stars]);
    if (isHome || isAway) c.add(text(this, 6, 4, isHome ? 'TÚ' : 'RIVAL', 10, isHome ? '#9fd0ff' : '#ffb0b0'));
    c.setSize(GRID.w, GRID.h);
    c.setInteractive(new Phaser.Geom.Rectangle(0, 0, GRID.w, GRID.h), Phaser.Geom.Rectangle.Contains);
    c.input!.cursor = 'pointer';
    c.on('pointerover', () => draw(true));
    c.on('pointerout', () => draw(false));
    c.on('pointerdown', () => this.choose(team));
    return c;
  }

  private choose(team: TeamData): void {
    this.sel[this.sel.active] = team.id;
    // como en FIFA: después de elegir tu equipo se pasa a elegir el rival
    if (this.sel.active === 'home') this.sel.active = 'away';
    this.renderGrid();
    this.renderSlots();
  }

  private randomRival(): void {
    const pool = TEAMS.filter((t) => t.id !== this.sel.home);
    const pickTeam = pool[Math.floor(Math.random() * pool.length)];
    if (!pickTeam) return;
    this.sel.away = pickTeam.id;
    this.sel.season = seasonOf(pickTeam);
    this.renderGrid();
    this.renderSlots();
  }

  // ---------------------------------------------------------------- fichas

  private renderSlots(): void {
    (['home', 'away'] as Slot[]).forEach((slot) => {
      const c = this.slots[slot];
      c.removeAll(true);
      const team = TEAMS.find((t) => t.id === this.sel[slot])!;
      const active = this.sel.active === slot;
      const color = slot === 'home' ? 0x2d5fb8 : 0xa8283a;
      const g = this.add.graphics();
      panelFrame(g, 0, 0, 240, 226, COLORS.panelDark);
      g.fillStyle(color).fillRoundedRect(2, 2, 236, 30, { tl: 10, tr: 10, bl: 0, br: 0 });
      if (active) g.lineStyle(3, 0xffd23f).strokeRoundedRect(0, 0, 240, 226, 10);
      c.add(g);
      c.add(text(this, 12, 8, slot === 'home' ? 'Tu equipo' : 'Rival', 16));
      if (active) c.add(text(this, 228, 9, '◀ eligiendo', 12, '#ffe28a').setOrigin(1, 0));
      c.add(this.add.image(120, 84, texKey.emblem(team.id)).setDisplaySize(80, 80));
      c.add(text(this, 120, 130, team.name, 17, '#ffffff', { align: 'center', wordWrap: { width: 220 } }).setOrigin(0.5, 0));
      const rating = teamRating(team);
      c.add(text(this, 14, 178, getSeason(seasonOf(team)).name, 12, '#b9d0ee'));
      c.add(text(this, 14, 198, `Media ${rating}`, 15, '#ffe28a'));
      const stars = this.add.graphics();
      drawStars(stars, 120, 207, ratingStars(rating), 16, COLORS.panelDark);
      c.add(stars);
      c.setSize(240, 226);
      c.setInteractive(new Phaser.Geom.Rectangle(0, 0, 240, 226), Phaser.Geom.Rectangle.Contains);
      c.input!.cursor = 'pointer';
      c.on('pointerdown', () => {
        this.sel.active = slot;
        this.sel.season = seasonOf(team);
        this.renderGrid();
        this.renderSlots();
      });
    });
  }

  private next(): void {
    this.registry.set('menuSelection', { ...this.sel });
    const home = TEAMS.find((t) => t.id === this.sel.home)!;
    const away = TEAMS.find((t) => t.id === this.sel.away)!;
    this.scene.start('formation', { home: defaultLineup(home), away: defaultLineup(away) });
  }
}
