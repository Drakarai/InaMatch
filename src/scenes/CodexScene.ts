import Phaser from 'phaser';
import { music } from '../audio/music';
import { sfx } from '../audio/sfx';
import { loadClub } from '../club/club';
import { loadPool, RARITY, type Card } from '../club/pool';
import { UNIFORMS } from '../club/uniforms';
import { filterCards, filterMoves, KIND_LABEL, paginate, progressLabel, type CardFilter } from '../codex/codex';
import { GAME_H, GAME_W, PORTRAIT } from '../config';
import { getTeam, MOVES } from '../data';
import { ELEMENT_COLOR, ELEMENT_LABEL } from '../data/elements';
import { SEASONS } from '../data/seasons';
import type { MoveKind, Position, Stats } from '../data/types';
import { drawCard, loadCardPortraits } from '../ui/card';
import { kitIcon } from '../ui/kitIcon';
import { THEME, cardPanel, fitCamera, stadiumBackdrop, topBar } from '../ui/theme';
import { Button, fitWidth, label } from '../ui/widgets';

type Tab = 'players' | 'moves' | 'uniforms';

const STAT_LABEL: [keyof Stats, string][] = [
  ['kick', 'Tiro'],
  ['body', 'Físico'],
  ['control', 'Control'],
  ['guard', 'Defensa'],
  ['speed', 'Rapidez'],
  ['stamina', 'Aguante'],
  ['guts', 'Valor'],
];
const POS_NAME: Record<Position, string> = { GK: 'Portero', DF: 'Defensa', MF: 'Centrocampista', FW: 'Delantero' };
const CODEX_SEASONS = SEASONS.filter((s) => s.id !== 'club' && s.id !== 'otros');
const KINDS: (MoveKind | 'all')[] = ['all', 'shoot', 'dribble', 'block', 'catch'];

/**
 * Enciclopedia: todos los jugadores que se pueden fichar (con su ficha), todas las supertécnicas y todos los uniformes.
 * Lo conseguido en Mi club sale marcado; el resto también se puede consultar.
 */
export class CodexScene extends Phaser.Scene {
  private tab: Tab = 'players';
  private page = 0;
  private filter: CardFilter = { season: 'all', position: 'all', ownedOnly: false };
  private kind: MoveKind | 'all' = 'all';
  private movesOwnedOnly = false;
  private pool: Card[] = [];
  private view!: Phaser.GameObjects.Container;
  private modal: Phaser.GameObjects.Container | null = null;
  private owned = new Set<string>();
  private notebooks: Record<string, number> = {};
  private uniformsOwned = new Set<string>();
  private pages = 1;

  constructor() {
    super('codex');
  }

  create(): void {
    fitCamera(this);
    music.play('menu');
    stadiumBackdrop(this, THEME.home, THEME.cyan);
    this.modal = null;
    const save = loadClub();
    this.owned = new Set(save?.owned ?? []);
    this.notebooks = save?.notebooks ?? {};
    this.uniformsOwned = new Set(save?.uniforms ?? []);
    this.view = this.add.container(0, 0);
    const wait = label(this, GAME_W / 2, GAME_H / 2, 'Cargando enciclopedia…', 18, '#ffffff').setOrigin(0.5);
    loadPool()
      .then((pool) => {
        wait.destroy();
        this.pool = pool;
        this.render();
      })
      .catch(() => wait.setText('No se ha podido cargar la enciclopedia'));
    const kb = this.input.keyboard;
    kb?.on('keydown-ESC', () => (this.modal ? this.closeModal() : this.scene.start('title')));
    kb?.on('keydown-LEFT', () => !this.modal && this.goPage(this.page - 1));
    kb?.on('keydown-RIGHT', () => !this.modal && this.goPage(this.page + 1));
  }

  private goPage(p: number): void {
    if (p < 0 || p >= this.pages || p === this.page) return;
    this.page = p;
    sfx.click();
    this.render();
  }

