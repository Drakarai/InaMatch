// Sprites dibujados de los ojeadores de cs (ver loadScoutSprites en ../pack.ts): solo se piden los de los fichados.
export const files = import.meta.glob<string>('../../assets/pack/vsprites/scouts-cs/*/*.png', { eager: true, query: '?url', import: 'default' });
