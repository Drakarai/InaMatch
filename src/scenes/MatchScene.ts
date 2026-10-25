import Phaser from 'phaser';
import { FIELD_VIEW, GOAL_DEPTH, GOAL_W, HALF_GAME_MINUTES, HALF_REAL_SECONDS, PITCH, WORLD } from '../config';
import { getTeam } from '../data';
import { getFormation } from '../data/formations';
import type { Formation, TeamData } from '../data/types';
import { lineupPlayers, type Lineup } from '../engine/lineup';
import {
  DUEL_FP_COST,
  SHOT_FP_COST,
  choiceLabel,
  cpuChoice,
  resolveDuel,
  resolveShot,
  type Choice,
} from '../engine/rules';
import { MatchPlayer, type Side, type Vec } from '../match/MatchPlayer';
import type { HudScene } from './HudScene';

type State = 'play' | 'event' | 'paused' | 'over';

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
const PASS_SPEED = 560;
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

  private pathGfx!: Phaser.GameObjects.Graphics;
  private markerGfx!: Phaser.GameObjects.Graphics;
  private drawing: { player: MatchPlayer; points: Vec[]; startScreen: Vec; tapCandidate: boolean } | null = null;
  private passHint: MatchPlayer | null = null;
  private passHintText!: Phaser.GameObjects.Text;
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
    this.passHintText = this.add
      .text(0, 0, '¡Pase!', { fontFamily: 'Arial', fontSize: '13px', color: '#1b2a40', backgroundColor: '#ffffff', padding: { x: 5, y: 2 } })
      .setOrigin(0.5, 1)
      .setDepth(9600)
      .setVisible(false);

    this.input.on('pointerdown', this.onPointerDown, this);
    this.input.on('pointermove', this.onPointerMove, this);
    this.input.on('pointerup', this.onPointerUp, this);
    this.input.keyboard?.on('keydown-SPACE', () => this.togglePause());
    this.input.mouse?.disableContextMenu();

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
    // pista exterior y césped con franjas
    g.fillStyle(0x9a4a35).fillRect(0, 0, WORLD.w, WORLD.h);
    g.fillStyle(0x3f9f48).fillRect(PITCH.x - 44, PITCH.y - 44, PITCH.w + 88, PITCH.h + 88);
    const stripes = 12;
    for (let i = 0; i < stripes; i++) {
      g.fillStyle(i % 2 ? 0x48ad50 : 0x41a24a).fillRect(PITCH.x - 44, PITCH.y + (i * PITCH.h) / stripes, PITCH.w + 88, PITCH.h / stripes);
    }
    g.lineStyle(4, 0xffffff, 0.95);
    g.strokeRect(PITCH.x, PITCH.y, PITCH.w, PITCH.h);
    g.lineBetween(PITCH.x, PITCH.y + PITCH.h / 2, PITCH.x + PITCH.w, PITCH.y + PITCH.h / 2);
    g.strokeCircle(CX, PITCH.y + PITCH.h / 2, 110);
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
    if (this.state !== 'play') return;
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
    for (const p of this.players[0]) if (p.path.length && p.manual && this.drawing?.player !== p) this.drawPath(g, p, p.path);
    if (this.drawing) this.drawPath(g, this.drawing.player, this.drawing.points);

    // "¡Pase!" sobre el mejor compañero libre
    if (this.passHint && this.state === 'play') {
      this.passHintText.setVisible(true).setPosition(this.passHint.x, this.passHint.y - 28);
    } else {
      this.passHintText.setVisible(false);
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
      if (possSide !== side && !passToUs) {
        const candidates = team.filter((p) => !p.isGK && !p.isStunned(this.now) && !(side === 0 && p.manual));
        const sorted = candidates.sort((a, c) => this.dist(a, b) - this.dist(c, b));
        chaser = sorted[0] ?? null;
        if (side === 1) cover = sorted[1] ?? null;
      }

      for (const p of team) {
        // en el suelo, o esperando a que se termine de dibujar su línea
        if (p.isStunned(this.now) || this.drawing?.player === p) {
          p.moving = false;
          continue;
        }
        const withBall = owner === p;
        const speed = p.speed(withBall);

        if (p.path.length) {
          if (p.moveTowards(p.path[0], speed, dt)) p.path.shift();
          if (!p.path.length) p.manual = false;
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
        if (p === chaser) {
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
    p.fp = Math.max(0, p.fp - dt * 0.15 * (30 / Math.max(10, p.data.stats.stamina)));
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
    this.cpuThinkAt = this.now + 0.25;

    const goal = this.goalOf(0);
    const dGoal = this.dist(owner, goal);
    if (dGoal < 310 && Math.abs(owner.x - CX) < 260) {
      void this.shoot(owner);
      return;
    }
    const pressure = Math.min(...this.players[0].map((p) => this.dist(p, owner)));
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

  private async duel(att: MatchPlayer, def: MatchPlayer): Promise<void> {
    this.state = 'event';
    this.passHint = null;
    this.drawing = null;
    this.hud.showDuel(att, def);
    this.drawDuelRing(att, def);

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
    const result = resolveDuel(att.fighter(), attChoice, def.fighter(), defChoice, rng);
    att.fp = Math.max(0, att.fp - DUEL_FP_COST);
    def.fp = Math.max(0, def.fp - DUEL_FP_COST);

    if (result.attackerWins) {
      def.stunnedUntil = this.now + STUN_BEATEN;
      this.push(def, att, 26);
      this.floatText(att.x, att.y - 46, `${choiceLabel(attChoice)}: ¡superado!`, att.side === 0 ? '#9fe2ff' : '#ffb0b0');
    } else {
      att.stunnedUntil = this.now + STUN_ROBBED;
      att.path = [];
      this.push(att, def, 22);
      this.giveBall(def);
      def.path = [];
      this.floatText(def.x, def.y - 46, `${choiceLabel(defChoice)}: ¡robo!`, def.side === 0 ? '#9fe2ff' : '#ffb0b0');
    }
    this.duelCooldownUntil = this.now + 0.9;
    this.time.delayedCall(900, () => this.hud.hideDuel());
    this.resumePlay();
  }

  private drawDuelRing(a: MatchPlayer, b: MatchPlayer): void {
    const cx = (a.x + b.x) / 2;
    const cy = (a.y + b.y) / 2 + 14;
    this.duelRing.clear().lineStyle(8, 0xd8344a, 0.85).strokeCircle(cx, cy, 70);
    this.duelRing.lineStyle(3, 0xffffff, 0.6).strokeCircle(cx, cy, 76);
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
    this.hud.showDuel(shooter, keeper);

    const shotChoice: Choice = shooter.side === 0 ? await this.hud.prompt('shoot', shooter) : cpuChoice(shooter.moves, 'shoot', shooter.tp, rng, 0.75);
    const keepChoice: Choice = keeper.side === 0 ? await this.hud.prompt('keep', keeper) : cpuChoice(keeper.moves, 'keep', keeper.tp, rng, 0.7);

    await this.playMoves([shooter, shotChoice]);
    const goal = this.goalOf(defSide);
    const distance = this.dist(shooter, goal);
    const result = resolveShot(shooter.fighter(), shotChoice, distance, keeper.fighter(), keepChoice, rng);
    shooter.fp = Math.max(0, shooter.fp - SHOT_FP_COST);
    keeper.fp = Math.max(0, keeper.fp - DUEL_FP_COST);

    // el balón vuela hacia la portería
    const b = this.ball;
    b.owner = null;
    b.pass = null;
    b.speed = 0;
    b.lastTouch = shooter.side;
    const aimX = CX + Phaser.Math.Between(-GOAL_W / 2 + 20, GOAL_W / 2 - 20);
    const keeperSpot = { x: (keeper.x + aimX) / 2, y: keeper.y + 10 };
    const isChip = shotChoice.type === 'basic' && shotChoice.id === 'chip';
    await this.tweenBall(keeperSpot, Math.min(700, 220 + distance * 0.5), isChip ? 40 : 6);
    await this.playMoves([keeper, keepChoice]);

    if (result.outcome === 'goal') {
      await this.tweenBall({ x: aimX, y: goal.y + this.attackDir(shooter.side) * 22 }, 180, 4);
      this.floatText(keeper.x, keeper.y - 46, `${result.shotPower} > ${result.keeperPower}`, '#ffffff');
      await this.onGoal(shooter);
      return;
    }
    if (result.outcome === 'caught') {
      this.giveBall(keeper);
      this.holdUntil = this.now + (keeper.side === 0 ? 4 : 1.2);
      this.floatText(keeper.x, keeper.y - 46, `¡Parada! ${result.keeperPower} > ${result.shotPower}`, '#ffffff');
    } else {
      // despeje: el balón sale rebotado
      const ang = Phaser.Math.FloatBetween(-0.9, 0.9) + (keeper.side === 0 ? -Math.PI / 2 : Math.PI / 2);
      b.dirX = Math.cos(ang);
      b.dirY = Math.sin(ang);
      b.speed = 380;
      b.travel = 140;
      b.kicker = keeper;
      b.kickedAt = this.now;
      b.lastTouch = keeper.side;
      this.floatText(keeper.x, keeper.y - 46, '¡Despejada!', '#ffffff');
    }
    this.duelCooldownUntil = this.now + 1;
    this.time.delayedCall(800, () => this.hud.hideDuel());
    this.resumePlay();
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
    if (this.state !== 'play' || pointer.x > FIELD_VIEW.w) return;
    const w = this.worldPoint(pointer);
    const owner = this.ball.owner;
    const humanHasBall = owner?.side === 0;

    // clic derecho con balón: pase al hueco hacia ese punto
    if (pointer.rightButtonDown()) {
      if (humanHasBall && owner && !owner.isGK) {
        const mate = this.closest(this.players[0].filter((p) => p !== owner && !p.isGK), w);
        this.kick(owner, this.clampToPitch(w), mate);
      }
      return;
    }

    const hit = this.humanAt(w);
    if (hit) {
      // tocar a un compañero (con balón propio) = pase; arrastrar = recorrido
      this.drawing = { player: hit, points: [], startScreen: { x: pointer.x, y: pointer.y }, tapCandidate: humanHasBall && hit !== owner };
      return;
    }
    if (humanHasBall && owner) {
      if (this.isOnGoal(w)) {
        void this.tryShoot(owner);
        return;
      }
      if (owner.isGK) return; // el portero solo pasa a un compañero
      // un clic en el campo nunca suelta el balón: el que lo lleva corre hacia ahí
      // (y si se arrastra, se dibuja su recorrido desde ese punto)
      this.drawing = { player: owner, points: [this.clampToPitch(w, -20)], startScreen: { x: pointer.x, y: pointer.y }, tapCandidate: false };
      return;
    }
    // sin balón: el jugador activo corre al punto
    const active = this.focusPlayer();
    active.path = [this.clampToPitch(w, -20)];
    active.manual = true;
  }

  private onPointerMove(pointer: Phaser.Input.Pointer): void {
    if (!this.drawing || !pointer.isDown) return;
    const w = this.worldPoint(pointer);
    const pts = this.drawing.points;
    const last = pts[pts.length - 1] ?? { x: this.drawing.player.x, y: this.drawing.player.y };
    if (Phaser.Math.Distance.Between(last.x, last.y, w.x, w.y) > 12) pts.push(this.clampToPitch(w, -20));
    if (Phaser.Math.Distance.Between(pointer.x, pointer.y, this.drawing.startScreen.x, this.drawing.startScreen.y) > 10) {
      this.drawing.tapCandidate = false;
    }
  }

  private onPointerUp(): void {
    const d = this.drawing;
    this.drawing = null;
    if (!d || this.state !== 'play') return;
    const owner = this.ball.owner;
    if (d.tapCandidate && owner && owner.side === 0 && d.player !== owner) {
      this.kick(owner, { x: d.player.x, y: d.player.y }, d.player, owner.isGK ? PASS_SPEED * 1.1 : PASS_SPEED);
      return;
    }
    if (d.points.length >= 1) {
      d.player.path = d.points.slice(0, 60);
      d.player.manual = true;
    }
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

