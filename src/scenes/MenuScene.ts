import Phaser from 'phaser';
import { GAME_H, GAME_W, hex } from '../config';
import { TEAMS } from '../data';
import { SEASONS, getSeason, seasonOf } from '../data/seasons';
import type { TeamData } from '../data/types';
import { defaultLineup } from '../engine/lineup';
import { lineRatings, ratingStars, teamRating } from '../engine/rating';
import { texKey } from '../gfx/placeholders';
import { Button, text } from '../ui/widgets';

export function drawBackdrop(scene: Phaser.Scene): void {
  const g = scene.add.graphics();
  g.fillGradientStyle(0x1d4f8f, 0x1d4f8f, 0x0d2547, 0x0d2547).fillRect(0, 0, GAME_W, GAME_H);
  g.fillStyle(0xffffff, 0.04);
  for (let i = -GAME_H; i < GAME_W; i += 80) g.fillTriangle(i, GAME_H, i + 40, GAME_H, i + 40 + GAME_H, 0).fillTriangle(i, GAME_H, i + GAME_H, 0, i + 40 + GAME_H, 0);
}

/** Estrellas de valoración (con medias estrellas), al estilo FIFA. `bg` es el color de fondo, para tapar la mitad vacía. */
export function drawStars(g: Phaser.GameObjects.Graphics, x: number, y: number, value: number, size: number, bg: number, empty = 0x3a4a5e): void {
  const pts = (cx: number, cy: number, r: number) =>
    Array.from({ length: 10 }, (_, i) => {
      const a = -Math.PI / 2 + (i * Math.PI) / 5;
      const rr = i % 2 ? r * 0.45 : r;
      return new Phaser.Geom.Point(cx + Math.cos(a) * rr, cy + Math.sin(a) * rr);
    });
  for (let i = 0; i < 5; i++) {
    const cx = x + i * size * 1.15 + size / 2;
    const fill = Math.min(1, Math.max(0, value - i));
    g.fillStyle(empty).fillPoints(pts(cx, y, size / 2), true);
    if (fill > 0) {
      g.fillStyle(0xe8c46a).fillPoints(pts(cx, y, size / 2), true);
      if (fill < 1) {
        // media estrella: se tapa la mitad derecha y se vuelve a pintar vacía
        g.fillStyle(bg).fillRect(cx, y - size / 2 - 1, size / 2 + 1, size + 2);
        g.fillStyle(empty).fillPoints(pts(cx, y, size / 2), true);
        g.fillStyle(0xe8c46a).fillPoints(
          pts(cx, y, size / 2).map((p) => new Phaser.Geom.Point(Math.min(p.x, cx), p.y)),
          true,
        );
      }
    }
  }
}

type Side = 'home' | 'away';

interface Selection {
  home: string;
  away: string;
  focus: Side;
}

// Pantalla "Partido clásico" de FIFA: una columna por equipo, con las temporadas como ligas.
const COL = { home: 360, away: 920 } as const;
const COL_W = 360;
const CHIPS_Y = 112;
const CARD = { y: 156, h: 368 };
const LEAGUE = { y: 536, h: 104 };
const CARD_BG = 0x161d29;
const FOCUS = 0x3fd6c6;
const SIDE_COLOR = { home: 0x2d6fd8, away: 0xd23a4a } as const;

const seasonsWithTeams = () => SEASONS.filter((s) => TEAMS.some((t) => seasonOf(t) === s.id));
const teamsOf = (season: string) => TEAMS.filter((t) => seasonOf(t) === season);
const teamById = (id: string) => TEAMS.find((t) => t.id === id)!;

export class MenuScene extends Phaser.Scene {
  private sel!: Selection;
  private columns!: Record<Side, Phaser.GameObjects.Container>;

  constructor() {
    super('menu');
  }

  create(): void {
    const saved = this.registry.get('menuSelection') as Selection | undefined;
    this.sel = saved && TEAMS.some((t) => t.id === saved.home) && TEAMS.some((t) => t.id === saved.away) ? { ...saved } : this.defaults();

    this.drawStadium();
    this.drawHeader();
    this.columns = { home: this.add.container(0, 0), away: this.add.container(0, 0) };
    this.renderColumn('home');
    this.renderColumn('away');
    this.drawCenter();
    this.bindKeys();
  }

