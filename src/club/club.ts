import { MOVES, upsertTeam } from '../data';
import type { MoveData } from '../data/types';
import type { PlayerData, Position, TeamData } from '../data/types';
import { byPosition, cardByKey, cardForStaleKey, loadPool, RARITY, type Card, type Rarity } from './pool';

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
/** Monedas por partido: con tu club se gana más. */
export const REWARD = { club: { win: 150, draw: 80, loss: 50 }, other: { win: 40, draw: 30, loss: 20 } };

/** Huecos de la plantilla inicial (4-4-2 y banquillo). */
const START_SLOTS: Position[] = ['GK', 'DF', 'DF', 'DF', 'DF', 'MF', 'MF', 'MF', 'MF', 'FW', 'FW', 'GK', 'DF', 'MF', 'FW', 'MF'];
const START_FORMATION = 'f-4-4-2';

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
    save = { v: 1, name: 'Mi club', coins: START_COINS, owned: [...squad], squad, formation: START_FORMATION, pulls: 0 };
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
    return [{ ...card.player, id, number: i + 1, origin: card.origin, originId: card.player.id, moves }];
  });
  return {
    id: 'club',
    season: 'club',
    name: save.name,
    short: 'MIC',
    colors: { shirt: '#ffd23f', shorts: '#0b1a2e', gkShirt: '#2f7bff', accent: '#ffd23f' },
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

/** Monedas por terminar un partido. Devuelve las ganadas. */
export function rewardMatch(result: 'win' | 'draw' | 'loss', withClub: boolean): number {
  const save = loadClub();
  if (!save) return 0;
  const coins = (withClub ? REWARD.club : REWARD.other)[result];
  saveClub({ ...save, coins: save.coins + coins });
  return coins;
}

export { RARITY };

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
