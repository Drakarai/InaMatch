"""Cuerpos base y vistas (frente, perfil, espalda) en vectores, con la cabeza de Axel. Unidades: la cabeza mide 100 de ancho."""
import sys
from PIL import Image, ImageDraw, ImageFont
import head_axel as V

SS = 6
NUM = '10'
OUT = V.OUT
X0, Y0 = -30, -20  # origen del lienzo en unidades
CW, CH = 160, 270
SKIN, HAIR = V.SKIN, V.HAIR
KIT = {
    'shirt': (246, 206, 52, 255), 'shirt_d': (214, 168, 30, 255),
    'sleeve': (36, 104, 184, 255), 'sleeve_d': (24, 74, 140, 255),
    'shorts': (36, 84, 168, 255), 'shorts_d': (24, 58, 124, 255),
    'sock': (246, 246, 246, 255), 'sock_d': (200, 206, 214, 255), 'stripe': (36, 104, 184, 255),
    'boot': (44, 44, 56, 255), 'boot_l': (90, 90, 106, 255),
}
# tipos de cuerpo: hombros, cintura, largo del torso, cadera, largo del pantalón, piernas, grosor de pierna y de brazo, largo del brazo
TYPES = {
    'normal': dict(sw=60, ww=50, tl=40, hip=54, sl=16, ll=46, lt=15, at=12, al=42),
    'delgado': dict(sw=54, ww=44, tl=46, hip=48, sl=16, ll=58, lt=12.5, at=10.5, al=50),
    'corpulento': dict(sw=80, ww=84, tl=54, hip=76, sl=18, ll=54, lt=21, at=17, al=54, round=True),
    'bajito': dict(sw=52, ww=46, tl=32, hip=48, sl=13, ll=34, lt=14, at=11.5, al=34),
    'chica': dict(sw=52, ww=42, tl=40, hip=54, sl=15, ll=50, lt=13, at=10.5, al=44),
}


def P(x, y):
    return ((x - X0) * SS, (y - Y0) * SS)


V.P = lambda x, y: P(x, y)
V.SS = SS


def shape(d, pts, fill, w=1.6):
    q = [P(*p) for p in pts]
    d.line(q + [q[0]], fill=OUT, width=int(w * 2 * SS), joint='curve')
    d.polygon(q, fill=fill)


def rrect(x0, y0, x1, y1, r):
    """Rectángulo redondeado como lista de puntos."""
    import math
    pts = []
    for cx, cy, a0 in ((x1 - r, y0 + r, -90), (x1 - r, y1 - r, 0), (x0 + r, y1 - r, 90), (x0 + r, y0 + r, 180)):
        for k in range(7):
            a = math.radians(a0 + k * 15)
            pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def trap(xt0, xt1, yt, xb0, xb1, yb, r=5):
    """Trapecio redondeado (torso): arriba de xt0 a xt1, abajo de xb0 a xb1."""
    return V.quad((xt0 + r, yt), (xt0, yt), (xt0 - 0.5, yt + r)) + V.quad((xb0, yb - r), (xb0, yb), (xb0 + r, yb))[0:] + \
        V.quad((xb1 - r, yb), (xb1, yb), (xb1, yb - r)) + V.quad((xt1 + 0.5, yt + r), (xt1, yt), (xt1 - r, yt))


def capsule(d, p0, p1, r, fill, shade=None, w=1.5):
    import math
    dx, dy = p1[0] - p0[0], p1[1] - p0[1]
    L = math.hypot(dx, dy) or 1
    nx, ny = -dy / L * r, dx / L * r
    a0 = math.atan2(ny, nx)
    pts = []
    for k in range(13):
        a = a0 + math.pi * k / 12
        pts.append((p0[0] + r * math.cos(a), p0[1] + r * math.sin(a)))
    for k in range(13):
        a = a0 + math.pi + math.pi * k / 12
        pts.append((p1[0] + r * math.cos(a), p1[1] + r * math.sin(a)))
    shape(d, pts, fill, w)
    if shade:  # tercio derecho en sombra
        sp = [(p0[0] + r * 0.35, p0[1]), (p0[0] + r * 0.95, p0[1]), (p1[0] + r * 0.95, p1[1]), (p1[0] + r * 0.35, p1[1])]
        d.polygon([P(*p) for p in sp], fill=shade)


# ------------------------------------------------------------------ cuerpo de frente / espalda

