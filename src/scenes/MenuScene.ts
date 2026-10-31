import Phaser from 'phaser';
import { music } from '../audio/music';
import { fitCamera } from '../ui/theme';
import { soundButton } from '../ui/soundPanel';
import { FONT, GAME_H, GAME_W, hex } from '../config';
import { TEAMS } from '../data';
import { SEASONS, getSeason, seasonOf } from '../data/seasons';
import type { TeamData } from '../data/types';
import { defaultLineup } from '../engine/lineup';
import { lineRatings, teamRating } from '../engine/rating';
import { texKey } from '../gfx/placeholders';
import { text } from '../ui/widgets';

type Side = 'home' | 'away';

interface Selection {
  home: string;
  away: string;
  /** Lado que se está eligiendo desde la estantería de escudos. */
  focus: Side;
}

// Pantalla de "versus": cada mitad con los colores de su equipo, partidas por un rayo.
const CX = { home: 330, away: 950 } as const;
const EMBLEM_Y = 222;
const SHELF_Y = 548;
const NIGHT = 0x0a1120;
const YELLOW = 0xffd23f;
const SIDE = {
  home: { label: 'TÚ', color: 0x2f7bff, css: '#7fb2ff' },
  away: { label: 'RIVAL', color: 0xff3b4e, css: '#ff8f9a' },
} as const;
/** El rayo que parte la pantalla: puntos de arriba abajo. */
const BOLT = [
  [700, 0],
  [652, 150],
  [690, 160],
  [615, 330],
  [662, 338],
  [585, SHELF_Y],
] as const;

const seasonsWithTeams = () => SEASONS.filter((s) => TEAMS.some((t) => seasonOf(t) === s.id));
const teamsOf = (season: string) => TEAMS.filter((t) => seasonOf(t) === season).sort((a, b) => a.name.localeCompare(b.name, 'es'));
const teamById = (id: string) => TEAMS.find((t) => t.id === id)!;
const pt = (x: number, y: number) => new Phaser.Geom.Point(x, y);
/** Color del equipo oscurecido para el fondo, que el texto se lea siempre. */
const dim = (color: string, amount = 0.62) => {
  const c = Phaser.Display.Color.Interpolate.ColorWithColor(Phaser.Display.Color.ValueToColor(hex(color)), Phaser.Display.Color.ValueToColor(NIGHT), 100, amount * 100);
  return Phaser.Display.Color.GetColor(c.r, c.g, c.b);
};

export class MenuScene extends Phaser.Scene {
  private sel!: Selection;
  private shelfSeason!: string;
  private bg!: Phaser.GameObjects.Graphics;
  private sides!: Record<Side, Phaser.GameObjects.Container>;
  private shelf!: Phaser.GameObjects.Container;

  constructor() {
    super('menu');
  }

  create(): void {
    fitCamera(this);
    music.play('menu');
    const saved = this.registry.get('menuSelection') as Selection | undefined;
    this.sel = saved && TEAMS.some((t) => t.id === saved.home) && TEAMS.some((t) => t.id === saved.away) ? { ...saved } : this.defaults();
    this.shelfSeason = seasonOf(teamById(this.sel[this.sel.focus]));

    this.bg = this.add.graphics();
    this.drawSplit();
    this.drawBolt();
    this.sides = { home: this.add.container(0, 0), away: this.add.container(0, 0) };
    this.shelf = this.add.container(0, 0);
    this.drawHeader();
    this.drawCenter();
    this.renderSide('home');
    this.renderSide('away');
    this.renderShelf();
    this.bindKeys();
    soundButton(this, GAME_W - 34, 96, GAME_W - 350, 120);
  }

  private defaults(): Selection {
    const home = TEAMS.find((t) => t.id === 'ie3-inazuma-japan') ?? TEAMS[0];
    const away = TEAMS.find((t) => t.id === 'ie3-desert-lion') ?? TEAMS.find((t) => t !== home) ?? home;
    return { home: home.id, away: away.id, focus: 'away' };
  }

  // ----------------------------------------------------------------- fondo

