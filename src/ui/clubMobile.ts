import Phaser from 'phaser';
import { DISPLAY, FONT, GAME_W, hex } from '../config';
import { THEME, coinChip } from './theme';

/** Alto de la cabecera de Mi club y Fichajes en el móvil (vertical). */
export const CLUB_HEADER_H = 76;

/**
 * Cabecera de móvil para Mi club y Fichajes: botón de volver grande, título y monedas a la derecha.
 * (La barra de arriba del ordenador, topBar, no cabe en 540 de ancho con todos sus botones.)
 */
export function clubMobileHeader(
  scene: Phaser.Scene,
  o: { title: string; subtitle?: string; onBack: () => void; accent?: number; coins?: number; icon?: string },
): Phaser.GameObjects.Container {
  const H = CLUB_HEADER_H;
  const c = scene.add.container(0, 0).setDepth(100);
  const g = scene.add.graphics();
  g.fillStyle(THEME.night, 0.9).fillRect(0, 0, GAME_W, H);
  g.fillStyle(0xffffff, 0.03).fillRect(0, 0, GAME_W, H / 2);
  g.lineStyle(1, 0xffffff, 0.1).lineBetween(0, H, GAME_W, H);
  g.fillStyle(o.accent ?? THEME.yellow).fillRect(0, H - 3, 160, 3);
  c.add(g);
  // volver: 60x60
  const back = scene.add.graphics();
  const drawBack = (on: boolean) => {
    back.clear().fillStyle(on ? THEME.yellow : THEME.panelLight, 1).fillRoundedRect(10, 8, 60, 60, 14);
    back.lineStyle(1, 0xffffff, on ? 0 : 0.15).strokeRoundedRect(10, 8, 60, 60, 14);
    back.lineStyle(4, on ? hex(THEME.ink) : 0xffffff).beginPath().moveTo(46, 24).lineTo(32, 38).lineTo(46, 52).strokePath();
  };
  drawBack(false);
  c.add(back);
  const zone = scene.add.zone(4, 2, 72, 72).setOrigin(0).setInteractive({ useHandCursor: true });
  zone.on('pointerdown', () => drawBack(true));
  zone.on('pointerout', () => drawBack(false));
  zone.on('pointerup', () => (drawBack(false), o.onBack()));
  c.add(zone);
  let x = 84;
  if (o.icon && scene.textures.exists(o.icon)) {
    c.add(scene.add.image(x + 22, H / 2, o.icon).setDisplaySize(44, 44));
    x += 54;
  }
  const title = scene.add.text(x, o.subtitle ? H / 2 - 11 : H / 2, o.title, { fontFamily: DISPLAY, fontSize: '34px', color: THEME.yellowCss }).setOrigin(0, 0.5).setLetterSpacing(1);
  c.add(title);
  if (o.subtitle) c.add(scene.add.text(x + 1, H / 2 + 17, o.subtitle, { fontFamily: FONT, fontSize: '15px', fontStyle: 'italic', color: THEME.muted }).setOrigin(0, 0.5));
  if (o.coins !== undefined) c.add(coinChip(scene, GAME_W - 12, H / 2, o.coins).setScale(1.15));
  return c;
}

export interface ScrollItem {
  x: number;
  y: number;
  w: number;
  h: number;
  onTap: () => void;
}

/**
 * Lista con scroll táctil: se arrastra con el dedo (con inercia) y los toques se reparten a los elementos
 * registrados con addItem (en coordenadas del contenido). Lo de fuera de la caja queda recortado.
 */
export class TouchScroller {
  readonly content: Phaser.GameObjects.Container;
  private items: ScrollItem[] = [];
  private total = 0;
  private offset = 0;
  private velocity = 0;
  private dragging = false;
  private startY = 0;
  private startOffset = 0;
  private moved = 0;
  private lastY = 0;
  private lastT = 0;
  private bar: Phaser.GameObjects.Graphics;
  private zone: Phaser.GameObjects.Zone;
  private maskShape: Phaser.GameObjects.Graphics;

