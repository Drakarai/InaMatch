import Phaser from "phaser";
import { music } from "../audio/music";
import { fitCamera } from "../ui/theme";
import { soundButton } from "../ui/soundPanel";
import { GAME_H, GAME_W, hex } from "../config";
import { TEAMS } from "../data";
import { SEASONS, getSeason, seasonOf } from "../data/seasons";
import type { TeamData } from "../data/types";
import { defaultLineup } from "../engine/lineup";
import { lineRatings, teamRating } from "../engine/rating";
import { Button, display, text } from "../ui/widgets";
import { loadClub } from "../club/club";
import { makeEmblem, texKey } from "../gfx/placeholders";

type Side = "home" | "away";

interface Selection {
  home: string;
  away: string;
  /** Lado que se está eligiendo desde la estantería de escudos. */
  focus: Side;
}

// Pantalla de "versus": cada mitad con los colores de su equipo, partidas por un rayo.
const CX = { home: 330, away: 950 } as const;
const EMBLEM_Y = 196;
const EMBLEM = 140;
const SHELF_Y = 446;
/** Azul de la enciclopedia oficial, fondo de los logos de cada juego. */
const ZUKAN_BLUE = 0x1d7ce0;
const NIGHT = 0x0a1120;
const YELLOW = 0xffd23f;
const SIDE = {
  home: { label: "TÚ", color: 0x2f7bff, css: "#7fb2ff" },
  away: { label: "RIVAL", color: 0xff3b4e, css: "#ff8f9a" },
} as const;
/** El rayo que parte la pantalla: puntos de arriba abajo. */
const BOLT = [
  [700, 0],
  [654, 128],
  [690, 136],
  [622, 280],
  [664, 288],
  [600, SHELF_Y],
] as const;

const seasonsWithTeams = () =>
  SEASONS.filter((s) => TEAMS.some((t) => seasonOf(t) === s.id));
const teamsOf = (season: string) =>
  TEAMS.filter((t) => seasonOf(t) === season).sort((a, b) =>
    a.name.localeCompare(b.name, "es"),
  );
const teamById = (id: string) => TEAMS.find((t) => t.id === id)!;
const pt = (x: number, y: number) => new Phaser.Geom.Point(x, y);
/** Color del equipo oscurecido para el fondo, que el texto se lea siempre. */
const dim = (color: string, amount = 0.62) => {
  const c = Phaser.Display.Color.Interpolate.ColorWithColor(
    Phaser.Display.Color.ValueToColor(hex(color)),
    Phaser.Display.Color.ValueToColor(NIGHT),
    100,
    amount * 100,
  );
  return Phaser.Display.Color.GetColor(c.r, c.g, c.b);
};

export class MenuScene extends Phaser.Scene {
  private sel!: Selection;
  private shelfSeason!: string;
  private bg!: Phaser.GameObjects.Graphics;
  private sides!: Record<Side, Phaser.GameObjects.Container>;
  private shelf!: Phaser.GameObjects.Container;

  constructor() {
    super("menu");
  }

  create(): void {
    fitCamera(this);
    music.play("menu");
    const club = TEAMS.find((t) => t.id === "club");
    if (club) makeEmblem(this, club);
    const saved = this.registry.get("menuSelection") as Selection | undefined;
    this.sel =
      saved &&
      TEAMS.some((t) => t.id === saved.home) &&
      TEAMS.some((t) => t.id === saved.away)
        ? { ...saved }
        : this.defaults();
    this.shelfSeason = seasonOf(teamById(this.sel[this.sel.focus]));

    this.bg = this.add.graphics();
    this.drawSplit();
    this.drawBolt();
    this.sides = {
      home: this.add.container(0, 0),
      away: this.add.container(0, 0),
    };
    this.shelf = this.add.container(0, 0);
    this.drawHeader();
    this.drawCenter();
    this.renderSide("home");
    this.renderSide("away");
    this.renderShelf();
    this.bindKeys();
    soundButton(this, GAME_W - 34, 96, GAME_W - 350, 120);
    // Mi club y fichajes
    const clubBtn = new Button(
      this,
      470,
      40,
      "⚡ Mi club",
      () => this.scene.start("club"),
      { w: 170, h: 44, color: 0xff7a3d },
    );
    const gachaBtn = new Button(
      this,
      650,
      40,
      "Fichajes",
      () => this.scene.start("gacha"),
      { w: 160, h: 44, color: YELLOW },
    );
    const coins = text(this, 760, 40, "", 16, "#ffd23f", {
      fontStyle: "bold",
      strokeThickness: 4,
    }).setOrigin(0, 0.5);
    coins.setText(`● ${loadClub()?.coins ?? 0}`);
    if (!loadClub())
      [clubBtn, gachaBtn, coins].forEach((o) => o.setVisible(false));
  }

