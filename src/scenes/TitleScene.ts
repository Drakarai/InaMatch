import Phaser from 'phaser';
import { music } from '../audio/music';
import { sfx } from '../audio/sfx';
import { DISPLAY, GAME_H, GAME_W, PORTRAIT } from '../config';
import type { TeamData } from '../data/types';
import { ensureSprites, VSPRITE_REF, vspriteKey } from '../gfx/pack';
import { soundButton } from '../ui/soundPanel';
import { THEME, boltLogo, fitCamera, glow, pt } from '../ui/theme';
import { label } from '../ui/widgets';

/** Protagonistas de cada etapa de la saga que salen al campo en la pantalla de inicio (sus sprites de partido). */
const HEROES: { team: string; id: string }[] = [
  { team: 'ares-inakuni-raimon', id: 'sonny-wright' },
  { team: 'go-shinsei-raimon', id: 'victor-blade' },
  { team: 'ie1-raimon', id: 'axel-blaze' },
  { team: 'ie1-raimon', id: 'mark-evans' },
  { team: 'vr-ouja-raimon', id: 'harper-evans' },
  { team: 'go-shinsei-raimon', id: 'arion-sherwind' },
  { team: 'ie1-raimon', id: 'jude-sharp' },
  { team: 'cs-team-raimon', id: 'fei-rune' },
];

const MODES = [
  { id: 'story', label: 'HISTORIA', sub: 'La ruta de cada equipo, partido a partido' },
  { id: 'menu', label: 'PARTIDO', sub: 'Elige dos equipos de toda la saga' },
  { id: 'club', label: 'MI CLUB', sub: 'Tu equipo, tus fichajes y tus uniformes' },
  { id: 'gacha', label: 'FICHAJES', sub: 'Consigue jugadores y cuadernos de técnicas' },
] as const;
type ModeId = (typeof MODES)[number]['id'];

/**
 * Pantalla de inicio: un estadio de noche con las gradas llenas de flashes, el césped en perspectiva con los protagonistas
 * de la saga, el logo dorado con un destello que lo recorre y, al pulsar, el menú de modos (flechas e Intro, o tocar).
 * El primer toque también sirve para que el navegador deje sonar la música.
 */
export class TitleScene extends Phaser.Scene {
  private started = false;
  private leaving = false;
  private sel = 0;
  private items: { box: Phaser.GameObjects.Container; draw: (on: boolean) => void }[] = [];
  private prompt?: Phaser.GameObjects.Container;
  private curtain!: Phaser.GameObjects.Rectangle;
  private bgLayer!: Phaser.GameObjects.Container;

  constructor() {
    super('title');
  }

  create(): void {
    fitCamera(this);
    this.started = false;
    this.leaving = false;
    this.items = [];
    this.sel = 0;
    music.play('menu');
    // lo que no se mueve (cielo, gradas con el público, torres de focos, césped) se dibuja una vez en una sola imagen:
    // como miles de formas sueltas se redibujaban en cada fotograma y la pantalla iba a trompicones
    this.bgLayer = this.make.container({ x: 0, y: 0 }, false);
    this.sky();
    this.stands();
    this.floodlights();
    this.pitch();
    this.bake();
    this.heroes();
    this.logo();
    this.footer();
    this.pressStart();
    soundButton(this, GAME_W - 30, 32, GAME_W - 350, 76);

    this.time.delayedCall(200, () => this.input.once('pointerup', () => this.start()));
    const kb = this.input.keyboard;
    kb?.on('keydown-ENTER', () => (this.started ? this.go(MODES[this.sel].id) : this.start()));
    kb?.on('keydown-SPACE', () => (this.started ? this.go(MODES[this.sel].id) : this.start()));
    kb?.on('keydown-UP', () => this.move(-1));
    kb?.on('keydown-DOWN', () => this.move(1));

    // telón negro para entrar y salir
    this.curtain = this.add.rectangle(0, 0, GAME_W, GAME_H, 0x000000, 1).setOrigin(0).setDepth(1000);
    this.tweens.add({ targets: this.curtain, alpha: 0, duration: 450 });
  }

  // ------------------------------------------------------------------ fondo

  /** Un gráfico del fondo fijo (va a la imagen de bake). */
  private bgGraphics(): Phaser.GameObjects.Graphics {
    const g = this.make.graphics({}, false);
    this.bgLayer.add(g);
    return g;
  }

