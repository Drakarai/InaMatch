import Phaser from 'phaser';
import { music } from '../audio/music';
import { sfx } from '../audio/sfx';
import { loadClub, saveClub } from '../club/club';
import { GAME_H, GAME_W, PORTRAIT } from '../config';
import { getTeam, TEAMS } from '../data';
import { SEASONS } from '../data/seasons';
import type { TeamData } from '../data/types';
import { defaultLineup } from '../engine/lineup';
import { ensureSprites, portraitsOf } from '../gfx/pack';
import { texKey } from '../gfx/placeholders';
import {
  finishRoute,
  loadProgress,
  loadStories,
  ROUTE_COINS,
  setStage,
  STORY_REGISTRY,
  STORY_RESULT,
  type Story,
  type StoryBook,
  type StoryLine,
  type StoryMatch,
} from '../story/story';
import { THEME, cardPanel, coinChip, fitCamera, glow, pt, stadiumBackdrop, toast, topBar } from '../ui/theme';
import { Button, display, fitWidth, label } from '../ui/widgets';

const STORY_SEASONS = SEASONS.filter((s) => s.id !== 'club' && s.id !== 'otros');

/**
 * Modo historia: se elige un equipo (por temporadas) y se juega su ruta, capítulo a capítulo: diálogo, partido y, si se
 * gana, el diálogo de después y el siguiente rival. Al acabar la ruta, su final y monedas para Mi club.
 */
export class StoryScene extends Phaser.Scene {
  private book: StoryBook = {};
  private season = 'ie1';
  private team: string | null = null;
  private view!: Phaser.GameObjects.Container;
  private busy = false;

  constructor() {
    super('story');
  }

  init(data: { team?: string }): void {
    this.team = data?.team ?? null;
  }

  create(): void {
    fitCamera(this);
    music.play('menu');
    this.busy = false;
    stadiumBackdrop(this, THEME.home, THEME.yellow);
    this.view = this.add.container(0, 0);
    const wait = label(this, GAME_W / 2, GAME_H / 2, 'Cargando historias…', 18, '#ffffff').setOrigin(0.5);
    loadStories().then((book) => {
      wait.destroy();
      this.book = book;
      // vuelta de un partido de la historia
      const res = this.registry.get(STORY_RESULT) as (StoryMatch & { won: boolean }) | undefined;
      this.registry.remove(STORY_RESULT);
      this.registry.remove(STORY_REGISTRY);
      if (res && book[res.team]) {
        this.team = res.team;
        this.season = this.seasonOf(res.team);
        void this.afterMatch(res);
        return;
      }
      if (this.team && book[this.team]) {
        this.season = this.seasonOf(this.team);
        this.showRoute(this.team);
      } else this.showSelect();
    });
    this.input.keyboard?.on('keydown-ESC', () => {
      if (this.busy) return;
      if (this.team) {
        this.team = null;
        this.showSelect();
      } else this.scene.start('title');
    });
  }

  private seasonOf(teamId: string): string {
    try {
      return getTeam(teamId).season ?? 'ie1';
    } catch {
      return 'ie1';
    }
  }

  // ------------------------------------------------------------- elegir equipo

