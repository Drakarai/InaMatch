import type { PlayerData, TeamData } from '../data/types';

/** Media del equipo: la de los atributos de campo de sus 11 titulares (o de los jugadores que se pasen). */
export function teamRating(team: TeamData, starters: PlayerData[] = team.players.slice(0, 11)): number {
  const keys = ['kick', 'body', 'control', 'guard', 'speed', 'guts'] as const;
  const perPlayer = starters.map((p) => keys.reduce((sum, k) => sum + p.stats[k], 0) / keys.length);
  return Math.round(perPlayer.reduce((a, b) => a + b, 0) / Math.max(1, perPlayer.length));
}

/** Estrellas de 0,5 a 5 en pasos de media, como en FIFA. Las medias de la saga van de ~45 a ~75. */
export function ratingStars(rating: number): number {
  const stars = (rating - 45) / 6 + 0.5;
  return Math.min(5, Math.max(0.5, Math.round(stars * 2) / 2));
}

export interface LineRatings {
  att: number;
  mid: number;
  def: number;
}

/**
 * Medias por líneas, como el ATA/MED/DEF de FIFA, con los titulares:
 * delanteros (tiro, control y velocidad), medios (control, físico, velocidad y tiro)
 * y defensas más portero (defensa, físico y agallas). Si una línea está vacía cuenta todo el equipo.
 */
export function lineRatings(team: TeamData, starters: PlayerData[] = team.players.slice(0, 11)): LineRatings {
  const line = (positions: string[], keys: (keyof PlayerData['stats'])[]) => {
    const group = starters.filter((p) => positions.includes(p.position));
    const players = group.length ? group : starters;
    const per = players.map((p) => keys.reduce((s, k) => s + p.stats[k], 0) / keys.length);
    return Math.round(per.reduce((a, b) => a + b, 0) / Math.max(1, per.length));
  };
  return {
    att: line(['FW'], ['kick', 'control', 'speed']),
    mid: line(['MF'], ['control', 'body', 'speed', 'kick']),
    def: line(['DF', 'GK'], ['guard', 'body', 'guts']),
  };
}
