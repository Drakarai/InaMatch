"""Lector mínimo de tablas Lua literales (los módulos de datos de la wiki: Module:PlayerData/IE3,
Module:WazaData...). Entiende tablas, cadenas, números, true/false, claves `x=` y `["x"]=`
y comentarios `--`. Los comentarios de línea que van justo antes de un grupo (`--Inazuma Japan`)
se guardan como `__group__` en cada entrada que les sigue.
"""
import re

TOKEN = re.compile(
    r'''\s*(?:
        (?P<comment>--\[\[.*?\]\]|--[^\n]*) |
        (?P<str>"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*') |
        (?P<num>-?\d+(?:\.\d+)?) |
        (?P<name>[A-Za-z_]\w*) |
        (?P<sym>[{}=,;\[\]])
    )''',
    re.S | re.X,
)


def tokenize(src):
    pos = 0
    out = []
    while pos < len(src):
        m = TOKEN.match(src, pos)
        if not m or m.end() == pos:
            if src[pos:].strip() == '':
                break
            raise ValueError(f'no entiendo el Lua en {pos}: {src[pos:pos + 40]!r}')
        pos = m.end()
        kind = m.lastgroup
        out.append((kind, m.group(kind)))
    return out


class Parser:
    def __init__(self, tokens):
        self.t = tokens
        self.i = 0

    def peek(self, skip_comments=True):
        j = self.i
        while skip_comments and j < len(self.t) and self.t[j][0] == 'comment':
            j += 1
        return self.t[j] if j < len(self.t) else (None, None)

    def next(self):
        while self.t[self.i][0] == 'comment':
            self.i += 1
        tok = self.t[self.i]
        self.i += 1
        return tok

    def comments(self):
        found = []
        while self.i < len(self.t) and self.t[self.i][0] == 'comment':
            found.append(self.t[self.i][1])
            self.i += 1
        return found

    def value(self):
        kind, val = self.next()
        if kind == 'str':
            return bytes(val[1:-1], 'utf-8').decode('unicode_escape').encode('latin-1').decode('utf-8')
        if kind == 'num':
            return float(val) if '.' in val else int(val)
        if kind == 'name':
            return {'true': True, 'false': False, 'nil': None}.get(val, val)
        if val == '{':
            return self.table()
        raise ValueError(f'valor inesperado {val!r}')

    def table(self):
        arr, obj = [], {}
        group = None
        while True:
            for c in self.comments():
                text = c[2:].strip()
                if text and not text.startswith('['):
                    group = text
            kind, val = self.peek()
            if val == '}':
                self.next()
                break
            key = None
            if kind == 'name' and self.t[self._after(self.i)][1] == '=':
                key = self.next()[1]
                self.next()
            elif val == '[':
                self.next()
                key = self.value()
                self.next()  # ]
                self.next()  # =
            v = self.value()
            if isinstance(v, dict) and group is not None:
                v.setdefault('__group__', group)
            if key is None:
                arr.append(v)
            else:
                obj[key] = v
            kind, val = self.peek()
            if val in (',', ';'):
                self.next()
        if obj and arr:
            obj['__list__'] = arr
            return obj
        return obj if obj else arr

    def _after(self, i):
        """Índice del siguiente token que no es comentario después de i."""
        j = i
        while self.t[j][0] == 'comment':
            j += 1
        j += 1
        while self.t[j][0] == 'comment':
            j += 1
        return j


def table_end(src, i):
    """Índice justo después de la llave que cierra la tabla que empieza en src[i] == '{'."""
    depth = 0
    n = len(src)
    while i < n:
        c = src[i]
        if c in '"\'':
            q = c
            i += 1
            while i < n and src[i] != q:
                i += 2 if src[i] == '\\' else 1
        elif src.startswith('--[[', i):
            i = src.index(']]', i) + 1
        elif src.startswith('--', i):
            i = src.find('\n', i)
            if i < 0:
                return n
        elif c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    raise ValueError('tabla sin cerrar')


def parse_module(src, var):
    """Devuelve la tabla asignada a `local <var>=` dentro del módulo."""
    start = re.search(r'local\s+%s\s*=\s*\{' % re.escape(var), src)
    if not start:
        raise ValueError(f'no encuentro local {var}')
    begin = start.end() - 1
    p = Parser(tokenize(src[begin : table_end(src, begin)]))
    p.next()  # {
    return p.table()
