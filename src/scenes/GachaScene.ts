import Phaser from 'phaser';
import { sfx } from '../audio/sfx';
import { music } from '../audio/music';
import { loadClub, NOTEBOOK_COST, onClubChange, pull, pullNotebooks, PULL_COST, TEN_NOTEBOOK_COST, TEN_PULL_COST, type NotebookResult, type PullResult } from '../club/club';
import { drawNotebook } from '../ui/notebook';
import { RARITY } from '../club/pool';
import { GAME_H, GAME_W, PORTRAIT } from '../config';
import { CLUB_HEADER_H, clubMobileHeader } from '../ui/clubMobile';
import { drawCard, loadCardPortraits } from '../ui/card';
import { THEME, cardPanel, chip, coinChip, fitCamera, glow, pt, sectionTitle, stadiumBackdrop, topBar } from '../ui/theme';
import { Button, display, label, text, wait } from '../ui/widgets';

type Mode = 'players' | 'notebooks';
// en el móvil (vertical) el balón va arriba, centrado, y los botones abajo
const STAGE = PORTRAIT ? { x: 270, y: 350 } : { x: 820, y: 330 };

/**
 * Fichajes: tiradas de 1 o de 10 para conseguir jugadores (o cuadernos de supertécnicas) para "Mi club". Cada
 * tirada sale de un balón que se carga de rayos; el color del destello avisa de lo mejor que ha salido.
 */
export class GachaScene extends Phaser.Scene {
  private coinsLabel!: Phaser.GameObjects.Container;
  private stage!: Phaser.GameObjects.Container;
  private buttons: Button[] = [];
  private busy = false;
  private mode: Mode = 'players';
  /** De dónde se vino (para el botón de volver). */
  private from: 'menu' | 'club' = 'club';

  constructor() {
    super('gacha');
  }

  init(data: { mode?: Mode; from?: 'menu' | 'club' }): void {
    this.mode = data?.mode ?? 'players';
    this.from = data?.from ?? 'club';
  }

