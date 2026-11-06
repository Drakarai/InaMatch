import Phaser from 'phaser';
import { music } from '../audio/music';
import { autoSquad, BASE_SLOTS, cardOverall, freeNotebooks, loadClub, movesFor, notebookRarity, onClubChange, setCrest, setMoves, setSquad, type ClubSave } from '../club/club';
import { applyClubCrest, crestById, crestKey, CRESTS, loadCrests } from '../club/crests';
import { ELEMENT_COLOR } from '../data/elements';
import type { MoveKind } from '../data/types';
import { KIND_LABEL } from '../ui/notebook';
import { cardByKey, RARITY, type Card, type Rarity } from '../club/pool';
import { GAME_H, GAME_W } from '../config';
import { getTeam, MOVES } from '../data';
import { getFormation } from '../data/formations';
import type { Position } from '../data/types';
import { teamRating } from '../engine/rating';
import { portraitKey } from '../gfx/placeholders';
import { cardPlayer, drawCard, loadCardPortraits } from '../ui/card';
import { POS_COLOR, THEME, cardPanel, chip, coinChip, fitCamera, sectionTitle, stadiumBackdrop, toast, topBar } from '../ui/theme';
import { Button, display, fitWidth, label, text } from '../ui/widgets';

const SQUAD = { x: 24, y: 84, w: 470, h: 624 };
const COLL = { x: 512, y: 84, w: 744, h: 426 };
const INFO = { x: 512, y: 522, w: 744, h: 186 };
const PER_PAGE = 10;
const CREST_PER_PAGE = 24;
const ROW_H = 31;
const FILTERS: ('ALL' | Position)[] = ['ALL', 'GK', 'DF', 'MF', 'FW'];
const STAT_LABEL: [keyof Card['player']['stats'], string][] = [
  ['kick', 'Tiro'],
  ['body', 'Físico'],
  ['control', 'Control'],
  ['guard', 'Defensa'],
  ['speed', 'Rapidez'],
  ['stamina', 'Aguante'],
  ['guts', 'Valor'],
];

/**
 * Mi club: la plantilla (16: 11 titulares y 5 en el banquillo) y la colección de jugadores conseguidos.
 * Pulsa un hueco de la plantilla y luego un jugador de la colección para ponerlo ahí; dos huecos, para cambiarlos.
 */
export class ClubScene extends Phaser.Scene {
  private save!: ClubSave;
  private selected: number | null = null;
  private filter: (typeof FILTERS)[number] = 'ALL';
  private rarityFilter: Rarity | 0 = 0;
  private page = 0;
  private squadBox!: Phaser.GameObjects.Container;
  private collBox!: Phaser.GameObjects.Container;
  private infoBox!: Phaser.GameObjects.Container;
  private header!: Phaser.GameObjects.Container;

  constructor() {
    super('club');
  }

  create(): void {
    fitCamera(this);
    music.play('menu');
    this.save = loadClub()!;
    this.selected = null;
    this.page = 0;
    stadiumBackdrop(this, THEME.yellow, THEME.orange);
    this.header = this.add.container(0, 0).setDepth(100);
    this.squadBox = this.add.container(0, 0);
    this.collBox = this.add.container(0, 0);
    this.infoBox = this.add.container(0, 0);
    const off = onClubChange(() => {
      this.save = loadClub()!;
      this.redraw();
    });
    this.events.once(Phaser.Scenes.Events.SHUTDOWN, off);
    this.input.keyboard?.on('keydown-ESC', () => (this.crestBox ? this.closeCrests() : this.editor ? this.closeEditor() : this.scene.start('menu')));
    const keys = [...this.save.squad, ...this.collection().slice(0, PER_PAGE).map((c) => c.key)];
    loadCardPortraits(this, keys.map((k) => cardByKey(k)).filter((c): c is Card => !!c), () => this.redraw());
    this.redraw();
  }

  private play(): void {
    const sel = (this.registry.get('menuSelection') as { home: string; away: string; focus: string } | undefined) ?? { home: 'club', away: 'ie3-desert-lion', focus: 'away' };
    this.registry.set('menuSelection', { ...sel, home: 'club', away: sel.away === 'club' ? 'ie3-desert-lion' : sel.away, focus: 'away' });
    this.scene.start('menu');
  }

