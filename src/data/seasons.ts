import type { TeamData } from './types';

/** Temporadas del menú, como las ligas de un FIFA: cada juego de la saga con sus equipos. */
export interface Season {
  id: string;
  name: string;
  short: string;
}

export const SEASONS: Season[] = [
  { id: 'ie1', name: 'Inazuma Eleven', short: 'IE1' },
  { id: 'ie2', name: 'Inazuma Eleven 2', short: 'IE2' },
  { id: 'ie3', name: 'Inazuma Eleven 3', short: 'IE3' },
  { id: 'otros', name: 'Otros equipos', short: '+' },
];

export function seasonOf(team: TeamData): string {
  return team.season ?? 'otros';
}

export function getSeason(id: string): Season {
  return SEASONS.find((s) => s.id === id) ?? SEASONS[SEASONS.length - 1];
}