  create(): void {
    fitCamera(this);
    music.play('menu');
    this.busy = false;
    const nb = this.mode === 'notebooks';
    stadiumBackdrop(this, nb ? 0x7a5aa8 : THEME.yellow, nb ? THEME.cyan : THEME.orange);
    this.drawRays();
    if (PORTRAIT) return this.createMobile();
    topBar(this, {
      title: nb ? 'Cuadernos' : 'Fichajes',
      subtitle: nb ? 'Cuadernos de supertécnicas para Mi club' : 'Consigue jugadores para Mi club',
      back: { label: this.from === 'menu' ? 'Menú' : 'Mi club', onClick: () => this.back() },
      accent: nb ? 0x7a5aa8 : THEME.yellow,
    });
    // pestañas: jugadores o cuadernos
    (['players', 'notebooks'] as const).forEach((m, i) => {
      new Button(this, 560 + i * 150, 32, m === 'players' ? 'Jugadores' : 'Cuadernos', () => m !== this.mode && !this.busy && this.scene.restart({ mode: m, from: this.from }), {
        w: 140,
        h: 38,
        variant: m === this.mode ? 'primary' : 'secondary',
        size: 15,
      })
        .setSelected(m === this.mode)
        .setDepth(101);
    });
    this.coinsLabel = coinChip(this, GAME_W - 24, 32, 0).setDepth(101);
    this.drawCoins();
    const off = onClubChange(() => this.drawCoins());
    this.events.once(Phaser.Scenes.Events.SHUTDOWN, off);

    // probabilidades
    const g = this.add.graphics();
    cardPanel(g, 40, 100, 320, 214);
    sectionTitle(this, 56, 122, 'Probabilidades');
    const rates: [1 | 2 | 3 | 4, number][] = [
      [4, 2],
      [3, 10],
      [2, 28],
      [1, 60],
    ];
    rates.forEach(([r, pct], i) => {
      const y = 158 + i * 32;
      text(this, 60, y, '★'.repeat(r), 16, RARITY[r].css, { strokeThickness: 0 }).setOrigin(0, 0.5);
      label(this, 140, y, RARITY[r].name, 14, THEME.text, { fontStyle: 'bold' }).setOrigin(0, 0.5);
      const bar = this.add.graphics();
      bar.fillStyle(0x000000, 0.45).fillRoundedRect(250, y - 4, 60, 8, 4);
      bar.fillStyle(RARITY[r].color).fillRoundedRect(250, y - 4, Math.max(6, (60 * pct) / 60), 8, 4);
      label(this, 342, y, `${pct} %`, 13, THEME.text, { fontStyle: 'bold' }).setOrigin(1, 0.5);
    });
    label(this, 56, 292, nb ? 'La rareza depende de la potencia de la técnica' : 'Los repetidos devuelven monedas', 11, THEME.muted, { fontStyle: 'italic' }).setOrigin(0, 0.5);
    const g2 = this.add.graphics();
    cardPanel(g2, 40, 334, 320, 146);
    sectionTitle(this, 56, 356, 'Cómo ganar monedas');
    label(this, 56, 378, 'Por cada partido terminado:', 12, THEME.muted);
    label(this, 56, 400, 'Con Mi club', 13, THEME.text, { fontStyle: 'bold' });
    label(this, 344, 400, '150 ganar · 80 empatar · 50 perder', 12, THEME.yellowCss).setOrigin(1, 0);
    label(this, 56, 424, 'Con otros equipos', 13, THEME.text, { fontStyle: 'bold' });
    label(this, 344, 424, '40 · 30 · 20', 12, THEME.yellowCss).setOrigin(1, 0);
    label(this, 56, 452, 'Las 10 tiradas traen al menos un ★★★', 12, '#7dff9a', { fontStyle: 'italic bold' });

    this.stage = this.add.container(0, 0);
    this.idle();

    const [one, ten] = nb ? [NOTEBOOK_COST, TEN_NOTEBOOK_COST] : [PULL_COST, TEN_PULL_COST];
    this.buttons = [
      new Button(this, 200, 540, 'Una tirada', () => this.roll(1), { w: 320, h: 56, variant: 'primary', size: 20, sub: `${one} ●` }),
      new Button(this, 200, 608, 'Diez tiradas', () => this.roll(10), { w: 320, h: 56, color: THEME.orange, size: 20, sub: `${ten} ●  (ahorras ${one * 10 - ten})` }),
    ];
    label(this, 200, 652, 'Pulsa 1 o 0 en el teclado para tirar', 11, THEME.muted, { fontStyle: 'italic' }).setOrigin(0.5);
    this.drawCoins();
    const kb = this.input.keyboard;
    kb?.on('keydown-ESC', () => !this.busy && this.back());
    kb?.on('keydown-ONE', () => this.roll(1));
    kb?.on('keydown-ZERO', () => this.roll(10));
  }