  private collection(): Card[] {
    const cards = this.save.owned.map((k) => cardByKey(k)).filter((c): c is Card => !!c);
    const order: Record<Position, number> = { GK: 0, DF: 1, MF: 2, FW: 3 };
    return cards
      .filter((c) => this.filter === 'ALL' || c.player.position === this.filter)
      .filter((c) => !this.rarityFilter || c.rarity === this.rarityFilter)
      .sort((a, b) => b.rarity - a.rarity || order[a.player.position] - order[b.player.position] || cardOverall(b.player) - cardOverall(a.player));
  }

  private redraw(): void {
    this.drawHeader();
    this.drawSquad();
    this.drawCollection();
  }

  private drawHeader(): void {
    const c = this.header;
    c.removeAll(true);
    let rating = 0;
    try {
      rating = teamRating(getTeam('club'));
    } catch {
      // aún sin equipo
    }
    c.add(topBar(this, { title: this.save.name, subtitle: `Media ${rating}  ·  ${this.save.owned.length} jugadores  ·  ${this.save.pulls} tiradas`, back: { label: 'Menú', onClick: () => this.scene.start('menu') }, icon: 'emblem:club' }));
    c.add(coinChip(this, GAME_W - 24, 32, this.save.coins));
    c.add(new Button(this, GAME_W - 200, 32, '¡A jugar!', () => this.play(), { w: 130, h: 38, variant: 'primary', size: 16 }));
    c.add(new Button(this, GAME_W - 340, 32, 'Fichajes', () => this.scene.start('gacha', { from: 'club' }), { w: 120, h: 38, color: THEME.orange, size: 15 }));
    c.add(new Button(this, GAME_W - 610, 32, 'Escudo', () => this.openCrests(), { w: 110, h: 38, color: 0x2f7bff, size: 15 }));
    c.add(new Button(this, GAME_W - 480, 32, 'Cuadernos', () => this.scene.start('gacha', { mode: 'notebooks', from: 'club' }), { w: 130, h: 38, color: 0x7a5aa8, size: 15 }));
  }

  // ------------------------------------------------------------- plantilla

