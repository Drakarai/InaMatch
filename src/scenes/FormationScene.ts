import Phaser from 'phaser';
import { COLORS, hex } from '../config';
import { getTeam, movesOf } from '../data';
import { ELEMENT_COLOR, ELEMENT_LABEL } from '../data/elements';
import { FORMATIONS, getFormation } from '../data/formations';
import type { PlayerData, Stats } from '../data/types';
import { texKey } from '../gfx/placeholders';
import { lineupPlayers, swapInLineup, type Lineup } from '../engine/lineup';
import { Button, StatBar, panelFrame, text } from '../ui/widgets';
import { drawBackdrop } from './MenuScene';

export const STAT_LABELS: [keyof Stats, string][] = [
  ['kick', 'Tiro'],
  ['body', 'Físico'],
  ['control', 'Control'],
  ['guard', 'Defensa'],
  ['speed', 'Rapidez'],
  ['stamina', 'Aguante'],
  ['guts', 'Valor'],
];

const MOVE_KIND_LABEL = { shoot: 'Tiro', dribble: 'Regate', block: 'Bloqueo', catch: 'Parada' } as const;

const PITCH_BOX = { x: 50, y: 60, w: 450, h: 600 };
const BENCH_BOX = { x: 540, y: 400, w: 700, h: 210 };

interface Token {
  index: number; // posición en lineup.order
  container: Phaser.GameObjects.Container;
}

export class FormationScene extends Phaser.Scene {
  private home!: Lineup;
  private away!: Lineup;
  private selected: number | null = null;
  private tokens: Token[] = [];
  private info!: Phaser.GameObjects.Container;
  private formationLabel!: Phaser.GameObjects.Text;

  constructor() {
    super('formation');
  }

  init(data: { home: Lineup; away: Lineup }): void {
    this.home = data.home;
    this.away = data.away;
    this.selected = null;
  }

  create(): void {
    drawBackdrop(this);
    const team = getTeam(this.home.teamId);

    // Campo
    const g = this.add.graphics();
    panelFrame(g, PITCH_BOX.x - 14, PITCH_BOX.y - 44, PITCH_BOX.w + 28, PITCH_BOX.h + 58, COLORS.panelDark);
    text(this, PITCH_BOX.x, PITCH_BOX.y - 36, `Formación · ${team.name}`, 20, '#ffe28a');
    this.drawMiniPitch(g);

    // Ficha
    this.info = this.add.container(540, 16);

    // Banquillo y botones
    panelFrame(g, BENCH_BOX.x, BENCH_BOX.y, BENCH_BOX.w, BENCH_BOX.h, COLORS.panelDark);
    text(this, BENCH_BOX.x + 16, BENCH_BOX.y + 8, 'Banquillo', 18, '#ffe28a');
    text(this, BENCH_BOX.x + 130, BENCH_BOX.y + 12, 'Pulsa dos jugadores para cambiarlos', 14, '#b9d0ee');

    new Button(this, 600, 650, '◀', () => this.cycleFormation(-1), { w: 44, h: 48 });
    this.formationLabel = text(this, 760, 650, '', 20).setOrigin(0.5);
    new Button(this, 920, 650, '▶', () => this.cycleFormation(1), { w: 44, h: 48 });
    new Button(this, 1130, 650, '¡A jugar!', () => this.play(), { w: 200, h: 56, size: 26, color: 0xe2552c });
    new Button(this, 1186, 418, 'Menú', () => this.scene.start('menu'), { w: 90, h: 30, size: 15, color: 0x51647d });

    this.layoutTokens();
    this.showInfo(lineupPlayers(team, this.home)[0]);
  }

  private drawMiniPitch(g: Phaser.GameObjects.Graphics): void {
    const { x, y, w, h } = PITCH_BOX;
    for (let i = 0; i < 8; i++) {
      g.fillStyle(i % 2 ? 0x55b85f : 0x4aa955).fillRect(x, y + (i * h) / 8, w, h / 8);
    }
    g.lineStyle(2, 0xffffff, 0.9).strokeRect(x, y, w, h);
    g.beginPath();
    g.arc(x + w / 2, y, 70, 0, Math.PI);
    g.strokePath();
    g.strokeRect(x + w / 2 - 110, y + h - 90, 220, 90);
    g.strokeRect(x + w / 2 - 50, y + h - 34, 100, 34);
    g.fillStyle(0xdfe7ef).fillRect(x + w / 2 - 45, y + h, 90, 10);
    const rows: [string, number][] = [
      ['FW', 0.33],
      ['MF', 0.55],
      ['DF', 0.78],
      ['GK', 0.96],
    ];
    for (const [label, sy] of rows) text(this, x - 8, this.slotY(sy) - 10, label, 14, '#ffffff').setOrigin(1, 0.5);
  }

  private slotY(sy: number): number {
    return PITCH_BOX.y + ((sy - 0.24) / 0.76) * (PITCH_BOX.h - 30);
  }

  private layoutTokens(): void {
    for (const t of this.tokens) t.container.destroy();
    this.tokens = [];
    const team = getTeam(this.home.teamId);
    const formation = getFormation(this.home.formationId);
    this.formationLabel.setText(formation.name);
    const players = lineupPlayers(team, this.home);

    players.forEach((p, index) => {
      let x: number;
      let y: number;
      if (index < 11) {
        const slot = formation.slots[index];
        x = PITCH_BOX.x + slot.x * PITCH_BOX.w;
        y = this.slotY(slot.y);
      } else {
        const b = index - 11;
        x = BENCH_BOX.x + 60 + (b % 7) * 96;
        y = BENCH_BOX.y + 80 + Math.floor(b / 7) * 92;
      }
      this.tokens.push({ index, container: this.makeToken(p, index, x, y) });
    });
  }

