import Phaser from 'phaser';
import { GAME_H, GAME_W } from './config';
import { BootScene } from './scenes/BootScene';
import { FormationScene } from './scenes/FormationScene';
import { HudScene } from './scenes/HudScene';
import { MatchScene } from './scenes/MatchScene';
import { MenuScene } from './scenes/MenuScene';

const game = new Phaser.Game({
  type: Phaser.AUTO,
  parent: 'game',
  width: GAME_W,
  height: GAME_H,
  backgroundColor: '#0d2547',
  scale: { mode: Phaser.Scale.FIT, autoCenter: Phaser.Scale.CENTER_BOTH },
  // el HUD va después del partido para dibujarse encima
  scene: [BootScene, MenuScene, FormationScene, MatchScene, HudScene],
});

// útil para depurar desde la consola del navegador
(window as unknown as { game: Phaser.Game }).game = game;
