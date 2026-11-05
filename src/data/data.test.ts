import { describe, expect, it } from 'vitest';
import { MOVES, TEAMS, validateTeams } from '.';
import scouts from './scouts.json';
import type { PlayerData } from './types';
import { rarityOf } from '../club/pool';

describe('datos', () => {
  it('los equipos son válidos (portero primero, técnicas que existen, ids únicos)', () => {
    expect(validateTeams()).toEqual([]);
  });

  it('hay equipos de todas las temporadas', () => {
    for (const s of ['ie1', 'ie2', 'ie3', 'go', 'cs', 'gx', 'ares', 'orion', 'vr']) {
      expect(TEAMS.filter((t) => t.season === s).length).toBeGreaterThan(5);
    }
  });

  it('los ojeadores tienen puesto, atributos y técnicas que existen', () => {
    const all = Object.values(scouts as Record<string, PlayerData[]>).flat();
    expect(all.length).toBeGreaterThan(1000);
    for (const p of all) {
      expect(['GK', 'DF', 'MF', 'FW']).toContain(p.position);
      expect(Object.keys(p.stats)).toHaveLength(7);
      for (const m of p.moves) expect(MOVES[m], `${p.id}: ${m}`).toBeDefined();
    }
  });

  it('rareza según lo conocido que es el jugador', () => {
    expect(rarityOf(0)).toBe(1);
    expect(rarityOf(1)).toBe(2);
    expect(rarityOf(3)).toBe(3);
    expect(rarityOf(9)).toBe(4);
  });
});
