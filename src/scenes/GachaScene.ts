import Phaser from 'phaser';
import { sfx } from '../audio/sfx';
import { loadClub, onClubChange, pull, PULL_COST, TEN_PULL_COST, type PullResult } from '../club/club';
import { RARITY } from '../club/pool';
import { GAME_H, GAME_W } from '../config';
import { drawCard, loadCardPortraits } from '../ui/card';
import { THEME, fitCamera, pt, sectionTitle, themePanel } from '../ui/theme';
import { Button, text, wait } from '../ui/widgets';

/**
 * Fichajes: tiradas de 1 o de 10 para conseguir jugadores para "Mi club". Cada tirada sale de un balón que se
 * carga de rayos; el color del destello avisa de lo mejor que ha salido.
 */
export class GachaScene extends Phaser.Scene {
  private coinsLabel!: Phaser.GameObjects.Text;
  private stage!: Phaser.GameObjects.Container;
  private buttons: Button[] = [];
  private busy = false;

  constructor() {
    super('gacha');
  }

  create(): void {
    fitCamera(this);
    this.busy = false;
    this.drawBackground();
    text(this, 40, 22, 'Fichajes', 34, '#ffd23f', { fontStyle: 'italic bold', strokeThickness: 7 });
    text(this, 42, 66, 'Consigue jugadores para Mi club', 15, '#ffffff', { fontStyle: 'italic' });
    this.coinsLabel = text(this, GAME_W - 40, 40, '', 24, '#ffd23f', { fontStyle: 'bold', strokeThickness: 5 }).setOrigin(1, 0.5);
    this.drawCoins();
    const off = onClubChange(() => this.drawCoins());
    this.events.once(Phaser.Scenes.Events.SHUTDOWN, off);

    // probabilidades
    const g = this.add.graphics();
    themePanel(g, 40, 120, 300, 230);
    sectionTitle(this, 56, 142, 'Probabilidades');
    const rates: [1 | 2 | 3 | 4, string][] = [
      [4, '2 %'],
      [3, '10 %'],
      [2, '28 %'],
      [1, '60 %'],
    ];
    rates.forEach(([r, pct], i) => {
      const y = 180 + i * 34;
      text(this, 60, y, '★'.repeat(r), 18, RARITY[r].css, { strokeThickness: 3 }).setOrigin(0, 0.5);
      text(this, 150, y, RARITY[r].name, 15, '#ffffff', { fontStyle: 'bold' }).setOrigin(0, 0.5);
      text(this, 320, y, pct, 15, '#ffffff', { fontStyle: 'bold' }).setOrigin(1, 0.5);
    });
    text(this, 60, 322, 'Repetidos: devuelven monedas', 12, THEME.muted, { fontStyle: 'italic', strokeThickness: 0 });
    const g2 = this.add.graphics();
    themePanel(g2, 40, 372, 300, 150);
    sectionTitle(this, 56, 394, 'Monedas');
    text(this, 60, 416, 'Por cada partido:\n· con Mi club: 150 ganando, 80 empatando, 50 perdiendo\n· con otros equipos: 20 a 40', 13, '#e3e9f2', {
      lineSpacing: 4,
      wordWrap: { width: 270 },
      strokeThickness: 0,
    });

    this.stage = this.add.container(0, 0);
    this.idle();

    this.buttons = [
      new Button(this, 190, 580, `Tirada · ${PULL_COST}`, () => this.roll(1), { w: 260, h: 54, color: THEME.yellow }),
      new Button(this, 190, 642, `10 tiradas · ${TEN_PULL_COST}`, () => this.roll(10), { w: 260, h: 54, color: 0xff7a3d }),
    ];
    text(this, 190, 686, 'Las 10 tiradas traen al menos un ★★★', 12, '#ffd23f', { fontStyle: 'italic', strokeThickness: 3 }).setOrigin(0.5);
    new Button(this, GAME_W - 130, 672, 'Mi club', () => this.scene.start('club'), { w: 200, h: 48, color: THEME.panelLight });
    this.input.keyboard?.on('keydown-ESC', () => this.scene.start('club'));
  }