  /** Pasa el fondo fijo a una imagen, a la resolución real de la pantalla (la cámara amplía el juego RES veces). */
  private bake(): void {
    const res = this.cameras.main.zoom || 1;
    const rt = this.add.renderTexture(0, 0, Math.ceil(GAME_W * res), Math.ceil(GAME_H * res)).setOrigin(0).setScale(1 / res).setDepth(-10);
    this.bgLayer.setScale(res);
    rt.draw(this.bgLayer, 0, 0);
    this.bgLayer.destroy(true);
  }

  private get horizon(): number {
    return PORTRAIT ? GAME_H * 0.6 : GAME_H * 0.56;
  }

  private sky(): void {
    const g = this.bgGraphics();
    g.fillGradientStyle(0x050b18, 0x050b18, 0x0d2244, 0x0d2244, 1).fillRect(0, 0, GAME_W, this.horizon);
    glow(g, GAME_W / 2, this.horizon - 40, GAME_W * 0.55, 0x2f7bff, 0.12);
    // halo dorado detrás del logo
    glow(g, GAME_W / 2, PORTRAIT ? 190 : 112, PORTRAIT ? 250 : 360, THEME.yellow, 0.1);
  }

  /** Gradas: bandas oscuras con siluetas de público y flashes de cámaras que se encienden al azar. */
  private stands(): void {
    const top = this.horizon - (PORTRAIT ? 230 : 190);
    const g = this.bgGraphics();
    for (let i = 0; i < 4; i++) {
      const y = top + i * ((this.horizon - top) / 4);
      g.fillStyle(i % 2 ? 0x0a1426 : 0x0c1830, 1).fillRect(0, y, GAME_W, (this.horizon - top) / 4 + 1);
    }
    // cabezas del público
    const rnd = new Phaser.Math.RandomDataGenerator(['inamatch']);
    for (let y = top + 8; y < this.horizon - 6; y += 9) {
      for (let x = rnd.between(0, 8); x < GAME_W; x += rnd.between(8, 13)) {
        g.fillStyle(rnd.pick([0x13233f, 0x172b4b, 0x1b2f52, 0x0f1c34]), 1).fillCircle(x, y, rnd.between(3, 4));
      }
    }
    // borde superior del graderío y valla publicitaria
    g.fillStyle(0x03070f, 1).fillRect(0, top - 6, GAME_W, 6);
    const ad = this.horizon - 16;
    g.fillGradientStyle(0x1a3a7a, 0x7a1a3a, 0x1a3a7a, 0x7a1a3a, 1).fillRect(0, ad, GAME_W, 16);
    g.lineStyle(2, 0xffd23f, 0.8).lineBetween(0, ad, GAME_W, ad);
    for (let x = 30; x < GAME_W; x += 220) this.bgLayer.add(label(this, x, ad + 8, 'INAMATCH  ⚡  INAZUMA ELEVEN', 10, '#ffffff', { fontStyle: 'bold' }).setOrigin(0, 0.5).setAlpha(0.6));
    // flashes
    for (let i = 0; i < (PORTRAIT ? 18 : 30); i++) {
      const f = this.add.circle(0, 0, 2.5, 0xffffff, 0).setBlendMode(Phaser.BlendModes.ADD);
      const flash = () => {
        f.setPosition(Phaser.Math.Between(0, GAME_W), Phaser.Math.Between(top + 6, ad - 6)).setAlpha(0.95).setScale(1);
        this.tweens.add({ targets: f, alpha: 0, scale: 2.2, duration: 260, delay: Phaser.Math.Between(300, 4200), onComplete: flash });
      };
      flash();
    }
  }

  /** Dos torres de focos con su halo y haces de luz que barren despacio. */
  private floodlights(): void {
    const towers = PORTRAIT ? [60, GAME_W - 60] : [130, GAME_W - 130];
    const y = this.horizon - (PORTRAIT ? 250 : 215);
    towers.forEach((x, i) => {
      const g = this.bgGraphics();
      glow(g, x, y, 160, 0xfff4cf, 0.22);
      g.fillStyle(0x0a1020, 1).fillRect(x - 36, y - 16, 72, 26);
      for (let k = 0; k < 4; k++) g.fillStyle(0xfffbe8, 1).fillCircle(x - 27 + k * 18, y - 3, 6);
      const beam = this.add.graphics({ x, y }).setBlendMode(Phaser.BlendModes.ADD);
      const len = GAME_H;
      beam.fillStyle(0xfff4cf, 0.05).fillPoints([pt(-14, 0), pt(14, 0), pt(170, len), pt(-170, len)], true);
      beam.setRotation(i ? 0.35 : -0.35);
      this.tweens.add({ targets: beam, rotation: i ? 0.12 : -0.12, duration: 5200, yoyo: true, repeat: -1, ease: 'Sine.InOut', delay: i * 900 });
    });
  }

