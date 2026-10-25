import { describe, expect, it } from 'vitest';
import { TEAMS, validateTeams } from '../data';
import { lineRatings, ratingStars, teamRating } from './rating';
import { SAME_ELEMENT_BONUS, elementMultiplier, hasStab } from '../data/elements';
import type { MoveData, Stats } from '../data/types';
import {
  affinityMultiplier,
  basePower,
  choicePower,
  cpuChoice,
  distanceFactor,
  fpFactor,
  isFoul,
  resolveBlock,
  resolveDuel,
  resolveKeeper,
  resolveShot,
  shotPower,
  supportMultiplier,
  usableMoves,
  type Choice,
  type Fighter,
} from './rules';

const stats = (v: number): Stats => ({ kick: v, body: v, control: v, guard: v, speed: v, stamina: v, guts: v });
const fighter = (v: number, element: Fighter['element'] = 'fire', fp = 100): Fighter => ({ stats: stats(v), element, fp, maxFp: 100 });
const fixed = (value: number) => () => value;
const basic = (id: Extract<Choice, { type: 'basic' }>['id']): Choice => ({ type: 'basic', id });
// técnicas de prueba, independientes de lo que tenga cada equipo en src/data
const MOVES: Record<string, MoveData> = {
  'fireball-screw': { id: 'fireball-screw', name: 'Torbellino de fuego', kind: 'shoot', element: 'fire', power: 90, tp: 52 },
  'fire-tornado': { id: 'fire-tornado', name: 'Tornado de fuego', kind: 'shoot', element: 'fire', power: 45, tp: 25 },
  'illusion-ball': { id: 'illusion-ball', name: 'Espejismo de balón', kind: 'dribble', element: 'wood', power: 45, tp: 28 },
  'heat-tackle': { id: 'heat-tackle', name: 'Entrada de llamas', kind: 'dribble', element: 'fire', power: 45, tp: 27 },
  'the-wall': { id: 'the-wall', name: 'El muro', kind: 'block', element: 'earth', power: 45, tp: 30 },
};
const move = (id: string): Choice => ({ type: 'move', move: MOVES[id] });

describe('datos', () => {
  it('los equipos son válidos', () => {
    expect(TEAMS.length).toBeGreaterThanOrEqual(2);
    expect(validateTeams()).toEqual([]);
  });

  it('cada equipo tiene portero titular y técnicas con nombre', () => {
    for (const t of TEAMS) {
      expect(t.players[0].position, t.id).toBe('GK');
      expect(t.players.length, t.id).toBeGreaterThanOrEqual(11);
    }
  });
});

describe('afinidades', () => {
  it('ciclo Bosque > Aire > Montaña > Fuego > Bosque', () => {
    expect(elementMultiplier('wood', 'wind')).toBeGreaterThan(1);
    expect(elementMultiplier('wind', 'earth')).toBeGreaterThan(1);
    expect(elementMultiplier('earth', 'fire')).toBeGreaterThan(1);
    expect(elementMultiplier('fire', 'wood')).toBeGreaterThan(1);
    expect(elementMultiplier('earth', 'wind')).toBeLessThan(1);
    expect(elementMultiplier('fire', 'fire')).toBe(1);
    expect(elementMultiplier('fire', 'wind')).toBe(1);
  });

  it('el neutro ni gana ni pierde y no tiene STAB', () => {
    for (const e of ['fire', 'wind', 'wood', 'earth', 'neutral'] as const) {
      expect(elementMultiplier('neutral', e)).toBe(1);
      expect(elementMultiplier(e, 'neutral')).toBe(1);
    }
    expect(hasStab('neutral', 'neutral')).toBe(false);
    expect(hasStab('wind', 'wind')).toBe(true);
  });

  it('STAB: la técnica de su misma afinidad pega más', () => {
    const windMove: Choice = { type: 'move', move: { id: 'w', name: 'w', kind: 'shoot', element: 'wind', power: 60, tp: 30 } };
    const woodMove: Choice = { type: 'move', move: { ...windMove.move, element: 'wood' } };
    const ratio = choicePower(fighter(30, 'wind'), windMove) / choicePower(fighter(30, 'wind'), woodMove);
    expect(ratio).toBeCloseTo(SAME_ELEMENT_BONUS);
  });

  it('la afinidad de los jugadores cuenta siempre, aunque nadie use técnica', () => {
    expect(affinityMultiplier(fighter(30, 'wind'), basic('dribble'), fighter(30, 'earth'), basic('tackle'))).toBeGreaterThan(1);
  });

  it('si solo uno usa técnica, solo cuenta la afinidad de los jugadores', () => {
    const fireMove = move('fireball-screw');
    expect(affinityMultiplier(fighter(30, 'wind'), basic('dribble'), fighter(30, 'earth'), fireMove)).toBeCloseTo(elementMultiplier('wind', 'earth'));
  });

  it('Aire con técnica de Bosque contra Montaña con técnica de Fuego: las ventajas se anulan', () => {
    const woodMove: Choice = { type: 'move', move: { ...MOVES['illusion-ball'], element: 'wood' } };
    const fireMove: Choice = { type: 'move', move: { ...MOVES['heat-tackle'], element: 'fire' } };
    expect(affinityMultiplier(fighter(30, 'wind'), woodMove, fighter(30, 'earth'), fireMove)).toBeCloseTo(1);
  });
});

