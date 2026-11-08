import Phaser from 'phaser';
import { music } from '../audio/music';
import { COLORS, GAME_H, GAME_W, PORTRAIT, hex } from '../config';
import { getTeam, movesOf } from '../data';
import { ELEMENT_COLOR, ELEMENT_LABEL } from '../data/elements';
import { FORMATIONS, getFormation } from '../data/formations';
import type { Formation, PlayerData, Stats } from '../data/types';
import { portraitPack, portraitsOf } from '../gfx/pack';
import { availableFormations, loadClub, setSquad } from '../club/club';
import { portraitKey, spriteKey, texKey } from '../gfx/placeholders';
import { VSPRITE_REF } from '../gfx/pack';
import { bestLineup, lineupPlayers, swapInLineup, type Lineup } from '../engine/lineup';
import { lineRatings, playerOverall, ratingStars, teamRating } from '../engine/rating';
import { cardPanel, chip, fitCamera, POS_COLOR, pt, sectionTitle, slant, stadiumBackdrop, starRow, THEME, toast, topBar } from '../ui/theme';
import { Button, StatBar, display, fitWidth, label, meter, text } from '../ui/widgets';

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

/** Diseño vertical (móvil, 540x960): campo arriba a lo ancho, banquillo debajo y la barra de acciones fija abajo. */
const MOB = { pitch: { x: 12, y: 128, w: 516, h: 460 }, bench: { x: 12, y: 598, w: 516, h: 118 }, bar: { x: 12, y: 724, w: 516, h: 228 } };
const PITCH_BOX = PORTRAIT ? MOB.pitch : { x: 24, y: 96, w: 452, h: 540 };
// rango de alturas de los puestos de todas las formaciones (src/data/formations.json), para que ninguna se salga del campo
const SLOT_Y_MIN = 0.19;
const SLOT_Y_MAX = 0.98;
const CARD = { x: 500, y: 84, w: 756, h: 316 };
const BENCH = { x: 500, y: 412, w: 756, h: 148 };
const BAR = { x: 500, y: 572, w: 756, h: 136 };
const FORMATIONS_PER_PAGE = 27;

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
  private summary!: Phaser.GameObjects.Container;
  private pitchHint!: Phaser.GameObjects.Text;
  /** En vertical: tira de abajo con el jugador elegido (o las medias del once) y la ficha que sube al pulsar "Ficha". */
  private strip: Phaser.GameObjects.Container | null = null;
  private sheet: Phaser.GameObjects.Container | null = null;

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
    // los de "Mi club" vienen de muchos equipos: sus retratos, uno a uno
    const club = [this.home, this.away].flatMap((l) => getTeam(l.teamId).players.filter((p) => p.origin).map((p) => ({ team: p.origin!, id: p.originId ?? p.id })));
    for (const { key, url } of [...portraitPack([this.home.teamId, this.away.teamId]), ...portraitsOf(club)]) {
      if (!this.textures.exists(key)) this.load.image(key, url);
    }
    this.load.on(Phaser.Loader.Events.FILE_COMPLETE, (key: string) => this.textures.get(key).setFilter(Phaser.Textures.FilterMode.LINEAR));
  }

  create(): void {
    fitCamera(this);
    if (!this.halftime) music.play('menu');
    const team = getTeam(this.home.teamId);
    const rival = getTeam(this.away.teamId);
    stadiumBackdrop(this, hex(team.colors.shirt), hex(rival.colors.shirt));
    this.strip = null;
    this.sheet = null;
    this.formationList = null;
    if (PORTRAIT) return this.createPortrait(team, rival);

    // cabecera: escudo, título, marcador en el descanso y el rival
    topBar(this, {
      title: this.halftime ? 'Descanso' : 'Formación',
      subtitle: team.name,
      icon: texKey.emblem(team.id),
      back: this.halftime ? undefined : { label: 'Menú', onClick: () => this.scene.start('menu') },
      accent: hex(team.colors.accent),
    });
    if (this.halftime) {
      const [a, b] = this.halftime.score;
      display(this, 640, 32, `${team.short}  ${a} - ${b}  ${rival.short}`, 34, '#ffffff').setOrigin(0.5).setDepth(101);
    }
    const rx = GAME_W - 24;
    this.add.image(rx - 24, 32, texKey.emblem(rival.id)).setDisplaySize(44, 44).setDepth(101);
    label(this, rx - 56, 23, 'RIVAL', 10, THEME.awayCss, { fontStyle: 'bold' }).setOrigin(1, 0.5).setDepth(101);
    label(this, rx - 56, 40, `${rival.name}  ·  ${teamRating(rival)}`, 15, THEME.text, { fontStyle: 'italic bold' }).setOrigin(1, 0.5).setDepth(101);

    this.drawPitch();
    this.info = this.add.container(CARD.x, CARD.y);

    // banquillo
    const g = this.add.graphics();
    cardPanel(g, BENCH.x, BENCH.y, BENCH.w, BENCH.h, { accent: hex(team.colors.accent) });
    sectionTitle(this, BENCH.x + 16, BENCH.y + 22, 'Banquillo');
    this.hint = label(this, BENCH.x + BENCH.w - 16, BENCH.y + 22, '', 12, THEME.muted, { fontStyle: 'italic' }).setOrigin(1, 0.5);

    // barra de abajo: formación, mejor once, medias del once y jugar
    const bg = this.add.graphics();
    cardPanel(bg, BAR.x, BAR.y, BAR.w, BAR.h, { plain: true });
    const fy = BAR.y + 36;
    label(this, BAR.x + 18, fy - 20, 'FORMACIÓN', 10, THEME.muted, { fontStyle: 'bold' }).setOrigin(0, 0.5);
    new Button(this, BAR.x + 40, fy + 8, '◀', () => this.cycleFormation(-1), { w: 40, h: 34, variant: 'secondary', size: 13 });
    new Button(this, BAR.x + 330, fy + 8, '▶', () => this.cycleFormation(1), { w: 40, h: 34, variant: 'secondary', size: 13 });
    this.formationLabel = label(this, BAR.x + 185, fy + 8, '', 18, THEME.text, { fontStyle: 'italic bold' }).setOrigin(0.5);
    // pulsar el nombre abre la lista de todas las formaciones
    const labelHit = this.add.zone(BAR.x + 64, fy - 10, 242, 36).setOrigin(0).setInteractive({ useHandCursor: true });
    labelHit.on('pointerdown', () => this.toggleFormationList());
    labelHit.on('pointerover', () => this.formationLabel.setColor(THEME.yellowCss));
    labelHit.on('pointerout', () => this.formationLabel.setColor(THEME.text));
    label(this, BAR.x + 185, fy + 32, 'pulsa el nombre para ver todas', 10, THEME.muted, { fontStyle: 'italic' }).setOrigin(0.5);
    new Button(this, BAR.x + 460, fy + 8, 'Mejor once', () => this.autoLineup(), { w: 150, h: 38, variant: 'accent', size: 15, icon: '✦' });
    this.summary = this.add.container(BAR.x + 18, BAR.y + 100);
    this.input.keyboard?.on('keydown-ESC', () => (this.formationList ? this.closeFormationList() : !this.halftime && this.scene.start('menu')));
    this.input.keyboard?.on('keydown-ENTER', () => this.play());
    new Button(this, BAR.x + BAR.w - 100, BAR.y + BAR.h / 2, this.halftime ? '¡2ª parte!' : '¡A jugar!', () => this.play(), { w: 170, h: 60, variant: 'primary', size: 24, hint: '⏎' });

    this.layoutTokens();
    this.showInfo(lineupPlayers(team, this.home)[0]);
  }

  /** Campo en verde oscuro con las líneas finas, dentro de un marco redondeado. */
  private drawPitch(): void {
    const { x, y, w, h } = PITCH_BOX;
    const g = this.add.graphics();
    g.fillStyle(0x000000, 0.45).fillRoundedRect(x + 4, y + 8, w, h, 12);
    g.fillStyle(0x1f6b3a).fillRoundedRect(x, y, w, h, 12);
    for (let i = 0; i < 10; i++) if (i % 2) g.fillStyle(0x247a43).fillRect(x, y + (i * h) / 10, w, h / 10);
    // brillo diagonal
    g.fillStyle(0xffffff, 0.05).fillPoints([pt(x, y), pt(x + w * 0.55, y), pt(x, y + h * 0.5)], true);
    g.lineStyle(2, 0xffffff, 0.55).strokeRect(x + 10, y + 10, w - 20, h - 20);
    g.lineBetween(x + 10, y + 10, x + w - 10, y + 10);
    g.beginPath();
    g.arc(x + w / 2, y + 10, 64, 0, Math.PI);
    g.strokePath();
    g.strokeRect(x + w / 2 - 110, y + h - 100, 220, 90);
    g.strokeRect(x + w / 2 - 50, y + h - 44, 100, 34);
    g.lineStyle(2, 0xffffff, 0.15).strokeRoundedRect(x, y, w, h, 12);
    const tag = chip(this, x + 10, y - 2, 'TITULARES', THEME.yellow, PORTRAIT ? { size: 15, h: 28, padX: 12 } : { size: 11, h: 22, padX: 10 });
    tag.setDepth(2);
    this.pitchHint = label(this, x + w - 10, y - 2, '', PORTRAIT ? 15 : 11, THEME.muted, { fontStyle: 'italic bold' }).setOrigin(1, 0.5).setDepth(2);
  }

  /** Altura de un puesto en el campo: las formaciones de la wiki van de y≈0,19 (delanteros muy adelantados) a 0,98 (portero). */
  private slotY(sy: number): number {
    const t = Phaser.Math.Clamp((sy - SLOT_Y_MIN) / (SLOT_Y_MAX - SLOT_Y_MIN), 0, 1);
    return PITCH_BOX.y + 34 + t * (PITCH_BOX.h - 84);
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
    const layout = ['DF', 'MF', 'FW'].map((pos) => formation.slots.filter((s) => s.pos === pos).length).join('-');
    this.formationLabel.setText(`${formation.name}  ·  ${layout}`);
    const players = lineupPlayers(team, this.home);

    players.forEach((p, index) => {
      let x: number;
      let y: number;
      if (index < 11) {
        const slot = formation.slots[index];
        x = PITCH_BOX.x + 40 + slot.x * (PITCH_BOX.w - 80);
        y = this.slotY(slot.y);
      } else if (PORTRAIT) {
        // banquillo en una fila: se aprietan si son muchos
        const n = Math.max(1, players.length - 11);
        const step = Math.min(76, (MOB.bench.w - 40) / n);
        x = MOB.bench.x + MOB.bench.w / 2 + (index - 11 - (n - 1) / 2) * step;
        y = MOB.bench.y + 64;
      } else {
        const b = index - 11;
        x = BENCH.x + 60 + (b % 9) * 76;
        y = BENCH.y + 80 + Math.floor(b / 9) * 64;
      }
      const token = this.makeToken(p, index, x, y);
      const from = before.get(index);
      if (from && (from.x !== x || from.y !== y)) {
        token.setPosition(from.x, from.y);
        this.tweens.add({ targets: token, x, y, duration: 180, ease: 'Cubic.Out' });
      }
      this.tokens.push({ index, container: token });
    });
    this.hint.setText(this.selected === null ? (PORTRAIT ? 'Toca dos para cambiarlos' : 'Pulsa dos jugadores para cambiarlos') : PORTRAIT ? 'Toca con quién cambiarlo' : 'Ahora pulsa con quién cambiarlo');
    this.drawSummary(formation.id);
  }

  /** Medias del once que hay en el campo ahora mismo (y avisos de jugadores fuera de su puesto). */
  private drawSummary(formationId: string): void {
    if (PORTRAIT) return this.drawSummaryPortrait(formationId);
    const c = this.summary;
    c.removeAll(true);
    const team = getTeam(this.home.teamId);
    const starters = lineupPlayers(team, this.home).slice(0, 11);
    const rating = teamRating(team, starters);
    const lines = lineRatings(team, starters);
    c.add(display(this, 0, 0, String(rating), 30, THEME.yellowCss, { strokeThickness: 0 }).setOrigin(0, 0.5));
    c.add(starRow(this, 46, -2, ratingStars(rating), 6));
    c.add(label(this, 46, 12, 'MEDIA DEL ONCE', 9, THEME.muted, { fontStyle: 'bold' }).setOrigin(0, 0.5));
    const rows = [
      ['ATA', lines.att, THEME.orange],
      ['MED', lines.mid, THEME.green],
      ['DEF', lines.def, 0x4fa3ff],
    ] as const;
    rows.forEach(([cap, v, color], i) => c.add(meter(this, 200 + i * 130, 0, 60, v - 30, 60, color, cap, String(v))));
    const slots = getFormation(formationId).slots;
    const wrong = starters.filter((p, i) => slots[i] && slots[i].pos !== p.position).length;
    const gkOk = starters[0]?.position === 'GK';
    const warn = !gkOk ? '⚠ Sin portero en la portería' : wrong ? `⚠ ${wrong} fuera de su puesto (chapa en rojo)` : '';
    this.pitchHint.setText(warn || 'Todos en su puesto ✓').setColor(warn ? THEME.coralCss : THEME.muted);
  }

  /** Chapa del jugador: sprite sobre un círculo, nombre en una banda y la demarcación en su color. */
  private makeToken(p: PlayerData, index: number, x: number, y: number): Phaser.GameObjects.Container {
    const c = this.add.container(x, y);
    const selected = this.selected === index;
    const slotPos = index < 11 ? getFormation(this.previewId ?? this.home.formationId).slots[index].pos : p.position;
    const outOfPosition = index < 11 && slotPos !== p.position;
    const g = this.add.graphics();
    g.fillStyle(0x000000, 0.35).fillEllipse(0, 20, 40, 12);
    if (selected) g.fillStyle(THEME.cyan, 0.3).fillCircle(0, 0, 28).lineStyle(3, THEME.cyan).strokeCircle(0, 0, 28);
    const sprite = this.add.image(0, -2, spriteKey(this, p, getTeam(this.home.teamId)));
    // los dibujados (vsprite) guardan la altura de cada uno: misma escala para todos
    sprite.setScale(sprite.texture.key.startsWith('vsprite:') ? 44 / VSPRITE_REF : 44 / sprite.height);
    const nameBand = this.add.graphics();
    const lbl = text(this, 0, 32, p.short, 12, '#ffffff', { fontStyle: 'italic bold', strokeThickness: 3 }).setOrigin(0.5);
    const bw = Math.max(54, lbl.width + 18);
    nameBand.fillStyle(0x000000, 0.6).fillRoundedRect(-bw / 2, 24, bw, 16, 8);
    const posChip = this.add.graphics();
    posChip.fillStyle(POS_COLOR[p.position]).fillRoundedRect(10, -32, 30, 14, 5);
    if (outOfPosition) posChip.lineStyle(2, THEME.coral).strokeRoundedRect(10, -32, 30, 14, 5);
    const pos = text(this, 25, -25, p.position, 10, '#ffffff', { fontStyle: 'bold', strokeThickness: 2 }).setOrigin(0.5);
    const elem = this.add.graphics().fillStyle(ELEMENT_COLOR[p.element]).fillCircle(-20, -24, 6).lineStyle(1.5, 0xffffff).strokeCircle(-20, -24, 6);
    c.add([g, sprite, nameBand, lbl, posChip, pos, elem]);
    if (this.halftime) {
      // en el descanso, la estamina de cada uno debajo del nombre, para decidir los cambios
      const { fp } = this.bars(p);
      const ratio = Phaser.Math.Clamp(fp / p.fp, 0, 1);
      const bar = this.add.graphics();
      bar.fillStyle(0x000000, 0.7).fillRoundedRect(-22, 42, 44, 5, 2);
      bar.fillStyle(ratio < 0.01 ? 0xe2463b : COLORS.fp).fillRoundedRect(-21, 43, 42 * ratio, 3, 1);
      c.add(bar);
    }
    c.setSize(60, 76);
    if (PORTRAIT) {
      // en el móvil, algo más grandes y sin "pasar el ratón": tocar elige (y la tira de abajo enseña al elegido)
      c.setScale(1.15);
      c.setInteractive().on('pointerdown', () => this.pick(index));
      return c;
    }
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

  private autoLineup(): void {
    const next = bestLineup(getTeam(this.home.teamId), this.home);
    if (next.order.join() === this.home.order.join()) return toast(this, 'Ya está el mejor once para esta formación', THEME.panelLight);
    this.home = next;
    this.selected = null;
    this.layoutTokens();
    toast(this, 'Colocados los mejores en cada puesto');
  }

  /**
   * Lista de formaciones sobre la ficha: filtro por distribución, páginas de 27 y, en cada fila, un mini campo con la
   * colocación (para distinguir las que tienen la misma distribución). Al pasar el ratón se ve en el campo grande y sus
   * otros nombres (las formaciones de la wiki con la misma colocación están juntas); al pulsar se elige.
   */
  private formationFilter = 'all';
  private formationPage = 0;

  private toggleFormationList(): void {
    if (this.formationList) return this.closeFormationList();
    // la página donde está la formación elegida
    const list = this.filteredFormations();
    const at = list.findIndex((f) => f.id === this.home.formationId);
    this.formationPage = at >= 0 ? Math.floor(at / this.formationsPerPage()) : 0;
    this.drawFormationList();
  }

  private filteredFormations(): Formation[] {
    const avail = availableFormations(this.home.teamId);
    const all = [...FORMATIONS].sort((a, b) => Number(!avail.has(a.id)) - Number(!avail.has(b.id)) || a.name.localeCompare(b.name));
    if (this.formationFilter === 'all') return all;
    if (this.formationFilter === 'other') return all.filter((f) => !this.formationFilters().includes(f.layout));
    return all.filter((f) => f.layout === this.formationFilter);
  }

  /** Distribuciones con al menos 4 formaciones (las demás van en "Otras"), de más a menos frecuentes. */
  private formationFilters(): string[] {
    const count = new Map<string, number>();
    for (const f of FORMATIONS) count.set(f.layout, (count.get(f.layout) ?? 0) + 1);
    return [...count.entries()].filter(([, n]) => n >= 4).sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0])).map(([l]) => l);
  }

  private formationsPerPage(): number {
    return PORTRAIT ? this.portraitListRows() : FORMATIONS_PER_PAGE;
  }

  private drawFormationList(): void {
    if (PORTRAIT) return this.drawFormationListPortrait();
    this.formationList?.destroy();
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
    cardPanel(g, X, Y, Wd, Hd, { alpha: 1 });
    const panelHit = this.add.zone(X, Y, Wd, Hd).setOrigin(0).setInteractive();
    c.add([back, g, panelHit]);
    c.add(sectionTitle(this, X + 18, Y + 22, 'Formaciones'));
    const avail = availableFormations(this.home.teamId);
    const won = FORMATIONS.filter((f) => !f.generic && avail.has(f.id)).length;
    const total = FORMATIONS.filter((f) => !f.generic).length;
    c.add(label(this, X + 160, Y + 22, `${won} de ${total} conseguidas · ganas una con cada victoria`, 12, THEME.yellowCss, { fontStyle: 'bold' }).setOrigin(0, 0.5));
    c.add(label(this, X + Wd - 18, Y + 22, 'Pasa el ratón para verla · pulsa para elegirla · Esc cierra', 12, THEME.muted, { fontStyle: 'italic' }).setOrigin(1, 0.5));

    // filtros por distribución
    const filters = ['all', ...this.formationFilters(), 'other'];
    let fx = X + 18;
    for (const id of filters) {
      const on = this.formationFilter === id;
      const n = id === 'all' ? FORMATIONS.length : id === 'other' ? FORMATIONS.filter((f) => !filters.includes(f.layout)).length : FORMATIONS.filter((f) => f.layout === id).length;
      const t = `${id === 'all' ? 'Todas' : id === 'other' ? 'Otras' : id} ${n}`;
      const ch = chip(this, fx, Y + 52, t, on ? THEME.yellow : THEME.panelLight, { size: 12, h: 24, padX: 10, textColor: on ? THEME.ink : THEME.text });
      const hit = this.add.zone(fx, Y + 40, ch.width, 24).setOrigin(0).setInteractive({ useHandCursor: true });
      hit.on('pointerdown', () => {
        this.formationFilter = id;
        this.formationPage = 0;
        this.drawFormationList();
      });
      c.add([ch, hit]);
      fx += ch.width + 6;
    }

    const list = this.filteredFormations();
    const pages = Math.max(1, Math.ceil(list.length / FORMATIONS_PER_PAGE));
    this.formationPage = Math.min(this.formationPage, pages - 1);
    const shown = list.slice(this.formationPage * FORMATIONS_PER_PAGE, (this.formationPage + 1) * FORMATIONS_PER_PAGE);
    const cols = 3;
    const rowsPer = FORMATIONS_PER_PAGE / cols;
    const cw = (Wd - 36 - (cols - 1) * 10) / cols;
    const rh = 40;
    const top = Y + 74;
    const also = label(this, X + 18, Y + Hd - 22, '', 12, THEME.muted, { fontStyle: 'italic' }).setOrigin(0, 0.5);
    c.add(also);
    shown.forEach((f, i) => {
      const cx = X + 18 + Math.floor(i / rowsPer) * (cw + 10);
      const cy = top + (i % rowsPer) * rh;
      const current = f.id === getFormation(this.home.formationId).id;
      const locked = !avail.has(f.id) && !current;
      const bg = this.add.graphics();
      const draw = (hover: boolean) => {
        bg.clear();
        bg.fillStyle(current ? THEME.yellow : hover ? THEME.panelLight : 0x14223a, current ? 0.92 : hover ? 1 : locked ? 0.35 : 0.7).fillRoundedRect(cx, cy + 2, cw, rh - 4, 8);
      };
      draw(false);
      // mini campo, con la portería propia a la izquierda y el ataque hacia la derecha
      const mw = 50;
      const mh = 30;
      const mx = cx + 6;
      const my = cy + (rh - mh) / 2;
      const m = this.add.graphics();
      m.fillStyle(0x2f7d3e, 1).fillRoundedRect(mx, my, mw, mh, 4);
      m.lineStyle(1, 0xffffff, 0.35).lineBetween(mx + mw / 2, my + 2, mx + mw / 2, my + mh - 2);
      for (const s of f.slots) {
        const col = s.pos === 'GK' ? 0xffffff : s.pos === 'DF' ? 0x4f9bff : s.pos === 'MF' ? 0xffb02e : 0xff5050;
        m.fillStyle(col, 1).fillCircle(mx + 3 + (1 - s.y) * (mw - 6), my + 3 + s.x * (mh - 6), 2.1);
      }
      if (locked) m.setAlpha(0.35);
      const name = label(this, cx + 64, cy + rh / 2, locked ? `🔒 ${f.name}` : f.name, 14, current ? THEME.ink : locked ? THEME.muted : THEME.text, { fontStyle: 'italic bold' }).setOrigin(0, 0.5);
      fitWidth(name, cw - 64 - 52, 10);
      const lay = label(this, cx + cw - 10, cy + rh / 2, f.layout, 12, current ? THEME.ink : '#9fb8d8', { fontStyle: 'bold' }).setOrigin(1, 0.5);
      const hit = this.add.zone(cx, cy, cw, rh).setOrigin(0).setInteractive({ useHandCursor: true });
      hit.on('pointerover', () => {
        draw(true);
        also.setText(
          locked
            ? `${f.name}: aún no la tienes${f.generic ? '' : ' (gana partidos para conseguirla)'}`
            : f.also?.length
              ? `${f.name}: la misma colocación que ${f.also.join(', ')}`
              : '',
        );
        this.layoutTokens(f.id);
      });
      hit.on('pointerout', () => {
        draw(false);
        also.setText('');
        if (this.previewId === f.id) this.layoutTokens();
      });
      hit.on('pointerdown', () => {
        if (locked) return toast(this, 'Esa formación aún no la tienes: se consiguen ganando partidos', THEME.panelLight);
        this.closeFormationList();
        this.setFormation(f.id);
      });
      c.add([bg, m, name, lay, hit]);
    });
    if (pages > 1) {
      const py = Y + Hd - 22;
      c.add(new Button(this, X + Wd - 150, py, '◀', () => ((this.formationPage = (this.formationPage + pages - 1) % pages), this.drawFormationList()), { w: 44, h: 30, variant: 'secondary', size: 14 }));
      c.add(label(this, X + Wd - 96, py, `${this.formationPage + 1} / ${pages}`, 13, THEME.text, { fontStyle: 'bold' }).setOrigin(0.5));
      c.add(new Button(this, X + Wd - 42, py, '▶', () => ((this.formationPage = (this.formationPage + 1) % pages), this.drawFormationList()), { w: 44, h: 30, variant: 'secondary', size: 14 }));
    }
  }

  private closeFormationList(): void {
    if (!this.formationList) return;
    this.formationList.destroy();
    this.formationList = null;
    if (this.previewId) this.layoutTokens();
  }

  private cycleFormation(d: number): void {
    const avail = availableFormations(this.home.teamId);
    const cur = getFormation(this.home.formationId).id;
    const all = [...FORMATIONS].filter((f) => avail.has(f.id) || f.id === cur).sort((a, b) => a.name.localeCompare(b.name));
    const i = all.findIndex((f) => f.id === cur);
    const next = all[(i + d + all.length) % all.length];
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
    cardPanel(g, 0, 0, W, H, { accent });
    // dorsal gigante de fondo
    const number = text(this, W - 20, -14, String(p.number), 150, '#ffffff', { fontStyle: 'italic bold', strokeThickness: 0 }).setOrigin(1, 0).setAlpha(0.05);
    // retrato en un marco inclinado
    g.fillStyle(accent).fillPoints(slant(14, 16, 132, 132, 18), true);
    g.fillStyle(0x000000, 0.35).fillPoints(slant(20, 22, 120, 120, 16), true);
    const portrait = this.add.image(80, 82, portraitKey(this, p, team)).setDisplaySize(112, 112);
    // nombre y etiquetas
    const name = display(this, 166, 18, p.name, 32, '#ffffff');
    fitWidth(name, 250, 15);
    const tags = this.add.graphics();
    tags.fillStyle(POS_COLOR[p.position]).fillRoundedRect(166, 58, 56, 22, 7);
    tags.fillStyle(ELEMENT_COLOR[p.element]).fillRoundedRect(228, 58, 96, 22, 7);
    tags.fillStyle(0x000000, 0.5).fillRoundedRect(330, 58, 72, 22, 7);
    const posT = label(this, 194, 69, p.position, 13, '#ffffff', { fontStyle: 'bold' }).setOrigin(0.5);
    const elT = label(this, 276, 69, ELEMENT_LABEL[p.element], 13, '#ffffff', { fontStyle: 'bold' }).setOrigin(0.5);
    const lvT = label(this, 366, 69, `Nv. ${p.level}`, 13, THEME.yellowCss, { fontStyle: 'bold' }).setOrigin(0.5);
    const fp = new StatBar(this, 166, 102, 'FP', COLORS.fp, 150);
    fp.set(this.bars(p).fp, p.fp);
    const tp = new StatBar(this, 166, 126, 'TP', COLORS.tp, 150);
    tp.set(this.bars(p).tp, p.tp);
    const ov = display(this, W - 24, 56, String(playerOverall(p)), 44, THEME.yellowCss, { strokeThickness: 0 }).setOrigin(1, 0.5);
    const ovL = label(this, W - 24, 84, 'MEDIA', 9, THEME.muted, { fontStyle: 'bold' }).setOrigin(1, 0.5);
    this.info.add([g, number, portrait, name, tags, posT, elT, lvT, fp, tp, ov, ovL]);

    // atributos en barras
    const sx = 430;
    STAT_LABELS.forEach(([key, lbl], i) => {
      const y = 108 + i * 17;
      const v = p.stats[key];
      const bar = this.add.graphics();
      bar.fillStyle(0x000000, 0.45).fillRoundedRect(sx + 66, y - 4, 160, 8, 4);
      bar.fillStyle(v >= 75 ? THEME.yellow : THEME.glow).fillRoundedRect(sx + 66, y - 4, Phaser.Math.Clamp(v / 99, 0.05, 1) * 160, 8, 4);
      this.info.add(bar);
      this.info.add(label(this, sx, y, lbl, 12, THEME.muted, { fontStyle: 'italic' }).setOrigin(0, 0.5));
      this.info.add(label(this, sx + 256, y, String(v), 13, THEME.text, { fontStyle: 'bold' }).setOrigin(1, 0.5));
    });

    // supertécnicas
    this.info.add(sectionTitle(this, 16, 172, 'Supertécnicas'));
    const moves = movesOf(p.moves);
    if (moves.length === 0) this.info.add(label(this, 34, 192, '—', 15));
    moves.slice(0, 6).forEach((m, i) => {
      const y = 190 + i * 20;
      const row = this.add.graphics();
      row.fillStyle(0x000000, i % 2 ? 0.15 : 0.3).fillRoundedRect(16, y, 396, 18, 4);
      row.fillStyle(ELEMENT_COLOR[m.element]).fillRoundedRect(16, y, 5, 18, 2);
      this.info.add(row);
      this.info.add(label(this, 30, y + 9, m.name, 13, THEME.text, { fontStyle: 'bold' }).setOrigin(0, 0.5));
      this.info.add(label(this, 406, y + 9, `${MOVE_KIND_LABEL[m.kind]}  ·  ${m.power}  ·  TP ${m.tp}`, 11, THEME.muted).setOrigin(1, 0.5));
    });

    // descripción
    const dg = this.add.graphics();
    dg.fillStyle(0x000000, 0.3).fillRoundedRect(430, 232, W - 446, H - 248, 8);
    dg.fillStyle(accent).fillRoundedRect(430, 232, 3, H - 248, 2);
    this.info.add(dg);
    this.info.add(
      label(this, 444, 242, p.description ?? `Jugador de ${team.name}.`, 12, THEME.text, {
        fontStyle: 'italic',
        wordWrap: { width: W - 474 },
        lineSpacing: 3,
      }),
    );
  }

  // ------------------------------------------------------------------ móvil (vertical)

  /** Pantalla de formación en vertical: campo arriba, banquillo, y abajo la tira del jugador, la formación y jugar. */
  private createPortrait(team: ReturnType<typeof getTeam>, rival: ReturnType<typeof getTeam>): void {
    const accent = hex(team.colors.accent);
    topBar(this, {
      title: this.halftime ? 'Descanso' : 'Formación',
      subtitle: team.name,
      icon: texKey.emblem(team.id),
      back: this.halftime ? undefined : { label: 'Menú', onClick: () => this.scene.start('menu') },
      accent,
    });
    if (this.halftime) {
      const [a, b] = this.halftime.score;
      display(this, GAME_W - 18, 32, `${a} - ${b}`, 36, '#ffffff').setOrigin(1, 0.5).setDepth(101);
    }
    // el rival, en una fila bajo la cabecera
    const ry = 86;
    this.add.image(32, ry, texKey.emblem(rival.id)).setDisplaySize(36, 36);
    label(this, 58, ry - 9, 'RIVAL', 13, THEME.awayCss, { fontStyle: 'bold' }).setOrigin(0, 0.5);
    const rn = label(this, 58, ry + 10, rival.name, 18, THEME.text, { fontStyle: 'italic bold' }).setOrigin(0, 0.5);
    fitWidth(rn, 340, 13);
    display(this, GAME_W - 18, ry, String(teamRating(rival)), 30, THEME.yellowCss, { strokeThickness: 0 }).setOrigin(1, 0.5);
    label(this, GAME_W - 58, ry, 'MEDIA', 12, THEME.muted, { fontStyle: 'bold' }).setOrigin(1, 0.5);

    this.drawPitch();

    // banquillo
    const { bench, bar } = MOB;
    const g = this.add.graphics();
    cardPanel(g, bench.x, bench.y, bench.w, bench.h, { accent });
    chip(this, bench.x + 12, bench.y + 18, 'BANQUILLO', THEME.panelLight, { size: 14, h: 26, padX: 10, textColor: THEME.text });
    this.hint = label(this, bench.x + bench.w - 12, bench.y + 18, '', 15, THEME.muted, { fontStyle: 'italic' }).setOrigin(1, 0.5);

    // barra de abajo: jugador elegido / medias, formación y botones
    const bg = this.add.graphics();
    cardPanel(bg, bar.x, bar.y, bar.w, bar.h, { plain: true });
    this.summary = this.add.container(0, 0);
    this.strip = this.add.container(0, 0);
    const fy = bar.y + 112;
    new Button(this, bar.x + 44, fy, '◀', () => this.cycleFormation(-1), { w: 64, h: 60, variant: 'secondary', size: 22 });
    new Button(this, bar.x + bar.w - 44, fy, '▶', () => this.cycleFormation(1), { w: 64, h: 60, variant: 'secondary', size: 22 });
    this.formationLabel = label(this, GAME_W / 2, fy - 9, '', 21, THEME.text, { fontStyle: 'italic bold' }).setOrigin(0.5);
    label(this, GAME_W / 2, fy + 16, 'toca para ver todas  ▾', 14, THEME.muted, { fontStyle: 'italic' }).setOrigin(0.5);
    const hit = this.add.zone(bar.x + 82, fy - 30, bar.w - 164, 60).setOrigin(0).setInteractive();
    hit.on('pointerdown', () => this.toggleFormationList());
    const by = bar.y + bar.h - 42;
    new Button(this, bar.x + 106, by, 'Mejor once', () => this.autoLineup(), { w: 196, h: 66, variant: 'accent', size: 19, icon: '✦' });
    new Button(this, bar.x + bar.w - 152, by, this.halftime ? '¡2ª parte!' : '¡A jugar!', () => this.play(), { w: 290, h: 72, variant: 'primary', size: 28 });

    this.input.keyboard?.on('keydown-ESC', () => (this.sheet ? this.closeSheet() : this.formationList ? this.closeFormationList() : !this.halftime && this.scene.start('menu')));
    this.input.keyboard?.on('keydown-ENTER', () => this.play());
    this.layoutTokens();
  }

  /** Avisos del once (sobre el campo) y la tira de abajo. */
  private drawSummaryPortrait(formationId: string): void {
    const team = getTeam(this.home.teamId);
    const starters = lineupPlayers(team, this.home).slice(0, 11);
    const slots = getFormation(formationId).slots;
    const wrong = starters.filter((p, i) => slots[i] && slots[i].pos !== p.position).length;
    const gkOk = starters[0]?.position === 'GK';
    const warn = !gkOk ? '⚠ Sin portero' : wrong ? `⚠ ${wrong} fuera de su puesto` : '';
    this.pitchHint.setText(warn || 'Todos en su puesto ✓').setColor(warn ? THEME.coralCss : THEME.muted);
    this.drawStrip();
  }

  /** Tira de arriba de la barra: el jugador elegido (con su ficha) o, si no hay ninguno, las medias del once. */
  private drawStrip(): void {
    const c = this.strip;
    if (!c) return;
    c.removeAll(true);
    const team = getTeam(this.home.teamId);
    const { bar } = MOB;
    const cy = bar.y + 38;
    const players = lineupPlayers(team, this.home);
    const p = this.selected !== null ? players[this.selected] : null;
    if (p) {
      const g = this.add.graphics();
      g.fillStyle(THEME.cyan, 0.16).fillRoundedRect(bar.x + 8, cy - 30, bar.w - 16, 60, 10).lineStyle(2, THEME.cyan, 0.8).strokeRoundedRect(bar.x + 8, cy - 30, bar.w - 16, 60, 10);
      const portrait = this.add.image(bar.x + 42, cy, portraitKey(this, p, team)).setDisplaySize(52, 52);
      const name = display(this, bar.x + 76, cy - 11, p.name, 24, '#ffffff', { strokeThickness: 0 }).setOrigin(0, 0.5);
      fitWidth(name, 250, 15);
      const info = label(this, bar.x + 76, cy + 14, `${p.position}  ·  ${ELEMENT_LABEL[p.element]}  ·  media ${playerOverall(p)}`, 15, THEME.muted, { fontStyle: 'bold' }).setOrigin(0, 0.5);
      c.add([g, portrait, name, info, new Button(this, bar.x + bar.w - 66, cy, 'Ficha', () => this.showSheet(p), { w: 108, h: 50, variant: 'accent', size: 18, icon: 'ⓘ' })]);
      return;
    }
    const starters = players.slice(0, 11);
    const rating = teamRating(team, starters);
    const lines = lineRatings(team, starters);
    c.add(display(this, bar.x + 18, cy, String(rating), 38, THEME.yellowCss, { strokeThickness: 0 }).setOrigin(0, 0.5));
    c.add(starRow(this, bar.x + 72, cy - 10, ratingStars(rating), 7));
    c.add(label(this, bar.x + 72, cy + 10, 'MEDIA DEL ONCE', 13, THEME.muted, { fontStyle: 'bold' }).setOrigin(0, 0.5));
    const rows = [
      ['ATA', lines.att, THEME.orange],
      ['MED', lines.mid, THEME.green],
      ['DEF', lines.def, 0x4fa3ff],
    ] as const;
    rows.forEach(([cap, v, color], i) => {
      const y = cy - 18 + i * 18;
      const g = this.add.graphics();
      const x0 = bar.x + 270;
      g.fillStyle(0x000000, 0.5).fillRoundedRect(x0, y - 4, 160, 8, 4);
      g.fillStyle(color).fillRoundedRect(x0, y - 4, Math.max(8, 160 * Phaser.Math.Clamp((v - 30) / 60, 0, 1)), 8, 4);
      c.add([g, label(this, x0 - 8, y, cap, 14, THEME.muted, { fontStyle: 'italic bold' }).setOrigin(1, 0.5), label(this, x0 + 168, y, String(v), 15, THEME.text, { fontStyle: 'bold' }).setOrigin(0, 0.5)]);
    });
  }

  /** Ficha completa del jugador: una hoja que sube desde abajo (se cierra con ✕ o tocando fuera). */
  private showSheet(p: PlayerData): void {
    this.closeSheet();
    const team = getTeam(this.home.teamId);
    const accent = hex(team.colors.accent);
    const W = GAME_W - 16;
    const top = 196;
    const H = GAME_H - top;
    const root = this.add.container(0, 0).setDepth(160);
    this.sheet = root;
    const shade = this.add.rectangle(GAME_W / 2, GAME_H / 2, GAME_W, GAME_H, 0x000000, 0.55).setInteractive();
    shade.on('pointerdown', () => this.closeSheet());
    root.add(shade);
    const c = this.add.container(8, top);
    root.add(c);
    const g = this.add.graphics();
    cardPanel(g, 0, 0, W, H + 20, { accent, alpha: 1 });
    const block = this.add.zone(0, 0, W, H).setOrigin(0).setInteractive();
    const number = text(this, W - 20, 120, String(p.number), 150, '#ffffff', { fontStyle: 'italic bold', strokeThickness: 0 }).setOrigin(1, 0).setAlpha(0.05);
    g.fillStyle(accent).fillPoints(slant(14, 18, 124, 124, 18), true);
    g.fillStyle(0x000000, 0.35).fillPoints(slant(20, 24, 112, 112, 16), true);
    const portrait = this.add.image(76, 80, portraitKey(this, p, team)).setDisplaySize(104, 104);
    const name = display(this, 150, 34, p.name, 32, '#ffffff').setOrigin(0, 0.5);
    fitWidth(name, W - 150 - 80, 16);
    const tags = this.add.graphics();
    tags.fillStyle(POS_COLOR[p.position]).fillRoundedRect(150, 58, 56, 28, 8);
    tags.fillStyle(ELEMENT_COLOR[p.element]).fillRoundedRect(212, 58, 104, 28, 8);
    tags.fillStyle(0x000000, 0.5).fillRoundedRect(322, 58, 80, 28, 8);
    const posT = label(this, 178, 72, p.position, 16, '#ffffff', { fontStyle: 'bold' }).setOrigin(0.5);
    const elT = label(this, 264, 72, ELEMENT_LABEL[p.element], 16, '#ffffff', { fontStyle: 'bold' }).setOrigin(0.5);
    const lvT = label(this, 362, 72, `Nv. ${p.level}`, 16, THEME.yellowCss, { fontStyle: 'bold' }).setOrigin(0.5);
    const fp = new StatBar(this, 150, 106, 'FP', COLORS.fp, 170);
    fp.set(this.bars(p).fp, p.fp);
    const tp = new StatBar(this, 150, 132, 'TP', COLORS.tp, 170);
    tp.set(this.bars(p).tp, p.tp);
    const ov = display(this, W - 20, 116, String(playerOverall(p)), 46, THEME.yellowCss, { strokeThickness: 0 }).setOrigin(1, 0.5);
    const ovL = label(this, W - 20, 146, 'MEDIA', 12, THEME.muted, { fontStyle: 'bold' }).setOrigin(1, 0.5);
    const close = new Button(this, W - 38, 34, '✕', () => this.closeSheet(), { w: 56, h: 52, variant: 'secondary', size: 22 });
    c.add([g, block, number, portrait, name, tags, posT, elT, lvT, fp, tp, ov, ovL, close]);

    // atributos
    c.add(sectionTitle(this, 16, 180, 'Atributos'));
    STAT_LABELS.forEach(([key, lbl], i) => {
      const y = 210 + i * 29;
      const v = p.stats[key];
      const bar = this.add.graphics();
      bar.fillStyle(0x000000, 0.45).fillRoundedRect(116, y - 5, W - 190, 10, 5);
      bar.fillStyle(v >= 75 ? THEME.yellow : THEME.glow).fillRoundedRect(116, y - 5, Phaser.Math.Clamp(v / 99, 0.05, 1) * (W - 190), 10, 5);
      c.add([bar, label(this, 20, y, lbl, 18, THEME.muted, { fontStyle: 'italic' }).setOrigin(0, 0.5), label(this, W - 20, y, String(v), 19, THEME.text, { fontStyle: 'bold' }).setOrigin(1, 0.5)]);
    });

    // supertécnicas
    c.add(sectionTitle(this, 16, 422, 'Supertécnicas'));
    const moves = movesOf(p.moves);
    if (moves.length === 0) c.add(label(this, 34, 452, '—', 18));
    moves.slice(0, 6).forEach((m, i) => {
      const y = 442 + i * 38;
      const row = this.add.graphics();
      row.fillStyle(0x000000, i % 2 ? 0.15 : 0.3).fillRoundedRect(16, y, W - 32, 34, 6);
      row.fillStyle(ELEMENT_COLOR[m.element]).fillRoundedRect(16, y, 6, 34, 3);
      const mn = label(this, 32, y + 17, m.name, 18, THEME.text, { fontStyle: 'bold' }).setOrigin(0, 0.5);
      fitWidth(mn, W - 32 - 200, 13);
      c.add([row, mn, label(this, W - 26, y + 17, `${MOVE_KIND_LABEL[m.kind]} · ${m.power} · TP ${m.tp}`, 15, THEME.muted).setOrigin(1, 0.5)]);
    });

    // descripción
    const dy = 442 + Math.max(1, Math.min(6, moves.length)) * 38 + 10;
    const dh = H - dy - 14;
    if (dh > 30) {
      const desc = label(this, 32, dy + 12, p.description ?? `Jugador de ${team.name}.`, 17, THEME.text, { fontStyle: 'italic', wordWrap: { width: W - 64 }, lineSpacing: 3 });
      const bh = Math.min(dh, desc.height + 24);
      const dg = this.add.graphics();
      dg.fillStyle(0x000000, 0.3).fillRoundedRect(16, dy, W - 32, bh, 8);
      dg.fillStyle(accent).fillRoundedRect(16, dy, 4, bh, 2);
      c.add([dg, desc]);
    }
    c.y = GAME_H;
    shade.setAlpha(0);
    this.tweens.add({ targets: c, y: top, duration: 220, ease: 'Cubic.Out' });
    this.tweens.add({ targets: shade, alpha: 1, duration: 220 });
  }

  private closeSheet(): void {
    this.sheet?.destroy();
    this.sheet = null;
  }

  /** Filas de la lista de formaciones que caben en la pantalla del móvil. */
  private portraitListRows(): number {
    return 9;
  }

  /** Lista de formaciones a pantalla completa: filtros arriba, filas grandes con su mini campo y páginas abajo. */
  private drawFormationListPortrait(): void {
    this.formationList?.destroy();
    // por encima de la barra de arriba (profundidad 100): ocupa toda la pantalla
    const c = this.add.container(0, 0).setDepth(150);
    this.formationList = c;
    const back = this.add.rectangle(GAME_W / 2, GAME_H / 2, GAME_W, GAME_H, THEME.night, 0.98).setInteractive();
    c.add(back);
    c.add(display(this, 18, 34, 'Formaciones', 34, THEME.yellowCss).setOrigin(0, 0.5));
    const avail = availableFormations(this.home.teamId);
    const won = FORMATIONS.filter((f) => !f.generic && avail.has(f.id)).length;
    const total = FORMATIONS.filter((f) => !f.generic).length;
    c.add(label(this, 18, 66, `${won} de ${total} conseguidas · una más con cada victoria`, 15, THEME.text, { fontStyle: 'bold' }).setOrigin(0, 0.5));
    c.add(new Button(this, GAME_W - 42, 38, '✕', () => this.closeFormationList(), { w: 60, h: 56, variant: 'secondary', size: 24 }));

    // filtros por distribución, en varias filas
    const filters = ['all', ...this.formationFilters(), 'other'];
    let fx = 14;
    let fy = 108;
    for (const id of filters) {
      const on = this.formationFilter === id;
      const n = id === 'all' ? FORMATIONS.length : id === 'other' ? FORMATIONS.filter((f) => !filters.includes(f.layout)).length : FORMATIONS.filter((f) => f.layout === id).length;
      const t = `${id === 'all' ? 'Todas' : id === 'other' ? 'Otras' : id} ${n}`;
      const ch = chip(this, fx, fy, t, on ? THEME.yellow : THEME.panelLight, { size: 16, h: 38, padX: 12, textColor: on ? THEME.ink : THEME.text });
      if (fx + ch.width > GAME_W - 14) {
        fx = 14;
        fy += 46;
        ch.setPosition(fx, fy);
      }
      const hit = this.add.zone(fx, fy - 19, ch.width, 38).setOrigin(0).setInteractive();
      hit.on('pointerdown', () => {
        this.formationFilter = id;
        this.formationPage = 0;
        this.drawFormationList();
      });
      c.add([ch, hit]);
      fx += ch.width + 8;
    }

    const list = this.filteredFormations();
    const per = this.portraitListRows();
    const pages = Math.max(1, Math.ceil(list.length / per));
    this.formationPage = Math.min(this.formationPage, pages - 1);
    const shown = list.slice(this.formationPage * per, (this.formationPage + 1) * per);
    const top = fy + 32;
    const bottom = GAME_H - 96;
    const rh = Math.min(72, (bottom - top) / per);
    const cw = GAME_W - 28;
    const cur = getFormation(this.home.formationId).id;
    shown.forEach((f, i) => {
      const cx = 14;
      const cy = top + i * rh;
      const current = f.id === cur;
      const locked = !avail.has(f.id) && !current;
      const bg = this.add.graphics();
      bg.fillStyle(current ? THEME.yellow : 0x14223a, current ? 0.95 : locked ? 0.4 : 0.8).fillRoundedRect(cx, cy + 3, cw, rh - 6, 10);
      // mini campo: portería propia abajo, ataque hacia arriba (como el campo grande)
      const mw = 44;
      const mh = rh - 14;
      const mx = cx + 8;
      const my = cy + 7;
      const m = this.add.graphics();
      m.fillStyle(0x2f7d3e, 1).fillRoundedRect(mx, my, mw, mh, 4);
      m.lineStyle(1, 0xffffff, 0.35).lineBetween(mx + 2, my + mh / 2, mx + mw - 2, my + mh / 2);
      for (const sl of f.slots) {
        const col = sl.pos === 'GK' ? 0xffffff : sl.pos === 'DF' ? 0x4f9bff : sl.pos === 'MF' ? 0xffb02e : 0xff5050;
        m.fillStyle(col, 1).fillCircle(mx + 4 + sl.x * (mw - 8), my + 4 + sl.y * (mh - 8), 2.4);
      }
      if (locked) m.setAlpha(0.35);
      const ink = current ? THEME.ink : locked ? THEME.muted : THEME.text;
      const name = label(this, cx + 66, cy + rh / 2 - (f.also?.length ? 9 : 0), locked ? `🔒 ${f.name}` : f.name, 19, ink, { fontStyle: 'italic bold' }).setOrigin(0, 0.5);
      fitWidth(name, cw - 66 - 80, 13);
      const parts: Phaser.GameObjects.GameObject[] = [bg, m, name];
      if (f.also?.length) {
        const al = label(this, cx + 66, cy + rh / 2 + 13, `= ${f.also.join(', ')}`, 13, current ? THEME.ink : THEME.muted, { fontStyle: 'italic' }).setOrigin(0, 0.5);
        fitWidth(al, cw - 66 - 80, 10);
        parts.push(al);
      }
      parts.push(label(this, cx + cw - 14, cy + rh / 2, f.layout, 18, current ? THEME.ink : '#9fb8d8', { fontStyle: 'bold' }).setOrigin(1, 0.5));
      const hit = this.add.zone(cx, cy, cw, rh).setOrigin(0).setInteractive();
      hit.on('pointerdown', () => {
        if (locked) return toast(this, 'Aún no la tienes: se consiguen ganando partidos', THEME.panelLight);
        this.closeFormationList();
        this.setFormation(f.id);
      });
      parts.push(hit);
      c.add(parts);
    });
    const py = GAME_H - 48;
    if (pages > 1) {
      c.add(new Button(this, 70, py, '◀', () => ((this.formationPage = (this.formationPage + pages - 1) % pages), this.drawFormationList()), { w: 112, h: 64, variant: 'secondary', size: 24 }));
      c.add(label(this, GAME_W / 2, py, `${this.formationPage + 1} / ${pages}`, 22, THEME.text, { fontStyle: 'bold' }).setOrigin(0.5));
      c.add(new Button(this, GAME_W - 70, py, '▶', () => ((this.formationPage = (this.formationPage + 1) % pages), this.drawFormationList()), { w: 112, h: 64, variant: 'secondary', size: 24 }));
    }
  }

  private play(): void {
    if (this.halftime) {
      const done = this.halftime.onDone;
      this.scene.stop();
      done(this.home);
      return;
    }
    // "Mi club" recuerda la alineación y la formación
    const save = this.home.teamId === 'club' ? loadClub() : null;
    if (save) {
      const byId = new Map(getTeam('club').players.map((p) => [p.id, `${p.origin}:${p.originId}`]));
      setSquad(save, this.home.order.map((id) => byId.get(id)!).filter(Boolean), this.home.formationId);
      this.home = { ...this.home, order: getTeam('club').players.map((p) => p.id) };
    }
    this.scene.start('match', { home: this.home, away: this.away });
  }
}
