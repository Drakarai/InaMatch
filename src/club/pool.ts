import { TEAMS } from '../data';
import type { PlayerData, Position } from '../data/types';

/**
 * Todos los jugadores que se pueden fichar: los de los equipos y los ojeadores (src/data/scouts.json, que se
 * carga aparte porque son miles). Cada personaje sale una vez, en su mejor versión.
 */

export type Rarity = 1 | 2 | 3 | 4;

export interface Card {
  /** "<equipo de origen>:<id del jugador>": lo que se guarda en la partida. */
  key: string;
  origin: string;
  player: PlayerData;
  season: string;
  rarity: Rarity;
  /** En cuántos equipos sale el personaje (lo conocido que es). */
  fame: number;
}

export const RARITY: Record<Rarity, { name: string; color: number; css: string }> = {
  1: { name: 'Ojeador', color: 0x9aa7b8, css: '#c9d3e0' },
  2: { name: 'Poco conocido', color: 0x46d68c, css: '#7dff9a' },
  3: { name: 'Conocido', color: 0x4fa3ff, css: '#8fc6ff' },
  4: { name: 'Estrella', color: 0xffd23f, css: '#ffd23f' },
};

type ScoutsFile = Record<string, PlayerData[]>;

let cache: Card[] | null = null;
let index = new Map<string, Card>();

const total = (p: PlayerData) => Object.values(p.stats).reduce((a, b) => a + b, 0) + (p.fp + p.tp) / 4;

/** Rareza por lo conocido que es: ojeadores, de un equipo, de dos o tres, o de cuatro o más (Mark, Axel...). */
export function rarityOf(fame: number): Rarity {
  return fame === 0 ? 1 : fame === 1 ? 2 : fame <= 3 ? 3 : 4;
}

export async function loadPool(): Promise<Card[]> {
  if (cache) return cache;
  const scouts = ((await import('../data/scouts.json')).default ?? {}) as ScoutsFile;
  const versions = new Map<string, { origin: string; season: string; player: PlayerData }[]>();
  const teamsOf = new Map<string, Set<string>>();
  const add = (wiki: string, origin: string, season: string, player: PlayerData) => {
    if (!versions.has(wiki)) versions.set(wiki, []);
    versions.get(wiki)!.push({ origin, season, player });
  };
  for (const team of TEAMS) {
    if (team.id === 'club') continue;
    for (const p of team.players) {
      const wiki = p.wiki ?? `${team.id}:${p.id}`;
      add(wiki, team.id, team.season ?? 'otros', p);
      if (!teamsOf.has(wiki)) teamsOf.set(wiki, new Set());
      teamsOf.get(wiki)!.add(team.id);
    }
  }
  for (const [season, players] of Object.entries(scouts)) {
    for (const p of players) add(p.wiki ?? `scouts-${season}:${p.id}`, `scouts-${season}`, season, p);
  }
  const cards: Card[] = [];
  for (const [wiki, list] of versions) {
    const best = list.reduce((a, b) => (total(b.player) > total(a.player) ? b : a));
    const fame = teamsOf.get(wiki)?.size ?? 0;
    cards.push({ key: `${best.origin}:${best.player.id}`, origin: best.origin, player: best.player, season: best.season, rarity: rarityOf(fame), fame });
  }
  cache = cards;
  index = new Map(cards.map((c) => [c.key, c]));
  return cards;
}

export function cardByKey(key: string): Card | undefined {
  return index.get(key);
}

export function byPosition(pool: Card[], pos: Position, rarity?: Rarity): Card[] {
  return pool.filter((c) => c.player.position === pos && (rarity === undefined || c.rarity === rarity));
}
