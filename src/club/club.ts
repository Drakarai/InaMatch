import { getTeam, MOVES, upsertTeam } from '../data';
import type { MoveData } from '../data/types';
import type { PlayerData, Position, TeamData } from '../data/types';
import { byPosition, cardByKey, cardForStaleKey, loadPool, RARITY, type Card, type Rarity } from './pool';
import { FORMATIONS, formationId, getFormation } from '../data/formations';
import { playerOverall } from '../engine/rating';
import crestList from '../data/crests.json';
import { getUniform, START_UNIFORMS, UNIFORMS } from './uniforms';

/**
 * "Mi club": el equipo propio, con los jugadores que se consiguen en el gacha.
 * - La primera vez cada uno recibe una plantilla distinta, al azar: casi todo ojeadores y jugadores poco
 *   conocidos, y uno o dos conocidos.
 * - Las monedas se ganan jugando partidos y se gastan en tiradas.
 * La partida se guarda en el navegador (localStorage).
 */

export interface ClubSave {
  v: 1;
  name: string;
  coins: number;
  /** Jugadores conseguidos (Card.key). */
  owned: string[];
  /** Plantilla: 16 jugadores; los 11 primeros son titulares en el orden de la formación. */
  squad: string[];
  formation: string;
  pulls: number;
  /** Cuadernos de supertécnicas conseguidos: id de la técnica -> cuántos. */
  notebooks?: Record<string, number>;
  /** Técnicas elegidas para cada jugador (Card.key): las 4 de base y las 2 extra ('' = hueco vacío). */
  custom?: Record<string, { base: string[]; extra: string[] }>;
  /** Escudos conseguidos (id de src/data/crests.json) y el que lleva el club. */
  crests?: string[];
  crest?: string;
  /** Formaciones conseguidas (id de src/data/formations.json): se pueden usar con cualquier equipo. */
  formations?: string[];
  /** Uniformes conseguidos (id de src/data/uniforms.json) y el que lleva el club. */
  uniforms?: string[];
  uniform?: string;
}

export const BASE_SLOTS = 4;
export const EXTRA_SLOTS = 2;
export const NOTEBOOK_COST = 80;
export const TEN_NOTEBOOK_COST = 700;

const KEY = 'inamatch-club';
export const PULL_COST = 100;
export const TEN_PULL_COST = 900;
const START_COINS = 500;
/** Probabilidad de cada rareza en una tirada. */
const RATES: [Rarity, number][] = [
  [1, 0.6],
  [2, 0.28],
  [3, 0.1],
  [4, 0.02],
];
/** Monedas que devuelve un jugador repetido. */
const DUPLICATE: Record<Rarity, number> = { 1: 10, 2: 25, 3: 60, 4: 150 };
/** Monedas por partido (con tu club se gana más) y por cada gol marcado. */
export const REWARD = { club: { win: 300, draw: 140, loss: 70, goal: 20 }, other: { win: 120, draw: 70, loss: 40, goal: 10 } };
/** Rango S: ganar por 5-0 o más sin encajar. Da monedas extra y un cuaderno ★★★ o mejor. */
export const RANK_S = { goals: 5, coins: 500 };
/** Escudos con los que se empieza; luego, uno por victoria (si ya se tienen todos, monedas). */
const START_CRESTS = 3;
const CREST_FULL_COINS = 100;
const CREST_IDS: string[] = (crestList as { id: string }[]).map((c) => c.id);

/** Huecos de la plantilla inicial (4-4-2 y banquillo). */
const START_SLOTS: Position[] = ['GK', 'DF', 'DF', 'DF', 'DF', 'MF', 'MF', 'MF', 'MF', 'FW', 'FW', 'GK', 'DF', 'MF', 'FW', 'MF'];
/** La formación del Raimon de IE1 (F-Basic): la del club al empezar y la primera conseguida. */
export const START_FORMATION = 'f-basic-ie3';

let memory: ClubSave | null = null;
const listeners: (() => void)[] = [];

