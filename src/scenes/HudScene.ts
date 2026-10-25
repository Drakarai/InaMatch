import Phaser from 'phaser';
import { COLORS, FIELD_VIEW, FONT, GOAL_W, HALF_GAME_MINUTES, HALF_REAL_SECONDS, PANEL, PITCH, hex } from '../config';
import { ELEMENT_COLOR, elementMultiplier } from '../data/elements';
import type { MoveData } from '../data/types';
import {
  BASIC_LABEL,
  BASIC_OPTIONS,
  FIRED_UP_SECONDS,
  SHOT_POWER_LEVELS,
  SITUATION_MOVE_KIND,
  type Choice,
  type Situation,
} from '../engine/rules';
import { texKey } from '../gfx/placeholders';
import type { MatchPlayer } from '../match/MatchPlayer';
import { Button, StatBar, panelFrame, text } from '../ui/widgets';
import type { MatchScene } from './MatchScene';

// Dígitos 5x7 del marcador de leds
const LED_DIGITS: Record<string, string[]> = {
  '0': ['01110', '10001', '10011', '10101', '11001', '10001', '01110'],
  '1': ['00100', '01100', '00100', '00100', '00100', '00100', '01110'],
  '2': ['01110', '10001', '00001', '00010', '00100', '01000', '11111'],
  '3': ['11111', '00010', '00100', '00010', '00001', '10001', '01110'],
  '4': ['00010', '00110', '01010', '10010', '11111', '00010', '00010'],
  '5': ['11111', '10000', '11110', '00001', '00001', '10001', '01110'],
  '6': ['00110', '01000', '10000', '11110', '10001', '10001', '01110'],
  '7': ['11111', '00001', '00010', '00100', '01000', '01000', '01000'],
  '8': ['01110', '10001', '10001', '01110', '10001', '10001', '01110'],
  '9': ['01110', '10001', '10001', '01111', '00001', '00010', '01100'],
};

const PROMPT_TITLE: Record<Situation, string> = {
  attack: '¡Supera al rival!',
  defend: '¡Recupera el balón!',
  shoot: '¡Elige el tiro!',
  keep: '¡Para el tiro!',
  block: '¡Bloquea el tiro!',
};

/** Datos extra del panel de duelo: "Poder" de cada uno y compañeros que ayudan. */
export interface DuelInfo {
  power?: [number, number];
  support?: [number, number];
  /** compañeros que ayudan y además comparten afinidad ("¡Bonus de afinidad!") */
  affinity?: [number, number];
}

const PROMPT_SECONDS = 7;

interface DuelRow {
  container: Phaser.GameObjects.Container;
  portrait: Phaser.GameObjects.Image;
  name: Phaser.GameObjects.Text;
  fp: StatBar;
  tp: StatBar;
  ball: Phaser.GameObjects.Image;
  power: Phaser.GameObjects.Text;
  support: Phaser.GameObjects.Text;
  elem: Phaser.GameObjects.Graphics;
}

export class HudScene extends Phaser.Scene {
  private match!: MatchScene;
  private clockText!: Phaser.GameObjects.Text;
  private halfText!: Phaser.GameObjects.Text;
  private led!: Phaser.GameObjects.Graphics;
  private scorers: Phaser.GameObjects.Text[] = [];
  private rows: DuelRow[] = [];
  private infoTitle!: Phaser.GameObjects.Text;
  private infoMoves!: Phaser.GameObjects.Text;
  private duelPair: [MatchPlayer, MatchPlayer] | null = null;
  private duelInfo: DuelInfo = {};
  private tension!: Phaser.GameObjects.Graphics;
  private firedLabels: Phaser.GameObjects.Text[] = [];
  private radar!: Phaser.GameObjects.Graphics;
  private toastText!: Phaser.GameObjects.Text;
  private shootButton!: Button;
  private lastScore = '';
  private overlay: Phaser.GameObjects.Container | null = null;

  constructor() {
    super('hud');
  }

