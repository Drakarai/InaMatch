import Phaser from 'phaser';
import { FIELD_VIEW, GAME_SPEED, GOAL_DEPTH, GOAL_W, HALF_GAME_MINUTES, HALF_REAL_SECONDS, PITCH, WORLD } from '../config';
import { getTeam } from '../data';
import { elementMultiplier } from '../data/elements';
import { getFormation } from '../data/formations';
import type { Formation, TeamData } from '../data/types';
import { lineupPlayers, type Lineup } from '../engine/lineup';
import {
  DUEL_FP_COST,
  FIRED_UP_BONUS,
  FIRED_UP_SECONDS,
  SHOT_FP_COST,
  SHOT_POWER_LEVELS,
  TENSION_GAIN,
  basePower,
  choiceLabel,
  cpuChoice,
  isFoul,
  resolveBlock,
  resolveDuel,
  resolveKeeper,
  shotPower,
  supportMultiplier,
  type Choice,
} from '../engine/rules';
import { texKey } from '../gfx/placeholders';
import { MatchPlayer, type Side, type Vec } from '../match/MatchPlayer';
import type { HudScene } from './HudScene';

type State = 'play' | 'shot' | 'event' | 'paused' | 'over';

/** Tiro en vuelo: el balón viaja en tiempo real y los defensas pueden cruzarse en su trayectoria. */
interface ShotFlight {
  shooter: MatchPlayer;
  shotChoice: Choice;
  power: number;
  target: Vec;
  keeper: MatchPlayer;
  defSide: Side;
  tried: Set<MatchPlayer>;
  isChip: boolean;
  speed: number;
  startDist: number;
  /** cámara lenta cuando defiende el humano, para que le dé tiempo a colocarse */
  slow: number;
}

interface Ball {
  sprite: Phaser.GameObjects.Image;
  shadow: Phaser.GameObjects.Ellipse;
  x: number;
  y: number;
  height: number;
  dirX: number;
  dirY: number;
  speed: number;
  /** distancia que aún recorre a velocidad constante antes de frenar */
  travel: number;
  owner: MatchPlayer | null;
  lastTouch: Side;
  kicker: MatchPlayer | null;
  kickedAt: number;
  pass: { receiver: MatchPlayer | null; tried: Set<MatchPlayer> } | null;
}

export interface GoalEntry {
  side: Side;
  name: string;
  minute: number;
}

const CX = PITCH.x + PITCH.w / 2;
const PICKUP_RADIUS = 16;
const DUEL_RADIUS = 24;
const SHOT_RANGE = 720;
const PASS_SPEED = 560 * GAME_SPEED;
const LOOSE_BALL_SPEED = 380 * GAME_SPEED;
/** Cámara lenta mientras vuela un tiro de la CPU. */
const SHOT_SLOWMO = 0.45;
/** Distancia a la que un defensa se cruza con el tiro y puede bloquearlo. */
const BLOCK_RADIUS = 34;
/** Segundos en el suelo tras perder un duelo. */
const STUN_BEATEN = 2.4; // defensa al que regatean
const STUN_ROBBED = 2.0; // atacante al que le roban
const CARRIER_GRAB_RADIUS = 48;

const rng = Math.random;

export class MatchScene extends Phaser.Scene {
  teams!: [TeamData, TeamData];
  score: [number, number] = [0, 0];
  goals: GoalEntry[] = [];
  half = 1;
  clock = 0;
  /** Tensión de cada equipo (0-100); al llenarse se ponen FIRED UP. */
  tension: [number, number] = [0, 0];
  private firedUntil: [number, number] = [0, 0];

  private lineups!: [Lineup, Lineup];
  private formations!: [Formation, Formation];
  private players: [MatchPlayer[], MatchPlayer[]] = [[], []];
  private ball!: Ball;
  private state: State = 'event';
  private stateBeforePause: State = 'play';
  private now = 0; // tiempo de juego (solo avanza en 'play')
  private duelCooldownUntil = 0;
  private holdUntil = 0; // el portero con el balón en las manos
  private cpuThinkAt = 0;
  private cpuPossessionSince = 0;
  private hud!: HudScene;
  private flight: ShotFlight | null = null;

  private pathGfx!: Phaser.GameObjects.Graphics;
  private markerGfx!: Phaser.GameObjects.Graphics;
  /** Línea que se está dibujando: el jugador la va siguiendo según se traza. */
  private drawing: { player: MatchPlayer; last: Vec; startScreen: Vec; tapCandidate: boolean; started: boolean } | null = null;
  private passHint: MatchPlayer | null = null;
  private passHintText!: Phaser.GameObjects.Text;
  private shootHint = false;
  private shootHintText!: Phaser.GameObjects.Text;
  private shotCone!: Phaser.GameObjects.Graphics;
  private passHintAt = 0;
  private duelRing!: Phaser.GameObjects.Graphics;

  constructor() {
    super('match');
  }

  init(data: { home: Lineup; away: Lineup }): void {
    this.lineups = [data.home, data.away];
    this.teams = [getTeam(data.home.teamId), getTeam(data.away.teamId)];
    this.formations = [getFormation(data.home.formationId), getFormation(data.away.formationId)];
    this.score = [0, 0];
    this.goals = [];
    this.half = 1;
    this.clock = 0;
    this.now = 0;
    this.state = 'event';
    this.players = [[], []];
    this.drawing = null;
    this.passHint = null;
    this.shootHint = false;
    this.tension = [0, 0];
    this.firedUntil = [0, 0];
    this.flight = null;
  }

  create(): void {
    this.cameras.main.setViewport(FIELD_VIEW.x, FIELD_VIEW.y, FIELD_VIEW.w, FIELD_VIEW.h);
    this.cameras.main.setBounds(0, 0, WORLD.w, WORLD.h);
    this.drawPitch();

    for (const side of [0, 1] as const) {
      const team = this.teams[side];
      const list = lineupPlayers(team, this.lineups[side]).slice(0, 11);
      this.players[side] = list.map((p, slot) => new MatchPlayer(this, p, team, side, slot));
    }

    const ballSprite = this.add.image(CX, WORLD.h / 2, 'ball');
    const ballShadow = this.add.ellipse(CX, WORLD.h / 2, 12, 5, 0x000000, 0.3);
    this.ball = {
      sprite: ballSprite,
      shadow: ballShadow,
      x: CX,
      y: WORLD.h / 2,
      height: 0,
      dirX: 0,
      dirY: 0,
      speed: 0,
      travel: 0,
      owner: null,
      lastTouch: 0,
      kicker: null,
      kickedAt: -1,
      pass: null,
    };

    this.pathGfx = this.add.graphics().setDepth(9000);
    this.markerGfx = this.add.graphics().setDepth(9500);
    this.duelRing = this.add.graphics().setDepth(9400);
    const bubble = { fontFamily: 'Arial', fontSize: '13px', fontStyle: 'bold', color: '#1b2a40', backgroundColor: '#ffffff', padding: { x: 5, y: 2 } };
    this.passHintText = this.add.text(0, 0, '¡Aquí!', bubble).setOrigin(0.5, 1).setDepth(9600).setVisible(false);
    this.shootHintText = this.add
      .text(0, 0, '¡Tira!', { ...bubble, color: '#ffffff', backgroundColor: '#d8344a' })
      .setOrigin(0.5, 1)
      .setDepth(9600)
      .setVisible(false);
    this.shotCone = this.add.graphics().setDepth(8900);

    this.input.on('pointerdown', this.onPointerDown, this);
    this.input.on('pointermove', this.onPointerMove, this);
    this.input.on('pointerup', this.onPointerUp, this);
    this.input.keyboard?.on('keydown-SPACE', () => this.togglePause());

    this.scene.launch('hud', { match: this });
    this.hud = this.scene.get('hud') as HudScene;
    this.events.once(Phaser.Scenes.Events.SHUTDOWN, () => this.scene.stop('hud'));
  }

