import type { PlayerData, TeamData } from '../data/types';
import { getFormation } from '../data/formations';
import { playerOverall } from './rating';

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

/** El mejor once para una formación: en cada hueco, el mejor jugador de ese puesto que quede; el resto, al banquillo. */
export function bestLineup(team: TeamData, lineup: Lineup): Lineup {
  const left = lineupPlayers(team, lineup).sort((a, b) => playerOverall(b) - playerOverall(a));
  const take = (pred: (p: PlayerData) => boolean): PlayerData | undefined => {
    const i = left.findIndex(pred);
    return i >= 0 ? left.splice(i, 1)[0] : undefined;
  };
  const order: string[] = [];
  for (const slot of getFormation(lineup.formationId).slots) {
    const p = take((x) => x.position === slot.pos) ?? take(() => true);
    if (p) order.push(p.id);
  }
  return { ...lineup, order: [...order, ...left.map((p) => p.id)] };
}
