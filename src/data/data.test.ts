import { describe, expect, it } from 'vitest';
import { MOVES, TEAMS, validateTeams } from '.';
import scouts from './scouts.json';
import type { PlayerData } from './types';
import { rarityOf } from '../club/pool';
import { START_UNIFORMS, UNIFORMS, getUniform, uniformKit } from '../club/uniforms';

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

  it('los uniformes de Victory Road tienen colores válidos y los iniciales existen', () => {
    expect(UNIFORMS.length).toBe(177);
    expect(new Set(UNIFORMS.map((u) => u.id)).size).toBe(UNIFORMS.length);
    for (const id of START_UNIFORMS) expect(getUniform(id), id).toBeDefined();
    for (const u of UNIFORMS) {
      for (const gk of [false, true]) {
        for (const c of Object.values(uniformKit(u.colors, gk))) {
          expect(c.every((v) => Number.isInteger(v) && v >= 0 && v <= 255), u.id).toBe(true);
        }
      }
    }
  });
});