  /** Lo llama el HUD al terminar su create(): ya se pueden mostrar avisos. */
  onHudReady(): void {
    this.kickoff(0, true);
  }

  // --------------------------------------------------------------- dibujo

  private drawPitch(): void {
    const g = this.add.graphics().setDepth(-10);
    const [home, away] = this.teams;
    // alrededores de estadio de noche, con vallas en los colores de cada equipo
    g.fillStyle(0x121a28).fillRect(0, 0, WORLD.w, WORLD.h);
    g.fillStyle(0x0c121d);
    for (let y = 0; y < WORLD.h; y += 24) g.fillRect(0, y, WORLD.w, 12);
    for (const [x, team] of [
      [PITCH.x - 76, home],
      [PITCH.x + PITCH.w + 56, away],
    ] as const) {
      for (let y = PITCH.y - 40; y < PITCH.y + PITCH.h + 40; y += 120) {
        g.fillStyle(Phaser.Display.Color.HexStringToColor(team.colors.shirt).color).fillRect(x, y, 20, 110);
        g.fillStyle(Phaser.Display.Color.HexStringToColor(team.colors.accent).color).fillRect(x, y + 50, 20, 10);
      }
    }
    // césped: franjas anchas y un ajedrezado suave de cortacésped
    g.fillStyle(0x2f8c3e).fillRect(PITCH.x - 44, PITCH.y - 44, PITCH.w + 88, PITCH.h + 88);
    const stripes = 12;
    for (let i = 0; i < stripes; i++) {
      g.fillStyle(i % 2 ? 0x3a9d48 : 0x339443).fillRect(PITCH.x - 44, PITCH.y + (i * PITCH.h) / stripes, PITCH.w + 88, PITCH.h / stripes);
    }
    g.fillStyle(0xffffff, 0.035);
    for (let x = PITCH.x - 44; x < PITCH.x + PITCH.w + 44; x += 150) g.fillRect(x, PITCH.y - 44, 75, PITCH.h + 88);
    g.lineStyle(4, 0xffffff, 0.9);
    g.strokeRect(PITCH.x, PITCH.y, PITCH.w, PITCH.h);
    g.lineBetween(PITCH.x, PITCH.y + PITCH.h / 2, PITCH.x + PITCH.w, PITCH.y + PITCH.h / 2);
    g.strokeCircle(CX, PITCH.y + PITCH.h / 2, 110);
    this.add.image(CX, PITCH.y + PITCH.h / 2, texKey.emblem(home.id)).setDisplaySize(170, 170).setAlpha(0.18).setDepth(-9);
    g.fillStyle(0xffffff).fillCircle(CX, PITCH.y + PITCH.h / 2, 5);
    for (const top of [true, false]) {
      const line = top ? PITCH.y : PITCH.y + PITCH.h;
      const dir = top ? 1 : -1;
      const boxH = 190;
      const smallH = 70;
      g.strokeRect(CX - 220, top ? line : line - boxH, 440, boxH);
      g.strokeRect(CX - 110, top ? line : line - smallH, 220, smallH);
      g.fillCircle(CX, line + dir * 130, 4);
      g.beginPath();
      g.arc(CX, line + dir * 130, 100, top ? 0.2 * Math.PI : 1.2 * Math.PI, top ? 0.8 * Math.PI : 1.8 * Math.PI);
      g.strokePath();
      // portería con red
      const gy = top ? line - GOAL_DEPTH : line;
      g.fillStyle(0xdfe6ee, 0.9).fillRect(CX - GOAL_W / 2, gy, GOAL_W, GOAL_DEPTH);
      g.lineStyle(1, 0x9aa7b5, 0.8);
      for (let x = CX - GOAL_W / 2; x <= CX + GOAL_W / 2; x += 10) g.lineBetween(x, gy, x, gy + GOAL_DEPTH);
      for (let y = gy; y <= gy + GOAL_DEPTH; y += 8) g.lineBetween(CX - GOAL_W / 2, y, CX + GOAL_W / 2, y);
      g.lineStyle(5, 0xffffff).strokeRect(CX - GOAL_W / 2, gy, GOAL_W, GOAL_DEPTH);
      g.lineStyle(4, 0xffffff, 0.95);
    }
    // corners
    for (const [x, y, a] of [
      [PITCH.x, PITCH.y, 0],
      [PITCH.x + PITCH.w, PITCH.y, 0.5],
      [PITCH.x + PITCH.w, PITCH.y + PITCH.h, 1],
      [PITCH.x, PITCH.y + PITCH.h, 1.5],
    ]) {
      g.beginPath();
      g.arc(x, y, 16, a * Math.PI, (a + 0.5) * Math.PI);
      g.strokePath();
    }
  }

  // ------------------------------------------------------- API para el HUD

  allPlayers(): MatchPlayer[] {
    return [...this.players[0], ...this.players[1]];
  }

  ballPos(): Vec {
    return { x: this.ball.x, y: this.ball.y };
  }

  ballOwner(): MatchPlayer | null {
    return this.ball.owner;
  }

  /** Jugador humano "activo": el que lleva el balón o el más cercano a él. */
  focusPlayer(): MatchPlayer {
    if (this.ball.owner?.side === 0) return this.ball.owner;
    return this.closest(this.players[0].filter((p) => !p.isGK), this.ball) ?? this.players[0][0];
  }

  togglePause(): void {
    if (this.state === 'paused') {
      this.state = this.stateBeforePause;
      this.hud.hidePause();
      this.tweens.resumeAll();
      return;
    }
    // solo se pausa en juego: en duelos y animaciones hay que elegir antes
    if (this.state !== 'play' && this.state !== 'shot') return;
    this.stateBeforePause = this.state;
    this.state = 'paused';
    this.tweens.pauseAll();
    this.hud.showPause(
      () => this.togglePause(),
      () => this.scene.start('menu'),
    );
  }

  // -------------------------------------------------------- utilidades

  private attackDir(side: Side): number {
    return side === 0 ? -1 : 1;
  }

  private goalOf(side: Side): Vec {
    // portería que defiende `side`
    return { x: CX, y: side === 0 ? PITCH.y + PITCH.h : PITCH.y };
  }

  private toWorld(side: Side, nx: number, depth: number): Vec {
    return side === 0
      ? { x: PITCH.x + nx * PITCH.w, y: PITCH.y + depth * PITCH.h }
      : { x: PITCH.x + (1 - nx) * PITCH.w, y: PITCH.y + (1 - depth) * PITCH.h };
  }

  /** 0 = junto a la portería rival, 1 = junto a la propia. */
  private depthOf(side: Side, y: number): number {
    const d = (y - PITCH.y) / PITCH.h;
    return side === 0 ? d : 1 - d;
  }

  private closest<T extends Vec>(list: T[], to: Vec): T | null {
    let best: T | null = null;
    let bestD = Infinity;
    for (const p of list) {
      const d = Phaser.Math.Distance.Between(p.x, p.y, to.x, to.y);
      if (d < bestD) {
        bestD = d;
        best = p;
      }
    }
    return best;
  }

  private dist(a: Vec, b: Vec): number {
    return Phaser.Math.Distance.Between(a.x, a.y, b.x, b.y);
  }

  private opponents(side: Side): MatchPlayer[] {
    return this.players[side === 0 ? 1 : 0];
  }

  private inOwnBox(p: MatchPlayer): boolean {
    const d = this.depthOf(p.side, p.y);
    return d > 1 - 190 / PITCH.h && Math.abs(p.x - CX) < 220;
  }