def body_front(d, t, back=False, num='10'):
    cx = 50
    top = 100
    waist = top + t['tl']
    leg_top = waist + t['sl'] - 4
    foot = leg_top + t['ll']
    # piernas
    for s in (-1, 1):
        x = cx + s * (t['hip'] / 2 - t['lt'] / 2 - 2)
        capsule(d, (x, leg_top), (x, foot - 6), t['lt'] / 2, SKIN['mid'], SKIN['shade'])
        sock_top = foot - t['ll'] * 0.5
        capsule(d, (x, sock_top), (x, foot - 6), t['lt'] / 2 + 0.6, KIT['sock'], KIT['sock_d'])
        d.rectangle([P(x - t['lt'] / 2 + 0.4, sock_top + 3), P(x + t['lt'] / 2 - 0.4, sock_top + 6)], fill=KIT['stripe'])
        bw = t['lt'] / 2 + 4
        shape(d, rrect(x - bw + s * 1.5, foot - 9, x + bw + s * 1.5, foot + 2, 5), KIT['boot'], 1.5)
        d.ellipse([P(x - bw * 0.5 + s * 1.5, foot - 7.5), P(x + s * 1.5, foot - 4.5)], fill=KIT['boot_l'])
    # pantalón
    hw = t['hip'] / 2
    shape(d, rrect(cx - hw, waist - 6, cx + hw, waist + t['sl'], 5), KIT['shorts'], 1.6)
    d.polygon([P(cx + hw * 0.45, waist - 4), P(cx + hw - 1.5, waist - 4), P(cx + hw - 1.5, waist + t['sl'] - 2), P(cx + hw * 0.45, waist + t['sl'] - 2)], fill=KIT['shorts_d'])
    d.line([P(cx, waist + 4), P(cx, waist + t['sl'] - 1)], fill=OUT, width=int(1.2 * SS))
    # brazos
    sw = t['sw'] / 2
    for s in (-1, 1):
        x = cx + s * (sw + t['at'] / 2 - 3)
        capsule(d, (x, top + 6), (x + s * 2, top + t['al']), t['at'] / 2, SKIN['mid'], SKIN['shade'])
        capsule(d, (x, top + 6), (x + s * 0.6, top + t['al'] * 0.42), t['at'] / 2 + 1, KIT['sleeve'], KIT['sleeve_d'])
        d.ellipse([P(x + s * 2 - t['at'] / 2 - 1, top + t['al'] - 2), P(x + s * 2 + t['at'] / 2 + 1, top + t['al'] + t['at'])], fill=OUT)
        d.ellipse([P(x + s * 2 - t['at'] / 2 + 0.6, top + t['al'] - 0.4), P(x + s * 2 + t['at'] / 2 - 0.6, top + t['al'] + t['at'] - 1.6)], fill=KIT.get('hand', SKIN['mid']))
    # torso
    ww = t['ww'] / 2
    if t.get('round'):
        bw = ww + 5  # barriga: más ancho a media altura que en hombros y cintura
        torso = V.quad((cx - sw + 8, top), (cx - sw - 2, top + 2), (cx - sw, top + 14)) + \
            V.quad((cx - sw, top + 14), (cx - bw - 2, waist - 18), (cx - ww + 4, waist + 2))[1:] + \
            V.quad((cx - ww + 4, waist + 2), (cx, waist + 6), (cx + ww - 4, waist + 2))[1:] + \
            V.quad((cx + ww - 4, waist + 2), (cx + bw + 2, waist - 18), (cx + sw, top + 14))[1:] + \
            V.quad((cx + sw, top + 14), (cx + sw + 2, top + 2), (cx + sw - 8, top))[1:]
    else:
        torso = trap(cx - sw, cx + sw, top, cx - ww, cx + ww, waist + 2, r=7)
    shape(d, torso, KIT['shirt'])
    d.polygon([P(cx + sw * 0.5, top + 3), P(cx + sw - 2, top + 5), P(cx + ww - 2, waist), P(cx + ww * 0.5, waist)], fill=KIT['shirt_d'])
    # mangas raglán (de color) desde el cuello
    for s in (-1, 1):
        d.polygon([P(cx + s * 7, top), P(cx + s * sw, top + 2), P(cx + s * (sw - 1), top + 14), P(cx + s * (sw - 7), top + 14)], fill=KIT['sleeve'])
        d.line([P(cx + s * 7, top), P(cx + s * (sw - 7), top + 14)], fill=OUT, width=int(1.1 * SS))
    if back:
        f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', int(22 * SS * t['sw'] / 60))
        d.text(P(cx, top + t['tl'] * 0.55), num, font=f, fill=KIT['sleeve'], anchor='mm', stroke_width=int(0.5 * SS), stroke_fill=KIT['sleeve_d'])
    else:
        d.polygon([P(cx - 8, top), P(cx + 8, top), P(cx, top + 9)], fill=KIT['sleeve'], outline=OUT)
    # cuello
    neck = rrect(cx - 7, 90, cx + 7, top + 3, 3)
    shape(d, neck, SKIN['shade'], 1.2)


