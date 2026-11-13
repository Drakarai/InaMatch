import Phaser from "phaser";
import { texKey } from "./placeholders";
import type { TeamData } from "../data/types";
import { loadLooks } from "../data/looks";
import { getUniform, makeUniformSprites } from "../club/uniforms";
import portraitIndex from "virtual:portrait-index";
import type { VspriteSet } from "virtual:vsprite-index";

// Paquete de imágenes: basta con dejarlas en src/assets/pack/ con el id del jugador o del equipo como
// nombre (sprites/mark-evans.png, emblems/ie3-desert-lion.png, portraits/<equipo>/<jugador>.webp...).
// Vite las mete en el juego al compilar; lo que falte se dibuja por código.
const packFiles = import.meta.glob<string>(
  "../assets/pack/{sprites,emblems}/**/*.{png,webp,gif,jpg,jpeg}",
  {
    eager: true,
    query: "?url",
    import: "default",
  },
);

export interface PackEntry {
  key: string;
  url: string;
  folder: string;
}

const entries: PackEntry[] = [
  ...Object.entries(packFiles).flatMap(([path, url]) => {
    const m = path.match(/\/(sprites|emblems)\/(?:([^/]+)\/)?([^/]+)\.\w+$/);
    if (!m) return [];
    const [, folder, team, name] = m;
    const id = name.toLowerCase();
    const key = folder === "emblems" ? texKey.emblem(id) : texKey.sprite(id, team);
    return [{ key, url, folder }];
  }),
  // los retratos, sin un módulo por imagen (vite-portraits.ts)
  ...Object.entries(portraitIndex).map(([path, url]) => {
    const [team, id] = path.split("/");
    return { key: texKey.portrait(id, team), url, folder: "portraits" };
  }),
];

// Logos de cada juego de la saga, de la enciclopedia oficial (zukan.inazuma.jp): series/<id>.png
const seriesFiles = import.meta.glob<string>("../assets/pack/series/*.png", {
  eager: true,
  query: "?url",
  import: "default",
});

/** Logos de los juegos, para las pestañas de temporada del menú. Clave: `series:<id>`. */
export const seriesPack: PackEntry[] = Object.entries(seriesFiles).map(
  ([path, url]) => ({
    key: `series:${path.match(/([^/]+)\.png$/)![1]}`,
    url,
    folder: "series",
  }),
);

// Sprites de partido dibujados (tools/pixelart/vector): vsprites/<equipo>/<jugador>/<vista>.png
// No se cargan al arrancar: van en trozos pequeños (uno por equipo y uno por ojeador, ver vite-vsprites.ts) y se piden
// antes de cada partido solo los de los jugadores que van a salir (ensureSprites).

/** Vistas de cada sprite dibujado: front, back, side0 (de perfil a la derecha), side1 y side2 (pasos). */
export const VSPRITE_VIEWS = ['front', 'back', 'side0', 'side1', 'side2'] as const;
export type VspriteView = (typeof VSPRITE_VIEWS)[number];
/** Altura en píxeles del cuerpo normal en los sprites dibujados (REF_PX de tools/pixelart/vector/export.py, menos el contorno). */
export const VSPRITE_REF = 78;
export const vspriteKey = (team: string, player: string, view: VspriteView) => `vsprite:${team}:${player}:${view}`;

type SetFiles = { files: Record<string, string> };
const unpacked = new Map<string, Promise<SetFiles>>();

/**
 * Las imágenes de un trozo de sprites (o de mapas): en desarrollo vienen en base64; en la web publicada, en un archivo
 * con todas seguidas que se baja una vez y se parte en imágenes (cada una con su url de objeto).
 */
function unpackSet(id: string, load: () => Promise<VspriteSet>): Promise<SetFiles> {
  let p = unpacked.get(id);
  if (!p) {
    p = load().then(async (m) => {
      if (m.files) return { files: m.files };
      if (!m.pack || !m.index) return { files: {} };
      const res = await fetch(m.pack);
      if (!res.ok) throw new Error(`no se pudo bajar ${m.pack}`);
      const buf = await res.arrayBuffer();
      const files: Record<string, string> = {};
      for (const [key, [off, len]] of Object.entries(m.index)) files[key] = URL.createObjectURL(new Blob([buf.slice(off, off + len)], { type: 'image/png' }));
      return { files };
    });
    // si falla (sin conexión), que se pueda volver a intentar
    p.catch(() => unpacked.delete(id));
    unpacked.set(id, p);
  }
  return p;
}

