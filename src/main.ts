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
import { GAME_H, GAME_W, RES } from './config';
import { BootScene } from './scenes/BootScene';
import { FormationScene } from './scenes/FormationScene';
import { HudScene } from './scenes/HudScene';
import { MatchScene } from './scenes/MatchScene';
import { ClubScene } from './scenes/ClubScene';
import { GachaScene } from './scenes/GachaScene';
import { MenuScene } from './scenes/MenuScene';

// los textos se rasterizan a la misma resolución que el lienzo (si no, se verían borrosos al ampliar)
const setStyle = Phaser.GameObjects.TextStyle.prototype.setStyle;
Phaser.GameObjects.TextStyle.prototype.setStyle = function (style, updateText, setDefaults) {
  if (!style?.resolution) this.resolution = RES;
  const out = setStyle.call(this, style, false, setDefaults);
  if (!style?.resolution) this.resolution = RES;
  if (updateText !== false) this.update(true);
  return out;
};

// el juego no arranca hasta tener las letras (si tardan más de 4 s, arranca con las del sistema)
function startGame(): void {
  const game = new Phaser.Game({
  type: Phaser.AUTO,
  parent: 'game',
  width: Math.round(GAME_W * RES),
  height: Math.round(GAME_H * RES),
  backgroundColor: '#0d2547',
  scale: { mode: Phaser.Scale.FIT, autoCenter: Phaser.Scale.CENTER_BOTH },
  // el HUD va después del partido para dibujarse encima
  scene: [BootScene, MenuScene, ClubScene, GachaScene, FormationScene, MatchScene, HudScene],
});

  // útil para depurar desde la consola del navegador
  (window as unknown as { game: Phaser.Game }).game = game;
}

Promise.race([
  Promise.all(['500 24px "Barlow Semi Condensed"', '700 24px "Barlow Semi Condensed"', 'italic 500 24px "Barlow Semi Condensed"', 'italic 700 24px "Barlow Semi Condensed"', '24px "Bebas Neue"'].map((f) => document.fonts.load(f, 'ÁÉÍÓÚÑáéíóúñ¡¿Aa'))),
  new Promise((r) => setTimeout(r, 4000)),
])
  .catch(() => undefined)
  .then(startGame);
