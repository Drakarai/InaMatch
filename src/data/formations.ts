import generated from './formations.json';
import aliases from './formation-aliases.json';
import type { Formation, FormationSlot } from './types';

/** Fila de cada línea (0 = portería rival, 1 = portería propia). */
const ROW_Y = { DF: 0.78, MF: 0.56, FW: 0.35 } as const;

/**
 * Formación a partir de su distribución ("4-4-2", "5-3-2"...), como las de la wiki.
 * Los jugadores de cada línea se reparten a lo ancho y los de las bandas se adelantan un poco.
 */
export function formationFromLayout(id: string, name: string, layout: string): Formation {
  const counts = layout.split('-').map(Number);
  const slots: FormationSlot[] = [{ pos: 'GK', x: 0.5, y: 0.96 }];
  (['DF', 'MF', 'FW'] as const).forEach((pos, line) => {
    const n = counts[line] ?? 0;
    for (let i = 0; i < n; i++) {
      const x = n === 1 ? 0.5 : 0.12 + (i * 0.76) / (n - 1);
      const wing = n > 2 && (i === 0 || i === n - 1) ? -0.04 : 0;
      slots.push({ pos, x, y: ROW_Y[pos] + wing });
    }
  });
  return { id, name, slots, layout };
}

/**
 * Las de la wiki (src/data/formations.json): las que salen en la wiki llevan la posición de cada jugador, sacada de sus
 * imágenes de formación (las de los juegos de DS, Chrono Stone y Victory Road; las que coinciden en todos los puestos
 * están juntas, con los otros nombres en `also`). Las de los equipos sin formación en la wiki son genéricas, por
 * distribución (F-4-4-2...).
 */
type FormationEntry = { id: string; name: string; layout: string; slots?: FormationSlot[]; also?: string[] };
export const FORMATIONS: Formation[] = (generated as FormationEntry[]).map((f) =>
  f.slots ? { id: f.id, name: f.name, slots: f.slots, layout: f.layout, also: f.also } : { ...formationFromLayout(f.id, f.name, f.layout), layout: f.layout },
);

/** Ids que ya no existen (formaciones juntadas o hechas a mano antes): para las partidas guardadas. */
const ALIASES = aliases as Record<string, string>;

export function getFormation(id: string): Formation {
  const real = ALIASES[id] ?? id;
  return FORMATIONS.find((f) => f.id === real) ?? FORMATIONS.find((f) => f.id === 'f-4-4-2') ?? FORMATIONS[0];
}