describe('cansancio y distancia', () => {
  it('la FP vacía reduce el rendimiento', () => {
    expect(fpFactor(100, 100)).toBe(1);
    expect(fpFactor(0, 100)).toBeCloseTo(0.55);
  });

  it('los tiros lejanos pierden fuerza', () => {
    expect(distanceFactor(100)).toBe(1);
    expect(distanceFactor(800)).toBeLessThan(distanceFactor(400));
    expect(distanceFactor(5000)).toBeGreaterThan(0);
  });
});

describe('duelos', () => {
  it('con stats parecidas el azar decide el duelo', () => {
    const seq = (...values: number[]) => () => values.shift() ?? 0.5;
    const lucky = resolveDuel(fighter(30), basic('dribble'), fighter(30), basic('tackle'), seq(1, 0));
    const unlucky = resolveDuel(fighter(30), basic('dribble'), fighter(30), basic('tackle'), seq(0, 1));
    expect(lucky.attackerWins).toBe(true);
    expect(unlucky.attackerWins).toBe(false);
  });

  it('una supertécnica supera a un comando básico con stats parecidas', () => {
    const r = resolveDuel(fighter(30), move('illusion-ball'), fighter(32), basic('tackle'), fixed(0.5));
    expect(r.attackerWins).toBe(true);
  });

  it('la finta castiga la entrada en plancha', () => {
    const vsSlide = resolveDuel(fighter(30), basic('feint'), fighter(30), basic('slide'), fixed(0.5));
    const vsTackle = resolveDuel(fighter(30), basic('feint'), fighter(30), basic('tackle'), fixed(0.5));
    expect(vsSlide.attackPower).toBeGreaterThan(vsTackle.attackPower);
  });
});

describe('tiros', () => {
  it('un tiro con supertécnica de cerca bate a un portero sin técnica', () => {
    const r = resolveShot(fighter(45), move('fireball-screw'), 200, fighter(40), basic('catch'), fixed(0.5));
    expect(r.outcome).toBe('goal');
  });

  it('un tiro normal desde lejos lo para el portero', () => {
    const r = resolveShot(fighter(35), basic('shot'), 900, fighter(40), basic('catch'), fixed(0.5));
    expect(r.outcome).toBe('caught');
  });

  it('si el portero despeja y gana, el balón queda suelto', () => {
    const r = resolveShot(fighter(20), basic('shot'), 900, fighter(45), basic('punch'), fixed(0.5));
    expect(r.outcome).toBe('punched');
  });
});

describe('CPU', () => {
  const moves = [MOVES['fireball-screw'], MOVES['fire-tornado'], MOVES['the-wall']];

  it('solo ofrece técnicas del tipo adecuado y con TP suficiente', () => {
    expect(usableMoves(moves, 'shoot', 100).map((m) => m.id)).toEqual(['fireball-screw', 'fire-tornado']);
    expect(usableMoves(moves, 'shoot', 35).map((m) => m.id)).toEqual(['fire-tornado']);
    expect(usableMoves(moves, 'keep', 100)).toEqual([]);
  });

  it('elige la técnica más potente cuando decide usar una', () => {
    const c = cpuChoice(moves, 'shoot', 100, fixed(0));
    expect(c).toEqual({ type: 'move', move: MOVES['fireball-screw'] });
  });

  it('sin TP usa un comando básico', () => {
    const c = cpuChoice(moves, 'shoot', 0, fixed(0));
    expect(c.type).toBe('basic');
  });
});

