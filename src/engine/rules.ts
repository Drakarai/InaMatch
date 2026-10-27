// Reglas de los enfrentamientos (duelos, tiros y paradas).
// Funciones puras: no dependen de Phaser, así se pueden testear y ajustar.

import { SAME_ELEMENT_BONUS, elementMultiplier, hasStab } from '../data/elements';
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
  | 'punch' // Despejar
  | 'shotblock' // Bloquear un tiro
  | 'letpass'; // Dejar pasar el tiro

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
  shotblock: 'Bloquear',
  letpass: 'Dejar pasar',
};

/** Las dos opciones básicas de cada situación (como los dos botones de IE3). */
export const BASIC_OPTIONS = {
  attack: ['dribble', 'feint'],
  defend: ['tackle', 'slide'],
  shoot: ['shot', 'chip'],
  keep: ['catch', 'punch'],
  block: ['shotblock', 'letpass'],
} as const satisfies Record<string, readonly [BasicId, BasicId]>;

export type Situation = keyof typeof BASIC_OPTIONS;

/** Qué tipo de supertécnica se puede usar en cada situación. */
export const SITUATION_MOVE_KIND: Record<Situation, MoveKind> = {
  attack: 'dribble',
  defend: 'block',
  shoot: 'shoot',
  keep: 'catch',
  block: 'block',
};

export interface Fighter {
  stats: Stats;
  element: Element;
  fp: number;
  maxFp: number;
}

export const DUEL_FP_COST = 4;
export const SHOT_FP_COST = 6;

/** Cada compañero que entra en el duelo suma un 10 % (máximo dos), como el doble aro de GO... */
export const SUPPORT_BONUS = 0.1;
/** ...y otro 10 % si es de la misma afinidad que el jugador del duelo ("¡Bonus de afinidad!"). */
export const AFFINITY_SUPPORT_BONUS = 0.1;
export const MAX_SUPPORTERS = 2;
/** Probabilidad de que una entrada en plancha ganada acabe en falta. */
export const FOUL_CHANCE = 0.2;

/** FIRED UP (IE3): la tensión del equipo sube con las buenas jugadas y al llenarse da +15 % un rato. */
export const FIRED_UP_BONUS = 1.15;
export const FIRED_UP_SECONDS = 25;
export const TENSION_GAIN = { duelWon: 14, shotBlocked: 18, save: 20, conceded: 25 } as const;

/** Niveles de "¡Regula la potencia!" (GO): más TP, más fuerza. */
export const SHOT_POWER_LEVELS = [
  { label: 'Normal', tp: 0, mul: 1 },
  { label: 'Fuerte', tp: 10, mul: 1.15 },
  { label: 'Máxima', tp: 20, mul: 1.3 },
] as const;

/** `sameElement` son cuántos de esos compañeros comparten afinidad con el jugador del duelo. */
export function supportMultiplier(supporters: number, sameElement = 0): number {
  const n = Math.min(MAX_SUPPORTERS, Math.max(0, supporters));
  const same = Math.min(n, Math.max(0, sameElement));
  return 1 + SUPPORT_BONUS * n + AFFINITY_SUPPORT_BONUS * same;
}

/** Multiplicadores externos: apoyo de compañeros, FIRED UP, potencia del tiro... */
export interface Mods {
  attack?: number;
  defense?: number;
}

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
    case 'shotblock':
      return s.guard * 0.8 + s.body * 0.8;
    case 'letpass':
      return 0;
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
    // STAB: técnica de la misma afinidad que el jugador
    if (hasStab(f.element, c.move.element)) raw *= SAME_ELEMENT_BONUS;
  }
  return raw * fpFactor(f.fp, f.maxFp);
}

/**
 * Afinidades de un enfrentamiento, en dos capas que se evalúan por separado:
 * - la de los jugadores, que cuenta siempre;
 * - la de las técnicas, solo si los dos usan supertécnica.
 * Así, un jugador de Aire con técnica de Bosque contra uno de Montaña con técnica de Fuego
 * gana por jugadores pero pierde por técnicas, y las dos ventajas se anulan.
 */
