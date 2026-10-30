// Medidas y constantes globales.

export const GAME_W = 1280;
export const GAME_H = 720;

/** Zona de la izquierda: el campo (la "pantalla táctil" de la DS). */
export const FIELD_VIEW = { x: 0, y: 0, w: 820, h: 720 };
/** Zona de la derecha: marcador y duelos (la "pantalla superior"). */
export const PANEL = { x: 820, y: 0, w: GAME_W - 820, h: 720 };

/** Rectángulo del terreno de juego en coordenadas del mundo. */
export const PITCH = { x: 90, y: 110, w: 900, h: 1500 };
export const WORLD = { w: PITCH.x * 2 + PITCH.w, h: PITCH.y * 2 + PITCH.h };
export const GOAL_W = 180;
export const GOAL_DEPTH = 36;

/** Duración de cada parte: minutos que marca el reloj y segundos reales que dura. */
export const HALF_GAME_MINUTES = 30;
export const HALF_REAL_SECONDS = 210;

/** Ritmo del partido: multiplica la velocidad de jugadores y balón (1 = el ritmo original). */
export const GAME_SPEED = 0.75;

export const FONT = '"Trebuchet MS", "Arial Black", Arial, sans-serif';

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