  /** Fichajes en el móvil (vertical): cabecera, pestañas grandes, el balón y los dos botones de tirada abajo. */
  private createMobile(): void {
    const nb = this.mode === 'notebooks';
    clubMobileHeader(this, { title: nb ? 'Cuadernos' : 'Fichajes', subtitle: nb ? 'Supertécnicas para Mi club' : 'Jugadores para Mi club', onBack: () => !this.busy && this.back(), accent: nb ? 0x7a5aa8 : THEME.yellow });
    this.coinsLabel = coinChip(this, GAME_W - 12, CLUB_HEADER_H / 2, 0).setDepth(101);
    const off = onClubChange(() => this.drawCoins());
    this.events.once(Phaser.Scenes.Events.SHUTDOWN, off);
    const tw = (GAME_W - 32) / 2;
    (['players', 'notebooks'] as const).forEach((m, i) => {
      new Button(this, 12 + tw / 2 + i * (tw + 8), CLUB_HEADER_H + 46, m === 'players' ? 'Jugadores' : 'Cuadernos', () => m !== this.mode && !this.busy && this.scene.restart({ mode: m, from: this.from }), {
        w: tw,
        h: 64,
        variant: m === this.mode ? 'primary' : 'secondary',
        size: 20,
      })
        .setSelected(m === this.mode)
        .setDepth(101);
    });
    this.stage = this.add.container(0, 0);
    this.idle();
    // probabilidades: cuatro chapas en fila
    const rates: [1 | 2 | 3 | 4, number][] = [
      [4, 2],
      [3, 10],
      [2, 28],
      [1, 60],
    ];
    const g = this.add.graphics();
    cardPanel(g, 12, 650, GAME_W - 24, 112, { accent: nb ? 0x7a5aa8 : THEME.yellow });
    const cw = (GAME_W - 40) / 4;
    rates.forEach(([r, pct], i) => {
      const x = 20 + i * cw + cw / 2;
      text(this, x, 678, '★'.repeat(r), r === 4 ? 15 : 17, RARITY[r].css, { strokeThickness: 0 }).setOrigin(0.5);
      label(this, x, 706, `${pct} %`, 22, THEME.text, { fontStyle: 'bold' }).setOrigin(0.5);
    });
    label(this, GAME_W / 2, 742, nb ? 'La rareza depende de la potencia de la técnica' : 'Los repetidos devuelven monedas · 10 tiradas: al menos un ★★★', 15, THEME.muted, { fontStyle: 'italic' }).setOrigin(0.5);
    const [one, ten] = nb ? [NOTEBOOK_COST, TEN_NOTEBOOK_COST] : [PULL_COST, TEN_PULL_COST];
    this.buttons = [
      new Button(this, GAME_W / 2, 812, 'Una tirada', () => this.roll(1), { w: GAME_W - 40, h: 72, variant: 'primary', size: 24, sub: `${one} ●` }),
      new Button(this, GAME_W / 2, 898, 'Diez tiradas', () => this.roll(10), { w: GAME_W - 40, h: 72, color: THEME.orange, size: 24, sub: `${ten} ●  (ahorras ${one * 10 - ten})` }),
    ];
    this.drawCoins();
  }

  private back(): void {
    this.scene.start(this.from === 'menu' ? 'menu' : 'club');
  }

  private drawCoins(): void {
    const coins = loadClub()?.coins ?? 0;
    const x = this.coinsLabel?.x ?? GAME_W - 24;
    this.coinsLabel?.destroy();
    this.coinsLabel = coinChip(this, x, PORTRAIT ? CLUB_HEADER_H / 2 : 32, coins).setDepth(101);
    if (PORTRAIT) this.coinsLabel.setScale(1.15);
    const nb = this.mode === 'notebooks';
    this.buttons[0]?.setEnabled(coins >= (nb ? NOTEBOOK_COST : PULL_COST));
    this.buttons[1]?.setEnabled(coins >= (nb ? TEN_NOTEBOOK_COST : TEN_PULL_COST));
  }

  private drawRays(): void {
    const g = this.add.graphics();
    const { x: cx, y: cy } = STAGE;
    for (let i = 0; i < 36; i++) {
      const a = (i / 36) * Math.PI * 2;
      g.fillStyle(0xffffff, i % 2 ? 0.03 : 0.012);
      g.fillTriangle(cx, cy, cx + Math.cos(a) * 900, cy + Math.sin(a) * 900, cx + Math.cos(a + 0.09) * 900, cy + Math.sin(a + 0.09) * 900);
    }
    glow(g, cx, cy, 300, THEME.yellow, 0.1);
    this.tweens.add({ targets: g, alpha: 0.6, duration: 1500, yoyo: true, repeat: -1, ease: 'Sine.inOut' });
  }

