"""Axel en vectores: cabeza de frente con curvas, sombreado de anime y contorno. Coordenadas en 0-100 (ancho)."""
import sys
from PIL import Image, ImageDraw

SS = 8  # escala de dibujo (supermuestreo)
OUT = (60, 24, 16, 255)
HAIR = {'mid': (246, 216, 176, 255), 'shade': (214, 160, 128, 255), 'deep': (160, 110, 82, 255), 'light': (255, 246, 226, 255)}
SKIN = {'mid': (238, 176, 124, 255), 'shade': (206, 138, 92, 255), 'light': (250, 202, 156, 255)}


OFF = 18


def P(x, y):
    return (x * SS, (y + OFF) * SS)


def quad(p0, c, p1, n=24):
    return [((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * c[0] + t * t * p1[0], (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * c[1] + t * t * p1[1]) for t in (i / n for i in range(n + 1))]


def spike(base_l, base_r, tip, bend=(0, 0)):
    """Pincho: dos curvas desde la base hasta la punta. `bend` desplaza los puntos de control (la curvatura)."""
    cl = ((base_l[0] + tip[0]) / 2 + bend[0] - 3, (base_l[1] + tip[1]) / 2 + bend[1])
    cr = ((base_r[0] + tip[0]) / 2 + bend[0] + 3, (base_r[1] + tip[1]) / 2 + bend[1])
    return quad(base_l, cl, tip) + quad(tip, cr, base_r)[1:]


def poly(d, pts, fill, outline=True, w=1.6):
    pts = [P(*p) for p in pts]
    if outline:
        d.line(pts + [pts[0]], fill=OUT, width=int(w * SS * 2), joint='curve')
    d.polygon(pts, fill=fill)


def lerp(a, b, t):
    return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)


def shaded_spike(d, base_l, base_r, tip, bend=(0, 0), light_left=True, w=1.6):
    s = spike(base_l, base_r, tip, bend)
    poly(d, s, HAIR['mid'], w=w)
    mid = lerp(base_l, base_r, 0.55 if light_left else 0.45)
    sh = spike(mid, base_r, tip, bend) if light_left else spike(base_l, mid, tip, bend)
    d.polygon([P(*p) for p in sh], fill=HAIR['shade'])
    # brillo: una franja clara dentro del lado iluminado, de la base a media altura
    a = lerp(base_l, base_r, 0.12 if light_left else 0.88)
    b = lerp(base_l, base_r, 0.38 if light_left else 0.62)
    t = lerp(lerp(a, b, 0.5), tip, 0.62)
    d.polygon([P(*p) for p in spike(lerp(a, tip, 0.12), lerp(b, tip, 0.12), t, (bend[0] * 0.6, bend[1] * 0.6))], fill=HAIR['light'])


SPIKES = [  # base izq., base der., punta, curvatura, luz por la izquierda
    ((20, 64), (30, 46), (6, 40), (-1, 5), True),        # sien izquierda, corta
    ((70, 46), (80, 64), (94, 40), (1, 5), False),       # sien derecha
    ((20, 56), (40, 36), (13, 12), (-4, 5), True),       # exterior izquierdo, más recto
    ((60, 36), (80, 56), (87, 12), (4, 5), False),       # exterior derecho
    ((28, 48), (52, 32), (29, -2), (-3, 5), True),       # interior izquierdo
    ((48, 32), (72, 48), (71, -2), (3, 5), False),       # interior derecho
    ((36, 44), (64, 44), (52, -10), (1, 2), True),       # central, el más alto
]
BANGS = [((20, 50), (38, 48), (26, 67), (-3, 0)), ((34, 48), (52, 46), (42, 64), (-2, 0)),
         ((48, 46), (66, 48), (58, 63), (2, 0)), ((62, 48), (80, 50), (74, 67), (3, 0)),
         ((16, 54), (26, 56), (20, 80), (-1, 0)), ((74, 56), (84, 54), (80, 80), (1, 0))]
CAP = quad((16, 66), (12, 30), (50, 28)) + quad((50, 28), (88, 30), (84, 66))[1:]


def head(d):
    W = 2.0
    shapes = [spike(bl, br, tp, bd) for bl, br, tp, bd, _ in SPIKES] + [CAP]
    bangs = [spike(bl, br, tp, bd) for bl, br, tp, bd in BANGS]
    face = quad((20, 54), (16, 98), (50, 103)) + quad((50, 103), (84, 98), (80, 54))[1:]
    # 1) contorno de toda la silueta (pelo + orejas + cara) y 2) relleno: un solo contorno exterior
    for cx in (19, 81):
        d.ellipse([P(cx - 6, 66), P(cx + 6, 82)], fill=OUT)
    for sh in shapes + bangs + [face]:
        pts = [P(*p) for p in sh]
        d.line(pts + [pts[0]], fill=OUT, width=int(W * SS * 2), joint='curve')
        d.polygon(pts, fill=OUT)
    for cx in (19, 81):
        d.ellipse([P(cx - 4.4, 67.6), P(cx + 4.4, 80.4)], fill=SKIN['mid'])
        d.ellipse([P(cx - 1.8, 70), P(cx + 1.8, 78)], fill=SKIN['shade'])
    d.polygon([P(*p) for p in CAP], fill=HAIR['shade'])
    # cada pincho de atrás hacia delante: relleno, sombra, brillo (sin contorno propio)
    for bl, br, tp, bd, ll in SPIKES:
        d.polygon([P(*p) for p in spike(bl, br, tp, bd)], fill=HAIR['mid'])
        mid = lerp(bl, br, 0.55 if ll else 0.45)
        sh = spike(mid, br, tp, bd) if ll else spike(bl, mid, tp, bd)
        d.polygon([P(*p) for p in sh], fill=HAIR['shade'])
        a = lerp(bl, br, 0.14 if ll else 0.86)
        b = lerp(bl, br, 0.36 if ll else 0.64)
        t = lerp(lerp(a, b, 0.5), tp, 0.6)
        d.polygon([P(*p) for p in spike(lerp(a, tp, 0.14), lerp(b, tp, 0.14), t, (bd[0] * 0.6, bd[1] * 0.6))], fill=HAIR['light'])
        # pliegue oscuro en la base del lado en sombra (separa este pincho del de al lado)
        side = br if ll else bl
        d.line([P(*p) for p in quad(lerp(side, tp, 0.05), lerp(lerp(side, tp, 0.4), (side[0] + bd[0], side[1]), 0.2), lerp(side, tp, 0.45))],
               fill=HAIR['deep'], width=int(1.1 * SS))
    # cara
    d.polygon([P(*p) for p in face], fill=SKIN['mid'])
    d.polygon([P(*p) for p in quad((20, 58), (50, 74), (80, 58)) + [(80, 54), (20, 54)]], fill=SKIN['shade'])
    d.polygon([P(*p) for p in quad((73, 64), (79, 92), (58, 100)) + quad((58, 100), (79, 93), (81, 62))[1:]], fill=SKIN['shade'])
    # flequillo y patillas encima de la cara
    for (bl, br, tp, bd), sh in zip(BANGS, bangs):
        d.polygon([P(*p) for p in sh], fill=HAIR['mid'])
        ll = tp[0] < 50
        mid = lerp(bl, br, 0.55 if ll else 0.45)
        sh2 = spike(mid, br, tp, bd) if ll else spike(bl, mid, tp, bd)
        d.polygon([P(*p) for p in sh2], fill=HAIR['shade'])
    # separaciones entre mechones del flequillo
    for x0, x1 in ((36, 37), (50, 50), (64, 63)):
        d.line([P(x0, 47), P(x1, 58)], fill=HAIR['deep'], width=int(1.0 * SS))
    # cejas
    for a, b in (((26, 70), (44, 74.5)), ((74, 70), (56, 74.5))):
        d.line([P(*a), P(*b)], fill=OUT, width=int(3.0 * SS))
    # ojos rasgados
    for cx, sgn in ((36, 1), (64, -1)):
        eye = [(cx - 8 * sgn, 79), (cx + 7 * sgn, 81.5), (cx + 5.5 * sgn, 88), (cx - 6 * sgn, 87)]
        d.polygon([P(*p) for p in eye], fill=(255, 255, 255, 255))
        d.ellipse([P(cx - 3.6 + sgn, 79.6), P(cx + 3.6 + sgn, 88.5)], fill=(48, 34, 50, 255))
        d.ellipse([P(cx - 1.2 + sgn * 2, 81.5), P(cx + 1.2 + sgn * 2, 84)], fill=(255, 255, 255, 255))
        d.line([P(*eye[0]), P(*eye[1])], fill=OUT, width=int(3.0 * SS))
        d.line([P(*eye[3]), P(*eye[2])], fill=SKIN['shade'], width=int(1.0 * SS))
    d.line([P(46, 95.5), P(54, 95.5)], fill=(130, 70, 50, 255), width=int(1.4 * SS))


if __name__ == '__main__':
    W, H = 100, 108
    im = Image.new('RGBA', (W * SS, (H + 20) * SS))
    d = ImageDraw.Draw(im)
    # todo desplazado 8 hacia abajo para que quepa la punta central
    head_img = Image.new('RGBA', im.size)
    hd = ImageDraw.Draw(head_img)
    head(hd)
    im = Image.new('RGBA', (W * SS, (H + 20) * SS))
    im.alpha_composite(head_img, (0, 0))
    big = im.resize((W * 4, (H + 20) * 4), Image.LANCZOS)
    ref = Image.open('../ref/axel_b0.png').convert('RGBA'); ref = ref.crop(ref.getbbox()); ref.thumbnail((440, 440))
    ds = Image.open('../ref/ds_R_IE_Gouenji_Shuuya_sprite.png').convert('RGBA').resize((256, 256), Image.NEAREST)
    sheet = Image.new('RGBA', (big.width + ref.width + ds.width + 60, max(big.height, ref.height)), (250, 248, 240, 255))
    sheet.alpha_composite(big, (0, 0)); sheet.alpha_composite(ref, (big.width + 20, 0)); sheet.alpha_composite(ds, (big.width + ref.width + 40, 0))
    sheet.save(sys.argv[1])
    im.save('vaxel_head.png')