  /** Césped en perspectiva, con franjas y las líneas del centro del campo. */
  private pitch(): void {
    const g = this.bgGraphics();
    const top = this.horizon;
    const bottom = GAME_H;
    const cx = GAME_W / 2;
    const wTop = GAME_W * 0.9;
    const wBot = GAME_W * 2.2;
    const at = (t: number) => ({ y: top + (bottom - top) * t, w: wTop + (wBot - wTop) * t });
    // franjas: más anchas cuanto más cerca (perspectiva)
    const n = 9;
    for (let i = 0; i < n; i++) {
      const t0 = Math.pow(i / n, 1.6);
      const t1 = Math.pow((i + 1) / n, 1.6);
      const a = at(t0);
      const b = at(t1);
      g.fillStyle(i % 2 ? 0x2f8a3f : 0x2a7c39, 1).fillPoints([pt(cx - a.w / 2, a.y), pt(cx + a.w / 2, a.y), pt(cx + b.w / 2, b.y), pt(cx - b.w / 2, b.y)], true);
    }
    // línea de medio campo y círculo central
    const mid = at(0.42);
    g.lineStyle(3, 0xffffff, 0.75).lineBetween(cx - mid.w / 2, mid.y, cx + mid.w / 2, mid.y);
    g.strokeEllipse(cx, mid.y, GAME_W * (PORTRAIT ? 0.62 : 0.34), (bottom - top) * 0.34);
    g.fillStyle(0xffffff, 0.8).fillEllipse(cx, mid.y, 10, 4);
    // luz de los focos sobre el césped y oscuridad en los bordes
    glow(g, cx, top + (bottom - top) * 0.45, GAME_W * 0.5, 0xfff4cf, 0.08);
    g.fillGradientStyle(0x000000, 0x000000, 0x000000, 0x000000, 0.45, 0.45, 0, 0).fillRect(0, top, GAME_W, 40);
    g.fillGradientStyle(0x000000, 0x000000, 0x000000, 0x000000, 0, 0, 0.6, 0.6).fillRect(0, GAME_H - 140, GAME_W, 140);
  }

  /** Los protagonistas, en fila sobre el césped (sprites de partido a escala, con su sombra), entran desde abajo. */
  private heroes(): void {
    const list = PORTRAIT ? HEROES.slice(1, 7) : HEROES;
    const teams = new Map<string, TeamData>();
    for (const h of list) {
      const t = teams.get(h.team) ?? ({ id: h.team, players: [] } as unknown as TeamData);
      t.players.push({ id: h.id } as TeamData['players'][number]);
      teams.set(h.team, t);
    }
    const feet = this.horizon + (GAME_H - this.horizon) * (PORTRAIT ? 0.62 : 0.74);
    const span = PORTRAIT ? GAME_W - 40 : GAME_W - 160;
    const scale = (PORTRAIT ? 118 : 132) / VSPRITE_REF;
    ensureSprites(this.textures, [...teams.values()])
      .catch(() => {})
      .then(() => {
        if (!this.scene.isActive()) return;
        list.forEach((h, i) => {
          const key = vspriteKey(h.team, h.id, 'front');
          if (!this.textures.exists(key)) return;
          const x = GAME_W / 2 + (i - (list.length - 1) / 2) * (span / list.length);
          // los del centro, un poco más adelante
          const depth = 1 - Math.abs(i - (list.length - 1) / 2) / list.length;
          const y = feet + depth * (PORTRAIT ? 26 : 14);
          const s = scale * (0.86 + depth * 0.2);
          this.add.ellipse(x, y, 70 * s, 16 * s, 0x000000, 0.35);
          const img = this.add.image(x, y + 40, key).setOrigin(0.5, 1).setScale(s).setAlpha(0);
          this.tweens.add({ targets: img, y, alpha: 1, duration: 520, ease: 'Back.Out', delay: 300 + Math.abs(i - (list.length - 1) / 2) * 110 });
          this.tweens.add({ targets: img, scaleY: s * 1.025, duration: 900 + i * 60, yoyo: true, repeat: -1, ease: 'Sine.InOut', delay: 1000 });
        });
      });
  }

  // ------------------------------------------------------------------- logo

