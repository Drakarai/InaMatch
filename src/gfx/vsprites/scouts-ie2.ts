// Sprites dibujados de los ojeadores de ie2 (ver loadScoutSprites en ../pack.ts): solo se piden los de los fichados.
export const files = import.meta.glob<string>('../../assets/pack/vsprites/scouts-ie2/*/*.png', { eager: true, query: '?url', import: 'default' });
