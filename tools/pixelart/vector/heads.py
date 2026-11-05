"""Cabezas en vectores: base común (cara, orejas, contorno y sombreado) y el pelo de cada personaje como capas.

Unidades: la cabeza mide 100 de ancho. De frente la cara va de x 16 a 84 y de y 54 a 103 (barbilla). De perfil mira a
la derecha. Cada personaje (chars.py) da, para cada vista, una lista de capas: forma, color, si va detrás o delante de la
cara y si forma parte de la silueta (contorno exterior).
"""
import math

P = None  # transformación a píxeles: la pone body.py
SS = 6
OUT = (60, 24, 16, 255)


# ------------------------------------------------------------------ formas

def quad(p0, c, p1, n=20):
    return [((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * c[0] + t * t * p1[0], (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * c[1] + t * t * p1[1])
            for t in (i / n for i in range(n + 1))]


def lerp(a, b, t):
    return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)


def fat(a, b, tip, bulge=6):
    """Pincho o mechón con los lados curvos (bulge > 0 abombado, < 0 cóncavo)."""
    def ctrl(p0, sgn):
        mx, my = (p0[0] + tip[0]) / 2, (p0[1] + tip[1]) / 2
        dx, dy = tip[0] - p0[0], tip[1] - p0[1]
        L = math.hypot(dx, dy) or 1
        return (mx - dy / L * bulge * sgn, my + dx / L * bulge * sgn)
    return quad(a, ctrl(a, -1), tip) + quad(tip, ctrl(b, 1), b)[1:]


def blob(pts, n=10):
    """Curva cerrada y suave (Catmull-Rom) que pasa por los puntos."""
    out = []
    k = len(pts)
    for i in range(k):
        p0, p1, p2, p3 = pts[i - 1], pts[i], pts[(i + 1) % k], pts[(i + 2) % k]
        for j in range(n):
            t = j / n
            t2, t3 = t * t, t * t * t
            out.append(tuple(0.5 * (2 * p1[c] + (-p0[c] + p2[c]) * t + (2 * p0[c] - 5 * p1[c] + 4 * p2[c] - p3[c]) * t2 + (-p0[c] + 3 * p1[c] - 3 * p2[c] + p3[c]) * t3) for c in (0, 1)))
    return out


def ell(cx, cy, rx, ry, n=36):
    return [(cx + rx * math.cos(2 * math.pi * i / n), cy + ry * math.sin(2 * math.pi * i / n)) for i in range(n)]


def mirror(pts):
    return [(100 - x, y) for x, y in pts][::-1]


# ------------------------------------------------------------------ capas

def L(shape, c='mid', z='b', sil=True, ln=False, w=0):
    """Capa: forma rellena (o, con w > 0, un trazo de ese grosor: mechones y rayas del pelo)."""
    return {'s': shape, 'c': c, 'z': z, 'sil': sil and not w, 'ln': ln, 'w': w}


def strand(pts, c='deep', z='b', w=1.0):
    """Línea de mechón dentro del pelo (curva suave por los puntos)."""
    out = []
    for i in range(len(pts) - 1):
        a, b = pts[i], pts[i + 1]
        out += [lerp(a, b, t / 6) for t in range(6)]
    out.append(pts[-1])
    return L(out, c, z, False, False, w)


def spk(a, b, tip, bulge=6, z='b', light_left=True, sil=True, ln=False):
    """Mechón con su tono medio, la sombra del lado contrario a la luz y un brillo."""
    out = [L(fat(a, b, tip, bulge), 'mid', z, sil, ln)]
    mid = lerp(a, b, 0.55 if light_left else 0.45)
    out.append(L(fat(mid, b, tip, bulge * 0.6) if light_left else fat(a, mid, tip, bulge * 0.6), 'shade', z, False))
    la, lb = (lerp(a, b, 0.12), lerp(a, b, 0.36)) if light_left else (lerp(a, b, 0.64), lerp(a, b, 0.88))
    out.append(L(fat(lerp(la, tip, 0.12), lerp(lb, tip, 0.12), lerp(lerp(la, lb, 0.5), tip, 0.6), bulge * 0.3), 'light', z, False))
    return out


# ------------------------------------------------------------------ caras

FACE_FRONT = quad((19, 52), (17, 92), (50, 100)) + quad((50, 100), (83, 92), (81, 52))[1:] + quad((81, 52), (50, 26), (19, 52))[1:-1]
FACE_SIDE = blob([(48, 20), (72, 24), (85, 40), (87, 62), (87, 82), (82, 96), (72, 102), (58, 101), (42, 94), (24, 80), (16, 58), (24, 32)])


def poly(d, pts, fill):
    d.polygon([P(*p) for p in pts], fill=fill)


def line(d, pts, fill, w):
    d.line([P(*p) for p in pts], fill=fill, width=max(1, int(w * SS)), joint='curve')


def eyes_front(d, f, pal):
    style = f.get('eyes', 'normal')
    iris = pal.get('iris', (48, 34, 50, 255))
    ey = f.get('eye_y', 75)
    sep = f.get('eye_sep', 14)
    for cx, s in ((50 - sep, 1), (50 + sep, -1)):
        if style == 'none':
            continue
        if style == 'closed':
            line(d, quad((cx - 6, ey), (cx, ey + 4), (cx + 6, ey)), OUT, 2.2)
            continue
        if style == 'round':
            # ojo redondo pequeño: el blanco justo alrededor de una pupila grande (si no, a tamaño de partido se ve en blanco)
            d.ellipse([P(cx - 4.4, ey - 4.6), P(cx + 4.4, ey + 4.6)], fill=OUT)
            d.ellipse([P(cx - 3.3, ey - 3.5), P(cx + 3.3, ey + 3.5)], fill=(255, 255, 255, 255))
            d.ellipse([P(cx - 2.5, ey - 2.7), P(cx + 2.5, ey + 2.7)], fill=(20, 14, 18, 255))
            d.ellipse([P(cx - 1.6 + s * 0.4, ey - 2.2), P(cx - 0.4 + s * 0.4, ey - 1.0)], fill=(255, 255, 255, 255))
            continue
        if style == 'dot':
            d.ellipse([P(cx - 2.6, ey - 3), P(cx + 2.6, ey + 3)], fill=OUT)
            d.ellipse([P(cx - 1, ey - 2), P(cx + 0.6, ey - 0.4)], fill=(255, 255, 255, 255))
            continue
        if style == 'sharp':
            eye = [(cx - 8 * s, ey - 4), (cx + 7 * s, ey - 1.5), (cx + 5.5 * s, ey + 5), (cx - 6 * s, ey + 3.5)]
            poly(d, eye, (255, 255, 255, 255))
            d.ellipse([P(cx - 3.6 + s, ey - 3.4), P(cx + 3.6 + s, ey + 5.5)], fill=iris)
            d.ellipse([P(cx - 1.2 + s * 2, ey - 2), P(cx + 1.2 + s * 2, ey + 0.4)], fill=(255, 255, 255, 255))
            line(d, [eye[0], eye[1]], OUT, 3.0)
            continue
        # normal / big: ojo redondo de anime
        big = 1.2 if style == 'big' else 1.0
        rx, ry = 5.4 * big, 6.6 * big
        d.ellipse([P(cx - rx, ey - ry), P(cx + rx, ey + ry)], fill=(255, 255, 255, 255))
        d.ellipse([P(cx - rx * 0.78, ey - ry * 0.75), P(cx + rx * 0.78, ey + ry)], fill=iris)
        d.ellipse([P(cx - rx * 0.4, ey - ry * 0.3), P(cx + rx * 0.4, ey + ry * 0.6)], fill=(20, 14, 18, 255))
        d.ellipse([P(cx - rx * 0.6 + s * 1.5, ey - ry * 0.6), P(cx - rx * 0.05 + s * 1.5, ey - ry * 0.05)], fill=(255, 255, 255, 255))
        line(d, quad((cx - rx - 1, ey - ry * 0.4), (cx, ey - ry - 2.2), (cx + rx + 1, ey - ry * 0.4)), OUT, 2.6)
    if f.get('brows', True) and style not in ('none',):
        by = ey - (11 if style != 'dot' else 8)
        for cx, s in ((50 - sep, 1), (50 + sep, -1)):
            if f.get('brows') == 'angry':
                line(d, [(cx - 8 * s, by - 2), (cx + 7 * s, by + 3)], OUT, 3.0)
            else:
                line(d, quad((cx - 7, by + 1), (cx, by - 2), (cx + 7, by + 1)), OUT, 2.0)


def mouth_front(d, f):
    m = f.get('mouth', 'line')
    y = f.get('mouth_y', 91)
    if m == 'line':
        line(d, [(46, y), (54, y)], (130, 70, 50, 255), 1.4)
    elif m == 'smile':
        line(d, quad((44, y - 1), (50, y + 3), (56, y - 1)), (130, 70, 50, 255), 1.4)
    elif m == 'grin':  # dientes (Tod, Jack)
        poly(d, [(42, y - 3), (58, y - 3), (56, y + 3), (44, y + 3)], (120, 40, 40, 255))
        poly(d, [(44, y - 3), (56, y - 3), (55, y), (45, y)], (255, 255, 255, 255))
        line(d, [(42, y - 3), (58, y - 3), (56, y + 3), (44, y + 3), (42, y - 3)], OUT, 1.2)
    elif m == 'lips':  # labios gruesos (Jack): boca ancha sonriente
        w = f.get('mouth_w', 9)
        poly(d, quad((50 - w, y - 2), (50, y - 4), (50 + w, y - 2)) + quad((50 + w, y - 2), (50, y + 9), (50 - w, y - 2))[1:], (196, 106, 86, 255))
        line(d, quad((50 - w + 1, y - 0.5), (50, y + 4), (50 + w - 1, y - 0.5)), OUT, 1.3)
    elif m == 'buck':  # boca apretada con los dos dientes de delante (Tod)
        line(d, quad((42, y), (50, y - 2), (58, y)), OUT, 1.4)
        poly(d, [(46.5, y - 1.2), (53.5, y - 1.2), (53.5, y + 3.5), (46.5, y + 3.5)], (255, 255, 255, 255))
        line(d, [(46.5, y - 1.2), (46.5, y + 3.5), (53.5, y + 3.5), (53.5, y - 1.2)], OUT, 1.0)
        line(d, [(50, y - 1), (50, y + 3.5)], OUT, 0.8)
    elif m == 'frown':
        line(d, quad((44, y + 1.5), (50, y - 2), (56, y + 1.5)), (130, 70, 50, 255), 1.4)


def eye_side(d, f, pal):
    style = f.get('eyes', 'normal')
    iris = pal.get('iris', (48, 34, 50, 255))
    ey = f.get('eye_y', 75)
    if style == 'none':
        return
    if style == 'closed':
        line(d, quad((74, ey), (79, ey + 3), (84, ey)), OUT, 2.2)
    elif style == 'dot':
        d.ellipse([P(79, ey - 3), P(83.5, ey + 3)], fill=OUT)
    elif style == 'round':
        d.ellipse([P(77, ey - 4.6), P(86, ey + 4.6)], fill=OUT)
        d.ellipse([P(78.2, ey - 3.4), P(84.8, ey + 3.4)], fill=(255, 255, 255, 255))
        d.ellipse([P(80.2, ey - 2.6), P(85, ey + 2.6)], fill=(20, 14, 18, 255))
    elif style == 'sharp':
        eye = [(74, ey - 3.5), (85, ey - 2), (84.5, ey + 5.5), (75, ey + 4.5)]
        poly(d, eye, (255, 255, 255, 255))
        d.ellipse([P(79, ey - 2.5), P(85.5, ey + 6)], fill=iris)
        line(d, [eye[0], eye[1]], OUT, 3.0)
    else:
        big = 1.2 if style == 'big' else 1.0
        d.ellipse([P(77, ey - 6.4 * big), P(86, ey + 6.4 * big)], fill=(255, 255, 255, 255))
        d.ellipse([P(79.5, ey - 4.6 * big), P(86.4, ey + 6.4 * big)], fill=iris)
        d.ellipse([P(81, ey - 3.6 * big), P(83.4, ey - 0.8 * big)], fill=(255, 255, 255, 255))
        line(d, quad((76, ey - 3), (81, ey - 7.5 * big), (86.6, ey - 4)), OUT, 2.6)
    if f.get('brows', True):
        by = ey - 11
        if f.get('brows') == 'angry':
            line(d, [(70, by - 1), (84, by + 3)], OUT, 3.0)
        else:
            line(d, quad((72, by + 1), (78, by - 2), (85, by)), OUT, 2.0)
    m = f.get('mouth', 'line')
    y = f.get('mouth_y', 91)
    if m in ('grin',):
        poly(d, [(80, y - 2.5), (87, y - 3), (86, y + 2.5), (80, y + 2)], (255, 255, 255, 255))
        line(d, [(80, y - 2.5), (87, y - 3), (86, y + 2.5), (80, y + 2), (80, y - 2.5)], OUT, 1.1)
    elif m == 'lips':
        poly(d, ell(84, y, 4, 3), (200, 110, 90, 255))
    else:
        line(d, [(80, y), (85.5, y - 0.5)], (130, 70, 50, 255), 1.3)


# ------------------------------------------------------------------ dibujo

def resolve(c, pal):
    return c if isinstance(c, tuple) else pal[c]


def draw(d, spec, view):
    """Dibuja la cabeza de un personaje (spec de chars.py) en la vista 'front', 'side' o 'back'."""
    pal = spec['pal']
    f = spec.get('face', {})
    layers = [l for item in spec[view] for l in (item if isinstance(item, list) else [item])]
    ears = f.get('ears', True)
    W = 2.0
    big_ears = f.get('big_ears', 0)
    eo = f.get('ear_out', 0)
    ear_spots = {'front': [(18 - eo, 72), (82 + eo, 72)], 'back': [(18 - eo, 70), (82 + eo, 70)], 'side': [(46, 70)]}[view]
    face_front = f.get('face_front', FACE_FRONT)
    face_side = f.get('face_side', FACE_SIDE)
    face = face_front if view == 'front' else face_side if view == 'side' else None
    # 1) silueta: contorno grueso alrededor de todo
    sil = [l['s'] for l in layers if l['sil']] + ([face] if face else [])
    if ears:
        for ex, ey in ear_spots:
            d.ellipse([P(ex - 6 - big_ears, ey - 8 - big_ears), P(ex + 6 + big_ears, ey + 8 + big_ears)], fill=OUT)
    for sh in sil:
        q = [P(*p) for p in sh]
        d.line(q + [q[0]], fill=OUT, width=int(W * 2 * SS), joint='curve')
        d.polygon(q, fill=OUT)
    # 2) orejas (de perfil, más tarde: encima del pelo)
    def draw_ears():
        for ex, ey in ear_spots:
            r = 4.4 + big_ears
            d.ellipse([P(ex - r - 1.6, ey - 8 - big_ears), P(ex + r + 1.6, ey + 8 + big_ears)], fill=OUT)
            d.ellipse([P(ex - r, ey - 6.4 - big_ears), P(ex + r, ey + 6.4 + big_ears)], fill=pal['skin'])
            d.ellipse([P(ex - r * 0.4, ey - 4), P(ex + r * 0.4, ey + 4)], fill=pal['skin_d'])

    if ears and view != 'side' and not (view == 'front' and f.get('ears_front')):
        for ex, ey in ear_spots:
            r = 4.4 + big_ears
            d.ellipse([P(ex - r, ey - 6.4 - big_ears), P(ex + r, ey + 6.4 + big_ears)], fill=pal['skin'])
            d.ellipse([P(ex - r * 0.4, ey - 4), P(ex + r * 0.4, ey + 4)], fill=pal['skin_d'])
    # 3) capas de detrás
    def paint(l):
        if l['w']:
            line(d, l['s'], resolve(l['c'], pal), l['w'])
        else:
            poly(d, l['s'], resolve(l['c'], pal))

    if view == 'side':  # de perfil la cabeza entera es piel y el pelo va encima (marca el nacimiento del pelo)
        poly(d, face_side, pal['skin'])
        if 'face_side' not in f:
            poly(d, quad((60, 92), (68, 100), (78, 101)) + [(62, 102), (50, 97)], pal['skin_d'])
    for l in layers:
        if l['z'] == 'b':
            paint(l)
    # 4) cara, sombra bajo el pelo y rasgos
    if view == 'front':
        poly(d, face_front, pal['skin'])
        if 'face_front' not in f:
            poly(d, quad((73, 64), (79, 92), (58, 100)) + quad((58, 100), (79, 93), (81, 62))[1:], pal['skin_d'])
        # el pelo tapa la frente hasta su línea de nacimiento ('hairline': altura en los lados y en el centro)
        hl = f.get('hairline', (64, 50))
        if hl:
            from PIL import Image, ImageDraw as _ID
            img = d._image
            top = Image.new('RGBA', img.size)
            td = _ID.Draw(top)
            for l in layers:
                if l['z'] == 'b':
                    if l['w']:
                        td.line([P(*p) for p in l['s']], fill=resolve(l['c'], pal), width=max(1, int(l['w'] * SS)))
                    else:
                        td.polygon([P(*p) for p in l['s']], fill=resolve(l['c'], pal))
            if isinstance(hl, list):  # nacimiento del pelo con forma propia (entradas, pico...)
                curve = [(-10, hl[0][1])] + blob(hl, 6)[:len(hl) * 6 - 5] + [(110, hl[-1][1])] if False else [(-10, hl[0][1])] + hl + [(110, hl[-1][1])]
            else:
                side_y, center_y = hl
                curve = quad((-10, side_y), (50, 2 * center_y - side_y), (110, side_y))
            mask = Image.new('L', img.size, 0)
            _ID.Draw(mask).polygon([P(-10, -60)] + [P(*p) for p in curve] + [P(110, -60)], fill=255)
            # línea del nacimiento del pelo (contorno fino), solo donde hay pelo
            edge = Image.new('RGBA', img.size)
            _ID.Draw(edge).line([P(*p) for p in curve], fill=OUT, width=int(1.3 * SS))
            ea = edge.split()[3]
            ta = top.split()[3].point(lambda v: 255 if v else 0)
            from PIL import ImageChops
            top.putalpha(ImageChops.multiply(ta, mask))
            img.alpha_composite(top)
            edge.putalpha(ImageChops.multiply(ea, ta.filter(__import__('PIL.ImageFilter', fromlist=['x']).MaxFilter(5))))
            img.alpha_composite(edge)
        eyes_front(d, f, pal)
        mouth_front(d, f)
        if f.get('nose'):
            nx, ny, nr = f['nose']
            d.ellipse([P(nx - nr - 1, ny - nr * 0.8 - 1), P(nx + nr + 1, ny + nr * 0.8 + 1)], fill=OUT)
            d.ellipse([P(nx - nr, ny - nr * 0.8), P(nx + nr, ny + nr * 0.8)], fill=pal.get('nose', pal['skin_d']))
    # 5) capas de delante (flequillos, gorros, gafas...)
    for l in layers:
        if l['z'] == 'f':
            paint(l)
    if view == 'front' and ears and f.get('ears_front'):
        draw_ears()
    if view == 'side':
        if ears:
            draw_ears()
        eye_side(d, f, pal)
        if f.get('nose_side'):
            nx, ny, nr = f['nose_side']
            d.ellipse([P(nx - nr - 1, ny - nr * 0.8 - 1), P(nx + nr + 1, ny + nr * 0.8 + 1)], fill=OUT)
            d.ellipse([P(nx - nr, ny - nr * 0.8), P(nx + nr, ny + nr * 0.8)], fill=pal.get('nose', pal['skin_d']))
    # 6) líneas interiores
    for l in layers:
        if l['ln']:
            q = [P(*p) for p in l['s']]
            d.line(q + [q[0]], fill=OUT, width=int(1.1 * SS), joint='curve')
    # 7) extras de la cara por encima de todo (gafas)
    if view == 'front' and f.get('glasses'):
        for cx in (36, 64):
            gy = f.get('eye_y', 75)
            if f.get('glasses_rect'):
                line(d, [(cx - 10, gy - 6), (cx + 10, gy - 6), (cx + 9, gy + 6), (cx - 9, gy + 6), (cx - 10, gy - 6)], f['glasses'], 1.8)
            else:
                line(d, ell(cx, gy, 9, 6.5) + [ell(cx, gy, 9, 6.5)[0]], f['glasses'], 1.6)
        line(d, [(45, f.get('eye_y', 75) - 1), (55, f.get('eye_y', 75) - 1)], f['glasses'], 1.4)
    if view == 'side' and f.get('glasses'):
        gy = f.get('eye_y', 75)
        line(d, ell(80, gy, 6, 6.5) + [ell(80, gy, 6, 6.5)[0]], f['glasses'], 1.6)
        line(d, [(74, gy - 1), (50, gy - 6)], f['glasses'], 1.4)
