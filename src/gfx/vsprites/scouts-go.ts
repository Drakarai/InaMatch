// Sprites dibujados de los ojeadores de go (ver loadScoutSprites en ../pack.ts): solo se piden los de los fichados.
export const files = import.meta.glob<string>('../../assets/pack/vsprites/scouts-go/*/*.png', { eager: true, query: '?url', import: 'default' });