export function loadClub(): ClubSave | null {
  if (memory) return memory;
  try {
    const raw = window.localStorage.getItem(KEY);
    if (raw) memory = JSON.parse(raw) as ClubSave;
  } catch {
    // sin almacenamiento: la partida dura lo que la pestaña
  }
  return memory;
}

export function saveClub(save: ClubSave): void {
  memory = save;
  try {
    window.localStorage.setItem(KEY, JSON.stringify(save));
  } catch {
    // sin almacenamiento
  }
  listeners.forEach((l) => l());
}

export function onClubChange(l: () => void): () => void {
  listeners.push(l);
  return () => listeners.splice(listeners.indexOf(l), 1);
}

const rand = (n: number) => {
  try {
    const a = new Uint32Array(1);
    crypto.getRandomValues(a);
    return a[0] % n;
  } catch {
    return Math.floor(Math.random() * n);
  }
};
const pickOne = <T>(list: T[]): T => list[rand(list.length)];

/** Escudos al azar que aún no se tienen. */
function newCrests(owned: string[], n: number): string[] {
  const left = CREST_IDS.filter((id) => !owned.includes(id));
  const out: string[] = [];
  while (out.length < n && left.length) out.push(left.splice(rand(left.length), 1)[0]);
  return out;
}

/** Los tres escudos iniciales (también a las partidas de antes de que hubiera escudos). */
function withStartCrests(save: ClubSave): ClubSave {
  const crests = (save.crests ?? []).filter((id) => CREST_IDS.includes(id));
  if (crests.length < START_CRESTS) crests.push(...newCrests(crests, START_CRESTS - crests.length));
  const crest = save.crest && crests.includes(save.crest) ? save.crest : crests[0];
  return { ...save, crests, crest };
}

/** Los uniformes iniciales (también a las partidas de antes de que hubiera uniformes). */
function withStartUniforms(save: ClubSave): ClubSave {
  const owned = new Set((save.uniforms ?? []).filter((id) => getUniform(id)));
  START_UNIFORMS.forEach((id) => owned.add(id));
  const uniform = save.uniform && owned.has(save.uniform) ? save.uniform : START_UNIFORMS[0];
  return { ...save, uniforms: [...owned], uniform };
}

/** Uniforme al azar que aún no se tiene. */
function newUniform(owned: string[]): string | undefined {
  const left = UNIFORMS.map((u) => u.id).filter((id) => !owned.includes(id));
  return left.length ? pickOne(left) : undefined;
}

/** Cambia el uniforme del club (uno de los conseguidos). */
export function setUniform(save: ClubSave, id: string): void {
  if (!(save.uniforms ?? []).includes(id)) return;
  saveClub({ ...save, uniform: id });
  upsertTeam(clubTeam(loadClub()!));
}

/** Formaciones que se pueden ganar: las de la wiki (no las genéricas por distribución). */
const PRIZE_FORMATIONS = (): string[] => FORMATIONS.filter((f) => !f.generic).map((f) => f.id);

/** La formación inicial y la que lleve el club (las partidas de antes de que hubiera premios conservan la suya). */
function withStartFormations(save: ClubSave): ClubSave {
  const owned = new Set((save.formations ?? []).map(formationId));
  owned.add(START_FORMATION);
  owned.add(formationId(save.formation));
  return { ...save, formations: [...owned], formation: formationId(save.formation) };
}

/** Las formaciones que puede usar un equipo: las conseguidas y, si no es Mi club, la suya propia. */
export function availableFormations(teamId: string): Set<string> {
  const save = loadClub();
  const out = new Set((save?.formations ?? [START_FORMATION]).map(formationId));
  if (teamId !== 'club') {
    try {
      out.add(formationId(getTeam(teamId).formation));
    } catch {
      // equipo desconocido
    }
  }
  return out;
}

/** Cambia el escudo del club (uno de los conseguidos). */
export function setCrest(save: ClubSave, id: string): void {
  if (!(save.crests ?? []).includes(id)) return;
  saveClub({ ...save, crest: id });
}

