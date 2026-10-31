import { audio, midiHz } from './engine';

/**
 * Música compuesta para InaMatch al estilo de las bandas sonoras de los juegos de fútbol de anime:
 * rock-pop enérgico con metales al frente, guitarra con distorsión, bajo y batería. Todo se sintetiza
 * en el momento (Web Audio); las canciones son listas de notas por corcheas.
 */

// ------------------------------------------------------------------ instrumentos

let distortion: Float32Array<ArrayBuffer> | null = null;
function driveCurve(): Float32Array<ArrayBuffer> {
  if (distortion) return distortion;
  const n = 1024;
  distortion = new Float32Array(new ArrayBuffer(n * 4));
  for (let i = 0; i < n; i++) {
    const x = (i / n) * 2 - 1;
    distortion[i] = Math.tanh(x * 4);
  }
  return distortion;
}

function env(g: GainNode, t: number, peak: number, a: number, d: number, sustain: number, end: number, r: number): void {
  g.gain.setValueAtTime(0.0001, t);
  g.gain.linearRampToValueAtTime(peak, t + a);
  g.gain.setTargetAtTime(peak * sustain, t + a, d);
  g.gain.setValueAtTime(peak * sustain, end);
  g.gain.exponentialRampToValueAtTime(0.0001, end + r);
}

/** Metales: dos sierras desafinadas con un filtro que se abre al atacar, y vibrato en las notas largas. */
function brass(dest: AudioNode, note: number, t: number, dur: number, vol = 0.16): void {
  const ctx = audio.ctx!;
  const f = ctx.createBiquadFilter();
  f.type = 'lowpass';
  f.Q.value = 2;
  f.frequency.setValueAtTime(700, t);
  f.frequency.linearRampToValueAtTime(3600, t + 0.05);
  f.frequency.setTargetAtTime(1800, t + 0.06, 0.15);
  const g = ctx.createGain();
  env(g, t, vol, 0.025, 0.12, 0.75, t + dur, 0.09);
  f.connect(g).connect(dest);
  for (const det of [-7, 7]) {
    const o = ctx.createOscillator();
    o.type = 'sawtooth';
    o.frequency.value = midiHz(note);
    o.detune.value = det;
    if (dur > 0.3) {
      const lfo = ctx.createOscillator();
      const lg = ctx.createGain();
      lfo.frequency.value = 5.5;
      lg.gain.setValueAtTime(0, t);
      lg.gain.linearRampToValueAtTime(14, t + dur);
      lfo.connect(lg).connect(o.detune);
      lfo.start(t);
      lfo.stop(t + dur + 0.2);
    }
    o.connect(f);
    o.start(t);
    o.stop(t + dur + 0.2);
  }
}

/** Guitarra eléctrica con distorsión tocando quintas (power chords). */
function guitar(dest: AudioNode, root: number, t: number, dur: number, vol = 0.07, muted = true): void {
  const ctx = audio.ctx!;
  const shaper = ctx.createWaveShaper();
  shaper.curve = driveCurve();
  const pre = ctx.createGain();
  pre.gain.value = 0.6;
  const f = ctx.createBiquadFilter();
  f.type = 'lowpass';
  f.frequency.value = muted ? 1400 : 2600;
  const g = ctx.createGain();
  env(g, t, vol, 0.005, muted ? 0.05 : 0.4, muted ? 0.3 : 0.7, t + dur, muted ? 0.04 : 0.15);
  pre.connect(shaper).connect(f).connect(g).connect(dest);
  for (const iv of [0, 7, 12]) {
    const o = ctx.createOscillator();
    o.type = 'sawtooth';
    o.frequency.value = midiHz(root + iv);
    o.detune.value = (Math.random() - 0.5) * 8;
    o.connect(pre);
    o.start(t);
    o.stop(t + dur + 0.2);
  }
}