  private defaults(): Selection {
    const home = TEAMS.find((t) => t.id === 'ie3-inazuma-japan') ?? TEAMS[0];
    const away = TEAMS.find((t) => t.id === 'ie3-desert-lion') ?? TEAMS.find((t) => t !== home) ?? home;
    return { home: home.id, away: away.id, focus: 'home' };
  }

  // ----------------------------------------------------------------- fondo

  /** Estadio de noche: degradado oscuro, focos, césped en perspectiva y un rayo dorado detrás del visitante. */
  private drawStadium(): void {
    const g = this.add.graphics();
    g.fillGradientStyle(0x0c121c, 0x0c121c, 0x111a22, 0x111a22).fillRect(0, 0, GAME_W, GAME_H);
    // gradas y focos
    for (let i = 0; i < 8; i++) g.fillStyle(0x9fd7ff, 0.012).fillEllipse(GAME_W / 2, 150, 500 + i * 110, 90 + i * 22);
    for (let i = 0; i < 12; i++) {
      const x = 200 + i * 80;
      const y = 74 + Math.abs(i - 5.5) * 3;
      g.fillStyle(0xdfe9ff, 0.08).fillCircle(x, y, 7);
      g.fillStyle(0xffffff, 0.6).fillCircle(x, y, 2);
    }
    // césped en perspectiva con niebla verdosa
    g.fillGradientStyle(0x0f241d, 0x0f241d, 0x1b3a2c, 0x1b3a2c, 1).fillRect(0, 430, GAME_W, GAME_H - 430);
    g.lineStyle(1, 0x5f9a7e, 0.12);
    for (let i = -8; i <= 8; i++) g.lineBetween(GAME_W / 2 + i * 40, 430, GAME_W / 2 + i * 190, GAME_H);
    for (let y = 450; y < GAME_H; y += (y - 410) * 0.35) g.lineBetween(0, y, GAME_W, y);
    g.fillStyle(0x58c49a, 0.06).fillEllipse(GAME_W / 2, 470, 1500, 160);
    // rayo de Inazuma, enorme y casi transparente, a la derecha
    g.fillStyle(0xd9a93a, 0.1);
    g.fillPoints(
      [
        { x: 1060, y: -20 },
        { x: 1300, y: -20 },
        { x: 1170, y: 250 },
        { x: 1290, y: 250 },
        { x: 960, y: 760 },
        { x: 1060, y: 380 },
        { x: 940, y: 380 },
      ].map((p) => new Phaser.Geom.Point(p.x, p.y)),
      true,
    );
    // viñeta
    g.fillGradientStyle(0x000000, 0x000000, 0x000000, 0x000000, 0.55, 0, 0.55, 0).fillRect(0, 0, 180, GAME_H);
    g.fillGradientStyle(0x000000, 0x000000, 0x000000, 0x000000, 0, 0.55, 0, 0.55).fillRect(GAME_W - 180, 0, 180, GAME_H);
    // LOCAL y VISITANTE en vertical, como HOME / AWAY
    const side = (x: number, label: string) =>
      this.add
        .text(x, GAME_H / 2 + 20, label, { fontFamily: '"Arial Black", Arial, sans-serif', fontSize: '64px', color: '#ffffff' })
        .setOrigin(0.5)
        .setAngle(-90)
        .setAlpha(0.22);
    side(92, 'LOCAL');
    side(GAME_W - 92, 'VISITANTE');
  }

  private drawHeader(): void {
    text(this, 40, 26, 'InaMatch', 30, '#ffd23f', { strokeThickness: 6 });
    const g = this.add.graphics();
    g.lineStyle(1, 0xffffff, 0.35).lineBetween(222, 28, 222, 64);
    text(this, 240, 32, 'Partido clásico', 22, '#ffffff', { strokeThickness: 0, fontStyle: 'bold' });
    text(this, 416, 37, 'Elige equipos', 15, '#c9d3e0', { strokeThickness: 0 });
    text(this, GAME_W - 30, 46, 'Proyecto de fans sin ánimo de lucro · Inazuma Eleven es una marca de LEVEL-5', 11, '#7f8fa6', {
      strokeThickness: 0,
    }).setOrigin(1, 0.5);
  }

