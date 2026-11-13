import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import type { Plugin } from 'vite';

/**
 * Sprites dibujados (src/assets/pack/vsprites/<equipo>/<jugador>/<vista>.png) en trozos pequeños que se piden cuando
 * hacen falta: uno por equipo y uno por ojeador (scouts-<temporada>/<id>, que son miles y se fichan de uno en uno).
 * - virtual:vsprite-index: { sets: { '<equipo>' | 'scouts-<t>/<id>': () => import(trozo) } }
 * - virtual:vsprite-index también da masks: los mapas de equipación (mask-<vista>.png), en trozos aparte (uno por equipo
 *   o temporada de ojeadores) que solo se piden para vestir a Mi club con un uniforme (src/club/uniforms.ts)
 * - cada trozo: { files: { '<equipo>/<jugador>/<vista>': url } } (las imágenes van dentro, en base64: así no son miles de
 *   archivos sueltos, que Cloudflare Pages no admite más de 20.000)
 */
export function vsprites(): Plugin {
  const dir = path.resolve(__dirname, 'src/assets/pack/vsprites');
  const INDEX = 'virtual:vsprite-index';
  const SET = 'virtual:vsprite-set/';
  const MASK = 'virtual:vsprite-mask/';
  const ls = (d: string) => (fs.existsSync(d) ? fs.readdirSync(d).filter((f) => !f.startsWith('.')).sort() : []);
  let serve = false;
  let single = false;
  return {
    name: 'vsprites',
    configResolved(c) {
      serve = c.command === 'serve';
      single = c.mode === 'single';
    },
    resolveId(id) {
      if (id === INDEX || id.startsWith(SET) || id.startsWith(MASK)) return '\0' + id;
      return null;
    },
    load(id) {
      if (id === '\0' + INDEX) {
        const sets: string[] = [];
        for (const team of ls(dir)) {
          if (team.startsWith('scouts-')) for (const p of ls(path.join(dir, team))) sets.push(`${team}/${p}`);
          else sets.push(team);
        }
        const map = (prefix: string, chunk: (s: string) => string) =>
          `{\n${sets.map((s) => `  ${JSON.stringify(s)}: () => import(${JSON.stringify(prefix + chunk(s))})`).join(',\n')}\n}`;
        // los mapas, en un trozo por equipo (los ojeadores, uno por temporada): son pocos bytes y así no hay miles de trozos
        return `export const sets = ${map(SET, (s) => s)};\nexport const masks = ${map(MASK, (s) => s.split('/')[0])};\n`;
      }
      if (id.startsWith('\0' + SET) || id.startsWith('\0' + MASK)) {
        const isMask = id.startsWith('\0' + MASK);
        const rel = id.slice(1 + (isMask ? MASK : SET).length);
        const [team, only] = rel.split('/');
        const files: { key: string; file: string }[] = [];
        for (const p of only ? [only] : ls(path.join(dir, team))) {
          for (const f of ls(path.join(dir, team, p)).filter((f) => f.endsWith('.png') && f.startsWith('mask-') === isMask)) {
            files.push({ key: `${team}/${p}/${f.slice(isMask ? 5 : 0, -4)}`, file: path.join(dir, team, p, f) });
          }
        }
        if (serve || single) {
          // en desarrollo (y en el HTML único): cada imagen, tal cual en base64
          const entries = files.map(({ key, file }) => `  ${JSON.stringify(key)}: "data:image/png;base64,${fs.readFileSync(file).toString('base64')}"`);
          return `export const files = {\n${entries.join(',\n')}\n};\n`;
        }
        // al compilar: todas las imágenes del trozo, seguidas, en un solo archivo binario (el juego lo baja y lo separa,
        // ver unpackSet en src/gfx/pack.ts). Así no van en el código como texto: antes eran ~300 MB de base64 que la
        // compilación tenía que tener en memoria
        const bufs: Buffer[] = [];
        const index: Record<string, [number, number]> = {};
        let off = 0;
        for (const { key, file } of files) {
          const b = fs.readFileSync(file);
          index[key] = [off, b.length];
          off += b.length;
          bufs.push(b);
        }
        const source = Buffer.concat(bufs);
        const hash = crypto.createHash('md5').update(source).digest('hex').slice(0, 8);
        const fileName = `assets/vs/${isMask ? 'm-' : ''}${rel.replace(/\//g, '__')}-${hash}.bin`;
        this.emitFile({ type: 'asset', fileName, source });
        return `export const pack = ${JSON.stringify('./' + fileName)};\nexport const index = JSON.parse(${JSON.stringify(JSON.stringify(index))});\n`;
      }
      return null;
    },
  };
}
