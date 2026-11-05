import type { TeamData } from "./types";

/** Temporadas del menú, como las ligas de un FIFA: cada juego de la saga con sus equipos. */
export interface Season {
  id: string;
  name: string;
  short: string;
  /** Logo del juego (src/assets/pack/series/<icon>.png), de la enciclopedia oficial. */
  icon?: string;
}

export const SEASONS: Season[] = [
  { id: "club", name: "Mi club", short: "Mi club" },
  { id: "ie1", name: "Inazuma Eleven", short: "IE1", icon: "ie1" },
  { id: "ie2", name: "Inazuma Eleven 2", short: "IE2", icon: "ie2" },
  { id: "ie3", name: "Inazuma Eleven 3", short: "IE3", icon: "ie3" },
  { id: "go", name: "Inazuma Eleven GO", short: "GO", icon: "go1" },
  {
    id: "cs",
    name: "Inazuma Eleven GO Chrono Stone",
    short: "Chrono",
    icon: "go2",
  },
  { id: "gx", name: "Inazuma Eleven GO Galaxy", short: "Galaxy", icon: "go3" },
  { id: "ares", name: "Inazuma Eleven Ares", short: "Ares", icon: "ars" },
  { id: "orion", name: "Inazuma Eleven Orión", short: "Orión", icon: "ori" },
  { id: "vr", name: "Inazuma Eleven Victory Road", short: "VR", icon: "vic" },
  { id: "otros", name: "Otros equipos", short: "+" },
];

export function seasonOf(team: TeamData): string {
  return team.season ?? "otros";
}

export function getSeason(id: string): Season {
  return SEASONS.find((s) => s.id === id) ?? SEASONS[SEASONS.length - 1];
}