  // --------------------------------------------------------------- columnas

  private renderColumn(side: Side, slide = 0): void {
    const c = this.columns[side];
    c.removeAll(true);
    const cx = COL[side];
    const x0 = cx - COL_W / 2;
    const team = teamById(this.sel[side]);
    const season = seasonOf(team);
    const focused = this.sel.focus === side;

    // temporadas: pestañas con círculo marcado, como Masculino / Femenino
    const seasons = seasonsWithTeams();
    const chipW = (COL_W - (seasons.length - 1) * 8) / seasons.length;
    seasons.forEach((s, i) => {
      const x = x0 + i * (chipW + 8);
      const on = s.id === season;
      const g = this.add.graphics();
      g.fillStyle(on ? 0x243042 : 0x161d29, 0.92).fillRoundedRect(x, CHIPS_Y - 17, chipW, 34, 8);
      if (on) g.lineStyle(1, 0x46566c).strokeRoundedRect(x, CHIPS_Y - 17, chipW, 34, 8);
      g.fillStyle(on ? 0x38c172 : 0x0b0f16).fillCircle(x + 20, CHIPS_Y, 8);
      g.lineStyle(1, on ? 0x38c172 : 0x6b7a90).strokeCircle(x + 20, CHIPS_Y, 8);
      if (on) g.lineStyle(2, 0xffffff).lineBetween(x + 16, CHIPS_Y, x + 19, CHIPS_Y + 3).lineBetween(x + 19, CHIPS_Y + 3, x + 24, CHIPS_Y - 3);
      const label = text(this, x + 36, CHIPS_Y, s.short, 15, on ? '#ffffff' : '#a9b4c4', { strokeThickness: 0, fontStyle: 'bold' }).setOrigin(0, 0.5);
      const zone = this.add.zone(x, CHIPS_Y - 17, chipW, 34).setOrigin(0).setInteractive({ useHandCursor: true });
      zone.on('pointerdown', () => this.setSeason(side, s.id));
      c.add([g, label, zone]);
    });

    // ficha del equipo
    const g = this.add.graphics();
    g.fillStyle(CARD_BG, 0.96).fillRoundedRect(x0, CARD.y, COL_W, CARD.h, 6);
    g.lineStyle(focused ? 2 : 1, focused ? FOCUS : 0x2b3646, focused ? 1 : 0.9).strokeRoundedRect(x0, CARD.y, COL_W, CARD.h, 6);
    g.fillStyle(SIDE_COLOR[side]).fillRoundedRect(x0 + 14, CARD.y + 14, 44, 20, 4);
    // la ficha entera: pulsar la enfoca, la rueda cambia de equipo (va debajo de las flechas)
    const hit = this.add.zone(x0, CARD.y, COL_W, CARD.h).setOrigin(0).setInteractive();
    hit.on('pointerdown', () => this.setFocus(side));
    hit.on('wheel', (_p: Phaser.Input.Pointer, _dx: number, dy: number) => this.cycle(side, dy > 0 ? 1 : -1));
    c.add([g, hit]);
    c.add(text(this, x0 + 36, CARD.y + 24, side === 'home' ? 'TÚ' : 'CPU', 12, '#ffffff', { strokeThickness: 0, fontStyle: 'bold' }).setOrigin(0.5));
    const list = teamsOf(season);
    c.add(text(this, x0 + COL_W - 14, CARD.y + 24, `${list.indexOf(team) + 1}/${list.length}`, 12, '#7f8fa6', { strokeThickness: 0 }).setOrigin(1, 0.5));
    const name = text(this, cx, CARD.y + 56, team.name, 24, '#ffffff', { strokeThickness: 0, fontStyle: 'bold' }).setOrigin(0.5);
    for (let size = 24; name.width > COL_W - 40 && size > 14; ) name.setFontSize(--size);
    c.add(name);

    const ey = CARD.y + 170;
    const glow = this.add.graphics();
    glow.fillStyle(hex(team.colors.accent), 0.14).fillCircle(cx, ey, 92);
    c.add(glow);
    const emblem = this.add.image(cx, ey, texKey.emblem(team.id)).setDisplaySize(170, 170);
    c.add(emblem);
    if (slide) {
      emblem.setX(cx + slide * 50).setAlpha(0);
      this.tweens.add({ targets: emblem, x: cx, alpha: 1, duration: 160, ease: 'Cubic.out' });
    }
    for (const dir of [-1, 1]) {
      const arrow = text(this, cx + dir * 140, ey, dir < 0 ? '◀' : '▶', 22, '#ffffff', { strokeThickness: 0 }).setOrigin(0.5);
      arrow.setPadding(14, 20, 14, 20).setInteractive({ useHandCursor: true }).on('pointerdown', () => this.cycle(side, dir));
      arrow.on('pointerover', () => arrow.setColor('#3fd6c6')).on('pointerout', () => arrow.setColor('#ffffff'));
      c.add(arrow);
    }

    const rating = teamRating(team);
    const stars = this.add.graphics();
    drawStars(stars, cx - 62, CARD.y + 280, ratingStars(rating), 22, CARD_BG, 0x3c4656);
    c.add(stars);
    const lines = lineRatings(team);
    (['att', 'mid', 'def'] as const).forEach((k, i) => {
      const lx = cx + (i - 1) * 76;
      c.add(text(this, lx, CARD.y + 312, { att: 'ATA', mid: 'MED', def: 'DEF' }[k], 13, '#ffffff', { strokeThickness: 0 }).setOrigin(0.5));
      c.add(text(this, lx, CARD.y + 340, String(lines[k]), 26, '#e6ebf2', { strokeThickness: 0 }).setOrigin(0.5));
    });

    // "liga": el logo de la temporada
    const lg = this.add.graphics();
    lg.fillStyle(0x161d29, 0.85).fillRoundedRect(x0, LEAGUE.y, COL_W, LEAGUE.h, 6);
    c.add(lg);
    const info = getSeason(season);
    c.add(text(this, cx, LEAGUE.y + 18, info.name.toUpperCase(), 12, '#c9d3e0', { strokeThickness: 0 }).setOrigin(0.5));
    this.seasonLogo(c, cx, LEAGUE.y + 64, info.id);
  }

