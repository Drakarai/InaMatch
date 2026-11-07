// Sprites dibujados de los ojeadores de vr (ver loadScoutSprites en ../pack.ts): solo se piden los de los fichados.
export const files = import.meta.glob<string>('../../assets/pack/vsprites/scouts-vr/*/*.png', { eager: true, query: '?url', import: 'default' });