  private render(): void {
    const c = this.view.removeAll(true);
    const totalOwned = this.pool.filter((x) => this.owned.has(x.key)).length;
    c.add(
      topBar(this, {
        title: 'Enciclopedia',
        subtitle: `Jugadores ${progressLabel(totalOwned, this.pool.length)}  ·  Uniformes ${this.uniformsOwned.size}/${UNIFORMS.length}`,
        back: { label: 'Inicio', onClick: () => this.scene.start('title') },
      }),
    );
    // pestañas
    const tabs: [Tab, string][] = [
      ['players', 'Jugadores'],
      ['moves', 'Supertécnicas'],
      ['uniforms', 'Uniformes'],
    ];
    const tw = PORTRAIT ? (GAME_W - 40) / 3 : 200;
    tabs.forEach(([id, name], i) => {
      const x = GAME_W / 2 + (i - 1) * (tw + 10);
      const b = new Button(this, x, PORTRAIT ? 98 : 96, name, () => {
        if (this.tab === id) return;
        this.tab = id;
        this.page = 0;
        this.render();
      }, { w: tw, h: 40, size: 17, variant: this.tab === id ? 'primary' : 'secondary' });
      c.add(b);
    });
    if (this.tab === 'players') this.renderPlayers(c);
    else if (this.tab === 'moves') this.renderMoves(c);
    else this.renderUniforms(c);
  }

  /** Fila de botones pequeños para filtrar; devuelve el ancho usado. */
  private chips<T extends string>(c: Phaser.GameObjects.Container, x: number, y: number, items: { id: T; text: string }[], current: T, w: number, onPick: (id: T) => void): number {
    items.forEach((it, i) => {
      const b = new Button(this, x + i * (w + 4) + w / 2, y, it.text, () => onPick(it.id), { w, h: 32, size: 13, variant: it.id === current ? 'primary' : 'secondary' });
      c.add(b);
    });
    return items.length * (w + 4);
  }

  private pager(c: Phaser.GameObjects.Container, page: number, pages: number, count: number): void {
    this.pages = pages;
    const y = GAME_H - (PORTRAIT ? 40 : 30);
    c.add(label(this, GAME_W / 2, y, `Página ${page + 1} de ${pages}  ·  ${count} en total`, 15, '#ffffff', { fontStyle: 'bold' }).setOrigin(0.5));
    const prev = new Button(this, GAME_W / 2 - (PORTRAIT ? 190 : 210), y, '◀', () => this.goPage(page - 1), { w: PORTRAIT ? 80 : 70, h: 40, size: 18 });
    const next = new Button(this, GAME_W / 2 + (PORTRAIT ? 190 : 210), y, '▶', () => this.goPage(page + 1), { w: PORTRAIT ? 80 : 70, h: 40, size: 18 });
    prev.setEnabled(page > 0);
    next.setEnabled(page < pages - 1);
    c.add([prev, next]);
  }

  // ------------------------------------------------------------- jugadores