  private defaults(): Selection {
    const home = TEAMS.find((t) => t.id === "ie3-inazuma-japan") ?? TEAMS[0];
    const away =
      TEAMS.find((t) => t.id === "ie3-desert-lion") ??
      TEAMS.find((t) => t !== home) ??
      home;
    return { home: home.id, away: away.id, focus: "away" };
  }

  // ----------------------------------------------------------------- fondo

  /** Las dos mitades con el color de cada equipo, tramado de puntos y líneas de velocidad, como en una viñeta. */
  private drawSplit(): void {
    const g = this.bg.clear();
    const home = teamById(this.sel.home);
    const away = teamById(this.sel.away);
    g.fillStyle(NIGHT).fillRect(0, 0, GAME_W, GAME_H);
    const left = [pt(0, 0), ...BOLT.map(([x, y]) => pt(x, y)), pt(0, SHELF_Y)];
    const right = [
      pt(GAME_W, 0),
      ...BOLT.map(([x, y]) => pt(x, y)),
      pt(GAME_W, SHELF_Y),
    ];
    g.fillStyle(dim(home.colors.shirt)).fillPoints(left, true);
    g.fillStyle(dim(away.colors.shirt)).fillPoints(right, true);
    // líneas de velocidad que salen de cada escudo
    for (const [side, team] of [
      ["home", home],
      ["away", away],
    ] as const) {
      g.lineStyle(2, hex(team.colors.accent), 0.16);
      for (let i = 0; i < 28; i++) {
        const a = (i / 28) * Math.PI * 2;
        const r0 = 128 + (i % 3) * 20;
        g.lineBetween(
          CX[side] + Math.cos(a) * r0,
          EMBLEM_Y + Math.sin(a) * r0,
          CX[side] + Math.cos(a) * 520,
          EMBLEM_Y + Math.sin(a) * 520,
        );
      }
    }
    // trama de puntos, más densa hacia el borde de abajo
    for (let y = 250; y < SHELF_Y; y += 14) {
      const r = ((y - 250) / (SHELF_Y - 250)) * 2.6;
      g.fillStyle(0x000000, 0.22);
      for (let x = (y / 14) % 2 ? 7 : 0; x < GAME_W; x += 14)
        g.fillCircle(x, y, r);
    }
    // sombra arriba para el título
    g.fillGradientStyle(
      0x000000,
      0x000000,
      0x000000,
      0x000000,
      0.55,
      0.55,
      0,
      0,
    ).fillRect(0, 0, GAME_W, 90);
  }

  private drawBolt(): void {
    const g = this.add.graphics();
    const line = (width: number, color: number, alpha: number) => {
      g.lineStyle(width, color, alpha).beginPath();
      BOLT.forEach(([x, y], i) => (i ? g.lineTo(x, y) : g.moveTo(x, y)));
      g.strokePath();
    };
    line(26, YELLOW, 0.12);
    line(12, YELLOW, 0.35);
    line(5, 0xfff6c8, 1);
    this.tweens.add({
      targets: g,
      alpha: 0.7,
      duration: 900,
      yoyo: true,
      repeat: -1,
      ease: "Sine.inOut",
    });
  }

  private drawHeader(): void {
    const g = this.add.graphics();
    g.fillStyle(YELLOW).fillPoints(
      [
        pt(24, 18),
        pt(44, 18),
        pt(36, 34),
        pt(46, 34),
        pt(26, 60),
        pt(31, 40),
        pt(20, 40),
      ],
      true,
    );
    display(this, 54, 8, "InaMatch", 46);
    text(this, 56, 58, "¡Elige a los equipos!", 15, "#ffffff", {
      fontStyle: "italic",
    });
    text(
      this,
      GAME_W - 24,
      30,
      "Proyecto de fans sin ánimo de lucro\nInazuma Eleven es una marca de LEVEL-5",
      11,
      "#c4cddc",
      {
        align: "right",
        strokeThickness: 3,
      },
    ).setOrigin(1, 0.5);
  }

