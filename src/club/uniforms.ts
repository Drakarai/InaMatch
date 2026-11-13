import type Phaser from 'phaser';
import list from '../data/uniforms.json';
import type { TeamData } from '../data/types';

/**
 * Uniformes de Victory Road (src/data/uniforms.json, de la lista de la wiki inglesa): Mi club empieza con los dos básicos
 * y gana uno nuevo al azar en cada victoria. Los jugadores del club salen al campo con el que lleve puesto.
 *
 * Los sprites dibujados ya traen la equipación de su equipo; para vestirlos con otra se usa el mapa de equipación de
 * cada sprite (mask-<vista>.png, de tools/pixelart/vector/masks.py): en cada píxel de ropa, R = 16 * papel y
 * G = 255 * tono. Se repintan esos píxeles con los colores del uniforme (los mismos cálculos que kit_for de body.py).
 */

export interface UniformColors {
  shirt: string;
  shorts: string;
  gkShirt: string;
  accent: string;
  sleeve?: string;
  socks?: string;
  gkShorts?: string;
  gkSleeve?: string;
  gkSocks?: string;
  gkGloves?: string;
  collar?: string;
  num?: string;
  stripe?: string;
  pants?: string;
  vstripes?: string;
  zig?: string;
  longSleeve?: boolean;
  longPants?: boolean;
  gkLongSleeve?: boolean;
  gkLongPants?: boolean;
  suit?: boolean;
  /** Pantalón del portero (si no es el del equipo), rayas del portero, rayas horizontales, guantes de los de campo y botas. */
  gkPants?: string;
  gkVstripes?: string;
  hstripes?: string;
  gkHstripes?: string;
  gloves?: string;
  boots?: string;
}

export interface Uniform {
  id: string;
  name: string;
  /** Equipo del juego cuyo uniforme es (si lo hay). */
  team?: string;
  colors: UniformColors;
}

export const UNIFORMS = list as Uniform[];
const BY_ID = new Map(UNIFORMS.map((u) => [u.id, u]));
export const getUniform = (id: string | undefined): Uniform | undefined => (id ? BY_ID.get(id) : undefined);
/** Los dos que da el juego desde el principio. */
export const START_UNIFORMS = ['simple', 'normal'];

/** Papeles de la equipación, en el orden de ROLES de masks.py (el papel i va como R = 16 * (i + 1)). */
const ROLES = ['shirt', 'sleeve', 'shorts', 'sock', 'stripe', 'collar', 'num', 'zig', 'vstripes', 'pants', 'hand', 'hstripes'] as const;
type Role = (typeof ROLES)[number];
type RGB = [number, number, number];

const hex = (h: string): RGB => [parseInt(h.slice(1, 3), 16), parseInt(h.slice(3, 5), 16), parseInt(h.slice(5, 7), 16)];
const tone = (c: RGB, f: number): RGB => [Math.min(255, Math.floor(c[0] * f)), Math.min(255, Math.floor(c[1] * f)), Math.min(255, Math.floor(c[2] * f))];

/** Color de cada papel con este uniforme (como kit_for de body.py). */
export function uniformKit(c: UniformColors, gk: boolean): Record<Role, RGB> {
  const shirt = hex(gk ? c.gkShirt : c.shirt);
  const shorts = hex(gk && c.gkShorts ? c.gkShorts : c.shorts);
  const sleeve = gk ? (c.gkSleeve ? hex(c.gkSleeve) : tone(shirt, 0.72)) : c.sleeve ? hex(c.sleeve) : shorts;
  let sock: RGB = c.socks ? hex(c.socks) : [246, 246, 246];
  if (gk && c.gkSocks) sock = hex(c.gkSocks);
  const accent = hex(c.accent);
  const longPants = !!c.suit && !gk ? true : gk ? !!c.gkLongPants : !!c.longPants;
  const pants = gk && c.gkPants ? hex(c.gkPants) : c.pants ? hex(c.pants) : shorts;
  const pick = (k: 'collar' | 'num' | 'stripe') => (c[k] && !(gk && k === 'collar') ? hex(c[k]!) : null);
  const collar = pick('collar') ?? (c.sleeve ? accent : sleeve);
  const num = pick('num') ?? (c.sleeve ? accent : sleeve);
  const stripe = pick('stripe') ?? (c.sleeve ? accent : shorts);
  return {
    shirt,
    sleeve,
    shorts: longPants ? pants : shorts,
    // con pantalón largo, las medias del sprite se pintan como el pantalón
    sock: longPants ? pants : sock,
    stripe: longPants ? pants : stripe,
    collar,
    num,
    zig: c.zig && !gk ? hex(c.zig) : shirt,
    vstripes: gk ? (c.gkVstripes ? hex(c.gkVstripes) : shirt) : c.vstripes ? hex(c.vstripes) : shirt,
    hstripes: gk ? (c.gkHstripes ? hex(c.gkHstripes) : shirt) : c.hstripes ? hex(c.hstripes) : shirt,
    pants: longPants ? pants : shorts,
    hand: gk ? (c.gkGloves ? hex(c.gkGloves) : [246, 246, 246]) : c.gloves ? hex(c.gloves) : [246, 246, 246],
  };
}

