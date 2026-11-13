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
  return {
    name: 'vsprites',
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
        const entries: string[] = [];
        for (const p of only ? [only] : ls(path.join(dir, team))) {
          for (const f of ls(path.join(dir, team, p)).filter((f) => f.endsWith('.png') && f.startsWith('mask-') === isMask)) {
            const key = JSON.stringify(`${team}/${p}/${f.slice(isMask ? 5 : 0, -4)}`);
            // los sprites y los mapas son diminutos (menos de 4 KB): van tal cual en base64. Antes cada sprite era un
            // módulo aparte (import ...png?url) y Vite acababa metiéndolo igual en base64, pero con 27.000 módulos la
            // compilación necesitaba 4 GB de memoria
            const data = fs.readFileSync(path.join(dir, team, p, f)).toString('base64');
            entries.push(`  ${key}: "data:image/png;base64,${data}"`);
          }
        }
        return `export const files = {\n${entries.join(',\n')}\n};\n`;
      }
      return null;
    },
  };
}