# ------------------------------------------------------------------ cuerpo de perfil (mirando a la derecha)

def body_side(d, t, step=0):
    cx = 50
    top = 100
    depth = max(34, t['sw'] * 0.66)
    waist = top + t['tl']
    leg_top = waist + t['sl'] - 4
    foot = leg_top + t['ll']
    lt = t['lt']
    stride = {0: 0, 1: 1, 2: -1}[step]
    # piernas: la de atrás más oscura
    for k, (dx, dark) in enumerate(((-stride * 9, True), (stride * 9, False))):
        x0 = cx
        x1 = cx + dx
        sk = SKIN['shade'] if dark else SKIN['mid']
        capsule(d, (x0, leg_top), (x1, foot - 6), lt / 2, sk, None if dark else SKIN['shade'])
        sock_top = leg_top + (foot - leg_top) * 0.5
        sx = x0 + (x1 - x0) * 0.5
        capsule(d, (sx, sock_top), (x1, foot - 6), lt / 2 + 0.6, KIT['sock_d'] if dark else KIT['sock'])
        shape(d, rrect(x1 - lt / 2 - 1, foot - 9, x1 + lt / 2 + 9, foot + 2, 5), KIT['boot'], 1.5)
        d.ellipse([P(x1 + 1, foot - 7.5), P(x1 + lt / 2 + 6, foot - 4.5)], fill=KIT['boot_l'])
    # pantalón
    shape(d, rrect(cx - depth / 2 - 1, waist - 6, cx + depth / 2 + 1, waist + t['sl'], 5), KIT['shorts'])
    # torso
    shape(d, rrect(cx - depth / 2, top, cx + depth / 2, waist + 2, 8), KIT['shirt'])
    d.polygon([P(cx - depth / 2 + 2, top + 8), P(cx - depth / 2 + 7, top + 8), P(cx - depth / 2 + 7, waist), P(cx - depth / 2 + 2, waist)], fill=KIT['shirt_d'])
    # brazo (el de este lado), colgando con un leve balanceo
    sw_arm = -stride * 6
    capsule(d, (cx, top + 7), (cx + sw_arm, top + t['al']), t['at'] / 2, SKIN['mid'], SKIN['shade'])
    capsule(d, (cx, top + 7), (cx + sw_arm * 0.4, top + t['al'] * 0.42), t['at'] / 2 + 1, KIT['sleeve'], KIT['sleeve_d'])
    d.ellipse([P(cx + sw_arm - t['at'] / 2 - 1, top + t['al'] - 2), P(cx + sw_arm + t['at'] / 2 + 1, top + t['al'] + t['at'])], fill=OUT)
    d.ellipse([P(cx + sw_arm - t['at'] / 2 + 0.6, top + t['al'] - 0.4), P(cx + sw_arm + t['at'] / 2 - 0.6, top + t['al'] + t['at'] - 1.6)], fill=KIT.get('hand', SKIN['mid']))
    shape(d, rrect(cx - 4, 90, cx + 8, top + 4, 3), SKIN['shade'], 1.2)


# ------------------------------------------------------------------ cabeza de Axel: perfil y espalda

def fat(base_a, base_b, tip, bulge=7):
    """Pincho gordo y redondeado: los puntos de control se abren hacia fuera para que los lados salgan curvos."""
    import math
    def side(p0, sgn):
        mx, my = (p0[0] + tip[0]) / 2, (p0[1] + tip[1]) / 2
        dx, dy = tip[0] - p0[0], tip[1] - p0[1]
        L = math.hypot(dx, dy) or 1
        return (mx - dy / L * bulge * sgn, my + dx / L * bulge * sgn)
    return V.quad(base_a, side(base_a, -1), tip) + V.quad(tip, side(base_b, 1), base_b)[1:]