/** Repinta la ropa de un sprite con su mapa de equipación. */
function recolor(sprite: HTMLImageElement, mask: HTMLImageElement, kit: Record<Role, RGB>): HTMLCanvasElement {
  const w = sprite.naturalWidth;
  const h = sprite.naturalHeight;
  const canvas = document.createElement('canvas');
  canvas.width = w;
  canvas.height = h;
  const ctx = canvas.getContext('2d', { willReadFrequently: true })!;
  ctx.drawImage(mask, 0, 0);
  const m = ctx.getImageData(0, 0, w, h).data;
  ctx.clearRect(0, 0, w, h);
  ctx.drawImage(sprite, 0, 0);
  const img = ctx.getImageData(0, 0, w, h);
  const px = img.data;
  for (let i = 0; i < px.length; i += 4) {
    const r = Math.round(m[i] / 16);
    if (!r || !px[i + 3]) continue;
    const role = ROLES[r - 1];
    if (!role) continue;
    const c = tone(kit[role], m[i + 1] / 255);
    px[i] = c[0];
    px[i + 1] = c[1];
    px[i + 2] = c[2];
  }
  ctx.putImageData(img, 0, 0);
  return canvas;
}

const loadImg = (url: string) =>
  new Promise<HTMLImageElement | null>((resolve) => {
    const img = new Image();
    img.onload = () => resolve(img);
    img.onerror = () => resolve(null);
    img.src = url;
  });

/** Equipo de los sprites con uniforme: '<equipo de origen>~<uniforme>'. */
export const uniformTeam = (team: string, uniform: string) => `${team}~${uniform}`;

/**
 * Crea las texturas de los jugadores de un equipo con uniforme (Mi club), a partir de las imágenes de sus sprites y de sus
 * mapas: `files` y `masks` son '<equipo>/<jugador>/<vista>' -> url.
 */
export async function makeUniformSprites(
  textures: Phaser.Textures.TextureManager,
  team: TeamData,
  uniform: Uniform,
  files: Record<string, string>,
  masks: Record<string, string>,
  key: (team: string, player: string, view: string) => string,
): Promise<void> {
  const jobs: Promise<void>[] = [];
  for (const p of team.players) {
    const vteam = p.origin ?? team.id;
    const vid = p.originId ?? p.id;
    const kit = uniformKit(uniform.colors, p.position === 'GK');
    for (const [path, url] of Object.entries(files)) {
      const [t, id, view] = path.split('/');
      if (t !== vteam || id !== vid) continue;
      const k = key(uniformTeam(vteam, uniform.id), vid, view);
      const maskUrl = masks[path];
      if (textures.exists(k) || !maskUrl) continue;
      jobs.push(
        Promise.all([loadImg(url), loadImg(maskUrl)]).then(([sprite, mask]) => {
          if (!sprite || !mask || textures.exists(k)) return;
          textures.addCanvas(k, recolor(sprite, mask, kit))?.setFilter(1 /* Phaser.Textures.FilterMode.NEAREST */);
        }),
      );
    }
  }
  await Promise.all(jobs);
}