  private makeToken(p: PlayerData, index: number, x: number, y: number): Phaser.GameObjects.Container {
    const c = this.add.container(x, y);
    const ring = this.add.graphics();
    if (this.selected === index) ring.fillStyle(0xffd23f, 0.9).fillEllipse(0, 22, 46, 16);
    else ring.fillStyle(0x000000, 0.25).fillEllipse(0, 22, 34, 10);
    const sprite = this.add.image(0, 0, texKey.sprite(p.id));
    sprite.setScale(46 / sprite.height);
    const name = text(this, 0, 30, p.short, 13).setOrigin(0.5, 0);
    const outOfPosition = index < 11 && getFormation(this.home.formationId).slots[index].pos !== p.position;
    const badge = text(this, 18, -26, p.position, 11, outOfPosition ? '#ff9f9f' : '#c8f7c5');
    c.add([ring, sprite, name, badge]);
    c.setSize(56, 70);
    c.setInteractive({ useHandCursor: true })
      .on('pointerover', () => this.showInfo(p))
      .on('pointerdown', () => this.pick(index));
    return c;
  }

  private pick(index: number): void {
    if (this.selected === null) {
      this.selected = index;
    } else if (this.selected === index) {
      this.selected = null;
    } else {
      this.home = swapInLineup(this.home, this.selected, index);
      this.selected = null;
    }
    this.layoutTokens();
  }

  private cycleFormation(d: number): void {
    const i = FORMATIONS.findIndex((f) => f.id === this.home.formationId);
    const next = FORMATIONS[(i + d + FORMATIONS.length) % FORMATIONS.length];
    this.home = { ...this.home, formationId: next.id };
    this.layoutTokens();
  }

  private showInfo(p: PlayerData): void {
    this.info.removeAll(true);
    const team = getTeam(this.home.teamId);
    const W = 700;
    const g = this.add.graphics();
    panelFrame(g, 0, 0, W, 370, 0x2f8a46);
    // franjas verdes como la ficha de IE3
    for (let i = 0; i < 10; i++) g.fillStyle(0xffffff, i % 2 ? 0.03 : 0).fillRect(4, 4 + i * 26, W - 8, 26);
    g.fillStyle(0x1f5f33).fillRoundedRect(150, 14, 420, 34, 6);
    g.fillStyle(ELEMENT_COLOR[p.element]).fillRoundedRect(W - 120, 14, 100, 34, 6);
    const portrait = this.add.image(20, 14, texKey.portrait(p.id)).setOrigin(0).setDisplaySize(112, 112);
    const name = text(this, 162, 18, p.name, 22);
    const lv = text(this, 556, 20, `Nv. ${p.level}`, 18, '#ffe28a').setOrigin(1, 0);
    const pos = text(this, W - 70, 31, `${p.position} · ${ELEMENT_LABEL[p.element]}`, 15).setOrigin(0.5);
    const fp = new StatBar(this, 162, 72, 'FP', COLORS.fp, 140);
    fp.set(p.fp, p.fp);
    const tp = new StatBar(this, 380, 72, 'TP', COLORS.tp, 140);
    tp.set(p.tp, p.tp);
    this.info.add([g, portrait, name, lv, pos, fp, tp]);

    STAT_LABELS.forEach(([key, label], i) => {
      const col = i < 4 ? 0 : 1;
      const row = i < 4 ? i : i - 4;
      const x = 162 + col * 230;
      const y = 100 + row * 26;
      this.info.add(text(this, x, y, label, 17, '#e8ffe8'));
      this.info.add(text(this, x + 180, y, String(p.stats[key]), 17).setOrigin(1, 0));
    });

    const moves = movesOf(p.moves);
    this.info.add(text(this, 20, 210, 'Supertécnicas', 16, '#ffe28a'));
    if (moves.length === 0) this.info.add(text(this, 20, 234, '—', 16));
    moves.forEach((m, i) => {
      const y = 234 + i * 24;
      const dot = this.add.graphics().fillStyle(ELEMENT_COLOR[m.element]).fillCircle(28, y + 10, 7);
      this.info.add(dot);
      this.info.add(text(this, 42, y, `${m.name}`, 16));
      this.info.add(text(this, 215, y + 2, `${MOVE_KIND_LABEL[m.kind]} · ${m.power} · TP ${m.tp}`, 13, '#d9f5d9'));
    });

    const desc = this.add.graphics();
    panelFrame(desc, 400, 206, W - 420, 150, 0x23477a);
    this.info.add(desc);
    this.info.add(
      text(this, 414, 216, p.description ?? `Jugador de ${team.name}.`, 15, '#ffffff', {
        wordWrap: { width: W - 450 },
        lineSpacing: 6,
      }),
    );
    this.info.add(text(this, 414, 330, team.name, 13, Phaser.Display.Color.IntegerToColor(hex(team.colors.shirt)).lighten(40).rgba));
  }

  private play(): void {
    this.scene.start('match', { home: this.home, away: this.away });
  }
}