  init(data: { match: MatchScene }): void {
    this.match = data.match;
    this.duelPair = null;
    this.duelInfo = {};
    this.firedLabels = [];
    this.overlay = null;
    this.lastScore = '';
    this.scorers = [];
    this.rows = [];
  }

  create(): void {
    this.buildScoreboard();
    this.buildPlayerPanel();
    this.buildRadar();
    this.toastText = text(this, FIELD_VIEW.w / 2, 70, '', 26, '#ffffff', { strokeThickness: 6 }).setOrigin(0.5).setDepth(50);
    new Button(this, FIELD_VIEW.w - 40, 34, 'II', () => this.match.togglePause(), { w: 48, h: 40, size: 18, color: 0x51647d });
    this.input.keyboard?.on('keydown-ESC', () => this.match.togglePause());
    // la portería no siempre se ve: botón (y tecla T) para tirar a distancia
    this.shootButton = new Button(this, FIELD_VIEW.w / 2, FIELD_VIEW.h - 40, 'Tirar  (T)', () => this.match.requestShot(), {
      w: 200,
      h: 48,
      color: COLORS.uiRed,
    }).setDepth(30);
    this.input.keyboard?.on('keydown-T', () => this.match.requestShot());
    this.match.onHudReady();
  }

  // ---------------------------------------------------------------- marcador

  private buildScoreboard(): void {
    const { x, w } = PANEL;
    const [home, away] = this.match.teams;
    const g = this.add.graphics();
    g.fillStyle(COLORS.panelDark).fillRect(x, 0, w, PANEL.h);
    panelFrame(g, x + 10, 10, w - 20, 250);
    // franja central y "VS" de fondo
    g.fillStyle(0x234a7c).fillRect(x + w / 2 - 18, 14, 36, 242);
    text(this, x + w / 2, 110, 'VS', 64, '#3a6aa5', { strokeThickness: 0 }).setOrigin(0.5).setAlpha(0.8);
    // reloj
    g.fillStyle(0x10151f).fillRoundedRect(x + w / 2 - 80, 16, 160, 56, 10);
    g.lineStyle(2, 0x8a9bb5).strokeRoundedRect(x + w / 2 - 80, 16, 160, 56, 10);
    this.halfText = text(this, x + w / 2, 21, '1ª', 13, '#ffcf6a').setOrigin(0.5, 0);
    this.clockText = text(this, x + w / 2, 50, '00:00', 30, '#ffffff', { strokeThickness: 0 }).setOrigin(0.5);
    // escudos y nombres
    this.add.image(x + 70, 60, texKey.emblem(home.id)).setDisplaySize(52, 52);
    this.add.image(x + w - 70, 60, texKey.emblem(away.id)).setDisplaySize(52, 52);
    g.fillStyle(hex(home.colors.accent)).fillRect(x + 14, 96, w / 2 - 22, 26);
    g.fillStyle(hex(away.colors.accent)).fillRect(x + w / 2 + 8, 96, w / 2 - 22, 26);
    text(this, x + w / 4 + 2, 109, home.name, 15).setOrigin(0.5);
    text(this, x + (3 * w) / 4 - 2, 109, away.name, 15).setOrigin(0.5);
    // leds
    g.fillStyle(0x0b0d12).fillRoundedRect(x + 24, 130, w / 2 - 46, 84, 6);
    g.fillStyle(0x0b0d12).fillRoundedRect(x + w / 2 + 22, 130, w / 2 - 46, 84, 6);
    this.led = this.add.graphics();
    this.scorers = [
      text(this, x + 26, 218, '', 11, '#cfe0ff'),
      text(this, x + w / 2 + 24, 218, '', 11, '#cfe0ff'),
    ];
    // tensión del equipo (FIRED UP de IE3)
    this.tension = this.add.graphics();
    this.firedLabels = [0, 1].map((i) =>
      text(this, i === 0 ? x + w / 4 + 1 : x + (3 * w) / 4 - 1, 243, 'FIRED UP', 12, '#ffffff').setOrigin(0.5).setVisible(false),
    );
  }

