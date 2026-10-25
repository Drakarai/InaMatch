#!/usr/bin/env bash
# Regenera data/tecnicas.json a partir de las wikis de Inazuma Eleven (inglés y español).
# Uso: tools/wiki/build.sh   (desde la raíz del repo; hace unas 50 peticiones, con pausas)
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$HERE/../.." && pwd)"
TMP="$(mktemp -d)"
EN_API=https://inazuma-eleven.fandom.com/api.php
ES_API=https://inazuma.fandom.com/es/api.php

python3 -I "$HERE/fetch_category.py" "$EN_API" "Category:Hissatsu" es "$TMP/hissatsu_raw.json"
python3 -I "$HERE/fetch_category.py" "$ES_API" "Categoría:Supertécnicas" en "$TMP/supertecnicas_raw.json"
python3 -I "$HERE/parse_hissatsu.py" "$TMP/hissatsu_raw.json" "$TMP/hissatsu.json"
python3 -I -c "
import json, sys
es = json.load(open('$TMP/supertecnicas_raw.json')); en = json.load(open('$TMP/hissatsu_raw.json'))
json.dump(sorted({p['link'] for p in es if p.get('link')}), open('$TMP/titles_en.json', 'w'))
json.dump(sorted({p['link'] for p in en if p.get('link')}), open('$TMP/titles_es.json', 'w'))
"
python3 -I "$HERE/resolve_redirects.py" "$EN_API" "$TMP/titles_en.json" "$TMP/redir_en.json"
python3 -I "$HERE/resolve_redirects.py" "$ES_API" "$TMP/titles_es.json" "$TMP/redir_es.json"
python3 -I "$HERE/merge_names.py" "$TMP/hissatsu.json" "$TMP/supertecnicas_raw.json" "$TMP/redir_en.json" "$TMP/redir_es.json" "$TMP/tecnicas.json"
python3 -I "$HERE/export.py" "$TMP/tecnicas.json" "$TMP/hissatsu_raw.json" "$ROOT/data/tecnicas.json"
rm -rf "$TMP"
