import { describe, expect, it } from 'vitest';
import { MOVES } from '../data';
import type { MoveData } from '../data/types';
import { filterCards, filterMoves, paginate, progressLabel, type CodexCard } from './codex';

const card = (key: string, name: string, season: string, rarity: number, position: CodexCard['player']['position']): CodexCard => ({ key, season, rarity, player: { name, position } });

const CARDS = [
  card('t:a', 'Álvaro', 'ie1', 2, 'FW'),
  card('t:b', 'Bruno', 'ie1', 4, 'GK'),
  card('t:c', 'Carla', 'go', 4, 'MF'),
  card('t:d', 'Dani', 'go', 1, 'FW'),
];

describe('enciclopedia', () => {
  it('filtra por temporada, demarcación y conseguidos', () => {
    const all = { season: 'all', position: 'all' as const, ownedOnly: false };
    expect(filterCards(CARDS, all, new Set())).toHaveLength(4);
    expect(filterCards(CARDS, { ...all, season: 'go' }, new Set()).map((c) => c.key)).toEqual(['t:c', 't:d']);
    expect(filterCards(CARDS, { ...all, position: 'FW' }, new Set()).map((c) => c.key)).toEqual(['t:a', 't:d']);
    expect(filterCards(CARDS, { ...all, ownedOnly: true }, new Set(['t:d'])).map((c) => c.key)).toEqual(['t:d']);
  });

  it('ordena por rareza y luego por nombre', () => {
    const list = filterCards(CARDS, { season: 'all', position: 'all', ownedOnly: false }, new Set());
    expect(list.map((c) => c.player.name)).toEqual(['Bruno', 'Carla', 'Álvaro', 'Dani']);
  });

  it('las técnicas se filtran por tipo y van de más a menos potencia', () => {
    const moves = Object.values(MOVES);
    const shots = filterMoves(moves, 'shoot');
    expect(shots.length).toBeGreaterThan(50);
    expect(shots.every((m) => m.kind === 'shoot')).toBe(true);
    for (let i = 1; i < shots.length; i++) expect(shots[i - 1].power).toBeGreaterThanOrEqual(shots[i].power);
    expect(filterMoves(moves, 'all')).toHaveLength(moves.length);
  });

  it('solo las técnicas con cuaderno, si se pide', () => {
    const m: MoveData[] = [
      { id: 'x', name: 'X', kind: 'shoot', element: 'fire', power: 10, tp: 5 },
      { id: 'y', name: 'Y', kind: 'shoot', element: 'fire', power: 20, tp: 5 },
    ];
    expect(filterMoves(m, 'all', true, { x: 2 }).map((v) => v.id)).toEqual(['x']);
    expect(filterMoves(m, 'all', false, { x: 2 }).map((v) => v.id)).toEqual(['y', 'x']);
  });

  it('pagina sin salirse del rango', () => {
    const list = Array.from({ length: 25 }, (_, i) => i);
    expect(paginate(list, 0, 10)).toEqual({ items: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], page: 0, pages: 3 });
    expect(paginate(list, 2, 10).items).toEqual([20, 21, 22, 23, 24]);
    expect(paginate(list, 9, 10).page).toBe(2);
    expect(paginate(list, -3, 10).page).toBe(0);
    expect(paginate([], 0, 10)).toEqual({ items: [], page: 0, pages: 1 });
  });

  it('texto del progreso', () => {
    expect(progressLabel(12, 340)).toBe('12 / 340 (3 %)');
    expect(progressLabel(0, 0)).toBe('0 / 0 (0 %)');
  });
});
