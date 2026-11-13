/**
 * Ajustes de juego que se guardan en el navegador (los de sonido van aparte, en audio/engine.ts).
 * - Dificultad de la CPU: Fácil, Normal o Difícil. Afecta a cómo juega y a lo fuerte que es en los duelos.
 */

export type Difficulty = 'easy' | 'normal' | 'hard';

export interface DifficultyProfile {
  label: string;
  /** Explicación corta para el panel de ajustes. */
  hint: string;
  /** Multiplica los atributos de los jugadores de la CPU en duelos, tiros y paradas. */
  power: number;
  /** Multiplica la probabilidad de que la CPU use supertécnica (sobre la de cada situación). */
  moveChance: number;
  /** Velocidad con la que la CPU presiona al que lleva el balón (1 = la de sus propios jugadores). */
  press: number;
  /** Segundos entre decisiones de la CPU con balón (pasar, tirar). */
  think: number;
  /** Se suma a la probabilidad de que la CPU tire desde la zona de tiro. */
  shotBias: number;
}

export const DIFFICULTIES: Record<Difficulty, DifficultyProfile> = {
  easy: { label: 'Fácil', hint: 'La CPU es más lenta, falla más y usa menos supertécnicas', power: 0.88, moveChance: 0.6, press: 0.78, think: 0.5, shotBias: -0.15 },
  normal: { label: 'Normal', hint: 'Como siempre: un reto justo', power: 1, moveChance: 1, press: 0.88, think: 0.3, shotBias: 0 },
  hard: { label: 'Difícil', hint: 'La CPU presiona más, piensa más rápido y es más fuerte', power: 1.12, moveChance: 1.35, press: 0.97, think: 0.18, shotBias: 0.12 },
};

export const DIFFICULTY_ORDER: Difficulty[] = ['easy', 'normal', 'hard'];

export interface GameSettings {
  difficulty: Difficulty;
}

export const SETTINGS_KEY = 'inamatch-settings';
const DEFAULTS: GameSettings = { difficulty: 'normal' };

let memory: GameSettings | null = null;
const listeners = new Set<() => void>();

/** Los ajustes guardados (o los de por defecto); lo que no sea válido se ignora. */
export function parseSettings(raw: string | null): GameSettings {
  if (!raw) return { ...DEFAULTS };
  try {
    const s = JSON.parse(raw) as Partial<GameSettings>;
    return { difficulty: s.difficulty && s.difficulty in DIFFICULTIES ? s.difficulty : DEFAULTS.difficulty };
  } catch {
    return { ...DEFAULTS };
  }
}

export function getSettings(): GameSettings {
  if (memory) return memory;
  let raw: string | null = null;
  try {
    raw = window.localStorage.getItem(SETTINGS_KEY);
  } catch {
    // sin almacenamiento: los de por defecto
  }
  memory = parseSettings(raw);
  return memory;
}

export function setSettings(patch: Partial<GameSettings>): void {
  memory = { ...getSettings(), ...patch };
  try {
    window.localStorage.setItem(SETTINGS_KEY, JSON.stringify(memory));
  } catch {
    // sin almacenamiento: dura lo que la pestaña
  }
  listeners.forEach((fn) => fn());
}

/** Vuelve a leer los ajustes del navegador (después de importar una partida). */
export function reloadSettings(): void {
  memory = null;
  listeners.forEach((fn) => fn());
}

export function onSettingsChange(fn: () => void): () => void {
  listeners.add(fn);
  return () => listeners.delete(fn);
}

/** El perfil de la dificultad elegida. */
export function difficulty(): DifficultyProfile {
  return DIFFICULTIES[getSettings().difficulty];
}

/** Probabilidad de supertécnica de la CPU con la dificultad (entre 0 y 1). */
export function cpuMoveChance(base: number, profile: DifficultyProfile = difficulty()): number {
  return Math.min(1, Math.max(0, base * profile.moveChance));
}
