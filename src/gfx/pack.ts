import { texKey } from './placeholders';

// Paquete de imágenes: basta con dejarlas en src/assets/pack/ con el id del jugador o del equipo como
// nombre (sprites/mark-evans.png, emblems/ie3-desert-lion.png, portraits/<equipo>/<jugador>.webp...).
// Vite las mete en el juego al compilar; lo que falte se dibuja por código.
const packFiles = import.meta.glob<string>('../assets/pack/{sprites,portraits,emblems}/**/*.{png,webp,gif,jpg,jpeg}', {
  eager: true,
  query: '?url',
  import: 'default',
});

interface PackEntry {
  key: string;
  url: string;
  folder: string;
}

const entries: PackEntry[] = Object.entries(packFiles).flatMap(([path, url]) => {
  const m = path.match(/\/(sprites|portraits|emblems)\/(?:([^/]+)\/)?([^/]+)\.\w+$/);
  if (!m) return [];
  const [, folder, team, name] = m;
  const id = name.toLowerCase();
  const key = folder === 'emblems' ? texKey.emblem(id) : folder === 'sprites' ? texKey.sprite(id, team) : texKey.portrait(id, team);
  return [{ key, url, folder }];
});

/** Lo que se carga al arrancar: sprites completos y escudos. */
export const bootPack = entries.filter((e) => e.folder !== 'portraits');

/** Retratos de Victory Road de los jugadores de unos equipos (se cargan al elegir equipos). */
export function portraitPack(teamIds: string[]): PackEntry[] {
  const keys = new Set(teamIds.map((t) => `portrait:${t}:`));
  return entries.filter((e) => e.folder === 'portraits' && [...keys].some((k) => e.key.startsWith(k)));
}