function bass(dest: AudioNode, note: number, t: number, dur: number, vol = 0.2): void {
  const ctx = audio.ctx!;
  const f = ctx.createBiquadFilter();
  f.type = 'lowpass';
  f.frequency.setValueAtTime(900, t);
  f.frequency.setTargetAtTime(380, t, 0.08);
  const g = ctx.createGain();
  env(g, t, vol, 0.005, 0.1, 0.6, t + dur * 0.9, 0.05);
  f.connect(g).connect(dest);
  const o = ctx.createOscillator();
  o.type = 'square';
  o.frequency.value = midiHz(note);
  const sub = ctx.createOscillator();
  sub.type = 'sine';
  sub.frequency.value = midiHz(note - 12);
  o.connect(f);
  sub.connect(g);
  [o, sub].forEach((x) => {
    x.start(t);
    x.stop(t + dur + 0.1);
  });
}

/** Cuerdas de fondo para las partes amplias. */
function pad(dest: AudioNode, notes: number[], t: number, dur: number, vol = 0.035): void {
  const ctx = audio.ctx!;
  const g = ctx.createGain();
  env(g, t, vol, 0.25, 0.5, 0.8, t + dur, 0.3);
  const f = ctx.createBiquadFilter();
  f.type = 'lowpass';
  f.frequency.value = 2200;
  f.connect(g).connect(dest);
  for (const n of notes) {
    for (const det of [-9, 9]) {
      const o = ctx.createOscillator();
      o.type = 'sawtooth';
      o.frequency.value = midiHz(n);
      o.detune.value = det;
      o.connect(f);
      o.start(t);
      o.stop(t + dur + 0.4);
    }
  }
}

function kick(dest: AudioNode, t: number, vol = 0.55): void {
  const ctx = audio.ctx!;
  const o = ctx.createOscillator();
  const g = ctx.createGain();
  o.frequency.setValueAtTime(160, t);
  o.frequency.exponentialRampToValueAtTime(42, t + 0.12);
  g.gain.setValueAtTime(vol, t);
  g.gain.exponentialRampToValueAtTime(0.0001, t + 0.28);
  o.connect(g).connect(dest);
  o.start(t);
  o.stop(t + 0.3);
}

function snare(dest: AudioNode, t: number, vol = 0.28): void {
  const ctx = audio.ctx!;
  const f = ctx.createBiquadFilter();
  f.type = 'bandpass';
  f.frequency.value = 1900;
  f.Q.value = 0.8;
  const g = ctx.createGain();
  g.gain.setValueAtTime(vol, t);
  g.gain.exponentialRampToValueAtTime(0.0001, t + 0.18);
  f.connect(g).connect(dest);
  audio.noiseSource(f, t, 0.2);
  const o = ctx.createOscillator();
  const og = ctx.createGain();
  o.type = 'triangle';
  o.frequency.setValueAtTime(220, t);
  o.frequency.exponentialRampToValueAtTime(140, t + 0.08);
  og.gain.setValueAtTime(vol * 0.6, t);
  og.gain.exponentialRampToValueAtTime(0.0001, t + 0.1);
  o.connect(og).connect(dest);
  o.start(t);
  o.stop(t + 0.12);
}

function hat(dest: AudioNode, t: number, vol = 0.06, open = false): void {
  const ctx = audio.ctx!;
  const f = ctx.createBiquadFilter();
  f.type = 'highpass';
  f.frequency.value = 7500;
  const g = ctx.createGain();
  const len = open ? 0.22 : 0.04;
  g.gain.setValueAtTime(vol, t);
  g.gain.exponentialRampToValueAtTime(0.0001, t + len);
  f.connect(g).connect(dest);
  audio.noiseSource(f, t, len);
}

function crash(dest: AudioNode, t: number, vol = 0.12): void {
  const ctx = audio.ctx!;
  const f = ctx.createBiquadFilter();
  f.type = 'highpass';
  f.frequency.value = 4200;
  const g = ctx.createGain();
  g.gain.setValueAtTime(vol, t);
  g.gain.exponentialRampToValueAtTime(0.0001, t + 1.4);
  f.connect(g).connect(dest);
  audio.noiseSource(f, t, 1.4);
}

// ------------------------------------------------------------------ canciones

/** Una parte de la canción: acordes por compás y melodía por corcheas (null = silencio, -1 = mantener). */
interface Section {
  chords: number[]; // raíz de cada compás (MIDI, octava del bajo)
  minor: boolean[]; // acorde menor
  lead: (number | null)[]; // 8 corcheas por compás
  style: 'drive' | 'open' | 'break';
}