  private renderPlayers(c: Phaser.GameObjects.Container): void {
    const seasons = [{ id: 'all', text: 'Todas' }, ...CODEX_SEASONS.map((s) => ({ id: s.id, text: s.short }))];
    const positions: { id: Position | 'all'; text: string }[] = [
      { id: 'all', text: 'Todos' },
      { id: 'GK', text: 'POR' },
      { id: 'DF', text: 'DEF' },
      { id: 'MF', text: 'MED' },
      { id: 'FW', text: 'DEL' },
    ];
    const set = (patch: Partial<CardFilter>) => {
      this.filter = { ...this.filter, ...patch };
      this.page = 0;
      this.render();
    };
    if (PORTRAIT) {
      const sw = (GAME_W - 24 - 4 * (seasons.length - 1)) / seasons.length;
      this.chips(c, 12, 144, seasons, this.filter.season, sw, (id) => set({ season: id }));
      const used = this.chips(c, 12, 182, positions, this.filter.position, 62, (id) => set({ position: id }));
      c.add(new Button(this, 12 + used + 90, 182, this.filter.ownedOnly ? '✓ Conseguidos' : 'Conseguidos', () => set({ ownedOnly: !this.filter.ownedOnly }), { w: 170, h: 32, size: 13, variant: this.filter.ownedOnly ? 'accent' : 'secondary' }));
    } else {
      let x = 24;
      x += this.chips(c, x, 144, seasons, this.filter.season, 64, (id) => set({ season: id })) + 14;
      x += this.chips(c, x, 144, positions, this.filter.position, 56, (id) => set({ position: id })) + 14;
      c.add(new Button(this, x + 70, 144, this.filter.ownedOnly ? '✓ Conseguidos' : 'Conseguidos', () => set({ ownedOnly: !this.filter.ownedOnly }), { w: 140, h: 32, size: 13, variant: this.filter.ownedOnly ? 'accent' : 'secondary' }));
    }
    const list = filterCards(this.pool, this.filter, this.owned);
    const cols = PORTRAIT ? 3 : 8;
    const rows = PORTRAIT ? 3 : 2;
    const { items, page, pages } = paginate(list, this.page, cols * rows);
    this.page = page;
    this.pager(c, page, pages, list.length);
    if (!items.length) {
      c.add(label(this, GAME_W / 2, GAME_H / 2, this.filter.ownedOnly ? 'Aún no tienes jugadores de este filtro. ¡Consíguelos en Fichajes!' : 'No hay jugadores con este filtro.', 17, '#ffffff', { align: 'center', wordWrap: { width: GAME_W - 60 } }).setOrigin(0.5));
      return;
    }
    const cw = PORTRAIT ? 150 : 132;
    const ch = PORTRAIT ? 200 : 180;
    const top = PORTRAIT ? 216 : 176;
    const gapX = (GAME_W - cols * cw) / (cols + 1);
    const gapY = PORTRAIT ? 18 : 22;
    const grid = this.add.container(0, 0);
    c.add(grid);
    const draw = () => {
      if (!grid.active) return;
      items.forEach((card, i) => {
        const x = gapX + (i % cols) * (cw + gapX) + cw / 2;
        const y = top + Math.floor(i / cols) * (ch + gapY) + ch / 2;
        const cardObj = drawCard(this, x, y, card, cw, ch);
        const have = this.owned.has(card.key);
        if (!have) cardObj.setAlpha(0.72);
        grid.add(cardObj);
        if (have) grid.add(label(this, x + cw / 2 - 10, y + ch / 2 - 12, '✓', 18, '#7dff9a', { fontStyle: 'bold', stroke: '#000000', strokeThickness: 4 }).setOrigin(0.5));
        const hit = this.add.zone(x, y, cw, ch).setInteractive({ useHandCursor: true });
        hit.on('pointerup', () => this.showPlayer(card));
        grid.add(hit);
      });
    };
    const loading = label(this, GAME_W / 2, top + 140, 'Cargando retratos…', 15, THEME.muted).setOrigin(0.5);
    c.add(loading);
    loadCardPortraits(this, items, () => {
      loading.destroy();
      draw();
    });
  }

  private closeModal(): void {
    this.modal?.destroy();
    this.modal = null;
  }

  private showPlayer(card: Card): void {
    sfx.click();
    // el retrato puede no estar cargado (la ficha se abre también desde fuera de la página)
    loadCardPortraits(this, [card], () => this.scene.isActive() && this.drawPlayer(card));
  }

