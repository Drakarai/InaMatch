import Phaser from 'phaser';
import { COLORS, hex } from '../config';
import { getTeam, movesOf } from '../data';
import { ELEMENT_COLOR, ELEMENT_LABEL } from '../data/elements';
import { FORMATIONS, getFormation } from '../data/formations';
import type { PlayerData, Stats } from '../data/types';
import { portraitPack } from '../gfx/pack';
import { portraitKey, spriteKey, texKey } from '../gfx/placeholders';
import { lineupPlayers, swapInLineup, type Lineup } from '../engine/lineup';
import { fitCamera, POS_COLOR, pt, sectionTitle, slant, teamBackdrop, THEME, themePanel } from '../ui/theme';
import { Button, StatBar, text } from '../ui/widgets';

export const STAT_LABELS: [keyof Stats, string][] = [
  ['kick', 'Tiro'],
  ['body', 'Físico'],
  ['control', 'Control'],
  ['guard', 'Defensa'],
  ['speed', 'Rapidez'],
  ['stamina', 'Aguante'],
  ['guts', 'Valor'],
];

const MOVE_KIND_LABEL = { shoot: 'Tiro', dribble: 'Regate', block: 'Bloqueo', catch: 'Parada' } as const;

const PITCH_BOX = { x: 44, y: 112, w: 452, h: 552 };
const CARD = { x: 536, y: 104, w: 704, h: 330 };
const BENCH = { x: 536, y: 450, w: 704, h: 150 };

/** Formación en el descanso de un partido: estamina y técnica de cada jugador y vuelta al partido. */
export interface Halftime {
  bars: Map<string, { fp: number; tp: number }>;
  score: [number, number];
  onDone: (lineup: Lineup) => void;
}

interface Token {
  index: number; // posición en lineup.order
  container: Phaser.GameObjects.Container;
}

export class FormationScene extends Phaser.Scene {
  private home!: Lineup;
  private away!: Lineup;
  private selected: number | null = null;
  private halftime: Halftime | null = null;
  private tokens: Token[] = [];
  private info!: Phaser.GameObjects.Container;
  private formationLabel!: Phaser.GameObjects.Text;
  private previewId: string | null = null;
  private formationList: Phaser.GameObjects.Container | null = null;
  private hint!: Phaser.GameObjects.Text;

  constructor() {
    super('formation');
  }

  init(data: { home: Lineup; away: Lineup; halftime?: Halftime }): void {
    this.home = data.home;
    this.away = data.away;
    this.halftime = data.halftime ?? null;
    this.selected = null;
  }

  /** Estamina y técnica actuales del jugador (en el descanso); fuera del partido, llenas. */
  private bars(p: PlayerData): { fp: number; tp: number } {
    return this.halftime?.bars.get(p.id) ?? { fp: p.fp, tp: p.tp };
  }

  /** Retratos de Victory Road de los dos equipos (se cargan aquí, no al arrancar el juego). */
  preload(): void {
    for (const { key, url } of portraitPack([this.home.teamId, this.away.teamId])) {
      if (!this.textures.exists(key)) this.load.image(key, url);
    }
    this.load.on(Phaser.Loader.Events.FILE_COMPLETE, (key: string) => this.textures.get(key).setFilter(Phaser.Textures.FilterMode.LINEAR));
  }

