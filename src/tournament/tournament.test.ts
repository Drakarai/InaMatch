import { describe, expect, it } from 'vitest';
import {
  advance,
  createCup,
  createLeague,
  CUP_SIZE,
  finishWithoutUser,
  LEAGUE_SIZE,
  parseTourney,
  penaltyShootout,
  pickOpponents,
  recordUserResult,
  roundName,
  roundRobin,
  simulateScore,
  standings,
  TOURNEY_COINS,
  tourneyCoins,
  userMatch,
  userPlace,
  winnerOf,
  type Tourney,
} from './tournament';

/** Generador con semilla (mulberry32): los mismos números en cada prueba. */
function seeded(seed: number): () => number {
  let a = seed >>> 0;
  return () => {
    a = (a + 0x6d2b79f5) >>> 0;
    let t = a;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

const TEAMS8 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'];
const flat = () => 60;

describe('copa', () => {
  it('sortea 8 equipos en 4 partidos, con el del jugador dentro', () => {
    const t = createCup('a', TEAMS8.slice(1), seeded(1));
    expect(t.rounds[0]).toHaveLength(4);
    const all = t.rounds[0].flatMap((m) => [m.home, m.away]).sort();
    expect(all).toEqual([...TEAMS8].sort());
    expect(userMatch(t)).not.toBeNull();
    expect(roundName(t)).toBe('Cuartos de final');
  });

  it('pide exactamente 7 rivales', () => {
    expect(() => createCup('a', ['b', 'c'], seeded(1))).toThrow();
  });

  it('si el jugador gana avanza, y tras tres victorias es campeón', () => {
    let t = createCup('a', TEAMS8.slice(1), seeded(2));
    for (let r = 0; r < 3; r++) {
      expect(userMatch(t)).not.toBeNull();
      t = recordUserResult(t, 3, 0, flat, seeded(10 + r));
      expect(t.out).toBe(false);
    }
    expect(t.champion).toBe('a');
    expect(userPlace(t)).toBe(1);
    expect(tourneyCoins(t)).toBe(TOURNEY_COINS.champion);
    expect(userMatch(t)).toBeNull();
  });

  it('si el jugador pierde queda eliminado y el resto se puede simular hasta tener campeón', () => {
    let t = createCup('a', TEAMS8.slice(1), seeded(3));
    t = recordUserResult(t, 0, 2, flat, seeded(4));
    expect(t.out).toBe(true);
    expect(userMatch(t)).toBeNull();
    t = finishWithoutUser(t, flat, seeded(5));
    expect(t.champion).not.toBeNull();
    expect(t.champion).not.toBe('a');
    expect(t.rounds).toHaveLength(3);
    expect(userPlace(t)).toBe(3);
    expect(tourneyCoins(t)).toBe(TOURNEY_COINS.played);
  });

  it('un empate se decide en penaltis', () => {
    const t = recordUserResult(createCup('a', TEAMS8.slice(1), seeded(6)), 1, 1, flat, seeded(7));
    const m = t.rounds[0].find((x) => x.home === 'a' || x.away === 'a')!;
    expect(m.pens).toBeDefined();
    expect(winnerOf(m)).not.toBeNull();
    expect(t.out).toBe(winnerOf(m) !== 'a');
  });

  it('no cambia el torneo que recibe', () => {
    const t = createCup('a', TEAMS8.slice(1), seeded(8));
    const copy = JSON.stringify(t);
    recordUserResult(t, 2, 1, flat, seeded(9));
    expect(JSON.stringify(t)).toBe(copy);
  });

  it('en cada ronda todos los partidos tienen ganador', () => {
    const t = finishWithoutUser(recordUserResult(createCup('a', TEAMS8.slice(1), seeded(11)), 0, 1, flat, seeded(12)), flat, seeded(13));
    for (const round of t.rounds) for (const m of round) expect(winnerOf(m)).not.toBeNull();
  });
});

describe('liga', () => {
  it('todos contra todos: cada pareja una vez y cada equipo un partido por jornada', () => {
    const teams = ['a', 'b', 'c', 'd', 'e', 'f'];
    const rounds = roundRobin(teams);
    expect(rounds).toHaveLength(5);
    const pairs = new Set<string>();
    for (const r of rounds) {
      expect(r).toHaveLength(3);
      const seen = r.flat();
      expect(new Set(seen).size).toBe(6);
      for (const [x, y] of r) pairs.add([x, y].sort().join('-'));
    }
    expect(pairs.size).toBe(15);
  });

  it('con número impar de equipos, uno descansa cada jornada', () => {
    const rounds = roundRobin(['a', 'b', 'c', 'd', 'e']);
    expect(rounds).toHaveLength(5);
    for (const r of rounds) expect(r).toHaveLength(2);
  });

  it('cinco jornadas y campeón el primero de la tabla', () => {
    let t = createLeague('a', ['b', 'c', 'd', 'e', 'f'], seeded(20));
    for (let r = 0; r < LEAGUE_SIZE - 1; r++) t = recordUserResult(t, 2, 0, flat, seeded(30 + r));
    expect(t.champion).not.toBeNull();
    const table = standings(t);
    expect(table[0].team).toBe(t.champion);
    for (const s of table) expect(s.played).toBe(5);
    // el jugador lo ha ganado todo: 15 puntos y campeón
    expect(table.find((s) => s.team === 'a')!.points).toBe(15);
    expect(t.champion).toBe('a');
  });

  it('la tabla cuenta puntos, goles y desempata por diferencia de goles', () => {
    const t: Tourney = {
      v: 1,
      kind: 'league',
      user: 'a',
      teams: ['a', 'b', 'c'],
      rounds: [
        [
          { home: 'a', away: 'b', hg: 1, ag: 1 },
          { home: 'c', away: 'a', hg: 0, ag: 3 },
          { home: 'b', away: 'c', hg: 1, ag: 0 },
        ],
      ],
      round: 0,
      champion: null,
      out: false,
    };
    const table = standings(t);
    expect(table.map((s) => s.team)).toEqual(['a', 'b', 'c']);
    expect(table[0]).toMatchObject({ points: 4, won: 1, drawn: 1, gf: 4, ga: 1 });
    expect(table[1]).toMatchObject({ points: 4, gf: 2, ga: 1 });
    expect(table[2].points).toBe(0);
    // los empates de liga no tienen ganador
    expect(winnerOf(t.rounds[0][0])).toBeNull();
  });

  it('pide exactamente 5 rivales', () => {
    expect(() => createLeague('a', ['b'], seeded(1))).toThrow();
  });
});

describe('simulación', () => {
  it('los penaltis nunca acaban en empate', () => {
    const rng = seeded(40);
    for (let i = 0; i < 300; i++) {
      const p = penaltyShootout(rng);
      expect(p.home).not.toBe(p.away);
    }
  });

  it('el mejor equipo gana más a menudo', () => {
    const rng = seeded(41);
    let strong = 0;
    let weak = 0;
    for (let i = 0; i < 2000; i++) {
      const [x, y] = simulateScore(75, 50, rng);
      if (x > y) strong++;
      else if (y > x) weak++;
    }
    expect(strong).toBeGreaterThan(weak * 2);
  });

  it('los goles son números enteros razonables', () => {
    const rng = seeded(42);
    for (let i = 0; i < 500; i++) {
      for (const g of simulateScore(80, 40, rng)) {
        expect(Number.isInteger(g)).toBe(true);
        expect(g).toBeGreaterThanOrEqual(0);
        expect(g).toBeLessThanOrEqual(11);
      }
    }
  });

  it('los rivales elegidos no repiten ni incluyen al jugador', () => {
    const picks = pickOpponents('a', TEAMS8, CUP_SIZE - 1, seeded(43));
    expect(picks).toHaveLength(7);
    expect(new Set(picks).size).toBe(7);
    expect(picks).not.toContain('a');
  });

  it('advance no simula dos veces un partido ya jugado', () => {
    const t = createCup('a', TEAMS8.slice(1), seeded(44));
    t.rounds[0][0].hg = 5;
    t.rounds[0][0].ag = 4;
    const next = advance(JSON.parse(JSON.stringify(t)), flat, seeded(45));
    expect(next.rounds[0][0]).toMatchObject({ hg: 5, ag: 4 });
  });
});

describe('guardado', () => {
  const exists = (id: string) => TEAMS8.includes(id);
  it('lee un torneo guardado válido', () => {
    const t = createCup('a', TEAMS8.slice(1), seeded(50));
    expect(parseTourney(JSON.stringify(t), exists)).toEqual(t);
  });
  it('descarta lo dañado, de otra versión o con equipos que ya no existen', () => {
    expect(parseTourney(null, exists)).toBeNull();
    expect(parseTourney('{nope', exists)).toBeNull();
    expect(parseTourney(JSON.stringify({ v: 2 }), exists)).toBeNull();
    const t = createCup('a', TEAMS8.slice(1), seeded(51));
    expect(parseTourney(JSON.stringify(t), (id) => id !== 'b')).toBeNull();
  });
});
