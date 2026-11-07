// Sprites dibujados de los equipos de IE (ver loadVspritePack en ../pack.ts).
export const files = import.meta.glob<string>('../../assets/pack/vsprites/ie*/*/*.png', { eager: true, query: '?url', import: 'default' });