  create(): void {
    fitCamera(this);
    const team = getTeam(this.home.teamId);
    const rival = getTeam(this.away.teamId);
    teamBackdrop(this, team, undefined, { x: 270, y: 380 });

    // cabecera: escudo, título y el rival
    this.add.image(60, 44, texKey.emblem(team.id)).setDisplaySize(58, 58);
    text(this, 100, 14, this.halftime ? 'Descanso' : 'Formación', 30, '#ffd23f', { fontStyle: 'italic bold', strokeThickness: 6 });
    if (this.halftime) {
      const [a, b] = this.halftime.score;
      text(this, 640, 40, `${team.short}  ${a} - ${b}  ${rival.short}`, 26, '#ffffff', { fontStyle: 'italic bold', strokeThickness: 6 }).setOrigin(0.5);
    }
    text(this, 102, 52, team.name, 16, '#ffffff', { fontStyle: 'italic' });
    const rx = 1240;
    this.add.image(rx - 26, 50, texKey.emblem(rival.id)).setDisplaySize(48, 48);
    text(this, rx - 60, 40, 'RIVAL', 12, THEME.awayCss, { fontStyle: 'italic bold' }).setOrigin(1, 0.5);
    text(this, rx - 60, 60, rival.name, 16, '#ffffff', { fontStyle: 'italic bold' }).setOrigin(1, 0.5);

    this.drawPitch();
    this.info = this.add.container(CARD.x, CARD.y);

    // banquillo
    const g = this.add.graphics();
    themePanel(g, BENCH.x, BENCH.y, BENCH.w, BENCH.h, hex(team.colors.accent));
    sectionTitle(this, BENCH.x + 16, BENCH.y + 20, 'Banquillo');
    this.hint = text(this, BENCH.x + BENCH.w - 16, BENCH.y + 20, '', 13, THEME.muted, { fontStyle: 'italic', strokeThickness: 0 }).setOrigin(1, 0.5);

    // barra de abajo: formación, volver y jugar
    const bar = this.add.graphics();
    bar.fillStyle(0x000000, 0.5).fillPoints(slant(536, 622, 400, 58, 16), true);
    bar.lineStyle(2, THEME.yellow, 0.8).strokePoints(slant(536, 622, 400, 58, 16), true);
    new Button(this, 578, 651, '◀', () => this.cycleFormation(-1), { w: 50, h: 42, color: THEME.panelLight });
    new Button(this, 892, 651, '▶', () => this.cycleFormation(1), { w: 50, h: 42, color: THEME.panelLight });
    text(this, 736, 636, 'FORMACIÓN  ▾ pulsa para ver todas', 11, THEME.muted, { fontStyle: 'bold', strokeThickness: 0 }).setOrigin(0.5);
    this.formationLabel = text(this, 736, 660, '', 20, '#ffffff', { fontStyle: 'italic bold' }).setOrigin(0.5);
    // pulsar el nombre abre la lista de todas las formaciones
    const labelHit = this.add.zone(612, 626, 248, 52).setOrigin(0).setInteractive({ useHandCursor: true });
    labelHit.on('pointerdown', () => this.toggleFormationList());
    labelHit.on('pointerover', () => this.formationLabel.setColor('#ffd23f'));
    labelHit.on('pointerout', () => this.formationLabel.setColor('#ffffff'));
    this.input.keyboard?.on('keydown-ESC', () => this.closeFormationList());
    if (!this.halftime) new Button(this, 1016, 651, 'Menú', () => this.scene.start('menu'), { w: 120, h: 46, size: 17, color: THEME.panelLight });
    new Button(this, 1160, 651, this.halftime ? '¡2ª parte!' : '¡A jugar!', () => this.play(), { w: 160, h: 58, size: 24, color: THEME.yellow });

    this.layoutTokens();
    this.showInfo(lineupPlayers(team, this.home)[0]);
  }

  /** Campo en verde oscuro con las líneas finas, dentro de un marco inclinado. */
  private drawPitch(): void {
    const { x, y, w, h } = PITCH_BOX;
    const g = this.add.graphics();
    g.fillStyle(0x000000, 0.45).fillRect(x + 6, y + 8, w, h);
    for (let i = 0; i < 10; i++) g.fillStyle(i % 2 ? 0x1f6b3a : 0x247a43).fillRect(x, y + (i * h) / 10, w, h / 10);
    // brillo diagonal
    g.fillStyle(0xffffff, 0.05).fillPoints([pt(x, y), pt(x + w * 0.55, y), pt(x, y + h * 0.5)], true);
    g.lineStyle(2, 0xffffff, 0.55).strokeRect(x + 10, y + 10, w - 20, h - 20);
    g.lineBetween(x + 10, y + 10, x + w - 10, y + 10);
    g.beginPath();
    g.arc(x + w / 2, y + 10, 64, 0, Math.PI);
    g.strokePath();
    g.strokeRect(x + w / 2 - 110, y + h - 100, 220, 90);
    g.strokeRect(x + w / 2 - 50, y + h - 44, 100, 34);
    g.lineStyle(3, THEME.yellow).strokeRect(x, y, w, h);
    g.fillStyle(THEME.yellow).fillPoints(slant(x - 2, y - 26, 150, 26, 10), true);
    text(this, x + 70, y - 13, 'TITULARES', 14, THEME.ink, { fontStyle: 'italic bold', strokeThickness: 0 }).setOrigin(0.5);
  }

  private slotY(sy: number): number {
    return PITCH_BOX.y + 30 + ((sy - 0.3) / 0.68) * (PITCH_BOX.h - 80);
  }