  /** El balón en reposo: flota, gira despacio y le orbitan chispas, esperando una tirada. */
  private idle(): void {
    this.tweens.killTweensOf(this.stage.list);
    this.stage.removeAll(true);
    const ball = this.ball(STAGE.x, STAGE.y, 92);
    this.stage.add(ball.root);
    this.tweens.add({ targets: ball.body, y: -10, duration: 1400, yoyo: true, repeat: -1, ease: 'Sine.inOut' });
    this.tweens.add({ targets: ball.shadow, scaleX: 0.86, alpha: 0.5, duration: 1400, yoyo: true, repeat: -1, ease: 'Sine.inOut' });
    this.tweens.add({ targets: ball.pattern, angle: 360, duration: 14000, repeat: -1 });
    this.tweens.add({ targets: ball.halo, angle: -360, duration: 9000, repeat: -1 });
    this.tweens.add({ targets: ball.halo, alpha: 0.55, duration: 1100, yoyo: true, repeat: -1, ease: 'Sine.inOut' });
    this.tweens.add({ targets: ball.sparks, angle: 360, duration: 5000, repeat: -1 });
    this.stage.add(display(this, STAGE.x, STAGE.y + 150, '¡Haz una tirada!', PORTRAIT ? 38 : 34, '#ffffff').setOrigin(0.5));
    this.stage.add(
      label(this, STAGE.x, STAGE.y + (PORTRAIT ? 194 : 182), this.mode === 'notebooks' ? 'Los cuadernos se ponen a un jugador desde Mi club → Editar' : 'Los nuevos jugadores van a tu colección de Mi club', PORTRAIT ? 17 : 12, THEME.muted, {
        fontStyle: 'italic',
        align: 'center',
        wordWrap: PORTRAIT ? { width: GAME_W - 60 } : undefined,
      }).setOrigin(0.5),
    );
  }

