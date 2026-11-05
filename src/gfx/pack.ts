import { texKey } from "./placeholders";

// Paquete de imágenes: basta con dejarlas en src/assets/pack/ con el id del jugador o del equipo como
// nombre (sprites/mark-evans.png, emblems/ie3-desert-lion.png, portraits/<equipo>/<jugador>.webp...).
// Vite las mete en el juego al compilar; lo que falte se dibuja por código.
const packFiles = import.meta.glob<string>(
  "../assets/pack/{sprites,portraits,emblems}/**/*.{png,webp,gif,jpg,jpeg}",
  {
    eager: true,
    query: "?url",
    import: "default",
  },
);

interface PackEntry {
  key: string;
  url: string;
  folder: string;
}

const entries: PackEntry[] = Object.entries(packFiles).flatMap(
  ([path, url]) => {
    const m = path.match(
      /\/(sprites|portraits|emblems)\/(?:([^/]+)\/)?([^/]+)\.\w+$/,
    );
    if (!m) return [];
    const [, folder, team, name] = m;
    const id = name.toLowerCase();
    const key =
      folder === "emblems"
        ? texKey.emblem(id)
        : folder === "sprites"
          ? texKey.sprite(id, team)
          : texKey.portrait(id, team);
    return [{ key, url, folder }];
  },
);

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
const vspriteFiles = import.meta.glob<string>('../assets/pack/vsprites/*/*/*.png', { eager: true, query: '?url', import: 'default' });

/** Vistas de cada sprite dibujado: front, back, side0 (de perfil a la derecha), side1 y side2 (pasos). */
export const VSPRITE_VIEWS = ['front', 'back', 'side0', 'side1', 'side2'] as const;
export type VspriteView = (typeof VSPRITE_VIEWS)[number];
/** Altura en píxeles del cuerpo normal en los sprites dibujados (REF_PX de tools/pixelart/vector/export.py, menos el contorno). */
export const VSPRITE_REF = 78;
export const vspriteKey = (team: string, player: string, view: VspriteView) => `vsprite:${team}:${player}:${view}`;

export const vspritePack: PackEntry[] = Object.entries(vspriteFiles).flatMap(([path, url]) => {
  const m = path.match(/vsprites\/([^/]+)\/([^/]+)\/([^/]+)\.png$/);
  return m ? [{ key: vspriteKey(m[1], m[2], m[3] as VspriteView), url, folder: 'vsprites' }] : [];
});

/** Lo que se carga al arrancar: sprites completos y escudos. */
export const bootPack = [
  ...entries.filter((e) => e.folder !== "portraits"),
  ...seriesPack,
  ...vspritePack,
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