  private drawSquad(): void {
    const c = this.squadBox;
    c.removeAll(true);
    const g = this.add.graphics();
    cardPanel(g, SQUAD.x, SQUAD.y, SQUAD.w, SQUAD.h);
    c.add(g);
    c.add(sectionTitle(this, SQUAD.x + 16, SQUAD.y + 22, 'Plantilla'));
    const f = getFormation(this.save.formation);
    c.add(label(this, SQUAD.x + 100, SQUAD.y + 22, f.name, 12, THEME.muted, { fontStyle: 'italic' }).setOrigin(0, 0.5));
    c.add(
      label(this, SQUAD.x + SQUAD.w - 16, SQUAD.y + 22, this.selected === null ? 'Pulsa un hueco para cambiarlo' : 'Ahora pulsa un jugador', 12, this.selected === null ? THEME.muted : THEME.cyanCss, {
        fontStyle: 'italic bold',
      }).setOrigin(1, 0.5),
    );
    const club = getTeam('club');
    this.save.squad.forEach((key, i) => {
      const card = cardByKey(key);
      const y = SQUAD.y + 60 + i * ROW_H + (i >= 11 ? 24 : 0);
      if (i === 11) c.add(label(this, SQUAD.x + 18, y - 24, 'BANQUILLO', 11, THEME.muted, { fontStyle: 'bold' }).setOrigin(0, 0.5));
      const slotPos = i < 11 ? f.slots[i].pos : null;
      const row = this.add.graphics();
      const on = this.selected === i;
      const wrong = !!card && !!slotPos && card.player.position !== slotPos;
      row.fillStyle(on ? THEME.yellow : i < 11 ? 0x1a2942 : 0x141f33, on ? 0.95 : 0.85).fillRoundedRect(SQUAD.x + 12, y - 14, SQUAD.w - 24, ROW_H - 3, 8);
      if (wrong && !on) row.lineStyle(1, THEME.coral, 0.8).strokeRoundedRect(SQUAD.x + 12, y - 14, SQUAD.w - 24, ROW_H - 3, 8);
      c.add(row);
      // hueco de la formación (o número de banquillo)
      c.add(label(this, SQUAD.x + 30, y, slotPos ?? `B${i - 10}`, 10, on ? THEME.ink : THEME.muted, { fontStyle: 'bold' }).setOrigin(0.5));
      if (!card) {
        c.add(label(this, SQUAD.x + 92, y, '— hueco vacío —', 13, THEME.muted, { fontStyle: 'italic' }).setOrigin(0, 0.5));
      } else {
        const p = card.player;
        row.fillStyle(POS_COLOR[p.position]).fillRoundedRect(SQUAD.x + 46, y - 9, 30, 18, 5);
        c.add(label(this, SQUAD.x + 61, y, p.position, 10, '#ffffff', { fontStyle: 'bold' }).setOrigin(0.5));
        const face = this.add.image(SQUAD.x + 96, y, portraitKey(this, cardPlayer(card), club)).setDisplaySize(26, 26);
        c.add(face);
        c.add(label(this, SQUAD.x + 116, y, p.name, 14, on ? THEME.ink : THEME.text, { fontStyle: 'italic bold' }).setOrigin(0, 0.5));
        c.add(text(this, SQUAD.x + SQUAD.w - 72, y, '★'.repeat(card.rarity), 12, on ? THEME.ink : RARITY[card.rarity].css, { strokeThickness: 0 }).setOrigin(1, 0.5));
        c.add(label(this, SQUAD.x + SQUAD.w - 26, y, String(cardOverall(p)), 14, on ? THEME.ink : wrong ? THEME.coralCss : THEME.text, { fontStyle: 'bold' }).setOrigin(1, 0.5));
      }
      const hit = this.add.zone(SQUAD.x + 12, y - 14, SQUAD.w - 24, ROW_H - 3).setOrigin(0).setInteractive({ useHandCursor: true });
      hit.on('pointerdown', () => this.pickSlot(i));
      if (card) hit.on('pointerover', () => this.showInfo(card));
      c.add(hit);
    });
    // pie: avisos y auto-alineación
    const fy = SQUAD.y + SQUAD.h - 30;
    const gk = cardByKey(this.save.squad[0]);
    const wrongCount = this.save.squad.slice(0, 11).filter((k, i) => cardByKey(k) && cardByKey(k)!.player.position !== f.slots[i].pos).length;
    const warn = !gk || gk.player.position !== 'GK' ? '⚠ Sin portero en la portería' : wrongCount ? `⚠ ${wrongCount} fuera de su puesto` : '';
    if (warn) c.add(chip(this, SQUAD.x + 16, fy, warn, THEME.coral, { size: 11, h: 24, padX: 10, textColor: '#ffffff' }));
    else c.add(label(this, SQUAD.x + 16, fy, 'Todos en su puesto ✓', 12, THEME.muted, { fontStyle: 'italic' }).setOrigin(0, 0.5));
    c.add(
      new Button(this, SQUAD.x + SQUAD.w - 86, fy, 'Auto-alinear', () => {
        const next = autoSquad(this.save);
        if (next.join() === this.save.squad.join()) return toast(this, 'Ya tienes a los mejores alineados', THEME.panelLight);
        this.selected = null;
        setSquad(this.save, next);
        toast(this, 'Plantilla reorganizada con tus mejores jugadores');
      }, { w: 140, h: 34, variant: 'accent', size: 14 }),
    );
  }

  private pickSlot(i: number): void {
    if (this.selected === null) {
      this.selected = i;
    } else if (this.selected === i) {
      this.selected = null;
    } else {
      const squad = [...this.save.squad];
      [squad[this.selected], squad[i]] = [squad[i], squad[this.selected]];
      this.selected = null;
      setSquad(this.save, squad);
      return;
    }
    this.drawSquad();
  }