  constructor(
    scene: Phaser.Scene,
    readonly x: number,
    readonly y: number,
    readonly w: number,
    readonly h: number,
    parent?: Phaser.GameObjects.Container,
  ) {
    this.content = scene.add.container(0, y);
    this.maskShape = scene.make.graphics({}, false);
    this.maskShape.fillStyle(0xffffff).fillRect(x, y, w, h);
    this.content.setMask(this.maskShape.createGeometryMask());
    this.bar = scene.add.graphics();
    this.zone = scene.add.zone(x, y, w, h).setOrigin(0).setInteractive();
    parent?.add([this.content, this.bar, this.zone]);
    this.zone.on('pointerdown', (p: Phaser.Input.Pointer) => {
      this.dragging = true;
      this.startY = p.y;
      this.lastY = p.y;
      this.lastT = scene.time.now;
      this.startOffset = this.offset;
      this.moved = 0;
      this.velocity = 0;
    });
    const move = (p: Phaser.Input.Pointer) => {
      if (!this.dragging || !p.isDown) return;
      const res = scene.cameras.main.zoom || 1;
      const dy = (p.y - this.startY) / res;
      this.moved = Math.max(this.moved, Math.abs(dy));
      const now = scene.time.now;
      if (now > this.lastT) this.velocity = ((p.y - this.lastY) / res / (now - this.lastT)) * 16;
      this.lastY = p.y;
      this.lastT = now;
      this.setOffset(this.startOffset - dy);
    };
    const up = (p: Phaser.Input.Pointer) => {
      if (!this.dragging) return;
      this.dragging = false;
      if (this.moved < 10) {
        this.velocity = 0;
        const w = scene.cameras.main.getWorldPoint(p.x, p.y);
        const cy = w.y - this.y + this.offset;
        const hit = this.items.find((it) => w.x >= it.x && w.x <= it.x + it.w && cy >= it.y && cy <= it.y + it.h);
        hit?.onTap();
      }
    };
    scene.input.on('pointermove', move);
    scene.input.on('pointerup', up);
    // rueda del ratón (para probar en el ordenador)
    const wheel = (_p: unknown, _o: unknown, _dx: number, dy: number) => this.setOffset(this.offset + dy * 0.6);
    this.zone.on('wheel', wheel);
    const tick = () => {
      if (this.dragging || Math.abs(this.velocity) < 0.2) return;
      this.setOffset(this.offset - this.velocity);
      this.velocity *= 0.92;
    };
    scene.events.on('update', tick);
    const cleanup = () => {
      scene.input.off('pointermove', move);
      scene.input.off('pointerup', up);
      scene.events.off('update', tick);
    };
    this.zone.once(Phaser.GameObjects.Events.DESTROY, () => {
      cleanup();
      this.maskShape.destroy();
    });
    scene.events.once(Phaser.Scenes.Events.SHUTDOWN, cleanup);
  }

  addItem(item: ScrollItem): void {
    this.items.push(item);
  }

  /** Alto total del contenido (para saber hasta dónde se puede bajar). */
  setTotal(total: number): void {
    this.total = total;
    this.setOffset(this.offset);
  }

  get scroll(): number {
    return this.offset;
  }

  setOffset(v: number): void {
    const max = Math.max(0, this.total - this.h);
    this.offset = Phaser.Math.Clamp(v, 0, max);
    this.content.y = this.y - this.offset;
    this.bar.clear();
    if (max > 0) {
      const bh = Math.max(40, (this.h * this.h) / this.total);
      const by = this.y + ((this.h - bh) * this.offset) / max;
      this.bar.fillStyle(0xffffff, 0.25).fillRoundedRect(this.x + this.w - 5, by, 4, bh, 2);
    }
  }

  destroy(): void {
    this.content.destroy();
    this.bar.destroy();
    this.zone.destroy();
  }
}