describe('apoyo, faltas y potencia', () => {
  it('cada compañero cerca suma, con un máximo de dos', () => {
    expect(supportMultiplier(0)).toBe(1);
    expect(supportMultiplier(1)).toBeCloseTo(1.1);
    expect(supportMultiplier(5)).toBeCloseTo(supportMultiplier(2));
  });

  it('el compañero de la misma afinidad da además el bonus de afinidad', () => {
    expect(supportMultiplier(1, 1)).toBeGreaterThan(supportMultiplier(1, 0));
    expect(supportMultiplier(2, 2)).toBeCloseTo(1.4);
    expect(supportMultiplier(1, 3)).toBeCloseTo(supportMultiplier(1, 1));
  });

  it('el apoyo puede darle la vuelta a un duelo igualado', () => {
    const solo = resolveDuel(fighter(30), basic('dribble'), fighter(30), basic('tackle'), fixed(0.5));
    const helped = resolveDuel(fighter(30), basic('dribble'), fighter(30), basic('tackle'), fixed(0.5), { attack: supportMultiplier(2) });
    expect(helped.attackPower).toBeGreaterThan(solo.attackPower);
    expect(helped.attackerWins).toBe(true);
  });

  it('solo la entrada en plancha ganada puede ser falta', () => {
    expect(isFoul(basic('slide'), true, fixed(0))).toBe(true);
    expect(isFoul(basic('slide'), false, fixed(0))).toBe(false);
    expect(isFoul(basic('tackle'), true, fixed(0))).toBe(false);
    expect(isFoul(basic('slide'), true, fixed(0.99))).toBe(false);
  });

  it('el poder de base se puede enseñar antes de elegir', () => {
    expect(basePower(fighter(30), 'attack')).toBeGreaterThan(0);
    expect(basePower(fighter(30), 'attack', 1.2)).toBeGreaterThan(basePower(fighter(30), 'attack'));
  });
});

describe('bloqueos de tiro', () => {
  it('un tiro flojo lo bloquea un defensa fuerte', () => {
    const power = shotPower(fighter(20), basic('shot'), 600, fixed(0.5));
    const r = resolveBlock(power, fighter(20), basic('shot'), fighter(45), basic('shotblock'), fixed(0.5));
    expect(r.blocked).toBe(true);
  });

  it('si no lo bloquea, el tiro sigue pero más flojo', () => {
    const power = shotPower(fighter(45), move('fireball-screw'), 200, fixed(0.5));
    const r = resolveBlock(power, fighter(45), move('fireball-screw'), fighter(25), basic('shotblock'), fixed(0.5));
    expect(r.blocked).toBe(false);
    expect(r.remaining).toBeLessThan(power);
    expect(r.remaining).toBeGreaterThan(0);
  });

  it('dejar pasar no toca el tiro', () => {
    const r = resolveBlock(100, fighter(30), basic('shot'), fighter(50), basic('letpass'), fixed(0.5));
    expect(r).toEqual({ blocked: false, blockPower: 0, remaining: 100 });
  });

  it('el portero recibe la fuerza que queda tras el bloqueo', () => {
    const full = resolveKeeper(120, fighter(40), basic('shot'), fighter(40), basic('catch'), fixed(0.5));
    const weak = resolveKeeper(40, fighter(40), basic('shot'), fighter(40), basic('catch'), fixed(0.5));
    expect(full.outcome).toBe('goal');
    expect(weak.outcome).toBe('caught');
  });

  it('la CPU nunca deja pasar un tiro', () => {
    expect(cpuChoice([], 'block', 100, fixed(0.99))).toEqual({ type: 'basic', id: 'shotblock' });
  });
});

describe('media del equipo', () => {
  it('las estrellas van de 0,5 a 5 en pasos de media', () => {
    expect(ratingStars(10)).toBe(0.5);
    expect(ratingStars(100)).toBe(5);
    expect(ratingStars(63) * 2).toBe(Math.round(ratingStars(63) * 2));
    expect(ratingStars(70)).toBeGreaterThan(ratingStars(55));
  });

  it('todos los equipos tienen una media razonable', () => {
    for (const t of TEAMS) {
      const r = teamRating(t);
      expect(r, t.id).toBeGreaterThan(20);
      expect(r, t.id).toBeLessThan(120);
    }
  });

  it('las medias por líneas salen de los atributos de cada línea', () => {
    for (const t of TEAMS) {
      const { att, mid, def } = lineRatings(t);
      for (const v of [att, mid, def]) expect(v, t.id).toBeGreaterThan(20);
    }
    const team = TEAMS[0];
    const strikers = team.players.slice(0, 11).map((p) =>
      p.position === 'FW' ? { ...p, stats: { ...p.stats, kick: 99, control: 99, speed: 99 } } : p,
    );
    expect(lineRatings(team, strikers).att).toBe(team.players.slice(0, 11).some((p) => p.position === 'FW') ? 99 : lineRatings(team, strikers).att);
  });
});