  private pickCard(card: Card): void {
    this.showInfo(card);
    if (this.selected === null) {
      // sin hueco elegido: si el jugador no está en el 16, se le busca sitio en el banquillo
      const squad = [...this.save.squad];
      if (squad.includes(card.key)) return toast(this, 'Ya está en la plantilla: pulsa un hueco para moverlo', THEME.panelLight);
      const empty = squad.findIndex((k) => !cardByKey(k));
      if (empty >= 0) {
        squad[empty] = card.key;
        setSquad(this.save, squad);
        return;
      }
      return toast(this, 'Pulsa primero el hueco donde quieres ponerlo', THEME.panelLight);
    }
    const squad = [...this.save.squad];
    const already = squad.indexOf(card.key);
    if (already >= 0) [squad[already], squad[this.selected]] = [squad[this.selected], squad[already]];
    else squad[this.selected] = card.key;
    this.selected = null;
    setSquad(this.save, squad);
  }

  // ------------------------------------------------------------- colección

  private drawCollection(): void {
    const c = this.collBox;
    c.removeAll(true);
    const g = this.add.graphics();
    cardPanel(g, COLL.x, COLL.y, COLL.w, COLL.h, { accent: THEME.orange });
    c.add(g);
    const all = this.collection();
    c.add(sectionTitle(this, COLL.x + 16, COLL.y + 22, `Colección (${all.length})`));
    // filtros: demarcación y rareza
    FILTERS.forEach((f, i) => {
      const x = COLL.x + 170 + i * 54;
      const on = this.filter === f;
      const tab = this.add.graphics();
      tab.fillStyle(on ? THEME.yellow : f === 'ALL' ? THEME.panelLight : POS_COLOR[f], on ? 1 : 0.55).fillRoundedRect(x, COLL.y + 10, 50, 24, 8);
      c.add(tab);
      c.add(label(this, x + 25, COLL.y + 22, f === 'ALL' ? 'Todos' : f, 12, on ? THEME.ink : '#ffffff', { fontStyle: 'bold' }).setOrigin(0.5));
      const hit = this.add.zone(x, COLL.y + 10, 50, 24).setOrigin(0).setInteractive({ useHandCursor: true });
      hit.on('pointerdown', () => {
        this.filter = f;
        this.page = 0;
        this.drawCollection();
      });
      c.add(hit);
    });
    ([0, 1, 2, 3, 4] as const).forEach((r, i) => {
      const x = COLL.x + 470 + i * 52;
      const on = this.rarityFilter === r;
      const tab = this.add.graphics();
      tab.fillStyle(on ? THEME.yellow : THEME.panelLight, on ? 1 : 0.8).fillRoundedRect(x, COLL.y + 10, 48, 24, 8);
      if (r) tab.lineStyle(1, RARITY[r].color, 0.8).strokeRoundedRect(x, COLL.y + 10, 48, 24, 8);
      c.add(tab);
      c.add(text(this, x + 24, COLL.y + 22, r ? '★'.repeat(r) : 'Todas', r ? 9 : 11, on ? THEME.ink : r ? RARITY[r].css : '#ffffff', { fontStyle: 'bold', strokeThickness: 0 }).setOrigin(0.5));
      const hit = this.add.zone(x, COLL.y + 10, 48, 24).setOrigin(0).setInteractive({ useHandCursor: true });
      hit.on('pointerdown', () => {
        this.rarityFilter = r;
        this.page = 0;
        this.drawCollection();
      });
      c.add(hit);
    });
    const pages = Math.max(1, Math.ceil(all.length / PER_PAGE));
    this.page = Math.min(this.page, pages - 1);
    const shown = all.slice(this.page * PER_PAGE, (this.page + 1) * PER_PAGE);
    const missing = shown.filter((card) => !this.textures.exists(`portrait:${card.origin}:${card.player.id}`));
    if (missing.length) loadCardPortraits(this, missing, () => this.scene.isActive() && this.drawCollectionCards(shown));
    this.drawCollectionCards(shown);
    if (!all.length) c.add(label(this, COLL.x + COLL.w / 2, COLL.y + COLL.h / 2, 'Ningún jugador con esos filtros', 16, THEME.muted, { fontStyle: 'italic' }).setOrigin(0.5));
    // páginas
    const navY = COLL.y + COLL.h - 24;
    c.add(label(this, COLL.x + COLL.w / 2, navY, `${this.page + 1} / ${pages}`, 14, THEME.text, { fontStyle: 'bold' }).setOrigin(0.5));
    for (const dir of [-1, 1]) {
      const b = new Button(this, COLL.x + COLL.w / 2 + dir * 76, navY, dir < 0 ? '◀' : '▶', () => {
        this.page = (this.page + dir + pages) % pages;
        this.drawCollection();
      }, { w: 44, h: 30, variant: 'secondary', size: 13 });
      b.setEnabled(pages > 1);
      c.add(b);
    }
  }