  private clampToPitch(v: Vec, margin = 8): Vec {
    return {
      x: Phaser.Math.Clamp(v.x, PITCH.x + margin, PITCH.x + PITCH.w - margin),
      y: Phaser.Math.Clamp(v.y, PITCH.y + margin, PITCH.y + PITCH.h - margin),
    };
  }

  private gameMinute(): number {
    return Math.min(
      this.half * HALF_GAME_MINUTES,
      Math.floor((this.clock / HALF_REAL_SECONDS) * HALF_GAME_MINUTES) + (this.half - 1) * HALF_GAME_MINUTES + 1,
    );
  }

  // ---------------------------------------------------------- saques

  private kickoff(side: Side, first = false): void {
    this.state = 'event';
    for (const s of [0, 1] as const) {
      const formation = this.formations[s];
      this.players[s].forEach((p, i) => {
        const slot = formation.slots[i];
        // todos en su campo, comprimidos hacia atrás
        let depth = slot.pos === 'GK' ? 0.97 : 0.53 + ((slot.y - 0.3) / 0.7) * 0.42;
        // el equipo que no saca espera fuera del círculo central
        if (s !== side) depth = Math.max(depth, 0.59);
        const w = this.toWorld(s, slot.x, depth);
        p.setPos(w.x, w.y);
        p.path = [];
        p.manual = false;
        p.stunnedUntil = 0;
      });
    }
    // los dos delanteros del equipo que saca, en el círculo central
    const fws = this.players[side].filter((p) => getFormation(this.lineups[side].formationId).slots[p.slot].pos === 'FW');
    const kicker = fws[0] ?? this.players[side][10];
    kicker.setPos(CX - 14, PITCH.y + PITCH.h / 2 - this.attackDir(side) * 6);
    if (fws[1]) fws[1].setPos(CX + 60, PITCH.y + PITCH.h / 2 - this.attackDir(side) * 30);
    this.giveBall(kicker);
    this.duelCooldownUntil = this.now + 1.5;
    this.cameras.main.centerOn(CX, PITCH.y + PITCH.h / 2);
    this.syncAll();
    void this.hud
      .banner(first ? (this.half === 1 ? '¡A jugar!' : '2ª parte') : '¡Saque!', first ? `${this.teams[0].name} vs ${this.teams[1].name}` : '', '#ffffff', 1100)
      .then(() => this.resumePlay());
  }

  private giveBall(p: MatchPlayer): void {
    const b = this.ball;
    b.owner = p;
    b.lastTouch = p.side;
    b.pass = null;
    b.speed = 0;
    b.travel = 0;
    b.height = 0;
    if (p.side === 1) this.cpuPossessionSince = this.now;
    // el receptor deja de seguir el destino del pase
    if (!p.manual) p.path = [];
  }

  // ---------------------------------------------------------- bucle

  update(_time: number, deltaMs: number): void {
    const dt = Math.min(deltaMs / 1000, 0.05);
    if (this.state === 'play') {
      this.now += dt;
      this.clock += dt;
      if (this.clock >= HALF_REAL_SECONDS) {
        this.clock = HALF_REAL_SECONDS;
        void this.endHalf();
      } else {
        this.stepPlayers(dt);
        this.stepBall(dt);
        this.checkDuel();
        this.checkOut();
        this.cpuCarrierLogic();
        this.passHintUpdate();
        this.keeperHoldLogic();
      }
    } else if (this.state === 'shot' && this.flight) {
      const sdt = dt * this.flight.slow;
      this.now += sdt;
      this.stepPlayers(sdt);
      this.stepShotFlight(sdt);
    }
    this.syncAll();
    this.followCamera(dt);
  }

  private followCamera(dt: number): void {
    const cam = this.cameras.main;
    const target = this.ball.owner ?? this.ball;
    const tx = target.x - cam.width / 2;
    // la cámara mira hacia donde ataca quien tiene el balón
    const ty = target.y - cam.height / 2 + (this.ball.owner?.side === 1 ? 80 : -120);
    const k = 1 - Math.exp(-5 * dt);
    cam.setScroll(cam.scrollX + (tx - cam.scrollX) * k, cam.scrollY + (ty - cam.scrollY) * k);
  }

  private syncAll(): void {
    const owner = this.ball.owner;
    const focus = this.focusPlayer();
    for (const p of this.allPlayers()) p.syncVisuals(this.now, p === owner || p === focus);

    const b = this.ball;
    if (b.owner) {
      const o = b.owner;
      b.x = o.x + o.facing.x * 9;
      b.y = o.y + 19 + o.facing.y * 5;
      b.height = 0;
    }
    b.shadow.setPosition(b.x, b.y + 4).setDepth(b.y - 1);
    b.sprite.setPosition(b.x, b.y - b.height).setDepth(b.y + 4);
    b.sprite.rotation += (b.owner?.moving ? 8 : b.speed / 40) * 0.016;

    // marcador amarillo sobre el poseedor y los recorridos dibujados
    const m = this.markerGfx.clear();
    if (owner) {
      m.fillStyle(0xffd23f).lineStyle(2, 0x6a4a00);
      const y = owner.y - 34;
      m.fillTriangle(owner.x - 8, y - 10, owner.x + 8, y - 10, owner.x, y);
      m.strokeTriangle(owner.x - 8, y - 10, owner.x + 8, y - 10, owner.x, y);
    }
    if (focus !== owner) {
      m.lineStyle(2, 0xffffff, 0.9).strokeEllipse(focus.x, focus.y + 21, 38, 14);
    }

    const g = this.pathGfx.clear();
    for (const p of this.players[0]) if (p.path.length && p.manual) this.drawPath(g, p, p.path);

    // trayectoria del tiro en vuelo, para saber dónde cruzarse
    if (this.flight && (this.state === 'shot' || this.state === 'event')) {
      const t = this.flight.target;
      this.shotCone
        .clear()
        .lineStyle(4, 0x3ff0d0, 0.75)
        .lineBetween(b.x, b.y, t.x, t.y)
        .fillStyle(0x3ff0d0, 0.9)
        .fillCircle(t.x, t.y, 6);
    }

    // "¡Aquí!" sobre el mejor compañero libre y "¡Tira!" si hay buena ocasión
    if (this.passHint && this.state === 'play') {
      this.passHintText.setVisible(true).setPosition(this.passHint.x, this.passHint.y - 28);
    } else {
      this.passHintText.setVisible(false);
    }
    if (this.shootHint && owner && this.state === 'play') {
      this.shootHintText.setVisible(true).setPosition(owner.x, owner.y - 44);
    } else {
      this.shootHintText.setVisible(false);
    }
  }

  private drawPath(g: Phaser.GameObjects.Graphics, p: MatchPlayer, pts: Vec[]): void {
    if (!pts.length) return;
    g.lineStyle(5, 0x0e5d1c, 0.6);
    g.beginPath();
    g.moveTo(p.x, p.y + 18);
    for (const pt of pts) g.lineTo(pt.x, pt.y + 18);
    g.strokePath();
    g.lineStyle(3, 0x5dff6b, 1);
    g.beginPath();
    g.moveTo(p.x, p.y + 18);
    for (const pt of pts) g.lineTo(pt.x, pt.y + 18);
    g.strokePath();
    const last = pts[pts.length - 1];
    const prev = pts.length > 1 ? pts[pts.length - 2] : { x: p.x, y: p.y };
    const ang = Math.atan2(last.y - prev.y, last.x - prev.x);
    g.fillStyle(0x5dff6b);
    g.fillTriangle(
      last.x + Math.cos(ang) * 10,
      last.y + 18 + Math.sin(ang) * 10,
      last.x + Math.cos(ang + 2.5) * 10,
      last.y + 18 + Math.sin(ang + 2.5) * 10,
      last.x + Math.cos(ang - 2.5) * 10,
      last.y + 18 + Math.sin(ang - 2.5) * 10,
    );
  }