  // ------------------------------------------------------------------ lados

  private renderSide(side: Side): void {
    const c = this.sides[side];
    this.tweens.killTweensOf(c.list);
    c.removeAll(true);
    const cx = CX[side];
    const team = teamById(this.sel[side]);
    const s = SIDE[side];
    const choosing = this.sel.focus === side;

    // destello giratorio detrás del escudo
    const rays = this.add.graphics({ x: cx, y: EMBLEM_Y });
    for (let i = 0; i < 16; i++) {
      const a = (i / 16) * Math.PI * 2;
      rays.fillStyle(
        i % 2 ? 0xffffff : hex(team.colors.accent),
        i % 2 ? 0.07 : 0.22,
      );
      rays.fillTriangle(
        0,
        0,
        Math.cos(a - 0.12) * 128,
        Math.sin(a - 0.12) * 128,
        Math.cos(a + 0.12) * 128,
        Math.sin(a + 0.12) * 128,
      );
    }
    rays.fillStyle(0x000000, 0.28).fillCircle(0, 0, 82);
    rays
      .lineStyle(4, choosing ? YELLOW : 0xffffff, choosing ? 0.9 : 0.35)
      .strokeCircle(0, 0, 82);
    this.tweens.add({
      targets: rays,
      angle: side === "home" ? 360 : -360,
      duration: 40000,
      repeat: -1,
    });
    c.add(rays);

    const emblem = this.add
      .image(cx, EMBLEM_Y, texKey.emblem(team.id))
      .setDisplaySize(EMBLEM, EMBLEM);
    c.add(emblem);

    // etiqueta TÚ / RIVAL, inclinada, encima del escudo
    const tag = this.add.graphics();
    tag
      .fillStyle(s.color)
      .fillPoints(
        [pt(cx - 54, 84), pt(cx + 62, 84), pt(cx + 52, 108), pt(cx - 64, 108)],
        true,
      );
    c.add(tag);
    c.add(
      text(this, cx - 1, 96, s.label, 16, "#ffffff", {
        fontStyle: "italic bold",
      }).setOrigin(0.5),
    );

    // media en un hexágono, a un lado del escudo
    const hx = cx + (side === "home" ? -112 : 112);
    const hy = EMBLEM_Y - 58;
    const hexG = this.add.graphics();
    const hexPts = Array.from({ length: 6 }, (_, i) =>
      pt(
        hx + Math.cos((i * Math.PI) / 3) * 34,
        hy + Math.sin((i * Math.PI) / 3) * 34,
      ),
    );
    hexG.fillStyle(NIGHT, 0.9).fillPoints(hexPts, true);
    hexG.lineStyle(3, YELLOW).strokePoints(hexPts, true);
    c.add(hexG);
    c.add(
      text(this, hx, hy - 9, String(teamRating(team)), 24, "#ffd23f", {
        fontStyle: "bold",
      }).setOrigin(0.5),
    );
    c.add(text(this, hx, hy + 15, "MEDIA", 10, "#ffffff").setOrigin(0.5));

    // flechas
    for (const dir of [-1, 1]) {
      const ax = cx + dir * 150;
      const arrow = this.add.graphics();
      const draw = (hover: boolean) => {
        arrow.clear().fillStyle(hover ? YELLOW : 0xffffff, hover ? 1 : 0.85);
        arrow.fillPoints(
          [
            pt(ax + dir * 16, EMBLEM_Y),
            pt(ax - dir * 10, EMBLEM_Y - 22),
            pt(ax - dir * 10, EMBLEM_Y + 22),
          ],
          true,
        );
      };
      draw(false);
      const zone = this.add
        .zone(ax - 24, EMBLEM_Y - 34, 48, 68)
        .setOrigin(0)
        .setInteractive({ useHandCursor: true });
      zone
        .on("pointerover", () => draw(true))
        .on("pointerout", () => draw(false));
      zone.on("pointerdown", () => this.cycle(side, dir));
      c.add([arrow, zone]);
    }

    // nombre en una banda blanca inclinada, como los rótulos del anime
    const band = this.add.graphics();
    band
      .fillStyle(0x000000, 0.35)
      .fillPoints(
        [
          pt(cx - 196, 294),
          pt(cx + 214, 294),
          pt(cx + 202, 338),
          pt(cx - 208, 338),
        ],
        true,
      );
    band
      .fillStyle(0xffffff)
      .fillPoints(
        [
          pt(cx - 200, 288),
          pt(cx + 210, 288),
          pt(cx + 198, 332),
          pt(cx - 212, 332),
        ],
        true,
      );
    band
      .fillStyle(hex(team.colors.accent))
      .fillPoints(
        [
          pt(cx - 212, 332),
          pt(cx + 198, 332),
          pt(cx + 196, 338),
          pt(cx - 214, 338),
        ],
        true,
      );
    c.add(band);
    const name = display(this, cx - 2, 311, team.name, 34, "#0b1a2e", {
      strokeThickness: 0,
      shadow: { offsetX: 0, offsetY: 0, color: "#000", blur: 0, fill: false },
    }).setOrigin(0.5);
    for (let size = 34; name.width > 380 && size > 14; )
      name.setFontSize(--size);
    c.add(name);
    // de qué juego es, con su logo
    const list = teamsOf(seasonOf(team));
    const season = getSeason(seasonOf(team));
    const info = text(
      this,
      cx + 14,
      356,
      `${season.name}  ·  ${list.indexOf(team) + 1}/${list.length}`,
      13,
      "#e3e9f2",
      { fontStyle: "italic" },
    ).setOrigin(0.5);
    c.add(info);
    if (season.icon && this.textures.exists(`series:${season.icon}`)) {
      c.add(
        this.add
          .image(info.x - info.width / 2 - 16, 356, `series:${season.icon}`)
          .setDisplaySize(22, 23),
      );
    }

    // barras de línea, como las de FP/TP del partido
    const lines = lineRatings(team);
    const rows = [
      ["Ataque", lines.att, 0xff7a3d],
      ["Medio", lines.mid, 0x46d68c],
      ["Defensa", lines.def, 0x4fa3ff],
    ] as const;
    rows.forEach(([label, value, color], i) => {
      const y = 384 + i * 20;
      const x0 = cx - 150;
      const bar = this.add.graphics();
      bar
        .fillStyle(0x000000, 0.45)
        .fillPoints(
          [
            pt(x0 + 86, y - 5),
            pt(x0 + 266, y - 5),
            pt(x0 + 263, y + 5),
            pt(x0 + 83, y + 5),
          ],
          true,
        );
      const w = Phaser.Math.Clamp((value - 30) / 60, 0.05, 1) * 180;
      bar
        .fillStyle(color)
        .fillPoints(
          [
            pt(x0 + 86, y - 5),
            pt(x0 + 86 + w, y - 5),
            pt(x0 + 83 + w, y + 5),
            pt(x0 + 83, y + 5),
          ],
          true,
        );
      c.add(bar);
      c.add(
        text(this, x0, y, label, 13, "#ffffff", {
          fontStyle: "italic bold",
        }).setOrigin(0, 0.5),
      );
      c.add(
        text(this, x0 + 300, y, String(value), 14, "#ffffff", {
          fontStyle: "bold",
        }).setOrigin(1, 0.5),
      );
    });

    // pulsar en cualquier parte de la mitad la elige para la estantería
    const hit = this.add
      .zone(cx - 250, 80, 500, SHELF_Y - 90)
      .setOrigin(0)
      .setInteractive();
    hit.on("pointerdown", () => this.setFocus(side));
    hit.on("wheel", (_p: Phaser.Input.Pointer, _dx: number, dy: number) =>
      this.cycle(side, dy > 0 ? 1 : -1),
    );
    c.add(hit);
    c.sendToBack(hit);
  }

