import Phaser from 'phaser';
import { uniformKit, type UniformColors } from '../club/uniforms';

const num = (c: [number, number, number]) => (c[0] << 16) | (c[1] << 8) | c[2];

/**
 * Dibujo de un uniforme (camiseta con mangas, pantalón y medias) centrado en (x, y), de `h` píxeles de alto: el de campo y,
 * si `gk`, el del portero al lado, más pequeño.
 */
export function kitIcon(scene: Phaser.Scene, x: number, y: number, colors: UniformColors, h = 100, gk = true): Phaser.GameObjects.Graphics {
  const g = scene.add.graphics();
  const one = (cx: number, top: number, s: number, keeper: boolean) => {
    const k = uniformKit(colors, keeper);
    const long = keeper ? colors.gkLongSleeve : colors.longSleeve || colors.suit;
    const longPants = keeper ? colors.gkLongPants : colors.longPants || colors.suit;
    const u = s / 100;
    g.lineStyle(Math.max(1.5, 3 * u), 0x10161f, 1);
    // mangas
    g.fillStyle(num(k.sleeve));
    const sl = long ? 44 : 22;
    g.fillPoints([new Phaser.Geom.Point(cx - 26 * u, top), new Phaser.Geom.Point(cx - 44 * u, top + sl * u), new Phaser.Geom.Point(cx - 34 * u, top + (sl + 6) * u), new Phaser.Geom.Point(cx - 20 * u, top + 14 * u)], true);
    g.strokePoints([new Phaser.Geom.Point(cx - 26 * u, top), new Phaser.Geom.Point(cx - 44 * u, top + sl * u), new Phaser.Geom.Point(cx - 34 * u, top + (sl + 6) * u), new Phaser.Geom.Point(cx - 20 * u, top + 14 * u)], true);
    g.fillPoints([new Phaser.Geom.Point(cx + 26 * u, top), new Phaser.Geom.Point(cx + 44 * u, top + sl * u), new Phaser.Geom.Point(cx + 34 * u, top + (sl + 6) * u), new Phaser.Geom.Point(cx + 20 * u, top + 14 * u)], true);
    g.strokePoints([new Phaser.Geom.Point(cx + 26 * u, top), new Phaser.Geom.Point(cx + 44 * u, top + sl * u), new Phaser.Geom.Point(cx + 34 * u, top + (sl + 6) * u), new Phaser.Geom.Point(cx + 20 * u, top + 14 * u)], true);
    // camiseta
    g.fillStyle(num(k.shirt));
    g.fillRoundedRect(cx - 24 * u, top, 48 * u, 46 * u, 6 * u);
    g.strokeRoundedRect(cx - 24 * u, top, 48 * u, 46 * u, 6 * u);
    if (!keeper && colors.vstripes) {
      g.fillStyle(num(k.vstripes));
      for (const dx of [-12, 4]) g.fillRect(cx + dx * u, top + 2 * u, 8 * u, 42 * u);
    }
    g.fillStyle(num(k.collar));
    g.fillTriangle(cx - 9 * u, top, cx + 9 * u, top, cx, top + 9 * u);
    // pantalón
    const sh = longPants ? 46 : 24;
    g.fillStyle(num(k.shorts));
    g.fillRect(cx - 24 * u, top + 46 * u, 23 * u, sh * u);
    g.fillRect(cx + 1 * u, top + 46 * u, 23 * u, sh * u);
    g.strokeRect(cx - 24 * u, top + 46 * u, 23 * u, sh * u);
    g.strokeRect(cx + 1 * u, top + 46 * u, 23 * u, sh * u);
    // medias
    if (!longPants) {
      g.fillStyle(num(k.sock));
      g.fillRect(cx - 20 * u, top + 72 * u, 14 * u, 22 * u);
      g.fillRect(cx + 6 * u, top + 72 * u, 14 * u, 22 * u);
      g.strokeRect(cx - 20 * u, top + 72 * u, 14 * u, 22 * u);
      g.strokeRect(cx + 6 * u, top + 72 * u, 14 * u, 22 * u);
    }
  };
  const s = h;
  if (gk) {
    one(x - s * 0.22, y - s / 2, s * 0.8, false);
    one(x + s * 0.42, y - s * 0.2, s * 0.5, true);
  } else one(x, y - s / 2, s * 0.95, false);
  return g;
}