  private cardsLayer?: Phaser.GameObjects.Container;

  private drawCollectionCards(shown: Card[]): void {
    this.cardsLayer?.destroy();
    const layer = this.add.container(0, 0);
    this.cardsLayer = layer;
    this.collBox.add(layer);
    const inSquad = new Set(this.save.squad);
    shown.forEach((card, i) => {
      const x = COLL.x + 82 + (i % 5) * 146;
      const y = COLL.y + 128 + Math.floor(i / 5) * 170;
      const cc = drawCard(this, x, y, card, 124, 160);
      if (inSquad.has(card.key)) {
        const idx = this.save.squad.indexOf(card.key);
        const tag = chip(this, 0, -46, idx < 11 ? 'TITULAR' : 'BANQUILLO', idx < 11 ? THEME.yellow : THEME.panelLight, { size: 9, h: 16, padX: 7 });
        tag.setX(-tag.width / 2);
        cc.add(tag);
      }
      cc.setInteractive({ useHandCursor: true });
      cc.on('pointerover', () => (cc.setScale(1.05), this.showInfo(card)));
      cc.on('pointerout', () => cc.setScale(1));
      cc.on('pointerdown', () => this.pickCard(card));
      layer.add(cc);
    });
  }

  // ---------------------------------------------------------------- ficha

  private showInfo(card: Card): void {
    const c = this.infoBox;
    c.removeAll(true);
    const g = this.add.graphics();
    cardPanel(g, INFO.x, INFO.y, INFO.w, INFO.h, { accent: RARITY[card.rarity].color });
    c.add(g);
    const p = card.player;
    c.add(label(this, INFO.x + 18, INFO.y + 24, p.name, 20, THEME.text, { fontStyle: 'italic bold' }).setOrigin(0, 0.5));
    let origin = 'Ojeador';
    if (!card.origin.startsWith('scouts')) {
      try {
        origin = getTeam(card.origin).name;
      } catch {
        // equipo que ya no está
      }
    }
    c.add(label(this, INFO.x + 18, INFO.y + 48, `${RARITY[card.rarity].name} ${'★'.repeat(card.rarity)}  ·  ${origin}  ·  ${p.position}  ·  Media ${cardOverall(p)}  ·  FP ${p.fp}  ·  TP ${p.tp}`, 12, RARITY[card.rarity].css, { fontStyle: 'bold' }).setOrigin(0, 0.5));
    STAT_LABEL.forEach(([k, lbl], i) => {
      const x = INFO.x + 18 + (i % 4) * 116;
      const y = INFO.y + 80 + Math.floor(i / 4) * 26;
      const v = p.stats[k];
      const bar = this.add.graphics();
      bar.fillStyle(0x000000, 0.45).fillRoundedRect(x + 52, y - 4, 44, 8, 4);
      bar.fillStyle(v >= 75 ? THEME.yellow : THEME.glow).fillRoundedRect(x + 52, y - 4, Math.max(6, (44 * v) / 99), 8, 4);
      c.add(bar);
      c.add(label(this, x, y, lbl, 11, THEME.muted).setOrigin(0, 0.5));
      c.add(label(this, x + 104, y, String(v), 13, THEME.text, { fontStyle: 'bold' }).setOrigin(1, 0.5));
    });
    const { base, extra } = movesFor(this.save, card);
    const moves = [...base, ...extra].filter(Boolean).map((id) => MOVES[id]?.name ?? id);
    c.add(label(this, INFO.x + 500, INFO.y + 20, 'SUPERTÉCNICAS', 10, THEME.yellowCss, { fontStyle: 'bold' }));
    c.add(label(this, INFO.x + 500, INFO.y + 36, moves.length ? moves.map((m) => `· ${m}`).join('\n') : 'Ninguna', 12, THEME.text, { lineSpacing: 2 }));
    if (this.save.owned.includes(card.key)) {
      c.add(new Button(this, INFO.x + INFO.w - 72, INFO.y + 26, 'Editar ✎', () => this.openEditor(card), { w: 116, h: 32, color: 0x7a5aa8, size: 14 }));
    }
    if (p.description) {
      c.add(label(this, INFO.x + 18, INFO.y + 140, p.description, 12, THEME.muted, { fontStyle: 'italic', wordWrap: { width: 470 } }).setOrigin(0, 0.5));
    }
  }