export function affinityMultiplier(a: Fighter, aChoice: Choice, b: Fighter, bChoice: Choice): number {
  let m = elementMultiplier(a.element, b.element);
  if (aChoice.type === 'move' && bChoice.type === 'move') m *= elementMultiplier(aChoice.move.element, bChoice.move.element);
  return m;
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
  mods: Mods = {},
): DuelResult {
  let a = choicePower(attacker, attChoice) * jitter(rng) * (mods.attack ?? 1);
  let d = choicePower(defender, defChoice) * jitter(rng) * (mods.defense ?? 1);
  a *= affinityMultiplier(attacker, attChoice, defender, defChoice);
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

/** Fuerza con la que sale el tiro (antes de bloqueos y portero). */
/** Fuerza que pierde un tiro largo por cada segundo en el aire (7 %). */
export const LONG_SHOT_DECAY = 0.07;

/** Fuerza de un tiro largo tras `seconds` segundos de vuelo. */
export function longShotDecay(power: number, seconds: number): number {
  return power * Math.pow(1 - LONG_SHOT_DECAY, seconds);
}

export function shotPower(shooter: Fighter, shotChoice: Choice, distance: number, rng: Rng, mul = 1): number {
  const long = shotChoice.type === 'move' && shotChoice.move.long;
  return choicePower(shooter, shotChoice) * (long ? 1 : distanceFactor(distance)) * jitter(rng) * mul;
}

export interface BlockResult {
  blocked: boolean;
  blockPower: number;
  /** fuerza con la que sigue el tiro si no se ha bloqueado */
  remaining: number;
}

/** Un defensa en la trayectoria intenta bloquear el tiro; si no puede, al menos le resta fuerza. */
export function resolveBlock(
  power: number,
  shooter: Fighter,
  shotChoice: Choice,
  blocker: Fighter,
  blockChoice: Choice,
  rng: Rng,
  mul = 1,
): BlockResult {
  if (blockChoice.type === 'basic' && blockChoice.id === 'letpass') {
    return { blocked: false, blockPower: 0, remaining: power };
  }
  let b = choicePower(blocker, blockChoice) * jitter(rng) * mul;
  b *= affinityMultiplier(blocker, blockChoice, shooter, shotChoice);
  const blocked = b >= power;
  return { blocked, blockPower: Math.round(b), remaining: blocked ? 0 : power - b * 0.5 };
}

/** El portero contra un tiro que llega con fuerza `power`. */
export function resolveKeeper(
  power: number,
  shooter: Fighter,
  shotChoice: Choice,
  keeper: Fighter,
  keepChoice: Choice,
  rng: Rng,
  mul = 1,
): ShotResult {
  let s = power;
  const k = choicePower(keeper, keepChoice) * jitter(rng) * mul;
  s *= affinityMultiplier(shooter, shotChoice, keeper, keepChoice);
  // La vaselina castiga al portero que intenta despejar de puños
  if (shotChoice.type === 'basic' && shotChoice.id === 'chip' && keepChoice.type === 'basic' && keepChoice.id === 'punch') {
    s *= 1.2;
  }
  let outcome: ShotOutcome;
  if (s > k) outcome = 'goal';
  else outcome = keepChoice.type === 'basic' && keepChoice.id === 'punch' ? 'punched' : 'caught';
  return { outcome, shotPower: Math.round(s), keeperPower: Math.round(k) };
}

/** Tiro completo sin bloqueos: fuerza de salida + portero. */
export function resolveShot(
  shooter: Fighter,
  shotChoice: Choice,
  distance: number,
  keeper: Fighter,
  keepChoice: Choice,
  rng: Rng,
  mods: Mods = {},
): ShotResult {
  const power = shotPower(shooter, shotChoice, distance, rng, mods.attack ?? 1);
  return resolveKeeper(power, shooter, shotChoice, keeper, keepChoice, rng, mods.defense ?? 1);
}

/** Una entrada en plancha que gana el balón puede acabar en falta. */
export function isFoul(defChoice: Choice, defenderWon: boolean, rng: Rng): boolean {
  return defenderWon && defChoice.type === 'basic' && defChoice.id === 'slide' && rng() < FOUL_CHANCE;
}

/** "Poder de base" que se enseña antes de elegir: la media de los dos comandos básicos. */
export function basePower(f: Fighter, situation: Situation, mul = 1): number {
  const [a, b] = BASIC_OPTIONS[situation];
  return Math.round(((choicePower(f, { type: 'basic', id: a }) + choicePower(f, { type: 'basic', id: b })) / 2) * mul);
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
  // la CPU nunca deja pasar un tiro a propósito
  if (situation === 'block') return { type: 'basic', id: a };
  return { type: 'basic', id: rng() < 0.5 ? a : b };
}

export function choiceLabel(c: Choice): string {
  return c.type === 'move' ? c.move.name : BASIC_LABEL[c.id];
}
