// Reglas de los enfrentamientos (duelos, tiros y paradas).
// Funciones puras: no dependen de Phaser, así se pueden testear y ajustar.

import { elementMultiplier } from '../data/elements';
import type { Element, MoveData, MoveKind, Stats } from '../data/types';

export type Rng = () => number;

export type BasicId =
  | 'dribble' // Regate
  | 'feint' // Finta
  | 'tackle' // Entrada
  | 'slide' // Entrada en plancha
  | 'shot' // Tiro
  | 'chip' // Vaselina
  | 'catch' // Atrapar
  | 'punch'; // Despejar

export type Choice = { type: 'basic'; id: BasicId } | { type: 'move'; move: MoveData };

export const BASIC_LABEL: Record<BasicId, string> = {
  dribble: 'Regate',
  feint: 'Finta',
  tackle: 'Entrada',
  slide: 'Entrada en plancha',
  shot: 'Tiro',
  chip: 'Vaselina',
  catch: 'Atrapar',
  punch: 'Despejar',
};

/** Las dos opciones básicas de cada situación (como los dos botones de IE3). */
export const BASIC_OPTIONS = {
  attack: ['dribble', 'feint'],
  defend: ['tackle', 'slide'],
  shoot: ['shot', 'chip'],
  keep: ['catch', 'punch'],
} as const satisfies Record<string, readonly [BasicId, BasicId]>;

export type Situation = keyof typeof BASIC_OPTIONS;

/** Qué tipo de supertécnica se puede usar en cada situación. */
export const SITUATION_MOVE_KIND: Record<Situation, MoveKind> = {
  attack: 'dribble',
  defend: 'block',
  shoot: 'shoot',
  keep: 'catch',
};

export interface Fighter {
  stats: Stats;
  element: Element;
  fp: number;
  maxFp: number;
}

export const DUEL_FP_COST = 4;
export const SHOT_FP_COST = 6;

/** Con la FP vacía un jugador rinde al 55 %. */
export function fpFactor(fp: number, maxFp: number): number {
  const ratio = maxFp > 0 ? Math.max(0, Math.min(1, fp / maxFp)) : 0;
  return 0.55 + 0.45 * ratio;
}

function basicPower(id: BasicId, s: Stats): number {
  switch (id) {
    case 'dribble':
      return s.control * 1.0 + s.speed * 0.5;
    case 'feint':
      return s.control * 0.6 + s.speed * 0.6 + s.guts * 0.3;
    case 'tackle':
      return s.guard * 0.9 + s.body * 0.6;
    case 'slide':
      return s.guard * 0.6 + s.body * 0.5 + s.speed * 0.5;
    case 'shot':
      return s.kick * 1.3;
    case 'chip':
      return s.kick * 0.6 + s.control * 0.8;
    case 'catch':
      return s.guard * 1.5;
    case 'punch':
      return s.guard * 1.3 + s.body * 0.4;
  }
}

function moveStat(kind: MoveKind, s: Stats): number {
  switch (kind) {
    case 'shoot':
      return s.kick;
    case 'dribble':
      return s.control;
    case 'block':
      return (s.guard + s.body) / 2;
    case 'catch':
      return s.guard;
  }
}

/** Potencia "en bruto" de una elección, sin azar ni elementos. */
export function choicePower(f: Fighter, c: Choice): number {
  let raw: number;
  if (c.type === 'basic') {
    raw = basicPower(c.id, f.stats);
  } else {
    raw = c.move.power + moveStat(c.move.kind, f.stats) * 0.8;
    // Bonus si el elemento de la técnica coincide con el del jugador
    if (c.move.element === f.element) raw *= 1.1;
  }
  return raw * fpFactor(f.fp, f.maxFp);
}

function choiceElement(f: Fighter, c: Choice): Element {
  return c.type === 'move' ? c.move.element : f.element;
}

/**
 * Piedra-papel-tijera de los comandos básicos:
 * la plancha es arriesgada (fuerte contra el regate, débil contra la finta)
 * y la finta pierde contra una entrada paciente.
 */
