import { describe, expect, it } from 'vitest';
import { MOVES, TEAMS, validateTeams } from '../data';
import { elementMultiplier } from '../data/elements';
import type { Stats } from '../data/types';
import {
  basePower,
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
const move = (id: string): Choice => ({ type: 'move', move: MOVES[id] });

describe('datos', () => {
  it('los equipos son válidos', () => {
    expect(TEAMS.length).toBeGreaterThanOrEqual(2);
    expect(validateTeams()).toEqual([]);
  });
});

describe('elementos', () => {
  it('cada elemento gana a uno y pierde contra otro', () => {
    expect(elementMultiplier('fire', 'wood')).toBeGreaterThan(1);
    expect(elementMultiplier('wood', 'fire')).toBeLessThan(1);
    expect(elementMultiplier('fire', 'fire')).toBe(1);
    expect(elementMultiplier('fire', 'wind')).toBe(1);
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
    expect(supportMultiplier(1)).toBeCloseTo(1.12);
    expect(supportMultiplier(5)).toBeCloseTo(supportMultiplier(2));
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
