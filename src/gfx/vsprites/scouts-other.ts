// Sprites dibujados de los ojeadores de Ares y Orion (ver loadScoutSprites en ../pack.ts).
export const files = import.meta.glob<string>(['../../assets/pack/vsprites/scouts-ares/*/*.png', '../../assets/pack/vsprites/scouts-orion/*/*.png'], { eager: true, query: '?url', import: 'default' });
