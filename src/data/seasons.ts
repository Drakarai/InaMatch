import type { TeamData } from './types';

/** Temporadas del menú, como las ligas de un FIFA: cada juego de la saga con sus equipos. */
export interface Season {
  id: string;
  name: string;
  short: string;
}

export const SEASONS: Season[] = [
  { id: 'club', name: 'Mi club', short: 'Mi club' },
  { id: 'ie1', name: 'Inazuma Eleven', short: 'IE1' },
  { id: 'ie2', name: 'Inazuma Eleven 2', short: 'IE2' },
  { id: 'ie3', name: 'Inazuma Eleven 3', short: 'IE3' },
  { id: 'go', name: 'Inazuma Eleven GO', short: 'GO' },
  { id: 'cs', name: 'Inazuma Eleven GO Chrono Stone', short: 'Chrono' },
  { id: 'gx', name: 'Inazuma Eleven GO Galaxy', short: 'Galaxy' },
  { id: 'ares', name: 'Inazuma Eleven Ares', short: 'Ares' },
  { id: 'orion', name: 'Inazuma Eleven Orión', short: 'Orión' },
  { id: 'vr', name: 'Inazuma Eleven Victory Road', short: 'VR' },
  { id: 'otros', name: 'Otros equipos', short: '+' },
];

export function seasonOf(team: TeamData): string {
  return team.season ?? 'otros';
}

export function getSeason(id: string): Season {
  return SEASONS.find((s) => s.id === id) ?? SEASONS[SEASONS.length - 1];
}
