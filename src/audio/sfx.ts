import { audio, midiHz } from './engine';

/**
 * Efectos de sonido sintetizados: uno por tipo de supertécnica (fuego que ruge, hielo que tintinea,
 * rayos, olas, viento, rugidos...) y los del partido (silbato, chut, gol, choque de técnicas, botones).
 */

type Ctx = AudioContext;

function out(): GainNode | null {
  const ctx = audio.ctx;
  return ctx && ctx.state === 'running' && audio.settings.sfx ? audio.sfxBus : null;
}

// ------------------------------------------------------------------ piezas

/** Tono con barrido de frecuencia y envolvente simple. */
function tone(dest: AudioNode, type: OscillatorType, f0: number, f1: number, t: number, dur: number, vol: number, attack = 0.01): void {
  const ctx = audio.ctx as Ctx;
  const o = ctx.createOscillator();
  const g = ctx.createGain();
  o.type = type;
  o.frequency.setValueAtTime(f0, t);
  o.frequency.exponentialRampToValueAtTime(Math.max(20, f1), t + dur);
  g.gain.setValueAtTime(0.0001, t);
  g.gain.linearRampToValueAtTime(vol, t + attack);
  g.gain.exponentialRampToValueAtTime(0.0001, t + dur);
  o.connect(g).connect(dest);
  o.start(t);
  o.stop(t + dur + 0.05);
}

/** Ruido filtrado con barrido (soplidos, explosiones, olas...). */
function noise(dest: AudioNode, type: BiquadFilterType, f0: number, f1: number, t: number, dur: number, vol: number, attack = 0.01, q = 1): void {
  const ctx = audio.ctx as Ctx;
  const f = ctx.createBiquadFilter();
  f.type = type;
  f.Q.value = q;
  f.frequency.setValueAtTime(f0, t);
  f.frequency.exponentialRampToValueAtTime(Math.max(30, f1), t + dur);
  const g = ctx.createGain();
  g.gain.setValueAtTime(0.0001, t);
  g.gain.linearRampToValueAtTime(vol, t + attack);
  g.gain.exponentialRampToValueAtTime(0.0001, t + dur);
  f.connect(g).connect(dest);
  audio.noiseSource(f, t, dur);
}

/** Campanita: senoidal con armónico, para hielo, luz, estrellas... */
function bell(dest: AudioNode, note: number, t: number, dur: number, vol: number): void {
  tone(dest, 'sine', midiHz(note), midiHz(note), t, dur, vol, 0.004);
  tone(dest, 'sine', midiHz(note) * 2.76, midiHz(note) * 2.76, t, dur * 0.5, vol * 0.35, 0.004);
}

/** Retumbe grave (golpes, muros, tierra). */
function boom(dest: AudioNode, t: number, vol = 0.6, low = 45): void {
  tone(dest, 'sine', 130, low, t, 0.5, vol, 0.005);
  noise(dest, 'lowpass', 1200, 120, t, 0.45, vol * 0.6, 0.005);
}

/** Rugido: sierra grave con temblor (dragones, bestias). */
function growl(dest: AudioNode, t: number, dur: number, base = 85, vol = 0.25): void {
  const ctx = audio.ctx as Ctx;
  const o = ctx.createOscillator();
  o.type = 'sawtooth';
  o.frequency.setValueAtTime(base, t);
  o.frequency.linearRampToValueAtTime(base * 1.4, t + dur * 0.3);
  o.frequency.linearRampToValueAtTime(base * 0.8, t + dur);
  const lfo = ctx.createOscillator();
  const lg = ctx.createGain();
  lfo.frequency.value = 28;
  lg.gain.value = base * 0.25;
  lfo.connect(lg).connect(o.frequency);
  const f = ctx.createBiquadFilter();
  f.type = 'lowpass';
  f.frequency.value = 900;
  const g = ctx.createGain();
  g.gain.setValueAtTime(0.0001, t);
  g.gain.linearRampToValueAtTime(vol, t + 0.08);
  g.gain.exponentialRampToValueAtTime(0.0001, t + dur);
  o.connect(f).connect(g).connect(dest);
  [o, lfo].forEach((x) => {
    x.start(t);
    x.stop(t + dur + 0.05);
  });
  noise(dest, 'bandpass', 600, 300, t, dur, vol * 0.5, 0.06, 2);
}

