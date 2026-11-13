import { describe, expect, it } from 'vitest';
import { TEAMS } from '../data';
import type { StoryBook, StoryLine } from './story';

const files = import.meta.glob<{ default: StoryBook }>('../data/story/*.json', { eager: true });
const BOOK: StoryBook = Object.assign({}, ...Object.values(files).map((m) => m.default));
const BY_ID = new Map(TEAMS.map((t) => [t.id, t]));

/** Rutas de la historia original de cada juego (pueden ser más largas). */
export const MAIN_ROUTES = [
  'ie1-raimon',
  'ie2-second-raimon',
  'ie3-inazuma-japan',
  'go-shinsei-raimon',
  'cs-team-raimon',
  'gx-earth-eleven',
  'ares-inakuni-raimon',
  'orion-inazuma-japan-orion',
  'vr-nagumohara',
];

function checkLines(where: string, lines: StoryLine[], errors: string[]): void {
  if (!Array.isArray(lines) || !lines.length) errors.push(`${where}: sin diálogo`);
  for (const l of lines ?? []) {
    if (!l.text?.trim()) errors.push(`${where}: línea vacía`);
    if (l.text && l.text.length > 240) errors.push(`${where}: línea demasiado larga (${l.text.length})`);
    if (l.who) {
      const [t, p] = l.who.split('/');
      const team = BY_ID.get(t);
      if (!team) errors.push(`${where}: equipo desconocido en "${l.who}"`);
      else if (!team.players.some((x) => x.id === p)) errors.push(`${where}: jugador desconocido en "${l.who}"`);
    }
  }
}

describe('modo historia', () => {
  it('cada equipo tiene su historia', () => {
    const missing = TEAMS.filter((t) => t.id !== 'club' && !BOOK[t.id]).map((t) => t.id);
    expect(missing).toEqual([]);
  });

  it('las historias son válidas (rivales, quién habla, longitud de las rutas)', () => {
    const errors: string[] = [];
    for (const [id, s] of Object.entries(BOOK)) {
      if (!BY_ID.has(id)) errors.push(`${id}: no es un equipo`);
      if (!s.title?.trim() || !s.summary?.trim()) errors.push(`${id}: sin título o resumen`);
      const main = MAIN_ROUTES.includes(id);
      if (!!s.main !== main) errors.push(`${id}: main debería ser ${main}`);
      const n = s.stages?.length ?? 0;
      if (main ? n < 5 : n < 5 || n > 7) errors.push(`${id}: ${n} partidos`);
      checkLines(`${id} intro`, s.intro, errors);
      checkLines(`${id} final`, s.ending, errors);
      (s.stages ?? []).forEach((st, i) => {
        if (!BY_ID.has(st.opponent)) errors.push(`${id} #${i + 1}: rival desconocido ${st.opponent}`);
        if (st.opponent === id) errors.push(`${id} #${i + 1}: juega contra sí mismo`);
        if (!st.title?.trim()) errors.push(`${id} #${i + 1}: sin título`);
        checkLines(`${id} #${i + 1} antes`, st.before, errors);
        checkLines(`${id} #${i + 1} después`, st.after, errors);
      });
    }
    expect(errors).toEqual([]);
  });
});