  private drawTension(): void {
    const { x, w } = PANEL;
    const g = this.tension.clear();
    for (const side of [0, 1] as const) {
      const bx = side === 0 ? x + 24 : x + w / 2 + 22;
      const bw = w / 2 - 46;
      const fired = this.match.firedLeft(side);
      g.fillStyle(0x0b0d12).fillRoundedRect(bx, 236, bw, 14, 4);
      if (fired > 0) {
        const blink = Math.floor(this.time.now / 150) % 2 === 0;
        g.fillStyle(blink ? 0xff3b2f : 0xff8a1f).fillRoundedRect(bx + 1, 237, (bw - 2) * (fired / FIRED_UP_SECONDS), 12, 4);
      } else {
        g.fillStyle(0xe8892b).fillRoundedRect(bx + 1, 237, (bw - 2) * (this.match.tension[side] / 100), 12, 4);
      }
      this.firedLabels[side].setVisible(fired > 0);
    }
  }

  private drawLed(value: number, cx: number, cy: number): void {
    const digits = String(Math.min(99, value));
    const cell = 7.5;
    const dw = cell * 5 + 8;
    const startX = cx - (digits.length * dw - 8) / 2;
    [...digits].forEach((d, i) => {
      LED_DIGITS[d].forEach((row, r) => {
        [...row].forEach((bit, c) => {
          this.led.fillStyle(bit === '1' ? COLORS.led : COLORS.ledOff);
          this.led.fillRect(startX + i * dw + c * cell, cy - 26 + r * cell, cell - 1.5, cell - 1.5);
        });
      });
    });
  }

  // ------------------------------------------------- ficha / panel de duelo

  private buildPlayerPanel(): void {
    const { x, w } = PANEL;
    const g = this.add.graphics();
    panelFrame(g, x + 10, 270, w - 20, 190, 0x2a5d97);
    for (let i = 0; i < 2; i++) {
      const y = 280 + i * 88;
      const c = this.add.container(x + 20, y);
      const band = this.add.graphics();
      const portrait = this.add.image(0, 0, '__WHITE').setOrigin(0).setDisplaySize(72, 72);
      const name = text(this, 84, 2, '', 16);
      const fp = new StatBar(this, 84, 36, 'FP', COLORS.fp, 210);
      const tp = new StatBar(this, 84, 58, 'TP', COLORS.tp, 210);
      const ball = this.add.image(w - 52, 36, 'ball').setScale(1.6);
      const power = text(this, w - 34, 11, '', 15, '#ffe28a').setOrigin(1, 0.5);
      const support = text(this, 0, 74, '', 12, '#9fffb0');
      const elem = this.add.graphics();
      c.add([band, portrait, name, fp, tp, ball, power, support, elem]);
      this.rows.push({ container: c, portrait, name, fp, tp, ball, power, support, elem });
    }
    this.infoTitle = text(this, x + 22, 364, '', 13, '#ffe28a');
    this.infoMoves = text(this, x + 22, 382, '', 13, '#ffffff', { lineSpacing: 2 });
  }

  showDuel(a: MatchPlayer, b: MatchPlayer, info: DuelInfo = {}): void {
    this.duelPair = [a, b];
    this.duelInfo = info;
  }

  hideDuel(): void {
    this.duelPair = null;
    this.duelInfo = {};
  }