  private showSelect(): void {
    this.team = null;
    const c = this.view.removeAll(true);
    c.add(topBar(this, { title: 'Modo historia', subtitle: 'Elige un equipo y juega su historia', back: { label: 'Inicio', onClick: () => this.scene.start('title') } }));
    // pestañas de temporada
    const tabY = PORTRAIT ? 104 : 100;
    const tw = Math.min(PORTRAIT ? 58 : 110, (GAME_W - 24) / STORY_SEASONS.length);
    STORY_SEASONS.forEach((s, i) => {
      const x = GAME_W / 2 + (i - (STORY_SEASONS.length - 1) / 2) * tw;
      const on = s.id === this.season;
      const g = this.add.graphics();
      g.fillStyle(on ? THEME.yellow : 0x10203a, on ? 1 : 0.85).fillRoundedRect(x - tw / 2 + 3, tabY - 26, tw - 6, 52, 10);
      c.add(g);
      const key = `series:${s.icon}`;
      if (this.textures.exists(key)) {
        const img = this.add.image(x, tabY, key);
        img.setScale(40 / img.height);
        c.add(img);
      } else c.add(label(this, x, tabY, s.short, 13, on ? '#0b1a2e' : '#ffffff', { fontStyle: 'bold' }).setOrigin(0.5));
      const hit = this.add.zone(x, tabY, tw - 6, 52).setInteractive({ useHandCursor: true });
      hit.on('pointerup', () => {
        this.season = s.id;
        this.showSelect();
      });
      c.add(hit);
    });
    const season = STORY_SEASONS.find((s) => s.id === this.season);
    c.add(label(this, GAME_W / 2, tabY + 44, season?.name ?? '', PORTRAIT ? 16 : 18, '#ffd23f', { fontStyle: 'bold italic' }).setOrigin(0.5));
    // cuadrícula de equipos
    const teams = TEAMS.filter((t) => t.season === this.season && this.book[t.id]).sort((a, b) => Number(!!this.book[b.id].main) - Number(!!this.book[a.id].main));
    const prog = loadProgress();
    const cols = PORTRAIT ? 3 : 6;
    const top = tabY + 70;
    const cw = (GAME_W - 40) / cols;
    const rows = Math.ceil(teams.length / cols);
    const ch = Math.min(PORTRAIT ? 150 : 132, (GAME_H - top - 20) / Math.max(1, rows));
    teams.forEach((t, i) => {
      const story = this.book[t.id];
      const x = 20 + (i % cols) * cw + cw / 2;
      const y = top + Math.floor(i / cols) * ch + ch / 2;
      const g = this.add.graphics();
      const main = !!story.main;
      g.fillStyle(main ? 0x3a2a08 : 0x10203a, 0.92).fillRoundedRect(x - cw / 2 + 5, y - ch / 2 + 4, cw - 10, ch - 8, 12);
      g.lineStyle(2, main ? THEME.yellow : 0xffffff, main ? 0.9 : 0.15).strokeRoundedRect(x - cw / 2 + 5, y - ch / 2 + 4, cw - 10, ch - 8, 12);
      c.add(g);
      const es = Math.min(ch * 0.46, 64);
      c.add(this.add.image(x, y - ch * 0.14, texKey.emblem(t.id)).setDisplaySize(es, es));
      c.add(fitWidth(label(this, x, y + ch * 0.2, t.name, PORTRAIT ? 12 : 12, '#ffffff', { fontStyle: 'bold', align: 'center' }).setOrigin(0.5), cw - 18, 8));
      const done = prog.done[t.id];
      const at = prog.stage[t.id] ?? 0;
      const status = done ? `★ Terminada${done > 1 ? ` ×${done}` : ''}` : at ? `Capítulo ${at + 1}/${story.stages.length}` : main ? 'Historia original' : `${story.stages.length} partidos`;
      c.add(fitWidth(label(this, x, y + ch * 0.36, status, 10, done ? '#7dff9a' : main ? '#ffd23f' : '#9fb3d1', { fontStyle: 'italic' }).setOrigin(0.5), cw - 18, 8));
      const hit = this.add.zone(x, y, cw - 10, ch - 8).setInteractive({ useHandCursor: true });
      hit.on('pointerup', () => this.showRoute(t.id));
      c.add(hit);
    });
    if (!teams.length) c.add(label(this, GAME_W / 2, top + 80, 'Aún no hay historias de esta temporada.', 16, '#ffffff').setOrigin(0.5));
  }

  // ------------------------------------------------------------- la ruta