  private logo(): void {
    const y = PORTRAIT ? 190 : 112;
    const size = PORTRAIT ? 96 : 132;
    const c = this.add.container(GAME_W / 2, y).setDepth(20);
    const style = { fontFamily: DISPLAY, fontSize: `${size}px`, color: '#ffd23f' };
    // sombra profunda, contorno oscuro y relleno dorado en degradado
    const shadow = this.add.text(5, 9, 'INAMATCH', { ...style, color: '#000000' }).setOrigin(0.5).setAlpha(0.55).setLetterSpacing(4);
    const outline = this.add.text(0, 0, 'INAMATCH', { ...style, color: '#0b1a2e', stroke: '#0b1a2e', strokeThickness: Math.round(size / 6) }).setOrigin(0.5).setLetterSpacing(4);
    const title = this.add.text(0, 0, 'INAMATCH', { ...style, stroke: '#ffffff', strokeThickness: Math.round(size / 26) }).setOrigin(0.5).setLetterSpacing(4);
    const grad = title.context.createLinearGradient(0, 0, 0, title.height);
    grad.addColorStop(0, '#fff6c4');
    grad.addColorStop(0.45, '#ffd23f');
    grad.addColorStop(0.55, '#f0a81a');
    grad.addColorStop(1, '#c9780c');
    title.setFill(grad);
    c.add([shadow, outline, title]);
    // destellos que saltan en las letras de vez en cuando (sin máscaras: son caras de dibujar en cada fotograma)
    const star = this.add.graphics().setBlendMode(Phaser.BlendModes.ADD);
    const r = size * 0.22;
    star.fillStyle(0xffffff, 1).fillPoints([pt(0, -r), pt(r * 0.16, -r * 0.16), pt(r, 0), pt(r * 0.16, r * 0.16), pt(0, r), pt(-r * 0.16, r * 0.16), pt(-r, 0), pt(-r * 0.16, -r * 0.16)], true);
    star.setScale(0).setAlpha(0.9);
    c.add(star);
    const spots = [
      [title.width * 0.42, -size * 0.3],
      [-title.width * 0.2, -size * 0.32],
      [title.width * 0.12, size * 0.28],
    ];
    let k = 0;
    const twinkle = () => {
      const [sx, sy] = spots[k++ % spots.length];
      star.setPosition(sx, sy).setScale(0).setAngle(0);
      this.tweens.add({ targets: star, scale: 1, angle: 90, duration: 260, yoyo: true, ease: 'Sine.Out', onComplete: () => this.time.delayedCall(1600, twinkle) });
    };
    this.time.delayedCall(1300, twinkle);
    // el rayo, a la izquierda
    const bolt = this.add.graphics();
    const bs = size / 44;
    boltLogo(bolt, -title.width / 2 - 30 * bs, -24 * bs, bs);
    c.add(bolt);
    c.setScale(1.6).setAlpha(0);
    this.tweens.add({ targets: c, scale: 1, alpha: 1, duration: 650, ease: 'Cubic.Out', delay: 150 });
  }

  private footer(): void {
    label(this, GAME_W / 2, GAME_H - 16, 'Juego de fans sin ánimo de lucro · Inazuma Eleven es una marca de LEVEL-5', PORTRAIT ? 11 : 12, '#ffffff', { align: 'center' })
      .setOrigin(0.5, 1)
      .setAlpha(0.45)
      .setDepth(20);
  }

  // ------------------------------------------------------------------- menú

  private get menuY(): number {
    return PORTRAIT ? 400 : 258;
  }

  private pressStart(): void {
    const c = this.add.container(GAME_W / 2, this.menuY + (PORTRAIT ? 70 : 60)).setDepth(30);
    const w = PORTRAIT ? 380 : 420;
    const g = this.add.graphics();
    g.fillStyle(0x000000, 0.45).fillRoundedRect(-w / 2, -26, w, 52, 26);
    g.lineStyle(2, THEME.yellow, 0.8).strokeRoundedRect(-w / 2, -26, w, 52, 26);
    const t = label(this, 0, 0, PORTRAIT ? 'TOCA PARA EMPEZAR' : 'PULSA PARA EMPEZAR', PORTRAIT ? 20 : 22, '#ffffff', { fontStyle: 'bold' }).setOrigin(0.5).setLetterSpacing(4);
    c.add([g, t]);
    this.prompt = c;
    c.setAlpha(0);
    this.tweens.add({ targets: c, alpha: 1, duration: 400, delay: 900, onComplete: () => this.tweens.add({ targets: t, alpha: 0.35, duration: 750, yoyo: true, repeat: -1, ease: 'Sine.InOut' }) });
  }