/** Subida de energía (cargar la técnica). */
function rise(dest: AudioNode, t: number, dur = 0.45, vol = 0.12): void {
  tone(dest, 'sawtooth', 180, 900, t, dur, vol * 0.6, dur * 0.8);
  noise(dest, 'bandpass', 400, 3500, t, dur, vol, dur * 0.8, 3);
}

// ------------------------------------------------------------------ técnicas

type Sfx = (dest: AudioNode, t: number, variant: string) => void;

const TECH: Record<string, Sfx> = {
  fire: (d, t, v) => {
    // rugido de llamas y chisporroteo
    noise(d, 'lowpass', 300, 2400, t, 0.9, 0.45, 0.12);
    noise(d, 'bandpass', 2500, 1200, t + 0.05, 0.7, 0.18, 0.02, 4);
    for (let i = 0; i < 8; i++) noise(d, 'highpass', 3000, 3000, t + 0.1 + Math.random() * 0.6, 0.03, 0.15);
    if (v === 'explosion' || v === 'burst' || v === 'zigzag') boom(d, t + (v === 'zigzag' ? 0.5 : 0.05), 0.7);
  },
  ice: (d, t) => {
    noise(d, 'highpass', 6000, 9000, t, 0.6, 0.15, 0.05);
    [88, 95, 91, 100, 96].forEach((n, i) => bell(d, n, t + i * 0.07, 0.6, 0.12));
    tone(d, 'triangle', 1800, 1200, t + 0.25, 0.4, 0.06);
  },
  lightning: (d, t) => {
    for (let i = 0; i < 3; i++) {
      noise(d, 'highpass', 1500, 400, t + i * 0.11, 0.18, 0.5, 0.002);
      tone(d, 'square', 1200, 80, t + i * 0.11, 0.15, 0.12, 0.002);
    }
    boom(d, t + 0.12, 0.5, 35);
  },
  water: (d, t) => {
    noise(d, 'lowpass', 400, 2600, t, 0.35, 0.4, 0.08);
    noise(d, 'lowpass', 2600, 300, t + 0.35, 0.6, 0.35, 0.01);
    for (let i = 0; i < 6; i++) tone(d, 'sine', 400 + Math.random() * 500, 900 + Math.random() * 600, t + 0.2 + i * 0.07, 0.08, 0.08);
  },
  wind: (d, t) => noise(d, 'bandpass', 300, 2600, t, 0.6, 0.35, 0.2, 2),
  tornado: (d, t) => {
    const ctx = audio.ctx as Ctx;
    // remolino: ruido filtrado que sube y baja como un torbellino
    const f = ctx.createBiquadFilter();
    f.type = 'bandpass';
    f.Q.value = 4;
    const lfo = ctx.createOscillator();
    const lg = ctx.createGain();
    lfo.frequency.setValueAtTime(3, t);
    lfo.frequency.linearRampToValueAtTime(9, t + 1);
    lg.gain.value = 500;
    f.frequency.value = 900;
    lfo.connect(lg).connect(f.frequency);
    const g = ctx.createGain();
    g.gain.setValueAtTime(0.0001, t);
    g.gain.linearRampToValueAtTime(0.45, t + 0.2);
    g.gain.exponentialRampToValueAtTime(0.0001, t + 1.1);
    f.connect(g).connect(d);
    audio.noiseSource(f, t, 1.1);
    lfo.start(t);
    lfo.stop(t + 1.15);
  },
  sandstorm: (d, t) => noise(d, 'bandpass', 800, 1800, t, 1, 0.3, 0.2, 0.7),
  earth: (d, t) => {
    boom(d, t, 0.8, 30);
    noise(d, 'lowpass', 500, 80, t, 1, 0.4, 0.02);
    for (let i = 0; i < 6; i++) tone(d, 'triangle', 300 + Math.random() * 200, 90, t + 0.1 + i * 0.08, 0.1, 0.12);
  },
  wall: (d, t) => {
    noise(d, 'lowpass', 200, 900, t, 0.5, 0.45, 0.2);
    boom(d, t + 0.35, 0.7, 35);
  },
  rocks: (d, t) => {
    for (let i = 0; i < 6; i++) tone(d, 'triangle', 220 + Math.random() * 180, 70, t + i * 0.07, 0.12, 0.15);
    boom(d, t + 0.6, 0.5);
  },
  dark: (d, t) => {
    tone(d, 'sawtooth', 55, 40, t, 1.1, 0.18, 0.4);
    tone(d, 'sawtooth', 58, 41, t, 1.1, 0.14, 0.4);
    noise(d, 'lowpass', 200, 1800, t, 0.9, 0.2, 0.7);
    tone(d, 'sine', 900, 120, t + 0.6, 0.4, 0.1);
  },
  light: (d, t) => {
    [86, 90, 93, 98].forEach((n, i) => bell(d, n, t + i * 0.05, 1, 0.1));
    noise(d, 'highpass', 5000, 8000, t, 0.8, 0.12, 0.3);
  },
  stars: (d, t) => [91, 95, 98, 103, 98].forEach((n, i) => bell(d, n, t + i * 0.09, 0.4, 0.1)),
  meteor: (d, t) => {
    tone(d, 'sine', 2400, 300, t, 0.6, 0.12, 0.02);
    noise(d, 'bandpass', 3000, 400, t, 0.6, 0.2, 0.05, 2);
    boom(d, t + 0.6, 0.9, 30);
  },
  hand: (d, t, v) => {
    rise(d, t, 0.35, 0.12);
    // la mano gigante aparece con un golpe de metal y un acorde brillante
    [62, 69, 74, 78].forEach((n, i) => tone(d, 'sawtooth', midiHz(n), midiHz(n), t + 0.3 + i * 0.01, 0.7, 0.05, 0.01));
    boom(d, t + 0.3, 0.6);
    if (v === 'majin' || v === 'demon' || v === 'deity') growl(d, t + 0.1, 0.8, 70, 0.2);
    if (v === 'god') noise(d, 'highpass', 1500, 400, t + 0.4, 0.2, 0.35, 0.002);
  },
  punch: (d, t) => {
    noise(d, 'bandpass', 400, 2000, t, 0.2, 0.25, 0.15);
    boom(d, t + 0.22, 0.8);
  },
  shield: (d, t) => {
    tone(d, 'sine', 300, 600, t, 0.5, 0.15, 0.1);
    tone(d, 'triangle', 600, 1200, t, 0.5, 0.06, 0.1);
    bell(d, 84, t + 0.3, 0.6, 0.08);
  },
  sword: (d, t) => {
    // sacar la espada (raspado metálico) y el tajo
    noise(d, 'highpass', 3000, 7000, t, 0.25, 0.25, 0.05, 2);
    bell(d, 96, t + 0.2, 0.8, 0.12);
    noise(d, 'bandpass', 5000, 1200, t + 0.4, 0.25, 0.35, 0.005, 1.5);
  },
  dragon: (d, t) => {
    growl(d, t, 1.1, 75, 0.32);
    noise(d, 'lowpass', 300, 1800, t + 0.4, 0.6, 0.3, 0.1);
  },
  beast: (d, t, v) => {
    growl(d, t, 0.8, v === 'wolf' ? 160 : 95, 0.3);
    if (v === 'claw' || v === 'jaws') noise(d, 'bandpass', 4000, 1500, t + 0.35, 0.12, 0.35, 0.005, 2);
  },
  bird: (d, t) => {
    noise(d, 'bandpass', 500, 2500, t, 0.5, 0.25, 0.1, 1.5);
    tone(d, 'sine', 1800, 2900, t + 0.2, 0.15, 0.1);
    tone(d, 'sine', 2600, 1700, t + 0.38, 0.2, 0.1);
  },
  penguin: (d, t) => {
    for (let i = 0; i < 5; i++) tone(d, 'square', 900 + i * 80, 1400 + i * 80, t + i * 0.08, 0.07, 0.06);
    noise(d, 'bandpass', 600, 2200, t + 0.5, 0.4, 0.25, 0.05, 1.5);
  },
  clone: (d, t) => {
    for (let i = 0; i < 4; i++) tone(d, 'triangle', 600 + i * 150, 300 + i * 150, t + i * 0.06, 0.18, 0.08);
  },
  flower: (d, t) => {
    noise(d, 'bandpass', 1500, 3500, t, 0.8, 0.12, 0.3, 1);
    [84, 88, 91, 96].forEach((n, i) => bell(d, n, t + i * 0.1, 0.5, 0.07));
  },
  impact: (d, t) => {
    boom(d, t, 0.7);
    noise(d, 'highpass', 2000, 500, t, 0.15, 0.25, 0.002);
  },
  wings: (d, t) => {
    noise(d, 'bandpass', 400, 1600, t, 0.35, 0.2, 0.05, 1.5);
    noise(d, 'bandpass', 400, 1600, t + 0.3, 0.35, 0.2, 0.05, 1.5);
    [86, 93, 98].forEach((n, i) => bell(d, n, t + 0.2 + i * 0.06, 0.6, 0.06));
  },
  speedlines: (d, t) => noise(d, 'bandpass', 600, 3500, t, 0.35, 0.3, 0.02, 2),
  train: (d, t) => {
    tone(d, 'square', 660, 660, t, 0.25, 0.08);
    tone(d, 'square', 880, 880, t, 0.25, 0.06);
    noise(d, 'lowpass', 300, 1500, t + 0.3, 0.7, 0.4, 0.1);
    boom(d, t + 0.8, 0.6);
  },
  missile: (d, t) => {
    noise(d, 'bandpass', 800, 3000, t, 0.6, 0.3, 0.05, 1.5);
    TECH['fire:explosion'](d, t + 0.6, 'explosion');
  },
  bubbles: (d, t) => {
    for (let i = 0; i < 8; i++) tone(d, 'sine', 300 + Math.random() * 400, 900 + Math.random() * 800, t + i * 0.08, 0.07, 0.08);
  },
  hearts: (d, t) => [84, 88, 91, 96].forEach((n, i) => bell(d, n, t + i * 0.12, 0.5, 0.08)),
  notes: (d, t) => [76, 79, 83, 86, 83].forEach((n, i) => tone(d, 'triangle', midiHz(n), midiHz(n), t + i * 0.12, 0.2, 0.1)),
  clock: (d, t) => {
    for (let i = 0; i < 6; i++) tone(d, 'square', i % 2 ? 1500 : 1200, i % 2 ? 1500 : 1200, t + i * 0.15, 0.03, 0.08);
    bell(d, 84, t + 0.9, 1, 0.1);
  },
  portal: (d, t) => {
    tone(d, 'sine', 80, 400, t, 0.8, 0.15, 0.3);
    noise(d, 'bandpass', 200, 1200, t, 0.8, 0.2, 0.4, 3);
  },
  scan: (d, t) => {
    for (let i = 0; i < 4; i++) tone(d, 'sine', 1800, 1800, t + i * 0.18, 0.06, 0.08);
  },
  web: (d, t) => noise(d, 'highpass', 4000, 6000, t, 0.5, 0.15, 0.2, 2),
  fakeball: (d, t) => tone(d, 'square', 300, 900, t, 0.3, 0.08),
};
// alias por similitud
Object.assign(TECH, {
  'fire:explosion': (d: AudioNode, t: number) => {
    boom(d, t, 0.95, 28);
    noise(d, 'lowpass', 3000, 200, t, 0.9, 0.55, 0.005);
  },
  sun: TECH.fire,
  comet: TECH.meteor,
  planet: TECH.meteor,
  moon: TECH.light,
  aurora: TECH.light,
  rainbow: TECH.light,
  fireworks: TECH.stars,
  tower: TECH.wall,
  colosseum: TECH.wall,
  giant: TECH.punch,
  foot: TECH.earth,
  drill: TECH.tornado,
  ballspin: TECH.tornado,
  ballride: TECH.earth,
  wheel: TECH.fire,
  crescent: TECH.sword,
  swords: TECH.sword,
  spear: TECH.sword,
  cross: TECH.light,
  triangle: TECH.dark,
  skull: TECH.dark,
  torii: TECH.dark,
  ghosthands: TECH.dark,
  shadowhand: TECH.dark,
  gravity: TECH.dark,
  wisps: TECH.dark,
  rays: TECH.dark,
  aura: (d: AudioNode, t: number) => rise(d, t, 0.6, 0.18),
  charge: TECH.punch,
  slide: TECH.speedlines,
  barrage: TECH.punch,
  whale: TECH.water,
  shark: TECH.water,
  snake: TECH.beast,
  unicorn: TECH.bird,
  butterfly: TECH.flower,
  confetti: TECH.stars,
  dna: TECH.scan,
  digital: TECH.scan,
  lasers: TECH.scan,
  runes: TECH.light,
  keys: TECH.clock,
  cape: TECH.wind,
  fan: TECH.wind,
  surfboard: TECH.wind,
  dogball: TECH.fakeball,
  yoyo: TECH.fakeball,
  vine: TECH.flower,
  bush: TECH.flower,
  mole: TECH.earth,
  ribbon: TECH.wind,
});