  private drawPlayer(card: Card): void {
    this.closeModal();
    const p = card.player;
    const c = this.add.container(0, 0).setDepth(300);
    this.modal = c;
    const shade = this.add.rectangle(0, 0, GAME_W, GAME_H, 0x000000, 0.75).setOrigin(0).setInteractive();
    shade.on('pointerup', () => this.closeModal());
    c.add(shade);
    const W = PORTRAIT ? GAME_W - 24 : 900;
    const H = PORTRAIT ? GAME_H - 60 : 600;
    const x0 = (GAME_W - W) / 2;
    const y0 = (GAME_H - H) / 2;
    const g = this.add.graphics();
    cardPanel(g, x0, y0, W, H, { accent: RARITY[card.rarity].color, alpha: 0.98 });
    c.add(g);
    c.add(this.add.zone(x0, y0, W, H).setOrigin(0).setInteractive());
    let teamLabel = 'Ojeador';
    if (!card.origin.startsWith('scouts-')) {
      try {
        teamLabel = getTeam(card.origin).name;
      } catch {
        teamLabel = card.origin;
      }
    }
    const season = SEASONS.find((s) => s.id === card.season)?.name ?? '';
    // carta y datos
    const cardX = x0 + (PORTRAIT ? 100 : 130);
    const cardY = y0 + (PORTRAIT ? 140 : 170);
    c.add(drawCard(this, cardX, cardY, card, PORTRAIT ? 160 : 200, PORTRAIT ? 220 : 270));
    const ix = x0 + (PORTRAIT ? 200 : 260);
    const iw = W - (ix - x0) - 24;
    c.add(fitWidth(label(this, ix, y0 + 40, p.name, PORTRAIT ? 24 : 30, '#ffffff', { fontStyle: 'bold italic' }).setOrigin(0, 0.5), iw, 14));
    const info: [string, string][] = [
      ['Equipo', teamLabel],
      ['Juego', season],
      ['Demarcación', POS_NAME[p.position]],
      ['Afinidad', ELEMENT_LABEL[p.element]],
      ['FP / TP', `${p.fp} / ${p.tp}`],
      ['En Mi club', this.owned.has(card.key) ? '✓ Conseguido' : 'No conseguido'],
    ];
    info.forEach(([k, v], i) => {
      const y = y0 + (PORTRAIT ? 76 : 84) + i * (PORTRAIT ? 30 : 34);
      c.add(label(this, ix, y, k, PORTRAIT ? 13 : 15, THEME.muted).setOrigin(0, 0.5));
      c.add(fitWidth(label(this, ix + (PORTRAIT ? 100 : 130), y, v, PORTRAIT ? 14 : 16, k === 'En Mi club' && this.owned.has(card.key) ? '#7dff9a' : '#ffffff', { fontStyle: 'bold' }).setOrigin(0, 0.5), iw - (PORTRAIT ? 100 : 130), 10));
    });
    c.add(this.add.circle(ix + (PORTRAIT ? 92 : 122), y0 + (PORTRAIT ? 76 : 84) + 3 * (PORTRAIT ? 30 : 34), 6, ELEMENT_COLOR[p.element]).setStrokeStyle(2, 0xffffff));
    // estadísticas
    const sy = y0 + (PORTRAIT ? 290 : 330);
    const colW = PORTRAIT ? (W - 48) / 2 : (W - 60) / 4;
    const perRow = PORTRAIT ? 2 : 4;
    STAT_LABEL.forEach(([k, lbl], i) => {
      const x = x0 + 24 + (i % perRow) * colW;
      const y = sy + Math.floor(i / perRow) * 34;
      const v = p.stats[k];
      const bw = colW - 120;
      const bar = this.add.graphics();
      bar.fillStyle(0x000000, 0.45).fillRoundedRect(x + 72, y - 5, bw, 10, 5);
      bar.fillStyle(v >= 75 ? THEME.yellow : THEME.glow).fillRoundedRect(x + 72, y - 5, Math.max(8, (bw * v) / 99), 10, 5);
      c.add(bar);
      c.add(label(this, x, y, lbl, 14, THEME.muted).setOrigin(0, 0.5));
      c.add(label(this, x + 72 + bw + 30, y, String(v), 16, '#ffffff', { fontStyle: 'bold' }).setOrigin(1, 0.5));
    });
    // supertécnicas
    const my = sy + Math.ceil(STAT_LABEL.length / perRow) * 34 + 12;
    c.add(label(this, x0 + 24, my, 'SUPERTÉCNICAS', 14, THEME.yellowCss, { fontStyle: 'bold' }).setOrigin(0, 0.5));
    const moves = p.moves.map((id) => MOVES[id]).filter(Boolean);
    if (!moves.length) c.add(label(this, x0 + 24, my + 30, 'Ninguna', 15, THEME.muted, { fontStyle: 'italic' }).setOrigin(0, 0.5));
    const mCols = PORTRAIT ? 2 : 3;
    const mw = (W - 48) / mCols;
    moves.forEach((m, i) => {
      const x = x0 + 24 + (i % mCols) * mw;
      const y = my + 30 + Math.floor(i / mCols) * 30;
      c.add(this.add.graphics().fillStyle(ELEMENT_COLOR[m.element]).fillRoundedRect(x, y - 10, 5, 20, 2));
      c.add(fitWidth(label(this, x + 12, y, `${m.name}  ·  ${KIND_LABEL[m.kind]} ${m.power}`, 14, '#ffffff', { fontStyle: 'bold' }).setOrigin(0, 0.5), mw - 20, 10));
    });
    const dy = my + 30 + Math.ceil(moves.length / mCols) * 30 + 8;
    if (p.description && dy < y0 + H - 80) {
      c.add(label(this, x0 + 24, dy, p.description, PORTRAIT ? 13 : 14, '#c9d6ec', { fontStyle: 'italic', wordWrap: { width: W - 48 }, lineSpacing: 3, maxLines: PORTRAIT ? 6 : 3 }).setOrigin(0, 0));
    }
    c.add(new Button(this, GAME_W / 2, y0 + H - 34, 'Cerrar', () => this.closeModal(), { w: 180, h: 44, size: 17, variant: 'secondary' }));
  }