export interface Song {
  bpm: number;
  sections: Section[];
}

const _ = null;
const H = -1;

// Tema del menú: en Re mayor, heroico y luminoso, con una estrofa animada y un estribillo amplio.
const MENU: Song = {
  bpm: 150,
  sections: [
    {
      style: 'drive',
      chords: [50, 45, 47, 43, 50, 45, 43, 45],
      minor: [false, false, true, false, false, false, false, false],
      lead: [
        74, _, 78, 81, 86, H, 85, 83,
        81, H, H, 78, 76, H, 73, 76,
        78, H, 74, 78, 83, H, 81, 78,
        79, H, H, H, 78, 76, 74, 76,
        74, _, 78, 81, 86, H, 88, 86,
        85, H, 81, H, 76, 78, 81, 85,
        86, H, 83, H, 79, H, 81, 83,
        81, H, H, H, H, H, _, _,
      ],
    },
    {
      style: 'open',
      chords: [47, 43, 50, 45, 47, 43, 40, 45],
      minor: [true, false, false, false, true, false, true, false],
      lead: [
        83, H, 81, 83, 86, H, 83, 81,
        79, H, 78, 79, 83, H, 81, 79,
        78, H, 76, 78, 81, H, 78, 76,
        76, H, 74, 76, 78, H, 81, H,
        83, H, 85, 86, 88, H, 86, 85,
        86, H, 83, H, 79, H, 83, 86,
        88, H, 86, H, 85, H, 83, H,
        81, H, 83, 85, 88, H, H, H,
      ],
    },
  ],
};

// Tema del partido: en Mi menor, rápido y con empuje, riff sincopado y subida final en Re mayor.
const MATCH: Song = {
  bpm: 168,
  sections: [
    {
      style: 'drive',
      chords: [40, 36, 38, 35, 40, 36, 38, 35],
      minor: [true, false, false, false, true, false, false, false],
      lead: [
        76, _, 76, 79, _, 81, 79, 76,
        79, H, 76, H, 72, H, 74, 76,
        78, _, 78, 81, _, 83, 81, 78,
        83, H, H, 78, 75, H, 78, 83,
        76, _, 76, 79, _, 81, 83, 86,
        84, H, 83, H, 79, H, 76, 79,
        81, _, 81, 83, _, 86, 83, 81,
        83, H, H, H, 75, 78, 83, 87,
      ],
    },
    {
      style: 'open',
      chords: [45, 36, 38, 43, 45, 36, 38, 38],
      minor: [true, false, false, false, true, false, false, false],
      lead: [
        81, H, 84, 83, 81, H, 79, 81,
        79, H, 76, 79, 84, H, 83, 79,
        81, H, 78, H, 74, 78, 81, 86,
        86, H, H, 83, 79, H, 83, 86,
        88, H, 86, 84, 83, H, 81, 83,
        84, H, 83, 81, 79, H, 76, 79,
        81, H, 83, 86, 90, H, 88, 86,
        86, H, H, H, H, H, _, _,
      ],
    },
  ],
};

// Fanfarria corta para los goles.
export const GOAL_FANFARE: [number, number][] = [
  [74, 0.12], [78, 0.12], [81, 0.12], [86, 0.5], [81, 0.12], [86, 0.7],
];

export const SONGS = { menu: MENU, match: MATCH };
export type SongId = keyof typeof SONGS;

// ------------------------------------------------------------------ reproductor

/** Reproduce una canción en bucle programando las notas un poco por delante (como un secuenciador). */
class MusicPlayer {
  private song: Song | null = null;
  private id: SongId | null = null;
  private step = 0;
  private nextTime = 0;
  private timer: number | null = null;
  private out: GainNode | null = null;

