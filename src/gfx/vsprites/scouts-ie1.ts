// Sprites dibujados de los ojeadores de ie1 (ver loadScoutSprites en ../pack.ts): solo se piden los de los fichados.
export const files = import.meta.glob<string>('../../assets/pack/vsprites/scouts-ie1/*/*.png', { eager: true, query: '?url', import: 'default' });