  // ----------------------------------------------------------------- centro

  private drawCenter(): void {
    const vs = display(this, 646, EMBLEM_Y - 6, "VS", 110, "#ffd23f", {
      strokeThickness: 12,
    }).setOrigin(0.5);
    this.tweens.add({
      targets: vs,
      scale: 1.06,
      duration: 700,
      yoyo: true,
      repeat: -1,
      ease: "Sine.inOut",
    });

    const round = (
      x: number,
      y: number,
      icon: string,
      hint: string,
      onClick: () => void,
    ) => {
      const g = this.add.graphics();
      const draw = (hover: boolean) => {
        g.clear()
          .fillStyle(hover ? YELLOW : NIGHT, 0.92)
          .fillCircle(x, y, 27);
        g.lineStyle(3, YELLOW).strokeCircle(x, y, 27);
      };
      draw(false);
      const label = text(this, x, y, icon, 22, "#ffffff").setOrigin(0.5);
      const tip = text(this, x, y + 42, hint, 12, "#ffffff", {
        fontStyle: "italic",
      })
        .setOrigin(0.5)
        .setAlpha(0);
      this.add
        .zone(x - 28, y - 28, 56, 56)
        .setOrigin(0)
        .setInteractive({ useHandCursor: true })
        .on(
          "pointerover",
          () => (draw(true), label.setColor("#0b1a2e"), tip.setAlpha(1)),
        )
        .on(
          "pointerout",
          () => (draw(false), label.setColor("#ffffff"), tip.setAlpha(0)),
        )
        .on("pointerdown", onClick);
    };
    round(610, 296, "⇄", "Cambiar lados", () => this.swap());
    round(680, 296, "⚄", "Rival aleatorio", () => this.randomRival());

    // botón principal: un rayo con el texto
    const bx = 640;
    const by = 392;
    const g = this.add.graphics();
    const shape = (dx: number, dy: number) => [
      pt(bx - 112 + dx, by - 30 + dy),
      pt(bx + 126 + dx, by - 30 + dy),
      pt(bx + 112 + dx, by + 30 + dy),
      pt(bx - 126 + dx, by + 30 + dy),
    ];
    const draw = (hover: boolean) => {
      g.clear().fillStyle(0x000000, 0.5).fillPoints(shape(5, 6), true);
      g.fillStyle(hover ? 0xffe27a : YELLOW).fillPoints(shape(0, 0), true);
      g.fillStyle(0xffffff, 0.35).fillPoints(
        [
          pt(bx - 108, by - 26),
          pt(bx + 121, by - 26),
          pt(bx + 117, by - 6),
          pt(bx - 113, by - 6),
        ],
        true,
      );
    };
    draw(false);
    text(this, bx, by, "¡A la formación!", 22, "#0b1a2e", {
      fontStyle: "italic bold",
      strokeThickness: 0,
    }).setOrigin(0.5);
    this.add
      .zone(bx - 126, by - 30, 252, 60)
      .setOrigin(0)
      .setInteractive({ useHandCursor: true })
      .on("pointerover", () => draw(true))
      .on("pointerout", () => draw(false))
      .on("pointerdown", () => this.next());
  }