  /** Las dos mitades con el color de cada equipo, tramado de puntos y líneas de velocidad, como en una viñeta. */
  private drawSplit(): void {
    const g = this.bg.clear();
    const home = teamById(this.sel.home);
    const away = teamById(this.sel.away);
    g.fillStyle(NIGHT).fillRect(0, 0, GAME_W, GAME_H);
    const left = [pt(0, 0), ...BOLT.map(([x, y]) => pt(x, y)), pt(0, SHELF_Y)];
    const right = [pt(GAME_W, 0), ...BOLT.map(([x, y]) => pt(x, y)), pt(GAME_W, SHELF_Y)];
    g.fillStyle(dim(home.colors.shirt)).fillPoints(left, true);
    g.fillStyle(dim(away.colors.shirt)).fillPoints(right, true);
    // líneas de velocidad que salen de cada escudo
    for (const [side, team] of [
      ['home', home],
      ['away', away],
    ] as const) {
      g.lineStyle(2, hex(team.colors.accent), 0.16);
      for (let i = 0; i < 28; i++) {
        const a = (i / 28) * Math.PI * 2;
        const r0 = 150 + (i % 3) * 20;
        g.lineBetween(CX[side] + Math.cos(a) * r0, EMBLEM_Y + Math.sin(a) * r0, CX[side] + Math.cos(a) * 520, EMBLEM_Y + Math.sin(a) * 520);
      }
    }
    // trama de puntos, más densa hacia el borde de abajo
    for (let y = 300; y < SHELF_Y; y += 14) {
      const r = ((y - 300) / (SHELF_Y - 300)) * 2.6;
      g.fillStyle(0x000000, 0.22);
      for (let x = (y / 14) % 2 ? 7 : 0; x < GAME_W; x += 14) g.fillCircle(x, y, r);
    }
    // sombra arriba para el título
    g.fillGradientStyle(0x000000, 0x000000, 0x000000, 0x000000, 0.55, 0.55, 0, 0).fillRect(0, 0, GAME_W, 90);
  }

  private drawBolt(): void {
    const g = this.add.graphics();
    const line = (width: number, color: number, alpha: number) => {
      g.lineStyle(width, color, alpha).beginPath();
      BOLT.forEach(([x, y], i) => (i ? g.lineTo(x, y) : g.moveTo(x, y)));
      g.strokePath();
    };
    line(26, YELLOW, 0.12);
    line(12, YELLOW, 0.35);
    line(5, 0xfff6c8, 1);
    this.tweens.add({ targets: g, alpha: 0.7, duration: 900, yoyo: true, repeat: -1, ease: 'Sine.inOut' });
  }

  private drawHeader(): void {
    const g = this.add.graphics();
    g.fillStyle(YELLOW).fillPoints([pt(24, 18), pt(44, 18), pt(36, 34), pt(46, 34), pt(26, 60), pt(31, 40), pt(20, 40)], true);
    text(this, 54, 18, 'InaMatch', 32, '#ffd23f', { fontStyle: 'italic bold', strokeThickness: 6 });
    text(this, 56, 58, '¡Elige a los equipos!', 15, '#ffffff', { fontStyle: 'italic' });
    text(this, GAME_W - 24, 30, 'Proyecto de fans sin ánimo de lucro\nInazuma Eleven es una marca de LEVEL-5', 11, '#c4cddc', {
      align: 'right',
      strokeThickness: 3,
    }).setOrigin(1, 0.5);
  }

  // ------------------------------------------------------------------ lados

