import looksJson from './looks.json';

/** Rasgos de un jugador sacados de su retrato de Victory Road (tools/wiki/sprites.py). */
export interface Look {
  hair: string;
  skin: string;
  eyes: string;
  accessory?: string;
  /** Cabeza en una rejilla de 22x20: # pelo, s piel, e ojos, a accesorio, . vacío. */
  head: string[];
}

const LOOKS = looksJson as Record<string, Look>;

export function lookOf(teamId: string, playerId: string): Look | undefined {
  return LOOKS[`${teamId}:${playerId}`];
}
