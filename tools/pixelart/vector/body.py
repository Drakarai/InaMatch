"""Cuerpos base y vistas (frente, perfil, espalda) en vectores, con la cabeza de Axel. Unidades: la cabeza mide 100 de ancho."""
import sys
from PIL import Image, ImageDraw, ImageFont
import head_axel as V

SS = 6
NUM = '10'
OUT = V.OUT
X0, Y0 = -30, -60  # origen del lienzo en unidades (margen arriba para los peinados altos)
CW, CH = 160, 330
SKIN, HAIR = V.SKIN, V.HAIR
KIT = {
    'shirt': (246, 206, 52, 255), 'shirt_d': (214, 168, 30, 255),
    'sleeve': (36, 104, 184, 255), 'sleeve_d': (24, 74, 140, 255),
    'shorts': (36, 84, 168, 255), 'shorts_d': (24, 58, 124, 255),
    'sock': (246, 246, 246, 255), 'sock_d': (200, 206, 214, 255), 'stripe': (36, 104, 184, 255),
    'boot': (44, 44, 56, 255), 'boot_l': (90, 90, 106, 255),
}
# tipos de cuerpo: hombros, cintura, largo del torso, cadera, largo del pantalón, piernas, grosor de pierna y de brazo, largo del brazo
TYPES = {  # medidas en unidades de cabeza (100 = ancho de la cabeza)
    'normal': dict(sw=54, ww=46, tl=40, hip=52, sl=22, ll=60, lt=11, at=9, al=50),
    'delgado': dict(sw=50, ww=40, tl=44, hip=46, sl=22, ll=70, lt=10, at=8.5, al=56),
    'corpulento': dict(sw=76, ww=80, tl=50, hip=76, sl=24, ll=56, lt=16, at=14, al=56, round=True),
    'bajito': dict(sw=48, ww=42, tl=32, hip=46, sl=18, ll=46, lt=10.5, at=8.5, al=40),
    'chica': dict(sw=48, ww=38, tl=40, hip=50, sl=20, ll=62, lt=10, at=8, al=50),
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
    """Cuerpo de frente (o de espaldas): brazos colgando, pantalón hasta la rodilla y medias altas."""
    cx, top = 50, 100
    sw, ww, hw = t['sw'] / 2, t['ww'] / 2, t['hip'] / 2
    waist = top + t['tl']
    short_bot = waist + t['sl']
    foot = short_bot + t['ll']
    knee = short_bot + t['ll'] * 0.3
    lt = t['lt']
    # piernas: muslo y rodilla de piel, media hasta debajo de la rodilla, bota
    for s in (-1, 1):
        x0 = cx + s * (hw * 0.45)
        x1 = cx + s * (hw * 0.42)
        if KIT.get('longPants'):  # pantalón largo de traje hasta los zapatos
            capsule(d, (x0, short_bot - 6), (x1, foot - 6), lt / 2 + 1.5, KIT['shorts'], KIT['shorts_d'])
        else:
            capsule(d, (x0, short_bot - 6), (x1, foot - 6), lt / 2, SKIN['mid'], SKIN['shade'])
            capsule(d, (x1, knee + 4), (x1, foot - 6), lt / 2 + 0.5, KIT['sock'], KIT['sock_d'])
            d.rectangle([P(x1 - lt / 2 + 0.2, knee + 6), P(x1 + lt / 2 - 0.2, knee + 9)], fill=KIT['stripe'])
        shape(d, blob_pts([(x1 - lt / 2 - 1.5 + s * 1, foot - 7), (x1 + lt / 2 + 1.5 + s * 1, foot - 7), (x1 + lt / 2 + 2.5 + s * 3, foot + 1.5),
                            (x1 - lt / 2 - 0.5 + s * 1, foot + 2)]), KIT['boot'], 1.4)
        d.ellipse([P(x1 - lt * 0.25 + s, foot - 5.5), P(x1 + lt * 0.15 + s, foot - 3)], fill=KIT['boot_l'])
    # pantalón: más ancho abajo, con la separación de las piernas
    shorts = [(cx - ww + 1, waist - 5), (cx + ww - 1, waist - 5), (cx + hw + 3, short_bot), (cx + 2, short_bot), (cx, short_bot - 6),
              (cx - 2, short_bot), (cx - hw - 3, short_bot)]
    shape(d, shorts, KIT['shorts'], 1.6)
    d.polygon([P(cx + ww * 0.4, waist - 3), P(cx + ww - 2, waist - 3), P(cx + hw + 1, short_bot - 1.5), P(cx + hw * 0.5, short_bot - 1.5)], fill=KIT['shorts_d'])
    # torso: hombros redondeados que se estrechan hacia la cintura (barriga en el corpulento)
    if t.get('round'):
        bw = ww + 4
        torso = V.quad((cx - sw + 8, top), (cx - sw - 2, top + 2), (cx - sw, top + 14)) + \
            V.quad((cx - sw, top + 14), (cx - bw - 2, waist - 18), (cx - ww + 4, waist + 2))[1:] + \
            V.quad((cx - ww + 4, waist + 2), (cx, waist + 6), (cx + ww - 4, waist + 2))[1:] + \
            V.quad((cx + ww - 4, waist + 2), (cx + bw + 2, waist - 18), (cx + sw, top + 14))[1:] + \
            V.quad((cx + sw, top + 14), (cx + sw + 2, top + 2), (cx + sw - 8, top))[1:]
    else:
        torso = V.quad((cx - sw + 7, top), (cx - sw, top), (cx - sw, top + 9)) + V.quad((cx - sw, top + 9), (cx - ww - 1, waist - 10), (cx - ww, waist + 1))[1:] + \
            [(cx + ww, waist + 1)] + V.quad((cx + ww, waist + 1), (cx + ww + 1, waist - 10), (cx + sw, top + 9))[1:] + V.quad((cx + sw, top + 9), (cx + sw, top), (cx + sw - 7, top))[1:]
    shape(d, torso, KIT['shirt'])
    if KIT.get('zig') and not back:  # la parte de abajo de la camiseta de otro color, que sube en dientes de sierra
        n, y0, y1 = 5, top + t['tl'] * 0.22, top + t['tl'] * 0.55
        pts = [(cx - ww - 1, waist + 1)]
        for k in range(2 * n + 1):  # picos blancos que suben (k impar) entre los dientes del color de la camiseta
            pts.append((cx - sw - 2 + (2 * sw + 4) * k / (2 * n), y0 if k % 2 else y1))
        pts.append((cx + ww + 1, waist + 1))
        import heads as _H
        clip = Image.new('L', (CW * SS, CH * SS), 0)
        ImageDraw.Draw(clip).polygon([P(*q) for q in torso], fill=255)
        layer = Image.new('RGBA', (CW * SS, CH * SS))
        ImageDraw.Draw(layer).polygon([P(*q) for q in pts], fill=KIT['zig'])
        from PIL import ImageChops
        layer.putalpha(ImageChops.multiply(layer.split()[3], clip))
        d._image.alpha_composite(layer)
    if KIT.get('vstripes'):  # rayas verticales (Argentina): franjas del otro color recortadas a la camiseta
        from PIL import ImageChops
        clip = Image.new('L', (CW * SS, CH * SS), 0)
        ImageDraw.Draw(clip).polygon([P(*q) for q in torso], fill=255)
        layer = Image.new('RGBA', (CW * SS, CH * SS))
        ld = ImageDraw.Draw(layer)
        for k in range(-3, 4, 2):
            x = cx + k * sw / 3.5
            ld.polygon([P(x - sw / 7, top - 2), P(x + sw / 7, top - 2), P(x + sw / 7, waist + 4), P(x - sw / 7, waist + 4)], fill=KIT['vstripes'])
        layer.putalpha(ImageChops.multiply(layer.split()[3], clip))
        d._image.alpha_composite(layer)
    d.polygon([P(cx + sw * 0.45, top + 3), P(cx + sw - 2, top + 6), P(cx + ww - 2, waist), P(cx + ww * 0.45, waist)], fill=KIT['shirt_d'])
    # mangas raglán: del cuello al sobaco
    for s in (-1, 1):
        rag = [(cx + s * 8, top), (cx + s * (sw - 6), top), (cx + s * (sw + 0.5), top + 8), (cx + s * (sw - 1), top + 15), (cx + s * (sw - 7), top + 13)]
        if KIT.get('sleeveless'):  # camiseta sin mangas: la sisa recortada y el hombro al aire
            continue
        d.polygon([P(*p) for p in rag], fill=KIT['sleeve'])
        d.line([P(cx + s * 8, top), P(cx + s * (sw - 7), top + 13), P(cx + s * (sw - 1), top + 15)], fill=OUT, width=int(1.1 * SS))
    # tela cruzada sobre un hombro hasta la cadera contraria (el himatión gris del Zeus)
    if KIT.get('sash'):
        k = 1 if not back else -1
        c, cd = KIT['sash'], tone(KIT['sash'], 0.8)
        band = [(cx + k * (sw - 9), top - 1), (cx + k * (sw + 1), top + 4), (cx + k * (sw - 2), top + 16), (cx - k * (ww - 4), waist + 4),
                (cx - k * (ww + 3), waist - 1), (cx - k * (ww + 1), waist - 9)]
        shape(d, blob_pts(band), c, 1.3)
        d.polygon([P(cx + k * (sw - 3), top + 10), P(cx + k * (sw - 2), top + 16), P(cx - k * (ww - 4), waist + 4), P(cx - k * (ww - 2), waist - 2)], fill=cd)
        d.line([P(cx + k * (sw - 6), top + 4), P(cx - k * (ww - 2), waist - 4)], fill=cd, width=int(1.0 * SS))
    # brazos colgando junto al torso, por delante de sus bordes
    for s in (-1, 1):
        sh = (cx + s * (sw - 1), top + 7)
        hand = (cx + s * (sw + t['at'] * 0.55), top + t['al'])
        capsule(d, sh, hand, t['at'] / 2, SKIN['mid'], SKIN['shade'] if s > 0 else None)
        if not KIT.get('sleeveless'):
            capsule(d, sh, V.lerp(sh, hand, 0.82 if KIT.get('longSleeve') else 0.28), t['at'] / 2 + 0.8, KIT['sleeve'], KIT['sleeve_d'] if s > 0 else None)
        r = t['at'] * 0.62
        d.ellipse([P(hand[0] - r - 1.4, hand[1] - r - 1.4), P(hand[0] + r + 1.4, hand[1] + r + 1.4)], fill=OUT)
        d.ellipse([P(hand[0] - r, hand[1] - r), P(hand[0] + r, hand[1] + r)], fill=KIT.get('hand', SKIN['mid']))
    if back:
        f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', int(20 * SS * t['sw'] / 54))
        d.text(P(cx, top + t['tl'] * 0.55), num, font=f, fill=KIT.get('num', KIT['sleeve']), anchor='mm', stroke_width=int(0.5 * SS), stroke_fill=tone(KIT.get('num', KIT['sleeve']), 0.75))
    elif KIT.get('suit'):  # camisa blanca en pico entre las solapas y la corbata negra
        d.polygon([P(cx - 9, top), P(cx + 9, top), P(cx, top + 22)], fill=KIT.get('collar', (242, 242, 242, 255)), outline=OUT)
        d.polygon([P(cx - 2, top + 1), P(cx + 2, top + 1), P(cx + 2.6, top + 17), P(cx, top + 20), P(cx - 2.6, top + 17)], fill=(20, 20, 24, 255))
        d.line([P(cx - 2.4, top + 14), P(cx + 2.4, top + 14)], fill=(200, 170, 60, 255), width=int(0.8 * SS))
    else:
        d.polygon([P(cx - 8, top), P(cx + 8, top), P(cx, top + 9)], fill=KIT.get('collar', KIT['sleeve']), outline=OUT)
    shape(d, rrect(cx - 6.5, 90, cx + 6.5, top + 3, 3), SKIN['shade'], 1.2)


def blob_pts(pts):
    import heads
    return heads.blob(pts, 6)


# ------------------------------------------------------------------ cuerpo de perfil (mirando a la derecha)

def body_side(d, t, step=0):
    """Cuerpo de perfil, mirando a la derecha; step 1 y 2: zancadas."""
    cx, top = 50, 100
    depth = max(30, t['sw'] * 0.6)
    waist = top + t['tl']
    short_bot = waist + t['sl']
    foot = short_bot + t['ll']
    lt = t['lt']
    stride = {0: 0, 1: 1, 2: -1}[step]
    for dx, dark in ((-stride * 11, True), (stride * 11, False)):
        hip = (cx, short_bot - 6)
        ft = (cx + dx, foot - 6)
        knee = V.lerp(hip, ft, 0.38)
        sk = SKIN['shade'] if dark else SKIN['mid']
        if KIT.get('longPants'):
            capsule(d, hip, ft, lt / 2 + 1.5, KIT['shorts_d'] if dark else KIT['shorts'])
        else:
            capsule(d, hip, ft, lt / 2, sk, None if dark else SKIN['shade'])
            capsule(d, knee, ft, lt / 2 + 0.5, KIT['sock_d'] if dark else KIT['sock'])
        shape(d, blob_pts([(ft[0] - lt / 2 - 1, foot - 7), (ft[0] + lt / 2 + 6, foot - 5), (ft[0] + lt / 2 + 8, foot + 1.5), (ft[0] - lt / 2 - 1, foot + 2)]),
              tone(KIT['boot'], 0.8) if dark else KIT['boot'], 1.4)
    # pantalón
    shape(d, [(cx - depth / 2, waist - 5), (cx + depth / 2, waist - 5), (cx + depth / 2 + 3, short_bot), (cx - depth / 2 - 3, short_bot)], KIT['shorts'])
    # torso
    shape(d, rrect(cx - depth / 2, top, cx + depth / 2, waist + 2, 8), KIT['shirt'])
    d.polygon([P(cx - depth / 2 + 2, top + 8), P(cx - depth / 2 + 6, top + 8), P(cx - depth / 2 + 6, waist), P(cx - depth / 2 + 2, waist)], fill=KIT['shirt_d'])
    if KIT.get('vstripes'):
        for k in (-1, 1):
            x = cx + k * depth / 4
            d.polygon([P(x - depth / 9, top + 2), P(x + depth / 9, top + 2), P(x + depth / 9, waist), P(x - depth / 9, waist)], fill=KIT['vstripes'])
    if KIT.get('sash'):  # la tela cruzada: de perfil, una franja que baja del hombro por el costado
        shape(d, blob_pts([(cx - depth / 2 + 1, top + 2), (cx + 4, top - 1), (cx + depth / 2 - 1, waist - 4), (cx + depth / 2 - 6, waist + 4),
                           (cx - 2, waist)]), KIT['sash'], 1.3)
        d.line([P(cx - 1, top + 6), P(cx + depth / 2 - 6, waist - 2)], fill=tone(KIT['sash'], 0.8), width=int(1.0 * SS))
    # brazo de este lado, balanceándose al correr
    sw_arm = -stride * 8
    sh = (cx, top + 6)
    hand = (cx + sw_arm, top + t['al'])
    capsule(d, sh, hand, t['at'] / 2, SKIN['mid'], SKIN['shade'])
    if not KIT.get('sleeveless'):
        capsule(d, sh, V.lerp(sh, hand, 0.82 if KIT.get('longSleeve') else 0.34), t['at'] / 2 + 1.6, KIT['sleeve'], KIT['sleeve_d'])
    if KIT.get('suit'):  # el pico blanco de la camisa asoma por delante
        d.polygon([P(cx + depth / 2 - 6, top + 1), P(cx + depth / 2 + 0.5, top + 1), P(cx + depth / 2 + 0.5, top + 14)], fill=KIT.get('collar', (242, 242, 242, 255)))
    r = t['at'] * 0.62
    d.ellipse([P(hand[0] - r - 1.4, hand[1] - r - 1.4), P(hand[0] + r + 1.4, hand[1] + r + 1.4)], fill=OUT)
    d.ellipse([P(hand[0] - r, hand[1] - r), P(hand[0] + r, hand[1] + r)], fill=KIT.get('hand', SKIN['mid']))
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
    shorts = hexc(colors['gkShorts'] if gk and colors.get('gkShorts') else colors['shorts'])
    sleeve = (hexc(colors['gkSleeve']) if colors.get('gkSleeve') else tone(shirt, 0.72)) if gk else hexc(colors['sleeve']) if colors.get('sleeve') else shorts
    k = dict(DEFAULT_KIT)
    k.update({'shirt': shirt, 'shirt_d': tone(shirt, 0.84), 'sleeve': sleeve, 'sleeve_d': tone(sleeve, 0.75),
              'shorts': shorts, 'shorts_d': tone(shorts, 0.72), 'stripe': hexc(colors['accent']) if colors.get('sleeve') else shorts})
    if colors.get('socks'):
        k['sock'] = hexc(colors['socks'])
        k['sock_d'] = tone(k['sock'], 0.78)
    if colors.get('sleeve'):  # mangas del color de la camiseta: cuello y dorsal con el color de los detalles
        k['collar'] = k['num'] = hexc(colors['accent'])
    if gk:
        k['hand'] = hexc(colors['gkGloves']) if colors.get('gkGloves') else (246, 246, 246, 255)
    if colors.get('vstripes') and not gk:
        k['vstripes'] = hexc(colors['vstripes'])
    if colors.get('zig') and not gk:
        k['zig'] = hexc(colors['zig'])
    for key in ('collar', 'num', 'stripe'):
        if colors.get(key) and not (gk and key == 'collar'):
            k[key] = hexc(colors[key])
    suit = bool(colors.get('suit')) and not gk
    k['longSleeve'] = suit or (gk and bool(colors.get('gkLongSleeve'))) or (not gk and bool(colors.get('longSleeve')))
    k['longPants'] = suit
    k['suit'] = suit
    if suit:
        k['boot'], k['boot_l'] = (24, 22, 26, 255), (70, 70, 80, 255)
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
    if char is not None and char.get('sash'):
        KIT['sash'] = hexc(char['sash'])
    if char is not None and char.get('sleeveless') and not KIT.get('longSleeve'):
        KIT['sleeveless'] = True
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