  private renderSide(side: Side): void {
    const c = this.sides[side];
    this.tweens.killTweensOf(c.list);
    c.removeAll(true);
    const cx = CX[side];
    const team = teamById(this.sel[side]);
    const s = SIDE[side];
    const choosing = this.sel.focus === side;

    // destello giratorio detrás del escudo
    const rays = this.add.graphics({ x: cx, y: EMBLEM_Y });
    for (let i = 0; i < 16; i++) {
      const a = (i / 16) * Math.PI * 2;
      rays.fillStyle(i % 2 ? 0xffffff : hex(team.colors.accent), i % 2 ? 0.07 : 0.22);
      rays.fillTriangle(0, 0, Math.cos(a - 0.12) * 150, Math.sin(a - 0.12) * 150, Math.cos(a + 0.12) * 150, Math.sin(a + 0.12) * 150);
    }
    rays.fillStyle(0x000000, 0.28).fillCircle(0, 0, 98);
    rays.lineStyle(4, choosing ? YELLOW : 0xffffff, choosing ? 0.9 : 0.35).strokeCircle(0, 0, 98);
    this.tweens.add({ targets: rays, angle: side === 'home' ? 360 : -360, duration: 40000, repeat: -1 });
    c.add(rays);

    const emblem = this.add.image(cx, EMBLEM_Y, texKey.emblem(team.id)).setDisplaySize(170, 170);
    c.add(emblem);

    // etiqueta TÚ / RIVAL, inclinada, encima del escudo
    const tag = this.add.graphics();
    tag.fillStyle(s.color).fillPoints([pt(cx - 54, 92), pt(cx + 62, 92), pt(cx + 52, 118), pt(cx - 64, 118)], true);
    c.add(tag);
    c.add(text(this, cx - 1, 105, s.label, 16, '#ffffff', { fontStyle: 'italic bold' }).setOrigin(0.5));

    // media en un hexágono, a un lado del escudo
    const hx = cx + (side === 'home' ? -118 : 118);
    const hy = EMBLEM_Y - 74;
    const hexG = this.add.graphics();
    const hexPts = Array.from({ length: 6 }, (_, i) => pt(hx + Math.cos((i * Math.PI) / 3) * 34, hy + Math.sin((i * Math.PI) / 3) * 34));
    hexG.fillStyle(NIGHT, 0.9).fillPoints(hexPts, true);
    hexG.lineStyle(3, YELLOW).strokePoints(hexPts, true);
    c.add(hexG);
    c.add(text(this, hx, hy - 9, String(teamRating(team)), 24, '#ffd23f', { fontStyle: 'bold' }).setOrigin(0.5));
    c.add(text(this, hx, hy + 15, 'MEDIA', 10, '#ffffff').setOrigin(0.5));

    // flechas
    for (const dir of [-1, 1]) {
      const ax = cx + dir * 168;
      const arrow = this.add.graphics();
      const draw = (hover: boolean) => {
        arrow.clear().fillStyle(hover ? YELLOW : 0xffffff, hover ? 1 : 0.85);
        arrow.fillPoints([pt(ax + dir * 16, EMBLEM_Y), pt(ax - dir * 10, EMBLEM_Y - 22), pt(ax - dir * 10, EMBLEM_Y + 22)], true);
      };
      draw(false);
      const zone = this.add.zone(ax - 24, EMBLEM_Y - 34, 48, 68).setOrigin(0).setInteractive({ useHandCursor: true });
      zone.on('pointerover', () => draw(true)).on('pointerout', () => draw(false));
      zone.on('pointerdown', () => this.cycle(side, dir));
      c.add([arrow, zone]);
    }

    // nombre en una banda blanca inclinada, como los rótulos del anime
    const band = this.add.graphics();
    band.fillStyle(0x000000, 0.35).fillPoints([pt(cx - 196, 344), pt(cx + 214, 344), pt(cx + 200, 396), pt(cx - 210, 396)], true);
    band.fillStyle(0xffffff).fillPoints([pt(cx - 200, 338), pt(cx + 210, 338), pt(cx + 196, 390), pt(cx - 214, 390)], true);
    band.fillStyle(hex(team.colors.accent)).fillPoints([pt(cx - 214, 390), pt(cx + 196, 390), pt(cx + 194, 396), pt(cx - 216, 396)], true);
    c.add(band);
    const name = text(this, cx - 2, 364, team.name, 28, '#0b1a2e', { fontStyle: 'italic bold', strokeThickness: 0 }).setOrigin(0.5);
    for (let size = 28; name.width > 380 && size > 14; ) name.setFontSize(--size);
    c.add(name);
    const list = teamsOf(seasonOf(team));
    c.add(
      text(this, cx, 412, `${getSeason(seasonOf(team)).name}  ·  ${list.indexOf(team) + 1}/${list.length}`, 13, '#e3e9f2', { fontStyle: 'italic' }).setOrigin(0.5),
    );

    // barras de línea, como las de FP/TP del partido
    const lines = lineRatings(team);
    const rows = [
      ['Ataque', lines.att, 0xff7a3d],
      ['Medio', lines.mid, 0x46d68c],
      ['Defensa', lines.def, 0x4fa3ff],
    ] as const;
    rows.forEach(([label, value, color], i) => {
      const y = 448 + i * 28;
      const x0 = cx - 150;
      const bar = this.add.graphics();
      bar.fillStyle(0x000000, 0.45).fillPoints([pt(x0 + 86, y - 7), pt(x0 + 266, y - 7), pt(x0 + 262, y + 7), pt(x0 + 82, y + 7)], true);
      const w = Phaser.Math.Clamp((value - 30) / 60, 0.05, 1) * 180;
      bar.fillStyle(color).fillPoints([pt(x0 + 86, y - 7), pt(x0 + 86 + w, y - 7), pt(x0 + 82 + w, y + 7), pt(x0 + 82, y + 7)], true);
      c.add(bar);
      c.add(text(this, x0, y, label, 14, '#ffffff', { fontStyle: 'italic bold' }).setOrigin(0, 0.5));
      c.add(text(this, x0 + 300, y, String(value), 16, '#ffffff', { fontStyle: 'bold' }).setOrigin(1, 0.5));
    });

    // pulsar en cualquier parte de la mitad la elige para la estantería
    const hit = this.add.zone(cx - 250, 80, 500, 440).setOrigin(0).setInteractive();
    hit.on('pointerdown', () => this.setFocus(side));
    hit.on('wheel', (_p: Phaser.Input.Pointer, _dx: number, dy: number) => this.cycle(side, dy > 0 ? 1 : -1));
    c.add(hit);
    c.sendToBack(hit);
  }

