import type { PlayerData, TeamData } from '../data/types';

/** Alineación elegida en la pantalla de formación. */
export interface Lineup {
  teamId: string;
  formationId: string;
  /** Todos los ids de la plantilla: los 11 primeros son titulares, el resto banquillo. */
  order: string[];
}

export function defaultLineup(team: TeamData): Lineup {
  return { teamId: team.id, formationId: team.formation, order: team.players.map((p) => p.id) };
}

export function lineupPlayers(team: TeamData, lineup: Lineup): PlayerData[] {
  const byId = new Map(team.players.map((p) => [p.id, p]));
  return lineup.order.map((id) => byId.get(id)).filter((p): p is PlayerData => !!p);
}

export function swapInLineup(lineup: Lineup, a: number, b: number): Lineup {
  const order = [...lineup.order];
  [order[a], order[b]] = [order[b], order[a]];
  return { ...lineup, order };
}
