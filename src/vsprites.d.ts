// Módulos virtuales de los sprites dibujados (vite-vsprites.ts).
declare module 'virtual:vsprite-index' {
  export const sets: Record<string, () => Promise<{ files: Record<string, string> }>>;
}