  private refreshPlayerPanel(): void {
    const pair = this.duelPair;
    const focus = this.match.focusPlayer();
    const shown: (MatchPlayer | null)[] = pair ? [...pair] : [focus, null];
    shown.forEach((p, i) => {
      const row = this.rows[i];
      row.container.setVisible(!!p);
      if (!p) return;
      const key = texKey.portrait(p.data.id);
      if (row.portrait.texture.key !== key) row.portrait.setTexture(key).setDisplaySize(72, 72);
      const band = row.container.list[0] as Phaser.GameObjects.Graphics;
      band.clear().fillStyle(p.side === 0 ? 0x2d5fb8 : 0xa8283a, 0.9).fillRoundedRect(76, -2, PANEL.w - 104, 26, 6);
      row.name.setText(`${p.data.number}  ${p.data.name}`);
      row.fp.set(p.fp, p.maxFp);
      row.tp.set(p.tp, p.maxTp);
      row.ball.setVisible(this.match.ballOwner() === p);
      const power = pair ? this.duelInfo.power?.[i] : undefined;
      row.power.setText(power !== undefined ? `Poder ${power}` : '');
      // afinidad del jugador en la esquina del retrato; flecha si gana la afinidad al rival
      const rival = pair ? pair[1 - i] : null;
      const favoured = rival ? elementMultiplier(p.data.element, rival.data.element) > 1 : false;
      row.elem.clear().fillStyle(ELEMENT_COLOR[p.data.element]).fillCircle(66, 66, 9).lineStyle(2, 0xffffff).strokeCircle(66, 66, 9);
      if (favoured) row.elem.fillStyle(0xffe28a).fillTriangle(60, 52, 72, 52, 66, 44);
      const support = pair ? (this.duelInfo.support?.[i] ?? 0) : 0;
      const affinity = pair ? (this.duelInfo.affinity?.[i] ?? 0) : 0;
      row.support.setText(affinity > 0 ? `¡Bonus de afinidad x${affinity}!` : support > 0 ? `¡Apoyo x${support}!` : '');
    });
    const showInfo = !pair && !!focus;
    this.infoTitle.setVisible(showInfo);
    this.infoMoves.setVisible(showInfo);
    if (showInfo && focus) {
      this.infoTitle.setText('Supertécnicas');
      this.infoMoves.setText(focus.moves.length ? focus.moves.map((m) => `• ${m.name}  (TP ${m.tp})`).join('\n') : '—');
    }
  }

  // ------------------------------------------------------------------ radar

  private buildRadar(): void {
    const { x, w } = PANEL;
    const g = this.add.graphics();
    panelFrame(g, x + 10, 470, w - 20, 240, COLORS.panelDark);
    text(this, x + 22, 476, 'Radar', 13, '#b9d0ee');
    this.radar = this.add.graphics();
  }

  private drawRadar(): void {
    const r = this.radar.clear();
    // el campo se dibuja girado: la portería rival queda a la derecha
    const box = { x: PANEL.x + 40, y: 500, w: PANEL.w - 80, h: 196 };
    const sx = box.w / PITCH.h;
    const sy = box.h / PITCH.w;
    const toRadar = (wx: number, wy: number) => ({
      x: box.x + (PITCH.y + PITCH.h - wy) * sx,
      y: box.y + (wx - PITCH.x) * sy,
    });
    r.fillStyle(0x3d9b4c).fillRect(box.x, box.y, box.w, box.h);
    r.lineStyle(1, 0xffffff, 0.7).strokeRect(box.x, box.y, box.w, box.h);
    r.lineBetween(box.x + box.w / 2, box.y, box.x + box.w / 2, box.y + box.h);
    r.strokeCircle(box.x + box.w / 2, box.y + box.h / 2, 18);
    const goalH = GOAL_W * sy;
    r.fillStyle(0xffffff).fillRect(box.x - 4, box.y + box.h / 2 - goalH / 2, 4, goalH).fillRect(box.x + box.w, box.y + box.h / 2 - goalH / 2, 4, goalH);
    // vista de la cámara
    const view = this.match.cameras.main.worldView;
    const a = toRadar(view.x, view.y + view.height);
    const b = toRadar(view.x + view.width, view.y);
    r.lineStyle(1, 0xffe28a, 0.8).strokeRect(Math.max(box.x, a.x), Math.max(box.y, a.y), Math.min(box.x + box.w, b.x) - Math.max(box.x, a.x), Math.min(box.y + box.h, b.y) - Math.max(box.y, a.y));
    for (const p of this.match.allPlayers()) {
      const pt = toRadar(p.x, p.y);
      r.fillStyle(p.side === 0 ? 0x4fa3ff : 0xff5a6a).fillCircle(pt.x, pt.y, p.isGK ? 4 : 3.5);
    }
    const ball = this.match.ballPos();
    const bp = toRadar(ball.x, ball.y);
    r.fillStyle(0xffffff).fillCircle(bp.x, bp.y, 3);
    r.lineStyle(1, 0x000000).strokeCircle(bp.x, bp.y, 3);
  }