  // ---------------------------------------------------- escudo del club

  private crestBox?: Phaser.GameObjects.Container;
  private crestPage = 0;

  /** Los escudos conseguidos (tres al empezar y uno por victoria): el que se pulse pasa a ser el del club. */
  private openCrests(): void {
    const owned = this.save.crests ?? [];
    this.crestPage = Math.max(0, Math.floor(owned.indexOf(this.save.crest ?? '') / CREST_PER_PAGE));
    this.drawCrests();
  }

  private closeCrests(): void {
    this.crestBox?.destroy();
    this.crestBox = undefined;
  }

  private drawCrests(): void {
    this.crestBox?.destroy();
    const c = this.add.container(0, 0).setDepth(300);
    this.crestBox = c;
    c.add(this.add.rectangle(0, 0, GAME_W, GAME_H, 0x000000, 0.72).setOrigin(0).setInteractive());
    const g = this.add.graphics();
    cardPanel(g, 40, 40, GAME_W - 80, GAME_H - 80, { accent: 0x2f7bff, alpha: 0.98 });
    c.add(g);
    const owned = this.save.crests ?? [];
    c.add(display(this, 64, 74, 'Escudo del club', 30, '#ffffff').setOrigin(0, 0.5));
    c.add(label(this, 66, 104, `${owned.length} de ${CRESTS.length} escudos de Victory Road. Ganas uno nuevo con cada victoria.`, 13, THEME.muted, { fontStyle: 'italic' }).setOrigin(0, 0.5));
    c.add(new Button(this, GAME_W - 130, 74, 'Hecho', () => this.closeCrests(), { w: 140, h: 42, variant: 'primary', hint: 'Esc' }));
    const pages = Math.max(1, Math.ceil(owned.length / CREST_PER_PAGE));
    this.crestPage = Math.min(this.crestPage, pages - 1);
    const list = owned.slice(this.crestPage * CREST_PER_PAGE, (this.crestPage + 1) * CREST_PER_PAGE);
    const cols = 8;
    const cw = (GAME_W - 160) / cols;
    const ch = 160;
    const cells = list.map((id, i) => {
      const x = 80 + (i % cols) * cw + cw / 2;
      const y = 140 + Math.floor(i / cols) * ch + ch / 2;
      const on = id === this.save.crest;
      const cell = this.add.graphics();
      cell.fillStyle(on ? THEME.yellow : 0x1a2942, on ? 0.95 : 0.85).fillRoundedRect(x - cw / 2 + 6, y - ch / 2 + 6, cw - 12, ch - 12, 12);
      c.add(cell);
      c.add(fitWidth(label(this, x, y + 56, crestById(id)?.name ?? id, 11, on ? THEME.ink : THEME.text, { fontStyle: 'bold', align: 'center' }).setOrigin(0.5), cw - 20, 8));
      const hit = this.add.zone(x - cw / 2 + 6, y - ch / 2 + 6, cw - 12, ch - 12).setOrigin(0).setInteractive({ useHandCursor: true });
      hit.on('pointerdown', () => {
        setCrest(this.save, id);
        this.save = loadClub()!;
        applyClubCrest(this, id, () => {
          this.drawHeader();
          if (this.crestBox) this.drawCrests();
        });
      });
      c.add(hit);
      return { id, x, y };
    });
    loadCrests(this, list, () => {
      if (this.crestBox !== c) return;
      for (const { id, x, y } of cells) if (this.textures.exists(crestKey(id))) c.add(this.add.image(x, y - 12, crestKey(id)).setDisplaySize(100, 100));
    });
    if (pages > 1) {
      const py = GAME_H - 66;
      c.add(new Button(this, GAME_W / 2 - 120, py, '◀', () => ((this.crestPage = (this.crestPage + pages - 1) % pages), this.drawCrests()), { w: 60, h: 38, variant: 'secondary' }));
      c.add(label(this, GAME_W / 2, py, `${this.crestPage + 1} / ${pages}`, 15, THEME.text, { fontStyle: 'bold' }).setOrigin(0.5));
      c.add(new Button(this, GAME_W / 2 + 120, py, '▶', () => ((this.crestPage = (this.crestPage + 1) % pages), this.drawCrests()), { w: 60, h: 38, variant: 'secondary' }));
    }
  }

