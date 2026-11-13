/**
 * Copia de seguridad de la partida: todo lo que InaMatch guarda en el navegador (Mi club, historia, torneo, ajustes y
 * sonido) en un archivo .json que se puede guardar y volver a cargar, en este navegador o en otro.
 */

/** Claves del navegador que son de InaMatch. */
export const SAVE_PREFIX = 'inamatch-';
export const SAVE_APP = 'inamatch';
export const SAVE_VERSION = 1;

export interface SaveFile {
  app: typeof SAVE_APP;
  v: number;
  /** Fecha de la copia (ISO). */
  date: string;
  /** clave del navegador -> lo que tenía guardado (texto). */
  data: Record<string, string>;
}

/** Lo mínimo de localStorage que hace falta (así se puede probar sin navegador). */
export interface KeyValueStore {
  readonly length: number;
  key(i: number): string | null;
  getItem(key: string): string | null;
  setItem(key: string, value: string): void;
  removeItem(key: string): void;
}

/** Copia de todo lo de InaMatch que hay en el almacenamiento. */
export function exportSave(store: KeyValueStore, now = new Date()): SaveFile {
  const data: Record<string, string> = {};
  for (let i = 0; i < store.length; i++) {
    const k = store.key(i);
    if (!k || !k.startsWith(SAVE_PREFIX)) continue;
    const v = store.getItem(k);
    if (v !== null) data[k] = v;
  }
  return { app: SAVE_APP, v: SAVE_VERSION, date: now.toISOString(), data };
}

export type ImportResult = { ok: true; keys: number } | { ok: false; error: string };

/** Comprueba un archivo de copia y, si es válido, lo carga (sustituye la partida de este navegador). */
export function importSave(store: KeyValueStore, text: string): ImportResult {
  let file: Partial<SaveFile>;
  try {
    file = JSON.parse(text) as Partial<SaveFile>;
  } catch {
    return { ok: false, error: 'El archivo no es una copia de InaMatch (no se puede leer).' };
  }
  if (!file || file.app !== SAVE_APP || typeof file.data !== 'object' || file.data === null) {
    return { ok: false, error: 'El archivo no es una copia de InaMatch.' };
  }
  if (typeof file.v !== 'number' || file.v > SAVE_VERSION) {
    return { ok: false, error: 'La copia es de una versión más nueva del juego.' };
  }
  const entries = Object.entries(file.data).filter(([k, v]) => k.startsWith(SAVE_PREFIX) && typeof v === 'string');
  if (!entries.length) return { ok: false, error: 'La copia está vacía.' };
  // cada valor tiene que ser JSON válido (es lo que guarda el juego)
  for (const [k, v] of entries) {
    try {
      JSON.parse(v);
    } catch {
      return { ok: false, error: `La copia está dañada (${k}).` };
    }
  }
  // se borra la partida actual y se pone la de la copia
  const old: string[] = [];
  for (let i = 0; i < store.length; i++) {
    const k = store.key(i);
    if (k?.startsWith(SAVE_PREFIX)) old.push(k);
  }
  old.forEach((k) => store.removeItem(k));
  for (const [k, v] of entries) store.setItem(k, v);
  return { ok: true, keys: entries.length };
}

/** Nombre del archivo de la copia: inamatch-partida-2026-11-13.json */
export function saveFileName(now = new Date()): string {
  return `inamatch-partida-${now.toISOString().slice(0, 10)}.json`;
}

// ----------------------------------------------------------- en el navegador

/** Descarga la copia de la partida como archivo. Devuelve false si no se puede (sin almacenamiento). */
export function downloadSave(): boolean {
  try {
    const file = exportSave(window.localStorage);
    const blob = new Blob([JSON.stringify(file, null, 1)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = saveFileName();
    document.body.appendChild(a);
    a.click();
    a.remove();
    setTimeout(() => URL.revokeObjectURL(url), 2000);
    return true;
  } catch {
    return false;
  }
}

/** Abre el selector de archivos y carga la copia elegida. `done` recibe el resultado (nada si se cancela). */
export function pickSaveFile(done: (result: ImportResult) => void): void {
  const input = document.createElement('input');
  input.type = 'file';
  input.accept = '.json,application/json';
  input.style.display = 'none';
  input.addEventListener('change', () => {
    const f = input.files?.[0];
    input.remove();
    if (!f) return;
    if (f.size > 5 * 1024 * 1024) {
      done({ ok: false, error: 'El archivo es demasiado grande para ser una copia de InaMatch.' });
      return;
    }
    f.text()
      .then((text) => {
        try {
          done(importSave(window.localStorage, text));
        } catch {
          done({ ok: false, error: 'No se ha podido guardar en este navegador.' });
        }
      })
      .catch(() => done({ ok: false, error: 'No se ha podido leer el archivo.' }));
  });
  document.body.appendChild(input);
  input.click();
}