/** Plantilla inicial al azar: cada club empieza distinto. */
function starterSquad(pool: Card[]): string[] {
  // uno o dos "conocidos" (rareza 3), unos pocos "poco conocidos" (2) y el resto ojeadores (1)
  const known = 1 + rand(2);
  const rarities: Rarity[] = START_SLOTS.map(() => (rand(100) < 22 ? 2 : 1));
  const starters = [...Array(11).keys()];
  for (let i = 0; i < known; i++) {
    const free = starters.filter((s) => rarities[s] !== 3 && s !== 0);
    rarities[pickOne(free)] = 3;
  }
  const chosen: string[] = [];
  START_SLOTS.forEach((pos, i) => {
    let options = byPosition(pool, pos, rarities[i]).filter((c) => !chosen.includes(c.key));
    if (!options.length) options = byPosition(pool, pos).filter((c) => c.rarity <= 2 && !chosen.includes(c.key));
    chosen.push(pickOne(options).key);
  });
  return chosen;
}

/** El club guardado, o uno nuevo si es la primera vez. Deja "Mi club" entre los equipos del menú. */
export async function ensureClub(): Promise<ClubSave> {
  const pool = await loadPool();
  let save = loadClub();
  if (save) {
    // jugadores cuyo equipo de origen ya no está: el mismo personaje en otro equipo, si sale en alguno
    save = withStartUniforms(withStartFormations(withStartCrests(save)));
    const remap = (k: string) => (cardByKey(k) ? k : (cardForStaleKey(k)?.key ?? k));
    save.squad = save.squad.map(remap);
    save.owned = [...new Set(save.owned.map(remap))];
    saveClub(save);
    // los que no existen en ningún sitio (datos regenerados): se sustituyen por ojeadores de su puesto
    const valid = (k: string) => !!cardByKey(k);
    if (!save.squad.every(valid) || !save.owned.every(valid)) {
      const fresh = starterSquad(pool);
      save.squad = save.squad.map((k, i) => (valid(k) ? k : fresh[i]));
      save.owned = [...new Set([...save.owned.filter(valid), ...save.squad])];
      saveClub(save);
    }
  } else {
    const squad = starterSquad(pool);
    save = withStartUniforms(withStartFormations(withStartCrests({ v: 1, name: 'Mi club', coins: START_COINS, owned: [...squad], squad, formation: START_FORMATION, pulls: 0 })));
    saveClub(save);
  }
  upsertTeam(clubTeam(save));
  return save;
}

export function clubTeam(save: ClubSave): TeamData {
  const used = new Set<string>();
  const players: PlayerData[] = save.squad.flatMap((key, i) => {
    const card = cardByKey(key);
    if (!card) return [];
    let id = card.player.id;
    while (used.has(id)) id += '-2';
    used.add(id);
    const { base, extra } = movesFor(save, card);
    const moves = [...base, ...extra].filter((m) => m && MOVES[m]);
    return [{ ...card.player, id, number: i + 1, origin: card.origin, originId: card.player.id, moves, captain: undefined }];
  });
  return {
    id: 'club',
    season: 'club',
    name: save.name,
    short: 'MIC',
    colors: getUniform(save.uniform)?.colors ?? { shirt: '#ffd23f', shorts: '#0b1a2e', gkShirt: '#2f7bff', accent: '#ffd23f' },
    uniform: getUniform(save.uniform)?.id,
    formation: save.formation,
    players,
  };
}

/** Cambia la plantilla (y la formación) y actualiza "Mi club" en el menú. */
export function setSquad(save: ClubSave, squad: string[], formation = save.formation): void {
  saveClub({ ...save, squad, formation });
  upsertTeam(clubTeam(loadClub()!));
}

export interface PullResult {
  card: Card;
  duplicate: boolean;
  refund: number;
}

function rollRarity(min: Rarity = 1): Rarity {
  const r = rand(10000) / 10000;
  let acc = 0;
  for (const [rarity, p] of RATES) {
    acc += p;
    if (r < acc) return Math.max(rarity, min) as Rarity;
  }
  return 4;
}

