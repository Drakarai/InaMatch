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
  /** Equipo y id de donde sale el jugador (los de "Mi club"): su retrato y sus rasgos son los de allí. */
  origin?: string;
  originId?: string;
  /** Página del jugador en la wiki inglesa: identifica al personaje entre equipos. */
  wiki?: string;
  /** Capitán de su equipo (la tabla de miembros de la wiki, tools/wiki/restats.py). */
  captain?: boolean;
  /** Colores del sprite provisional (se ignoran si hay sprite en el pack). */
  look?: { hair?: string; skin?: string };
}

export interface TeamData {
  id: string;
  /** Temporada (juego) del que sale el equipo: ie1, ie2, ie3... */
  season?: string;
  name: string;
  short: string;
  colors: {
    shirt: string;
    shorts: string;
    gkShirt: string;
    accent: string; // color del lado del marcador / paneles
    /** Color de las mangas, si no son del color del pantalón (sprites dibujados). */
    sleeve?: string;
    /** Color de las medias (si no son blancas). */
    socks?: string;
    /** Color del pantalón del portero (si no es el del equipo). */
    gkShorts?: string;
    /** Color de las mangas del portero (si no son de un tono más oscuro que su camiseta). */
    gkSleeve?: string;
    /** Equipación de traje (sprites dibujados): manga larga, pantalón largo, camisa y corbata. */
    suit?: boolean;
    /** Los jugadores de campo llevan manga larga. */
    longSleeve?: boolean;
    /** Pantalón largo (bombachos) para los de campo y para el portero, y su color si no es el del pantalón. */
    longPants?: boolean;
    gkLongPants?: boolean;
    /** Medias del portero, si no son las del equipo. */
    gkSocks?: string;
    pants?: string;
    /** Rayas verticales y parte de abajo en dientes de sierra de otro color (sprites dibujados). */
    vstripes?: string;
    zig?: string;
    /** Equipos mixtos: equipación del equipo de origen de algunos jugadores (id del jugador → id del equipo). */
    kitFrom?: Record<string, string>;
    /** Alas a la espalda (Sky Team, Dark Angel). */
    wings?: string;
    /** El portero lleva manga larga. */
    gkLongSleeve?: boolean;
    /** Color de los guantes del portero (si no son blancos). */
    gkGloves?: string;
    /** Color del cuello, del dorsal y de la franja de las medias (si no son los de los detalles). */
    collar?: string;
    num?: string;
    stripe?: string;
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
  /** Tiro largo: el único tiro que se puede hacer desde lejos de la portería. */
  long?: boolean;
  /**
   * Sirve para cortar un tiro rival en vuelo: técnica defensiva de bloqueo de tiro (El muro, La montaña...) o tiro de
   * contra (Contra, Remate tarzán...). Sin una de estas, solo el portero puede parar un tiro.
   */
  shotBlock?: boolean;
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
  /** Distribución por puestos (defensas-medios-delanteros). */
  layout: string;
  /** Otros nombres de la wiki con la misma colocación (formaciones juntadas). */
  also?: string[];
  /** Genérica (solo por distribución, sin datos de la wiki): no sale como premio. */
  generic?: boolean;
}