  /**
   * Coloca las chapas. Con `previewId` las pone como quedarían en esa formación (vista previa de la lista),
   * sin cambiarla; las chapas se deslizan desde donde estaban.
   */
  private layoutTokens(previewId?: string): void {
    const before = new Map(this.tokens.map((t) => [t.index, { x: t.container.x, y: t.container.y }]));
    for (const t of this.tokens) t.container.destroy();
    this.tokens = [];
    const team = getTeam(this.home.teamId);
    const formation = getFormation(previewId ?? this.home.formationId);
    this.previewId = previewId ?? null;
    this.formationLabel.setText(formation.name);
    const players = lineupPlayers(team, this.home);

    players.forEach((p, index) => {
      let x: number;
      let y: number;
      if (index < 11) {
        const slot = formation.slots[index];
        x = PITCH_BOX.x + 40 + slot.x * (PITCH_BOX.w - 80);
        y = this.slotY(slot.y);
      } else {
        const b = index - 11;
        x = BENCH.x + 60 + (b % 9) * 74;
        y = BENCH.y + 78 + Math.floor(b / 9) * 64;
      }
      const token = this.makeToken(p, index, x, y);
      const from = before.get(index);
      if (from && (from.x !== x || from.y !== y)) {
        token.setPosition(from.x, from.y);
        this.tweens.add({ targets: token, x, y, duration: 180, ease: 'Cubic.Out' });
      }
      this.tokens.push({ index, container: token });
    });
    this.hint.setText(this.selected === null ? 'Pulsa dos jugadores para cambiarlos' : 'Ahora pulsa con quién cambiarlo');
  }

  /** Chapa del jugador: sprite sobre un círculo, nombre en una banda y la demarcación en su color. */
  private makeToken(p: PlayerData, index: number, x: number, y: number): Phaser.GameObjects.Container {
    const c = this.add.container(x, y);
    const selected = this.selected === index;
    const slotPos = index < 11 ? getFormation(this.previewId ?? this.home.formationId).slots[index].pos : p.position;
    const outOfPosition = index < 11 && slotPos !== p.position;
    const g = this.add.graphics();
    g.fillStyle(0x000000, 0.35).fillEllipse(0, 20, 40, 12);
    if (selected) g.fillStyle(THEME.yellow, 0.35).fillCircle(0, 0, 28).lineStyle(3, THEME.yellow).strokeCircle(0, 0, 28);
    const sprite = this.add.image(0, -2, spriteKey(this, p, getTeam(this.home.teamId)));
    sprite.setScale(44 / sprite.height);
    const nameBand = this.add.graphics();
    const label = text(this, 0, 32, p.short, 12, '#ffffff', { fontStyle: 'italic bold', strokeThickness: 3 }).setOrigin(0.5);
    const bw = Math.max(54, label.width + 18);
    nameBand.fillStyle(0x000000, 0.6).fillPoints(slant(-bw / 2, 24, bw, 16, 5), true);
    const chip = this.add.graphics();
    chip.fillStyle(POS_COLOR[p.position]).fillPoints(slant(10, -32, 30, 14, 4), true);
    if (outOfPosition) chip.lineStyle(2, 0xff5a5a).strokePoints(slant(10, -32, 30, 14, 4), true);
    const pos = text(this, 25, -25, p.position, 10, '#ffffff', { fontStyle: 'bold', strokeThickness: 2 }).setOrigin(0.5);
    const elem = this.add.graphics().fillStyle(ELEMENT_COLOR[p.element]).fillCircle(-20, -24, 6).lineStyle(1.5, 0xffffff).strokeCircle(-20, -24, 6);
    c.add([g, sprite, nameBand, label, chip, pos, elem]);
    if (this.halftime) {
      // en el descanso, la estamina de cada uno debajo del nombre, para decidir los cambios
      const { fp } = this.bars(p);
      const ratio = Phaser.Math.Clamp(fp / p.fp, 0, 1);
      const bar = this.add.graphics();
      bar.fillStyle(0x000000, 0.7).fillRect(-22, 42, 44, 5);
      bar.fillStyle(ratio < 0.01 ? 0xe2463b : COLORS.fp).fillRect(-21, 43, 42 * ratio, 3);
      c.add(bar);
    }
    c.setSize(60, 76);
    c.setInteractive({ useHandCursor: true })
      .on('pointerover', () => this.showInfo(p))
      .on('pointerdown', () => this.pick(index));
    return c;
  }

  private pick(index: number): void {
    if (this.selected === null) {
      this.selected = index;
    } else if (this.selected === index) {
      this.selected = null;
    } else {
      this.home = swapInLineup(this.home, this.selected, index);
      this.selected = null;
    }
    this.layoutTokens();
  }

  private setFormation(id: string): void {
    this.home = { ...this.home, formationId: id };
    this.layoutTokens();
  }