SIDE_SPIKES = [  # pocos, gordos y hacia arriba (un poco hacia atrás): base de atrás, base de delante, punta
    ((24, 84), (10, 46), (-8, 50)),
    ((14, 62), (34, 34), (2, 6)),
    ((26, 40), (52, 28), (24, -10)),
    ((46, 30), (70, 34), (54, -12)),
    ((62, 36), (80, 48), (82, 4)),
]


def head_side(d):
    W = 2.0
    # cráneo con la nuca rellena hasta el cuello (sin huecos detrás de la base del último pincho)
    skull = V.quad((44, 86), (24, 92), (18, 70)) + V.quad((18, 70), (12, 26), (52, 24))[1:] + V.quad((52, 24), (84, 26), (84, 62))[1:]
    face = V.quad((62, 48), (86, 50), (88, 76)) + V.quad((88, 76), (90, 98), (72, 102))[1:] + V.quad((72, 102), (52, 102), (40, 90))[1:] + [(40, 60)]
    spikes = [fat(a, b, tp) for a, b, tp in SIDE_SPIKES]
    for sh in spikes + [skull, face]:
        q = [P(*p) for p in sh]
        d.line(q + [q[0]], fill=OUT, width=int(W * 2 * SS), joint='curve')
        d.polygon(q, fill=OUT)
    d.polygon([P(*p) for p in face], fill=SKIN['mid'])
    d.polygon([P(*p) for p in skull], fill=HAIR['shade'])
    for (a, b, tp) in SIDE_SPIKES:
        d.polygon([P(*p) for p in fat(a, b, tp)], fill=HAIR['mid'])
        d.polygon([P(*p) for p in fat(a, V.lerp(a, b, 0.45), tp, 4)], fill=HAIR['shade'])
        la, lb = V.lerp(a, b, 0.62), V.lerp(a, b, 0.88)
        d.polygon([P(*p) for p in fat(V.lerp(la, tp, 0.12), V.lerp(lb, tp, 0.12), V.lerp(V.lerp(la, lb, 0.5), tp, 0.62), 2.5)], fill=HAIR['light'])
    # pelo que baja por detrás hasta la nuca, y patilla
    back = V.quad((16, 50), (16, 80), (36, 88)) + [(44, 84), (44, 50)]
    d.polygon([P(*p) for p in back], fill=HAIR['shade'])
    d.polygon([P(*p) for p in V.spike((52, 54), (62, 54), (56, 78), (-1, 0))], fill=HAIR['shade'])
    # pinchos del lado de la cabeza que vemos: nacen junto a la frente y la sien y se van hacia atrás,
    # tapando el lateral (como en el modelo 3D); con línea propia para que se lean como capas
    NEAR = [  # dos pinchos gordos en el lateral, de la sien hacia arriba y atrás
        ((40, 62), (58, 46), (22, 18), (0, 0)),
        ((56, 50), (70, 36), (44, 4), (0, 0)),
    ]
    for lo, hi, tp, bd in NEAR:
        sp = fat(lo, hi, tp, 6)
        q = [P(*p) for p in sp]
        d.polygon(q, fill=HAIR['mid'])
        d.polygon([P(*p) for p in fat(lo, V.lerp(lo, hi, 0.45), tp, 3)], fill=HAIR['shade'])
        d.polygon([P(*p) for p in fat(V.lerp(lo, hi, 0.68), hi, V.lerp(V.lerp(lo, hi, 0.85), tp, 0.62), 2)], fill=HAIR['light'])
        d.line(q, fill=OUT, width=int(1.1 * SS), joint='curve')
    # flequillo hacia delante sobre la frente
    d.polygon([P(*p) for p in V.spike((60, 42), (78, 44), (84, 62), (3, 0))], fill=HAIR['mid'])
    d.polygon([P(*p) for p in V.spike((68, 43), (78, 44), (84, 62), (3, 0))], fill=HAIR['light'])
    q = [P(*p) for p in V.spike((60, 42), (78, 44), (84, 62), (3, 0))]
    d.line(q, fill=OUT, width=int(1.2 * SS))
    # oreja
    d.ellipse([P(40, 66), P(52, 82)], fill=OUT)
    d.ellipse([P(41.6, 67.6), P(50.4, 80.4)], fill=SKIN['mid'])
    d.ellipse([P(44, 70), P(48, 78)], fill=SKIN['shade'])
    # ceja, ojo y boca
    d.line([P(70, 70), P(84, 73)], fill=OUT, width=int(3.0 * SS))
    eye = [(74, 78.5), (85, 80), (84.5, 87.5), (75, 86.5)]
    d.polygon([P(*p) for p in eye], fill=(255, 255, 255, 255))
    d.ellipse([P(79, 79.5), P(85.5, 88)], fill=(48, 34, 50, 255))
    d.ellipse([P(81.5, 81), P(83.5, 83.4)], fill=(255, 255, 255, 255))
    d.line([P(*eye[0]), P(*eye[1])], fill=OUT, width=int(3.0 * SS))
    d.line([P(80, 96), P(85, 95.5)], fill=(130, 70, 50, 255), width=int(1.3 * SS))
    # sombra de la mejilla bajo el pelo
    d.polygon([P(*p) for p in V.quad((50, 84), (60, 98), (72, 101)) + [(52, 101), (42, 90)]], fill=SKIN['shade'])


