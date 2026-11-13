import Phaser from 'phaser';
import { GAME_H, GAME_W, PORTRAIT } from '../config';
import { downloadSave, pickSaveFile } from '../save';
import { DIFFICULTIES, DIFFICULTY_ORDER, getSettings, onSettingsChange, setSettings } from '../settings';
import { soundRows } from './soundPanel';
import { THEME, confirmDialog, sectionTitle, themePanel, toast } from './theme';
import { Button, text } from './widgets';

/**
 * Ajustes (pantalla de inicio): sonido, dificultad de la CPU y copia de seguridad de la partida (guardarla en un
 * archivo o cargar una). Devuelve el contenedor; destruirlo lo cierra.
 */
export function settingsPanel(scene: Phaser.Scene, onClose?: () => void): Phaser.GameObjects.Container {
  const W = PORTRAIT ? GAME_W - 32 : 420;
  const H = 470;
  const x = (GAME_W - W) / 2;
  const y = Math.max(20, (GAME_H - H) / 2);
  const root = scene.add.container(0, 0).setDepth(400);
  // fondo oscuro que cierra al tocar fuera
  const shade = scene.add.rectangle(0, 0, GAME_W, GAME_H, 0x000000, 0.55).setOrigin(0).setInteractive();
  root.add(shade);
  const c = scene.add.container(x, y);
  root.add(c);
  const close = () => {
    root.destroy();
    onClose?.();
  };
  shade.on('pointerup', close);
  const g = scene.add.graphics();
  themePanel(g, 0, 0, W, H, THEME.yellow, 0.98);
  c.add([g, scene.add.zone(0, 0, W, H).setOrigin(0).setInteractive()]);
  c.add(text(scene, 18, 26, 'AJUSTES', 24, THEME.yellowCss, { fontStyle: 'bold', strokeThickness: 0 }).setOrigin(0, 0.5));
  const x0 = text(scene, W - 18, 26, '✕', 20, '#ffffff').setOrigin(1, 0.5).setInteractive({ useHandCursor: true });
  x0.on('pointerdown', close);
  c.add(x0);

  // sonido
  c.add(sectionTitle(scene, 16, 64, 'Sonido'));
  const sound = scene.add.container(0, 0);
  c.add(sound);
  soundRows(scene, sound, 100);

  // dificultad
  c.add(sectionTitle(scene, 16, 184, 'Dificultad de la CPU'));
  const bw = (W - 32 - 16) / 3;
  const buttons = DIFFICULTY_ORDER.map((d, i) => {
    const b = new Button(scene, 16 + bw / 2 + i * (bw + 8), 222, DIFFICULTIES[d].label, () => setSettings({ difficulty: d }), { w: bw, h: 42, size: 17, variant: 'secondary' });
    c.add(b);
    return { d, b };
  });
  const hint = text(scene, W / 2, 260, '', 12, THEME.muted, { fontStyle: 'italic', strokeThickness: 0, align: 'center', wordWrap: { width: W - 32 } }).setOrigin(0.5, 0);
  c.add(hint);
  const redraw = () => {
    const cur = getSettings().difficulty;
    buttons.forEach(({ d, b }) => b.setSelected(d === cur));
    hint.setText(DIFFICULTIES[cur].hint);
  };
  redraw();
  const off = onSettingsChange(redraw);
  root.once(Phaser.GameObjects.Events.DESTROY, off);

  // partida
  c.add(sectionTitle(scene, 16, 312, 'Tu partida'));
  c.add(
    text(scene, 18, 336, 'Se guarda en este navegador. Haz una copia para no perderla o para llevarla a otro dispositivo.', 12, '#c9d6ec', {
      strokeThickness: 0,
      wordWrap: { width: W - 36 },
    }).setOrigin(0, 0),
  );
  const half = (W - 32 - 10) / 2;
  c.add(
    new Button(scene, 16 + half / 2, 404, 'Guardar copia', () => {
      if (downloadSave()) toast(scene, 'Copia descargada: guárdala bien', THEME.green, 2200);
      else toast(scene, 'No se ha podido crear la copia', THEME.coral, 2200);
    }, { w: half, h: 46, size: 16, variant: 'primary', icon: '⬇' }),
  );
  c.add(
    new Button(scene, W - 16 - half / 2, 404, 'Cargar copia', () => {
      confirmDialog(
        scene,
        {
          title: '¿Cargar una copia?',
          body: 'Se sustituirá la partida de este navegador (Mi club, historia, torneo y ajustes) por la del archivo.',
          ok: 'Elegir archivo',
          onOk: () =>
            pickSaveFile((res) => {
              if (!res.ok) {
                toast(scene, res.error, THEME.coral, 3000);
                return;
              }
              toast(scene, 'Partida cargada. Reiniciando…', THEME.green, 1500);
              scene.time.delayedCall(900, () => window.location.reload());
            }),
        },
        500,
      );
    }, { w: half, h: 46, size: 16, variant: 'secondary', icon: '⬆' }),
  );
  c.add(text(scene, W / 2, H - 20, 'Todo se guarda solo al momento', 11, THEME.muted, { fontStyle: 'italic', strokeThickness: 0 }).setOrigin(0.5));
  root.setAlpha(0);
  scene.tweens.add({ targets: root, alpha: 1, duration: 160 });
  return root;
}

/** Botón redondo con un engranaje que abre los ajustes. */
export function settingsButton(scene: Phaser.Scene, x: number, y: number): void {
  let panel: Phaser.GameObjects.Container | null = null;
  const g = scene.add.graphics().setDepth(199);
  const draw = (hover: boolean) => {
    g.clear().fillStyle(hover ? THEME.yellow : THEME.night, 0.92).fillCircle(x, y, 20).lineStyle(2, THEME.yellow).strokeCircle(x, y, 20);
  };
  const icon = text(scene, x, y + 1, '⚙', 22, '#ffffff').setOrigin(0.5).setDepth(199);
  draw(false);
  scene.add
    .zone(x - 20, y - 20, 40, 40)
    .setOrigin(0)
    .setDepth(199)
    .setInteractive({ useHandCursor: true })
    .on('pointerover', () => (draw(true), icon.setColor(THEME.ink)))
    .on('pointerout', () => (draw(false), icon.setColor('#ffffff')))
    .on('pointerdown', () => {
      if (panel?.active) return;
      panel = settingsPanel(scene, () => (panel = null));
    });
}