  // -------------------------------------------------------------- update

  update(): void {
    const half = this.match.half;
    const secs = (this.match.clock / HALF_REAL_SECONDS) * HALF_GAME_MINUTES * 60 + (half - 1) * HALF_GAME_MINUTES * 60;
    const mm = Math.floor(secs / 60);
    const ss = Math.floor(secs % 60);
    this.clockText.setText(`${String(mm).padStart(2, '0')}:${String(ss).padStart(2, '0')}`);
    this.halfText.setText(half === 1 ? '1ª parte' : '2ª parte');

    const scoreKey = this.match.score.join('-') + this.match.goals.length;
    if (scoreKey !== this.lastScore) {
      this.lastScore = scoreKey;
      this.led.clear();
      this.drawLed(this.match.score[0], PANEL.x + PANEL.w / 4 + 1, 172);
      this.drawLed(this.match.score[1], PANEL.x + (3 * PANEL.w) / 4 - 1, 172);
      for (const side of [0, 1] as const) {
        this.scorers[side].setText(
          this.match.goals
            .filter((g) => g.side === side)
            .slice(-2)
            .map((g) => `${g.minute}' ${g.name}`)
            .join('   '),
        );
      }
    }
    this.refreshPlayerPanel();
    this.drawRadar();
    this.drawTension();
    this.shootButton.setVisible(this.match.canShoot());
  }

  // ------------------------------------------------------------ comandos

  /**
   * Barra de comandos sobre el campo: título, botones, teclas y cuenta atrás.
   * `setup` coloca los botones y devuelve qué tecla elige qué opción.
   */
  private commandBar<T>(
    title: string,
    fallback: T,
    setup: (c: Phaser.GameObjects.Container, cy: number, finish: (value: T) => void) => Record<string, T>,
  ): Promise<T> {
    return new Promise((resolve) => {
      const c = this.add.container(0, 0).setDepth(40);
      const cy = FIELD_VIEW.h - 46;
      const g = this.add.graphics();
      g.fillStyle(0x0b1a2e, 0.55).fillRect(0, cy - 44, FIELD_VIEW.w, 100);
      c.add(g);
      c.add(text(this, FIELD_VIEW.w / 2, cy - 30, title, 20, '#ffffff').setOrigin(0.5));
      const timer = this.add.graphics();
      c.add(timer);

      let done = false;
      const finish = (value: T) => {
        if (done) return;
        done = true;
        this.input.keyboard?.off('keydown', onKey);
        tick.remove();
        c.destroy();
        resolve(value);
      };
      const keys = setup(c, cy, finish);
      const onKey = (ev: KeyboardEvent) => {
        if (ev.key in keys) finish(keys[ev.key]);
      };
      this.input.keyboard?.on('keydown', onKey);

      const start = this.time.now;
      const tick = this.time.addEvent({
        delay: 50,
        loop: true,
        callback: () => {
          const left = 1 - (this.time.now - start) / (PROMPT_SECONDS * 1000);
          timer.clear().fillStyle(0x000000, 0.5).fillRect(FIELD_VIEW.w / 2 - 150, cy - 14, 300, 6);
          timer.fillStyle(left < 0.3 ? 0xff5a4a : 0xffd23f).fillRect(FIELD_VIEW.w / 2 - 150, cy - 14, 300 * Math.max(0, left), 6);
          if (left <= 0) finish(fallback);
        },
      });
    });
  }

