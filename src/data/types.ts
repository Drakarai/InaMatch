// Tipos de datos del juego. Los equipos y supertécnicas viven en JSON
// (src/data/teams/*.json y src/data/moves.json) para poder añadir
// contenido sin tocar código.

export type Element = 'fire' | 'wind' | 'wood' | 'earth' | 'neutral';
export type Position = 'GK' | 'DF' | 'MF' | 'FW';
export type MoveKind = 'shoot' | 'dribble' | 'block' | 'catch';

export interface Stats {
  kick: number;
  body: number;
  control: number;
  guard: number;
  speed: number;
  stamina: number;
  guts: number;
}

export interface PlayerData {
  id: string;
  name: string; // nombre completo ("Mark Evans")
  short: string; // nombre corto que se muestra en el campo ("Mark")
  number: number;
  position: Position;
  element: Element;
  level: number;
  fp: number; // Fuerza física (FP)
  tp: number; // Puntos técnicos (TP)
  stats: Stats;
  moves: string[]; // ids de moves.json
  description?: string;
  /** Colores del sprite provisional (se ignoran si hay sprite en el pack). */
  look?: { hair?: string; skin?: string };
}

export interface TeamData {
  id: string;
  name: string;
  short: string;
  colors: {
    shirt: string;
    shorts: string;
    gkShirt: string;
    accent: string; // color del lado del marcador / paneles
  };
  formation: string; // id en formations.ts
  /** Los 11 primeros son titulares en el orden de los huecos de la formación. */
  players: PlayerData[];
}

export interface MoveData {
  id: string;
  name: string;
  kind: MoveKind;
  element: Element;
  power: number;
  tp: number;
  /** Título de la técnica en la wiki inglesa, para buscarla en data/tecnicas.json. */
  wiki?: string;
}

export interface FormationSlot {
  pos: Position;
  /** 0 = banda izquierda, 1 = banda derecha (visto atacando hacia arriba). */
  x: number;
  /** 0 = portería rival, 1 = portería propia. */
  y: number;
}

export interface Formation {
  id: string;
  name: string;
  slots: FormationSlot[]; // 11 huecos, el primero siempre el portero
}
