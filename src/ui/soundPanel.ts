import Phaser from 'phaser';
import { audio, type AudioSettings } from '../audio/engine';
import { THEME, sectionTitle, slant, themePanel } from './theme';
import { text } from './widgets';

/**
 * Panel de sonido: activar o quitar la música y los efectos, y el volumen de cada uno.
 * Se usa en el menú principal y en la pausa. Devuelve el contenedor (destruirlo lo cierra).
 */
export function soundPanel(scene: Phaser.Scene, x: number, y: number, onClose?: () => void): Phaser.GameObjects.Container {
  const W = 320;
  const H = 190;
  const c = scene.add.container(x, y).setDepth(200);
  const g = scene.add.graphics();
  themePanel(g, 0, 0, W, H, THEME.yellow, 0.98);
  // que los clics no atraviesen el panel
  const block = scene.add.zone(0, 0, W, H).setOrigin(0).setInteractive();
  c.add([g, block, sectionTitle(scene, 16, 22, 'Sonido')]);
  const close = text(scene, W - 16, 22, '✕', 18, '#ffffff').setOrigin(1, 0.5).setInteractive({ useHandCursor: true });
  close.on('pointerdown', () => {
    c.destroy();
    onClose?.();
  });
  c.add(close);

  const row = (label: string, y0: number, on: keyof AudioSettings, vol: keyof AudioSettings) => {
    c.add(text(scene, 18, y0, label, 15, '#ffffff', { fontStyle: 'italic bold' }).setOrigin(0, 0.5));
    // interruptor
    const sw = scene.add.graphics();
    const swLabel = text(scene, 136, y0, '', 12, THEME.ink, { fontStyle: 'bold', strokeThickness: 0 }).setOrigin(0.5);
    const drawSw = () => {
      const enabled = audio.settings[on] as boolean;
      sw.clear().fillStyle(enabled ? THEME.yellow : 0x3a4658).fillPoints(slant(108, y0 - 12, 58, 24, 7), true);
      swLabel.setText(enabled ? 'SÍ' : 'NO').setColor(enabled ? THEME.ink : '#c9d3e0');
    };
    const swHit = scene.add.zone(108, y0 - 12, 58, 24).setOrigin(0).setInteractive({ useHandCursor: true });
    swHit.on('pointerdown', () => audio.set({ [on]: !audio.settings[on] }));
    // volumen
    const bx = 182;
    const bw = 118;
    const bar = scene.add.graphics();
    const drawBar = () => {
      const v = audio.settings[vol] as number;
      const enabled = audio.settings[on] as boolean;
      bar.clear().fillStyle(0x000000, 0.6).fillRect(bx, y0 - 4, bw, 8);
      bar.fillStyle(enabled ? 0x7fb2ff : 0x55606f).fillRect(bx, y0 - 4, bw * v, 8);
      bar.fillStyle(0xffffff).fillCircle(bx + bw * v, y0, 8);
    };
    const barHit = scene.add.zone(bx - 8, y0 - 14, bw + 16, 28).setOrigin(0).setInteractive({ useHandCursor: true, draggable: true });
    const setFrom = (p: Phaser.Input.Pointer) => {
      const local = c.getLocalPoint(p.worldX, p.worldY);
      audio.set({ [vol]: Phaser.Math.Clamp((local.x - bx) / bw, 0, 1), [on]: true });
    };
    barHit.on('pointerdown', setFrom);
    barHit.on('drag', (p: Phaser.Input.Pointer) => setFrom(p));
    c.add([sw, swLabel, swHit, bar, barHit]);
    return () => {
      drawSw();
      drawBar();
    };
  };
  const redraws = [row('Música', 74, 'music', 'musicVolume'), row('Efectos', 126, 'sfx', 'sfxVolume')];
  c.add(text(scene, W / 2, H - 22, 'Se guarda para la próxima vez', 11, THEME.muted, { fontStyle: 'italic', strokeThickness: 0 }).setOrigin(0.5));
  const redraw = () => redraws.forEach((r) => r());
  redraw();
  const off = audio.onChange(redraw);
  c.once(Phaser.GameObjects.Events.DESTROY, off);
  return c;
}

/** Botón redondo con una nota musical que abre y cierra el panel de sonido. */
export function soundButton(scene: Phaser.Scene, x: number, y: number, panelX: number, panelY: number): void {
  let panel: Phaser.GameObjects.Container | null = null;
  const g = scene.add.graphics().setDepth(199);
  const draw = (hover: boolean) => {
    const off = !audio.settings.music && !audio.settings.sfx;
    g.clear().fillStyle(hover ? THEME.yellow : THEME.night, 0.92).fillCircle(x, y, 20).lineStyle(2, THEME.yellow).strokeCircle(x, y, 20);
    if (off) g.lineStyle(3, 0xff5a5a).lineBetween(x - 12, y + 12, x + 12, y - 12);
  };
  const icon = text(scene, x, y, '♪', 20, '#ffffff').setOrigin(0.5).setDepth(199);
  draw(false);
  const off = audio.onChange(() => draw(false));
  scene.events.once(Phaser.Scenes.Events.SHUTDOWN, off);
  scene.add
    .zone(x - 20, y - 20, 40, 40)
    .setOrigin(0)
    .setDepth(199)
    .setInteractive({ useHandCursor: true })
    .on('pointerover', () => (draw(true), icon.setColor(THEME.ink)))
    .on('pointerout', () => (draw(false), icon.setColor('#ffffff')))
    .on('pointerdown', () => {
      if (panel?.active) {
        panel.destroy();
        panel = null;
      } else panel = soundPanel(scene, panelX, panelY, () => (panel = null));
    });
}
