import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import type { Plugin } from 'vite';

/**
 * Retratos de Victory Road (src/assets/pack/portraits/<equipo>/<jugador>.webp, unos 5.500) sin un módulo por imagen.
 * - virtual:portrait-index: { '<equipo>/<jugador>': url }
 * - Al compilar, cada retrato se copia tal cual a assets/portraits/<equipo>/<jugador>-<huella>.webp (la huella cambia si
 *   cambia la imagen, para que el navegador no use una vieja). En desarrollo, la url es la del archivo original.
 * Antes eran un import.meta.glob con un módulo por retrato, lo que disparaba la memoria al compilar.
 */
export function portraits(): Plugin {
  const dir = path.resolve(__dirname, 'src/assets/pack/portraits');
  const ID = 'virtual:portrait-index';
  let serve = false;
  let single = false;
  const ls = (d: string) => (fs.existsSync(d) ? fs.readdirSync(d).filter((f) => !f.startsWith('.')).sort() : []);
  return {
    name: 'portraits',
    configResolved(c) {
      serve = c.command === 'serve';
      // el HTML único (npm run build:single) no lleva retratos: usa los provisionales
      single = c.mode === 'single';
    },
    resolveId(id) {
      return id === ID ? '\0' + ID : null;
    },
    load(id) {
      if (id !== '\0' + ID) return null;
      const out: Record<string, string> = {};
      if (!single) {
        for (const team of ls(dir)) {
          const tdir = path.join(dir, team);
          if (!fs.statSync(tdir).isDirectory()) continue;
          for (const f of ls(tdir)) {
            const m = f.match(/^(.+)\.(webp|png|jpe?g|gif)$/i);
            if (!m) continue;
            const key = `${team}/${m[1].toLowerCase()}`;
            if (serve) {
              out[key] = `/src/assets/pack/portraits/${team}/${f}`;
              continue;
            }
            const source = fs.readFileSync(path.join(tdir, f));
            const hash = crypto.createHash('md5').update(source).digest('hex').slice(0, 8);
            const fileName = `assets/portraits/${team}/${m[1]}-${hash}.${m[2].toLowerCase()}`;
            this.emitFile({ type: 'asset', fileName, source });
            out[key] = `./${fileName}`;
          }
        }
      }
      return `export default JSON.parse(${JSON.stringify(JSON.stringify(out))});\n`;
    },
  };
}