  /** Comandos de un duelo, tiro, bloqueo o parada: dos básicos y las supertécnicas. */
  prompt(situation: Situation, player: MatchPlayer): Promise<Choice> {
    const [a, b] = BASIC_OPTIONS[situation];
    const basicA: Choice = { type: 'basic', id: a };
    const basicB: Choice = { type: 'basic', id: b };
    return this.commandBar<Choice>(PROMPT_TITLE[situation], basicA, (c, cy, finish) => {
      // rojo al atacar, azul al defender, como los botones de IE3
      const defensive = situation === 'defend' || situation === 'keep' || situation === 'block';
      const color = defensive ? 0x2f6fc4 : 0xd8344a;
      c.add(new Button(this, 130, cy + 10, `1 · ${BASIC_LABEL[a]}`, () => finish(basicA), { w: 230, h: 50, color }));
      c.add(new Button(this, FIELD_VIEW.w - 130, cy + 10, `2 · ${BASIC_LABEL[b]}`, () => finish(basicB), { w: 230, h: 50, color }));

      const keys: Record<string, Choice> = { '1': basicA, '2': basicB };
      const kind = SITUATION_MOVE_KIND[situation];
      const moves = player.moves.filter((m) => m.kind === kind);
      moves.forEach((move, i) => {
        const ok = move.tp <= player.tp;
        const choice: Choice = { type: 'move', move };
        const btn = new Button(this, FIELD_VIEW.w / 2, cy + 10 - i * 54, `${i + 3} · ${move.name}`, () => finish(choice), {
          w: 270,
          h: 46,
          size: 18,
          color: ELEMENT_COLOR[move.element],
          sub: `TP ${move.tp}`,
        });
        btn.setEnabled(ok);
        c.add(btn);
        if (ok) keys[String(i + 3)] = choice;
      });
      if (moves.length === 0) c.add(text(this, FIELD_VIEW.w / 2, cy + 10, 'Sin supertécnicas', 15, '#9fb8d8').setOrigin(0.5));
      return keys;
    });
  }

  /** "¡Regula la potencia!" de GO: devuelve el nivel elegido (0 = normal). */
  promptPower(tpAvailable: number): Promise<number> {
    return this.commandBar<number>('¡Regula la potencia!', 0, (c, cy, finish) => {
      const keys: Record<string, number> = {};
      SHOT_POWER_LEVELS.forEach((level, i) => {
        const ok = level.tp <= tpAvailable;
        const btn = new Button(this, FIELD_VIEW.w / 2 + (i - 1) * 260, cy + 10, `${i + 1} · ${level.label}`, () => finish(i), {
          w: 240,
          h: 50,
          color: [0x4f7fb8, 0xe0862c, 0xd8344a][i],
          sub: level.tp ? `TP ${level.tp}` : undefined,
        });
        btn.setEnabled(ok);
        c.add(btn);
        if (ok) keys[String(i + 1)] = i;
      });
      return keys;
    });
  }

  /** Enseña el choque de potencias del duelo ("54 VS 37") sobre el campo. */
  showClash(left: number, right: number, leftWins: boolean, leftSide: 0 | 1): void {
    const c = this.add.container(FIELD_VIEW.w / 2, 150).setDepth(45);
    const colorOf = (side: 0 | 1) => (side === 0 ? '#7fc4ff' : '#ff8a8a');
    const rightSide: 0 | 1 = leftSide === 0 ? 1 : 0;
    const g = this.add.graphics();
    g.fillStyle(0x0b1a2e, 0.7).fillRoundedRect(-190, -34, 380, 68, 14);
    const l = text(this, -70, 0, String(left), leftWins ? 44 : 32, colorOf(leftSide), { strokeThickness: 7 }).setOrigin(0.5);
    const vs = text(this, 0, 0, 'VS', 22, '#ffe28a').setOrigin(0.5);
    const r = text(this, 70, 0, String(right), leftWins ? 32 : 44, colorOf(rightSide), { strokeThickness: 7 }).setOrigin(0.5);
    c.add([g, l, vs, r]);
    c.setScale(0.6);
    this.tweens.add({ targets: c, scale: 1, duration: 180, ease: 'Back.Out' });
    this.tweens.add({ targets: c, alpha: 0, delay: 1100, duration: 300, onComplete: () => c.destroy() });
  }

