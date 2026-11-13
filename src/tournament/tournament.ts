/**
 * Modo torneo: una copa (eliminatorias de 8 equipos) o una liga (6 equipos, todos contra todos a una vuelta).
 * El jugador juega sus partidos; los demás se simulan con la media de cada equipo.
 * Funciones puras (sin Phaser): el estado se guarda en el navegador (TOURNEY_KEY) como JSON.
 */

export type TourneyKind = 'cup' | 'league';

export interface MatchResult {
  home: string;
  away: string;
  /** Goles; null si aún no se ha jugado. */
  hg: number | null;
  ag: number | null;
  /** Copa: si acabó en empate, el ganador en los penaltis y el resultado de la tanda. */
  pens?: { home: number; away: number };
}

export interface Tourney {
  v: 1;
  kind: TourneyKind;
  /** Equipo del jugador. */
  user: string;
  /** Equipos participantes, en el orden del cuadro (copa) o del sorteo (liga). */
  teams: string[];
  /** Rondas (copa: cuartos, semis, final; liga: jornadas). */
  rounds: MatchResult[][];
  /** Ronda en juego. */
  round: number;
  /** Terminado: campeón (id) o null mientras se juega. */
  champion: string | null;
  /** Copa: el jugador ha sido eliminado (el torneo sigue simulándose hasta el final al rendirse). */
  out: boolean;
  /** Monedas ya cobradas. */
  paid?: boolean;
}

export type Rng = () => number;

export const TOURNEY_KEY = 'inamatch-tournament';
export const CUP_SIZE = 8;
export const LEAGUE_SIZE = 6;
/** Puntos de liga. */
export const POINTS = { win: 3, draw: 1, loss: 0 };
/** Monedas para Mi club: campeón, subcampeón y el resto (por haber jugado). */
export const TOURNEY_COINS = { champion: 800, runnerUp: 300, played: 100 };

export const CUP_ROUND_NAMES = ['Cuartos de final', 'Semifinales', 'Final'];