  /** Logo de la temporada: "INAZUMA ELEVEN" con el número grande y un rayo. */
  private seasonLogo(c: Phaser.GameObjects.Container, x: number, y: number, season: string): void {
    const num = ({ ie1: '1', ie2: '2', ie3: '3' } as Record<string, string>)[season] ?? '+';
    const bolt = this.add.graphics();
    bolt.fillStyle(0xffd23f).fillPoints(
      [
        { x: -8, y: -22 },
        { x: 10, y: -22 },
        { x: 2, y: -4 },
        { x: 12, y: -4 },
        { x: -10, y: 24 },
        { x: -3, y: 2 },
        { x: -13, y: 2 },
      ].map((p) => new Phaser.Geom.Point(x - 112 + p.x, y + p.y)),
      true,
    );
    c.add(bolt);
    c.add(
      this.add
        .text(x - 92, y - 2, 'INAZUMA\nELEVEN', { fontFamily: '"Arial Black", Arial, sans-serif', fontSize: '20px', color: '#ffffff', lineSpacing: -6 })
        .setOrigin(0, 0.5),
    );
    c.add(text(this, x + 82, y, num, 52, '#ffd23f', { fontFamily: '"Arial Black", Arial, sans-serif', stroke: '#b5521f', strokeThickness: 6 }).setOrigin(0.5));
  }

  // ----------------------------------------------------------------- centro

