// Medidas y constantes globales.

/**
 * Versión de móvil: con la pantalla en vertical el juego se monta en 540x960 y cada escena usa su diseño vertical
 * (como una DS abierta: arriba el marcador, abajo el campo táctil). Se decide al cargar; si se gira el móvil, main.ts
 * recarga la página con el otro diseño.
 */
export const PORTRAIT = typeof window !== 'undefined' && window.innerHeight > window.innerWidth;

export const GAME_W = PORTRAIT ? 540 : 1280;
export const GAME_H = PORTRAIT ? 960 : 720;

/**
 * Resolución de dibujado: el lienzo se crea al tamaño real con el que se va a ver (pantalla y densidad de
 * píxeles) para que todo salga nítido. El juego sigue pensado en 1280x720: cada escena amplía su cámara
 * por este factor (ver fitCamera) y los textos se rasterizan a esta resolución.
 * Cambia al redimensionar la ventana (main.ts vuelve a crear el lienzo y avisa a las escenas).
 */
export function computeRes(): number {
  if (typeof window === 'undefined') return 1;
  const fit = Math.min(window.innerWidth / GAME_W, window.innerHeight / GAME_H);
  // sin redondear: así el lienzo coincide píxel a píxel con la ventana y no se reescala (lo que emborrona)
  const r = fit * (window.devicePixelRatio || 1);
  return Math.min(3, Math.max(0.5, Math.round(r * 1000) / 1000));
}

export let RES = computeRes();

export function setRes(r: number): void {
  RES = r;
}

/** Evento global (game.events) que se emite cuando cambia la resolución de dibujado. */
export const RES_EVENT = 'inamatch-res';

/** Zona del campo (la "pantalla táctil" de la DS): a la izquierda; en vertical, abajo. */
export const FIELD_VIEW = PORTRAIT ? { x: 0, y: 350, w: GAME_W, h: GAME_H - 350 } : { x: 0, y: 0, w: 820, h: 720 };
/** Zona del marcador y los duelos (la "pantalla superior"): a la derecha; en vertical, arriba. */
export const PANEL = PORTRAIT ? { x: 0, y: 0, w: GAME_W, h: 350 } : { x: 820, y: 0, w: GAME_W - 820, h: 720 };

/** Rectángulo del terreno de juego en coordenadas del mundo. */
export const PITCH = { x: 90, y: 110, w: 900, h: 1500 };
export const WORLD = { w: PITCH.x * 2 + PITCH.w, h: PITCH.y * 2 + PITCH.h };
export const GOAL_W = 180;
export const GOAL_DEPTH = 36;

/** Duración de cada parte: minutos que marca el reloj y segundos reales que dura. */
export const HALF_GAME_MINUTES = 30;
export const HALF_REAL_SECONDS = 105;

/** Ritmo del partido: multiplica la velocidad de jugadores y balón (1 = el ritmo original). */
export const GAME_SPEED = 0.75;

/** Letra de la interfaz: Barlow Semi Condensed, de rótulo deportivo (se carga antes de arrancar el juego, en main.ts). */
export const FONT = '"Barlow Semi Condensed", "Arial Narrow", Arial, sans-serif';
/** Letra de los rótulos grandes y marcadores: Bebas Neue, como en las retransmisiones deportivas. */
export const DISPLAY = '"Bebas Neue", "Barlow Semi Condensed", Impact, sans-serif';

export const COLORS = {
  panelBg: 0x2c4f7a,
  panelDark: 0x1b3352,
  panelLine: 0x6f9fd6,
  led: 0xffc93c,
  ledOff: 0x3a2c10,
  green: 0x3ec46d,
  fp: 0xff9a2a,
  tp: 0x5ed37a,
  white: 0xffffff,
  ui: 0x2f6fc4,
  uiRed: 0xd8344a,
};

export function hex(color: string): number {
  return parseInt(color.replace('#', ''), 16);
}
