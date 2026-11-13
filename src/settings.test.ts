import { describe, expect, it } from 'vitest';
import { scaleStats } from './engine/rules';
import { cpuMoveChance, DIFFICULTIES, DIFFICULTY_ORDER, parseSettings } from './settings';

describe('ajustes', () => {
  it('sin nada guardado, o con algo dañado, la dificultad es Normal', () => {
    expect(parseSettings(null).difficulty).toBe('normal');
    expect(parseSettings('{roto').difficulty).toBe('normal');
    expect(parseSettings(JSON.stringify({ difficulty: 'imposible' })).difficulty).toBe('normal');
    expect(parseSettings(JSON.stringify({ difficulty: 'hard' })).difficulty).toBe('hard');
  });

  it('cada nivel es más difícil que el anterior', () => {
    const [easy, normal, hard] = DIFFICULTY_ORDER.map((d) => DIFFICULTIES[d]);
    expect(easy.power).toBeLessThan(normal.power);
    expect(normal.power).toBeLessThan(hard.power);
    expect(easy.moveChance).toBeLessThan(hard.moveChance);
    expect(easy.press).toBeLessThan(hard.press);
    // piensa más rápido cuanto más difícil
    expect(easy.think).toBeGreaterThan(normal.think);
    expect(normal.think).toBeGreaterThan(hard.think);
    expect(easy.shotBias).toBeLessThan(hard.shotBias);
  });

  it('Normal deja el juego como estaba', () => {
    const n = DIFFICULTIES.normal;
    expect(n.power).toBe(1);
    expect(n.moveChance).toBe(1);
    expect(n.press).toBe(0.88);
    expect(n.think).toBe(0.3);
    expect(n.shotBias).toBe(0);
  });

  it('la probabilidad de supertécnica se queda entre 0 y 1', () => {
    for (const d of DIFFICULTY_ORDER) {
      for (const base of [0, 0.45, 0.75, 1]) {
        const p = cpuMoveChance(base, DIFFICULTIES[d]);
        expect(p).toBeGreaterThanOrEqual(0);
        expect(p).toBeLessThanOrEqual(1);
      }
    }
    expect(cpuMoveChance(0.5, DIFFICULTIES.normal)).toBe(0.5);
  });

  it('los atributos de la CPU se escalan, menos el aguante', () => {
    const s = { kick: 50, body: 60, control: 70, guard: 80, speed: 40, stamina: 90, guts: 55 };
    const hard = scaleStats(s, 1.12);
    expect(hard.kick).toBe(56);
    expect(hard.guard).toBe(90);
    expect(hard.stamina).toBe(90);
    expect(scaleStats(s, 1)).toEqual(s);
    // no cambia el original
    expect(s.kick).toBe(50);
  });
});