  /**
   * Balón de verdad: esfera sombreada, costuras y pentágonos en perspectiva (los del borde, achatados), brillo
   * y un halo eléctrico detrás. Devuelve las piezas por separado para animarlas: el dibujo gira dentro del cuerpo,
   * y el sombreado y el brillo quedan fijos, así parece que gira una esfera.
   */
  private ball(x: number, y: number, r: number): { root: Phaser.GameObjects.Container; body: Phaser.GameObjects.Container; pattern: Phaser.GameObjects.Graphics; halo: Phaser.GameObjects.Graphics; sparks: Phaser.GameObjects.Container; shadow: Phaser.GameObjects.Graphics } {
    const root = this.add.container(x, y);
    // sombra en el suelo
    const shadow = this.add.graphics({ y: r + 26 });
    for (let i = 5; i >= 1; i--) shadow.fillStyle(0x000000, 0.1).fillEllipse(0, 0, r * 0.38 * i, r * 0.11 * i);
    root.add(shadow);
    // halo eléctrico: anillo con dientes, como una rueda de rayos
    const halo = this.add.graphics();
    glow(halo, 0, 0, r * 1.9, THEME.yellow, 0.22, 8);
    halo.lineStyle(3, THEME.yellow, 0.9);
    for (let i = 0; i < 18; i++) {
      const a = (i / 18) * Math.PI * 2;
      const r0 = r * 1.16;
      const r1 = r * (i % 3 ? 1.3 : 1.48);
      halo.lineBetween(Math.cos(a) * r0, Math.sin(a) * r0, Math.cos(a + 0.12) * r1, Math.sin(a + 0.12) * r1);
    }
    halo.lineStyle(2, 0xffffff, 0.5).strokeCircle(0, 0, r * 1.14);
    root.add(halo);
    const body = this.add.container(0, 0);
    root.add(body);
    // esfera: círculos concéntricos del claro al oscuro, desplazados hacia la luz (arriba a la izquierda)
    const sphere = this.add.graphics();
    const steps = 14;
    for (let i = 0; i < steps; i++) {
      const t = i / (steps - 1);
      const c = Phaser.Display.Color.Interpolate.ColorWithColor(Phaser.Display.Color.ValueToColor(0x7f8aa0), Phaser.Display.Color.ValueToColor(0xffffff), 100, t * 100);
      sphere.fillStyle(Phaser.Display.Color.GetColor(c.r, c.g, c.b)).fillCircle(-r * 0.22 * t, -r * 0.22 * t, r * (1 - t * 0.78));
    }
    body.add(sphere);
    // dibujo del balón (gira): pentágonos negros con perspectiva y costuras
    const pattern = this.add.graphics();
    const pent = (cx: number, cy: number, s: number, squash: number, rot: number) => {
      const d = Math.hypot(cx, cy);
      const ux = d ? cx / d : 1;
      const uy = d ? cy / d : 0;
      const pts: Phaser.Geom.Point[] = [];
      for (let i = 0; i < 5; i++) {
        const a = rot + (i * 2 * Math.PI) / 5;
        // se aplasta en la dirección radial (perspectiva de esfera)
        const px = Math.cos(a) * s;
        const py = Math.sin(a) * s;
        const rad = px * ux + py * uy;
        const tan = -px * uy + py * ux;
        pts.push(pt(cx + ux * rad * squash - uy * tan, cy + uy * rad * squash + ux * tan));
      }
      pattern.fillPoints(pts, true);
      pattern.lineStyle(1.5, 0x5a6478, 0.9).strokePoints(pts, true);
      return pts;
    };
    pattern.fillStyle(0x1b2230);
    const center = pent(0, 0, r * 0.3, 1, -Math.PI / 2);
    const ring: Phaser.Geom.Point[][] = [];
    for (let i = 0; i < 5; i++) {
      const a = -Math.PI / 2 + (i * 2 * Math.PI) / 5;
      ring.push(pent(Math.cos(a) * r * 0.72, Math.sin(a) * r * 0.72, r * 0.23, 0.55, a + Math.PI));
    }
    // costuras: del centro a cada pentágono y entre vecinos
    pattern.lineStyle(2.5, 0x1b2230, 0.6);
    for (let i = 0; i < 5; i++) {
      const c0 = center[(i + 1) % 5];
      const a = -Math.PI / 2 + (i * 2 * Math.PI) / 5;
      pattern.lineBetween(c0.x, c0.y, Math.cos(a) * r * 0.5, Math.sin(a) * r * 0.5);
      const b1 = ring[i][2];
      const b2 = ring[(i + 1) % 5][3];
      pattern.lineBetween(b1.x, b1.y, b2.x, b2.y);
    }
    body.add(pattern);
    // sombreado fijo encima: borde oscuro y brillo especular
    const shade = this.add.graphics();
    // borde oscuro hacia abajo a la derecha (anillos cada vez más pequeños, siempre dentro de la esfera)
    for (let i = 0; i < 4; i++) shade.lineStyle(r * 0.1, 0x0b1220, 0.07 + i * 0.03).strokeCircle(r * 0.03 * i, r * 0.03 * i, r - r * (0.05 + 0.07 * i));
    shade.fillStyle(0xffffff, 0.75).fillEllipse(-r * 0.4, -r * 0.46, r * 0.42, r * 0.22);
    shade.fillStyle(0xffffff, 0.35).fillEllipse(-r * 0.3, -r * 0.3, r * 0.9, r * 0.6);
    shade.lineStyle(3, 0x0b1220, 0.6).strokeCircle(0, 0, r);
    body.add(shade);
    // chispas que orbitan (en una elipse inclinada, por delante y por detrás del balón)
    const sparks = this.add.container(0, 0);
    for (let i = 0; i < 4; i++) {
      const a = (i / 4) * Math.PI * 2;
      const sp = this.add.graphics({ x: Math.cos(a) * r * 1.35, y: Math.sin(a) * r * 1.35 });
      sp.fillStyle(THEME.yellow, 0.9).fillCircle(0, 0, 5);
      sp.fillStyle(0xffffff).fillCircle(0, 0, 2.2);
      sparks.add(sp);
    }
    sparks.setScale(1, 0.45);
    root.add(sparks);
    return { root, body, pattern, halo, sparks, shadow };
  }

  private async roll(count: 1 | 10): Promise<void> {
    if (this.busy) return;
    const save = loadClub();
    const nb = this.mode === 'notebooks';
    const cost = count === 10 ? (nb ? TEN_NOTEBOOK_COST : TEN_PULL_COST) : nb ? NOTEBOOK_COST : PULL_COST;
    if (!save || save.coins < cost) return;
    this.busy = true;
    if (nb) {
      const books = pullNotebooks(count);
      if (books) {
        await this.charge(Math.max(...books.map((r) => r.rarity)));
        await this.revealNotebooks(books);
      }
      this.busy = false;
      return;
    }
    const results = await pull(count);
    if (!results) {
      this.busy = false;
      return;
    }
    await new Promise<void>((done) => loadCardPortraits(this, results.map((r) => r.card), done));
    await this.charge(Math.max(...results.map((r) => r.card.rarity)));
    await this.reveal(results);
    this.busy = false;
  }