  // ------------------------------------------------------ movimiento / IA

  private homeTarget(p: MatchPlayer): Vec {
    const formation = this.formations[p.side];
    const slot = formation.slots[p.slot];
    if (p.isGK) {
      const goal = this.goalOf(p.side);
      const x = Phaser.Math.Clamp(this.ball.x, CX - GOAL_W / 2 + 12, CX + GOAL_W / 2 - 12);
      return { x: CX + (x - CX) * 0.8, y: goal.y + this.attackDir(p.side) * 28 };
    }
    const ballDepth = this.depthOf(p.side, this.ball.y);
    const progress = 1 - ballDepth; // 1 = balón junto a la portería rival
    const possession = this.ball.owner?.side ?? (this.ball.pass ? this.ball.lastTouch : null);
    let depth = slot.y - (progress - 0.45) * 0.55;
    if (possession === p.side) depth -= slot.pos === 'FW' ? 0.12 : 0.06;
    else if (possession !== null) depth += 0.04;
    depth = Phaser.Math.Clamp(depth, 0.1, 0.92);
    const ballNx = (this.ball.x - PITCH.x) / PITCH.w;
    const sideNx = p.side === 0 ? ballNx : 1 - ballNx;
    const nx = slot.x * 0.8 + sideNx * 0.2;
    return this.toWorld(p.side, nx, depth);
  }

  private stepPlayers(dt: number): void {
    const b = this.ball;
    const owner = b.owner;
    const possSide = owner?.side ?? null;

    for (const side of [0, 1] as const) {
      const team = this.players[side];
      // perseguidor: el más cercano al balón si no lo tenemos
      let chaser: MatchPlayer | null = null;
      let cover: MatchPlayer | null = null;
      const passToUs = b.pass && b.lastTouch === side;
      const interceptors = this.shotInterceptors(side);
      if (possSide !== side && !passToUs && !this.flight) {
        const candidates = team.filter((p) => !p.isGK && !p.isStunned(this.now) && !(side === 0 && p.manual));
        const sorted = candidates.sort((a, c) => this.dist(a, b) - this.dist(c, b));
        chaser = sorted[0] ?? null;
        if (side === 1) cover = sorted[1] ?? null;
      }

      for (const p of team) {
        if (p.isStunned(this.now)) {
          p.moving = false;
          continue;
        }
        const beingDrawn = this.drawing?.started === true && this.drawing.player === p;
        // ha alcanzado la punta de la línea que aún se está dibujando: espera ahí
        if (beingDrawn && !p.path.length) {
          p.moving = false;
          continue;
        }
        const withBall = owner === p;
        const speed = p.speed(withBall);

        if (p.path.length) {
          if (p.moveTowards(p.path[0], speed, dt)) p.path.shift();
          if (!p.path.length && !beingDrawn) p.manual = false;
          this.drainFp(p, dt);
          continue;
        }
        if (withBall) {
          // el humano conduce con recorridos; la CPU la maneja cpuCarrierLogic
          if (side === 0) p.moving = false;
          else this.cpuDribble(p, speed, dt);
          continue;
        }

        let target: Vec;
        let sp = speed;
        if (interceptors.has(p)) {
          target = interceptors.get(p)!;
        } else if (p === chaser) {
          target = owner ? { x: owner.x, y: owner.y } : { x: b.x, y: b.y };
          // la CPU presiona algo más despacio para que se pueda escapar regateando
          sp *= side === 0 ? 0.95 : 0.88;
        } else if (p === cover && owner) {
          const goal = this.goalOf(side);
          const t = 90 / Math.max(90, this.dist(owner, goal));
          target = { x: owner.x + (goal.x - owner.x) * t, y: owner.y + (goal.y - owner.y) * t };
          sp *= 0.85;
        } else if (p.isGK && !owner && !b.pass && this.dist(b, this.goalOf(side)) < 170) {
          target = { x: b.x, y: b.y }; // el portero sale a por el balón suelto
        } else {
          target = this.homeTarget(p);
          sp *= 0.7;
        }
        const arrived = p.moveTowards(this.clampToPitch(target, -30), sp, dt);
        if (!arrived) this.drainFp(p, dt);
        // mirar al balón cuando está quieto
        if (arrived) {
          const dx = b.x - p.x;
          const dy = b.y - p.y;
          const d = Math.hypot(dx, dy) || 1;
          p.facing = { x: dx / d, y: dy / d };
        }
      }
    }
  }

  private drainFp(p: MatchPlayer, dt: number): void {
    p.fp = Math.max(0, p.fp - dt * 0.15 * (65 / Math.max(20, p.data.stats.stamina)));
  }

  private cpuDribble(p: MatchPlayer, speed: number, dt: number): void {
    const goal = this.goalOf(0);
    // avanza hacia la portería esquivando al rival más cercano
    let tx = goal.x + (p.x - goal.x) * 0.6;
    const ty = goal.y;
    const near = this.closest(this.players[0], p);
    if (near && this.dist(near, p) < 110) tx += p.x < near.x ? -120 : 120;
    const target = this.clampToPitch({ x: tx, y: Math.min(ty, p.y + 200) }, 20);
    p.moveTowards(target, speed, dt);
    this.drainFp(p, dt);
  }

  // ---------------------------------------------------------------- balón

  private kick(from: MatchPlayer, to: Vec, receiver: MatchPlayer | null, speed = PASS_SPEED): void {
    const b = this.ball;
    const d = this.dist(b, to) || 1;
    b.owner = null;
    b.dirX = (to.x - b.x) / d;
    b.dirY = (to.y - b.y) / d;
    b.speed = speed;
    b.travel = d;
    b.kicker = from;
    b.kickedAt = this.now;
    b.lastTouch = from.side;
    b.pass = { receiver, tried: new Set() };
    from.path = [];
    from.manual = false;
    if (receiver) {
      receiver.path = [this.clampToPitch(to)];
      receiver.manual = false;
    }
  }

  private stepBall(dt: number): void {
    const b = this.ball;
    if (b.owner) return;
    if (b.speed > 0) {
      const step = b.speed * dt;
      b.x += b.dirX * step;
      b.y += b.dirY * step;
      if (b.travel > 0) b.travel -= step;
      else b.speed *= Math.exp(-3.2 * dt);
      if (b.speed < 8) {
        b.speed = 0;
        b.pass = null;
      }
      b.height = b.travel > 0 && b.pass ? Math.min(10, b.travel * 0.04) : 0;
    }
    // ¿alguien la recoge?
    for (const p of this.allPlayers()) {
      if (p.isStunned(this.now)) continue;
      if (p === b.kicker && this.now - b.kickedAt < 0.35) continue;
      if (this.dist(p, { x: b.x, y: b.y - 18 }) > PICKUP_RADIUS + 8) continue;
      const kickerSide = b.kicker?.side;
      if (b.pass && b.speed > 0 && kickerSide !== undefined && p.side !== kickerSide) {
        if (b.pass.tried.has(p)) continue;
        b.pass.tried.add(p);
        const passer = b.kicker!;
        const chance = Phaser.Math.Clamp(0.35 + (p.data.stats.guard - passer.data.stats.control) / 80, 0.12, 0.75);
        if (rng() > chance) continue;
        this.floatText(p.x, p.y - 40, '¡Interceptado!', '#ffb0b0');
      }
      this.giveBall(p);
      if (p.isGK && this.inOwnBox(p)) this.holdUntil = this.now + (p.side === 0 ? 4 : 1.2);
      break;
    }
  }