  private drawCenter(): void {
    const cx = GAME_W / 2;
    const item = (y: number, icon: string, label: string, onClick: () => void) => {
      const box = this.add.graphics();
      const draw = (hover: boolean) => {
        box.clear().fillStyle(hover ? 0x2a3546 : 0x161d29, hover ? 0.95 : 0.7).fillRoundedRect(cx - 80, y - 44, 160, 88, 8);
      };
      draw(false);
      text(this, cx, y - 16, icon, 24, '#ffffff', { strokeThickness: 0 }).setOrigin(0.5);
      text(this, cx, y + 18, label, 15, '#e6ebf2', { strokeThickness: 0, align: 'center' }).setOrigin(0.5);
      this.add
        .zone(cx - 80, y - 44, 160, 88)
        .setOrigin(0)
        .setInteractive({ useHandCursor: true })
        .on('pointerover', () => draw(true))
        .on('pointerout', () => draw(false))
        .on('pointerdown', onClick);
    };
    item(250, '⇄', 'Cambiar lados', () => this.swap());
    item(354, '⚄', 'Rival aleatorio', () => this.randomRival());

    text(this, cx, 452, '◀ ▶  cambiar equipo\n▲ ▼  cambiar temporada\nTab  otra columna', 12, '#8a97aa', {
      strokeThickness: 0,
      align: 'center',
      lineSpacing: 4,
    }).setOrigin(0.5);

    new Button(this, cx, 672, 'Formación  ▶', () => this.next(), { w: 250, h: 52, size: 22, color: 0xe2552c });
  }

  // --------------------------------------------------------------- acciones

  private bindKeys(): void {
    const kb = this.input.keyboard;
    if (!kb) return;
    kb.on('keydown-LEFT', () => this.cycle(this.sel.focus, -1));
    kb.on('keydown-RIGHT', () => this.cycle(this.sel.focus, 1));
    kb.on('keydown-UP', () => this.stepSeason(this.sel.focus, -1));
    kb.on('keydown-DOWN', () => this.stepSeason(this.sel.focus, 1));
    kb.on('keydown-TAB', (e: KeyboardEvent) => {
      e.preventDefault();
      this.setFocus(this.sel.focus === 'home' ? 'away' : 'home');
    });
    kb.on('keydown-ENTER', () => this.next());
  }

  private setFocus(side: Side): void {
    if (this.sel.focus === side) return;
    this.sel.focus = side;
    this.renderColumn('home');
    this.renderColumn('away');
  }

  private cycle(side: Side, dir: number): void {
    const team = teamById(this.sel[side]);
    const list = teamsOf(seasonOf(team));
    const i = list.indexOf(team);
    this.sel[side] = list[(i + dir + list.length) % list.length].id;
    this.sel.focus = side;
    this.renderColumn(side, dir);
    this.renderColumn(side === 'home' ? 'away' : 'home');
  }

  private setSeason(side: Side, season: string): void {
    this.sel.focus = side;
    if (seasonOf(teamById(this.sel[side])) !== season) {
      const list = teamsOf(season);
      // se queda con el equipo del mismo nombre si lo hay, si no el primero
      const current = teamById(this.sel[side]).name;
      this.sel[side] = (list.find((t) => t.name === current) ?? list[0]).id;
    }
    this.renderColumn('home');
    this.renderColumn('away');
  }

  private stepSeason(side: Side, dir: number): void {
    const seasons = seasonsWithTeams();
    const i = seasons.findIndex((s) => s.id === seasonOf(teamById(this.sel[side])));
    this.setSeason(side, seasons[(i + dir + seasons.length) % seasons.length].id);
  }

  private swap(): void {
    [this.sel.home, this.sel.away] = [this.sel.away, this.sel.home];
    this.renderColumn('home');
    this.renderColumn('away');
  }

  private randomRival(): void {
    const pool = TEAMS.filter((t) => t.id !== this.sel.home);
    const pick: TeamData | undefined = pool[Math.floor(Math.random() * pool.length)];
    if (!pick) return;
    this.sel.away = pick.id;
    this.sel.focus = 'away';
    this.renderColumn('home');
    this.renderColumn('away', 1);
  }

  private next(): void {
    this.registry.set('menuSelection', { ...this.sel });
    const home = teamById(this.sel.home);
    const away = teamById(this.sel.away);
    this.scene.start('formation', { home: defaultLineup(home), away: defaultLineup(away) });
  }
}
