import type { Element } from './types';

export const ELEMENT_LABEL: Record<Element, string> = {
  fire: 'Fuego',
  wind: 'Aire',
  wood: 'Bosque',
  earth: 'Montaña',
  neutral: 'Neutro',
};

export const ELEMENT_COLOR: Record<Element, number> = {
  fire: 0xe8452c,
  wind: 0x3fa9f5,
  wood: 0x4cb848,
  earth: 0xe39b2d,
  neutral: 0x9b59d0,
};

/**
 * Ciclo de afinidades: Bosque > Aire > Montaña > Fuego > Bosque.
 * Neutro va aparte: ni gana ni pierde contra nadie y no tiene STAB.
 */
const BEATS: Partial<Record<Element, Element>> = {
  wood: 'wind',
  wind: 'earth',
  earth: 'fire',
  fire: 'wood',
};

// Valores ajustables: los juegos no publican las cifras exactas.
/** Ventaja de afinidad (se aplica una vez por jugadores y otra por técnicas). */
export const ELEMENT_ADVANTAGE = 1.2;
/** STAB: técnica del mismo elemento que el jugador que la usa. */
export const SAME_ELEMENT_BONUS = 1.25;

/** Multiplicador que recibe `attacker` frente a `defender`. */
export function elementMultiplier(attacker: Element, defender: Element): number {
  if (BEATS[attacker] === defender) return ELEMENT_ADVANTAGE;
  if (BEATS[defender] === attacker) return 1 / ELEMENT_ADVANTAGE;
  return 1;
}

/** STAB: la técnica es del mismo elemento que el jugador (el neutro no cuenta). */
export function hasStab(player: Element, move: Element): boolean {
  return player === move && player !== 'neutral';
}