def head_back(d):
    W = 2.0
    mass = V.quad((18, 54), (12, 92), (36, 98)) + [(42, 92), (50, 99), (58, 92), (64, 98)] + V.quad((64, 98), (88, 92), (82, 54))[1:]
    spikes = [V.spike(bl, br, tp, bd) for bl, br, tp, bd, _ in V.SPIKES] + [V.CAP, mass]
    for cx in (18, 82):
        d.ellipse([P(cx - 6, 64), P(cx + 6, 80)], fill=OUT)
    for sh in spikes:
        q = [P(*p) for p in sh]
        d.line(q + [q[0]], fill=OUT, width=int(W * 2 * SS), joint='curve')
        d.polygon(q, fill=OUT)
    for cx in (18, 82):
        d.ellipse([P(cx - 4.4, 65.6), P(cx + 4.4, 78.4)], fill=SKIN['mid'])
        d.ellipse([P(cx - 1.8, 68), P(cx + 1.8, 76)], fill=SKIN['shade'])
    d.polygon([P(*p) for p in V.CAP], fill=HAIR['shade'])
    # la masa de la nuca primero; los pinchos encima
    d.polygon([P(*p) for p in mass], fill=HAIR['mid'])
    d.polygon([P(*p) for p in V.quad((54, 60), (72, 62), (82, 58)) + V.quad((82, 58), (86, 90), (64, 98))[1:] + [(58, 92), (56, 74)]], fill=HAIR['shade'])
    for bl, br, tp, bd, ll in V.SPIKES:
        d.polygon([P(*p) for p in V.spike(bl, br, tp, bd)], fill=HAIR['mid'])
        mid = V.lerp(bl, br, 0.55 if ll else 0.45)
        sh = V.spike(mid, br, tp, bd) if ll else V.spike(bl, mid, tp, bd)
        d.polygon([P(*p) for p in sh], fill=HAIR['shade'])
        a = V.lerp(bl, br, 0.14 if ll else 0.86)
        b = V.lerp(bl, br, 0.36 if ll else 0.64)
        d.polygon([P(*p) for p in V.spike(V.lerp(a, tp, 0.14), V.lerp(b, tp, 0.14), V.lerp(V.lerp(a, b, 0.5), tp, 0.6), (bd[0] * 0.6, bd[1] * 0.6))], fill=HAIR['light'])
    # mechones de la nuca
    for bl, br, tp in (((20, 62), (40, 60), (30, 96)), ((38, 60), (62, 60), (50, 100)), ((60, 60), (80, 62), (70, 96))):
        d.polygon([P(*p) for p in V.spike(bl, br, tp, (0, 0))], fill=HAIR['mid'])
        d.polygon([P(*p) for p in V.spike(V.lerp(bl, br, 0.5), br, tp, (0, 0))], fill=HAIR['shade'])
    for x in (36, 50, 64):
        d.line([P(x, 80), P(x + (2 if x > 50 else -2 if x < 50 else 0), 96)], fill=HAIR['deep'], width=int(1.0 * SS))


# ------------------------------------------------------------------ montaje

import heads as H  # noqa: E402

H.P = P
H.SS = SS
AXEL_SKIN = dict(SKIN)
DEFAULT_KIT = dict(KIT)


def hexc(h):
    return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5)) + (255,)


def tone(c, f):
    return tuple(max(0, min(255, int(v * f))) for v in c[:3]) + (255,)