/** Baraja una copia (Fisher-Yates). */
export function shuffle<T>(list: T[], rng: Rng): T[] {
  const a = [...list];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(rng() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

/** Elige `n` rivales al azar de una lista de candidatos (sin el equipo del jugador). */
export function pickOpponents(user: string, candidates: string[], n: number, rng: Rng): string[] {
  return shuffle(
    candidates.filter((t) => t !== user),
    rng,
  ).slice(0, n);
}

/** Copa de 8: sorteo del cuadro; el jugador puede caer en cualquier hueco. */
export function createCup(user: string, opponents: string[], rng: Rng): Tourney {
  if (opponents.length !== CUP_SIZE - 1) throw new Error(`La copa necesita ${CUP_SIZE - 1} rivales`);
  const teams = shuffle([user, ...opponents], rng);
  const first: MatchResult[] = [];
  for (let i = 0; i < teams.length; i += 2) first.push({ home: teams[i], away: teams[i + 1], hg: null, ag: null });
  return { v: 1, kind: 'cup', user, teams, rounds: [first], round: 0, champion: null, out: false };
}

/** Calendario de todos contra todos (método del círculo): n-1 jornadas de n/2 partidos. */
export function roundRobin(teams: string[]): [string, string][][] {
  const list = [...teams];
  if (list.length % 2) list.push('');
  const n = list.length;
  const rounds: [string, string][][] = [];
  for (let r = 0; r < n - 1; r++) {
    const games: [string, string][] = [];
    for (let i = 0; i < n / 2; i++) {
      const a = list[i];
      const b = list[n - 1 - i];
      if (a && b) games.push(r % 2 ? [b, a] : [a, b]);
    }
    rounds.push(games);
    // rota todos menos el primero
    list.splice(1, 0, list.pop()!);
  }
  return rounds;
}

/** Liga de 6 a una vuelta: 5 jornadas. */
export function createLeague(user: string, opponents: string[], rng: Rng): Tourney {
  if (opponents.length !== LEAGUE_SIZE - 1) throw new Error(`La liga necesita ${LEAGUE_SIZE - 1} rivales`);
  const teams = shuffle([user, ...opponents], rng);
  const rounds = roundRobin(teams).map((games) => games.map(([home, away]) => ({ home, away, hg: null, ag: null }) as MatchResult));
  return { v: 1, kind: 'league', user, teams, rounds, round: 0, champion: null, out: false };
}

/** El partido del jugador en la ronda actual (null si no juega o el torneo ha acabado). */
export function userMatch(t: Tourney): MatchResult | null {
  if (t.champion || t.out) return null;
  return t.rounds[t.round]?.find((m) => m.home === t.user || m.away === t.user) ?? null;
}

/** Goles de un partido simulado: cada equipo marca más cuanto mejor es su media frente a la del rival. */
export function simulateScore(ratingA: number, ratingB: number, rng: Rng): [number, number] {
  const diff = (ratingA - ratingB) / 10;
  const goals = (expected: number) => {
    // Poisson por el método de Knuth
    const L = Math.exp(-Math.max(0.2, expected));
    let k = 0;
    let p = 1;
    do {
      k++;
      p *= rng();
    } while (p > L && k < 12);
    return k - 1;
  };
  return [goals(1.4 + diff * 0.6), goals(1.4 - diff * 0.6)];
}

/** Tanda de penaltis simulada (5 lanzamientos y muerte súbita); nunca acaba en empate. */
export function penaltyShootout(rng: Rng): { home: number; away: number } {
  let h = 0;
  let a = 0;
  for (let i = 0; i < 5; i++) {
    if (rng() < 0.75) h++;
    if (rng() < 0.75) a++;
  }
  while (h === a) {
    if (rng() < 0.75) h++;
    if (rng() < 0.75) a++;
  }
  return { home: h, away: a };
}

/** Ganador de un partido jugado (copa: con penaltis si hubo empate); null si fue empate de liga o no se ha jugado. */
export function winnerOf(m: MatchResult): string | null {
  if (m.hg === null || m.ag === null) return null;
  if (m.hg > m.ag) return m.home;
  if (m.ag > m.hg) return m.away;
  if (m.pens) return m.pens.home > m.pens.away ? m.home : m.away;
  return null;
}

/** Pone el resultado de un partido; en copa, los empates se deciden en penaltis. */
function setScore(t: Tourney, m: MatchResult, hg: number, ag: number, rng: Rng): void {
  m.hg = hg;
  m.ag = ag;
  if (t.kind === 'cup' && hg === ag) m.pens = penaltyShootout(rng);
}

/**
 * Guarda el resultado del partido del jugador (goles a favor y en contra), simula el resto de la ronda y pasa a la
 * siguiente. Devuelve el torneo nuevo (no cambia el que recibe).
 */
export function recordUserResult(t: Tourney, goalsFor: number, goalsAgainst: number, rating: (team: string) => number, rng: Rng): Tourney {
  const next: Tourney = structuredCloneSafe(t);
  const m = userMatch(next);
  if (!m) return next;
  const userHome = m.home === next.user;
  setScore(next, m, userHome ? goalsFor : goalsAgainst, userHome ? goalsAgainst : goalsFor, rng);
  return advance(next, rating, rng);
}

/** Simula lo que queda de la ronda actual (los partidos sin jugar) y prepara la siguiente; si acaba, el campeón. */
export function advance(t: Tourney, rating: (team: string) => number, rng: Rng): Tourney {
  const round = t.rounds[t.round];
  for (const m of round) {
    if (m.hg !== null) continue;
    const [hg, ag] = simulateScore(rating(m.home), rating(m.away), rng);
    setScore(t, m, hg, ag, rng);
  }
  if (t.kind === 'cup') {
    const winners = round.map((m) => winnerOf(m)!);
    if (!winners.includes(t.user) && round.some((m) => m.home === t.user || m.away === t.user)) t.out = true;
    if (winners.length === 1) {
      t.champion = winners[0];
      return t;
    }
    const nextRound: MatchResult[] = [];
    for (let i = 0; i < winners.length; i += 2) nextRound.push({ home: winners[i], away: winners[i + 1], hg: null, ag: null });
    t.rounds.push(nextRound);
    t.round++;
    return t;
  }
  if (t.round + 1 >= t.rounds.length) {
    t.champion = standings(t)[0].team;
    return t;
  }
  t.round++;
  return t;
}

/** Eliminado de la copa: se simula el resto hasta tener campeón. */
export function finishWithoutUser(t: Tourney, rating: (team: string) => number, rng: Rng): Tourney {
  let next = structuredCloneSafe(t);
  let guard = 0;
  while (!next.champion && guard++ < 20) next = advance(next, rating, rng);
  return next;
}

export interface Standing {
  team: string;
  played: number;
  won: number;
  drawn: number;
  lost: number;
  gf: number;
  ga: number;
  points: number;
}

/** Clasificación de la liga: puntos, diferencia de goles, goles a favor y, al final, el orden del sorteo. */
export function standings(t: Tourney): Standing[] {
  const table = new Map<string, Standing>(t.teams.map((team) => [team, { team, played: 0, won: 0, drawn: 0, lost: 0, gf: 0, ga: 0, points: 0 }]));
  for (const round of t.rounds) {
    for (const m of round) {
      if (m.hg === null || m.ag === null) continue;
      const h = table.get(m.home)!;
      const a = table.get(m.away)!;
      h.played++;
      a.played++;
      h.gf += m.hg;
      h.ga += m.ag;
      a.gf += m.ag;
      a.ga += m.hg;
      if (m.hg > m.ag) {
        h.won++;
        a.lost++;
        h.points += POINTS.win;
      } else if (m.hg < m.ag) {
        a.won++;
        h.lost++;
        a.points += POINTS.win;
      } else {
        h.drawn++;
        a.drawn++;
        h.points += POINTS.draw;
        a.points += POINTS.draw;
      }
    }
  }
  const order = new Map(t.teams.map((team, i) => [team, i]));
  return [...table.values()].sort((x, y) => y.points - x.points || y.gf - y.ga - (x.gf - x.ga) || y.gf - x.gf || order.get(x.team)! - order.get(y.team)!);
}

/** Puesto final del jugador (1 = campeón); en copa, 2 = finalista y 3 = el resto. */
export function userPlace(t: Tourney): number {
  if (t.kind === 'league') return standings(t).findIndex((s) => s.team === t.user) + 1;
  if (t.champion === t.user) return 1;
  const final = t.rounds[CUP_ROUND_NAMES.length - 1];
  if (final?.some((m) => m.home === t.user || m.away === t.user)) return 2;
  return 3;
}

/** Monedas por el puesto final. */
export function tourneyCoins(t: Tourney): number {
  const place = userPlace(t);
  return place === 1 ? TOURNEY_COINS.champion : place === 2 ? TOURNEY_COINS.runnerUp : TOURNEY_COINS.played;
}

/** Nombre de la ronda actual. */
export function roundName(t: Tourney, round = t.round): string {
  return t.kind === 'cup' ? (CUP_ROUND_NAMES[round] ?? `Ronda ${round + 1}`) : `Jornada ${round + 1} de ${t.rounds.length}`;
}

/** Comprueba un torneo guardado (por si está dañado o es de otra versión). */
export function parseTourney(raw: string | null, exists: (team: string) => boolean): Tourney | null {
  if (!raw) return null;
  try {
    const t = JSON.parse(raw) as Tourney;
    if (t?.v !== 1 || (t.kind !== 'cup' && t.kind !== 'league') || !Array.isArray(t.teams) || !Array.isArray(t.rounds)) return null;
    if (!t.teams.every(exists)) return null;
    return t;
  } catch {
    return null;
  }
}

function structuredCloneSafe<T>(v: T): T {
  return JSON.parse(JSON.stringify(v)) as T;
}

// ------------------------------------------------------------ en el navegador

export function loadTourney(exists: (team: string) => boolean): Tourney | null {
  try {
    return parseTourney(window.localStorage.getItem(TOURNEY_KEY), exists);
  } catch {
    return null;
  }
}

export function saveTourney(t: Tourney | null): void {
  try {
    if (t) window.localStorage.setItem(TOURNEY_KEY, JSON.stringify(t));
    else window.localStorage.removeItem(TOURNEY_KEY);
  } catch {
    // sin almacenamiento
  }
}

/** El partido de torneo que se está jugando (lo leen la formación y el partido para volver al torneo). */
export const TOURNEY_REGISTRY = 'tourneyMatch';
export const TOURNEY_RESULT = 'tourneyResult';
export interface TourneyMatchResult {
  goalsFor: number;
  goalsAgainst: number;
  /** Abandonado: cuenta como derrota por 0-3. */
  quit?: boolean;
}