  play(id: SongId): void {
    if (this.id === id) return;
    this.id = id;
    audio.whenReady(() => {
      if (this.id !== id) return;
      this.stopNow(0.6);
      const ctx = audio.ctx!;
      this.song = SONGS[id];
      this.out = ctx.createGain();
      this.out.gain.setValueAtTime(0.0001, ctx.currentTime);
      this.out.gain.linearRampToValueAtTime(1, ctx.currentTime + 0.8);
      this.out.connect(audio.duckBus);
      this.step = 0;
      this.nextTime = ctx.currentTime + 0.1;
      this.timer = window.setInterval(() => this.schedule(), 40);
    });
  }

  stop(): void {
    this.id = null;
    this.stopNow(0.8);
  }

  private stopNow(fade: number): void {
    if (this.timer !== null) window.clearInterval(this.timer);
    this.timer = null;
    const out = this.out;
    if (out && audio.ctx) {
      const t = audio.ctx.currentTime;
      out.gain.cancelScheduledValues(t);
      out.gain.setTargetAtTime(0.0001, t, fade / 4);
      window.setTimeout(() => out.disconnect(), fade * 1000 + 300);
    }
    this.out = null;
  }

  private schedule(): void {
    const ctx = audio.ctx;
    const song = this.song;
    const out = this.out;
    if (!ctx || !song || !out) return;
    const eighth = 60 / song.bpm / 2;
    // si la pestaña estuvo en segundo plano, no intentar recuperar todo lo perdido
    if (this.nextTime < ctx.currentTime - 0.2) this.nextTime = ctx.currentTime + 0.05;
    while (this.nextTime < ctx.currentTime + 0.15) {
      this.playStep(song, out, this.step, this.nextTime, eighth);
      this.step++;
      this.nextTime += eighth;
    }
  }

  private playStep(song: Song, out: GainNode, step: number, t: number, eighth: number): void {
    const total = song.sections.reduce((n, s) => n + s.chords.length * 8, 0);
    let s = step % total;
    let sec = song.sections[0];
    for (const x of song.sections) {
      if (s < x.chords.length * 8) {
        sec = x;
        break;
      }
      s -= x.chords.length * 8;
    }
    const bar = Math.floor(s / 8);
    const pos = s % 8;
    const root = sec.chords[bar];
    const third = sec.minor[bar] ? 3 : 4;
    // melodía: la duración llega hasta la siguiente nota
    const note = sec.lead[s];
    if (note !== null && note !== H) {
      let len = 1;
      while (s + len < sec.lead.length && sec.lead[s + len] === H) len++;
      brass(out, note, t, len * eighth * 0.95);
    }
    // bajo: corcheas con salto de octava
    bass(out, root + (pos % 2 === 1 && sec.style === 'drive' ? 12 : 0), t, eighth);
    // guitarra
    if (sec.style === 'drive') guitar(out, root + 12, t, eighth * 0.9, 0.06, true);
    else if (pos === 0 || pos === 3 || pos === 6) guitar(out, root + 12, t, eighth * (pos === 6 ? 2 : 3) * 0.95, 0.055, false);
    if (sec.style === 'open' && pos === 0) pad(out, [root + 24, root + 24 + third, root + 31], t, eighth * 8);
    // batería
    if (pos === 0 && bar % 4 === 0) crash(out, t);
    if (pos === 0 || pos === 4 || (sec.style === 'drive' && pos === 5) || (sec.style === 'open' && pos === 3)) kick(out, t);
    if (pos === 2 || pos === 6) snare(out, t);
    hat(out, t, pos % 2 ? 0.04 : 0.065, sec.style === 'open' && pos === 7);
    // redoble al final de cada parte
    if (bar === sec.chords.length - 1 && pos >= 4) snare(out, t + eighth / 2, 0.18);
  }
}

export const music = new MusicPlayer();

/** Fanfarria de gol, por encima de la música (que baja un momento). */
export function playFanfare(): void {
  const ctx = audio.ctx;
  if (!ctx || ctx.state !== 'running') return;
  audio.duck(0.25, 1800);
  let t = ctx.currentTime + 0.02;
  for (const [n, d] of GOAL_FANFARE) {
    brass(audio.sfxBus, n, t, d * 0.95, 0.2);
    brass(audio.sfxBus, n - 12, t, d * 0.95, 0.12);
    t += d;
  }
  crash(audio.sfxBus, ctx.currentTime + 0.38, 0.2);
}