def kit_for(colors, gk=False):
    """Equipación a partir de los colores del equipo (src/data/teams): camiseta, mangas, pantalón y medias."""
    shirt = hexc(colors['gkShirt'] if gk else colors['shirt'])
    shorts = hexc(colors['shorts'])
    sleeve = tone(shirt, 0.72) if gk else shorts
    k = dict(DEFAULT_KIT)
    k.update({'shirt': shirt, 'shirt_d': tone(shirt, 0.84), 'sleeve': sleeve, 'sleeve_d': tone(sleeve, 0.75),
              'shorts': shorts, 'shorts_d': tone(shorts, 0.72), 'stripe': shorts})
    if gk:
        k['hand'] = (246, 246, 246, 255)
    return k


def cape(d, t, view):
    """Capa (Jude): de frente asoma por detrás de los hombros; de espaldas cubre la espalda; de perfil, por detrás."""
    c = KIT['cape']
    cd = tone(c, 0.75)
    top, sw = 100, t['sw'] / 2
    bottom = top + t['tl'] + t['sl'] + t['ll'] * 0.45
    if view == 'front':
        shape(d, [(50 - sw - 2, top + 2), (50 + sw + 2, top + 2), (50 + sw + 12, bottom), (50 - sw - 12, bottom)], cd)
    elif view == 'side':
        shape(d, [(36, top + 2), (56, top + 2), (36, bottom), (14, bottom + 2)], c)
    return bottom


def cape_back(d, t):
    c = KIT['cape']
    top, sw = 100, t['sw'] / 2
    bottom = top + t['tl'] + t['sl'] + t['ll'] * 0.45
    shape(d, [(50 - sw - 2, top), (50 + sw + 2, top), (50 + sw + 12, bottom), (50 - sw - 12, bottom)], c)
    d.polygon([P(50 + sw * 0.3, top + 4), P(50 + sw + 1, top + 4), P(50 + sw + 10, bottom - 2), P(50 + sw * 0.4, bottom - 2)], fill=tone(c, 0.8))


def figure(view, tname, step=0, char=None, kit=None, num=None):
    """Figura completa en vectores. char: ficha de chars.py (None = Axel); kit: de kit_for (None = el del Raimon)."""
    KIT.clear()
    KIT.update(kit or DEFAULT_KIT)
    if char is not None and char.get('cape'):
        KIT['cape'] = hexc(char['cape'])
    SKIN.clear()
    if char is None:
        SKIN.update(AXEL_SKIN)
    else:
        SKIN.update({'mid': char['pal']['skin'], 'shade': char['pal']['skin_d'], 'light': char['pal']['skin']})
    im = Image.new('RGBA', (CW * SS, CH * SS))
    d = ImageDraw.Draw(im)
    t = TYPES[tname]
    if 'cape' in KIT and view != 'back':
        cape(d, t, view)
    if view == 'front':
        body_front(d, t)
        V.head(d) if char is None else H.draw(d, char, 'front')
    elif view == 'back':
        body_front(d, t, back=True, num=num or NUM)
        if 'cape' in KIT:
            cape_back(d, t)
        head_back(d) if char is None else H.draw(d, char, 'back')
    else:
        body_side(d, t, step)
        head_side(d) if char is None else H.draw(d, char, 'side')
    return im


if __name__ == '__main__':
    V.OFF = 0
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 18)
    mode = sys.argv[2] if len(sys.argv) > 2 else 'views'
    if mode == 'views':
        cells = [('Frente', 'front', 'normal', 0), ('Perfil', 'side', 'normal', 0), ('Paso 1', 'side', 'normal', 1), ('Paso 2', 'side', 'normal', 2), ('Espalda', 'back', 'normal', 0)]
    else:
        cells = [(n.capitalize(), 'front', n, 0) for n in TYPES]
    sc = 300 / CH
    cw = int(CW * sc)
    sheet = Image.new('RGBA', (len(cells) * cw + 20, 340), (250, 248, 240, 255))
    dd = ImageDraw.Draw(sheet)
    for i, (label, view, tn, st) in enumerate(cells):
        f = figure(view, tn, st).resize((cw, 300), Image.LANCZOS)
        sheet.alpha_composite(f, (10 + i * cw, 30))
        dd.text((10 + i * cw + cw // 2, 14), label, fill=(40, 30, 30), font=font, anchor='mm')
    sheet.save(sys.argv[1])
