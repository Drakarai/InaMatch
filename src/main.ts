import Phaser from 'phaser';
import { GAME_H, GAME_W, RES } from './config';
import { BootScene } from './scenes/BootScene';
import { FormationScene } from './scenes/FormationScene';
import { HudScene } from './scenes/HudScene';
import { MatchScene } from './scenes/MatchScene';
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

const game = new Phaser.Game({
  type: Phaser.AUTO,
  parent: 'game',
  width: Math.round(GAME_W * RES),
  height: Math.round(GAME_H * RES),
  backgroundColor: '#0d2547',
  scale: { mode: Phaser.Scale.FIT, autoCenter: Phaser.Scale.CENTER_BOTH },
  // el HUD va después del partido para dibujarse encima
  scene: [BootScene, MenuScene, FormationScene, MatchScene, HudScene],
});

// útil para depurar desde la consola del navegador
(window as unknown as { game: Phaser.Game }).game = game;