function basicMatchup(att: Choice, def: Choice): number {
  if (att.type !== 'basic' || def.type !== 'basic') return 1;
  const key = `${att.id}/${def.id}`;
  switch (key) {
    case 'feint/slide':
      return 1.3;
    case 'dribble/slide':
      return 1 / 1.2;
    case 'feint/tackle':
      return 1 / 1.15;
    default:
      return 1;
  }
}

function jitter(rng: Rng): number {
  return 0.85 + rng() * 0.3;
}

export interface DuelResult {
  attackerWins: boolean;
  attackPower: number;
  defensePower: number;
}

export function resolveDuel(
  attacker: Fighter,
  attChoice: Choice,
  defender: Fighter,
  defChoice: Choice,
  rng: Rng,
): DuelResult {
  let a = choicePower(attacker, attChoice) * jitter(rng);
  let d = choicePower(defender, defChoice) * jitter(rng);
  // El elemento solo cuenta cuando al menos uno usa supertécnica
  if (attChoice.type === 'move' || defChoice.type === 'move') {
    a *= elementMultiplier(choiceElement(attacker, attChoice), choiceElement(defender, defChoice));
  }
  a *= basicMatchup(attChoice, defChoice);
  return { attackerWins: a > d, attackPower: Math.round(a), defensePower: Math.round(d) };
}

/** Los tiros pierden fuerza con la distancia (en píxeles del campo). */
export function distanceFactor(distance: number): number {
  const full = 260; // a menos de esto el tiro llega con toda su fuerza
  const zero = 1500;
  if (distance <= full) return 1;
  return Math.max(0.35, 1 - ((distance - full) / (zero - full)) * 0.65);
}

export type ShotOutcome = 'goal' | 'caught' | 'punched';

export interface ShotResult {
  outcome: ShotOutcome;
  shotPower: number;
  keeperPower: number;
}

export function resolveShot(
  shooter: Fighter,
  shotChoice: Choice,
  distance: number,
  keeper: Fighter,
  keepChoice: Choice,
  rng: Rng,
): ShotResult {
  let s = choicePower(shooter, shotChoice) * distanceFactor(distance) * jitter(rng);
  const k = choicePower(keeper, keepChoice) * jitter(rng);
  if (shotChoice.type === 'move' || keepChoice.type === 'move') {
    s *= elementMultiplier(choiceElement(shooter, shotChoice), choiceElement(keeper, keepChoice));
  }
  // La vaselina castiga al portero que intenta despejar de puños
  if (shotChoice.type === 'basic' && shotChoice.id === 'chip' && keepChoice.type === 'basic' && keepChoice.id === 'punch') {
    s *= 1.2;
  }
  let outcome: ShotOutcome;
  if (s > k) outcome = 'goal';
  else outcome = keepChoice.type === 'basic' && keepChoice.id === 'punch' ? 'punched' : 'caught';
  return { outcome, shotPower: Math.round(s), keeperPower: Math.round(k) };
}

/** Supertécnicas que un jugador puede usar ahora mismo en esta situación. */
export function usableMoves(moves: MoveData[], situation: Situation, tp: number): MoveData[] {
  const kind = SITUATION_MOVE_KIND[situation];
  return moves.filter((m) => m.kind === kind && m.tp <= tp);
}

/**
 * Decisión de la CPU: usa supertécnica con cierta probabilidad si tiene TP,
 * y si no, una de las dos opciones básicas.
 */
export function cpuChoice(moves: MoveData[], situation: Situation, tp: number, rng: Rng, moveChance = 0.6): Choice {
  const usable = usableMoves(moves, situation, tp);
  if (usable.length > 0 && rng() < moveChance) {
    const best = usable.reduce((a, b) => (b.power > a.power ? b : a));
    return { type: 'move', move: best };
  }
  const [a, b] = BASIC_OPTIONS[situation];
  return { type: 'basic', id: rng() < 0.5 ? a : b };
}

export function choiceLabel(c: Choice): string {
  return c.type === 'move' ? c.move.name : BASIC_LABEL[c.id];
}