  /** El balón gira cada vez más deprisa, tiembla, se carga de rayos del color de la mejor carta y estalla. */
  private async charge(best: number): Promise<void> {
    this.tweens.killTweensOf(this.stage.list);
    this.stage.removeAll(true);
    const color = RARITY[best as 1 | 2 | 3 | 4].color;
    const ball = this.ball(STAGE.x, STAGE.y, 92);
    this.stage.add(ball.root);
    const bolts = this.add.graphics();
    this.stage.add(bolts);
    // el balón sube, gira cada vez más rápido y el halo se enciende
    this.tweens.add({ targets: ball.body, y: -30, duration: 900, ease: 'Sine.inOut' });
    this.tweens.add({ targets: ball.shadow, scaleX: 0.7, alpha: 0.5, duration: 900 });
    this.tweens.add({ targets: ball.pattern, angle: 1800, duration: 1400, ease: 'Quad.in' });
    this.tweens.add({ targets: ball.halo, angle: -720, scale: 1.3, duration: 1400, ease: 'Quad.in' });
    this.tweens.add({ targets: ball.sparks, angle: 1080, scale: 1.4, duration: 1400, ease: 'Quad.in' });
    sfx.duelStart();
    for (let i = 0; i < 18; i++) {
      const k = i / 17;
      // cada rayo se pinta dos veces: un halo grueso de color y un núcleo fino blanco
      bolts.clear();
      const n = 3 + Math.floor(k * 7);
      const paths: [number, number][][] = [];
      for (let b = 0; b < n; b++) {
        const a = Math.random() * Math.PI * 2;
        let x = STAGE.x + Math.cos(a) * 100;
        let y = STAGE.y - 15 + Math.sin(a) * 100;
        const path: [number, number][] = [[x, y]];
        for (let st = 0; st < 5; st++) {
          x += Math.cos(a) * 30 + (Math.random() - 0.5) * 44;
          y += Math.sin(a) * 30 + (Math.random() - 0.5) * 44;
          path.push([x, y]);
        }
        paths.push(path);
      }
      for (const [width, col, alpha] of [
        [6 + k * 6, i > 9 ? color : THEME.yellow, 0.35],
        [2 + k * 2, 0xffffff, 0.95],
      ] as const) {
        bolts.lineStyle(width, col, alpha);
        for (const path of paths) {
          bolts.beginPath().moveTo(path[0][0], path[0][1]);
          for (const [px, py] of path.slice(1)) bolts.lineTo(px, py);
          bolts.strokePath();
        }
      }
      // tiembla cada vez más
      ball.body.setPosition((Math.random() - 0.5) * 10 * k, ball.body.y);
      ball.body.setScale(1 + k * 0.12);
      if (i > 10) this.cameras.main.shake(80, 0.002 * k);
      await wait(this, 75);
    }
    sfx.win();
    // estallido: destello, tres ondas de choque y chispas que salen disparadas (van fuera del escenario)
    const fx: Phaser.GameObjects.GameObject[] = [];
    const flash = this.add.circle(STAGE.x, STAGE.y - 15, 40, color, 1).setDepth(5);
    fx.push(flash);
    this.tweens.add({ targets: flash, scale: 24, alpha: 0, duration: 520, ease: 'Cubic.out' });
    for (let w = 0; w < 3; w++) {
      const ringG = this.add.graphics({ x: STAGE.x, y: STAGE.y - 15 }).setDepth(5);
      ringG.lineStyle(6 - w, w ? color : 0xffffff, 0.9).strokeCircle(0, 0, 60);
      fx.push(ringG);
      this.tweens.add({ targets: ringG, scale: 8 + w * 3, alpha: 0, duration: 650 + w * 150, delay: w * 90, ease: 'Cubic.out' });
    }
    for (let p = 0; p < 26; p++) {
      const a = Math.random() * Math.PI * 2;
      const d = 260 + Math.random() * 220;
      const spark = this.add.circle(STAGE.x, STAGE.y - 15, 3 + Math.random() * 4, p % 3 ? color : 0xffffff, 1).setDepth(5);
      fx.push(spark);
      this.tweens.add({ targets: spark, x: STAGE.x + Math.cos(a) * d, y: STAGE.y - 15 + Math.sin(a) * d + 120, scale: 0, duration: 600 + Math.random() * 400, ease: 'Cubic.out' });
    }
    this.cameras.main.shake(220, 0.006);
    this.time.delayedCall(1300, () => fx.forEach((o) => o.destroy()));
    ball.root.destroy();
    bolts.destroy();
    await wait(this, 380);
  }