  // ------------------------------------------------------------- técnicas

  private renderMoves(c: Phaser.GameObjects.Container): void {
    const all = Object.values(MOVES);
    const items = KINDS.map((k) => ({ id: k, text: k === 'all' ? 'Todas' : KIND_LABEL[k] }));
    const used = this.chips(c, PORTRAIT ? 12 : 24, 144, items, this.kind, PORTRAIT ? 74 : 90, (id) => {
      this.kind = id;
      this.page = 0;
      this.render();
    });
    const have = all.filter((m) => (this.notebooks[m.id] ?? 0) > 0).length;
    const toggleX = PORTRAIT ? GAME_W - 12 - 75 : (PORTRAIT ? 12 : 24) + used + 90;
    c.add(
      new Button(this, toggleX, PORTRAIT ? 184 : 144, this.movesOwnedOnly ? '✓ Con cuaderno' : 'Con cuaderno', () => {
        this.movesOwnedOnly = !this.movesOwnedOnly;
        this.page = 0;
        this.render();
      }, { w: 150, h: 32, size: 13, variant: this.movesOwnedOnly ? 'accent' : 'secondary' }),
    );
    c.add(label(this, PORTRAIT ? 12 : GAME_W - 24, PORTRAIT ? 184 : 144, `Cuadernos: ${progressLabel(have, all.length)}`, 13, THEME.muted, { fontStyle: 'italic' }).setOrigin(PORTRAIT ? 0 : 1, 0.5));
    const list = filterMoves(all, this.kind, this.movesOwnedOnly, this.notebooks);
    const cols = PORTRAIT ? 1 : 2;
    const rows = PORTRAIT ? 12 : 10;
    const { items: page, page: p, pages } = paginate(list, this.page, cols * rows);
    this.page = p;
    this.pager(c, p, pages, list.length);
    if (!page.length) {
      c.add(label(this, GAME_W / 2, GAME_H / 2, 'No hay supertécnicas con este filtro.', 17, '#ffffff').setOrigin(0.5));
      return;
    }
    const top = PORTRAIT ? 214 : 178;
    const rowH = PORTRAIT ? 54 : 48;
    const colW = (GAME_W - 48 - (cols - 1) * 20) / cols;
    page.forEach((m, i) => {
      const x = 24 + Math.floor(i / rows) * (colW + 20);
      const y = top + (i % rows) * rowH;
      const g = this.add.graphics();
      g.fillStyle(0x0b1a2e, 0.9).fillRoundedRect(x, y, colW, rowH - 6, 8);
      g.fillStyle(ELEMENT_COLOR[m.element]).fillRoundedRect(x, y, 6, rowH - 6, { tl: 8, bl: 8, tr: 0, br: 0 });
      c.add(g);
      const n = this.notebooks[m.id] ?? 0;
      const mid = y + (rowH - 6) / 2;
      c.add(fitWidth(label(this, x + 18, mid - (PORTRAIT ? 8 : 0), m.name, 16, '#ffffff', { fontStyle: 'bold' }).setOrigin(0, 0.5), colW * (PORTRAIT ? 0.9 : 0.42), 11));
      const meta = `${KIND_LABEL[m.kind]} · ${ELEMENT_LABEL[m.element]}`;
      if (PORTRAIT) c.add(label(this, x + 18, mid + 11, meta, 12, THEME.muted).setOrigin(0, 0.5));
      else c.add(label(this, x + colW * 0.47, mid, meta, 13, THEME.muted).setOrigin(0, 0.5));
      c.add(label(this, x + colW - (PORTRAIT ? 100 : 150), mid, `⚡${m.power}`, 15, '#ffd23f', { fontStyle: 'bold' }).setOrigin(0.5));
      c.add(label(this, x + colW - (PORTRAIT ? 50 : 96), mid, `${m.tp} TP`, 13, '#7dff9a').setOrigin(0.5));
      if (!PORTRAIT || n) c.add(label(this, x + colW - 14, mid, n ? `📒×${n}` : '—', 13, n ? '#ffffff' : THEME.muted).setOrigin(1, 0.5));
    });
  }