  private showRoute(teamId: string): void {
    this.team = teamId;
    const story = this.book[teamId];
    const team = getTeam(teamId);
    const at = loadProgress().stage[teamId] ?? 0;
    const done = loadProgress().done[teamId] ?? 0;
    const c = this.view.removeAll(true);
    c.add(topBar(this, { title: story.title, subtitle: team.name, back: { label: 'Equipos', onClick: () => this.showSelect() }, icon: texKey.emblem(teamId) }));
    const save = loadClub();
    if (save) c.add(coinChip(this, GAME_W - 24, 32, save.coins));
    // ficha
    const g = this.add.graphics();
    const fx = 24;
    const fy = 84;
    const fw = GAME_W - 48;
    const fh = PORTRAIT ? 230 : 170;
    cardPanel(g, fx, fy, fw, fh, { accent: THEME.yellow, alpha: 0.95 });
    glow(g, fx + 90, fy + fh / 2, 120, Phaser.Display.Color.HexStringToColor(team.colors.shirt).color, 0.25);
    c.add(g);
    c.add(this.add.image(fx + 90, fy + fh / 2, texKey.emblem(teamId)).setDisplaySize(120, 120));
    c.add(fitWidth(display(this, fx + 170, fy + 40, story.title, PORTRAIT ? 30 : 38, '#ffd23f').setOrigin(0, 0.5), fw - 190, 18));
    if (story.main) c.add(label(this, fx + 172, fy + 74, 'HISTORIA ORIGINAL', 12, '#0b1a2e', { backgroundColor: '#ffd23f', padding: { x: 6, y: 2 }, fontStyle: 'bold' }).setOrigin(0, 0.5));
    c.add(label(this, fx + 172, fy + (story.main ? 96 : 76), story.summary, PORTRAIT ? 14 : 15, '#dce6f5', { wordWrap: { width: fw - 200 }, lineSpacing: 3 }));
    if (done) c.add(label(this, fx + fw - 20, fy + fh - 18, `★ Ruta terminada${done > 1 ? ` ${done} veces` : ''}`, 13, '#7dff9a', { fontStyle: 'bold' }).setOrigin(1, 0.5));
    // camino de rivales
    const n = story.stages.length;
    const pathTop = fy + fh + (PORTRAIT ? 40 : 34);
    const perRow = PORTRAIT ? Math.min(n, n > 8 ? 5 : 4) : Math.min(n, 10);
    const stepX = (GAME_W - 80) / perRow;
    const rows = Math.ceil(n / perRow);
    // el camino cabe entre la ficha y el rótulo del capítulo: con muchas filas, más juntas y los nodos más pequeños
    const room = GAME_H - (PORTRAIT ? 70 : 56) - (PORTRAIT ? 110 : 90) - pathTop;
    const rowH = Math.min(150, room / rows);
    const k = Math.min(1, rowH / 130, stepX / 100);
    const path = this.add.graphics();
    c.add(path);
    const nodes = story.stages.map((s, i) => {
      const row = Math.floor(i / perRow);
      const col = row % 2 ? perRow - 1 - (i % perRow) : i % perRow;
      return { x: 40 + stepX * col + stepX / 2, y: pathTop + 50 * k + row * rowH, s, i };
    });
    path.lineStyle(6, 0xffffff, 0.15);
    for (let i = 1; i < nodes.length; i++) path.lineBetween(nodes[i - 1].x, nodes[i - 1].y, nodes[i].x, nodes[i].y);
    path.lineStyle(6, THEME.yellow, 0.9);
    for (let i = 1; i <= Math.min(at, nodes.length - 1); i++) path.lineBetween(nodes[i - 1].x, nodes[i - 1].y, nodes[i].x, nodes[i].y);
    for (const nd of nodes) {
      const cleared = nd.i < at;
      const current = nd.i === at;
      const r = (current ? 42 : 34) * k;
      const ng = this.add.graphics();
      if (current) glow(ng, nd.x, nd.y, 70 * k, THEME.yellow, 0.3);
      ng.fillStyle(cleared ? 0x1f6a3a : current ? 0x3a2a08 : 0x0b1a2e, 1).fillCircle(nd.x, nd.y, r);
      ng.lineStyle(3, cleared ? 0x7dff9a : current ? THEME.yellow : 0xffffff, current ? 1 : 0.35).strokeCircle(nd.x, nd.y, r);
      c.add(ng);
      let opp: TeamData | null = null;
      try {
        opp = getTeam(nd.s.opponent);
      } catch {
        // rival desconocido
      }
      const img = this.add.image(nd.x, nd.y, texKey.emblem(nd.s.opponent)).setDisplaySize(r * 1.5, r * 1.5);
      if (!cleared && !current) img.setAlpha(0.55);
      c.add(img);
      c.add(label(this, nd.x - r + 4, nd.y - r + 4, String(nd.i + 1), 13, '#0b1a2e', { backgroundColor: cleared ? '#7dff9a' : '#ffd23f', padding: { x: 5, y: 1 }, fontStyle: 'bold' }).setOrigin(0.5));
      if (cleared) c.add(label(this, nd.x + r - 6, nd.y + r - 8, '✓', 20, '#7dff9a', { fontStyle: 'bold', stroke: '#000000', strokeThickness: 4 }).setOrigin(0.5));
      c.add(fitWidth(label(this, nd.x, nd.y + r + 14, opp?.name ?? nd.s.opponent, 11, current ? '#ffd23f' : '#ffffff', { fontStyle: 'bold', align: 'center' }).setOrigin(0.5), stepX - 8, 8));
      if (current) this.tweens.add({ targets: img, scale: img.scale * 1.08, duration: 700, yoyo: true, repeat: -1, ease: 'Sine.InOut' });
    }
    // capítulo actual y botones
    const cur = story.stages[at];
    const by = GAME_H - (PORTRAIT ? 70 : 56);
    c.add(fitWidth(label(this, GAME_W / 2, by - (PORTRAIT ? 70 : 56), `Capítulo ${at + 1}: ${cur.title}`, PORTRAIT ? 18 : 20, '#ffffff', { fontStyle: 'bold italic' }).setOrigin(0.5), GAME_W - 40, 12));
    c.add(new Button(this, GAME_W / 2 + (at ? (PORTRAIT ? 90 : 110) : 0), by, at ? 'Continuar' : '¡Empezar!', () => void this.playStage(), { variant: 'primary', w: PORTRAIT ? 300 : 260, h: PORTRAIT ? 70 : 56, size: PORTRAIT ? 24 : 22, hint: PORTRAIT ? undefined : '⏎' }));
    if (at) {
      c.add(
        new Button(this, GAME_W / 2 - (PORTRAIT ? 175 : 150), by, 'Desde el principio', () => {
          setStage(teamId, 0);
          this.showRoute(teamId);
        }, { variant: 'secondary', w: PORTRAIT ? 150 : 190, h: PORTRAIT ? 70 : 56, size: PORTRAIT ? 14 : 16 }),
      );
    }
    this.input.keyboard?.removeAllListeners('keydown-ENTER');
    this.input.keyboard?.on('keydown-ENTER', () => this.team === teamId && !this.busy && void this.playStage());
  }

