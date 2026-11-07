// Sprites dibujados de los equipos de CS (ver loadVspritePack en ../pack.ts).
export const files = import.meta.glob<string>('../../assets/pack/vsprites/cs-*/*/*.png', { eager: true, query: '?url', import: 'default' });