/** Tiradas del gacha. Las de diez cuestan menos y traen al menos un jugador conocido. */
export async function pull(count: 1 | 10): Promise<PullResult[] | null> {
  const save = loadClub();
  const cost = count === 10 ? TEN_PULL_COST : PULL_COST;
  if (!save || save.coins < cost) return null;
  const pool = await loadPool();
  const owned = new Set(save.owned);
  const results: PullResult[] = [];
  let coins = save.coins - cost;
  for (let i = 0; i < count; i++) {
    const guaranteed = count === 10 && i === count - 1 && !results.some((r) => r.card.rarity >= 3);
    const rarity = rollRarity(guaranteed ? 3 : 1);
    const card = pickOne(pool.filter((c) => c.rarity === rarity));
    const duplicate = owned.has(card.key);
    const refund = duplicate ? DUPLICATE[rarity] : 0;
    coins += refund;
    owned.add(card.key);
    results.push({ card, duplicate, refund });
  }
  saveClub({ ...save, coins, owned: [...owned], pulls: save.pulls + count });
  return results;
}

export interface MatchReward {
  /** Monedas en total (partido, goles, rango S y escudo repetido). */
  coins: number;
  /** Escudo nuevo ganado con la victoria. */
  crest?: string;
  /** Uniforme nuevo ganado con la victoria. */
  uniform?: string;
  /** Formación nueva ganada con la victoria. */
  formation?: string;
  rankS: boolean;
  /** Cuaderno del rango S. */
  notebook?: MoveData;
}

/** Premio por terminar un partido: monedas según el resultado y los goles; si se gana, un escudo, un uniforme y una formación; con 5-0, el rango S. */
export function rewardMatch(goalsFor: number, goalsAgainst: number, withClub: boolean): MatchReward | null {
  const save = loadClub();
  if (!save) return null;
  const table = withClub ? REWARD.club : REWARD.other;
  const result = goalsFor > goalsAgainst ? 'win' : goalsFor < goalsAgainst ? 'loss' : 'draw';
  let coins = table[result] + table.goal * goalsFor;
  const next: ClubSave = { ...save };
  const reward: MatchReward = { coins: 0, rankS: false };
  if (result === 'win') {
    const [crest] = newCrests(save.crests ?? [], 1);
    if (crest) {
      next.crests = [...(save.crests ?? []), crest];
      reward.crest = crest;
    } else coins += CREST_FULL_COINS;
    const uniform = newUniform(save.uniforms ?? []);
    if (uniform) {
      next.uniforms = [...(save.uniforms ?? []), uniform];
      reward.uniform = uniform;
    } else coins += CREST_FULL_COINS;
    const have = new Set((save.formations ?? []).map(formationId));
    const left = PRIZE_FORMATIONS().filter((id) => !have.has(id));
    if (left.length) {
      const f = pickOne(left);
      next.formations = [...have, f];
      reward.formation = f;
    } else coins += CREST_FULL_COINS;
  }
  if (goalsFor >= RANK_S.goals && goalsAgainst === 0) {
    reward.rankS = true;
    coins += RANK_S.coins;
    const good = Object.values(MOVES).filter((m) => notebookRarity(m) >= 3);
    if (good.length) {
      const move = pickOne(good);
      next.notebooks = { ...(save.notebooks ?? {}), [move.id]: (save.notebooks?.[move.id] ?? 0) + 1 };
      reward.notebook = move;
    }
  }
  reward.coins = coins;
  saveClub({ ...next, coins: save.coins + coins });
  return reward;
}

export { RARITY };

export const cardOverall = playerOverall;

/**
 * Mejor plantilla posible con lo que se tiene: para cada hueco de la formación, el mejor jugador de ese puesto
 * que quede; el banquillo, los mejores que sobren (con un portero si lo hay). Devuelve las claves en orden.
 */
export function autoSquad(save: ClubSave, size = 16): string[] {
  const cards = save.owned.map((k) => cardByKey(k)).filter((c): c is Card => !!c);
  const byOverall = (a: Card, b: Card) => cardOverall(b.player) - cardOverall(a.player);
  const left = [...cards].sort(byOverall);
  const take = (pred: (c: Card) => boolean): Card | undefined => {
    const i = left.findIndex(pred);
    return i >= 0 ? left.splice(i, 1)[0] : undefined;
  };
  const squad: string[] = [];
  for (const slot of getFormation(save.formation).slots) {
    const c = take((x) => x.player.position === slot.pos) ?? take(() => true);
    if (c) squad.push(c.key);
  }
  const gk = take((x) => x.player.position === 'GK');
  if (gk) squad.push(gk.key);
  while (squad.length < size && left.length) squad.push(left.shift()!.key);
  return squad;
}