  /** Diálogo de antes y al partido. */
  private async playStage(): Promise<void> {
    if (this.busy || !this.team) return;
    this.busy = true;
    const teamId = this.team;
    const story = this.book[teamId];
    const at = loadProgress().stage[teamId] ?? 0;
    const stage = story.stages[at];
    sfx.click();
    if (at === 0 && story.intro.length) await this.dialogue(story.intro, teamId, story.title);
    await this.dialogue(stage.before, teamId, `Capítulo ${at + 1}: ${stage.title}`);
    const home = getTeam(teamId);
    const away = getTeam(stage.opponent);
    const wait = label(this, GAME_W / 2, GAME_H / 2, 'Cargando jugadores…', 18, '#ffffff', { backgroundColor: '#0b1a2ecc', padding: { x: 10, y: 4 } }).setOrigin(0.5).setDepth(900);
    await ensureSprites(this.textures, [home, away]).catch(() => {});
    wait.destroy();
    this.registry.set(STORY_REGISTRY, { team: teamId, stage: at } satisfies StoryMatch);
    this.scene.start('formation', { home: defaultLineup(home), away: defaultLineup(away) });
  }

  /** Vuelta de un partido: si se ha ganado, el diálogo de después y el siguiente capítulo (o el final). */
  private async afterMatch(res: StoryMatch & { won: boolean }): Promise<void> {
    const story = this.book[res.team];
    const stage = story.stages[res.stage];
    if (!res.won) {
      this.showRoute(res.team);
      toast(this, 'Hay que ganar para seguir con la historia. ¡Inténtalo otra vez!', THEME.coral, 2600);
      return;
    }
    this.busy = true;
    this.view.removeAll(true);
    await this.dialogue(stage.after, res.team, `Capítulo ${res.stage + 1}: ${stage.title}`);
    if (res.stage + 1 >= story.stages.length) {
      await this.dialogue(story.ending, res.team, 'Final');
      const first = !(loadProgress().done[res.team] ?? 0);
      finishRoute(res.team);
      const coins = first ? ROUTE_COINS.first : ROUTE_COINS.again;
      const save = loadClub();
      if (save) saveClub({ ...save, coins: save.coins + coins });
      this.busy = false;
      this.showRoute(res.team);
      this.celebrate(story, coins);
      return;
    }
    setStage(res.team, res.stage + 1);
    this.busy = false;
    this.showRoute(res.team);
  }

