import Phaser from 'phaser';

/**
 * Audio del juego, todo generado con Web Audio (sin archivos): música compuesta para InaMatch y efectos
 * de las supertécnicas. Música y efectos tienen su propio volumen y se pueden apagar; la elección se
 * guarda en el navegador.
 */

export interface AudioSettings {
  music: boolean;
  sfx: boolean;
  musicVolume: number;
  sfxVolume: number;
}

const KEY = 'inamatch-audio';
const DEFAULTS: AudioSettings = { music: true, sfx: true, musicVolume: 0.55, sfxVolume: 0.7 };

function load(): AudioSettings {
  try {
    const raw = window.localStorage.getItem(KEY);
    return raw ? { ...DEFAULTS, ...JSON.parse(raw) } : { ...DEFAULTS };
  } catch {
    return { ...DEFAULTS };
  }
}

export class AudioEngine {
  ctx: AudioContext | null = null;
  musicBus!: GainNode;
  sfxBus!: GainNode;
  /** Bus de la música antes del volumen general, para bajarla un momento (gol, choque de técnicas). */
  duckBus!: GainNode;
  noise!: AudioBuffer;
  settings: AudioSettings = load();
  private listeners: (() => void)[] = [];
  private pending: (() => void)[] = [];

  init(game: Phaser.Game): void {
    if (this.ctx) return;
    const sm = game.sound as Phaser.Sound.WebAudioSoundManager;
    if (!sm || !('context' in sm) || !sm.context) return;
    const ctx = sm.context;
    this.ctx = ctx;
    const master = ctx.createDynamicsCompressor();
    master.threshold.value = -14;
    master.ratio.value = 4;
    master.connect(ctx.destination);
    this.musicBus = ctx.createGain();
    this.sfxBus = ctx.createGain();
    this.duckBus = ctx.createGain();
    this.duckBus.connect(this.musicBus);
    this.musicBus.connect(master);
    this.sfxBus.connect(master);
    this.applyVolumes();
    // ruido blanco para la batería y los efectos
    const len = ctx.sampleRate * 2;
    this.noise = ctx.createBuffer(1, len, ctx.sampleRate);
    const d = this.noise.getChannelData(0);
    for (let i = 0; i < len; i++) d[i] = Math.random() * 2 - 1;
    // el navegador solo deja sonar después de un clic o una tecla
    const go = () => {
      const queued = this.pending;
      this.pending = [];
      queued.forEach((f) => f());
    };
    if (ctx.state === 'running') go();
    else {
      sm.once(Phaser.Sound.Events.UNLOCKED, go);
      const resume = () => void ctx.resume().then(go);
      window.addEventListener('pointerdown', resume, { once: true });
      window.addEventListener('keydown', resume, { once: true });
    }
  }

  /** Ejecuta `f` en cuanto el audio esté desbloqueado. */
  whenReady(f: () => void): void {
    if (this.ctx?.state === 'running') f();
    else this.pending.push(f);
  }

  get now(): number {
    return this.ctx?.currentTime ?? 0;
  }

  set(patch: Partial<AudioSettings>): void {
    this.settings = { ...this.settings, ...patch };
    try {
      window.localStorage.setItem(KEY, JSON.stringify(this.settings));
    } catch {
      // sin almacenamiento: se usa solo en esta sesión
    }
    this.applyVolumes();
    this.listeners.forEach((l) => l());
  }

  onChange(l: () => void): () => void {
    this.listeners.push(l);
    return () => (this.listeners = this.listeners.filter((x) => x !== l));
  }

  private applyVolumes(): void {
    if (!this.ctx) return;
    const t = this.ctx.currentTime;
    const s = this.settings;
    this.musicBus.gain.setTargetAtTime(s.music ? s.musicVolume * 0.5 : 0, t, 0.05);
    // los efectos van por encima de la música (el compresor del final evita que saturen)
    this.sfxBus.gain.setTargetAtTime(s.sfx ? s.sfxVolume * 2.4 : 0, t, 0.05);
  }

  /** Baja la música un momento para que se oiga bien un efecto o una fanfarria. */
  duck(amount = 0.35, ms = 900): void {
    if (!this.ctx) return;
    const t = this.ctx.currentTime;
    const g = this.duckBus.gain;
    g.cancelScheduledValues(t);
    g.setTargetAtTime(amount, t, 0.04);
    g.setTargetAtTime(1, t + ms / 1000, 0.25);
  }

  /** Fuente de ruido blanco ya conectada a `dest`. */
  noiseSource(dest: AudioNode, at: number, dur: number): AudioBufferSourceNode {
    const ctx = this.ctx!;
    const src = ctx.createBufferSource();
    src.buffer = this.noise;
    src.loop = true;
    src.loopStart = Math.random();
    src.connect(dest);
    src.start(at, Math.random() * 1.5);
    src.stop(at + dur + 0.05);
    return src;
  }
}

export const audio = new AudioEngine();

export const midiHz = (n: number) => 440 * Math.pow(2, (n - 69) / 12);