  /** Cambia el "pulsa para empezar" por el menú de modos. */
  private start(): void {
    if (this.started || this.leaving) return;
    this.started = true;
    sfx.whistle();
    music.play('menu');
    const p = this.prompt;
    if (p) this.tweens.add({ targets: p, alpha: 0, scale: 0.9, duration: 180, onComplete: () => p.destroy() });
    const w = PORTRAIT ? 440 : 460;
    const h = PORTRAIT ? 78 : 66;
    const gap = PORTRAIT ? 14 : 10;
    MODES.forEach((m, i) => {
      const y = this.menuY + i * (h + gap);
      const box = this.add.container(GAME_W / 2, y).setDepth(30);
      const g = this.add.graphics();
      const title = label(this, -w / 2 + 34, -9, m.label, PORTRAIT ? 26 : 24, '#ffffff', { fontFamily: DISPLAY }).setOrigin(0, 0.5).setLetterSpacing(3);
      const sub = label(this, -w / 2 + 36, 17, m.sub, PORTRAIT ? 13 : 12, '#c9d6ec', { fontStyle: 'italic' }).setOrigin(0, 0.5);
      const arrow = label(this, w / 2 - 30, 0, '▶', 20, '#0b1a2e').setOrigin(0.5);
      box.add([g, title, sub, arrow]);
      const draw = (on: boolean) => {
        g.clear();
        const sk = 14;
        if (on) {
          g.fillStyle(0x000000, 0.35).fillPoints([pt(-w / 2 + sk + 4, -h / 2 + 5), pt(w / 2 + 4, -h / 2 + 5), pt(w / 2 - sk + 4, h / 2 + 5), pt(-w / 2 + 4, h / 2 + 5)], true);
          g.fillGradientStyle(0xffe27a, 0xffd23f, 0xf0a81a, 0xe89b12, 1).fillPoints([pt(-w / 2 + sk, -h / 2), pt(w / 2, -h / 2), pt(w / 2 - sk, h / 2), pt(-w / 2, h / 2)], true);
          g.lineStyle(2, 0xffffff, 0.9).strokePoints([pt(-w / 2 + sk, -h / 2), pt(w / 2, -h / 2), pt(w / 2 - sk, h / 2), pt(-w / 2, h / 2)], true);
        } else {
          g.fillStyle(0x0b1a2e, 0.78).fillPoints([pt(-w / 2 + sk, -h / 2), pt(w / 2, -h / 2), pt(w / 2 - sk, h / 2), pt(-w / 2, h / 2)], true);
          g.lineStyle(2, 0xffffff, 0.22).strokePoints([pt(-w / 2 + sk, -h / 2), pt(w / 2, -h / 2), pt(w / 2 - sk, h / 2), pt(-w / 2, h / 2)], true);
          g.fillStyle(THEME.yellow, 1).fillRect(-w / 2 + 8, -h / 2 + 12, 4, h - 24);
        }
        title.setColor(on ? '#0b1a2e' : '#ffffff');
        sub.setColor(on ? '#3a2a00' : '#c9d6ec');
        arrow.setVisible(on);
      };
      draw(i === this.sel);
      const hit = this.add.zone(0, 0, w, h).setInteractive({ useHandCursor: true });
      hit.on('pointerover', () => this.select(i));
      hit.on('pointerup', () => this.go(m.id));
      box.add(hit);
      this.items.push({ box, draw });
      box.setAlpha(0).setX(GAME_W / 2 + (i % 2 ? 60 : -60));
      this.tweens.add({ targets: box, alpha: 1, x: GAME_W / 2, duration: 320, ease: 'Cubic.Out', delay: 60 + i * 80 });
    });
  }

  private select(i: number): void {
    if (i === this.sel) return;
    this.sel = i;
    this.items.forEach((it, k) => it.draw(k === i));
    sfx.click();
  }

  private move(d: number): void {
    if (!this.started) return;
    this.select((this.sel + d + MODES.length) % MODES.length);
  }

  private go(scene: ModeId): void {
    if (this.leaving || !this.started) return;
    this.leaving = true;
    this.tweens.add({
      targets: this.curtain,
      alpha: 1,
      duration: 260,
      onComplete: () => this.scene.start(scene, scene === 'gacha' ? { from: 'title' } : undefined),
    });
  }
}