  /** Lista de formaciones sobre la ficha: al pasar el ratón se ve en el campo, al pulsar se elige. */
  private toggleFormationList(): void {
    if (this.formationList) return this.closeFormationList();
    const X = CARD.x;
    const Y = CARD.y;
    const Wd = CARD.w;
    const Hd = BENCH.y + BENCH.h - CARD.y;
    const c = this.add.container(0, 0).setDepth(50);
    this.formationList = c;
    // fondo que cierra la lista al pulsar fuera
    const back = this.add.rectangle(640, 360, 1280, 720, 0x000000, 0.12).setInteractive();
    back.on('pointerdown', () => this.closeFormationList());
    const g = this.add.graphics();
    themePanel(g, X, Y, Wd, Hd, THEME.yellow, 1);
    const panelHit = this.add.zone(X, Y, Wd, Hd).setOrigin(0).setInteractive();
    c.add([back, g, panelHit]);
    c.add(sectionTitle(this, X + 18, Y + 22, 'Formaciones'));
    c.add(text(this, X + Wd - 18, Y + 22, 'Pasa el ratón para verla en el campo · pulsa para elegirla', 12, THEME.muted, { fontStyle: 'italic', strokeThickness: 0 }).setOrigin(1, 0.5));
    const cols = 3;
    const rows = Math.ceil(FORMATIONS.length / cols);
    const cw = (Wd - 36 - (cols - 1) * 8) / cols;
    const rh = Math.min(34, (Hd - 56) / rows);
    FORMATIONS.forEach((f, i) => {
      const cx = X + 18 + Math.floor(i / rows) * (cw + 8);
      const cy = Y + 44 + (i % rows) * rh;
      const current = f.id === this.home.formationId;
      const lines = ['DF', 'MF', 'FW'].map((pos) => f.slots.filter((s) => s.pos === pos).length).join('-');
      const bg = this.add.graphics();
      const draw = (hover: boolean) => {
        bg.clear();
        if (current || hover) bg.fillStyle(current ? THEME.yellow : THEME.panelLight, current ? 0.9 : 1).fillPoints(slant(cx, cy + 2, cw, rh - 4, 6), true);
      };
      draw(false);
      const name = text(this, cx + 14, cy + rh / 2, f.name, 14, current ? THEME.ink : '#ffffff', { fontStyle: 'italic bold', strokeThickness: current ? 0 : 3 }).setOrigin(0, 0.5);
      for (let size = 14; name.width > cw - 70 && size > 10; ) name.setFontSize(--size);
      const lay = text(this, cx + cw - 12, cy + rh / 2, lines, 12, current ? THEME.ink : '#9fb8d8', { fontStyle: 'bold', strokeThickness: 0 }).setOrigin(1, 0.5);
      const hit = this.add.zone(cx, cy, cw, rh).setOrigin(0).setInteractive({ useHandCursor: true });
      hit.on('pointerover', () => {
        draw(true);
        this.layoutTokens(f.id);
      });
      hit.on('pointerout', () => {
        draw(false);
        if (this.previewId === f.id) this.layoutTokens();
      });
      hit.on('pointerdown', () => {
        this.closeFormationList();
        this.setFormation(f.id);
      });
      c.add([bg, name, lay, hit]);
    });
  }

  private closeFormationList(): void {
    if (!this.formationList) return;
    this.formationList.destroy();
    this.formationList = null;
    if (this.previewId) this.layoutTokens();
  }

  private cycleFormation(d: number): void {
    const i = FORMATIONS.findIndex((f) => f.id === this.home.formationId);
    const next = FORMATIONS[(i + d + FORMATIONS.length) % FORMATIONS.length];
    this.home = { ...this.home, formationId: next.id };
    this.layoutTokens();
  }