  private checkOut(): void {
    const b = this.ball;
    if (b.owner) return;
    const outX = b.x < PITCH.x - 4 || b.x > PITCH.x + PITCH.w + 4;
    const outTop = b.y < PITCH.y - 4;
    const outBottom = b.y > PITCH.y + PITCH.h + 4;
    if (!outX && !outTop && !outBottom) return;

    if (outX) {
      const side: Side = b.lastTouch === 0 ? 1 : 0;
      const spot = this.clampToPitch({ x: b.x, y: b.y }, 10);
      this.restartWith(side, spot, 'Saque de banda');
      return;
    }
    // línea de fondo: arriba defiende la CPU (1), abajo el humano (0)
    const defending: Side = outTop ? 1 : 0;
    if (b.lastTouch !== defending) {
      const gk = this.players[defending][0];
      const goal = this.goalOf(defending);
      this.restartWith(defending, { x: CX, y: goal.y + this.attackDir(defending) * 60 }, 'Saque de puerta', gk);
    } else {
      const attacker: Side = defending === 0 ? 1 : 0;
      const spot = this.clampToPitch({ x: b.x < CX ? PITCH.x : PITCH.x + PITCH.w, y: outTop ? PITCH.y : PITCH.y + PITCH.h }, 10);
      this.restartWith(attacker, spot, 'Córner');
    }
  }

  private restartWith(side: Side, spot: Vec, label: string, who?: MatchPlayer): void {
    const taker = who ?? this.closest(this.players[side].filter((p) => !p.isGK), spot)!;
    taker.setPos(spot.x, spot.y);
    taker.path = [];
    // los rivales se apartan un poco del lanzador
    for (const o of this.opponents(side)) {
      const d = this.dist(o, spot);
      if (d < 80) {
        const k = (80 - d) / (d || 1);
        o.setPos(o.x + (o.x - spot.x) * k, o.y + (o.y - spot.y) * k);
      }
    }
    this.giveBall(taker);
    this.duelCooldownUntil = this.now + 1.2;
    if (taker.isGK) this.holdUntil = this.now + (side === 0 ? 4 : 1);
    this.hud.toast(label);
  }

  // --------------------------------------------------------- CPU con balón

  private cpuCarrierLogic(): void {
    const owner = this.ball.owner;
    if (!owner || owner.side !== 1 || owner.isGK) return;
    if (this.now < this.cpuThinkAt) return;
    this.cpuThinkAt = this.now + 0.3;

    const goal = this.goalOf(0);
    const dGoal = this.dist(owner, goal);
    const pressure = Math.min(...this.players[0].map((p) => this.dist(p, owner)));
    if (Math.abs(owner.x - CX) < 300) {
      // de cerca tira siempre; desde la frontal, a veces (más si tiene supertécnica o le aprietan)
      const hasShotMove = owner.moves.some((m) => m.kind === 'shoot' && m.tp <= owner.tp);
      const chance = dGoal < 280 ? 1 : dGoal < 540 ? 0.22 + (hasShotMove ? 0.15 : 0) + (pressure < 70 ? 0.2 : 0) : 0;
      if (rng() < chance) {
        void this.shoot(owner);
        return;
      }
    }
    const held = this.now - this.cpuPossessionSince;
    if ((pressure < 75 && rng() < 0.45) || (held > 2.5 && rng() < 0.2)) {
      const option = this.bestPassOption(owner);
      if (option) this.kick(owner, { x: option.x, y: option.y }, option);
    }
  }

  private keeperHoldLogic(): void {
    const owner = this.ball.owner;
    if (!owner || !owner.isGK || this.now < this.holdUntil) return;
    const option = this.bestPassOption(owner, true);
    if (option) this.kick(owner, { x: option.x, y: option.y }, option, PASS_SPEED * 1.1);
    else {
      const t = this.toWorld(owner.side, 0.5, 0.55);
      this.kick(owner, t, null, PASS_SPEED * 1.2);
    }
  }

  private passHintUpdate(): void {
    if (this.now < this.passHintAt) return;
    this.passHintAt = this.now + 0.3;
    const owner = this.ball.owner;
    this.passHint = owner && owner.side === 0 ? this.bestPassOption(owner) : null;
    this.shootHint = this.canShoot() && !!owner && this.dist(owner, this.goalOf(1)) < 430 && Math.abs(owner.x - CX) < 300;
  }

  /** Mejor compañero para pasar: libre de marca, por delante y con la línea de pase despejada. */
  private bestPassOption(from: MatchPlayer, long = false): MatchPlayer | null {
    let best: MatchPlayer | null = null;
    let bestScore = -Infinity;
    const opps = this.opponents(from.side);
    for (const mate of this.players[from.side]) {
      if (mate === from || mate.isGK || mate.isStunned(this.now)) continue;
      const d = this.dist(from, mate);
      if (d < 70 || d > (long ? 650 : 430)) continue;
      const free = Math.min(...opps.map((o) => this.dist(o, mate)));
      if (free < 45) continue;
      let blocked = false;
      for (const o of opps) {
        const line = new Phaser.Geom.Line(from.x, from.y, mate.x, mate.y);
        const near = Phaser.Geom.Line.GetNearestPoint(line, new Phaser.Geom.Point(o.x, o.y));
        const onSegment =
          Math.min(from.x, mate.x) - 1 <= near.x && near.x <= Math.max(from.x, mate.x) + 1 && Math.min(from.y, mate.y) - 1 <= near.y && near.y <= Math.max(from.y, mate.y) + 1;
        if (onSegment && Phaser.Math.Distance.Between(near.x, near.y, o.x, o.y) < 24) {
          blocked = true;
          break;
        }
      }
      if (blocked) continue;
      const gain = (this.depthOf(from.side, from.y) - this.depthOf(from.side, mate.y)) * PITCH.h;
      const score = gain + Math.min(free, 150) * 0.8 - d * 0.15;
      if (score > bestScore) {
        bestScore = score;
        best = mate;
      }
    }
    return best;
  }

  // ------------------------------------------------------------- duelos

  private checkDuel(): void {
    const owner = this.ball.owner;
    if (!owner || this.now < this.duelCooldownUntil) return;
    if (owner.isGK && this.inOwnBox(owner)) return;
    for (const o of this.opponents(owner.side)) {
      if (o.isStunned(this.now) || o.isGK) continue;
      if (this.dist(o, owner) < DUEL_RADIUS) {
        void this.duel(owner, o);
        return;
      }
    }
  }

  // ---------------------------------------------------- tensión y apoyos

  /** Segundos de FIRED UP que le quedan a un equipo (0 si no lo está). */
  firedLeft(side: Side): number {
    return Math.max(0, this.firedUntil[side] - this.now);
  }

  private sideMul(side: Side): number {
    return this.firedLeft(side) > 0 ? FIRED_UP_BONUS : 1;
  }

  private addTension(side: Side, amount: number): void {
    if (this.firedLeft(side) > 0) return;
    this.tension[side] = Math.min(100, this.tension[side] + amount);
    if (this.tension[side] < 100) return;
    this.tension[side] = 0;
    this.firedUntil[side] = this.now + FIRED_UP_SECONDS;
    void this.hud.banner('FIRED UP!', this.teams[side].name, side === 0 ? '#ffb347' : '#ff6a6a', 1000);
  }

  /** Cuántos de los compañeros que ayudan comparten afinidad (el neutro no cuenta). */
  private sameElement(p: MatchPlayer, helpers: MatchPlayer[]): number {
    const el = p.data.element;
    return el === 'neutral' ? 0 : helpers.filter((h) => h.data.element === el).length;
  }

  /** Compañeros que están lo bastante cerca para echar una mano en un duelo. */
  private supporters(p: MatchPlayer): MatchPlayer[] {
    return this.players[p.side].filter((m) => m !== p && !m.isGK && !m.isStunned(this.now) && this.dist(m, p) < 90);
  }

