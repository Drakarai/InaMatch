import { defineConfig } from 'vite';

// base relativa para que funcione en GitHub Pages (usuario.github.io/InaMatch/)
export default defineConfig({
  base: './',
  build: { chunkSizeWarningLimit: 2000 },
});
