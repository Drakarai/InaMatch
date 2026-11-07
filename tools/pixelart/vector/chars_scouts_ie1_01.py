"""Ojeadores de IE1 (scouts-ie1), tanda 01: dibujados a partir de su retrato de Victory Road; claves 'scouts-ie1:<id>'.
Ninguno de esta tanda tiene modelo 3D en la enciclopedia: frente sacado del retrato y perfil y espalda deducidos del peinado.
Todos son chicos (ScoutCharacter, gender M en la wiki)."""
from chars import CHARS, L, OUTC, blob, ell, longhair, messy, outline, pal, rope, strand  # noqa: F401
from chars_bigwaves import rect_glasses
from chars_vr_keizen_arashiyama import cloud, fr
from chars_vr_meiran_gakuin import bangs
from chars_vr_nikogawa import WIDE, blush, brow_side, brows, crop, ring_glasses
from heads import quad  # noqa: F401

VIEWS = ('front', 'side', 'back')
WHITE = (248, 248, 248, 255)
BLACK = (30, 26, 30, 255)
BROWN_LINE = (130, 70, 50, 255)
SKIN = '#f4ba74'      # piel clara de los retratos de VR
TAN = '#cc9048'       # morena
DARK = '#a88460'      # muy morena
PALE = '#f8d0a0'      # muy clara
# caras: ancha y mofletuda (gorditos), alargada de adulto (mandíbula larga)
CHUBBY = blob([(12, 50), (50, 30), (88, 50), (94, 78), (88, 100), (68, 112), (50, 114), (32, 112), (12, 100), (6, 78)])
LONG = blob([(18, 50), (50, 30), (82, 50), (84, 80), (78, 100), (62, 112), (50, 114), (38, 112), (22, 100), (16, 80)])


def each(fn, **k):
    return {v: fn(v, **k) for v in VIEWS}


def cap(**k):
    """Pelo corto pegado (crop de Twinford) en las tres vistas."""
    return each(crop, **k)


def spiky(**k):
    """Pelo de pinchos revueltos (messy) en las tres vistas."""
    return each(messy, **k)


def F(*ls):
    return {'front': list(ls)}


def S(*ls):
    return {'side': list(ls)}


def B(*ls):
    return {'back': list(ls)}


def mk(cid, body, p, face, *parts):
    out = {'front': [], 'side': [], 'back': []}
    for part in parts:
        for v in VIEWS:
            out[v] += part.get(v, [])
    CHARS['scouts-ie1:' + cid] = dict(body=body, pal=p, face=face, **out)


def bowl(lo=66, fr_y=60, w=4, top=0, n=6, jag=3, nape=84, c='mid'):
    """Melena de tazón: casco redondo hasta lo a los lados y flequillo recto (o en picos con jag) hasta fr_y."""
    return {'front': [L(outline([(12 - w, lo + 4), (6 - w, 40), (16 - w * 0.4, 10 + top), (50, top), (84 + w * 0.4, 10 + top), (94 + w, 40), (88 + w, lo + 4),
                                 (80, 52), (20, 52)]), c),
                      L(outline([(62, top + 4), (86, 16 + top), (94 + w, 42), (88 + w, lo), (80, 44)]), 'shade', 'b', False),
                      bangs(fr_y, 16, 84, n, 24 + top, c, jag)],
            'side': [L(outline([(52, 68), (60, 60), (82, fr_y + 2), (92, fr_y - 2, 1), (94, 38), (86, 12 + top), (60, top - 2), (30, top + 2), (8, 20), (0 - w, 46),
                                (2, 70), (16, nape), (32, nape - 2), (38, 72), (44, 62)]), c),
                     L(outline([(1 - w, 46), (28, 48), (40, 62), (34, 74), (30, nape - 2), (16, nape), (4, 70)]), 'shade', 'b', False)],
            'back': [L(outline([(10 - w, lo + 10), (6 - w, 40), (16 - w * 0.4, 12 + top), (50, top + 2), (84 + w * 0.4, 12 + top), (94 + w, 40), (90 + w, lo + 10),
                                (66, nape), (50, nape + 2), (34, nape)]), c),
                     L(outline([(58, top + 6), (84, 16 + top), (94 + w, 44), (90 + w, lo + 8), (66, nape), (60, 50)]), 'shade', 'b', False)]}


def slick(top=4, side=56, nape=84, w=0, lines=True):
    """Pelo peinado hacia atrás: casquete corto con rayas de peine."""
    out = cap(top=top, side=side, nape=nape, w=w)
    if lines:
        out['front'] = out['front'] + [strand([(x, 40), (x + (x - 50) * 0.15, 10 + abs(x - 50) * 0.2)], 'deep', 'b', 1.0) for x in (32, 44, 56, 68)]
        out['side'] = out['side'] + [strand([(80, 30 + k * 6), (50, 14 + k * 8), (20, 30 + k * 10)], 'deep', 'b', 1.0) for k in range(3)]
        out['back'] = out['back'] + [strand([(x, 14), (x + (x - 50) * 0.1, 70)], 'deep', 'b', 1.0) for x in (34, 50, 66)]
    return out


def headband(y=46, h=10, c=(196, 50, 40, 255), tails=True):
    """Cinta en la frente atada por detrás."""
    cd = tuple(int(v * 0.78) for v in c[:3]) + (255,)
    out = {'front': [L(outline([(10, y + h / 2), (12, y - h / 2), (50, y - h / 2 - 3), (88, y - h / 2), (90, y + h / 2), (50, y + h / 2 - 3)]), c, 'f')],
           'side': [L(outline([(2, y + h / 2 - 2), (4, y - h / 2 - 2), (50, y - h / 2 - 4), (90, y - h / 2 + 2), (90, y + h / 2 + 2), (50, y + h / 2 - 4)]), c, 'f')],
           'back': [L(outline([(10, y + h / 2), (12, y - h / 2), (50, y - h / 2 - 3), (88, y - h / 2), (90, y + h / 2), (50, y + h / 2 - 3)]), c, 'f')]}
    if tails:
        out['side'].append(L(outline([(8, y), (-8, y + 12, 1), (-4, y + 2), (-12, y + 4, 1)]), cd, 'f'))
        out['back'].append(L(outline([(48, y), (40, y + 22, 1), (50, y + 4), (60, y + 22, 1), (52, y)]), cd, 'f'))
    return out


# ---------------------------------------------------------------------------------------------------- hoja 0

# Keira (Aaron Peacy, portero): señor de cara alargada; pelo corto verde musgo revuelto en puntas, cejas gruesas verdes,
# ojos entornados, nariz grande y media sonrisa
mk('aaron-peacy', 'normal', pal('#557060', SKIN, iris='#2a2a2a'),
   {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'nose': (50, 88, 3.4), 'face_front': LONG, 'hairline': (60, 46)},
   spiky(amp=9, n=10, seed=4, cy=40, ry=36, lo=58, nape=84),
   F(*brows(64, 'shade', 4.5, 14, 0.3, 13)), S(*brow_side(64, 'shade', 4.5)))

# Kumaya (Abe Seiler): moreno con el pelo azul grisáceo claro peinado hacia atrás, una cicatriz en estrella en la frente y
# ojos blancos de mirada malvada
mk('abe-seiler', 'normal', pal('#9cc2c2', TAN, iris='#f0f0f0', scar='#7a3c1c'),
   {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'face_front': LONG, 'hairline': (56, 30)},
   slick(top=2, side=54, nape=84),
   F(L(outline([(60, 44, 1), (64, 48), (70, 46, 1), (66, 52), (70, 58, 1), (63, 55), (58, 58, 1), (60, 51)]), 'scar', 'f', False)))

# Hayami (Ace Bragg): melena corta verde azulado que le enmarca la cara, con un mechón largo en punta que sale hacia su
# derecha; ojos afilados, bigotes de gato en las mejillas y sonrisa
mk('ace-bragg', 'normal', pal('#4e8478', SKIN, iris='#1e1e1e'),
   {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'hairline': False},
   {'front': [L(outline([(10, 92), (4, 50), (-26, 18, 1), (10, 22), (26, 6), (50, 0), (76, 6), (92, 26), (96, 60), (90, 92), (82, 84), (82, 56), (18, 56), (18, 84)])),
              L(outline([(60, 4), (86, 18), (96, 50), (90, 88), (84, 60)]), 'shade', 'b', False),
              fr([(14, 60), (16, 40), (28, 24), (50, 18), (72, 22), (86, 40), (86, 60), (78, 48), (70, 56, 1), (64, 42), (54, 50, 1), (46, 40), (34, 52, 1), (28, 42),
                  (20, 58)])],
    'side': [L(outline([(54, 66), (62, 54), (82, 50), (92, 34), (86, 10), (60, -2), (30, 2), (8, 20), (-2, 50), (0, 84), (14, 96), (30, 94), (40, 80), (46, 70)])),
             L(outline([(-1, 50), (26, 50), (40, 64), (36, 82), (26, 94), (12, 94), (2, 82)]), 'shade', 'b', False),
             L(outline([(60, 10), (40, 4), (10, -4, 1), (36, 14)]), 'mid')],
    'back': [L(outline([(8, 92), (4, 44), (16, 14), (50, 0), (84, 14), (96, 44), (92, 92), (70, 98), (50, 100), (30, 98)])),
             L(outline([(58, 6), (84, 16), (96, 46), (92, 90), (64, 96)]), 'shade', 'b', False),
             L(outline([(20, 18), (-24, 16, 1), (10, 30)]), 'mid')]},
   F(L([(26, 84), (32, 86)], OUTC, 'f', False, False, 1.0), L([(68, 86), (74, 84)], OUTC, 'f', False, False, 1.0)))

# Kobore (Ace Breaker): moreno con el pelo corto gris azulado a los lados y un copete crema enroscado encima; gafas verdes
# rectangulares de cristal claro y una sonrisa enorme de dientes
mk('ace-breaker', 'normal', pal('#7a8aa4', TAN, iris='#2a2a2a', top='#ece4bc', top_d='#c4b890', lens='#e8e8d8'),
   {'eyes': 'none', 'brows': False, 'mouth': 'grin', 'mouth_y': 96, 'face_front': LONG, 'hairline': (60, 40)},
   cap(top=8, side=60, nape=84),
   {'front': [L(outline([(28, 40), (24, 18), (40, 0), (60, -2), (74, 12), (72, 36), (58, 40)]), 'top', 'f'),
              L(outline([(46, 12), (58, 6), (64, 16), (54, 24), (48, 20)]), 'top_d', 'f', False),
              L([(18, 70), (82, 70), (82, 80), (18, 80)], 'lens', 'f', False)] + rect_glasses('front', 75, (60, 170, 60, 255)),
    'side': [L(outline([(40, 40), (36, 14), (54, -2), (76, 4), (86, 20), (80, 36), (60, 42)]), 'top', 'f')] + rect_glasses('side', 75, (60, 170, 60, 255)),
    'back': [L(outline([(28, 40), (26, 14), (42, -2), (60, -2), (74, 14), (72, 40), (50, 46)]), 'top', 'f')]})

# Orio (Ace Fettick, portero): pelo morado grisáceo con raya al lado, liso hasta la mandíbula; ojos afilados y sonrisa
mk('ace-fettick', 'normal', pal('#786c80', SKIN, iris='#1e1e1e'),
   {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'hairline': False},
   {'front': [L(outline([(10, 84), (4, 46), (14, 16), (38, 2), (66, 2), (88, 18), (96, 50), (92, 84), (84, 78), (84, 56), (18, 56), (16, 78)])),
              L(outline([(58, 4), (86, 18), (96, 50), (92, 82), (84, 56)]), 'shade', 'b', False),
              fr([(16, 66), (14, 40), (26, 20), (44, 10), (70, 14), (86, 34), (86, 58), (74, 40), (60, 32), (44, 34), (30, 44), (22, 60)])],
    'side': [L(outline([(54, 64), (62, 54), (80, 48), (92, 32), (86, 10), (60, -2), (30, 2), (8, 22), (0, 52), (4, 80), (16, 90), (32, 88), (40, 74), (46, 66)])),
             L(outline([(1, 52), (28, 52), (40, 66), (34, 80), (16, 88), (4, 78)]), 'shade', 'b', False)],
    'back': [L(outline([(8, 86), (4, 44), (16, 14), (50, 0), (84, 14), (96, 44), (92, 86), (66, 92), (50, 94), (34, 92)])),
             L(outline([(58, 6), (84, 16), (96, 46), (92, 84), (64, 90)]), 'shade', 'b', False)]})