  // ---------------------------------------------------- editor de técnicas

  private editor?: Phaser.GameObjects.Container;
  private editSlot = 0;
  private editKind: 'ALL' | MoveKind = 'ALL';
  private editPage = 0;

  /** Las 4 técnicas de base y las 2 extra de un jugador, y los cuadernos que se le pueden poner. */
  private openEditor(card: Card): void {
    this.editSlot = 0;
    this.editPage = 0;
    this.editKind = 'ALL';
    this.drawEditor(card);
  }

  private closeEditor(): void {
    this.editor?.destroy();
    this.editor = undefined;
    this.redraw();
  }

  private drawEditor(card: Card, message = ''): void {
    this.editor?.destroy();
    const c = this.add.container(0, 0).setDepth(300);
    this.editor = c;
    c.add(this.add.rectangle(0, 0, GAME_W, GAME_H, 0x000000, 0.72).setOrigin(0).setInteractive());
    const g = this.add.graphics();
    cardPanel(g, 40, 40, GAME_W - 80, GAME_H - 80, { accent: 0x7a5aa8, alpha: 0.98 });
    c.add(g);
    c.add(display(this, 64, 74, `Supertécnicas de ${card.player.name}`, 30, '#ffffff').setOrigin(0, 0.5));
    c.add(label(this, 66, 104, 'Pulsa un hueco y luego una técnica. Las suyas no gastan cuaderno.', 13, THEME.muted, { fontStyle: 'italic' }).setOrigin(0, 0.5));
    if (message) c.add(label(this, GAME_W - 70, 104, message, 13, THEME.coralCss, { fontStyle: 'bold' }).setOrigin(1, 0.5));
    c.add(new Button(this, GAME_W - 130, 74, 'Hecho', () => this.closeEditor(), { w: 140, h: 42, variant: 'primary', hint: 'Esc' }));

    // huecos
    const { base, extra } = movesFor(this.save, card);
    const slots = [...base, ...extra];
    slots.forEach((id, i) => {
      const y = 150 + i * 70 + (i >= BASE_SLOTS ? 22 : 0);
      if (i === 0) c.add(label(this, 66, y - 18, 'BASE', 12, THEME.yellowCss, { fontStyle: 'bold' }));
      if (i === BASE_SLOTS) c.add(label(this, 66, y - 18, 'EXTRA', 12, '#c7a6ff', { fontStyle: 'bold' }));
      const on = i === this.editSlot;
      const m = id ? MOVES[id] : undefined;
      const row = this.add.graphics();
      row.fillStyle(on ? THEME.yellow : 0x1a2942, 0.95).fillRoundedRect(62, y, 420, 54, 10);
      if (m) row.fillStyle(ELEMENT_COLOR[m.element]).fillRoundedRect(70, y + 8, 6, 38, 3);
      c.add(row);
      const ink = on ? THEME.ink : THEME.text;
      c.add(label(this, 86, y + 18, m ? m.name : '— vacío —', 17, ink, { fontStyle: 'italic bold' }).setOrigin(0, 0.5));
      if (m) c.add(label(this, 86, y + 38, `${KIND_LABEL[m.kind]} · potencia ${m.power} · TP ${m.tp}`, 12, on ? THEME.ink : THEME.muted).setOrigin(0, 0.5));
      const hit = this.add.zone(62, y, 420, 54).setOrigin(0).setInteractive({ useHandCursor: true });
      hit.on('pointerdown', () => ((this.editSlot = i), this.drawEditor(card)));
      c.add(hit);
      if (m) c.add(new Button(this, 452, y + 27, '✕', () => this.assign(card, i, ''), { w: 40, h: 34, variant: 'danger', size: 15 }));
    });

    // técnicas disponibles: las suyas y los cuadernos libres
    const own = new Set(card.player.moves);
    const all = Object.values(MOVES)
      .filter((m) => own.has(m.id) || freeNotebooks(this.save, m.id) > 0 || slots.includes(m.id))
      .filter((m) => this.editKind === 'ALL' || m.kind === this.editKind)
      .sort((a, b) => Number(own.has(b.id)) - Number(own.has(a.id)) || b.power - a.power);
    const LX = 520;
    const kinds: ('ALL' | MoveKind)[] = ['ALL', 'shoot', 'dribble', 'block', 'catch'];
    kinds.forEach((k, i) => {
      const on = k === this.editKind;
      const b = new Button(this, LX + 50 + i * 104, 150, k === 'ALL' ? 'Todas' : KIND_LABEL[k], () => ((this.editKind = k), (this.editPage = 0), this.drawEditor(card)), {
        w: 98,
        h: 32,
        size: 13,
        variant: on ? 'primary' : 'secondary',
      });
      c.add(b);
    });
    const PER = 16;
    const pages = Math.max(1, Math.ceil(all.length / PER));
    this.editPage = Math.min(this.editPage, pages - 1);
    if (!all.length) c.add(label(this, LX + 340, 330, 'No tienes cuadernos de este tipo.\nConsíguelos en Cuadernos.', 16, THEME.muted, { align: 'center' }).setOrigin(0.5));
    all.slice(this.editPage * PER, (this.editPage + 1) * PER).forEach((m, i) => {
      const x = LX + (i % 2) * 344;
      const y = 186 + Math.floor(i / 2) * 52;
      const r = notebookRarity(m);
      const row = this.add.graphics();
      row.fillStyle(0x0e1626, 0.95).fillRoundedRect(x, y, 334, 46, 8);
      row.lineStyle(1.5, RARITY[r].color, 0.9).strokeRoundedRect(x, y, 334, 46, 8);
      row.fillStyle(ELEMENT_COLOR[m.element]).fillRoundedRect(x + 6, y + 8, 5, 30, 2);
      c.add(row);
      c.add(label(this, x + 18, y + 15, m.name, 14, THEME.text, { fontStyle: 'bold' }).setOrigin(0, 0.5));
      c.add(label(this, x + 18, y + 33, `${KIND_LABEL[m.kind]} · ${m.power} · TP ${m.tp}  ${'★'.repeat(r)}`, 11, RARITY[r].css).setOrigin(0, 0.5));
      const tag = own.has(m.id) ? 'suya' : slots.includes(m.id) ? 'puesta' : `×${freeNotebooks(this.save, m.id)}`;
      c.add(label(this, x + 324, y + 23, tag, 13, own.has(m.id) ? '#7dff9a' : THEME.yellowCss, { fontStyle: 'bold' }).setOrigin(1, 0.5));
      const hit = this.add.zone(x, y, 334, 46).setOrigin(0).setInteractive({ useHandCursor: true });
      hit.on('pointerdown', () => this.assign(card, this.editSlot, m.id));
      c.add(hit);
    });
    const navY = GAME_H - 72;
    c.add(label(this, LX + 340, navY, `${this.editPage + 1} / ${pages}`, 14, THEME.text, { fontStyle: 'bold' }).setOrigin(0.5));
    for (const dir of [-1, 1]) {
      c.add(new Button(this, LX + 340 + dir * 80, navY, dir < 0 ? '◀' : '▶', () => ((this.editPage = (this.editPage + dir + pages) % pages), this.drawEditor(card)), { w: 46, h: 30, variant: 'secondary', size: 13 }));
    }
  }

  private assign(card: Card, slot: number, moveId: string): void {
    const { base, extra } = movesFor(this.save, card);
    const slots = [...base, ...extra];
    if (moveId && slots.includes(moveId) && slots[slot] !== moveId) {
      // ya la tiene en otro hueco: se cambian de sitio
      slots[slots.indexOf(moveId)] = slots[slot];
    }
    slots[slot] = moveId;
    const ok = setMoves(this.save, card, slots.slice(0, BASE_SLOTS), slots.slice(BASE_SLOTS));
    this.save = loadClub()!;
    if (ok && moveId) this.editSlot = Math.min(slots.length - 1, slot + 1);
    this.drawEditor(card, ok ? '' : 'No te quedan cuadernos de esa técnica');
  }
}
