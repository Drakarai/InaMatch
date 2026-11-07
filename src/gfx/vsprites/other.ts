// Sprites dibujados de las demás temporadas (ver loadVspritePack en ../pack.ts).
export const files = import.meta.glob<string>(['../../assets/pack/vsprites/*/*/*.png', '!../../assets/pack/vsprites/ie*/**', '!../../assets/pack/vsprites/go-*/**', '!../../assets/pack/vsprites/cs-*/**'], { eager: true, query: '?url', import: 'default' });