  // ----------------------------------------------------------------- centro

  private drawCenter(): void {
    const vs = text(this, 646, EMBLEM_Y - 6, 'VS', 76, '#ffd23f', {
      fontFamily: '"Arial Black", ' + FONT,
      fontStyle: 'italic',
      stroke: '#0b1a2e',
      strokeThickness: 12,
    }).setOrigin(0.5);
    this.tweens.add({ targets: vs, scale: 1.06, duration: 700, yoyo: true, repeat: -1, ease: 'Sine.inOut' });

    const round = (x: number, y: number, icon: string, hint: string, onClick: () => void) => {
      const g = this.add.graphics();
      const draw = (hover: boolean) => {
        g.clear().fillStyle(hover ? YELLOW : NIGHT, 0.92).fillCircle(x, y, 27);
        g.lineStyle(3, YELLOW).strokeCircle(x, y, 27);
      };
      draw(false);
      const label = text(this, x, y, icon, 22, '#ffffff').setOrigin(0.5);
      const tip = text(this, x, y + 42, hint, 12, '#ffffff', { fontStyle: 'italic' }).setOrigin(0.5).setAlpha(0);
      this.add
        .zone(x - 28, y - 28, 56, 56)
        .setOrigin(0)
        .setInteractive({ useHandCursor: true })
        .on('pointerover', () => (draw(true), label.setColor('#0b1a2e'), tip.setAlpha(1)))
        .on('pointerout', () => (draw(false), label.setColor('#ffffff'), tip.setAlpha(0)))
        .on('pointerdown', onClick);
    };
    round(604, 340, '⇄', 'Cambiar lados', () => this.swap());
    round(676, 340, '⚄', 'Rival aleatorio', () => this.randomRival());

    // botón principal: un rayo con el texto
    const bx = 640;
    const by = 470;
    const g = this.add.graphics();
    const shape = (dx: number, dy: number) => [pt(bx - 112 + dx, by - 30 + dy), pt(bx + 126 + dx, by - 30 + dy), pt(bx + 112 + dx, by + 30 + dy), pt(bx - 126 + dx, by + 30 + dy)];
    const draw = (hover: boolean) => {
      g.clear().fillStyle(0x000000, 0.5).fillPoints(shape(5, 6), true);
      g.fillStyle(hover ? 0xffe27a : YELLOW).fillPoints(shape(0, 0), true);
      g.fillStyle(0xffffff, 0.35).fillPoints([pt(bx - 108, by - 26), pt(bx + 121, by - 26), pt(bx + 117, by - 6), pt(bx - 113, by - 6)], true);
    };
    draw(false);
    text(this, bx, by, '¡A la formación!', 22, '#0b1a2e', { fontStyle: 'italic bold', strokeThickness: 0 }).setOrigin(0.5);
    this.add
      .zone(bx - 126, by - 30, 252, 60)
      .setOrigin(0)
      .setInteractive({ useHandCursor: true })
      .on('pointerover', () => draw(true))
      .on('pointerout', () => draw(false))
      .on('pointerdown', () => this.next());
  }

  // ------------------------------------------------------------- estantería

