import fs from 'node:fs';
import path from 'node:path';
import type { Plugin } from 'vite';

/**
 * Sprites dibujados (src/assets/pack/vsprites/<equipo>/<jugador>/<vista>.png) en trozos pequeños que se piden cuando
 * hacen falta: uno por equipo y uno por ojeador (scouts-<temporada>/<id>, que son miles y se fichan de uno en uno).
 * - virtual:vsprite-index: { sets: { '<equipo>' | 'scouts-<t>/<id>': () => import(trozo) } }
 * - cada trozo: { files: { '<equipo>/<jugador>/<vista>': url } } (las imágenes van dentro, en base64: así no son miles de
 *   archivos sueltos, que Cloudflare Pages no admite más de 20.000)
 */
export function vsprites(): Plugin {
  const dir = path.resolve(__dirname, 'src/assets/pack/vsprites');
  const INDEX = 'virtual:vsprite-index';
  const SET = 'virtual:vsprite-set/';
  const ls = (d: string) => (fs.existsSync(d) ? fs.readdirSync(d).filter((f) => !f.startsWith('.')).sort() : []);
  return {
    name: 'vsprites',
    resolveId(id) {
      if (id === INDEX || id.startsWith(SET)) return '\0' + id;
      return null;
    },
    load(id) {
      if (id === '\0' + INDEX) {
        const sets: string[] = [];
        for (const team of ls(dir)) {
          if (team.startsWith('scouts-')) for (const p of ls(path.join(dir, team))) sets.push(`${team}/${p}`);
          else sets.push(team);
        }
        return `export const sets = {\n${sets.map((s) => `  ${JSON.stringify(s)}: () => import(${JSON.stringify(SET + s)})`).join(',\n')}\n};\n`;
      }
      if (id.startsWith('\0' + SET)) {
        const rel = id.slice(1 + SET.length);
        const [team, only] = rel.split('/');
        const lines: string[] = [];
        const entries: string[] = [];
        for (const p of only ? [only] : ls(path.join(dir, team))) {
          for (const f of ls(path.join(dir, team, p)).filter((f) => f.endsWith('.png'))) {
            const v = `u${lines.length}`;
            lines.push(`import ${v} from ${JSON.stringify(path.join(dir, team, p, f) + '?url')};`);
            entries.push(`  ${JSON.stringify(`${team}/${p}/${f.slice(0, -4)}`)}: ${v}`);
          }
        }
        return `${lines.join('\n')}\nexport const files = {\n${entries.join(',\n')}\n};\n`;
      }
      return null;
    },
  };
}