  private async duel(att: MatchPlayer, def: MatchPlayer): Promise<void> {
    this.state = 'event';
    this.passHint = null;
    this.drawing = null;

    const attHelpers = this.supporters(att);
    const defHelpers = this.supporters(def);
    const attSame = this.sameElement(att, attHelpers);
    const defSame = this.sameElement(def, defHelpers);
    const attHelp = attHelpers.length;
    const defHelp = defHelpers.length;
    const attMul = supportMultiplier(attHelp, attSame) * this.sideMul(att.side);
    const defMul = supportMultiplier(defHelp, defSame) * this.sideMul(def.side);
    // el "Poder" que se enseña ya incluye la afinidad entre los dos jugadores
    const playerAffinity = elementMultiplier(att.data.element, def.data.element);
    this.hud.showDuel(att, def, {
      power: [basePower(att.fighter(), 'attack', attMul * playerAffinity), basePower(def.fighter(), 'defend', defMul)],
      support: [Math.min(2, attHelp), Math.min(2, defHelp)],
      affinity: [Math.min(2, attSame), Math.min(2, defSame)],
    });
    this.drawDuelRing(att, def, attHelp + defHelp > 0);

    const human = att.side === 0 ? att : def;
    const cpu = att.side === 0 ? def : att;
    const humanSituation = att.side === 0 ? 'attack' : 'defend';
    const cpuSituation = att.side === 0 ? 'defend' : 'attack';
    const humanChoice = await this.hud.prompt(humanSituation, human);
    const cpuPick = cpuChoice(cpu.moves, cpuSituation, cpu.tp, rng, 0.45);
    const attChoice = att.side === 0 ? humanChoice : cpuPick;
    const defChoice = att.side === 0 ? cpuPick : humanChoice;
    this.duelRing.clear();

    await this.playMoves([att, attChoice], [def, defChoice]);
    const result = resolveDuel(att.fighter(), attChoice, def.fighter(), defChoice, rng, { attack: attMul, defense: defMul });
    att.fp = Math.max(0, att.fp - DUEL_FP_COST);
    def.fp = Math.max(0, def.fp - DUEL_FP_COST);
    this.hud.showClash(result.attackPower, result.defensePower, result.attackerWins, att.side);
    const colorOf = (p: MatchPlayer) => (p.side === 0 ? '#9fe2ff' : '#ffb0b0');

    if (isFoul(defChoice, !result.attackerWins, rng)) {
      // la entrada en plancha se lleva el balón... y al jugador: falta
      att.stunnedUntil = this.now + 0.8;
      att.path = [];
      this.floatText(def.x, def.y - 46, '¡Falta!', '#ff6a5a');
      await this.hud.banner('¡Falta!', `Tiro libre para ${this.teams[att.side].name}`, '#ff5a4a', 1000);
      this.restartWith(att.side, { x: att.x, y: att.y }, 'Tiro libre', att);
    } else if (result.attackerWins) {
      def.stunnedUntil = this.now + STUN_BEATEN;
      this.push(def, att, 26);
      this.floatText(att.x, att.y - 46, `${choiceLabel(attChoice)}: ¡superado!`, colorOf(att));
      this.addTension(att.side, TENSION_GAIN.duelWon);
    } else {
      att.stunnedUntil = this.now + STUN_ROBBED;
      att.path = [];
      this.push(att, def, 22);
      this.giveBall(def);
      def.path = [];
      this.floatText(def.x, def.y - 46, `${choiceLabel(defChoice)}: ¡robo!`, colorOf(def));
      this.addTension(def.side, TENSION_GAIN.duelWon);
    }
    this.duelCooldownUntil = this.now + 0.9;
    this.time.delayedCall(900, () => this.hud.hideDuel());
    this.resumePlay();
  }

  private drawDuelRing(a: MatchPlayer, b: MatchPlayer, crowded: boolean): void {
    const cx = (a.x + b.x) / 2;
    const cy = (a.y + b.y) / 2 + 14;
    this.duelRing.clear().lineStyle(8, 0xd8344a, 0.85).strokeCircle(cx, cy, 70);
    this.duelRing.lineStyle(3, 0xffffff, 0.6).strokeCircle(cx, cy, 76);
    // doble aro, como en GO, cuando entran más jugadores en el duelo
    if (crowded) this.duelRing.lineStyle(6, 0xd8344a, 0.85).strokeCircle(cx, cy, 36);
  }

  private push(p: MatchPlayer, from: MatchPlayer, amount: number): void {
    const dx = p.x - from.x;
    const dy = p.y - from.y;
    const d = Math.hypot(dx, dy) || 1;
    const t = this.clampToPitch({ x: p.x + (dx / d) * amount, y: p.y + (dy / d) * amount }, -20);
    this.tweens.add({ targets: p.sprite, x: t.x, y: t.y, duration: 220, ease: 'Quad.Out' });
  }

  /** Paga los TP y reproduce la animación de cada supertécnica usada. */
  private async playMoves(...entries: [MatchPlayer, Choice][]): Promise<void> {
    for (const [p, c] of entries) {
      if (c.type !== 'move') continue;
      p.tp = Math.max(0, p.tp - c.move.tp);
      await this.hud.cutin(p, c.move);
    }
  }

  private resumePlay(): void {
    if (this.state === 'event') this.state = 'play';
    else if (this.state === 'paused') this.stateBeforePause = 'play';
  }

  // --------------------------------------------------------------- tiros

  private async shoot(shooter: MatchPlayer): Promise<void> {
    if (this.state !== 'play') return;
    this.state = 'event';
    this.passHint = null;
    this.drawing = null;
    shooter.path = [];
    const defSide: Side = shooter.side === 0 ? 1 : 0;
    const keeper = this.players[defSide][0];
    const goal = this.goalOf(defSide);
    const distance = this.dist(shooter, goal);
    this.hud.showDuel(shooter, keeper);
    this.drawShotCone(shooter, goal);

    // 1) tipo de tiro y potencia
    let shotChoice: Choice;
    let level = 0;
    if (shooter.side === 0) {
      shotChoice = await this.hud.prompt('shoot', shooter);
      const tpLeft = shooter.tp - (shotChoice.type === 'move' ? shotChoice.move.tp : 0);
      level = await this.hud.promptPower(tpLeft);
    } else {
      shotChoice = cpuChoice(shooter.moves, 'shoot', shooter.tp, rng, 0.75);
      const tpLeft = shooter.tp - (shotChoice.type === 'move' ? shotChoice.move.tp : 0);
      level = SHOT_POWER_LEVELS.reduce((best, l, i) => (l.tp <= tpLeft && rng() < 0.5 ? i : best), 0);
    }
    this.shotCone.clear();
    shooter.tp = Math.max(0, shooter.tp - SHOT_POWER_LEVELS[level].tp);
    await this.playMoves([shooter, shotChoice]);
    shooter.fp = Math.max(0, shooter.fp - SHOT_FP_COST);
    const power = shotPower(shooter.fighter(), shotChoice, distance, rng, SHOT_POWER_LEVELS[level].mul * this.sideMul(shooter.side));

    // 2) el balón sale volando en tiempo real: los defensas pueden cruzarse en su camino
    const b = this.ball;
    b.owner = null;
    b.pass = null;
    b.speed = 0;
    b.lastTouch = shooter.side;
    b.kicker = shooter;
    b.kickedAt = this.now;
    // el tiro sale de los pies del que tira
    b.x = shooter.x;
    b.y = shooter.y + 19;
    const target = { x: CX + Phaser.Math.Between(-GOAL_W / 2 + 20, GOAL_W / 2 - 20), y: goal.y };
    const isChip = shotChoice.type === 'basic' && shotChoice.id === 'chip';
    this.flight = {
      shooter,
      shotChoice,
      power,
      target,
      keeper,
      defSide,
      tried: new Set(),
      isChip,
      // los tiros potentes vuelan más rápido y cuesta más cruzarse a tiempo
      speed: Phaser.Math.Clamp(200 + power * 0.45, 220, 400) * GAME_SPEED * (isChip ? 0.8 : 1),
      startDist: Math.max(1, this.dist(b, target)),
      slow: defSide === 0 ? SHOT_SLOWMO : 1,
    };
    this.hud.hideDuel();
    if (defSide === 0) this.hud.toast(isChip ? '¡Vaselina! Va por encima' : '¡Ponte delante del tiro!', 1500);
    this.state = 'shot';
  }

