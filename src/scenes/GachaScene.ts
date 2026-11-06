import Phaser from 'phaser';
import { sfx } from '../audio/sfx';
import { music } from '../audio/music';
import { loadClub, NOTEBOOK_COST, onClubChange, pull, pullNotebooks, PULL_COST, TEN_NOTEBOOK_COST, TEN_PULL_COST, type NotebookResult, type PullResult } from '../club/club';
import { drawNotebook } from '../ui/notebook';
import { RARITY } from '../club/pool';
import { GAME_H, GAME_W } from '../config';
import { drawCard, loadCardPortraits } from '../ui/card';
import { THEME, cardPanel, chip, coinChip, fitCamera, glow, pt, sectionTitle, stadiumBackdrop, topBar } from '../ui/theme';
import { Button, display, label, text, wait } from '../ui/widgets';

type Mode = 'players' | 'notebooks';
const STAGE = { x: 820, y: 330 };

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

  private back(): void {
    this.scene.start(this.from === 'menu' ? 'menu' : 'club');
  }

  private drawCoins(): void {
    const coins = loadClub()?.coins ?? 0;
    const x = this.coinsLabel?.x ?? GAME_W - 24;
    this.coinsLabel?.destroy();
    this.coinsLabel = coinChip(this, x, 32, coins).setDepth(101);
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

  /** El balón en reposo, latiendo, esperando una tirada. */
  private idle(): void {
    this.tweens.killTweensOf(this.stage.list);
    this.stage.removeAll(true);
    const ball = this.ball(STAGE.x, STAGE.y, 90);
    this.tweens.add({ targets: ball, scale: 1.06, duration: 800, yoyo: true, repeat: -1, ease: 'Sine.inOut' });
    this.stage.add(ball);
    this.stage.add(display(this, STAGE.x, STAGE.y + 140, '¡Haz una tirada!', 34, '#ffffff').setOrigin(0.5));
    this.stage.add(label(this, STAGE.x, STAGE.y + 172, this.mode === 'notebooks' ? 'Los cuadernos se ponen a un jugador desde Mi club → Editar' : 'Los nuevos jugadores van a tu colección de Mi club', 12, THEME.muted, { fontStyle: 'italic' }).setOrigin(0.5));
  }

  private ball(x: number, y: number, r: number): Phaser.GameObjects.Container {
    const c = this.add.container(x, y);
    const g = this.add.graphics();
    g.fillStyle(0x000000, 0.35).fillEllipse(6, r + 14, r * 1.6, r * 0.35);
    g.fillStyle(0xd8dee8).fillCircle(0, 0, r);
    g.fillStyle(0xffffff).fillCircle(-r * 0.1, -r * 0.1, r * 0.88);
    g.fillStyle(0x1a1a1a);
    const pent = (px: number, py: number, s: number) =>
      g.fillPoints(Array.from({ length: 5 }, (_, i) => pt(px + Math.cos(-Math.PI / 2 + (i * 2 * Math.PI) / 5) * s, py + Math.sin(-Math.PI / 2 + (i * 2 * Math.PI) / 5) * s)), true);
    pent(0, 0, r * 0.3);
    for (let i = 0; i < 5; i++) {
      const a = -Math.PI / 2 + (i * 2 * Math.PI) / 5;
      pent(Math.cos(a) * r * 0.78, Math.sin(a) * r * 0.78, r * 0.2);
    }
    g.lineStyle(4, THEME.yellow).strokeCircle(0, 0, r);
    c.add(g);
    return c;
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

  /** El balón se carga de rayos del color de la mejor carta y estalla. */
  private async charge(best: number): Promise<void> {
    this.tweens.killTweensOf(this.stage.list);
    this.stage.removeAll(true);
    const color = RARITY[best as 1 | 2 | 3 | 4].color;
    const ball = this.ball(STAGE.x, STAGE.y, 90);
    this.stage.add(ball);
    const bolts = this.add.graphics();
    this.stage.add(bolts);
    sfx.duelStart();
    for (let i = 0; i < 10; i++) {
      bolts.clear().lineStyle(4, i > 5 ? color : 0xffffff, 0.9);
      for (let k = 0; k < 6; k++) {
        const a = Math.random() * Math.PI * 2;
        let x = STAGE.x + Math.cos(a) * 95;
        let y = STAGE.y + Math.sin(a) * 95;
        bolts.beginPath().moveTo(x, y);
        for (let s = 0; s < 4; s++) {
          x += Math.cos(a) * 30 + (Math.random() - 0.5) * 30;
          y += Math.sin(a) * 30 + (Math.random() - 0.5) * 30;
          bolts.lineTo(x, y);
        }
        bolts.strokePath();
      }
      ball.setScale(1 + i * 0.03).setAngle((Math.random() - 0.5) * 12);
      await wait(this, 70);
    }
    sfx.win();
    // el destello va fuera del escenario: se borra solo al acabar
    const flash = this.add.circle(STAGE.x, STAGE.y, 40, color, 1);
    this.tweens.add({ targets: flash, scale: 22, alpha: 0, duration: 500, onComplete: () => flash.destroy() });
    ball.destroy();
    bolts.destroy();
    await wait(this, 350);
  }

  /** Coloca las 1 o 10 cartas y las va abriendo una a una. */
  private async revealItems<T>(items: T[], draw: (item: T, x: number, y: number, w: number, h: number) => Phaser.GameObjects.Container, tagOf: (item: T) => { text: string; isNew: boolean }, rarityOf: (item: T) => number): Promise<void> {
    this.tweens.killTweensOf(this.stage.list);
    this.stage.removeAll(true);
    const one = items.length === 1;
    const w = one ? 200 : 126;
    const h = one ? 270 : 168;
    items.forEach((it, i) => {
      const x = one ? STAGE.x : 540 + (i % 5) * 140;
      const y = one ? STAGE.y - 10 : 210 + Math.floor(i / 5) * 212;
      const card = draw(it, x, y, w, h);
      card.setScale(0, 1);
      this.stage.add(card);
      const tag = tagOf(it);
      const t = chip(this, x, y + h / 2 + 16, tag.text, tag.isNew ? THEME.green : THEME.panelLight, { size: one ? 12 : 10, h: one ? 22 : 18, padX: 8, textColor: tag.isNew ? THEME.ink : THEME.muted });
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
    const summary = label(this, STAGE.x, GAME_H - 40, best >= 4 ? '¡¡UNA ESTRELLA!!' : best >= 3 ? '¡Un jugador conocido!' : 'Sigue probando suerte', 15, best >= 4 ? THEME.yellowCss : best >= 3 ? '#8fc6ff' : THEME.muted, { fontStyle: 'italic bold' })
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