  // ------------------------------------------------- animación de técnica

  cutin(player: MatchPlayer, move: MoveData): Promise<void> {
    return new Promise((resolve) => {
      const W = FIELD_VIEW.w;
      const H = FIELD_VIEW.h;
      const color = ELEMENT_COLOR[move.element];
      const c = this.add.container(0, 0).setDepth(60);
      // que la animación no se salga del campo y tape el marcador
      const maskShape = this.make.graphics({}, false).fillStyle(0xffffff).fillRect(0, 0, W, H);
      c.setMask(maskShape.createGeometryMask());
      const shade = this.add.rectangle(W / 2, H / 2, W, H, 0x000000, 0).setInteractive();
      const burst = this.add.graphics({ x: W / 2, y: H / 2 });
      for (let i = 0; i < 24; i++) {
        const a0 = (i / 24) * Math.PI * 2;
        const a1 = a0 + Math.PI / 30;
        burst.fillStyle(i % 2 ? color : 0xffffff, i % 2 ? 0.55 : 0.18);
        burst.fillTriangle(0, 0, Math.cos(a0) * 900, Math.sin(a0) * 900, Math.cos(a1) * 900, Math.sin(a1) * 900);
      }
      burst.setAlpha(0);
      const band = this.add.graphics();
      band.fillStyle(0x0b1a2e, 0.85).fillPoints([
        { x: 0, y: H / 2 + 40 },
        { x: W, y: H / 2 - 30 },
        { x: W, y: H / 2 + 70 },
        { x: 0, y: H / 2 + 140 },
      ]);
      band.lineStyle(4, color).lineBetween(0, H / 2 + 40, W, H / 2 - 30).lineBetween(0, H / 2 + 140, W, H / 2 + 70);
      band.setAlpha(0);
      const portrait = this.add.image(-200, H / 2 - 70, texKey.portrait(player.data.id)).setDisplaySize(230, 230);
      const name = this.add
        .text(W + 400, H / 2 + 62, move.name, {
          fontFamily: FONT,
          fontSize: '52px',
          fontStyle: 'bold',
          color: '#ffffff',
          stroke: Phaser.Display.Color.IntegerToColor(color).darken(30).rgba,
          strokeThickness: 10,
        })
        .setOrigin(0.5)
        .setAngle(-4);
      const who = text(this, W - 30, H / 2 + 104, `${player.data.short} · TP -${move.tp}`, 18, '#ffe28a').setOrigin(1, 0.5).setAngle(-4).setAlpha(0);
      c.add([shade, burst, band, portrait, name, who]);

      let finished = false;
      const end = () => {
        if (finished) return;
        finished = true;
        this.tweens.add({
          targets: c,
          alpha: 0,
          duration: 180,
          onComplete: () => {
            c.destroy();
            maskShape.destroy();
            resolve();
          },
        });
      };
      shade.on('pointerdown', end);

      this.tweens.add({ targets: shade, fillAlpha: 0.7, duration: 150 });
      this.tweens.add({ targets: [burst, band], alpha: 1, duration: 200 });
      this.tweens.add({ targets: burst, angle: 40, duration: 1700 });
      this.tweens.add({ targets: portrait, x: 190, duration: 260, ease: 'Back.Out' });
      this.tweens.add({ targets: name, x: W / 2 + 60, duration: 300, delay: 120, ease: 'Back.Out' });
      this.tweens.add({ targets: who, alpha: 1, duration: 200, delay: 350 });
      this.cameras.main.flash(120, 255, 255, 255);
      this.time.delayedCall(1600, end);
    });
  }

  // ---------------------------------------------------- avisos y pantallas

  toast(msg: string, ms = 1300): void {
    this.toastText.setText(msg).setAlpha(1);
    this.tweens.killTweensOf(this.toastText);
    this.tweens.add({ targets: this.toastText, alpha: 0, delay: ms, duration: 300 });
  }