  /** Ficha del jugador, como un cromo: retrato, dorsal enorme de fondo, atributos en barras y supertécnicas. */
  private showInfo(p: PlayerData): void {
    this.info.removeAll(true);
    const team = getTeam(this.home.teamId);
    const { w: W, h: H } = CARD;
    const accent = hex(team.colors.accent);
    const g = this.add.graphics();
    themePanel(g, 0, 0, W, H, accent);
    // dorsal gigante de fondo
    const number = text(this, W - 20, -18, String(p.number), 150, '#ffffff', { fontStyle: 'italic bold', strokeThickness: 0 }).setOrigin(1, 0).setAlpha(0.06);
    // retrato en un marco inclinado
    g.fillStyle(accent).fillPoints(slant(14, 16, 132, 132, 18), true);
    g.fillStyle(0x000000, 0.35).fillPoints(slant(20, 22, 120, 120, 16), true);
    const portrait = this.add.image(80, 82, portraitKey(this, p, team)).setDisplaySize(112, 112);
    // nombre y etiquetas
    const name = text(this, 166, 20, p.name, 26, '#ffffff', { fontStyle: 'italic bold', strokeThickness: 4 });
    for (let size = 26; name.width > 360 && size > 15; ) name.setFontSize(--size);
    const tags = this.add.graphics();
    tags.fillStyle(POS_COLOR[p.position]).fillPoints(slant(166, 58, 56, 22, 6), true);
    tags.fillStyle(ELEMENT_COLOR[p.element]).fillPoints(slant(228, 58, 96, 22, 6), true);
    tags.fillStyle(0x000000, 0.5).fillPoints(slant(330, 58, 72, 22, 6), true);
    const posT = text(this, 194, 69, p.position, 13, '#ffffff', { fontStyle: 'bold' }).setOrigin(0.5);
    const elT = text(this, 276, 69, ELEMENT_LABEL[p.element], 13, '#ffffff', { fontStyle: 'bold' }).setOrigin(0.5);
    const lvT = text(this, 366, 69, `Nv. ${p.level}`, 13, '#ffd23f', { fontStyle: 'bold' }).setOrigin(0.5);
    const fp = new StatBar(this, 166, 102, 'FP', COLORS.fp, 150);
    fp.set(this.bars(p).fp, p.fp);
    const tp = new StatBar(this, 166, 126, 'TP', COLORS.tp, 150);
    tp.set(this.bars(p).tp, p.tp);
    this.info.add([g, number, portrait, name, tags, posT, elT, lvT, fp, tp]);

    // atributos en barras
    const sx = 430;
    STAT_LABELS.forEach(([key, label], i) => {
      const y = 28 + i * 17;
      const v = p.stats[key];
      const bar = this.add.graphics();
      bar.fillStyle(0x000000, 0.45).fillPoints(slant(sx + 66, y - 5, 160, 10, 3), true);
      bar.fillStyle(v >= 75 ? THEME.yellow : 0x7fb2ff).fillPoints(slant(sx + 66, y - 5, Phaser.Math.Clamp(v / 99, 0.05, 1) * 160, 10, 3), true);
      this.info.add(bar);
      this.info.add(text(this, sx, y, label, 12, '#c9d3e0', { fontStyle: 'italic', strokeThickness: 0 }).setOrigin(0, 0.5));
      this.info.add(text(this, sx + 256, y, String(v), 13, '#ffffff', { fontStyle: 'bold', strokeThickness: 2 }).setOrigin(1, 0.5));
    });

    // supertécnicas
    this.info.add(sectionTitle(this, 16, 172, 'Supertécnicas'));
    const moves = movesOf(p.moves);
    if (moves.length === 0) this.info.add(text(this, 34, 198, '—', 15));
    moves.slice(0, 6).forEach((m, i) => {
      const y = 194 + i * 22;
      const row = this.add.graphics();
      row.fillStyle(0x000000, i % 2 ? 0.15 : 0.3).fillRect(16, y, 400, 20);
      row.fillStyle(ELEMENT_COLOR[m.element]).fillRect(16, y, 5, 20);
      this.info.add(row);
      this.info.add(text(this, 30, y + 10, m.name, 14, '#ffffff', { fontStyle: 'bold', strokeThickness: 2 }).setOrigin(0, 0.5));
      this.info.add(text(this, 410, y + 10, `${MOVE_KIND_LABEL[m.kind]}  ·  ${m.power}  ·  TP ${m.tp}`, 12, '#c9d3e0', { strokeThickness: 0 }).setOrigin(1, 0.5));
    });

    // descripción
    const dg = this.add.graphics();
    dg.fillStyle(0x000000, 0.3).fillRect(430, 160, W - 446, H - 176);
    dg.fillStyle(accent).fillRect(430, 160, 3, H - 176);
    this.info.add(dg);
    this.info.add(
      text(this, 444, 170, p.description ?? `Jugador de ${team.name}.`, 13, '#e3e9f2', {
        fontStyle: 'italic',
        strokeThickness: 0,
        wordWrap: { width: W - 474 },
        lineSpacing: 4,
      }),
    );
  }

  private play(): void {
    if (this.halftime) {
      const done = this.halftime.onDone;
      this.scene.stop();
      done(this.home);
      return;
    }
    this.scene.start('match', { home: this.home, away: this.away });
  }
}