  private celebrate(story: Story, coins: number): void {
    const c = this.add.container(0, 0).setDepth(800);
    c.add(this.add.rectangle(0, 0, GAME_W, GAME_H, 0x000000, 0.75).setOrigin(0).setInteractive());
    const g = this.add.graphics();
    glow(g, GAME_W / 2, GAME_H / 2 - 40, 300, THEME.yellow, 0.25);
    c.add(g);
    c.add(fitWidth(display(this, GAME_W / 2, GAME_H / 2 - 90, '¡RUTA COMPLETADA!', PORTRAIT ? 48 : 64, '#ffd23f').setOrigin(0.5), GAME_W - 40, 28));
    c.add(fitWidth(label(this, GAME_W / 2, GAME_H / 2 - 20, story.title, 22, '#ffffff', { fontStyle: 'bold italic' }).setOrigin(0.5), GAME_W - 40, 14));
    c.add(label(this, GAME_W / 2, GAME_H / 2 + 24, `+${coins} monedas para Mi club`, 18, '#0b1a2e', { backgroundColor: '#ffd23f', padding: { x: 12, y: 5 }, fontStyle: 'bold' }).setOrigin(0.5));
    c.add(new Button(this, GAME_W / 2, GAME_H / 2 + 110, '¡Genial!', () => c.destroy(), { variant: 'primary', w: 220, h: 56, size: 22 }));
    sfx.win();
    c.setAlpha(0);
    this.tweens.add({ targets: c, alpha: 1, duration: 300 });
  }

  // ------------------------------------------------------------- diálogos

  private speaker(line: StoryLine): { name: string; team?: TeamData; portrait?: string } {
    if (line.who) {
      const [t, p] = line.who.split('/');
      try {
        const team = getTeam(t);
        const pl = team.players.find((x) => x.id === p);
        return { name: pl?.name ?? p, team, portrait: texKey.portrait(p, t) };
      } catch {
        return { name: p ?? line.who };
      }
    }
    return { name: line.name ?? '' };
  }