  /** Mientras vuela el tiro: ¿hay que bloquear o ya llega al portero? */
  private stepShotFlight(dt: number): void {
    const f = this.flight!;
    const b = this.ball;
    const remaining = this.dist(b, f.target);
    const step = f.speed * dt;
    const keeperFeet = { x: f.keeper.x, y: f.keeper.y + 18 };
    if (remaining <= step || this.dist(b, keeperFeet) < 36) {
      this.state = 'event';
      void this.keeperPhase();
      return;
    }
    b.x += ((f.target.x - b.x) / remaining) * step;
    b.y += ((f.target.y - b.y) / remaining) * step;
    const progress = 1 - remaining / f.startDist;
    b.height = f.isChip ? Math.sin(progress * Math.PI) * 46 : 6;
    if (f.isChip) return; // la vaselina pasa por encima de los defensas
    for (const o of this.opponents(f.shooter.side)) {
      if (o.isGK || o.isStunned(this.now) || f.tried.has(o)) continue;
      if (Phaser.Math.Distance.Between(o.x, o.y + 16, b.x, b.y) < BLOCK_RADIUS) {
        f.tried.add(o);
        this.state = 'event';
        void this.blockPhase(o);
        return;
      }
    }
  }

  /** Un defensa se ha cruzado en la trayectoria: duelo de bloqueo. */
  private async blockPhase(blocker: MatchPlayer): Promise<void> {
    const f = this.flight!;
    const { shooter, shotChoice } = f;
    this.hud.showDuel(shooter, blocker, {
      power: [Math.round(f.power), basePower(blocker.fighter(), 'block', this.sideMul(blocker.side) * elementMultiplier(blocker.data.element, shooter.data.element))],
    });
    const blockChoice: Choice = blocker.side === 0 ? await this.hud.prompt('block', blocker) : cpuChoice(blocker.moves, 'block', blocker.tp, rng, 0.5);
    await this.playMoves([blocker, blockChoice]);
    const block = resolveBlock(f.power, shooter.fighter(), shotChoice, blocker.fighter(), blockChoice, rng, this.sideMul(blocker.side));
    if (block.blockPower > 0) {
      blocker.fp = Math.max(0, blocker.fp - DUEL_FP_COST);
      this.hud.showClash(Math.round(f.power), block.blockPower, !block.blocked, shooter.side);
    }
    if (block.blocked) {
      this.floatText(blocker.x, blocker.y - 46, '¡Bloqueado!', '#ffffff');
      this.addTension(blocker.side, TENSION_GAIN.shotBlocked);
      this.looseBall(blocker, 160);
      this.endShot();
      return;
    }
    f.power = block.remaining;
    if (block.blockPower > 0) this.floatText(blocker.x, blocker.y - 46, 'No basta...', '#ffe28a');
    this.time.delayedCall(500, () => this.hud.hideDuel());
    // el tiro sigue su camino
    if (this.state === 'event') this.state = 'shot';
    else if (this.state === 'paused') this.stateBeforePause = 'shot';
  }

  /** El tiro llega al portero. */
  private async keeperPhase(): Promise<void> {
    const f = this.flight!;
    const { shooter, shotChoice, keeper, defSide, target } = f;
    const goal = this.goalOf(defSide);
    this.hud.showDuel(shooter, keeper, {
      power: [Math.round(f.power), basePower(keeper.fighter(), 'keep', this.sideMul(keeper.side) * elementMultiplier(keeper.data.element, shooter.data.element))],
    });
    const keepChoice: Choice = keeper.side === 0 ? await this.hud.prompt('keep', keeper) : cpuChoice(keeper.moves, 'keep', keeper.tp, rng, 0.7);
    await this.playMoves([keeper, keepChoice]);
    const result = resolveKeeper(f.power, shooter.fighter(), shotChoice, keeper.fighter(), keepChoice, rng, this.sideMul(keeper.side));
    keeper.fp = Math.max(0, keeper.fp - DUEL_FP_COST);
    this.hud.showClash(result.shotPower, result.keeperPower, result.outcome === 'goal', shooter.side);

    if (result.outcome === 'goal') {
      await this.tweenBall({ x: target.x, y: goal.y + this.attackDir(shooter.side) * 22 }, 220, 4);
      this.addTension(defSide, TENSION_GAIN.conceded);
      this.flight = null;
      await this.onGoal(shooter);
      return;
    }
    this.addTension(defSide, TENSION_GAIN.save);
    if (result.outcome === 'caught') {
      this.giveBall(keeper);
      this.holdUntil = this.now + (keeper.side === 0 ? 4 : 1.2);
      this.floatText(keeper.x, keeper.y - 46, '¡Parada!', '#ffffff');
    } else {
      this.floatText(keeper.x, keeper.y - 46, '¡Despejada!', '#ffffff');
      this.looseBall(keeper, 140);
    }
    this.endShot();
  }

  /** Los dos defensas de la CPU más cercanos a la trayectoria corren a cortarla. */
  private shotInterceptors(side: Side): Map<MatchPlayer, Vec> {
    const out = new Map<MatchPlayer, Vec>();
    const f = this.flight;
    if (!f || side !== f.defSide || side === 0 || f.isChip) return out;
    const b = this.ball;
    const dx = f.target.x - b.x;
    const dy = f.target.y - b.y;
    const len2 = dx * dx + dy * dy || 1;
    const options = this.players[side]
      .filter((p) => !p.isGK && !p.isStunned(this.now) && !f.tried.has(p))
      .map((p) => {
        // punto de la trayectoria por delante del balón más cercano a los pies de este defensa
        const feetY = p.y + 16;
        const t = Phaser.Math.Clamp(((p.x - b.x) * dx + (feetY - b.y) * dy) / len2, 0.15, 0.9);
        const point = { x: b.x + dx * t, y: b.y + dy * t - 16 };
        return { p, point, d: this.dist(p, point) };
      })
      .sort((a, c) => a.d - c.d)
      .slice(0, 2);
    for (const o of options) out.set(o.p, o.point);
    return out;
  }

  /** El humano puede mover a sus jugadores en juego y mientras vuela un tiro rival. */
  private canSteer(): boolean {
    return this.state === 'play' || (this.state === 'shot' && this.flight?.defSide === 0);
  }

  private endShot(): void {
    this.flight = null;
    this.shotCone.clear();
    this.duelCooldownUntil = this.now + 1;
    this.time.delayedCall(800, () => this.hud.hideDuel());
    this.resumePlay();
  }

  /** El balón sale rebotado desde `from`, alejándose de su portería. */
  private looseBall(from: MatchPlayer, travel: number): void {
    const b = this.ball;
    const ang = Phaser.Math.FloatBetween(-0.9, 0.9) + (from.side === 0 ? -Math.PI / 2 : Math.PI / 2);
    b.owner = null;
    b.pass = null;
    b.dirX = Math.cos(ang);
    b.dirY = Math.sin(ang);
    b.speed = LOOSE_BALL_SPEED;
    b.travel = travel;
    b.kicker = from;
    b.kickedAt = this.now;
    b.lastTouch = from.side;
  }