  // ------------------------------------------------------------- estantería

  /**
   * Abajo: una fila con el logo de cada juego de la saga (los de la enciclopedia oficial) y, debajo, todos los
   * escudos del juego elegido, en hasta tres filas, para elegir de un vistazo.
   */
  private renderShelf(): void {
    const c = this.shelf;
    this.tweens.killTweensOf(c.list);
    c.removeAll(true);
    const g = this.add.graphics();
    g.fillStyle(0x060b15, 0.96).fillPoints(
      [
        pt(0, SHELF_Y + 12),
        pt(GAME_W, SHELF_Y - 8),
        pt(GAME_W, GAME_H),
        pt(0, GAME_H),
      ],
      true,
    );
    g.lineStyle(3, YELLOW, 0.9).lineBetween(
      0,
      SHELF_Y + 12,
      GAME_W,
      SHELF_Y - 8,
    );
    // banda azul de los logos, como la barra de juegos de la enciclopedia
    g.fillStyle(ZUKAN_BLUE, 0.22).fillRect(0, SHELF_Y + 22, GAME_W, 74);
    g.fillStyle(ZUKAN_BLUE, 0.6).fillRect(0, SHELF_Y + 94, GAME_W, 2);
    c.add(g);

    // logos de los juegos
    const seasons = seasonsWithTeams();
    const step = Math.min(84, (GAME_W - 420) / seasons.length);
    const x0 = 28 + step / 2;
    const ty = SHELF_Y + 59;
    seasons.forEach((s, i) => {
      const x = x0 + i * step;
      const on = s.id === this.shelfSeason;
      const tile = this.add.graphics();
      const draw = (hover: boolean) => {
        const w = step - 10;
        const pts = [
          pt(x - w / 2 + 8, ty - 32),
          pt(x + w / 2 + 2, ty - 32),
          pt(x + w / 2 - 8, ty + 32),
          pt(x - w / 2 - 2, ty + 32),
        ];
        tile.clear();
        tile.fillStyle(0x000000, 0.4).fillPoints(
          pts.map((p) => pt(p.x + 3, p.y + 4)),
          true,
        );
        tile
          .fillStyle(
            on
              ? YELLOW
              : s.id === "club"
                ? 0xff7a3d
                : hover
                  ? 0x3b95f0
                  : ZUKAN_BLUE,
          )
          .fillPoints(pts, true);
        tile
          .fillStyle(0xffffff, on ? 0.35 : 0.16)
          .fillPoints(
            [
              pts[0],
              pts[1],
              pt(pts[1].x - 3, ty - 20),
              pt(pts[0].x - 3, ty - 20),
            ],
            true,
          );
        if (on) tile.lineStyle(3, 0xffffff).strokePoints(pts, true);
      };
      draw(false);
      c.add(tile);
      if (s.icon && this.textures.exists(`series:${s.icon}`)) {
        const icon = this.add
          .image(x, ty - 2, `series:${s.icon}`)
          .setDisplaySize(50, 53);
        if (on) icon.setTint(0x0b1a2e);
        c.add(icon);
      } else if (s.id === "club") {
        c.add(
          this.add
            .image(x, ty - 8, texKey.emblem("club"))
            .setDisplaySize(36, 36),
        );
        c.add(
          text(this, x, ty + 20, "MI CLUB", 11, on ? "#0b1a2e" : "#ffffff", {
            fontStyle: "bold",
            strokeThickness: on ? 0 : 3,
          }).setOrigin(0.5),
        );
      } else {
        c.add(
          display(this, x, ty - 4, s.short, 34, on ? "#0b1a2e" : "#ffffff", {
            strokeThickness: 0,
            shadow: {
              offsetX: 0,
              offsetY: 0,
              color: "#000",
              blur: 0,
              fill: false,
            },
          }).setOrigin(0.5),
        );
      }
      const zone = this.add
        .zone(x - step / 2, ty - 34, step, 68)
        .setOrigin(0)
        .setInteractive({ useHandCursor: true });
      zone.on(
        "pointerover",
        () => (
          on ? null : draw(true),
          tip
            .setText(`${s.name} · ${teamsOf(s.id).length}`)
            .setPosition(Phaser.Math.Clamp(x, 120, GAME_W - 120), ty - 46)
            .setVisible(true),
          c.bringToTop(tip)
        ),
      );
      zone.on("pointerout", () => (draw(false), tip.setVisible(false)));
      zone.on("pointerdown", () => {
        this.shelfSeason = s.id;
        this.renderShelf();
      });
      c.add(zone);
    });

    // a la derecha: el juego elegido y para qué lado se elige
    const season = getSeason(this.shelfSeason);
    const teams = teamsOf(this.shelfSeason);
    const rx = GAME_W - 26;
    const title = display(this, rx, ty - 14, season.name, 30, "#ffffff", {
      strokeThickness: 5,
    }).setOrigin(1, 0.5);
    for (let size = 30; title.width > 360 && size > 16; )
      title.setFontSize(--size);
    c.add(title);
    const who = SIDE[this.sel.focus];
    const whoText = text(this, rx, ty + 16, who.label, 15, who.css, {
      fontStyle: "italic bold",
    }).setOrigin(1, 0.5);
    c.add(whoText);
    c.add(
      text(
        this,
        rx - whoText.width - 6,
        ty + 16,
        `${teams.length} ${teams.length === 1 ? "equipo" : "equipos"}  ·  eligiendo:`,
        13,
        "#c9d3e0",
        { fontStyle: "italic" },
      ).setOrigin(1, 0.5),
    );

    // escudos del juego: hasta tres filas, centradas
    const rows = teams.length > 30 ? 3 : teams.length > 15 ? 2 : 1;
    const perRow = Math.ceil(teams.length / rows);
    const size = rows === 3 ? 44 : rows === 2 ? 50 : 56;
    const stepX = Math.min(size + 20, (GAME_W - 60) / perRow);
    const area = { top: SHELF_Y + 104, bottom: GAME_H - 6 };
    const stepY = (area.bottom - area.top) / rows;
    const tip = text(this, 0, 0, "", 13, "#ffffff", {
      fontStyle: "italic bold",
      strokeThickness: 5,
    })
      .setOrigin(0.5)
      .setVisible(false);
    teams.forEach((team, i) => {
      const row = Math.floor(i / perRow);
      const inRow = row === rows - 1 ? teams.length - perRow * row : perRow;
      const x =
        GAME_W / 2 - ((inRow - 1) * stepX) / 2 + (i - perRow * row) * stepX;
      const y = area.top + stepY * (row + 0.5);
      const ring = this.add.graphics();
      const mark =
        team.id === this.sel.home
          ? SIDE.home.color
          : team.id === this.sel.away
            ? SIDE.away.color
            : null;
      const r = size / 2 + 4;
      if (mark !== null)
        ring
          .fillStyle(mark, 0.35)
          .fillCircle(x, y, r)
          .lineStyle(3, mark)
          .strokeCircle(x, y, r);
      const img = this.add
        .image(x, y, texKey.emblem(team.id))
        .setDisplaySize(size, size);
      img.setInteractive({ useHandCursor: true });
      img.on("pointerover", () => {
        c.bringToTop(img);
        this.tweens.add({
          targets: img,
          displayWidth: size + 14,
          displayHeight: size + 14,
          duration: 100,
        });
        tip
          .setText(team.name)
          .setPosition(
            Phaser.Math.Clamp(x, 120, GAME_W - 120),
            y - size / 2 - 16,
          )
          .setVisible(true);
        c.bringToTop(tip);
      });
      img.on("pointerout", () => {
        this.tweens.add({
          targets: img,
          displayWidth: size,
          displayHeight: size,
          duration: 100,
        });
        tip.setVisible(false);
      });
      img.on("pointerdown", () => this.choose(team));
      c.add([ring, img]);
    });
    c.add(tip);
  }

