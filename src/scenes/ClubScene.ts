import Phaser from 'phaser';
import { music } from '../audio/music';
import { loadClub, onClubChange, setSquad, type ClubSave } from '../club/club';
import { cardByKey, RARITY, type Card } from '../club/pool';
import { GAME_H, GAME_W } from '../config';
import { getTeam, MOVES } from '../data';
import type { Position } from '../data/types';
import { teamRating } from '../engine/rating';
import { portraitKey } from '../gfx/placeholders';
import { cardPlayer, drawCard, loadCardPortraits } from '../ui/card';
import { POS_COLOR, THEME, fitCamera, slant, sectionTitle, themePanel } from '../ui/theme';
import { Button, text } from '../ui/widgets';

const SQUAD = { x: 24, y: 112, w: 470, h: 588 };
const COLL = { x: 512, y: 112, w: 744, h: 420 };
const INFO = { x: 512, y: 548, w: 744, h: 152 };
const PER_PAGE = 10;
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
    const bg = this.add.graphics();
    bg.fillStyle(THEME.night).fillRect(0, 0, GAME_W, GAME_H);
    bg.fillStyle(0x16233b).fillPoints([new Phaser.Geom.Point(GAME_W * 0.55, 0), new Phaser.Geom.Point(GAME_W, 0), new Phaser.Geom.Point(GAME_W, GAME_H), new Phaser.Geom.Point(GAME_W * 0.42, GAME_H)], true);
    this.header = this.add.container(0, 0);
    this.squadBox = this.add.container(0, 0);
    this.collBox = this.add.container(0, 0);
    this.infoBox = this.add.container(0, 0);
    new Button(this, GAME_W - 400, 62, 'Fichajes', () => this.scene.start('gacha'), { w: 170, h: 46, color: 0xff7a3d });
    new Button(this, GAME_W - 220, 62, '¡A jugar!', () => this.play(), { w: 170, h: 46, color: THEME.yellow });
    new Button(this, GAME_W - 74, 62, 'Menú', () => this.scene.start('menu'), { w: 110, h: 46, color: THEME.panelLight });
    const off = onClubChange(() => {
      this.save = loadClub()!;
      this.redraw();
    });
    this.events.once(Phaser.Scenes.Events.SHUTDOWN, off);
    this.input.keyboard?.on('keydown-ESC', () => this.scene.start('menu'));
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
      .sort((a, b) => b.rarity - a.rarity || order[a.player.position] - order[b.player.position] || a.player.name.localeCompare(b.player.name));
  }

  private redraw(): void {
    this.drawHeader();
    this.drawSquad();
    this.drawCollection();
  }

  private drawHeader(): void {
    const c = this.header;
    c.removeAll(true);
    c.add(text(this, 40, 18, this.save.name, 32, '#ffd23f', { fontStyle: 'italic bold', strokeThickness: 6 }));
    let rating = 0;
    try {
      rating = teamRating(getTeam('club'));
    } catch {
      // aún sin equipo
    }
    c.add(text(this, 42, 62, `Media ${rating}  ·  ${this.save.owned.length} jugadores  ·  ${this.save.pulls} tiradas`, 15, '#ffffff', { fontStyle: 'italic' }));
    c.add(text(this, GAME_W - 40, 22, `● ${this.save.coins} monedas`, 20, '#ffd23f', { fontStyle: 'bold', strokeThickness: 5 }).setOrigin(1, 0.5));
  }

  // ------------------------------------------------------------- plantilla

  private drawSquad(): void {
    const c = this.squadBox;
    c.removeAll(true);
    const g = this.add.graphics();
    themePanel(g, SQUAD.x, SQUAD.y, SQUAD.w, SQUAD.h);
    c.add(g);
    c.add(sectionTitle(this, SQUAD.x + 16, SQUAD.y + 20, 'Plantilla'));
    c.add(
      text(this, SQUAD.x + SQUAD.w - 16, SQUAD.y + 20, this.selected === null ? 'Pulsa un hueco para cambiarlo' : 'Ahora pulsa un jugador', 12, this.selected === null ? THEME.muted : '#ffd23f', {
        fontStyle: 'italic',
        strokeThickness: 0,
      }).setOrigin(1, 0.5),
    );
    const club = getTeam('club');
    this.save.squad.forEach((key, i) => {
      const card = cardByKey(key);
      const y = SQUAD.y + 52 + i * 33 + (i >= 11 ? 14 : 0);
      if (i === 11) c.add(text(this, SQUAD.x + 18, y - 12, 'BANQUILLO', 11, THEME.muted, { fontStyle: 'bold', strokeThickness: 0 }).setOrigin(0, 0.5));
      const row = this.add.graphics();
      const on = this.selected === i;
      row.fillStyle(on ? THEME.yellow : i < 11 ? 0x1a2840 : 0x131e31, on ? 0.95 : 0.9).fillPoints(slant(SQUAD.x + 12, y - 14, SQUAD.w - 24, 29, 8), true);
      c.add(row);
      if (!card) return;
      const p = card.player;
      row.fillStyle(POS_COLOR[p.position]).fillPoints(slant(SQUAD.x + 18, y - 10, 34, 21, 6), true);
      c.add(text(this, SQUAD.x + 35, y, p.position, 11, '#ffffff', { fontStyle: 'bold', strokeThickness: 2 }).setOrigin(0.5));
      const face = this.add.image(SQUAD.x + 72, y, portraitKey(this, cardPlayer(card), club)).setDisplaySize(27, 27);
      c.add(face);
      c.add(text(this, SQUAD.x + 92, y, p.name, 15, on ? THEME.ink : '#ffffff', { fontStyle: 'italic bold', strokeThickness: on ? 0 : 3 }).setOrigin(0, 0.5));
      c.add(text(this, SQUAD.x + SQUAD.w - 70, y, '★'.repeat(card.rarity), 13, on ? THEME.ink : RARITY[card.rarity].css, { strokeThickness: on ? 0 : 3 }).setOrigin(1, 0.5));
      c.add(text(this, SQUAD.x + SQUAD.w - 24, y, String(this.overall(card)), 15, on ? THEME.ink : '#ffffff', { fontStyle: 'bold', strokeThickness: on ? 0 : 3 }).setOrigin(1, 0.5));
      const hit = this.add.zone(SQUAD.x + 12, y - 14, SQUAD.w - 24, 29).setOrigin(0).setInteractive({ useHandCursor: true });
      hit.on('pointerdown', () => this.pickSlot(i));
      hit.on('pointerover', () => this.showInfo(card));
      c.add(hit);
    });
  }

  /** Media de un jugador según su puesto (la misma idea que la de los equipos del menú). */
  private overall(card: Card): number {
    const s = card.player.stats;
    const v =
      card.player.position === 'GK'
        ? s.guard * 0.5 + s.body * 0.2 + s.guts * 0.3
        : card.player.position === 'DF'
          ? s.guard * 0.4 + s.body * 0.3 + s.speed * 0.15 + s.guts * 0.15
          : card.player.position === 'MF'
            ? s.control * 0.35 + s.speed * 0.25 + s.kick * 0.2 + s.body * 0.2
            : s.kick * 0.5 + s.control * 0.25 + s.speed * 0.25;
    return Math.round(v);
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
    if (this.selected === null) return;
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
    themePanel(g, COLL.x, COLL.y, COLL.w, COLL.h, 0xff7a3d);
    c.add(g);
    const all = this.collection();
    c.add(sectionTitle(this, COLL.x + 16, COLL.y + 20, `Colección (${all.length})`));
    FILTERS.forEach((f, i) => {
      const x = COLL.x + 260 + i * 62;
      const on = this.filter === f;
      const tab = this.add.graphics();
      tab.fillStyle(on ? THEME.yellow : f === 'ALL' ? 0x2c3d5c : POS_COLOR[f], on ? 1 : 0.6).fillPoints(slant(x, COLL.y + 8, 56, 24, 6), true);
      c.add(tab);
      c.add(text(this, x + 28, COLL.y + 20, f === 'ALL' ? 'Todos' : f, 12, on ? THEME.ink : '#ffffff', { fontStyle: 'bold', strokeThickness: on ? 0 : 2 }).setOrigin(0.5));
      const hit = this.add.zone(x, COLL.y + 8, 56, 24).setOrigin(0).setInteractive({ useHandCursor: true });
      hit.on('pointerdown', () => {
        this.filter = f;
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
    // páginas
    const navY = COLL.y + COLL.h - 22;
    c.add(text(this, COLL.x + COLL.w / 2, navY, `${this.page + 1} / ${pages}`, 14, '#ffffff', { fontStyle: 'bold' }).setOrigin(0.5));
    for (const dir of [-1, 1]) {
      const b = new Button(this, COLL.x + COLL.w / 2 + dir * 80, navY, dir < 0 ? '◀' : '▶', () => {
        this.page = (this.page + dir + pages) % pages;
        this.drawCollection();
      }, { w: 46, h: 30, color: THEME.panelLight, size: 14 });
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
      const x = COLL.x + 80 + (i % 5) * 146;
      const y = COLL.y + 132 + Math.floor(i / 5) * 186;
      const cc = drawCard(this, x, y, card, 128, 172);
      if (inSquad.has(card.key)) {
        cc.add(this.add.graphics().fillStyle(THEME.yellow).fillPoints(slant(-60, -60, 60, 18, 5), true));
        cc.add(text(this, -30, -51, 'EN EL 16', 10, THEME.ink, { fontStyle: 'bold', strokeThickness: 0 }).setOrigin(0.5));
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
    themePanel(g, INFO.x, INFO.y, INFO.w, INFO.h, RARITY[card.rarity].color);
    c.add(g);
    const p = card.player;
    c.add(text(this, INFO.x + 18, INFO.y + 22, p.name, 20, '#ffffff', { fontStyle: 'italic bold' }).setOrigin(0, 0.5));
    let origin = 'Ojeador';
    if (!card.origin.startsWith('scouts')) {
      try {
        origin = getTeam(card.origin).name;
      } catch {
        // equipo que ya no está
      }
    }
    c.add(text(this, INFO.x + 18, INFO.y + 46, `${RARITY[card.rarity].name} · ${origin} · FP ${p.fp} · TP ${p.tp}`, 13, RARITY[card.rarity].css, { fontStyle: 'bold' }).setOrigin(0, 0.5));
    STAT_LABEL.forEach(([k, label], i) => {
      const x = INFO.x + 18 + (i % 4) * 118;
      const y = INFO.y + 76 + Math.floor(i / 4) * 26;
      c.add(text(this, x, y, label, 12, THEME.muted, { strokeThickness: 0 }).setOrigin(0, 0.5));
      c.add(text(this, x + 100, y, String(p.stats[k]), 14, '#ffffff', { fontStyle: 'bold' }).setOrigin(1, 0.5));
    });
    const moves = p.moves.map((id) => MOVES[id]?.name).filter(Boolean);
    c.add(text(this, INFO.x + 500, INFO.y + 18, 'Supertécnicas', 12, '#ffd23f', { fontStyle: 'bold' }));
    c.add(text(this, INFO.x + 500, INFO.y + 38, moves.length ? moves.map((m) => `· ${m}`).join('\n') : 'Ninguna', 13, '#e3e9f2', { lineSpacing: 4, strokeThickness: 0 }));
    if (p.description) {
      const d = text(this, INFO.x + 18, INFO.y + 128, p.description, 12, '#c9d3e0', { fontStyle: 'italic', wordWrap: { width: 470 }, strokeThickness: 0 }).setOrigin(0, 0.5);
      c.add(d);
    }
  }
}
