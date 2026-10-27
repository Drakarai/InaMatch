import movesJson from './moves.json';
import moveFxJson from './movefx.json';
import type { FxName } from '../gfx/fx';
import { getFormation } from './formations';
import type { MoveData, TeamData } from './types';

// Cualquier .json que se añada a src/data/teams/ aparece automáticamente en el menú
const teamModules = import.meta.glob<{ default: TeamData }>('./teams/*.json', { eager: true });

export const MOVES: Record<string, MoveData> = Object.fromEntries(
  (movesJson as MoveData[]).map((m) => [m.id, m]),
);

export const TEAMS: TeamData[] = Object.values(teamModules)
  .map((m) => m.default)
  .sort((a, b) => a.name.localeCompare(b.name));

export function getTeam(id: string): TeamData {
  const t = TEAMS.find((team) => team.id === id);
  if (!t) throw new Error(`Equipo desconocido: ${id}`);
  return t;
}

/** Efecto especial de cada técnica (src/data/movefx.json, de tools/wiki/vfx.py). */
export function moveFx(id: string): FxName {
  return ((moveFxJson as Record<string, string>)[id] ?? 'impact') as FxName;
}

export function movesOf(ids: string[]): MoveData[] {
  return ids.map((id) => MOVES[id]).filter((m): m is MoveData => !!m);
}

/** Errores de datos (técnicas inexistentes, plantillas cortas...), útil para tests. */
export function validateTeams(teams: TeamData[] = TEAMS): string[] {
  const errors: string[] = [];
  for (const t of teams) {
    if (t.players.length < 11) errors.push(`${t.id}: necesita al menos 11 jugadores`);
    const formation = getFormation(t.formation);
    if (formation.id !== t.formation) errors.push(`${t.id}: formación desconocida ${t.formation}`);
    const ids = new Set<string>();
    t.players.forEach((p, i) => {
      if (ids.has(p.id)) errors.push(`${t.id}: id repetido ${p.id}`);
      ids.add(p.id);
      for (const m of p.moves) if (!MOVES[m]) errors.push(`${t.id}/${p.id}: técnica desconocida ${m}`);
      if (i === 0 && p.position !== 'GK') errors.push(`${t.id}: el primer jugador debe ser el portero`);
    });
  }
  return errors;
}