  /** Muestra unas líneas de diálogo (tocar o Intro para avanzar; "Saltar" para pasarlas todas). */
  private async dialogue(lines: StoryLine[], hero: string, title: string): Promise<void> {
    if (!lines.length) return;
    // retratos de los que hablan
    const want = lines.filter((l) => l.who).map((l) => ({ team: l.who!.split('/')[0], id: l.who!.split('/')[1] }));
    const missing = portraitsOf(want).filter((e) => !this.textures.exists(e.key));
    if (missing.length) {
      await new Promise<void>((resolve) => {
        for (const e of missing) this.load.image(e.key, e.url);
        this.load.once(Phaser.Loader.Events.COMPLETE, () => resolve());
        this.load.start();
      });
    }
    return new Promise((resolve) => {
      const c = this.add.container(0, 0).setDepth(700);
      c.add(this.add.rectangle(0, 0, GAME_W, GAME_H, 0x000000, 0.6).setOrigin(0).setInteractive());
      const boxH = PORTRAIT ? 230 : 170;
      const boxY = GAME_H - boxH - (PORTRAIT ? 30 : 20);
      const boxX = PORTRAIT ? 16 : 120;
      const boxW = GAME_W - boxX * 2;
      c.add(label(this, GAME_W / 2, PORTRAIT ? 70 : 50, title, PORTRAIT ? 18 : 20, '#ffd23f', { fontStyle: 'bold italic', stroke: '#000000', strokeThickness: 4 }).setOrigin(0.5));
      const portraitL = this.add.image(PORTRAIT ? 130 : 260, boxY - 10, '__DEFAULT').setOrigin(0.5, 1).setVisible(false);
      const portraitR = this.add.image(GAME_W - (PORTRAIT ? 130 : 260), boxY - 10, '__DEFAULT').setOrigin(0.5, 1).setVisible(false);
      c.add([portraitL, portraitR]);
      const box = this.add.graphics();
      c.add(box);
      const nameText = label(this, 0, 0, '', PORTRAIT ? 18 : 18, '#0b1a2e', { fontStyle: 'bold' }).setOrigin(0, 0.5);
      const body = label(this, boxX + 28, boxY + 30, '', PORTRAIT ? 19 : 19, '#ffffff', { wordWrap: { width: boxW - 56 }, lineSpacing: 6 });
      const more = label(this, boxX + boxW - 26, boxY + boxH - 20, '▼', 18, '#ffd23f').setOrigin(0.5);
      this.tweens.add({ targets: more, y: more.y + 5, duration: 450, yoyo: true, repeat: -1 });
      c.add([nameText, body, more]);
      const skip = new Button(this, GAME_W - (PORTRAIT ? 70 : 90), PORTRAIT ? 70 : 50, 'Saltar ▶▶', () => finish(), { variant: 'secondary', w: PORTRAIT ? 120 : 140, h: 40, size: 15 });
      c.add(skip);
      let i = -1;
      let full = '';
      let typing: Phaser.Time.TimerEvent | null = null;
      const finish = () => {
        typing?.remove();
        this.input.keyboard?.off('keydown-ENTER', advance);
        this.input.keyboard?.off('keydown-SPACE', advance);
        c.destroy();
        resolve();
      };
      const draw = (sp: ReturnType<StoryScene['speaker']>, left: boolean) => {
        box.clear();
        box.fillStyle(0x000000, 0.4).fillRoundedRect(boxX + 4, boxY + 6, boxW, boxH, 16);
        box.fillStyle(0x0b1a2e, 0.96).fillRoundedRect(boxX, boxY, boxW, boxH, 16);
        const accent = sp.team ? Phaser.Display.Color.HexStringToColor(sp.team.colors.shirt).color : 0x9fb3d1;
        box.lineStyle(3, accent, 0.9).strokeRoundedRect(boxX, boxY, boxW, boxH, 16);
        nameText.setVisible(!!sp.name);
        if (sp.name) {
          nameText.setText(sp.name);
          const nw = nameText.width + 36;
          const nx = left ? boxX + 20 : boxX + boxW - 20 - nw;
          box.fillStyle(accent, 1).fillPoints([pt(nx + 10, boxY - 20), pt(nx + nw + 10, boxY - 20), pt(nx + nw, boxY + 14), pt(nx, boxY + 14)], true);
          nameText.setPosition(nx + 20, boxY - 3).setColor(lumaOf(accent) > 150 ? '#0b1a2e' : '#ffffff');
        }
        body.setFontStyle(sp.name ? 'normal' : 'italic');
      };
      const show = () => {
        const line = lines[i];
        const sp = this.speaker(line);
        const left = !sp.team || sp.team.id === hero;
        draw(sp, left);
        const img = left ? portraitL : portraitR;
        const other = left ? portraitR : portraitL;
        other.setAlpha(0.35);
        if (sp.portrait && this.textures.exists(sp.portrait)) {
          img.setTexture(sp.portrait).setDisplaySize(PORTRAIT ? 200 : 240, PORTRAIT ? 200 : 240).setVisible(true).setAlpha(1);
          img.setFlipX(!left);
        } else if (sp.name || !line.who) {
          if (!sp.portrait) img.setAlpha(0.35);
        }
        full = line.text;
        body.setText('');
        let k = 0;
        typing?.remove();
        typing = this.time.addEvent({
          delay: 18,
          repeat: full.length - 1,
          callback: () => {
            k++;
            body.setText(full.slice(0, k));
            if (k >= full.length) typing = null;
          },
        });
      };
      const advance = () => {
        if (typing) {
          typing.remove();
          typing = null;
          body.setText(full);
          return;
        }
        i++;
        if (i >= lines.length) return finish();
        sfx.click();
        show();
      };
      c.list[0].on('pointerup', advance);
      this.input.keyboard?.on('keydown-ENTER', advance);
      this.input.keyboard?.on('keydown-SPACE', advance);
      advance();
    });
  }
}

function lumaOf(c: number): number {
  return 0.299 * ((c >> 16) & 255) + 0.587 * ((c >> 8) & 255) + 0.114 * (c & 255);
}
