import { describe, expect, it } from 'vitest';
import { exportSave, importSave, saveFileName, SAVE_VERSION, type KeyValueStore } from './save';

/** Almacenamiento en memoria con la misma interfaz que localStorage. */
function memoryStore(init: Record<string, string> = {}): KeyValueStore & { dump(): Record<string, string> } {
  const m = new Map(Object.entries(init));
  return {
    get length() {
      return m.size;
    },
    key: (i) => [...m.keys()][i] ?? null,
    getItem: (k) => (m.has(k) ? m.get(k)! : null),
    setItem: (k, v) => void m.set(k, v),
    removeItem: (k) => void m.delete(k),
    dump: () => Object.fromEntries(m),
  };
}

const CLUB = JSON.stringify({ v: 1, name: 'Mi club', coins: 900 });
const STORY = JSON.stringify({ stage: { 'ie1-raimon': 3 }, done: {} });

describe('copia de la partida', () => {
  it('exporta solo lo de InaMatch', () => {
    const store = memoryStore({ 'inamatch-club': CLUB, 'inamatch-story': STORY, 'otra-web': 'x' });
    const file = exportSave(store, new Date('2026-11-13T10:00:00Z'));
    expect(file.app).toBe('inamatch');
    expect(file.v).toBe(SAVE_VERSION);
    expect(file.date).toBe('2026-11-13T10:00:00.000Z');
    expect(Object.keys(file.data).sort()).toEqual(['inamatch-club', 'inamatch-story']);
  });

  it('exportar e importar deja la misma partida (y borra la que había)', () => {
    const from = memoryStore({ 'inamatch-club': CLUB, 'inamatch-story': STORY });
    const text = JSON.stringify(exportSave(from));
    const to = memoryStore({ 'inamatch-club': JSON.stringify({ coins: 1 }), 'inamatch-tournament': '{}', 'otra-web': 'x' });
    const res = importSave(to, text);
    expect(res).toEqual({ ok: true, keys: 2 });
    expect(to.dump()).toEqual({ 'inamatch-club': CLUB, 'inamatch-story': STORY, 'otra-web': 'x' });
  });

  it('rechaza archivos que no son copias de InaMatch, sin tocar nada', () => {
    const store = memoryStore({ 'inamatch-club': CLUB });
    const before = store.dump();
    for (const text of ['no es json', '{}', JSON.stringify({ app: 'otra', v: 1, data: {} }), JSON.stringify({ app: 'inamatch', v: 1 })]) {
      const res = importSave(store, text);
      expect(res.ok).toBe(false);
    }
    expect(store.dump()).toEqual(before);
  });

  it('rechaza copias de una versión más nueva, vacías o dañadas', () => {
    const store = memoryStore({ 'inamatch-club': CLUB });
    expect(importSave(store, JSON.stringify({ app: 'inamatch', v: SAVE_VERSION + 1, data: { 'inamatch-club': CLUB } })).ok).toBe(false);
    expect(importSave(store, JSON.stringify({ app: 'inamatch', v: 1, data: {} })).ok).toBe(false);
    expect(importSave(store, JSON.stringify({ app: 'inamatch', v: 1, data: { 'inamatch-club': '{roto' } })).ok).toBe(false);
    expect(store.getItem('inamatch-club')).toBe(CLUB);
  });

  it('ignora claves ajenas que vengan en la copia', () => {
    const store = memoryStore();
    const res = importSave(store, JSON.stringify({ app: 'inamatch', v: 1, data: { 'inamatch-club': CLUB, 'mala-clave': '1' } }));
    expect(res).toEqual({ ok: true, keys: 1 });
    expect(store.getItem('mala-clave')).toBeNull();
  });

  it('nombre del archivo con la fecha', () => {
    expect(saveFileName(new Date('2026-11-13T10:00:00Z'))).toBe('inamatch-partida-2026-11-13.json');
  });
});