  /** Abajo: pestañas de temporada y todos sus escudos, para elegir de un vistazo. */
  private renderShelf(): void {
    const c = this.shelf;
    this.tweens.killTweensOf(c.list);
    c.removeAll(true);
    const g = this.add.graphics();
    g.fillStyle(0x060b15, 0.94).fillPoints([pt(0, SHELF_Y + 14), pt(GAME_W, SHELF_Y - 10), pt(GAME_W, GAME_H), pt(0, GAME_H)], true);
    g.lineStyle(3, YELLOW, 0.9).lineBetween(0, SHELF_Y + 14, GAME_W, SHELF_Y - 10);
    c.add(g);

    // temporadas
    seasonsWithTeams().forEach((s, i) => {
      const x = 24 + i * 150;
      const y = SHELF_Y + 30;
      const on = s.id === this.shelfSeason;
      const tab = this.add.graphics();
      tab.fillStyle(on ? YELLOW : 0x1c2740).fillPoints([pt(x + 10, y), pt(x + 140, y), pt(x + 130, y + 30), pt(x, y + 30)], true);
      c.add(tab);
      c.add(text(this, x + 70, y + 15, `${s.short} · ${teamsOf(s.id).length} equipos`, 14, on ? '#0b1a2e' : '#c9d3e0', {
        fontStyle: 'italic bold',
        strokeThickness: 0,
      }).setOrigin(0.5));
      const zone = this.add.zone(x, y, 140, 30).setOrigin(0).setInteractive({ useHandCursor: true });
      zone.on('pointerdown', () => {
        this.shelfSeason = s.id;
        this.renderShelf();
      });
      c.add(zone);
    });

    // para qué lado se elige
    const who = SIDE[this.sel.focus];
    c.add(text(this, GAME_W - 24, SHELF_Y + 34, `Eligiendo: ${who.label}`, 15, who.css, { fontStyle: 'italic bold' }).setOrigin(1, 0));
    c.add(text(this, GAME_W - 24, SHELF_Y + 54, 'pulsa una mitad para cambiar', 11, '#8a97aa', { strokeThickness: 0 }).setOrigin(1, 0));

    // escudos de la temporada
    const teams = teamsOf(this.shelfSeason);
    const step = Math.min(58, (GAME_W - 60) / teams.length);
    const x0 = GAME_W / 2 - ((teams.length - 1) * step) / 2;
    const y = SHELF_Y + 112;
    const tip = text(this, 0, y - 46, '', 13, '#ffffff', { fontStyle: 'italic bold' }).setOrigin(0.5).setVisible(false);
    teams.forEach((team, i) => {
      const x = x0 + i * step;
      const ring = this.add.graphics();
      const mark = team.id === this.sel.home ? SIDE.home.color : team.id === this.sel.away ? SIDE.away.color : null;
      if (mark !== null) ring.fillStyle(mark, 0.35).fillCircle(x, y, 27).lineStyle(3, mark).strokeCircle(x, y, 27);
      const img = this.add.image(x, y, texKey.emblem(team.id)).setDisplaySize(46, 46);
      img.setInteractive({ useHandCursor: true });
      img.on('pointerover', () => {
        this.tweens.add({ targets: img, displayWidth: 58, displayHeight: 58, duration: 100 });
        tip.setText(team.name).setPosition(Phaser.Math.Clamp(x, 120, GAME_W - 120), y - 46).setVisible(true);
      });
      img.on('pointerout', () => {
        this.tweens.add({ targets: img, displayWidth: 46, displayHeight: 46, duration: 100 });
        tip.setVisible(false);
      });
      img.on('pointerdown', () => this.choose(team));
      c.add([ring, img]);
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
  }

  private refresh(): void {
    this.drawSplit();
    this.renderSide('home');
    this.renderSide('away');
    this.renderShelf();
  }

  private setFocus(side: Side): void {
    if (this.sel.focus === side) return;
    this.sel.focus = side;
    this.shelfSeason = seasonOf(teamById(this.sel[side]));
    this.refresh();
  }

  private choose(team: TeamData): void {
    this.sel[this.sel.focus] = team.id;
    this.refresh();
  }

  private cycle(side: Side, dir: number): void {
    const team = teamById(this.sel[side]);
    const list = teamsOf(seasonOf(team));
    this.sel[side] = list[(list.indexOf(team) + dir + list.length) % list.length].id;
    this.sel.focus = side;
    this.shelfSeason = seasonOf(team);
    this.refresh();
  }

  /** Arriba/abajo: cambia la temporada de la estantería y elige su primer equipo para el lado activo. */
  private stepSeason(dir: number): void {
    const seasons = seasonsWithTeams();
    const i = seasons.findIndex((s) => s.id === this.shelfSeason);
    this.shelfSeason = seasons[(i + dir + seasons.length) % seasons.length].id;
    this.sel[this.sel.focus] = teamsOf(this.shelfSeason)[0].id;
    this.refresh();
  }

  private swap(): void {
    [this.sel.home, this.sel.away] = [this.sel.away, this.sel.home];
    this.refresh();
  }

  private randomRival(): void {
    const pool = TEAMS.filter((t) => t.id !== this.sel.home);
    const pick: TeamData | undefined = pool[Math.floor(Math.random() * pool.length)];
    if (!pick) return;
    this.sel.away = pick.id;
    this.refresh();
  }

  private next(): void {
    this.registry.set('menuSelection', { ...this.sel });
    const home = teamById(this.sel.home);
    const away = teamById(this.sel.away);
    this.scene.start('formation', { home: defaultLineup(home), away: defaultLineup(away) });
  }
}
