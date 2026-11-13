/**
 * Enciclopedia: listas filtradas y paginadas de jugadores, técnicas y uniformes (funciones puras, sin Phaser).
 */
import type { MoveData, MoveKind, Position } from '../data/types';

export interface CodexCard {
  key: string;
  season: string;
  rarity: number;
  player: { name: string; position: Position };
}

export interface CardFilter {
  /** Temporada ('all' = todas). */
  season: string;
  /** Demarcación ('all' = todas). */
  position: Position | 'all';
  /** Solo los conseguidos en Mi club. */
  ownedOnly: boolean;
}

/** Jugadores que pasan el filtro: primero los de más rareza y, dentro, por nombre. */
export function filterCards<T extends CodexCard>(cards: T[], f: CardFilter, owned: Set<string>): T[] {
  return cards
    .filter((c) => (f.season === 'all' || c.season === f.season) && (f.position === 'all' || c.player.position === f.position) && (!f.ownedOnly || owned.has(c.key)))
    .sort((a, b) => b.rarity - a.rarity || a.player.name.localeCompare(b.player.name, 'es'));
}

/** Técnicas de un tipo ('all' = todas), de más a menos potencia y, a igualdad, por nombre. */
export function filterMoves(moves: MoveData[], kind: MoveKind | 'all', ownedOnly = false, notebooks: Record<string, number> = {}): MoveData[] {
  return moves
    .filter((m) => (kind === 'all' || m.kind === kind) && (!ownedOnly || (notebooks[m.id] ?? 0) > 0))
    .sort((a, b) => b.power - a.power || a.name.localeCompare(b.name, 'es'));
}

export interface Page<T> {
  items: T[];
  /** Página mostrada (ajustada al rango). */
  page: number;
  pages: number;
}

/** Una página de la lista (las páginas empiezan en 0; si se pasa del final, la última). */
export function paginate<T>(list: T[], page: number, size: number): Page<T> {
  const pages = Math.max(1, Math.ceil(list.length / size));
  const p = Math.min(Math.max(0, page), pages - 1);
  return { items: list.slice(p * size, p * size + size), page: p, pages };
}

/** "12 / 340 (3 %)": cuántos se tienen de cuántos hay. */
export function progressLabel(have: number, total: number): string {
  const pct = total ? Math.floor((have / total) * 100) : 0;
  return `${have} / ${total} (${pct} %)`;
}

export const KIND_LABEL: Record<MoveKind, string> = {
  shoot: 'Tiro',
  dribble: 'Regate',
  block: 'Bloqueo',
  catch: 'Parada',
};