/** Carga (si no estaban) los sprites dibujados de los jugadores de estos equipos (los de Mi club, los de su equipo de origen). */
export async function ensureSprites(textures: Phaser.Textures.TextureManager, teams: TeamData[]): Promise<void> {
  const { sets, masks } = await import('virtual:vsprite-index');
  let missing = false; // algún jugador sin sprite dibujado: necesita los rasgos (looks.json, 3 MB) para el de reserva
  const wanted = new Map<string, Set<string>>(); // trozo -> '<equipo>/<jugador>'
  const setOf = (vteam: string, vid: string) => (vteam.startsWith('scouts-') ? `${vteam}/${vid}` : vteam);
  for (const team of teams) {
    for (const p of team.players) {
      const vteam = p.origin ?? team.id;
      const vid = p.originId ?? p.id;
      const set = setOf(vteam, vid);
      if (!sets[set]) {
        missing = true;
        continue;
      }
      // con uniforme hacen falta las imágenes aunque ya estén las texturas (para repintarlas)
      if (textures.exists(vspriteKey(vteam, vid, 'front')) && !team.uniform) continue;
      if (!wanted.has(set)) wanted.set(set, new Set());
      wanted.get(set)!.add(`${vteam}/${vid}`);
    }
  }
  if (missing) await loadLooks().catch(() => {});
  const empty = { files: {} as Record<string, string> };
  const mods = await Promise.all([...wanted.keys()].map((set) => unpackSet(`s:${set}`, sets[set]).catch(() => empty)));
  // Mi club con uniforme: sus jugadores, repintados con sus mapas de equipación
  for (const team of teams) {
    const uniform = getUniform(team.uniform);
    if (!uniform) continue;
    const own = [...new Set(team.players.map((p) => setOf(p.origin ?? team.id, p.originId ?? p.id)))].filter((s) => wanted.has(s));
    const keys = [...wanted.keys()];
    const files = Object.assign({}, ...own.map((s) => mods[keys.indexOf(s)].files)) as Record<string, string>;
    const maskMods = await Promise.all(own.map((s) => (masks[s] ? unpackSet(`m:${s.split("/")[0]}`, masks[s]).catch(() => empty) : Promise.resolve(empty))));
    const maskFiles = Object.assign({}, ...maskMods.map((m) => m.files)) as Record<string, string>;
    await makeUniformSprites(textures, team, uniform, files, maskFiles, (t, id, v) => vspriteKey(t, id, v as VspriteView));
  }
  const jobs: Promise<void>[] = [];
  [...wanted.values()].forEach((players, i) => {
    for (const [path, url] of Object.entries(mods[i].files)) {
      const [vteam, vid, view] = path.split('/');
      const key = vspriteKey(vteam, vid, view as VspriteView);
      if (!players.has(`${vteam}/${vid}`) || textures.exists(key)) continue;
      jobs.push(new Promise<void>((resolve) => {
        const img = new Image();
        img.onload = () => {
          if (!textures.exists(key)) textures.addImage(key, img)?.setFilter(Phaser.Textures.FilterMode.NEAREST);
          resolve();
        };
        img.onerror = () => resolve();
        img.src = url;
      }));
    }
  });
  await Promise.all(jobs);
}

/** Lo que se carga al arrancar: sprites completos y escudos (los dibujados, aparte: ensureSprites antes de cada partido). */
export const bootPack = [
  ...entries.filter((e) => e.folder !== "portraits"),
  ...seriesPack,
];

/** Retratos de Victory Road de los jugadores de unos equipos (se cargan al elegir equipos). */
export function portraitPack(teamIds: string[]): PackEntry[] {
  const keys = new Set(teamIds.map((t) => `portrait:${t}:`));
  return entries.filter(
    (e) =>
      e.folder === "portraits" && [...keys].some((k) => e.key.startsWith(k)),
  );
}

/** Retratos de unos jugadores concretos (los de "Mi club" o los que salen en el gacha). */
export function portraitsOf(
  players: { team: string; id: string }[],
): PackEntry[] {
  const keys = new Set(players.map((p) => texKey.portrait(p.id, p.team)));
  return entries.filter((e) => keys.has(e.key));
}