  // --------------------------------------------------------------- acciones

  private bindKeys(): void {
    const kb = this.input.keyboard;
    if (!kb) return;
    kb.on("keydown-LEFT", () => this.cycle(this.sel.focus, -1));
    kb.on("keydown-RIGHT", () => this.cycle(this.sel.focus, 1));
    kb.on("keydown-UP", () => this.stepSeason(-1));
    kb.on("keydown-DOWN", () => this.stepSeason(1));
    kb.on("keydown-TAB", (e: KeyboardEvent) => {
      e.preventDefault();
      this.setFocus(this.sel.focus === "home" ? "away" : "home");
    });
    kb.on("keydown-ENTER", () => this.next());
  }

  private refresh(): void {
    this.drawSplit();
    this.renderSide("home");
    this.renderSide("away");
    this.renderShelf();
  }

  private setFocus(side: Side): void {
    if (this.sel.focus === side) return;
    this.sel.focus = side;
    this.shelfSeason = seasonOf(teamById(this.sel[side]));
    this.refresh();
  }

  private choose(team: TeamData): void {
    this.sel[this.sel.focus] = team.id;
    this.refresh();
  }

  private cycle(side: Side, dir: number): void {
    const team = teamById(this.sel[side]);
    const list = teamsOf(seasonOf(team));
    this.sel[side] =
      list[(list.indexOf(team) + dir + list.length) % list.length].id;
    this.sel.focus = side;
    this.shelfSeason = seasonOf(team);
    this.refresh();
  }

  /** Arriba/abajo: cambia la temporada de la estantería y elige su primer equipo para el lado activo. */
  private stepSeason(dir: number): void {
    const seasons = seasonsWithTeams();
    const i = seasons.findIndex((s) => s.id === this.shelfSeason);
    this.shelfSeason = seasons[(i + dir + seasons.length) % seasons.length].id;
    this.sel[this.sel.focus] = teamsOf(this.shelfSeason)[0].id;
    this.refresh();
  }

  private swap(): void {
    [this.sel.home, this.sel.away] = [this.sel.away, this.sel.home];
    this.refresh();
  }

  private randomRival(): void {
    const pool = TEAMS.filter((t) => t.id !== this.sel.home);
    const pick: TeamData | undefined =
      pool[Math.floor(Math.random() * pool.length)];
    if (!pick) return;
    this.sel.away = pick.id;
    this.refresh();
  }

  private next(): void {
    this.registry.set("menuSelection", { ...this.sel });
    const home = teamById(this.sel.home);
    const away = teamById(this.sel.away);
    this.scene.start("formation", {
      home: defaultLineup(home),
      away: defaultLineup(away),
    });
  }
}
