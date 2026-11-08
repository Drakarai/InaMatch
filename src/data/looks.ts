/** Rasgos de un jugador sacados de su retrato de Victory Road (tools/wiki/sprites.py). */
export interface Look {
  hair: string;
  skin: string;
  eyes: string;
  accessory?: string;
  /** Cabeza en una rejilla de 22x20: # pelo, s piel, e ojos, a accesorio, . vacío. */
  head: string[];
}

// 3,4 MB: solo hacen falta para el sprite de reserva de los jugadores sin sprite dibujado, así que se piden con los sprites
// de cada partido (loadLooks, desde ensureSprites) y no al arrancar
let LOOKS: Record<string, Look> = {};
let loading: Promise<void> | null = null;

export function loadLooks(): Promise<void> {
  loading ??= import('./looks.json').then((m) => {
    LOOKS = (m.default ?? m) as unknown as Record<string, Look>;
  });
  return loading;
}

export function lookOf(teamId: string, playerId: string): Look | undefined {
  return LOOKS[`${teamId}:${playerId}`];
}