  /** Cono de tiro hacia la portería, como el de GO. */
  private drawShotCone(shooter: MatchPlayer, goal: Vec): void {
    const feet = { x: shooter.x, y: shooter.y + 18 };
    this.shotCone
      .clear()
      .fillStyle(0x3ff0d0, 0.28)
      .fillTriangle(feet.x, feet.y, CX - GOAL_W / 2, goal.y, CX + GOAL_W / 2, goal.y)
      .lineStyle(2, 0x3ff0d0, 0.7)
      .strokeTriangle(feet.x, feet.y, CX - GOAL_W / 2, goal.y, CX + GOAL_W / 2, goal.y);
  }

  private tweenBall(to: Vec, duration: number, arc: number): Promise<void> {
    return new Promise((resolve) => {
      const b = this.ball;
      const from = { x: b.x, y: b.y };
      this.tweens.addCounter({
        from: 0,
        to: 1,
        duration,
        onUpdate: (tw) => {
          const t = tw.getValue() ?? 1;
          b.x = from.x + (to.x - from.x) * t;
          b.y = from.y + (to.y - from.y) * t;
          b.height = Math.sin(t * Math.PI) * arc;
        },
        onComplete: () => resolve(),
      });
    });
  }

  private async onGoal(scorer: MatchPlayer): Promise<void> {
    this.score[scorer.side]++;
    this.goals.push({ side: scorer.side, name: scorer.data.short, minute: this.gameMinute() });
    this.hud.hideDuel();
    this.cameras.main.shake(250, 0.006);
    await this.hud.banner('¡GOL!', `${scorer.data.name} · ${this.teams[scorer.side].name}`, '#ffd23f', 2000);
    if (this.state === 'over') return;
    this.kickoff(scorer.side === 0 ? 1 : 0);
  }

  private async endHalf(): Promise<void> {
    this.state = 'event';
    this.drawing = null;
    if (this.half === 1) {
      await this.hud.banner('Descanso', `${this.score[0]} - ${this.score[1]}`, '#ffffff', 1800);
      for (const p of this.allPlayers()) {
        p.fp = Math.min(p.maxFp, p.fp + p.maxFp * 0.3);
        p.tp = Math.min(p.maxTp, p.tp + p.maxTp * 0.3);
      }
      this.half = 2;
      this.clock = 0;
      this.kickoff(1, true);
      return;
    }
    this.state = 'over';
    await this.hud.banner('¡Final!', '', '#ffffff', 1400);
    this.hud.showResult(
      () => this.scene.restart({ home: this.lineups[0], away: this.lineups[1] }),
      () => this.scene.start('menu'),
    );
  }

  private floatText(x: number, y: number, msg: string, color: string): void {
    const t = this.add
      .text(x, y, msg, { fontFamily: 'Arial Black, Arial', fontSize: '16px', color, stroke: '#0b1a2e', strokeThickness: 4 })
      .setOrigin(0.5)
      .setDepth(9800);
    this.tweens.add({ targets: t, y: y - 30, alpha: 0, delay: 700, duration: 600, onComplete: () => t.destroy() });
  }

  // ---------------------------------------------------------- controles

  private worldPoint(pointer: Phaser.Input.Pointer): Vec {
    const p = this.cameras.main.getWorldPoint(pointer.x, pointer.y);
    return { x: p.x, y: p.y };
  }

  private humanAt(w: Vec): MatchPlayer | null {
    // el jugador con balón tiene prioridad y se coge con más margen,
    // para no dar un pase sin querer a un compañero que esté pegado
    const owner = this.ball.owner;
    if (owner?.side === 0 && Phaser.Math.Distance.Between(owner.x, owner.y + 6, w.x, w.y) < CARRIER_GRAB_RADIUS) return owner;
    let best: MatchPlayer | null = null;
    let bestD = 30;
    for (const p of this.players[0]) {
      const d = Phaser.Math.Distance.Between(p.x, p.y + 4, w.x, w.y);
      if (d < bestD) {
        bestD = d;
        best = p;
      }
    }
    return best;
  }

  private onPointerDown(pointer: Phaser.Input.Pointer): void {
    if (!this.canSteer() || pointer.x > FIELD_VIEW.w) return;
    const w = this.worldPoint(pointer);
    const owner = this.ball.owner;
    const humanHasBall = owner?.side === 0;

    const hit = this.humanAt(w);
    if (hit) {
      // tocar a un compañero (con balón propio) = pase; arrastrar = recorrido
      this.drawing = {
        player: hit,
        last: { x: hit.x, y: hit.y },
        startScreen: { x: pointer.x, y: pointer.y },
        tapCandidate: humanHasBall && hit !== owner,
        started: false,
      };
      return;
    }
    if (humanHasBall && owner) {
      if (this.isOnGoal(w)) {
        void this.tryShoot(owner);
        return;
      }
      if (owner.isGK) return; // el portero solo pasa a un compañero
      // pase al hueco: el compañero más cercano a ese punto corre a por él
      const mate = this.closest(this.players[0].filter((p) => p !== owner && !p.isGK), w);
      this.kick(owner, this.clampToPitch(w), mate);
      return;
    }
    // sin balón: el jugador activo corre al punto
    const active = this.focusPlayer();
    active.path = [this.clampToPitch(w, -20)];
    active.manual = true;
  }

  private onPointerMove(pointer: Phaser.Input.Pointer): void {
    const d = this.drawing;
    if (!d || !pointer.isDown) return;
    if (Phaser.Math.Distance.Between(pointer.x, pointer.y, d.startScreen.x, d.startScreen.y) > 10) d.tapCandidate = false;
    if (d.tapCandidate) return;
    const w = this.worldPoint(pointer);
    if (Phaser.Math.Distance.Between(d.last.x, d.last.y, w.x, w.y) <= 12) return;
    if (!d.started) {
      // empieza una línea nueva: sustituye al recorrido anterior
      d.started = true;
      d.player.path = [];
      d.player.manual = true;
    }
    const point = this.clampToPitch(w, -20);
    if (d.player.path.length < 80) d.player.path.push(point);
    d.last = point;
  }

  private onPointerUp(): void {
    const d = this.drawing;
    this.drawing = null;
    if (!d || !this.canSteer()) return;
    const owner = this.ball.owner;
    if (d.tapCandidate && owner && owner.side === 0 && d.player !== owner) {
      this.kick(owner, { x: d.player.x, y: d.player.y }, d.player, owner.isGK ? PASS_SPEED * 1.1 : PASS_SPEED);
      return;
    }
    // la línea ya se ha ido siguiendo mientras se dibujaba; si ya llegó al final, suelta el control
    if (d.started && !d.player.path.length) d.player.manual = false;
  }

  private isOnGoal(w: Vec): boolean {
    return Math.abs(w.x - CX) < GOAL_W / 2 + 70 && w.y < PITCH.y + 70 && w.y > PITCH.y - GOAL_DEPTH - 50;
  }

  canShoot(): boolean {
    const owner = this.ball.owner;
    return this.state === 'play' && !!owner && owner.side === 0 && !owner.isGK && this.dist(owner, this.goalOf(1)) <= SHOT_RANGE;
  }

  requestShot(): void {
    const owner = this.ball.owner;
    if (this.state !== 'play' || !owner || owner.side !== 0 || owner.isGK) return;
    void this.tryShoot(owner);
  }

  private async tryShoot(owner: MatchPlayer): Promise<void> {
    const distance = this.dist(owner, this.goalOf(1));
    if (distance > SHOT_RANGE) {
      this.hud.toast('¡Demasiado lejos para tirar!');
      return;
    }
    await this.shoot(owner);
  }
}