/** Sonido de una supertécnica según su efecto ("dragon:wyvern" → dragon, con su variante). */
export function techSfx(fx: string, delay = 0): void {
  const d = out();
  if (!d) return;
  const [base, variant = ''] = fx.split(':');
  const fn = TECH[fx] ?? TECH[base] ?? TECH.impact;
  fn(d, audio.now + delay, variant);
}

// ------------------------------------------------------------------ partido e interfaz

export const sfx = {
  /** Carga de la animación de la técnica (retrato). */
  cutin(): void {
    const d = out();
    if (!d) return;
    const t = audio.now;
    rise(d, t, 0.3, 0.14);
    tone(d, 'sawtooth', 220, 220, t + 0.28, 0.3, 0.06);
    noise(d, 'highpass', 3000, 1000, t + 0.28, 0.3, 0.2, 0.005);
  },
  /** Los dos rayos del duelo de técnicas chocan. */
  clash(): void {
    const d = out();
    if (!d) return;
    const t = audio.now;
    noise(d, 'bandpass', 800, 2400, t, 0.9, 0.35, 0.02, 2);
    tone(d, 'sawtooth', 110, 130, t, 0.9, 0.12, 0.02);
    tone(d, 'sawtooth', 116, 124, t, 0.9, 0.1, 0.02);
  },
  win(): void {
    const d = out();
    if (!d) return;
    const t = audio.now;
    boom(d, t, 0.8);
    noise(d, 'highpass', 2500, 600, t, 0.3, 0.3, 0.002);
  },
  shatter(): void {
    const d = out();
    if (!d) return;
    const t = audio.now;
    for (let i = 0; i < 7; i++) bell(d, 96 + Math.floor(Math.random() * 10), t + i * 0.025, 0.25, 0.05);
    noise(d, 'highpass', 4000, 2000, t, 0.25, 0.2, 0.002);
  },
  kick(strong = false): void {
    const d = out();
    if (!d) return;
    const t = audio.now;
    tone(d, 'sine', strong ? 220 : 180, 60, t, 0.12, strong ? 0.45 : 0.25, 0.002);
    noise(d, 'bandpass', 1500, 600, t, 0.06, strong ? 0.3 : 0.15, 0.001);
  },
  whistle(long = false): void {
    const d = out();
    if (!d) return;
    const t = audio.now;
    const parts = long ? [[0, 0.25], [0.32, 0.25], [0.64, 0.7]] : [[0, 0.45]];
    for (const [s, len] of parts) {
      tone(d, 'sine', 2900, 2950, t + s, len, 0.12, 0.01);
      tone(d, 'square', 2950, 3000, t + s, len, 0.02, 0.01);
    }
  },
  goal(): void {
    const d = out();
    if (!d) return;
    const t = audio.now;
    // red y grada
    noise(d, 'lowpass', 1500, 400, t, 0.3, 0.35, 0.002);
    noise(d, 'bandpass', 900, 1300, t + 0.1, 2.4, 0.3, 0.4, 0.6);
  },
  duelStart(): void {
    const d = out();
    if (!d) return;
    const t = audio.now;
    tone(d, 'square', 660, 660, t, 0.06, 0.06);
    tone(d, 'square', 990, 990, t + 0.07, 0.08, 0.06);
  },
  click(): void {
    const d = out();
    if (!d) return;
    tone(d, 'triangle', 1200, 900, audio.now, 0.05, 0.08, 0.002);
  },
};