  /** Coloca las 1 o 10 cartas y las va abriendo una a una. */
  private async revealItems<T>(items: T[], draw: (item: T, x: number, y: number, w: number, h: number) => Phaser.GameObjects.Container, tagOf: (item: T) => { text: string; isNew: boolean }, rarityOf: (item: T) => number): Promise<void> {
    this.tweens.killTweensOf(this.stage.list);
    this.stage.removeAll(true);
    const one = items.length === 1;
    // en el móvil: las 10 en dos filas de 5 encima de los botones
    const w = one ? 200 : PORTRAIT ? 100 : 126;
    const h = one ? 270 : PORTRAIT ? 136 : 168;
    items.forEach((it, i) => {
      const x = one ? STAGE.x : PORTRAIT ? 58 + (i % 5) * 106 : 540 + (i % 5) * 140;
      const y = one ? STAGE.y - 10 : PORTRAIT ? 256 + Math.floor(i / 5) * 196 : 210 + Math.floor(i / 5) * 212;
      const card = draw(it, x, y, w, h);
      card.setScale(0, 1);
      this.stage.add(card);
      const tag = tagOf(it);
      const big = one || PORTRAIT;
      const t = chip(this, x, y + h / 2 + 16, PORTRAIT && !one ? tag.text.replace('Ya tenías · ahora ', '').replace('Repetido · ', '') : tag.text, tag.isNew ? THEME.green : THEME.panelLight, {
        size: big ? (PORTRAIT ? 14 : 12) : 10,
        h: big ? (PORTRAIT ? 26 : 22) : 18,
        padX: 8,
        textColor: tag.isNew ? THEME.ink : THEME.muted,
      });
      t.setX(x - t.width / 2).setAlpha(0);
      this.stage.add(t);
      this.time.delayedCall(i * 160, () => {
        if (rarityOf(it) >= 3) sfx.cutin();
        else sfx.click();
        this.tweens.add({ targets: card, scaleX: 1, duration: 220, ease: 'Back.out' });
        this.tweens.add({ targets: t, alpha: 1, duration: 200, delay: 180 });
      });
    });
    const best = Math.max(...items.map(rarityOf));
    const summary = label(this, STAGE.x, PORTRAIT ? 616 : GAME_H - 40, best >= 4 ? '¡¡UNA ESTRELLA!!' : best >= 3 ? '¡Un jugador conocido!' : 'Sigue probando suerte', PORTRAIT ? 22 : 15, best >= 4 ? THEME.yellowCss : best >= 3 ? '#8fc6ff' : THEME.muted, { fontStyle: 'italic bold' })
      .setOrigin(0.5)
      .setAlpha(0);
    this.stage.add(summary);
    this.tweens.add({ targets: summary, alpha: 1, delay: items.length * 160 + 200, duration: 300 });
    await wait(this, items.length * 160 + 300);
  }

  private revealNotebooks(results: NotebookResult[]): Promise<void> {
    return this.revealItems(
      results,
      (r, x, y, w, h) => drawNotebook(this, x, y, r.move, r.rarity, w, h),
      (r) => ({ text: r.total > 1 ? `Ya tenías · ahora ×${r.total}` : '¡NUEVO!', isNew: r.total <= 1 }),
      (r) => r.rarity,
    );
  }

  private reveal(results: PullResult[]): Promise<void> {
    return this.revealItems(
      results,
      (r, x, y, w, h) => drawCard(this, x, y, r.card, w, h),
      (r) => ({ text: r.duplicate ? `Repetido · +${r.refund} ●` : '¡NUEVO!', isNew: !r.duplicate }),
      (r) => r.card.rarity,
    );
  }
}