  banner(main: string, sub = '', color = '#ffd23f', ms = 1800): Promise<void> {
    return new Promise((resolve) => {
      const c = this.add.container(FIELD_VIEW.w / 2, FIELD_VIEW.h / 2).setDepth(70);
      const g = this.add.graphics();
      g.fillStyle(0x0b1a2e, 0.75).fillRect(-FIELD_VIEW.w / 2, -70, FIELD_VIEW.w, 140);
      const t = text(this, 0, sub ? -14 : 0, main, 76, color, { strokeThickness: 12, fontStyle: 'bold' }).setOrigin(0.5);
      c.add([g, t]);
      if (sub) c.add(text(this, 0, 44, sub, 22).setOrigin(0.5));
      t.setScale(2.2);
      this.tweens.add({ targets: t, scale: 1, duration: 300, ease: 'Back.Out' });
      this.time.delayedCall(ms, () => {
        this.tweens.add({ targets: c, alpha: 0, duration: 250, onComplete: () => (c.destroy(), resolve()) });
      });
    });
  }

  showPause(onResume: () => void, onQuit: () => void): void {
    this.hidePause();
    const c = this.add.container(0, 0).setDepth(80);
    c.add(this.add.rectangle(FIELD_VIEW.w / 2, FIELD_VIEW.h / 2, FIELD_VIEW.w, FIELD_VIEW.h, 0x000000, 0.6).setInteractive());
    c.add(text(this, FIELD_VIEW.w / 2, 230, 'Pausa', 56).setOrigin(0.5));
    c.add(new Button(this, FIELD_VIEW.w / 2, 340, 'Reanudar', onResume, { w: 260, h: 54 }));
    c.add(new Button(this, FIELD_VIEW.w / 2, 410, 'Abandonar partido', onQuit, { w: 260, h: 54, color: COLORS.uiRed }));
    c.add(
      text(
        this,
        FIELD_VIEW.w / 2,
        520,
        'Con balón: arrastra desde tu jugador para regatear, pulsa a un compañero\npara pasar, pulsa un hueco para pase al espacio y la portería (o T) para tirar.\nSin balón: arrastra a cualquier jugador o pulsa en el campo.',
        16,
        '#d8e8ff',
        { align: 'center', lineSpacing: 6 },
      ).setOrigin(0.5),
    );
    this.overlay = c;
  }

  hidePause(): void {
    this.overlay?.destroy();
    this.overlay = null;
  }

  showResult(onRematch: () => void, onMenu: () => void): void {
    const [home, away] = this.match.teams;
    const [a, b] = this.match.score;
    const c = this.add.container(0, 0).setDepth(90);
    c.add(this.add.rectangle(FIELD_VIEW.w / 2, FIELD_VIEW.h / 2, FIELD_VIEW.w, FIELD_VIEW.h, 0x000000, 0.7).setInteractive());
    const g = this.add.graphics();
    panelFrame(g, FIELD_VIEW.w / 2 - 300, 150, 600, 400);
    c.add(g);
    c.add(text(this, FIELD_VIEW.w / 2, 200, 'Final del partido', 36, '#ffe28a').setOrigin(0.5));
    c.add(text(this, FIELD_VIEW.w / 2, 300, `${a}  -  ${b}`, 72).setOrigin(0.5));
    c.add(text(this, FIELD_VIEW.w / 2 - 170, 300, home.name, 20).setOrigin(0.5));
    c.add(text(this, FIELD_VIEW.w / 2 + 170, 300, away.name, 20).setOrigin(0.5));
    const verdict = a > b ? '¡Victoria!' : a < b ? 'Derrota...' : 'Empate';
    c.add(text(this, FIELD_VIEW.w / 2, 380, verdict, 30, a > b ? '#7dff9a' : a < b ? '#ff8a8a' : '#ffffff').setOrigin(0.5));
    c.add(new Button(this, FIELD_VIEW.w / 2 - 130, 480, 'Revancha', onRematch, { w: 220, h: 54 }));
    c.add(new Button(this, FIELD_VIEW.w / 2 + 130, 480, 'Menú', onMenu, { w: 220, h: 54, color: 0x51647d }));
  }
}
