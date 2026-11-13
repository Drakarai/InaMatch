/**
 * Modo historia, al estilo del modo Clásico de Smash: cada equipo tiene su propia ruta de partidos con diálogos.
 * - Los equipos protagonistas de cada juego (Raimon, Inazuma Japón...) siguen la historia original de su juego.
 * - El resto, una historia propia de 5 a 7 partidos a partir de lo que caracteriza a ese equipo.
 *
 * Las historias están en src/data/story/<temporada>.json ({ '<id de equipo>': Story }) y se cargan al abrir el modo.
 */

/** Una línea de diálogo. `who` es '<equipo>/<jugador>' (sale su retrato); `name`, alguien que no es jugador
 * (entrenadores, gerentes...); sin ninguno de los dos, el narrador. */
export interface StoryLine {
  who?: string;
  name?: string;
  text: string;
}

export interface StoryStage {
  /** Id del equipo rival (src/data/teams). */
  opponent: string;
  /** Título del capítulo, p. ej. "La maldición de Occult". */
  title: string;
  /** Diálogo antes del partido. */
  before: StoryLine[];
  /** Diálogo al ganarlo. */
  after: StoryLine[];
}

export interface Story {
  /** Título de la ruta. */
  title: string;
  /** Resumen de una o dos frases para la ficha de la ruta. */
  summary: string;
  /** Ruta de la historia original del juego (puede tener más de 7 partidos). */
  main?: boolean;
  intro: StoryLine[];
  stages: StoryStage[];
  ending: StoryLine[];
}

export type StoryBook = Record<string, Story>;

const files = import.meta.glob<{ default: StoryBook }>('../data/story/*.json');

let book: Promise<StoryBook> | null = null;

/** Todas las historias (se piden una vez, al entrar en el modo historia). */
export function loadStories(): Promise<StoryBook> {
  if (!book) {
    book = Promise.all(Object.values(files).map((load) => load().then((m) => m.default).catch(() => ({}) as StoryBook))).then((parts) =>
      Object.assign({}, ...parts),
    );
  }
  return book;
}

// --------------------------------------------------------------- progreso

export interface StoryProgress {
  /** Capítulo por el que va cada equipo (0 = el primero). */
  stage: Record<string, number>;
  /** Rutas terminadas (y cuántas veces). */
  done: Record<string, number>;
}

const KEY = 'inamatch-story';
let memory: StoryProgress | null = null;

export function loadProgress(): StoryProgress {
  if (memory) return memory;
  memory = { stage: {}, done: {} };
  try {
    const raw = window.localStorage.getItem(KEY);
    if (raw) {
      const saved = JSON.parse(raw) as Partial<StoryProgress>;
      memory = { stage: saved.stage ?? {}, done: saved.done ?? {} };
    }
  } catch {
    // sin almacenamiento: dura lo que la pestaña
  }
  return memory;
}

function save(p: StoryProgress): void {
  memory = p;
  try {
    window.localStorage.setItem(KEY, JSON.stringify(p));
  } catch {
    // sin almacenamiento
  }
}

export function setStage(team: string, stage: number): void {
  const p = loadProgress();
  save({ ...p, stage: { ...p.stage, [team]: stage } });
}

export function finishRoute(team: string): void {
  const p = loadProgress();
  save({ stage: { ...p.stage, [team]: 0 }, done: { ...p.done, [team]: (p.done[team] ?? 0) + 1 } });
}

/** Monedas para Mi club al terminar una ruta (la primera vez, más). */
export const ROUTE_COINS = { first: 600, again: 200 };

/** El partido de historia que se está jugando (lo leen la formación y el partido para volver a la historia). */
export interface StoryMatch {
  team: string;
  stage: number;
}
export const STORY_REGISTRY = 'storyMatch';
export const STORY_RESULT = 'storyResult';