  // ------------------------------------------------------------- uniformes

  private renderUniforms(c: Phaser.GameObjects.Container): void {
    c.add(label(this, GAME_W / 2, 144, `Conseguidos en Mi club: ${progressLabel(this.uniformsOwned.size, UNIFORMS.length)}  ·  se ganan al vencer con tu club`, 14, THEME.muted, { fontStyle: 'italic', align: 'center', wordWrap: { width: GAME_W - 40 } }).setOrigin(0.5));
    const list = [...UNIFORMS].sort((a, b) => Number(this.uniformsOwned.has(b.id)) - Number(this.uniformsOwned.has(a.id)));
    const cols = PORTRAIT ? 3 : 6;
    const rows = PORTRAIT ? 4 : 3;
    const { items, page, pages } = paginate(list, this.page, cols * rows);
    this.page = page;
    this.pager(c, page, pages, list.length);
    const top = PORTRAIT ? 176 : 172;
    const cw = (GAME_W - 40) / cols;
    const ch = PORTRAIT ? 172 : 156;
    items.forEach((u, i) => {
      const x = 20 + (i % cols) * cw + cw / 2;
      const y = top + Math.floor(i / cols) * ch + ch / 2;
      const have = this.uniformsOwned.has(u.id);
      const g = this.add.graphics();
      g.fillStyle(0x0b1a2e, 0.9).fillRoundedRect(x - cw / 2 + 6, y - ch / 2 + 4, cw - 12, ch - 8, 12);
      g.lineStyle(2, have ? THEME.green : 0xffffff, have ? 0.8 : 0.12).strokeRoundedRect(x - cw / 2 + 6, y - ch / 2 + 4, cw - 12, ch - 8, 12);
      c.add(g);
      const k = kitIcon(this, x, y - 14, u.colors, PORTRAIT ? 90 : 84, true);
      if (!have) k.setAlpha(0.55);
      c.add(k);
      c.add(fitWidth(label(this, x, y + ch / 2 - 30, u.name, 13, '#ffffff', { fontStyle: 'bold', align: 'center' }).setOrigin(0.5), cw - 22, 9));
      c.add(label(this, x, y + ch / 2 - 14, have ? '✓ Conseguido' : 'Sin conseguir', 11, have ? '#7dff9a' : THEME.muted, { fontStyle: 'italic' }).setOrigin(0.5));
    });
  }
}