# Hikage (Ace Irvin): melena morada grisácea en casco que le tapa el ojo izquierdo; el otro ojo amarillo, piel muy clara
mk('ace-irvin', 'normal', pal('#786c84', PALE, iris='#d8b020'),
   {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': False},
   bowl(lo=74, fr_y=62, w=4, top=-2, n=5, jag=4),
   F(fr([(40, 28), (66, 22), (88, 36), (94, 60), (90, 86), (80, 92, 1), (76, 74), (64, 88, 1), (56, 70), (46, 64, 1), (48, 46)]),
     strand([(56, 30), (64, 60), (70, 84)], 'shade', 'f', 1.2)))

# Sakon (Ace Server, portero): pinchos verde azulado de punta hacia arriba y a los lados, con un mechón rosado en medio de
# la frente y dos trenzas finas a rayas que le cuelgan junto a la cara; ojos afilados
mk('ace-server', 'normal', pal('#5a8e8e', SKIN, iris='#3a2a2a', pink='#c49aa4', braid='#e0d0b4', braid_d='#8a6a4a'),
   {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'hairline': (58, 46)},
   spiky(amp=16, n=11, seed=7, cy=38, ry=36, lo=60, nape=88, sweep=0.2),
   {'front': [fr([(44, 22), (52, 16), (56, 30), (50, 66, 1), (46, 40)], 'pink'),
              L(rope((16, 68), (12, 86), (14, 112), 5, 10), 'braid', 'b'), L(rope((84, 68), (88, 86), (86, 112), 5, 10), 'braid', 'b')],
    'side': [L(rope((44, 66), (42, 86), (44, 112), 5, 10), 'braid', 'b')],
    'back': [L(rope((18, 70), (14, 90), (16, 110), 5, 10), 'braid', 'b'), L(rope((82, 70), (86, 90), (84, 110), 5, 10), 'braid', 'b')]},
   F(*[L([(x0, y), (x0 + 5, y)], 'braid_d', 'f', False, False, 1.2) for x0 in (11, 82) for y in (84, 92, 100)]))

# Shinjiro (Adam Hesive): pelo verde clarito en casco de tazón, orejas de punta como un elfo, ojos redondos enormes y la
# boca abierta de susto
mk('adam-hesive', 'normal', pal('#cccc92', PALE, iris='#1e1e1e', lip='#b05a5a'),
   {'eyes': 'round', 'brows': False, 'mouth': 'none', 'hairline': False, 'ears': False, 'eye_sep': 15},
   bowl(lo=60, fr_y=56, w=2, top=0, n=6, jag=3, nape=80),
   {'front': [L(outline([(14, 66), (-4, 52, 1), (16, 82)]), (248, 208, 160, 255), 'b'), L(outline([(86, 66), (104, 52, 1), (84, 82)]), (248, 208, 160, 255), 'b'),
              L(ell(50, 94, 6, 4.5), 'lip', 'f', ln=True), L(ell(50, 95, 3, 1.6), (90, 40, 40, 255), 'f', False)],
    'side': [L(outline([(42, 64), (30, 50, 1), (46, 80)]), (248, 208, 160, 255), 'f', ln=True), L(ell(85, 93, 3, 4), 'lip', 'f', ln=True)],
    'back': [L(outline([(14, 66), (-4, 52, 1), (16, 82)]), (248, 208, 160, 255), 'b'), L(outline([(86, 66), (104, 52, 1), (84, 82)]), (248, 208, 160, 255), 'b')]})

# ---------------------------------------------------------------------------------------------------- hoja 1

# Kirifuri (Adam Icklock, portero): moreno; pelo castaño grisáceo en pinchos con un pico que le baja a la frente, cejas
# negras gruesas de enfado y dos rayas amarillas pintadas bajo los ojos
mk('adam-icklock', 'normal', pal('#9a7a70', TAN, iris='#6a3a1a', paint='#e0b020'),
   {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': [(14, 58), (24, 46), (40, 44), (50, 56), (60, 44), (76, 46), (86, 58)]},
   spiky(amp=10, n=10, seed=11, cy=42, ry=34, rx=44, lo=58, nape=86),
   F(*brows(63, BLACK, 4.5, 14, 0.8, 14),
     L([(30, 82), (32, 100)], 'paint', 'f', False, False, 3.0), L([(38, 82), (40, 98)], 'paint', 'f', False, False, 3.0),
     L([(70, 82), (68, 100)], 'paint', 'f', False, False, 3.0), L([(62, 82), (60, 98)], 'paint', 'f', False, False, 3.0)),
   S(*brow_side(63, BLACK, 4.5, 0.8)))

# Gojo (Adam Nesiac): señor de cara larga con un tupé verde azulado alto peinado hacia atrás, cejas verdes arqueadas y la
# boca abierta en una O
mk('adam-nesiac', 'normal', pal('#5a9488', SKIN, iris='#1e1e1e', lip='#7a3a24'),
   {'eyes': 'dot', 'brows': False, 'mouth': 'none', 'face_front': LONG, 'nose': (50, 88, 3.6), 'hairline': (56, 36), 'eye_y': 76},
   slick(top=-6, side=56, nape=84),
   {'front': [L(outline([(26, 34), (30, 8), (50, -12), (72, -4), (76, 20), (70, 36)]), 'mid', 'b')],
    'side': [L(outline([(50, 20), (66, -10), (88, -2), (92, 22), (82, 36)]), 'mid', 'b')],
    'back': [L(outline([(28, 30), (32, 6), (50, -10), (70, -2), (72, 24)]), 'mid', 'b')]},
   F(*brows(64, 'mid', 3.2, 14, -0.6, 13), L(ell(50, 101, 6, 5), 'lip', 'f', ln=True)), S(*brow_side(64, 'mid', 3.2)))

# Shiba (Ade Posting): pelo verde azulado en casco con flequillo de mechones hasta las cejas y un pelo de antena; ojos
# afilados azul clarito
mk('ade-posting', 'normal', pal('#4e8478', SKIN, iris='#7ab8c8'),
   {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'hairline': False},
   bowl(lo=62, fr_y=62, w=6, top=2, n=6, jag=8),
   F(L(quad((50, 4), (44, -8), (54, -14)), 'mid', 'b', False, False, 2.4)), S(L(quad((60, -2), (56, -12), (66, -16)), 'mid', 'b', False, False, 2.4)))

# Kakeru (Aessop Fabel): pinchos altos naranja rojizo hacia arriba con un mechón largo que le cae por delante de la cara
# hasta la mejilla; ojos verdes
mk('aessop-fabel', 'normal', pal('#b04210', SKIN, iris='#7ab840'),
   {'eyes': 'normal', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 93, 'hairline': (58, 44)},
   {'front': [L(outline([(16, 62), (10, 40), (4, 8, 1), (20, 18), (16, -16, 1), (34, 4), (46, -30, 1), (54, 0), (70, -22, 1), (70, 6), (90, -6, 1), (86, 20), (96, 30, 1),
                         (88, 42), (86, 62), (80, 50), (20, 50)])),
              L(outline([(58, -2), (70, -18), (72, 8), (88, -2), (84, 22), (90, 40), (84, 56), (74, 30)]), 'shade', 'b', False),
              fr([(40, 26), (56, 22), (66, 40), (70, 66), (68, 90, 1), (62, 64), (54, 46), (44, 40)])],
    'side': [L(outline([(56, 52), (66, 44), (84, 40), (98, 28, 1), (86, 22), (96, 0, 1), (76, 6), (78, -24, 1), (60, 0), (48, -30, 1), (40, 4), (20, -10, 1), (20, 12),
                        (6, 24), (2, 46), (14, 70), (30, 72), (44, 58)])),
             L(outline([(4, 40), (30, 46), (40, 58), (28, 70), (14, 68)]), 'shade', 'b', False),
             fr([(80, 30), (92, 40), (96, 66), (92, 86, 1), (86, 60), (80, 44)])],
    'back': [L(outline([(16, 74), (10, 40), (4, 8, 1), (20, 18), (18, -14, 1), (34, 4), (46, -28, 1), (54, 0), (70, -20, 1), (70, 6), (90, -4, 1), (86, 20), (94, 32, 1),
                        (88, 44), (86, 74), (50, 82)])),
             L(outline([(58, 0), (86, 16), (90, 44), (86, 72), (62, 80)]), 'shade', 'b', False)]})

# Iseki (Aidan Model): gordito de cara redonda, pelo verde azulado en pinchos hacia arriba sobre una cinta roja gruesa,
# nariz naranja redonda, ojos afilados y boca ondulada
mk('aidan-model', 'corpulento', pal('#4e8478', SKIN, iris='#1e1e1e', nose='#e07a30'),
   {'eyes': 'sharp', 'brows': False, 'mouth': 'none', 'face_front': CHUBBY, 'nose': (50, 88, 5), 'hairline': (54, 46), 'ear_out': 6},
   {'front': [L(outline([(16, 52), (14, 30), (16, 4, 1), (28, 14), (32, -8, 1), (44, 8), (52, -14, 1), (60, 6), (72, -8, 1), (74, 12), (86, 4, 1), (86, 30), (84, 52)])),
              L(outline([(60, 2), (72, -6), (74, 14), (86, 6), (86, 40), (74, 30)]), 'shade', 'b', False)],
    'side': [L(outline([(70, 46), (88, 30), (92, 8, 1), (78, 14), (78, -8, 1), (62, 6), (52, -12, 1), (40, 6), (22, -4, 1), (22, 14), (6, 30), (4, 48), (20, 52)])),
             L(outline([(4, 40), (40, 40), (40, 52), (6, 52)]), 'shade', 'b', False)],
    'back': [L(outline([(14, 66), (12, 30), (16, 4, 1), (28, 14), (32, -8, 1), (44, 8), (52, -14, 1), (60, 6), (72, -8, 1), (74, 12), (86, 4, 1), (88, 30), (86, 66),
                        (50, 72)])),
             L(outline([(58, 4), (86, 8), (88, 64), (60, 70)]), 'shade', 'b', False)]},
   headband(44, 12, (190, 44, 30, 255)),
   F(L(quad((40, 98), (45, 95), (50, 99)) + quad((50, 99), (55, 95), (60, 98))[1:], OUTC, 'f', False, False, 1.4)))

# Kanpatsu (Ainsley Burns): grandullón de cara ancha; pelo rosa salmón en casco con raya al lado y flequillo hasta las
# cejas; ojos pequeños de enfado con la piel rosada alrededor
mk('ainsley-burns', 'corpulento', pal('#e4a08a', PALE, iris='#1e1e1e', blushc='#f0a8a0'),
   {'eyes': 'dot', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'face_front': CHUBBY, 'hairline': False, 'eye_y': 76, 'ear_out': 6},
   bowl(lo=60, fr_y=58, w=6, top=2, n=4, jag=6, nape=78),
   F(L(outline([(24, 70), (44, 74), (40, 82), (28, 80)]), 'blushc', 'f', False), L(outline([(76, 70), (56, 74), (60, 82), (72, 80)]), 'blushc', 'f', False),
     L([(24, 68), (44, 76)], OUTC, 'f', False, False, 2.2), L([(76, 68), (56, 76)], OUTC, 'f', False, False, 2.2)))

# Mitsuoka (Al Askan): cara arrugada como de perro con la nariz ancha; pelo verde azulado con dos mechones largos que le
# caen como orejas de perro por los lados y una franja verde pintada sobre los ojos
mk('al-askan', 'normal', pal('#5a9090', SKIN, iris='#1e1e1e', band='#2a7a4a'),
   {'eyes': 'closed', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'face_front': LONG, 'nose': (50, 90, 5), 'hairline': (56, 44)},
   cap(top=4, side=54, nape=80),
   {'front': [L(outline([(26, 20), (10, 30), (-6, 60), (-4, 92), (8, 96), (16, 74), (22, 50)]), 'mid', 'f'),
              L(outline([(74, 20), (90, 30), (106, 60), (104, 92), (92, 96), (84, 74), (78, 50)]), 'mid', 'f'),
              L(outline([(40, 2), (50, -8, 1), (56, 4), (68, -4, 1), (64, 10)]), 'mid', 'b'),
              L([(22, 70), (44, 72), (44, 80), (22, 78)], 'band', 'f', False), L([(78, 70), (56, 72), (56, 80), (78, 78)], 'band', 'f', False)],
    'side': [L(outline([(40, 26), (20, 36), (14, 70), (20, 100), (32, 98), (40, 70), (46, 46)]), 'mid', 'f'), L([(74, 70), (88, 72), (88, 80), (74, 78)], 'band', 'f', False)],
    'back': [L(outline([(24, 26), (8, 36), (-6, 64), (-4, 94), (8, 96), (18, 70)]), 'mid', 'f'),
             L(outline([(76, 26), (92, 36), (106, 64), (104, 94), (92, 96), (82, 70)]), 'mid', 'f')]})

# Hosokawa (Al Chemmy): piel muy pálida con una grieta de cicatriz que le baja por media cara; pelo azul marino oscuro
# corto con raya al lado, ojos blancos malvados y sonrisa torcida
mk('al-chemmy', 'normal', pal('#2e4660', '#e4ccb0', iris='#f0f0f0', crack='#a08870'),
   {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'face_front': LONG, 'hairline': (58, 40)},
   cap(top=2, side=60, nape=84, w=2),
   F(fr([(16, 56), (18, 36), (32, 22), (56, 18), (76, 26), (86, 40), (84, 52), (70, 40), (50, 38), (34, 44)]),
     L([(62, 40), (60, 52), (66, 60), (62, 72), (68, 84), (64, 96), (68, 106)], 'crack', 'f', False, False, 2.4)))

# ---------------------------------------------------------------------------------------------------- hoja 2

# Saijo (Al Istatin): moreno; pelo azul pizarra revuelto de mechones sueltos, ojos afilados, nariz grande y boca apretada
mk('al-istatin', 'normal', pal('#46546a', '#c09054', iris='#1e1e1e'),
   {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'face_front': LONG, 'nose': (50, 86, 3.4), 'hairline': [(16, 60), (26, 48), (40, 54), (50, 46), (60, 54), (74, 48), (84, 60)]},
   spiky(amp=11, n=11, seed=21, cy=40, ry=36, lo=60, nape=88, sweep=0.3))

# Kawara (Al Mannack): cabeza rapada con una cresta fina verde en punta de la frente a la nuca y dos rayas afeitadas a
# los lados; ojos afilados de enfado
mk('al-mannack', 'normal', pal('#5a9a3c', SKIN, iris='#1e1e1e'),
   {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'face_front': LONG, 'hairline': False},
   {'front': [L(outline([(44, 40), (42, 20), (48, 0), (50, -14, 1), (54, 0), (58, 20), (56, 40)])),
              L([(24, 22), (28, 46)], 'mid', 'f', False, False, 2.4), L([(76, 22), (72, 46)], 'mid', 'f', False, False, 2.4)],
    'side': [L(outline([(80, 30), (76, 14), (62, 2), (50, -10, 1), (46, 0), (28, 6), (14, 20), (8, 36), (12, 38), (18, 24), (32, 12), (48, 6), (62, 8), (72, 18),
                        (76, 32)])),
             L([(30, 30), (24, 56)], 'mid', 'f', False, False, 2.4)],
    'back': [L(outline([(44, 80), (44, 20), (48, 2), (50, -10, 1), (52, 2), (56, 20), (56, 80)]))]})

# Ishiba (Al Plates): gordito moreno; pelo verde hierba revuelto con flequillo de mechones, ojos de sueño, nariz marrón
# redonda y boca ancha
mk('al-plates', 'corpulento', pal('#6a9a3e', TAN, iris='#1e1e1e', nose='#8a5030'),
   {'eyes': 'round', 'brows': False, 'mouth': 'none', 'face_front': CHUBBY, 'nose': (50, 88, 5), 'hairline': False, 'ear_out': 6, 'eye_y': 76},
   spiky(amp=9, n=10, seed=31, cy=40, ry=38, lo=60, nape=86),
   F(fr([(14, 64), (14, 40), (30, 22), (50, 18), (72, 22), (88, 40), (86, 64), (78, 50), (70, 62, 1), (62, 46), (52, 58, 1), (44, 44), (34, 60, 1), (26, 46), (20, 62)]),
     L([(28, 70), (44, 72)], OUTC, 'f', False, False, 2.0), L([(72, 70), (56, 72)], OUTC, 'f', False, False, 2.0),
     L(quad((36, 100), (50, 103), (64, 99)), OUTC, 'f', False, False, 1.4)))

# Tenbin (Al Reddie): moreno; melena de pinchos blanco verdoso que le cae por los lados, con dos trenzas finas que
# acaban en cuentas rojas junto a la cara; ojos redondos y sonrisa
mk('al-reddie', 'normal', pal('#d4f0dc', TAN, iris='#1e1e1e', bead='#d03a2a', braid='#d4f0dc'),
   {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'face_front': LONG, 'hairline': [(16, 62), (24, 46), (40, 48), (50, 40), (60, 48), (76, 46), (84, 62)]},
   spiky(amp=14, n=12, seed=41, cy=44, ry=40, rx=48, lo=74, nape=92),
   {'front': [L(rope((16, 70), (14, 88), (16, 104), 4, 10), 'braid', 'b'), L(rope((84, 70), (86, 88), (84, 104), 4, 10), 'braid', 'b'),
              L(ell(15, 90, 3, 3), 'bead', 'f', ln=True), L(ell(85, 90, 3, 3), 'bead', 'f', ln=True)],
    'side': [L(rope((44, 68), (42, 88), (44, 104), 4, 10), 'braid', 'b'), L(ell(43, 90, 3, 3), 'bead', 'f', ln=True)],
    'back': [L(rope((16, 76), (14, 92), (16, 106), 4, 10), 'braid', 'b'), L(rope((84, 76), (86, 92), (84, 106), 4, 10), 'braid', 'b')]})

# Ijiwaru (Al Urgy): pelo morado oscuro tupido con flequillo de mechones y puntas hacia fuera en la nuca; ojos afilados
# grandes de enfado, nariz marrón y boca de morros
mk('al-urgy', 'normal', pal('#4e4462', SKIN, iris='#1e1e1e', nose='#9a5a3a'),
   {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'face_front': CHUBBY, 'nose': (50, 88, 3.4), 'hairline': False},
   {'front': [L(outline([(10, 80), (-2, 74, 1), (6, 60), (4, 34), (18, 10), (50, 0), (82, 10), (96, 34), (94, 60), (102, 74, 1), (90, 80), (84, 56), (16, 56)])),
              L(outline([(60, 4), (84, 14), (96, 40), (92, 72), (84, 56)]), 'shade', 'b', False),
              fr([(14, 60), (14, 36), (30, 18), (50, 14), (70, 18), (86, 36), (86, 60), (76, 46), (68, 56, 1), (62, 42), (52, 54, 1), (44, 42), (34, 56, 1), (28, 44),
                  (20, 58)])],
    'side': [L(outline([(54, 62), (62, 52), (80, 48), (92, 32), (86, 8), (60, -4), (30, 0), (8, 20), (0, 50), (-6, 72, 1), (10, 80), (14, 92, 1), (26, 84), (38, 76),
                        (46, 66)])),
             L(outline([(1, 50), (28, 50), (40, 64), (26, 84), (10, 80)]), 'shade', 'b', False)],
    'back': [L(outline([(10, 82), (-2, 76, 1), (6, 60), (4, 34), (18, 10), (50, 0), (82, 10), (96, 34), (94, 60), (102, 76, 1), (90, 82), (76, 90, 1), (64, 84),
                        (50, 92, 1), (36, 84), (24, 90, 1)])),
             L(outline([(58, 4), (84, 14), (96, 40), (92, 78), (64, 86)]), 'shade', 'b', False)]})

# Mitsuya (Alan Carte): moreno de mandíbula enorme; pelo verde corto con raya al lado y mechones en punta sobre las
# orejas, cejas verdes de enfado y la boca abierta gritando
mk('alan-carte', 'corpulento', pal('#6a9a3e', TAN, iris='#1e1e1e', mouthc='#5a2a1e'),
   {'eyes': 'sharp', 'brows': False, 'mouth': 'none', 'face_front': CHUBBY, 'nose': (50, 86, 3.6), 'hairline': (56, 40), 'eye_y': 74},
   cap(top=4, side=54, nape=84, w=2),
   {'front': [L(outline([(16, 54), (4, 62, 1), (8, 72), (0, 82, 1), (14, 80)]), 'mid', 'b'), L(outline([(84, 54), (96, 62, 1), (92, 72), (100, 82, 1), (86, 80)]), 'mid', 'b'),
              L(outline([(38, 94), (62, 94), (60, 106), (40, 106)]), 'mouthc', 'f', ln=True), L([(40, 95), (60, 95), (59, 98), (41, 98)], WHITE, 'f', False)],
    'side': [L(outline([(30, 60), (20, 76, 1), (34, 72), (30, 86, 1), (40, 74)]), 'mid', 'b')]},
   F(*brows(62, 'mid', 4.0, 14, 0.8, 13)), S(*brow_side(62, 'mid', 4.0, 0.8)))

# Yaji (Alan Mode): pelo rosa rojizo recogido en un moño alto con dos gomas verde azulado y una coleta que sale por
# arriba; ojos grandes y sonrisa
mk('alan-mode', 'normal', pal('#c25a5a', SKIN, iris='#1e1e1e', tie='#5a9a9a'),
   {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'hairline': False},
   {'front': [L(outline([(14, 66), (10, 40), (22, 18), (50, 10), (78, 18), (90, 40), (86, 66), (80, 54), (20, 54)])),
              L(outline([(60, 12), (82, 20), (90, 42), (86, 62), (78, 40)]), 'shade', 'b', False),
              fr([(14, 62), (16, 40), (30, 24), (50, 20), (70, 24), (84, 40), (86, 62), (76, 46), (66, 56, 1), (60, 40), (50, 54, 1), (42, 40), (32, 56, 1), (24, 46)]),
              L(cloud(50, 6, 16, 12, 6), 'mid', 'b'), L(ell(50, -6, 8, 4), 'tie', 'b', ln=True),
              L(outline([(44, -8), (36, -30, 1), (48, -20), (50, -36, 1), (54, -20), (66, -28, 1), (58, -8)]), 'mid', 'b')],
    'side': [L(outline([(54, 62), (62, 52), (80, 46), (90, 30), (84, 12), (60, 2), (30, 6), (10, 22), (4, 50), (12, 72), (28, 76), (40, 70), (46, 64)])),
             L(cloud(40, 0, 14, 12, 6), 'mid', 'b'), L(ell(42, -10, 7, 4), 'tie', 'b', ln=True),
             L(outline([(36, -10), (26, -32, 1), (40, -20), (46, -36, 1), (50, -12)]), 'mid', 'b')],
    'back': [L(outline([(14, 74), (10, 40), (22, 16), (50, 8), (78, 16), (90, 40), (86, 74), (50, 80)])),
             L(outline([(58, 10), (82, 18), (90, 42), (86, 72), (60, 78)]), 'shade', 'b', False),
             L(cloud(50, 6, 16, 12, 6), 'mid', 'b'), L(ell(50, 18, 9, 4), 'tie', 'b', ln=True),
             L(outline([(44, -6), (36, -28, 1), (48, -18), (50, -34, 1), (54, -18), (66, -26, 1), (58, -6)]), 'mid', 'b')]})

# Nakaya (Albert Wister, portero): muy moreno; pelo rubio dorado en mechones de punta que caen hacia su izquierda sobre la
# frente; cejas rubias de enfado, ojos pequeños y boca abierta de dientes
mk('albert-wister', 'normal', pal('#dcb460', '#c06c30', iris='#1e1e1e'),
   {'eyes': 'dot', 'brows': False, 'mouth': 'grin', 'mouth_y': 96, 'face_front': LONG, 'hairline': False},
   spiky(amp=12, n=10, seed=51, cy=40, ry=36, lo=60, nape=88, sweep=0.6),
   F(fr([(12, 62), (14, 40), (30, 22), (52, 18), (74, 24), (90, 44), (96, 60, 1), (82, 52), (76, 66, 1), (68, 48), (56, 60, 1), (50, 44), (36, 56, 1), (32, 42), (20, 60)]),
     *brows(66, 'mid', 3.4, 14, 0.8, 12)), S(*brow_side(66, 'mid', 3.4, 0.8)))

# ---------------------------------------------------------------------------------------------------- hoja 3

# Mukadeya (Alec Dote, portero): gordito con pelo castaño en tazón y un pelito de antena; gafas de sol redondas azul oscuro
# con montura amarilla y boca de pena
mk('alec-dote', 'corpulento', pal('#5a4a24', SKIN, iris='#1e1e1e', lens='#30485e', frame='#e0c040', mouthc='#7a3a24'),
   {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': CHUBBY, 'hairline': False, 'ear_out': 6},
   bowl(lo=60, fr_y=54, w=4, top=0, n=5, jag=0, nape=78),
   {'front': [L(ell(34, 74, 10, 9), 'lens', 'f', ln=True), L(ell(66, 74, 10, 9), 'lens', 'f', ln=True),
              L(ell(34, 74, 10.5, 9.5) + [ell(34, 74, 10.5, 9.5)[0]], 'frame', 'f', False, False, 1.6),
              L(ell(66, 74, 10.5, 9.5) + [ell(66, 74, 10.5, 9.5)[0]], 'frame', 'f', False, False, 1.6),
              L([(44, 73), (56, 73)], 'frame', 'f', False, False, 1.6), L([(24, 72), (12, 70)], 'frame', 'f', False, False, 1.6), L([(76, 72), (88, 70)], 'frame', 'f', False, False, 1.6),
              L(outline([(40, 100), (50, 92), (60, 100), (50, 98)]), 'mouthc', 'f', ln=True),
              L(quad((50, 2), (46, -8), (54, -12)), 'mid', 'b', False, False, 2.2)],
    'side': [L(ell(82, 74, 6, 9), 'lens', 'f', ln=True), L([(76, 72), (48, 68)], 'frame', 'f', False, False, 1.6)]})

# Mutsuyama (Alec Smart, portero): de mandíbula larga y piel clara; pelo castaño oscuro en pinchos hacia los lados con
# mechones sobre la frente, ojos afilados verdes y sonrisa de listo
mk('alec-smart', 'normal', pal('#564a1e', PALE, iris='#5a8a6a'),
   {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'face_front': LONG, 'nose': (50, 86, 3), 'hairline': [(16, 60), (24, 46), (36, 56), (44, 44), (56, 56), (64, 44), (76, 48), (84, 60)]},
   spiky(amp=13, n=11, seed=61, cy=40, ry=36, rx=48, lo=60, nape=86))

# Arima (Alf Groundsy): pelo verde oliva de pinchos revueltos con mechones sobre la frente; cejas negras gruesas de enfado,
# ojos azules y boca apretada
mk('alf-groundsy-groundsman', 'normal', pal('#8a8a34', SKIN, iris='#4a8ab0'),
   {'eyes': 'normal', 'brows': False, 'mouth': 'frown', 'mouth_y': 94, 'hairline': [(16, 60), (24, 48), (34, 58), (42, 46), (52, 60), (60, 46), (74, 50), (84, 60)]},
   spiky(amp=12, n=11, seed=71, cy=40, ry=36, lo=62, nape=88, sweep=-0.3),
   F(*brows(64, BLACK, 4.2, 14, 0.9, 13)), S(*brow_side(64, BLACK, 4.2, 0.9)))

# Kousaka (Alfie Fine, portero): pelo azul marino casi negro en pinchos largos que caen en mechones hasta los hombros;
# ojos grandes morados y ceño fruncido
mk('alfie-fine', 'normal', pal('#2e2440', '#eca460', iris='#8a7ab0'),
   {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'hairline': False},
   spiky(amp=16, n=12, seed=81, cy=42, ry=40, rx=48, lo=70, nape=100, sweep=0.3),
   {'front': [L(outline([(16, 60), (4, 96, 1), (12, 82), (14, 106, 1), (22, 80)]), 'mid', 'b'), L(outline([(84, 60), (96, 96, 1), (88, 82), (86, 106, 1), (78, 80)]), 'mid', 'b'),
              fr([(14, 62), (16, 40), (30, 24), (52, 18), (72, 24), (86, 40), (86, 62), (78, 48), (70, 66, 1), (64, 46), (52, 62, 1), (46, 44), (34, 60, 1), (28, 44), (20, 60)])]})

# Okoshi (Alfonse Way): moreno; pelo malva grisáceo en tazón con el flequillo recto y la nuca rapada; ojos afilados
mk('alfonse-way', 'normal', pal('#9a7a74', '#c09054', iris='#1e1e1e'),
   {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'face_front': LONG, 'hairline': False},
   bowl(lo=60, fr_y=60, w=4, top=2, n=6, jag=0, nape=74),
   F(*[strand([(x, 20), (x, 58)], 'deep', 'f', 1.0) for x in (30, 42, 54, 66)]))

# Tenkuu (Alistair Horizon): gordito moreno con un gorro de lana rosa con franja crema, del que asoman puntas de pelo rosa
# a los lados; cejas rosas, ojos pequeños y boca de enfado
mk('alistair-horizon', 'corpulento', pal('#c86e66', TAN, iris='#1e1e1e', hat='#d87a7a', hat_d='#b05a5a', band='#ece4c4'),
   {'eyes': 'dot', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'face_front': CHUBBY, 'hairline': False, 'ear_out': 7, 'eye_y': 78},
   {'front': [L(outline([(12, 60), (-2, 70, 1), (6, 76), (0, 86, 1), (14, 82)])), L(outline([(88, 60), (102, 70, 1), (94, 76), (100, 86, 1), (86, 82)])),
              L(outline([(10, 62), (8, 34), (22, 12), (50, 2), (78, 12), (92, 34), (90, 62), (50, 56)]), 'hat', 'f'),
              L(outline([(12, 46), (50, 38), (88, 46), (90, 56), (50, 48), (10, 56)]), 'band', 'f', False),
              *[strand([(x, 8 + abs(x - 50) * 0.2), (x * 0.98 + 1, 58 - abs(x - 50) * 0.08)], 'hat_d', 'f', 1.0) for x in (22, 34, 46, 58, 70, 82)]],
    'side': [L(outline([(30, 60), (20, 72, 1), (28, 76), (24, 88, 1), (38, 78)])),
             L(outline([(90, 52), (94, 30), (84, 8), (56, -2), (26, 4), (6, 24), (2, 50), (8, 66), (40, 60)]), 'hat', 'f'),
             L(outline([(4, 40), (50, 36), (94, 38), (92, 48), (50, 46), (4, 50)]), 'band', 'f', False)],
    'back': [L(outline([(12, 62), (-2, 74, 1), (10, 80), (8, 92, 1), (24, 84), (50, 90), (76, 84), (92, 92, 1), (90, 80), (102, 74, 1), (88, 62)])),
             L(outline([(10, 66), (8, 34), (22, 12), (50, 2), (78, 12), (92, 34), (90, 66), (50, 70)]), 'hat', 'f'),
             L(outline([(10, 48), (50, 42), (90, 48), (90, 58), (50, 52), (10, 58)]), 'band', 'f', False)]},
   F(*brows(66, 'mid', 3.6, 14, 0.6, 12)))

# Kenrou (Alton Oldhat): cara alargada con barbilla de punta; un tupé malva grisáceo altísimo en cono con una raya oscura,
# orejas de punta, ojos de pillo y dos dientes enormes
mk('alton-oldhat', 'normal', pal('#b49ea0', SKIN, iris='#1e1e1e', streak='#7a5a64'),
   {'eyes': 'normal', 'brows': 'angry', 'mouth': 'buck', 'mouth_y': 98, 'hairline': False,
    'face_front': blob([(16, 46), (50, 30), (84, 46), (86, 74), (74, 98), (58, 114), (50, 118), (42, 114), (26, 98), (14, 74)])},
   {'front': [L(outline([(16, 54), (12, 20), (24, -16), (50, -36), (76, -16), (88, 20), (84, 54), (70, 40), (50, 54, 1), (30, 40)])),
              L(outline([(56, -30), (64, -10), (54, 20), (50, 54), (46, 26)]), 'streak', 'b', False),
              L(outline([(60, -28), (78, -10), (88, 22), (82, 50), (72, 30)]), 'shade', 'b', False)],
    'side': [L(outline([(70, 40), (88, 26), (90, -4), (72, -30), (40, -36), (16, -14), (4, 20), (8, 56), (24, 66), (40, 56), (56, 40)])),
             L(outline([(40, -30), (60, -30), (60, 20), (40, 40)]), 'streak', 'b', False)],
    'back': [L(outline([(16, 70), (12, 20), (24, -16), (50, -36), (76, -16), (88, 20), (84, 70), (50, 76)])),
             L(outline([(58, -28), (78, -10), (88, 22), (84, 66), (62, 72)]), 'shade', 'b', False)]},
   {'front': [L(outline([(16, 64), (2, 50, 1), (18, 82)]), (244, 186, 116, 255), 'b'), L(outline([(84, 64), (98, 50, 1), (82, 82)]), (244, 186, 116, 255), 'b')]})

# Kaminari (Ames Shivers, portero): melena verde oliva ondulada hasta la mandíbula, gafas negras rectangulares y sonrisa
mk('ames-shivers', 'normal', pal('#727228', SKIN, iris='#8a7a4a'),
   {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
   {'front': [L(outline([(6, 96), (4, 70), (0, 40), (14, 12), (50, 0), (86, 12), (100, 40), (96, 70), (98, 96), (84, 92), (82, 58), (18, 58), (18, 92)])),
              L(outline([(60, 4), (86, 16), (98, 44), (96, 92), (84, 70)]), 'shade', 'b', False),
              fr([(14, 66), (16, 40), (30, 22), (52, 16), (74, 22), (88, 40), (86, 64), (78, 50), (68, 60, 1), (60, 44), (46, 58, 1), (40, 42), (28, 58, 1), (22, 46)])]
             + rect_glasses('front', 76, BLACK),
    'side': [L(outline([(54, 62), (62, 52), (80, 46), (92, 32), (86, 8), (60, -2), (30, 2), (8, 20), (-2, 50), (0, 84), (8, 98), (24, 96), (36, 86), (40, 72), (46, 64)])),
             L(outline([(-1, 50), (26, 50), (40, 64), (34, 86), (22, 96), (8, 96)]), 'shade', 'b', False)] + rect_glasses('side', 76, BLACK),
    'back': [L(outline([(6, 98), (2, 44), (16, 12), (50, 0), (84, 12), (98, 44), (94, 98), (76, 94), (64, 102), (50, 96), (36, 102), (24, 94)])),
             L(outline([(58, 6), (84, 16), (98, 46), (94, 96), (64, 100)]), 'shade', 'b', False)]})

# ---------------------------------------------------------------------------------------------------- hoja 4

# Akagi (Andrew Meikle, portero): moreno de cara redonda; melena rubia dorada con un mechón crema en medio que le cae por
# los lados de la cara; ojos pequeños (guiña uno), nariz redonda y sonrisa
mk('andrew-meikle', 'normal', pal('#dcb41a', '#c09054', iris='#1e1e1e', streak='#f0e6b4', nose='#b07a44'),
   {'eyes': 'dot', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'face_front': CHUBBY, 'nose': (50, 86, 3.4), 'hairline': False},
   {'front': [L(outline([(4, 84), (0, 44), (14, 12), (50, 0), (86, 12), (100, 44), (96, 84), (86, 78), (84, 56), (16, 56), (14, 78)])),
              L(outline([(60, 4), (86, 16), (100, 46), (96, 82), (86, 60)]), 'shade', 'b', False),
              fr([(10, 76), (12, 40), (28, 18), (50, 10), (72, 18), (88, 40), (90, 76), (80, 60), (74, 44), (60, 34), (50, 44, 1), (40, 34), (26, 44), (20, 60)]),
              fr([(40, 14), (50, 8), (60, 14), (64, 34), (54, 40), (50, 48, 1), (46, 40), (36, 34)], 'streak')],
    'side': [L(outline([(54, 62), (62, 52), (80, 46), (92, 30), (86, 8), (60, -2), (30, 2), (8, 20), (-2, 50), (0, 80), (16, 90), (32, 88), (40, 74), (46, 64)])),
             L(outline([(-1, 50), (26, 50), (40, 64), (32, 86), (14, 88), (2, 78)]), 'shade', 'b', False), fr([(64, 2), (86, 10), (94, 30), (88, 48), (78, 34)], 'streak')],
    'back': [L(outline([(4, 86), (0, 44), (14, 12), (50, 0), (86, 12), (100, 44), (96, 86), (66, 92), (50, 94), (34, 92)])),
             L(outline([(58, 6), (84, 16), (100, 46), (96, 84), (64, 90)]), 'shade', 'b', False), L(outline([(40, 2), (60, 2), (58, 40), (42, 40)]), 'streak', 'b', False)]})

# Hamanoue (Andy Craft): pelo verde muy oscuro en pinchos altos de punta, cejas verdes gruesas, ojos redondos de susto
mk('andy-craft', 'normal', pal('#24543e', SKIN, iris='#1e1e1e'),
   {'eyes': 'round', 'brows': False, 'mouth': 'frown', 'mouth_y': 94, 'nose': (50, 86, 2.6), 'hairline': [(16, 60), (22, 46), (36, 52), (50, 42), (64, 52), (78, 46), (84, 60)]},
   {'front': [L(outline([(16, 62), (12, 44), (-6, 40, 1), (10, 28), (0, 10, 1), (20, 14), (22, -8, 1), (36, 6), (50, -22, 1), (62, 6), (78, -8, 1), (80, 14), (100, 10, 1),
                         (90, 28), (106, 40, 1), (88, 44), (84, 62), (78, 50), (22, 50)])),
              L(outline([(60, 2), (78, -4), (80, 16), (98, 12), (90, 30), (100, 40), (86, 46), (80, 30)]), 'shade', 'b', False)],
    'side': [L(outline([(58, 50), (66, 42), (84, 40), (100, 30, 1), (88, 22), (98, 4, 1), (76, 8), (78, -14, 1), (58, 2), (44, -16, 1), (36, 6), (12, -4, 1), (16, 16),
                        (-6, 24, 1), (6, 34), (-8, 50, 1), (10, 56), (8, 74, 1), (24, 66), (40, 60), (50, 54)])),
             L(outline([(4, 40), (34, 44), (40, 58), (24, 64), (10, 56)]), 'shade', 'b', False)],
    'back': [L(outline([(16, 72), (12, 44), (-6, 40, 1), (10, 28), (0, 10, 1), (20, 14), (22, -8, 1), (36, 6), (50, -22, 1), (62, 6), (78, -8, 1), (80, 14), (100, 10, 1),
                        (90, 28), (106, 40, 1), (88, 44), (84, 72), (70, 80, 1), (60, 74), (50, 84, 1), (40, 74), (30, 80, 1)])),
             L(outline([(58, 2), (86, 16), (100, 40), (86, 70), (62, 76)]), 'shade', 'b', False)]},
   F(*brows(63, 'mid', 4.0, 14, 0.7, 12)), S(*brow_side(63, 'mid', 4.0, 0.7)))

# Nishikiyama (Andy Crafter): grandullón de cara ancha; pelo rubio ondulado peinado hacia atrás hasta la nuca, cejas negras
# gruesas de enfado, ojos pequeños y una boca enorme de labios gruesos
mk('andy-crafter', 'corpulento', pal('#e0c47a', PALE, iris='#1e1e1e', lip='#c08a5a'),
   {'eyes': 'dot', 'brows': False, 'mouth': 'none', 'face_front': CHUBBY, 'hairline': (56, 30), 'ear_out': 5},
   {'front': [L(outline([(12, 90), (6, 60), (8, 30), (22, 10), (50, 2), (78, 10), (92, 30), (94, 60), (88, 90), (82, 80), (82, 56), (18, 56), (18, 80)])),
              L(outline([(60, 4), (84, 14), (94, 40), (90, 86), (82, 60)]), 'shade', 'b', False),
              *[strand([(x, 12), (x + 2, 22), (x - 2, 32)], 'deep', 'b', 1.0) for x in (32, 44, 56, 68)],
              L(outline([(34, 92), (66, 92), (64, 102), (36, 102)]), 'lip', 'f', ln=True), L([(36, 97), (64, 97)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(70, 44), (84, 30), (80, 8), (56, -2), (28, 2), (8, 20), (0, 50), (4, 84), (16, 96), (30, 92), (38, 76), (44, 60), (56, 50)])),
             L(outline([(1, 50), (28, 50), (40, 64), (30, 92), (14, 94), (4, 82)]), 'shade', 'b', False), L(ell(85, 97, 4, 5), 'lip', 'f', ln=True)],
    'back': [L(outline([(10, 94), (4, 44), (16, 12), (50, 2), (84, 12), (96, 44), (90, 94), (66, 100), (50, 102), (34, 100)])),
             L(outline([(58, 6), (84, 16), (96, 46), (90, 92), (64, 98)]), 'shade', 'b', False)]},
   F(*brows(64, BLACK, 4.6, 15, 0.9, 13)), S(*brow_side(64, BLACK, 4.6, 0.9)))

# Ebata (Andy Roff): cara larga de señor; pelo oliva muy corto pegado y plano encima, cejas oliva gruesas y ojos de sueño
mk('andy-roff', 'normal', pal('#7e7e30', SKIN, iris='#1e1e1e'),
   {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 100, 'face_front': LONG, 'nose': (50, 88, 3.6), 'hairline': (52, 30), 'eye_y': 76},
   cap(top=0, side=54, nape=80, flat=8),
   F(*brows(63, 'mid', 4.6, 14, -0.3, 13), L([(30, 72), (42, 72)], OUTC, 'f', False, False, 2.2), L([(58, 72), (70, 72)], OUTC, 'f', False, False, 2.2)),
   S(*brow_side(63, 'mid', 4.6)))

# Takazawa (Andy Sided): viejo moreno con la melena blanca peinada hacia atrás que le cae por la nuca hasta los hombros,
# cejas blancas, ojos de sueño y labios gruesos
mk('andy-sided', 'normal', pal('#d4d0b4', DARK, iris='#1e1e1e', lip='#9a5a3a', brow='#ece8d4'),
   {'eyes': 'normal', 'brows': False, 'mouth': 'none', 'face_front': LONG, 'nose': (50, 88, 3.4), 'hairline': (56, 30)},
   {'front': [L(outline([(10, 100), (4, 70), (6, 34), (20, 10), (50, 0), (80, 10), (94, 34), (96, 70), (90, 100), (80, 92), (82, 56), (18, 56), (20, 92)])),
              L(outline([(60, 4), (84, 14), (94, 40), (92, 96), (82, 60)]), 'shade', 'b', False),
              *[strand([(x, 8 + abs(x - 50) * 0.2), (x * 1.04 - 2, 50)], 'shade', 'b', 1.0) for x in (30, 42, 58, 70)],
              L(outline([(38, 96), (62, 96), (60, 104), (40, 104)]), 'lip', 'f', ln=True),
              L([(30, 66), (42, 64)], 'brow', 'f', False, False, 2.4), L([(70, 66), (58, 64)], 'brow', 'f', False, False, 2.4),
              L([(30, 72), (42, 72)], OUTC, 'f', False, False, 2.2), L([(58, 72), (70, 72)], OUTC, 'f', False, False, 2.2)],
    'side': [L(outline([(70, 44), (84, 30), (80, 8), (56, -2), (28, 2), (8, 20), (0, 50), (-2, 90), (8, 106), (24, 104), (34, 90), (40, 70), (56, 50)])),
             L(outline([(1, 50), (28, 50), (38, 70), (24, 102), (6, 102)]), 'shade', 'b', False), L(ell(85, 98, 4, 4), 'lip', 'f', ln=True)],
    'back': [L(outline([(6, 104), (2, 44), (16, 12), (50, 2), (84, 12), (98, 44), (94, 104), (74, 98), (62, 108), (50, 100), (38, 108), (26, 98)])),
             L(outline([(58, 6), (84, 16), (98, 46), (94, 102), (64, 104)]), 'shade', 'b', False)]})

# Katsuragi (Andy Wallpole): moreno; pelo rubio dorado en ondas que le caen por los lados con un moño castaño oscuro en
# lo alto de la cabeza; ojos afilados verdes y sonrisa
mk('andy-wallpole', 'normal', pal('#dcb41a', TAN, iris='#5a8a5a', bun='#5a4824', bun_d='#3e321a'),
   {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'face_front': LONG, 'hairline': False},
   {'front': [L(cloud(50, 6, 34, 18, 7), 'bun', 'b'), L(outline([(56, -8), (80, 4), (82, 20), (60, 14)]), 'bun_d', 'b', False),
              L(outline([(10, 96), (14, 82), (6, 66), (10, 44), (20, 22), (50, 14), (80, 22), (92, 44), (94, 66), (86, 82), (90, 96), (80, 86), (82, 56), (18, 56), (20, 86)])),
              fr([(14, 70), (16, 44), (30, 28), (50, 24), (70, 28), (84, 44), (86, 70), (78, 56), (70, 44), (58, 40), (46, 54, 1), (40, 40), (28, 46), (22, 58)]),
              strand([(16, 70), (10, 82), (16, 94)], 'shade', 'f', 1.0), strand([(84, 70), (90, 82), (84, 94)], 'shade', 'f', 1.0)],
    'side': [L(cloud(46, 2, 30, 18, 7), 'bun', 'b'),
             L(outline([(54, 62), (62, 52), (80, 46), (90, 30), (84, 14), (60, 10), (30, 12), (10, 26), (4, 50), (8, 76), (4, 92), (20, 98), (32, 88), (40, 72), (46, 64)]))],
    'back': [L(cloud(50, 6, 34, 18, 7), 'bun', 'b'),
             L(outline([(8, 96), (6, 44), (18, 20), (50, 14), (82, 20), (94, 44), (92, 96), (74, 90), (62, 100), (50, 92), (38, 100), (26, 90)])),
             L(outline([(58, 16), (82, 22), (94, 48), (92, 94), (64, 98)]), 'shade', 'b', False)]})

# Otake (Ant Hophila): cabeza redonda enorme rapada, con una franja de pelo verde oscuro a los lados y un mechón blanco de
# punta encima; cejas verdes, ojos pequeños, colorete y la lengua fuera
mk('ant-hophila', 'corpulento', pal('#2a5a4a', SKIN, iris='#1e1e1e', tuft='#d4ccb0', tongue='#e07a80'),
   {'eyes': 'dot', 'brows': False, 'mouth': 'none', 'face_front': CHUBBY, 'hairline': False, 'ear_out': 8},
   {'front': [L(outline([(8, 62), (6, 40), (14, 26), (18, 40), (16, 56)])), L(outline([(92, 62), (94, 40), (86, 26), (82, 40), (84, 56)])),
              L(outline([(38, 30), (28, 10, 1), (42, 18), (44, -2, 1), (52, 16), (62, 0, 1), (60, 18), (74, 12, 1), (64, 30)]), 'tuft', 'f'),
              L(quad((30, 98), (50, 104), (72, 96)), OUTC, 'f', False, False, 1.6), L(ell(66, 98, 5, 4), 'tongue', 'f', ln=True)]
             + blush(86, (240, 140, 120, 255), 26, 4) + brows(66, 'mid', 4.4, 15, 0.2, 13),
    'side': [L(outline([(14, 74), (6, 50), (12, 30), (26, 22), (30, 40), (34, 62)])),
             L(outline([(54, 26), (44, 6, 1), (58, 14), (66, -2, 1), (68, 16), (80, 12, 1), (74, 30)]), 'tuft', 'f')],
    'back': [L(outline([(8, 72), (6, 40), (16, 22), (50, 14), (84, 22), (94, 40), (92, 72), (50, 80)])),
             L(outline([(38, 24), (28, 4, 1), (42, 12), (48, -4, 1), (54, 12), (66, 0, 1), (64, 16), (72, 8, 1), (64, 28)]), 'tuft', 'f')]})

# Herzen (Anthony "Anton" Herzen): melena rubia ceniza ondulada hasta los hombros, piel muy clara y ojos verde agua
mk('anthony-anton-herzen', 'normal', pal('#c4aa7a', '#f0d6c0', iris='#5aaa9a'),
   {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 92, 'hairline': False},
   {'front': [L(outline([(2, 104), (6, 86), (-2, 66), (4, 40), (16, 14), (50, 0), (84, 14), (98, 40), (102, 66), (94, 86), (98, 104), (84, 96), (82, 56), (18, 56), (16, 96)])),
              L(outline([(60, 4), (84, 16), (98, 44), (96, 100), (84, 70)]), 'shade', 'b', False),
              fr([(14, 70), (14, 40), (28, 20), (50, 14), (72, 20), (86, 40), (86, 68), (78, 52), (68, 40), (54, 36), (44, 52, 1), (36, 40), (26, 48), (20, 62)]),
              strand([(12, 70), (6, 84), (12, 98)], 'shade', 'f', 1.0), strand([(88, 70), (94, 84), (88, 98)], 'shade', 'f', 1.0)],
    'side': [L(outline([(54, 62), (62, 52), (80, 46), (92, 30), (86, 8), (60, -2), (30, 2), (8, 20), (-4, 50), (0, 80), (-4, 100), (12, 108), (28, 102), (36, 86), (42, 70),
                        (48, 62)])),
             L(outline([(-3, 50), (26, 50), (40, 66), (28, 100), (10, 104)]), 'shade', 'b', False)],
    'back': [L(outline([(2, 106), (0, 44), (14, 12), (50, 0), (86, 12), (100, 44), (98, 106), (80, 98), (66, 108), (50, 100), (34, 108), (20, 98)])),
             L(outline([(58, 6), (84, 16), (100, 46), (98, 104), (64, 104)]), 'shade', 'b', False)]})

# ---------------------------------------------------------------------------------------------------- hoja 5

# Zenigata (Anthony Coyne): señor de cara ancha con pecas y patillas largas; pelo verde oliva oscuro revuelto con dos
# pelos de antena; ojos amarillos entornados y media sonrisa
mk('anthony-coyne', 'normal', pal('#5a5a26', SKIN, iris='#d8c030', freckle='#c07a4a'),
   {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'face_front': CHUBBY, 'hairline': (56, 40), 'ear_out': 4},
   spiky(amp=9, n=10, seed=91, cy=40, ry=36, rx=50, lo=60, nape=86, sweep=-0.4),
   {'front': [L(outline([(13, 56), (10, 84), (14, 88), (17, 62)]), 'mid', 'f'), L(outline([(87, 56), (90, 84), (86, 88), (83, 62)]), 'mid', 'f'),
              L(quad((52, 4), (56, -12), (64, -18)), 'mid', 'b', False, False, 2.4), L(quad((56, 6), (64, -6), (72, -8)), 'mid', 'b', False, False, 2.4),
              *[L(ell(x, y, 1.0, 1.0), 'freckle', 'f', False) for x, y in ((28, 84), (32, 87), (25, 88), (72, 84), (68, 87), (75, 88))]],
    'side': [L(outline([(44, 56), (40, 86), (48, 90), (52, 64)]), 'mid', 'f'), L(quad((56, 0), (62, -16), (72, -20)), 'mid', 'b', False, False, 2.4)]},
   F(L([(26, 70), (44, 72)], 'mid', 'f', False, False, 2.4), L([(74, 70), (56, 72)], 'mid', 'f', False, False, 2.4)))

# Kitagawa (Anthony Phinder): muy moreno; pelo crema claro rapado en franjas y alto como un cepillo, ojos azules afilados
# de enfado y labios gruesos
mk('anthony-phinder', 'normal', pal('#e6e4cc', DARK, iris='#4a9ac8', lip='#7a4a34'),
   {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'face_front': LONG, 'hairline': (56, 40)},
   {'front': [L(outline([(16, 56), (14, 20), (22, 0), (50, -6), (78, 0), (86, 20), (84, 56), (78, 44), (22, 44)])),
              *[strand([(x, -2 + abs(x - 50) * 0.1), (x, 42)], 'shade', 'b', 1.0) for x in (26, 34, 42, 50, 58, 66, 74)],
              L(outline([(40, 94), (60, 94), (58, 100), (42, 100)]), 'lip', 'f', ln=True)],
    'side': [L(outline([(80, 40), (86, 20), (80, 0), (56, -8), (28, -4), (10, 12), (6, 40), (16, 60), (36, 56), (56, 46)])),
             *[strand([(x, -4), (x - 4, 50)], 'shade', 'b', 1.0) for x in (24, 38, 52, 66)]],
    'back': [L(outline([(16, 70), (14, 20), (22, 0), (50, -6), (78, 0), (86, 20), (84, 70), (50, 76)])),
             *[strand([(x, -2), (x, 70)], 'shade', 'b', 1.0) for x in (30, 42, 58, 70)]]})

# Shishido (Aran Cheeks, portero): cara alargada con nariz larga; pelo malva rosado rizado y abultado con un rizo en media
# luna en la frente, ojos redondos y unas lágrimas azules pintadas bajo los ojos
mk('aran-cheeks', 'normal', pal('#b47a66', SKIN, iris='#1e1e1e', paint='#30486a'),
   {'eyes': 'round', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'face_front': LONG, 'nose': (50, 88, 3.4), 'hairline': (54, 40)},
   {'front': [L(cloud(50, 26, 44, 30, 9)), L(outline([(60, 2), (86, 18), (92, 42), (82, 50), (72, 26)]), 'shade', 'b', False),
              L(quad((40, 30), (54, 20), (58, 40)) + quad((58, 40), (50, 30), (42, 34))[1:], 'shade', 'f', False),
              L(quad((28, 82), (34, 88), (40, 82)), 'paint', 'f', False, False, 2.4), L(quad((60, 82), (66, 88), (72, 82)), 'paint', 'f', False, False, 2.4)],
    'side': [L(cloud(46, 26, 44, 30, 9)), L(blob([(10, 40), (30, 30), (40, 54), (20, 62)], 6), 'shade', 'b', False)],
    'back': [L(cloud(50, 30, 46, 34, 9)), L(outline([(60, 4), (88, 20), (94, 50), (80, 60), (70, 30)]), 'shade', 'b', False)]})

# Takamine (Archie Meades, portero): melena rosa en casco con la raya al lado y el flequillo largo hacia un lado; ojos
# afilados y gesto serio
mk('archie-meades', 'normal', pal('#c66262', SKIN, iris='#1e1e1e'),
   {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'hairline': False},
   {'front': [L(outline([(8, 88), (2, 50), (12, 18), (40, 0), (66, 2), (90, 18), (98, 50), (94, 88), (84, 82), (82, 56), (18, 56), (16, 82)])),
              L(outline([(60, 4), (86, 18), (98, 50), (94, 86), (84, 60)]), 'shade', 'b', False),
              fr([(14, 66), (16, 40), (30, 20), (52, 12), (74, 18), (88, 36), (86, 60), (76, 44), (60, 36), (46, 40), (34, 52), (24, 66, 1)])],
    'side': [L(outline([(54, 64), (62, 54), (80, 48), (92, 32), (86, 8), (60, -2), (30, 2), (8, 22), (-2, 52), (2, 82), (16, 92), (32, 90), (40, 76), (46, 66)])),
             L(outline([(-1, 52), (26, 52), (40, 66), (32, 88), (16, 90), (4, 80)]), 'shade', 'b', False)],
    'back': [L(outline([(6, 90), (2, 44), (16, 12), (50, 0), (84, 12), (98, 44), (94, 90), (66, 96), (50, 98), (34, 96)])),
             L(outline([(58, 6), (84, 16), (98, 46), (94, 88), (64, 94)]), 'shade', 'b', False)]})

# Katou (Archie Tate, portero): piel clara; tupé verde oscuro ondulado peinado hacia un lado que le tapa media frente, ojos
# claros entornados y sonrisa tranquila
mk('archie-tate', 'normal', pal('#24543e', SKIN, iris='#8a9aa0'),
   {'eyes': 'normal', 'brows': True, 'mouth': 'smile', 'mouth_y': 94, 'face_front': LONG, 'hairline': False},
   {'front': [L(outline([(14, 62), (6, 40), (14, 12), (42, -2), (74, 0), (94, 16), (96, 40), (88, 62), (82, 50), (18, 50)])),
              L(outline([(60, 2), (90, 14), (96, 40), (88, 60), (80, 36)]), 'shade', 'b', False),
              fr([(4, 46), (10, 24), (30, 10), (56, 8), (80, 16), (92, 34), (80, 34), (62, 30), (44, 38), (30, 52), (18, 60, 1), (16, 50)]),
              strand([(20, 30), (40, 22), (64, 22)], 'deep', 'f', 1.0)],
    'side': [L(outline([(60, 54), (70, 44), (90, 40), (98, 22), (86, 4), (60, -6), (30, -2), (8, 16), (0, 44), (8, 70), (22, 80), (36, 74), (44, 62), (52, 56)])),
             L(outline([(1, 44), (28, 46), (40, 60), (34, 74), (20, 78), (8, 68)]), 'shade', 'b', False)],
    'back': [L(outline([(12, 80), (6, 40), (16, 12), (50, -2), (84, 12), (96, 40), (90, 80), (50, 86)])),
             L(outline([(58, 4), (86, 14), (96, 42), (90, 78), (62, 84)]), 'shade', 'b', False)]})

# Yoshino (Archy Medez, portero): pelo lila grisáceo corto en pinchos, con tres puntas hacia arriba y flequillo en picos;
# ojos grandes y sonrisa
mk('archy-medez', 'normal', pal('#7e7088', SKIN, iris='#1e1e1e'),
   {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93, 'hairline': [(16, 62), (24, 50), (32, 58), (40, 48), (50, 58), (60, 48), (68, 58), (76, 50), (84, 62)]},
   {'front': [L(outline([(16, 64), (10, 40), (16, 18), (34, 8), (40, -14, 1), (48, 4), (54, -20, 1), (60, 4), (70, -10, 1), (70, 10), (86, 20), (90, 40), (84, 64),
                         (78, 50), (22, 50)])),
              L(outline([(58, 2), (70, -8), (72, 12), (86, 22), (90, 42), (84, 60), (76, 36)]), 'shade', 'b', False)],
    'side': [L(outline([(58, 52), (68, 44), (84, 40), (92, 26), (86, 10), (70, 4), (72, -14, 1), (56, 0), (50, -18, 1), (40, 2), (22, 8), (6, 26), (2, 50), (10, 74),
                        (24, 80), (38, 72), (46, 60)])),
             L(outline([(3, 46), (30, 48), (42, 60), (36, 72), (22, 78), (10, 70)]), 'shade', 'b', False)],
    'back': [L(outline([(14, 78), (10, 40), (16, 18), (34, 8), (40, -12, 1), (48, 4), (54, -18, 1), (60, 4), (70, -8, 1), (70, 10), (86, 20), (90, 40), (86, 78),
                        (50, 84)])),
             L(outline([(58, 4), (86, 20), (90, 44), (86, 76), (62, 82)]), 'shade', 'b', False)]})

# Sasanami (Armstrong Peck, portero): cara alargada de mandíbula fuerte; pelo rojo oscuro con un copete en punta encima,
# los lados cortos y unas patillas de pinchos oscuros; ojos afilados y sonrisa de lado
mk('armstrong-peck', 'normal', pal('#a02a0a', '#f4ae66', iris='#1e1e1e', burn='#6a2a1a'),
   {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'face_front': LONG, 'nose': (50, 86, 3), 'hairline': [(16, 60), (22, 46), (34, 52), (44, 42), (50, 60), (58, 44), (70, 46), (84, 60)]},
   cap(top=6, side=60, nape=84, w=0),
   {'front': [L(outline([(28, 30), (24, 4), (40, -16), (52, -24, 1), (54, -10), (66, -6), (74, 14), (72, 32)]), 'mid', 'b'),
              L(outline([(16, 60), (6, 72, 1), (12, 76), (4, 88, 1), (18, 84)]), 'burn', 'b'), L(outline([(84, 60), (94, 72, 1), (88, 76), (96, 88, 1), (82, 84)]), 'burn', 'b')],
    'side': [L(outline([(60, 30), (56, 4), (68, -16), (80, -24, 1), (82, -8), (90, 4), (88, 26)]), 'mid', 'b'),
             L(outline([(36, 64), (26, 74, 1), (34, 78), (28, 90, 1), (42, 82)]), 'burn', 'b')],
    'back': [L(outline([(30, 30), (26, 6), (42, -14), (54, -22, 1), (56, -8), (68, -4), (74, 14), (70, 32)]), 'mid', 'b')]})

# Morisaki (Art Pendragon, portero): moreno; pelo pardo verdoso en casco con un mechón alto que se curva hacia arriba, una
# gota roja pintada en la frente, rayas rojas en las mejillas y ojos naranjas redondos
mk('art-pendragon', 'normal', pal('#8e7a42', '#c09054', iris='#d86a20', paint='#c41e1e'),
   {'eyes': 'normal', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
   bowl(lo=66, fr_y=60, w=4, top=4, n=6, jag=6),
   {'front': [L(outline([(50, 8), (54, -10), (68, -22, 1), (62, -6), (58, 10)]), 'mid', 'b'),
              L(outline([(50, 54), (54, 62), (50, 70, 1), (46, 62)]), 'paint', 'f', ln=True),
              L([(26, 84), (36, 90)], 'paint', 'f', False, False, 1.6), L([(26, 88), (34, 94)], 'paint', 'f', False, False, 1.6),
              L([(74, 84), (64, 90)], 'paint', 'f', False, False, 1.6), L([(74, 88), (66, 94)], 'paint', 'f', False, False, 1.6)],
    'side': [L(outline([(60, 6), (66, -12), (80, -22, 1), (74, -4), (68, 8)]), 'mid', 'b')],
    'back': [L(outline([(50, 8), (54, -10), (68, -22, 1), (62, -6), (58, 10)]), 'mid', 'b')]})

# ---------------------------------------------------------------------------------------------------- hoja 6

# Sakai (Art Teest): moreno claro; pelo verde agua en casco con un flequillo largo que le tapa el ojo derecho y una punta
# que sale hacia un lado; sonrisa
mk('art-teest', 'normal', pal('#6a9c90', SKIN, iris='#1e1e1e'),
   {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
   {'front': [L(outline([(10, 84), (4, 46), (14, 14), (50, 0), (84, 12), (104, 22, 1), (94, 34), (96, 60), (92, 84), (84, 78), (84, 56), (18, 56), (16, 78)])),
              L(outline([(60, 4), (86, 16), (96, 46), (92, 82), (84, 60)]), 'shade', 'b', False),
              fr([(8, 80), (8, 44), (20, 22), (44, 14), (70, 18), (86, 34), (88, 56), (76, 46), (62, 50), (58, 60, 1), (52, 52), (46, 70), (36, 92, 1), (32, 74), (22, 86, 1),
                  (18, 70)]),
              strand([(20, 30), (34, 56), (34, 82)], 'deep', 'f', 1.0)],
    'side': [L(outline([(54, 62), (62, 52), (80, 46), (92, 30), (86, 8), (60, -2), (30, 2), (8, 20), (-2, 50), (2, 80), (16, 90), (32, 88), (40, 74), (46, 64)])),
             L(outline([(-1, 50), (26, 50), (40, 64), (32, 86), (16, 88), (4, 78)]), 'shade', 'b', False)],
    'back': [L(outline([(6, 88), (2, 44), (16, 12), (50, 0), (84, 12), (100, 24, 1), (96, 44), (94, 88), (66, 94), (50, 96), (34, 94)])),
             L(outline([(58, 6), (84, 16), (98, 46), (94, 86), (64, 92)]), 'shade', 'b', False)]})

# Sakaki (Arthur Dox): un pañuelo crema que le envuelve toda la cabeza en punta y le deja la cara al aire, con un vendaje
# en la frente; cejas negras gruesas y sonrisa
mk('arthur-dox', 'normal', pal('#e6e4c4', SKIN, iris='#1e1e1e', bandage='#f4f2e4'),
   {'eyes': 'round', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False, 'ears': False},
   {'front': [L(outline([(8, 110), (2, 70), (8, 30), (30, 4), (50, -10, 1), (70, 4), (92, 30), (98, 70), (92, 110), (82, 96), (84, 60), (16, 60), (18, 96)])),
              L(outline([(60, 0), (90, 28), (98, 70), (92, 106), (84, 70)]), 'shade', 'b', False),
              L(outline([(16, 48), (50, 40), (84, 48), (84, 60), (50, 54), (16, 60)]), 'bandage', 'f', ln=True)] + brows(64, BLACK, 4.6, 14, 0.4, 13),
    'side': [L(outline([(60, 66), (70, 50), (86, 46), (90, 28), (76, 6), (52, -10, 1), (26, 0), (6, 24), (0, 60), (4, 104), (24, 112), (44, 100), (54, 82)])),
             L(outline([(2, 60), (30, 60), (44, 90), (24, 110), (4, 102)]), 'shade', 'b', False)] + brow_side(64, BLACK, 4.6),
    'back': [L(outline([(8, 112), (2, 70), (8, 30), (30, 4), (50, -10, 1), (70, 4), (92, 30), (98, 70), (92, 112), (50, 118)])),
             L(outline([(58, 0), (90, 28), (98, 70), (92, 110), (62, 116)]), 'shade', 'b', False)]})

# Matsuyama (Arthur Myrddin): gordito de cara redonda; pinchos naranja oscuro en abanico hacia arriba con un flequillo
# corto rosado en medio; ojos redondos, nariz grande y sonrisa ancha
mk('arthur-myrddin', 'corpulento', pal('#a8461a', SKIN, iris='#1e1e1e', tuft='#c08a8a'),
   {'eyes': 'round', 'brows': True, 'mouth': 'none', 'face_front': CHUBBY, 'nose': (50, 86, 5), 'hairline': [(14, 56), (30, 46), (50, 42), (70, 46), (86, 56)], 'ear_out': 7},
   {'front': [L(outline([(12, 60), (8, 40), (-8, 30, 1), (10, 24), (2, 4, 1), (22, 12), (24, -10, 1), (38, 6), (50, -22, 1), (62, 6), (76, -10, 1), (78, 12), (98, 4, 1),
                         (90, 24), (108, 30, 1), (92, 40), (88, 60), (80, 48), (20, 48)])),
              L(outline([(58, 0), (76, -8), (80, 14), (96, 8), (90, 26), (104, 32), (90, 44), (80, 30)]), 'shade', 'b', False),
              fr([(36, 36), (50, 30), (64, 36), (62, 52), (56, 46), (50, 54, 1), (44, 46), (38, 52)], 'tuft'),
              L(quad((32, 96), (50, 106), (68, 96)), OUTC, 'f', False, False, 1.6)],
    'side': [L(outline([(64, 46), (84, 40), (100, 30, 1), (88, 22), (96, 2, 1), (74, 8), (74, -14, 1), (56, 2), (42, -18, 1), (34, 4), (10, -6, 1), (14, 16), (-8, 26, 1),
                        (6, 36), (0, 54, 1), (14, 60), (34, 56), (52, 50)])),
             L(outline([(4, 40), (34, 44), (40, 54), (14, 58)]), 'shade', 'b', False)],
    'back': [L(outline([(12, 70), (8, 40), (-8, 30, 1), (10, 24), (2, 4, 1), (22, 12), (24, -10, 1), (38, 6), (50, -22, 1), (62, 6), (76, -10, 1), (78, 12), (98, 4, 1),
                        (90, 24), (108, 30, 1), (92, 40), (88, 70), (50, 76)])),
             L(outline([(58, 2), (88, 12), (92, 40), (88, 68), (62, 74)]), 'shade', 'b', False)]})

# Akatsuki (Ash Cloud): pelo rojo intenso revuelto en pinchos con mechones sobre la frente, dos rombos naranjas pintados en
# las mejillas, ojos afilados y ceño fruncido
mk('ash-cloud', 'normal', pal('#b0280a', SKIN, iris='#1e1e1e', paint='#e07a3a'),
   {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'hairline': [(16, 62), (24, 48), (34, 58), (42, 46), (52, 60), (60, 46), (72, 52), (84, 62)]},
   spiky(amp=12, n=11, seed=101, cy=40, ry=36, lo=64, nape=90, sweep=-0.2),
   F(L(outline([(28, 80), (34, 86), (28, 92), (22, 86)]), 'paint', 'f', False), L(outline([(72, 80), (78, 86), (72, 92), (66, 86)]), 'paint', 'f', False)))

# Yayoi (Ashley Dale): melena rosa rojizo larga por un lado que le tapa el ojo derecho, con una coleta baja que sale hacia
# un lado y dos puntas arriba; un ojo amarillo claro
mk('ashley-dale', 'normal', pal('#c26c62', SKIN, iris='#e0d880'),
   {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
   {'front': [L(outline([(10, 80), (4, 44), (16, 14), (40, 2), (44, -14, 1), (52, 0), (62, -8, 1), (64, 4), (86, 14), (100, 30, 1), (94, 40), (96, 70), (92, 86), (84, 80),
                         (84, 56), (18, 56), (16, 76)])),
              L(outline([(14, 70), (-8, 92), (-20, 104, 1), (0, 96), (16, 84)]), 'mid', 'b'),
              L(outline([(60, 4), (86, 16), (96, 46), (92, 84), (84, 60)]), 'shade', 'b', False),
              fr([(42, 20), (66, 16), (86, 30), (94, 56), (92, 86), (80, 96, 1), (76, 76), (64, 90, 1), (58, 72), (48, 64, 1), (46, 42)]),
              fr([(14, 60), (16, 40), (28, 26), (44, 20), (42, 36), (32, 46), (22, 58, 1)])],
    'side': [L(outline([(54, 62), (62, 52), (80, 46), (92, 30), (86, 8), (60, -2), (30, 2), (8, 20), (-2, 50), (2, 78), (16, 88), (32, 86), (40, 74), (46, 64)])),
             L(outline([(14, 70), (-6, 90), (-16, 100, 1), (4, 94), (20, 84)]), 'mid', 'b')],
    'back': [L(outline([(8, 82), (4, 44), (16, 14), (40, 2), (44, -12, 1), (52, 0), (62, -6, 1), (64, 4), (86, 14), (96, 44), (92, 82), (50, 88)])),
             L(outline([(40, 76), (20, 96), (8, 108, 1), (26, 100), (46, 82)]), 'mid', 'b'),
             L(outline([(58, 6), (86, 16), (96, 46), (92, 80), (62, 86)]), 'shade', 'b', False)]})

# Shiragiku (Ashley Fay): pelo rubio crema alborotado con un flequillo largo que le tapa el ojo derecho y una coleta corta
# que sale de lado con una goma roja; el ojo visible con una estrella
mk('ashley-fay', 'normal', pal('#dcd8a0', PALE, iris='#1e1e1e', tie='#c03a2a'),
   {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
   spiky(amp=10, n=10, seed=111, cy=40, ry=36, lo=62, nape=88),
   {'front': [fr([(10, 50), (24, 22), (48, 14), (70, 20), (80, 34), (66, 40), (54, 60), (50, 90, 1), (42, 78), (32, 92, 1), (24, 68), (14, 66, 1)]),
              L(outline([(84, 66), (104, 76), (118, 94, 1), (100, 86), (86, 80)]), 'mid', 'b'), L(ell(88, 72, 3, 4), 'tie', 'f', ln=True)],
    'side': [L(outline([(26, 56), (6, 70), (-8, 90, 1), (10, 80), (26, 68)]), 'mid', 'b'), L(ell(26, 60, 3, 4), 'tie', 'f', ln=True)],
    'back': [L(outline([(16, 66), (-4, 76), (-18, 94, 1), (0, 86), (14, 80)]), 'mid', 'b'), L(ell(12, 72, 3, 4), 'tie', 'f', ln=True)]})

# Kumano (Aston Isher): un pañuelo naranja atado en la cabeza del que sale por detrás un tupé enorme malva grisáceo que se
# curva hacia un lado; ojos lilas afilados
mk('aston-isher', 'normal', pal('#9a7a74', SKIN, iris='#7a7aa0', scarf='#e0862a', scarf_d='#b06a1e'),
   {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
   {'front': [L(outline([(46, 30), (52, 0), (70, -16), (94, -6), (110, 24), (106, 58), (96, 72), (94, 50), (80, 30)]), 'mid', 'b'),
              L(outline([(70, -10), (96, 0), (108, 30), (100, 60), (92, 40)]), 'shade', 'b', False),
              L(outline([(10, 62), (8, 36), (20, 14), (46, 6), (62, 16), (58, 40), (40, 56), (18, 60)]), 'scarf', 'f'),
              L(outline([(10, 60), (-4, 78, 1), (14, 70), (12, 84, 1), (20, 64)]), 'scarf_d', 'f')],
    'side': [L(outline([(40, 20), (50, -10), (74, -18), (98, -4), (104, 24), (90, 40), (70, 30), (56, 46)]), 'mid', 'b'),
             L(outline([(70, 40), (84, 24), (70, 6), (44, 0), (20, 10), (6, 30), (4, 54), (20, 62), (40, 56), (56, 46)]), 'scarf', 'f'),
             L(outline([(8, 50), (-8, 66, 1), (8, 60), (4, 74, 1), (16, 58)]), 'scarf_d', 'f')],
    'back': [L(outline([(30, 30), (36, 0), (60, -16), (88, -6), (104, 24), (100, 56), (90, 70), (86, 40)]), 'mid', 'b'),
             L(outline([(10, 66), (8, 36), (22, 14), (50, 6), (78, 14), (92, 36), (90, 66), (50, 72)]), 'scarf', 'f'),
             L(outline([(44, 66), (36, 90, 1), (50, 72), (64, 90, 1), (56, 66)]), 'scarf_d', 'f')]})

# Kumokawa (Attley Hightable, portero): cara alargada con nariz larga; pelo azul pizarra abultado en bolas de rizos por
# arriba y a los lados, ojos de sueño y boca seria
mk('attley-hightable', 'normal', pal('#46546a', SKIN, iris='#1e1e1e'),
   {'eyes': 'normal', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100, 'face_front': LONG, 'nose': (50, 88, 3.6), 'hairline': (52, 44)},
   {'front': [L(cloud(50, 14, 42, 22, 8)), L(cloud(14, 54, 12, 18, 5)), L(cloud(86, 54, 12, 18, 5)), L(cloud(12, 82, 9, 10, 4)), L(cloud(88, 82, 9, 10, 4)),
              L(outline([(60, -4), (86, 8), (92, 30), (80, 30)]), 'shade', 'b', False),
              L([(30, 72), (42, 72)], OUTC, 'f', False, False, 2.2), L([(58, 72), (70, 72)], OUTC, 'f', False, False, 2.2)],
    'side': [L(cloud(44, 14, 42, 24, 8)), L(cloud(20, 52, 18, 22, 6)), L(cloud(20, 82, 12, 12, 4))],
    'back': [L(cloud(50, 16, 44, 24, 8)), L(cloud(16, 52, 14, 22, 5)), L(cloud(84, 52, 14, 22, 5)), L(cloud(50, 62, 34, 22, 7))]})

# ---------------------------------------------------------------------------------------------------- hoja 7

# Kumai (Aubry Dient, portero): pelo verde azulado oscuro revuelto con mechones sobre la frente y puntas en la nuca; ojos
# afilados y sonrisa de pillo
mk('aubry-dient', 'normal', pal('#4e6c64', SKIN, iris='#1e1e1e'),
   {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93, 'hairline': False},
   spiky(amp=8, n=10, seed=121, cy=40, ry=38, lo=66, nape=92),
   F(fr([(12, 66), (14, 40), (30, 22), (52, 16), (74, 22), (88, 40), (88, 64), (80, 50), (72, 62, 1), (64, 46), (54, 58, 1), (46, 44), (36, 58, 1), (28, 46), (20, 62)])))

# Suemitsu (Austin Tayssus): pelo verde hierba ondulado que le cae hasta la mandíbula, con mechones sobre los ojos; cejas
# verdes gruesas, ojos de sueño y boca seria
mk('austin-tayssus', 'normal', pal('#6a9a3e', SKIN, iris='#1e1e1e'),
   {'eyes': 'normal', 'brows': False, 'mouth': 'frown', 'mouth_y': 94, 'hairline': False},
   {'front': [L(outline([(4, 96), (8, 76), (0, 50), (12, 16), (50, 0), (88, 16), (100, 50), (92, 76), (96, 96), (84, 90), (84, 58), (18, 58), (16, 90)])),
              L(outline([(60, 4), (88, 18), (98, 50), (94, 92), (84, 70)]), 'shade', 'b', False),
              fr([(14, 70), (14, 40), (30, 20), (52, 14), (74, 20), (88, 40), (86, 66), (76, 52), (70, 40), (58, 48), (48, 40), (36, 52), (26, 46), (20, 66)])]
             + brows(66, 'mid', 4.0, 14, -0.4, 13) + [L([(30, 74), (42, 74)], OUTC, 'f', False, False, 2.2), L([(58, 74), (70, 74)], OUTC, 'f', False, False, 2.2)],
    'side': [L(outline([(54, 62), (62, 52), (80, 46), (92, 30), (86, 8), (60, -2), (30, 2), (8, 20), (-2, 50), (2, 84), (-2, 98), (14, 102), (30, 96), (38, 80), (46, 64)])),
             L(outline([(-1, 50), (26, 50), (40, 64), (30, 96), (12, 100)]), 'shade', 'b', False)] + brow_side(66, 'mid', 4.0),
    'back': [L(outline([(4, 98), (2, 44), (16, 12), (50, 0), (84, 12), (98, 44), (96, 98), (78, 92), (64, 102), (50, 94), (36, 102), (22, 92)])),
             L(outline([(58, 6), (84, 16), (98, 46), (96, 96), (64, 100)]), 'shade', 'b', False)]})

# Hanayama (Balt Decker): pinchos grandes rosa crema en todas direcciones con mechones de punta sobre la frente, rayas rojas
# en las mejillas, ojos redondos grandes y sonrisa
mk('balt-decker', 'normal', pal('#e6d6b6', SKIN, iris='#1e1e1e', paint='#c03a2a'),
   {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': [(16, 62), (24, 46), (34, 56), (42, 44), (52, 58), (60, 44), (72, 50), (84, 62)]},
   spiky(amp=22, n=10, seed=131, cy=42, ry=38, rx=46, lo=66, nape=92),
   F(L([(22, 86), (32, 86)], 'paint', 'f', False, False, 2.6), L([(68, 86), (78, 86)], 'paint', 'f', False, False, 2.6)))

# Arakida (Bamber Mandrina): la cabeza entera envuelta en vendas verde oliva como una momia, con un solo ojo al aire
mk('bamber-mandrina', 'normal', pal('#6e6c26', '#e6d8b8', iris='#1e1e1e', band_d='#545218'),
   {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False, 'ears': False},
   {'front': [L(outline([(8, 80), (2, 44), (14, 12), (50, -2), (86, 12), (98, 44), (94, 80), (80, 98), (50, 104), (20, 98)]), 'mid', 'f'),
              *[strand([(4, y), (50, y + 6), (96, y)], 'band_d', 'f', 1.2) for y in (12, 26, 40, 84)],
              L(outline([(26, 62), (52, 58), (54, 80), (28, 80)]), 'skin', 'f', ln=True),
              L(ell(42, 70, 4.6, 5.6), WHITE, 'f', False), L(ell(43, 71, 3, 4), BLACK, 'f', False), L([(34, 64), (50, 64)], OUTC, 'f', False, False, 2.0)],
    'side': [L(outline([(90, 50), (92, 26), (80, 4), (50, -6), (20, 2), (4, 26), (0, 60), (6, 90), (30, 104), (60, 102), (82, 92), (90, 76)]), 'mid', 'f'),
             *[strand([(0, y), (90, y + 4)], 'band_d', 'f', 1.2) for y in (14, 30, 48, 86)]],
    'back': [L(outline([(8, 82), (2, 44), (14, 12), (50, -2), (86, 12), (98, 44), (94, 82), (76, 98), (50, 102), (24, 98)]), 'mid', 'f'),
             *[strand([(4, y), (50, y + 6), (96, y)], 'band_d', 'f', 1.2) for y in (14, 30, 48, 66, 84)]]})

# Kosaka (Bamber Shoot): señor de cara larga y mandíbula marcada; pelo naranja rojizo peinado hacia atrás en dos rollos a
# los lados de la cabeza; ojos de sueño y sonrisa
mk('bamber-shoot', 'normal', pal('#c0501e', SKIN, iris='#1e1e1e'),
   {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 100, 'face_front': LONG, 'nose': (50, 88, 3.8), 'hairline': (50, 30), 'eye_y': 76},
   slick(top=4, side=54, nape=82),
   {'front': [L(cloud(12, 46, 10, 16, 5)), L(cloud(88, 46, 10, 16, 5)),
              L([(30, 72), (42, 72)], OUTC, 'f', False, False, 2.2), L([(58, 72), (70, 72)], OUTC, 'f', False, False, 2.2),
              L([(28, 64), (42, 62)], 'mid', 'f', False, False, 2.4), L([(72, 64), (58, 62)], 'mid', 'f', False, False, 2.4)],
    'side': [L(cloud(22, 44, 16, 18, 5))],
    'back': [L(cloud(12, 48, 10, 16, 5)), L(cloud(88, 48, 10, 16, 5))]})

# Sakigake (Bambis Shakin): crío con la cabeza rapada y un penacho verde azulado de hojas en lo alto que le baja en punta
# por la frente; cejas verdes, ojos pequeños y sonrisa
mk('bambis-shakin', 'normal', pal('#4e8478', SKIN, iris='#1e1e1e'),
   {'eyes': 'dot', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
   {'front': [L(outline([(44, 20), (30, -6, 1), (44, 2), (46, -16, 1), (54, 0), (66, -12, 1), (62, 6), (78, 0, 1), (60, 20), (54, 40), (50, 56, 1), (46, 40)]), 'mid', 'f'),
              L(outline([(50, 0), (54, 30), (50, 54), (48, 30)]), 'shade', 'f', False)] + brows(66, 'mid', 3.6, 14, 0.5, 12),
    'side': [L(outline([(70, 20), (60, -8, 1), (70, -2), (76, -14, 1), (80, 4), (92, 0, 1), (84, 20), (84, 36), (74, 30)]), 'mid', 'f')] + brow_side(66, 'mid', 3.6),
    'back': [L(outline([(44, 24), (32, -4, 1), (44, 4), (50, -14, 1), (56, 4), (68, -4, 1), (56, 24)]), 'mid', 'f')]})

# Purin (Bane Marie): gordito de cara muy ancha; pelo rubio crema muy corto con dos moños enroscados a los lados como
# caracolas; ojos pequeños de pillo y sonrisa
mk('bane-marie', 'corpulento', pal('#ece2a8', SKIN, iris='#1e1e1e'),
   {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'face_front': CHUBBY, 'nose': (50, 88, 3.4), 'hairline': (54, 44), 'ear_out': 6, 'eye_y': 78},
   cap(top=14, side=54, nape=78, w=2),
   {'front': [L(ell(22, 30, 13, 12), ln=True), L(ell(78, 30, 13, 12), ln=True),
              L(quad((14, 30), (22, 18), (30, 30)) + quad((30, 30), (22, 36), (20, 28))[1:], 'shade', 'f', False, False, 1.4),
              L(quad((86, 30), (78, 18), (70, 30)) + quad((70, 30), (78, 36), (80, 28))[1:], 'shade', 'f', False, False, 1.4)],
    'side': [L(ell(54, 18, 13, 12))],
    'back': [L(ell(22, 30, 13, 12)), L(ell(78, 30, 13, 12))]})

# Mizuki (Bard Crooner): pelo naranja en casco con flequillo de mechones y puntas hacia fuera sobre las orejas; ojos
# redondos grandes, bigotes en las mejillas y sonrisa
mk('bard-crooner', 'normal', pal('#dc6e10', PALE, iris='#1e1e1e'),
   {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
   bowl(lo=66, fr_y=62, w=4, top=2, n=6, jag=8),
   {'front': [L(outline([(10, 62), (0, 70, 1), (12, 72)])), L(outline([(90, 62), (100, 70, 1), (88, 72)])),
              L([(24, 84), (30, 86)], OUTC, 'f', False, False, 1.0), L([(70, 86), (76, 84)], OUTC, 'f', False, False, 1.0)]})

# ---------------------------------------------------------------------------------------------------- hoja 8

# Ataru (Barry Lugh): pelo naranja peinado hacia arriba en dos alas onduladas a los lados de una raya en medio, con
# patillas; cejas naranjas enormes y ojos redondos
mk('barry-lugh', 'normal', pal('#d06e10', SKIN, iris='#1e1e1e'),
   {'eyes': 'round', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': (52, 36)},
   cap(top=10, side=66, nape=82, w=2),
   {'front': [L(outline([(50, 14), (36, 2), (14, 4), (-2, 14, 1), (12, 20), (16, 34), (40, 28)])), L(outline([(50, 14), (64, 2), (86, 4), (102, 14, 1), (88, 20), (84, 34), (60, 28)])),
              strand([(16, 12), (34, 10), (46, 18)], 'deep', 'f', 1.0), strand([(84, 12), (66, 10), (54, 18)], 'deep', 'f', 1.0)]
             + brows(64, 'mid', 6.0, 15, 0.0, 16),
    'side': [L(outline([(84, 28), (90, 10), (102, 6, 1), (92, 0), (70, -2), (50, 4), (60, 20)]))] + brow_side(64, 'mid', 6.0),
    'back': [L(outline([(50, 16), (36, 4), (14, 6), (-2, 16, 1), (12, 24), (40, 30)])), L(outline([(50, 16), (64, 4), (86, 6), (102, 16, 1), (88, 24), (60, 30)]))]})

# Shimosaka (Barry Sterr): señor de cara larga; pelo verde azulado ondulado con un tupé que cae hacia un lado sobre la
# frente y la nuca corta; ojos lilas afilados y media sonrisa
mk('barry-sterr', 'normal', pal('#4e8478', SKIN, iris='#7a6aa0'),
   {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'face_front': LONG, 'hairline': False},
   {'front': [L(outline([(14, 74), (8, 40), (18, 12), (46, 0), (76, 4), (94, 22), (96, 56), (90, 76), (84, 66), (84, 52), (18, 52)])),
              L(outline([(60, 4), (88, 16), (96, 50), (90, 72), (84, 54)]), 'shade', 'b', False),
              fr([(14, 52), (20, 26), (44, 12), (72, 14), (90, 30), (94, 56), (86, 66, 1), (80, 46), (64, 34), (50, 40), (36, 34), (24, 44)]),
              L(outline([(16, 62), (8, 74, 1), (18, 72)])), strand([(30, 22), (54, 18), (80, 28)], 'deep', 'f', 1.0)],
    'side': [L(outline([(56, 56), (66, 46), (86, 44), (96, 28), (88, 6), (60, -4), (30, 0), (8, 18), (2, 48), (10, 72), (24, 80), (36, 72), (44, 62)])),
             L(outline([(3, 46), (28, 48), (40, 62), (34, 72), (20, 78), (8, 68)]), 'shade', 'b', False)],
    'back': [L(outline([(14, 80), (8, 40), (18, 12), (50, 0), (82, 12), (94, 40), (88, 80), (50, 86)])),
             L(outline([(58, 4), (84, 14), (94, 42), (88, 78), (62, 84)]), 'shade', 'b', False)]})

# Takahashi (Barry Straw): melena de champiñón castaño dorado con flequillo largo de mechones hasta los ojos y la nuca
# corta; piel muy clara, ojos grandes oscuros
mk('barry-straw', 'normal', pal('#907842', PALE, iris='#3a3030'),
   {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
   bowl(lo=66, fr_y=66, w=6, top=0, n=5, jag=8, nape=82),
   F(strand([(36, 14), (30, 40)], 'deep', 'f', 1.0), strand([(58, 12), (64, 40)], 'deep', 'f', 1.0)))