// ------------------------------------------------------------ supertécnicas

/** Las técnicas de un jugador del club: las elegidas o, si no se han tocado, las suyas (4 de base, 2 extra vacías). */
export function movesFor(save: ClubSave, card: Card): { base: string[]; extra: string[] } {
  const c = save.custom?.[card.key];
  const pad = (list: string[], n: number) => [...list.slice(0, n), ...Array(Math.max(0, n - list.length)).fill('')];
  if (c) return { base: pad(c.base, BASE_SLOTS), extra: pad(c.extra, EXTRA_SLOTS) };
  return { base: pad(card.player.moves, BASE_SLOTS), extra: pad([], EXTRA_SLOTS) };
}

/** Cuadernos de una técnica que no está puesta en ningún jugador (las suyas propias no gastan cuaderno). */
export function freeNotebooks(save: ClubSave, moveId: string): number {
  let used = 0;
  for (const [key, c] of Object.entries(save.custom ?? {})) {
    const own = cardByKey(key)?.player.moves ?? [];
    used += [...c.base, ...c.extra].filter((m) => m === moveId && !own.includes(m)).length;
  }
  return (save.notebooks?.[moveId] ?? 0) - used;
}

/** Cambia las técnicas de un jugador. Devuelve false si se usa un cuaderno que no se tiene. */
export function setMoves(save: ClubSave, card: Card, base: string[], extra: string[]): boolean {
  const next: ClubSave = { ...save, custom: { ...(save.custom ?? {}), [card.key]: { base, extra } } };
  const own = card.player.moves;
  for (const m of new Set([...base, ...extra].filter((x) => x && !own.includes(x)))) {
    if (freeNotebooks(next, m) < 0) return false;
  }
  saveClub(next);
  upsertTeam(clubTeam(next));
  return true;
}

/** Rareza de un cuaderno según la potencia de la técnica entre las de su tipo: el 7 % más potente es ★★★★. */
let moveRarity: Map<string, Rarity> | null = null;
export function notebookRarity(move: MoveData): Rarity {
  if (!moveRarity) {
    moveRarity = new Map();
    for (const kind of ['shoot', 'dribble', 'block', 'catch']) {
      const list = Object.values(MOVES)
        .filter((m) => m.kind === kind)
        .sort((a, b) => a.power - b.power);
      list.forEach((m, i) => {
        const f = i / Math.max(1, list.length - 1);
        moveRarity!.set(m.id, f >= 0.93 ? 4 : f >= 0.75 ? 3 : f >= 0.4 ? 2 : 1);
      });
    }
  }
  return moveRarity.get(move.id) ?? 1;
}

export interface NotebookResult {
  move: MoveData;
  rarity: Rarity;
  total: number;
}

/** Tiradas de cuadernos. Las de diez traen al menos uno ★★★. */
export function pullNotebooks(count: 1 | 10): NotebookResult[] | null {
  const save = loadClub();
  const cost = count === 10 ? TEN_NOTEBOOK_COST : NOTEBOOK_COST;
  if (!save || save.coins < cost) return null;
  const notebooks = { ...(save.notebooks ?? {}) };
  const all = Object.values(MOVES);
  const results: NotebookResult[] = [];
  for (let i = 0; i < count; i++) {
    const guaranteed = count === 10 && i === count - 1 && !results.some((r) => r.rarity >= 3);
    const rarity = rollRarity(guaranteed ? 3 : 1);
    const move = pickOne(all.filter((m) => notebookRarity(m) === rarity));
    notebooks[move.id] = (notebooks[move.id] ?? 0) + 1;
    results.push({ move, rarity, total: notebooks[move.id] });
  }
  saveClub({ ...save, coins: save.coins - cost, notebooks });
  return results;
}
