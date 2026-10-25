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