  private drawCoins(): void {
    this.coinsLabel?.setText(`● ${loadClub()?.coins ?? 0} monedas`);
    const coins = loadClub()?.coins ?? 0;
    this.buttons[0]?.setEnabled(coins >= PULL_COST);
    this.buttons[1]?.setEnabled(coins >= TEN_PULL_COST);
  }

  private drawBackground(): void {
    const g = this.add.graphics();
    g.fillStyle(THEME.night).fillRect(0, 0, GAME_W, GAME_H);
    const cx = 800;
    const cy = 340;
    for (let i = 0; i < 36; i++) {
      const a = (i / 36) * Math.PI * 2;
      g.fillStyle(i % 2 ? 0x16233b : 0x0e182b);
      g.fillTriangle(cx, cy, cx + Math.cos(a) * 900, cy + Math.sin(a) * 900, cx + Math.cos(a + 0.18) * 900, cy + Math.sin(a + 0.18) * 900);
    }
    g.fillGradientStyle(0x000000, 0x000000, 0x000000, 0x000000, 0.6, 0.6, 0, 0).fillRect(0, 0, GAME_W, 100);
  }

  /** El balón en reposo, latiendo, esperando una tirada. */
  private idle(): void {
    this.tweens.killTweensOf(this.stage.list);
    this.stage.removeAll(true);
    const ball = this.ball(800, 330, 90);
    this.tweens.add({ targets: ball, scale: 1.06, duration: 800, yoyo: true, repeat: -1, ease: 'Sine.inOut' });
    this.stage.add(ball);
    this.stage.add(text(this, 800, 470, '¡Haz una tirada!', 26, '#ffffff', { fontStyle: 'italic bold', strokeThickness: 6 }).setOrigin(0.5));
  }

  private ball(x: number, y: number, r: number): Phaser.GameObjects.Container {
    const c = this.add.container(x, y);
    const g = this.add.graphics();
    g.fillStyle(0xffffff).fillCircle(0, 0, r);
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
    this.busy = true;
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
    const ball = this.ball(800, 330, 90);
    this.stage.add(ball);
    const bolts = this.add.graphics();
    this.stage.add(bolts);
    sfx.duelStart();
    for (let i = 0; i < 10; i++) {
      bolts.clear().lineStyle(4, i > 5 ? color : 0xffffff, 0.9);
      for (let k = 0; k < 6; k++) {
        const a = Math.random() * Math.PI * 2;
        let x = 800 + Math.cos(a) * 95;
        let y = 330 + Math.sin(a) * 95;
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
    const flash = this.add.circle(800, 330, 40, color, 1);
    this.tweens.add({ targets: flash, scale: 22, alpha: 0, duration: 500, onComplete: () => flash.destroy() });
    ball.destroy();
    bolts.destroy();
    await wait(this, 350);
  }

  private async reveal(results: PullResult[]): Promise<void> {
    this.tweens.killTweensOf(this.stage.list);
    this.stage.removeAll(true);
    const one = results.length === 1;
    const w = one ? 200 : 126;
    const h = one ? 270 : 168;
    results.forEach((r, i) => {
      const x = one ? 800 : 520 + (i % 5) * 140;
      const y = one ? 320 : 220 + Math.floor(i / 5) * 210;
      const card = drawCard(this, x, y, r.card, w, h);
      card.setScale(0, 1);
      this.stage.add(card);
      const tag = r.duplicate ? `Repetido · +${r.refund} ●` : '¡NUEVO!';
      const label = text(this, x, y + h / 2 + 14, tag, one ? 16 : 12, r.duplicate ? THEME.muted : '#7dff9a', { fontStyle: 'bold' }).setOrigin(0.5).setAlpha(0);
      this.stage.add(label);
      this.time.delayedCall(i * 160, () => {
        if (r.card.rarity >= 3) sfx.cutin();
        else sfx.click();
        this.tweens.add({ targets: card, scaleX: 1, duration: 220, ease: 'Back.out' });
        this.tweens.add({ targets: label, alpha: 1, duration: 200, delay: 180 });
      });
    });
    await wait(this, results.length * 160 + 300);
  }
}
