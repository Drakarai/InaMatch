// Sprites dibujados de los equipos de GO (ver loadVspritePack en ../pack.ts).
export const files = import.meta.glob<string>('../../assets/pack/vsprites/go-*/*/*.png', { eager: true, query: '?url', import: 'default' });
