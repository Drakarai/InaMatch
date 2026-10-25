import type { Element } from './types';

export const ELEMENT_LABEL: Record<Element, string> = {
  fire: 'Fuego',
  wind: 'Aire',
  wood: 'Bosque',
  earth: 'Montaña',
};

export const ELEMENT_COLOR: Record<Element, number> = {
  fire: 0xe8452c,
  wind: 0x3fa9f5,
  wood: 0x4cb848,
  earth: 0xe39b2d,
};

/**
 * Ciclo de ventajas: cada elemento gana al siguiente.
 * Ajustable aquí si se quiere cambiar el equilibrio.
 */
const BEATS: Record<Element, Element> = {
  fire: 'wood',
  wood: 'wind',
  wind: 'earth',
  earth: 'fire',
};

export const ELEMENT_ADVANTAGE = 1.2;

/** Multiplicador que recibe `attacker` frente a `defender`. */
export function elementMultiplier(attacker: Element, defender: Element): number {
  if (BEATS[attacker] === defender) return ELEMENT_ADVANTAGE;
  if (BEATS[defender] === attacker) return 1 / ELEMENT_ADVANTAGE;
  return 1;
}
