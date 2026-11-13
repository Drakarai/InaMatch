import Phaser from 'phaser';
import '@fontsource/barlow-semi-condensed/latin-500.css';
import '@fontsource/barlow-semi-condensed/latin-ext-500.css';
import '@fontsource/barlow-semi-condensed/latin-700.css';
import '@fontsource/barlow-semi-condensed/latin-ext-700.css';
import '@fontsource/barlow-semi-condensed/latin-500-italic.css';
import '@fontsource/barlow-semi-condensed/latin-ext-500-italic.css';
import '@fontsource/barlow-semi-condensed/latin-700-italic.css';
import '@fontsource/barlow-semi-condensed/latin-ext-700-italic.css';
import '@fontsource/bebas-neue/latin-400.css';
import '@fontsource/bebas-neue/latin-ext-400.css';
import { GAME_H, GAME_W, PORTRAIT, RES, RES_EVENT, computeRes, setRes } from './config';
import { BootScene } from './scenes/BootScene';
import { FormationScene } from './scenes/FormationScene';
import { HudScene } from './scenes/HudScene';
import { MatchScene } from './scenes/MatchScene';
import { ClubScene } from './scenes/ClubScene';
import { GachaScene } from './scenes/GachaScene';
import { MenuScene } from './scenes/MenuScene';
import { TitleScene } from './scenes/TitleScene';
import { StoryScene } from './scenes/StoryScene';

// los textos se rasterizan a la misma resolución que el lienzo (si no, se verían borrosos al ampliar)
const setStyle = Phaser.GameObjects.TextStyle.prototype.setStyle;
Phaser.GameObjects.TextStyle.prototype.setStyle = function (style, updateText, setDefaults) {
  if (!style?.resolution) this.resolution = RES;
  const out = setStyle.call(this, style, false, setDefaults);
  if (!style?.resolution) this.resolution = RES;
  if (updateText !== false) this.update(true);
  return out;
};

/** Recorre todos los objetos de una escena (también los que están dentro de contenedores). */
function walk(list: Phaser.GameObjects.GameObject[], fn: (o: Phaser.GameObjects.GameObject) => void): void {
  for (const o of list) {
    fn(o);
    const inner = (o as Phaser.GameObjects.Container).list;
    if (Array.isArray(inner)) walk(inner, fn);
  }
}

/**
 * Al cambiar el tamaño de la ventana (maximizar, otra pantalla, zoom del navegador) el lienzo se vuelve a crear
 * a la resolución nueva: si no, el navegador lo estiraría y se vería borroso. Los textos se vuelven a rasterizar.
 */
function watchResize(game: Phaser.Game): void {
  let timer = 0;
  const apply = () => {
    // al girar el móvil cambia el diseño entero (vertical u horizontal): se recarga la página con el otro
    if (window.innerHeight > window.innerWidth !== PORTRAIT) {
      window.location.reload();
      return;
    }
    const next = computeRes();
    if (Math.abs(next - RES) < 0.01) return;
    setRes(next);
    game.scale.resize(Math.round(GAME_W * next), Math.round(GAME_H * next));
    for (const scene of game.scene.getScenes(false)) {
      if (!scene.sys.settings.active && !scene.sys.settings.isBooted) continue;
      walk(scene.children.list, (o) => {
        if (o instanceof Phaser.GameObjects.Text) o.setResolution(next);
      });
      scene.events.emit(RES_EVENT, next);
    }
  };
  window.addEventListener('resize', () => {
    window.clearTimeout(timer);
    timer = window.setTimeout(apply, 150);
  });
}

// el juego no arranca hasta tener las letras (si tardan más de 4 s, arranca con las del sistema)
function startGame(): void {
  const game = new Phaser.Game({
    type: Phaser.AUTO,
    parent: 'game',
    width: Math.round(GAME_W * RES),
    height: Math.round(GAME_H * RES),
    backgroundColor: '#070d18',
    // roundPixels: cada imagen y texto cae en píxeles enteros del lienzo (sin medio píxel difuminado)
    render: { roundPixels: true, antialias: true },
    scale: { mode: Phaser.Scale.FIT, autoCenter: Phaser.Scale.CENTER_BOTH },
    // el HUD va después del partido para dibujarse encima
    scene: [BootScene, TitleScene, StoryScene, MenuScene, ClubScene, GachaScene, FormationScene, MatchScene, HudScene],
  });
  watchResize(game);

  // útil para depurar desde la consola del navegador
  (window as unknown as { game: Phaser.Game }).game = game;
}

Promise.race([
  Promise.all(['500 24px "Barlow Semi Condensed"', '700 24px "Barlow Semi Condensed"', 'italic 500 24px "Barlow Semi Condensed"', 'italic 700 24px "Barlow Semi Condensed"', '24px "Bebas Neue"'].map((f) => document.fonts.load(f, 'ÁÉÍÓÚÑáéíóúñ¡¿Aa'))),
  new Promise((r) => setTimeout(r, 4000)),
])
  .catch(() => undefined)
  .then(startGame);
