import { defineConfig } from 'vite';
import { viteSingleFile } from 'vite-plugin-singlefile';
import { vsprites } from './vite-vsprites';
import { portraits } from './vite-portraits';

// `npm run build:single` genera un único HTML que se abre con doble clic, sin servidor.
// Sin servidor no se puede leer public/assets/pack, así que usa los gráficos provisionales.
export default defineConfig(({ mode }) =>
  mode === 'single'
    ? {
        base: './',
        plugins: [vsprites(), portraits(), viteSingleFile()],
        build: { outDir: 'dist-single', copyPublicDir: false, chunkSizeWarningLimit: 2000 },
      }
    : {
        // base relativa: funciona igual en la raíz de un dominio que en una subcarpeta
        base: './',
        plugins: [vsprites(), portraits()],
        // los JSON grandes (rasgos, ojeadores, historias, equipos) van como JSON.parse('...'): un solo texto en vez de
        // un objeto de JavaScript con miles de nodos que analizar (mucha menos memoria al compilar y carga más rápida)
        json: { stringify: true },
        build: {
          chunkSizeWarningLimit: 2000,
          rollupOptions: {
            output: {
              // Phaser y los datos casi nunca cambian: van aparte para que el navegador los guarde entre versiones
              // y no los vuelva a bajar cada vez que cambia el código del juego
              manualChunks(id) {
                if (id.includes('node_modules/phaser')) return 'phaser';
                if (/src\/data\/teams\/[^/]+\.json$/.test(id)) return 'teams';
                if (/src\/data\/(moves|movefx|formations|formation-aliases|uniforms|crests)\.json$/.test(id)) return 'data';
                // listas de imágenes del paquete (miles de rutas): solo cambian cuando se añaden imágenes
                if (/src\/gfx\/pack\.ts$|src\/club\/crests\.ts$/.test(id)) return 'assets';
                return undefined;
              },
            },
          },
        },
      },
);
