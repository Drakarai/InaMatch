import { defineConfig } from 'vite';
import { viteSingleFile } from 'vite-plugin-singlefile';
import { vsprites } from './vite-vsprites';

// `npm run build:single` genera un único HTML que se abre con doble clic, sin servidor.
// Sin servidor no se puede leer public/assets/pack, así que usa los gráficos provisionales.
export default defineConfig(({ mode }) =>
  mode === 'single'
    ? {
        base: './',
        plugins: [vsprites(), viteSingleFile()],
        build: { outDir: 'dist-single', copyPublicDir: false, chunkSizeWarningLimit: 2000 },
      }
    : {
        // base relativa: funciona igual en la raíz de un dominio que en una subcarpeta
        base: './',
        plugins: [vsprites()],
        build: { chunkSizeWarningLimit: 2000 },
      },
);
