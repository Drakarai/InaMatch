import generated from './formations.json';
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
  return { id, name, slots };
}

const HANDMADE: Formation[] = [
  {
    id: 'f-basic',
    name: 'F-Básica',
    slots: [
      { pos: 'GK', x: 0.5, y: 0.96 },
      { pos: 'DF', x: 0.14, y: 0.76 },
      { pos: 'DF', x: 0.38, y: 0.8 },
      { pos: 'DF', x: 0.62, y: 0.8 },
      { pos: 'DF', x: 0.86, y: 0.76 },
      { pos: 'MF', x: 0.14, y: 0.55 },
      { pos: 'MF', x: 0.38, y: 0.6 },
      { pos: 'MF', x: 0.62, y: 0.6 },
      { pos: 'MF', x: 0.86, y: 0.55 },
      { pos: 'FW', x: 0.36, y: 0.36 },
      { pos: 'FW', x: 0.64, y: 0.36 },
    ],
  },
  {
    id: 'f-desert-lions',
    name: 'F-Leones',
    slots: [
      { pos: 'GK', x: 0.5, y: 0.96 },
      { pos: 'DF', x: 0.14, y: 0.74 },
      { pos: 'DF', x: 0.38, y: 0.79 },
      { pos: 'DF', x: 0.62, y: 0.79 },
      { pos: 'DF', x: 0.86, y: 0.74 },
      { pos: 'MF', x: 0.5, y: 0.6 },
      { pos: 'MF', x: 0.2, y: 0.5 },
      { pos: 'MF', x: 0.8, y: 0.5 },
      { pos: 'MF', x: 0.5, y: 0.45 },
      { pos: 'FW', x: 0.3, y: 0.33 },
      { pos: 'FW', x: 0.7, y: 0.33 },
    ],
  },
  {
    id: 'f-attack',
    name: 'F-Ataque (4-3-3)',
    slots: [
      { pos: 'GK', x: 0.5, y: 0.96 },
      { pos: 'DF', x: 0.14, y: 0.76 },
      { pos: 'DF', x: 0.38, y: 0.8 },
      { pos: 'DF', x: 0.62, y: 0.8 },
      { pos: 'DF', x: 0.86, y: 0.76 },
      { pos: 'MF', x: 0.25, y: 0.56 },
      { pos: 'MF', x: 0.5, y: 0.6 },
      { pos: 'MF', x: 0.75, y: 0.56 },
      { pos: 'FW', x: 0.18, y: 0.36 },
      { pos: 'FW', x: 0.5, y: 0.32 },
      { pos: 'FW', x: 0.82, y: 0.36 },
    ],
  },
  {
    id: 'f-defense',
    name: 'F-Defensa (5-3-2)',
    slots: [
      { pos: 'GK', x: 0.5, y: 0.96 },
      { pos: 'DF', x: 0.1, y: 0.72 },
      { pos: 'DF', x: 0.3, y: 0.8 },
      { pos: 'DF', x: 0.5, y: 0.82 },
      { pos: 'DF', x: 0.7, y: 0.8 },
      { pos: 'DF', x: 0.9, y: 0.72 },
      { pos: 'MF', x: 0.25, y: 0.58 },
      { pos: 'MF', x: 0.5, y: 0.6 },
      { pos: 'MF', x: 0.75, y: 0.58 },
      { pos: 'FW', x: 0.36, y: 0.38 },
      { pos: 'FW', x: 0.64, y: 0.38 },
    ],
  },
];

/** Las de la wiki (src/data/formations.json, generadas por tools/wiki/teams.py) y las hechas a mano. */
export const FORMATIONS: Formation[] = [
  ...HANDMADE,
  ...(generated as { id: string; name: string; layout: string }[])
    .filter((f) => !HANDMADE.some((h) => h.id === f.id))
    .map((f) => formationFromLayout(f.id, f.name, f.layout)),
];

export function getFormation(id: string): Formation {
  return FORMATIONS.find((f) => f.id === id) ?? FORMATIONS[0];
}
