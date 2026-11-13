// Módulos virtuales de los sprites dibujados (vite-vsprites.ts).
// Cada trozo trae las imágenes en base64 (`files`, en desarrollo) o un archivo con todas seguidas (`pack` e `index`,
// al compilar): src/gfx/pack.ts los convierte en { files }.
declare module 'virtual:vsprite-index' {
  export interface VspriteSet {
    files?: Record<string, string>;
    pack?: string;
    index?: Record<string, [number, number]>;
  }
  export const sets: Record<string, () => Promise<VspriteSet>>;
  export const masks: Record<string, () => Promise<VspriteSet>>;
}

// Retratos de Victory Road (vite-portraits.ts): '<equipo>/<jugador>' -> url.
declare module 'virtual:portrait-index' {
  const portraits: Record<string, string>;
  export default portraits;
}
