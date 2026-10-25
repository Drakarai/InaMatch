import type { Formation } from './types';

export const FORMATIONS: Formation[] = [
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

export function getFormation(id: string): Formation {
  return FORMATIONS.find((f) => f.id === id) ?? FORMATIONS[0];
}
