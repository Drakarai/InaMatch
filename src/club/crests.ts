import Phaser from 'phaser';
import crestList from '../data/crests.json';
import { texKey } from '../gfx/placeholders';

/**
 * Escudos para "Mi club": todos los de Victory Road de la wiki (Category:Victory Road emblem images), a 192 px.
 * Se empieza con tres al azar y se gana uno nuevo por cada victoria. Las imágenes se cargan cuando hacen falta.
 */

export interface Crest {
  id: string;
  name: string;
  wiki: string;
}

export const CRESTS: Crest[] = crestList as Crest[];
const byId = new Map(CRESTS.map((c) => [c.id, c]));

const files = import.meta.glob<string>('../assets/crests/*.webp', { eager: true, query: '?url', import: 'default' });
const urlOf = (id: string): string | undefined => files[`../assets/crests/${id}.webp`];

export const crestById = (id: string): Crest | undefined => byId.get(id);
export const crestKey = (id: string): string => `crest:${id}`;

/** Carga los escudos que falten y llama a done cuando estén (también si ya estaban). */
export function loadCrests(scene: Phaser.Scene, ids: string[], done: () => void): void {
  const missing = ids.filter((id) => urlOf(id) && !scene.textures.exists(crestKey(id)));
  if (!missing.length) {
    done();
    return;
  }
  for (const id of missing) scene.load.image(crestKey(id), urlOf(id)!);
  scene.load.once(Phaser.Loader.Events.COMPLETE, () => {
    for (const id of missing) if (scene.textures.exists(crestKey(id))) scene.textures.get(crestKey(id)).setFilter(Phaser.Textures.FilterMode.LINEAR);
    done();
  });
  scene.load.start();
}

/** Pone un escudo como el de "Mi club" (la textura emblem:club que usan el menú, el partido y el marcador). */
export function applyClubCrest(scene: Phaser.Scene, id: string | undefined, done: () => void = () => {}): void {
  if (!id || !urlOf(id)) {
    done();
    return;
  }
  loadCrests(scene, [id], () => {
    const key = texKey.emblem('club');
    const src = scene.textures.exists(crestKey(id)) ? scene.textures.get(crestKey(id)).getSourceImage() : null;
    if (src) {
      if (scene.textures.exists(key)) scene.textures.remove(key);
      scene.textures.addImage(key, src as HTMLImageElement);
      scene.textures.get(key).setFilter(Phaser.Textures.FilterMode.LINEAR);
    }
    done();
  });
}
