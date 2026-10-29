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
import { fxColors, fxParticle, type FxRecipe } from '../gfx/fx';
import { portraitKey, texKey } from '../gfx/placeholders';
import type { MatchPlayer } from '../match/MatchPlayer';
import { THEME, dim, pt, sectionTitle, slant, themePanel } from '../ui/theme';
import { Button, StatBar, text } from '../ui/widgets';
import type { MatchScene } from './MatchScene';

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
  private scoreTexts: Phaser.GameObjects.Text[] = [];
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
    this.scoreTexts = [];
    this.rows = [];
  }

  create(): void {
    this.buildScoreboard();
    this.buildPlayerPanel();
    this.buildRadar();
    this.toastText = text(this, FIELD_VIEW.w / 2, 70, '', 26, '#ffffff', { strokeThickness: 6, fontStyle: 'italic bold' }).setOrigin(0.5).setDepth(50);
    new Button(this, FIELD_VIEW.w - 42, 34, 'II', () => this.match.togglePause(), { w: 54, h: 40, size: 18, color: THEME.panelLight });
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
    g.fillStyle(THEME.night).fillRect(x, 0, w, PANEL.h);
    // mitades con el color de cada equipo, partidas por un rayo
    const split = [pt(x + w * 0.56, 0), pt(x + w * 0.5, 120), pt(x + w * 0.54, 128), pt(x + w * 0.46, 240)];
    g.fillStyle(dim(home.colors.shirt)).fillPoints([pt(x, 0), ...split, pt(x, 240)], true);
    g.fillStyle(dim(away.colors.shirt)).fillPoints([pt(x + w, 0), ...split, pt(x + w, 240)], true);
    g.lineStyle(10, THEME.yellow, 0.25).strokePoints(split, false);
    g.lineStyle(3, 0xfff6c8).strokePoints(split, false);
    g.fillGradientStyle(0x000000, 0x000000, 0x000000, 0x000000, 0, 0, 0.6, 0.6).fillRect(x, 150, w, 90);
    g.fillStyle(THEME.yellow).fillRect(x, 240, w, 3);
    // reloj en una placa inclinada
    g.fillStyle(0x000000, 0.75).fillPoints(slant(x + w / 2 - 78, 10, 156, 48, 12), true);
    g.lineStyle(2, THEME.yellow).strokePoints(slant(x + w / 2 - 78, 10, 156, 48, 12), true);
    this.halfText = text(this, x + w / 2, 21, '1ª PARTE', 11, '#ffd23f', { fontStyle: 'bold' }).setOrigin(0.5);
    this.clockText = text(this, x + w / 2, 41, '00:00', 24, '#ffffff', { fontStyle: 'italic bold', strokeThickness: 0 }).setOrigin(0.5);
    // escudos y goles
    this.add.image(x + 62, 96, texKey.emblem(home.id)).setDisplaySize(76, 76);
    this.add.image(x + w - 62, 96, texKey.emblem(away.id)).setDisplaySize(76, 76);
    this.scoreTexts = [-1, 1].map((d) =>
      text(this, x + w / 2 + d * 62, 100, '0', 64, '#ffffff', { fontStyle: 'italic bold', strokeThickness: 8 }).setOrigin(0.5),
    );
    text(this, x + w / 2, 100, '-', 34, '#ffd23f', { fontStyle: 'bold', strokeThickness: 5 }).setOrigin(0.5);
    // nombres en bandas blancas inclinadas
    for (const [i, team] of [home, away].entries()) {
      const bx = i === 0 ? x + 12 : x + w / 2 + 6;
      const bw = w / 2 - 18;
      g.fillStyle(0xffffff).fillPoints(slant(bx, 146, bw, 26, 8), true);
      g.fillStyle(hex(team.colors.accent)).fillPoints(slant(bx - 1, 170, bw - 6, 4, 1), true);
      fitWidth(text(this, bx + bw / 2, 159, team.name, 15, THEME.ink, { fontStyle: 'italic bold', strokeThickness: 0 }).setOrigin(0.5), bw - 26, 10);
    }
    this.scorers = [
      text(this, x + 16, 184, '', 11, '#e3e9f2', { fontStyle: 'italic' }),
      text(this, x + w / 2 + 10, 184, '', 11, '#e3e9f2', { fontStyle: 'italic' }),
    ];
    // tensión del equipo (FIRED UP de IE3)
    text(this, x + w / 2, 216, 'TENSIÓN', 10, THEME.muted, { fontStyle: 'bold', strokeThickness: 0 }).setOrigin(0.5);
    this.tension = this.add.graphics();
    this.firedLabels = [0, 1].map((i) =>
      text(this, i === 0 ? x + w / 4 : x + (3 * w) / 4, 217, '¡FIRED UP!', 13, '#ffffff', { fontStyle: 'italic bold' }).setOrigin(0.5).setVisible(false),
    );
  }

  private drawTension(): void {
    const { x, w } = PANEL;
    const g = this.tension.clear();
    for (const side of [0, 1] as const) {
      const bw = w / 2 - 54;
      const bx = side === 0 ? x + 16 : x + w / 2 + 38;
      const fired = this.match.firedLeft(side);
      g.fillStyle(0x000000, 0.6).fillPoints(slant(bx, 210, bw, 14, 5), true);
      const ratio = fired > 0 ? fired / FIRED_UP_SECONDS : this.match.tension[side] / 100;
      const blink = Math.floor(this.time.now / 150) % 2 === 0;
      const color = fired > 0 ? (blink ? 0xff3b2f : THEME.yellow) : 0xff8a1f;
      if (ratio > 0) g.fillStyle(color).fillPoints(slant(bx + 1, 211, Math.max(8, (bw - 2) * ratio), 12, 4), true);
      this.firedLabels[side].setVisible(fired > 0);
    }
  }

  // ------------------------------------------------- ficha / panel de duelo

  private buildPlayerPanel(): void {
    const { x, w } = PANEL;
    const g = this.add.graphics();
    themePanel(g, x + 10, 254, w - 20, 206);
    for (let i = 0; i < 2; i++) {
      const y = 268 + i * 92;
      const c = this.add.container(x + 20, y);
      const band = this.add.graphics();
      const portrait = this.add.image(0, 0, '__WHITE').setOrigin(0).setDisplaySize(72, 72);
      const name = text(this, 92, 2, '', 16, '#ffffff', { fontStyle: 'italic bold' });
      const fp = new StatBar(this, 84, 36, 'FP', COLORS.fp, 210);
      const tp = new StatBar(this, 84, 58, 'TP', COLORS.tp, 210);
      const ball = this.add.image(w - 52, 36, 'ball').setScale(1.6);
      const power = text(this, w - 34, 11, '', 15, '#ffd23f', { fontStyle: 'italic bold' }).setOrigin(1, 0.5);
      const support = text(this, 0, 76, '', 12, '#9fffb0', { fontStyle: 'italic bold' });
      const elem = this.add.graphics();
      c.add([band, portrait, name, fp, tp, ball, power, support, elem]);
      this.rows.push({ container: c, portrait, name, fp, tp, ball, power, support, elem });
    }
    this.infoTitle = text(this, x + 26, 360, '', 13, '#ffd23f', { fontStyle: 'italic bold' });
    this.infoMoves = text(this, x + 26, 378, '', 13, '#ffffff', { lineSpacing: 2 });
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
      const key = portraitKey(this, p.data, p.team);
      if (row.portrait.texture.key !== key) row.portrait.setTexture(key).setDisplaySize(72, 72);
      const band = row.container.list[0] as Phaser.GameObjects.Graphics;
      const sideColor = p.side === 0 ? THEME.home : THEME.away;
      band.clear().fillStyle(sideColor).fillPoints(slant(-4, -4, 82, 80, 12), true);
      band.fillStyle(sideColor, 0.85).fillPoints(slant(80, -2, PANEL.w - 112, 26, 8), true);
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
    themePanel(g, x + 10, 472, w - 20, 238);
    sectionTitle(this, x + 24, 490, 'Radar');
    this.radar = this.add.graphics();
  }

  private drawRadar(): void {
    const r = this.radar.clear();
    // el campo se dibuja girado: la portería rival queda a la derecha
    const box = { x: PANEL.x + 40, y: 508, w: PANEL.w - 80, h: 186 };
    const sx = box.w / PITCH.h;
    const sy = box.h / PITCH.w;
    const toRadar = (wx: number, wy: number) => ({
      x: box.x + (PITCH.y + PITCH.h - wy) * sx,
      y: box.y + (wx - PITCH.x) * sy,
    });
    for (let i = 0; i < 8; i++) r.fillStyle(i % 2 ? 0x1f6b3a : 0x247a43).fillRect(box.x + (i * box.w) / 8, box.y, box.w / 8, box.h);
    r.lineStyle(1, 0xffffff, 0.55).strokeRect(box.x, box.y, box.w, box.h);
    r.lineBetween(box.x + box.w / 2, box.y, box.x + box.w / 2, box.y + box.h);
    r.strokeCircle(box.x + box.w / 2, box.y + box.h / 2, 18);
    const goalH = GOAL_W * sy;
    r.fillStyle(0xffffff).fillRect(box.x - 4, box.y + box.h / 2 - goalH / 2, 4, goalH).fillRect(box.x + box.w, box.y + box.h / 2 - goalH / 2, 4, goalH);
    // vista de la cámara
    const view = this.match.cameras.main.worldView;
    const a = toRadar(view.x, view.y + view.height);
    const b = toRadar(view.x + view.width, view.y);
    r.lineStyle(2, THEME.yellow, 0.9).strokeRect(Math.max(box.x, a.x), Math.max(box.y, a.y), Math.min(box.x + box.w, b.x) - Math.max(box.x, a.x), Math.min(box.y + box.h, b.y) - Math.max(box.y, a.y));
    for (const p of this.match.allPlayers()) {
      const pt = toRadar(p.x, p.y);
      r.fillStyle(p.side === 0 ? THEME.home : THEME.away).fillCircle(pt.x, pt.y, p.isGK ? 4.5 : 4);
      r.lineStyle(1, 0xffffff, 0.9).strokeCircle(pt.x, pt.y, p.isGK ? 4.5 : 4);
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
    this.halfText.setText(half === 1 ? '1ª PARTE' : '2ª PARTE');

    const scoreKey = this.match.score.join('-') + this.match.goals.length;
    if (scoreKey !== this.lastScore) {
      this.lastScore = scoreKey;
      this.scoreTexts.forEach((t, i) => t.setText(String(this.match.score[i])));
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
    const canShoot = this.match.canShoot();
    this.shootButton.setVisible(canShoot);
    if (canShoot) this.shootButton.setCaption(this.match.shotIsLong() ? 'Tiro largo  (T)' : 'Tirar  (T)');
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
      g.fillGradientStyle(THEME.night, THEME.night, THEME.night, THEME.night, 0, 0, 0.85, 0.85).fillRect(0, cy - 80, FIELD_VIEW.w, 136);
      g.fillStyle(THEME.yellow).fillPoints(slant(FIELD_VIEW.w / 2 - 150, cy - 46, 300, 30, 10), true);
      c.add(g);
      c.add(text(this, FIELD_VIEW.w / 2, cy - 31, title, 18, THEME.ink, { fontStyle: 'italic bold', strokeThickness: 0 }).setOrigin(0.5));
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
          timer.clear().fillStyle(0x000000, 0.6).fillRect(FIELD_VIEW.w / 2 - 140, cy - 13, 280, 5);
          timer.fillStyle(left < 0.3 ? 0xff5a4a : 0xffffff).fillRect(FIELD_VIEW.w / 2 - 140, cy - 13, 280 * Math.max(0, left), 5);
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

  /** Tiro desde lejos: solo las supertécnicas de tiro largo, o cancelar (null). */
  promptLongShot(moves: MoveData[]): Promise<Choice | null> {
    return this.commandBar<Choice | null>('¡Tiro largo!', null, (c, cy, finish) => {
      c.add(new Button(this, 130, cy + 10, '1 · Cancelar', () => finish(null), { w: 230, h: 50, color: THEME.panelLight }));
      const keys: Record<string, Choice | null> = { '1': null };
      moves.forEach((move, i) => {
        const choice: Choice = { type: 'move', move };
        c.add(
          new Button(this, FIELD_VIEW.w / 2 + 60, cy + 10 - i * 54, `${i + 2} · ${move.name}`, () => finish(choice), {
            w: 290,
            h: 46,
            size: 18,
            color: ELEMENT_COLOR[move.element],
            sub: `TP ${move.tp}`,
          }),
        );
        keys[String(i + 2)] = choice;
      });
      return keys;
    });
  }

  /** "¡Regula la potencia!" de GO, solo para tiros normales: devuelve el nivel elegido (0 = normal). */
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
    g.fillStyle(0x000000, 0.5).fillPoints(slant(-196, -30, 400, 68, 18), true);
    g.fillStyle(THEME.night, 0.9).fillPoints(slant(-200, -34, 400, 68, 18), true);
    g.lineStyle(2, THEME.yellow).strokePoints(slant(-200, -34, 400, 68, 18), true);
    const l = text(this, -76, 0, String(left), leftWins ? 46 : 32, colorOf(leftSide), { fontStyle: 'italic bold', strokeThickness: 7 }).setOrigin(0.5);
    const vs = text(this, 0, 0, 'VS', 24, '#ffd23f', { fontStyle: 'italic bold', strokeThickness: 5 }).setOrigin(0.5);
    const r = text(this, 76, 0, String(right), leftWins ? 32 : 46, colorOf(rightSide), { fontStyle: 'italic bold', strokeThickness: 7 }).setOrigin(0.5);
    c.add([g, l, vs, r]);
    c.setScale(0.6);
    this.tweens.add({ targets: c, scale: 1, duration: 180, ease: 'Back.Out' });
    this.tweens.add({ targets: c, alpha: 0, delay: 1100, duration: 300, onComplete: () => c.destroy() });
  }

  // ------------------------------------------------- animación de técnica

  cutin(player: MatchPlayer, move: MoveData, fx: FxRecipe = { fx: 'impact' }): Promise<void> {
    return new Promise((resolve) => {
      const W = FIELD_VIEW.w;
      const H = FIELD_VIEW.h;
      // el color y las partículas son los del efecto de la técnica (llamas, copos, pétalos...)
      const [color, color2] = fxColors(fx, move.element);
      const c = this.add.container(0, 0).setDepth(60);
      // que la animación no se salga del campo y tape el marcador
      const maskShape = this.make.graphics({}, false).fillStyle(0xffffff).fillRect(0, 0, W, H);
      c.setMask(maskShape.createGeometryMask());
      const shade = this.add.rectangle(W / 2, H / 2, W, H, 0x000000, 0).setInteractive();
      const burst = this.add.graphics({ x: W / 2, y: H / 2 });
      for (let i = 0; i < 24; i++) {
        const a0 = (i / 24) * Math.PI * 2;
        const a1 = a0 + Math.PI / 30;
        burst.fillStyle(i % 2 ? color : color2, i % 2 ? 0.55 : 0.22);
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
      const portrait = this.add.image(-200, H / 2 - 70, portraitKey(this, player.data, player.team)).setDisplaySize(230, 230);
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
      const part = fxParticle(fx);
      const shower = this.add.particles(0, 0, part.key, {
        x: { min: 0, max: W },
        y: { min: -20, max: H },
        speedX: { min: -260, max: -120 },
        speedY: { min: -40, max: 80 },
        scale: { start: part.key === 'fx-glow' ? 1.6 : part.key === 'fx-penguin' ? 1.6 : 1.4, end: 0.3 },
        alpha: { start: 0.9, end: 0 },
        rotate: { min: 0, max: 360 },
        tint: part.key === 'fx-penguin' ? 0xffffff : [color, color2],
        lifespan: 1200,
        frequency: part.key === 'fx-penguin' ? 90 : 20,
        quantity: 2,
        blendMode: part.additive ? 'ADD' : 'NORMAL',
      });
      c.add([shade, burst, shower, band, portrait, name, who]);

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
      const half = FIELD_VIEW.w / 2;
      g.fillStyle(THEME.night, 0.85).fillPoints([pt(-half, -60), pt(half, -86), pt(half, 60), pt(-half, 86)], true);
      g.fillStyle(THEME.yellow).fillPoints([pt(-half, -60), pt(half, -86), pt(half, -80), pt(-half, -54)], true);
      g.fillStyle(THEME.yellow).fillPoints([pt(-half, 80), pt(half, 54), pt(half, 60), pt(-half, 86)], true);
      const t = text(this, 0, sub ? -14 : 0, main, 76, color, { strokeThickness: 12, fontStyle: 'italic bold' }).setOrigin(0.5).setAngle(-2);
      c.add([g, t]);
      if (sub) c.add(text(this, 0, 44, sub, 22, '#ffffff', { fontStyle: 'italic' }).setOrigin(0.5).setAngle(-2));
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
    c.add(this.add.rectangle(FIELD_VIEW.w / 2, FIELD_VIEW.h / 2, FIELD_VIEW.w, FIELD_VIEW.h, THEME.night, 0.8).setInteractive());
    c.add(text(this, FIELD_VIEW.w / 2, 230, 'PAUSA', 64, '#ffd23f', { fontStyle: 'italic bold', strokeThickness: 10 }).setOrigin(0.5));
    c.add(new Button(this, FIELD_VIEW.w / 2, 340, 'Reanudar', onResume, { w: 280, h: 56, color: THEME.yellow }));
    c.add(new Button(this, FIELD_VIEW.w / 2, 410, 'Abandonar partido', onQuit, { w: 280, h: 52, color: COLORS.uiRed }));
    c.add(
      text(
        this,
        FIELD_VIEW.w / 2,
        520,
        'Con balón: arrastra desde tu jugador para regatear, pulsa a un compañero\npara pasar, pulsa un hueco para pase al espacio y la portería (o T) para tirar.\nSin balón: arrastra a cualquier jugador o pulsa en el campo.',
        16,
        '#c9d3e0',
        { align: 'center', lineSpacing: 6, fontStyle: 'italic' },
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
    const W = FIELD_VIEW.w;
    const c = this.add.container(0, 0).setDepth(90);
    c.add(this.add.rectangle(W / 2, FIELD_VIEW.h / 2, W, FIELD_VIEW.h, THEME.night, 0.85).setInteractive());
    const g = this.add.graphics();
    g.fillStyle(dim(home.colors.shirt)).fillPoints([pt(0, 170), pt(W / 2 + 30, 150), pt(W / 2 - 30, 470), pt(0, 490)], true);
    g.fillStyle(dim(away.colors.shirt)).fillPoints([pt(W, 130), pt(W / 2 + 30, 150), pt(W / 2 - 30, 470), pt(W, 450)], true);
    g.lineStyle(4, THEME.yellow).lineBetween(W / 2 + 30, 150, W / 2 - 30, 470);
    c.add(g);
    c.add(text(this, W / 2, 110, 'FINAL DEL PARTIDO', 34, '#ffd23f', { fontStyle: 'italic bold', strokeThickness: 7 }).setOrigin(0.5));
    c.add(this.add.image(W / 2 - 220, 260, texKey.emblem(home.id)).setDisplaySize(130, 130));
    c.add(this.add.image(W / 2 + 220, 260, texKey.emblem(away.id)).setDisplaySize(130, 130));
    c.add(text(this, W / 2, 270, `${a}  -  ${b}`, 84, '#ffffff', { fontStyle: 'italic bold', strokeThickness: 10 }).setOrigin(0.5));
    const wrap = { align: 'center', wordWrap: { width: 190 }, fontStyle: 'italic bold' };
    c.add(fitWidth(text(this, W / 2 - 220, 360, home.name, 18, '#ffffff', wrap).setOrigin(0.5, 0), 190, 13));
    c.add(fitWidth(text(this, W / 2 + 220, 360, away.name, 18, '#ffffff', wrap).setOrigin(0.5, 0), 190, 13));
    const verdict = a > b ? '¡VICTORIA!' : a < b ? 'DERROTA...' : 'EMPATE';
    c.add(text(this, W / 2, 540, verdict, 44, a > b ? '#7dff9a' : a < b ? '#ff8a8a' : '#ffffff', { fontStyle: 'italic bold', strokeThickness: 8 }).setOrigin(0.5));
    c.add(new Button(this, W / 2 - 130, 630, 'Revancha', onRematch, { w: 220, h: 56, color: THEME.yellow }));
    c.add(new Button(this, W / 2 + 130, 630, 'Menú', onMenu, { w: 220, h: 52, color: THEME.panelLight }));
  }
}

/** Reduce el tamaño de letra hasta que el texto quepa en `maxW` (sin bajar de `minSize`). */
function fitWidth(t: Phaser.GameObjects.Text, maxW: number, minSize: number): Phaser.GameObjects.Text {
  let size = parseInt(String(t.style.fontSize), 10);
  while (t.width > maxW && size > minSize) t.setFontSize(--size);
  return t;
}
