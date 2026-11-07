"""Inazuma Legend Japan (cs-inazuma-legend-japan): los héroes de Inazuma Japón de mayores (la película Inazuma Eleven GO vs.
Danbor Senki W y Chrono Stone). Referencias: los renders 3D del equipo en la wiki ('(ILJ) <nombre> 3D') y los modelos de
adulto de la enciclopedia (los de Chrono Stone con el uniforme azul; Endou, Kidou y Sakuma, los de entrenador de GO). Los de
Victory Road no valen: son más mayores y con otros peinados (Kidou con trenza y perilla, Gouenji peinado hacia atrás).

Todos con cuerpo de adulto ('delgado', más alto; Kabeyama, 'corpulento'). Los que de mayores tienen otro peinado se dibujan de
nuevo; los demás parten de su dibujo de siempre con los cambios de la edad (gafas, patillas, sin bufanda ni capa)."""
import copy

from chars import CHARS, L, OUTC, ell, outline, pal, strand

T = 'cs-inazuma-legend-japan'
WHITE = (246, 246, 246, 255)


def adult(base, body='delgado', drop=(), face=None, extra=None):
    """Copia del dibujo de siempre como adulto: otro cuerpo, sin las capas de los colores de drop y con capas extra por vista."""
    ch = copy.deepcopy(CHARS[base])
    ch['body'] = body
    ch.pop('cape', None)
    for v in ('front', 'side', 'back'):
        flat = [l for it in ch[v] for l in (it if isinstance(it, list) else [it])]
        ch[v] = [l for l in flat if not (isinstance(l['c'], str) and l['c'] in drop)] + list((extra or {}).get(v, []))
    if face:
        ch['face'] = {**ch.get('face', {}), **face}
    return ch


# Endou: el mismo pelo de pinchos con la cinta naranja, pero con patillas largas que le bajan hasta la mandíbula
CHARS[f'{T}:mark-evans'] = adult('mark-evans', face={'eyes': 'normal', 'mouth': 'line', 'mouth_y': 94}, extra={
    'front': [L(outline([(14, 62), (20, 62), (20, 96), (17, 100, 1)]), 'mid', 'f'), L(outline([(86, 62), (80, 62), (80, 96), (83, 100, 1)]), 'mid', 'f')],
    'side': [L(outline([(56, 60), (62, 62), (62, 94), (58, 98, 1)]), 'mid', 'f')]})
# Kabeyama: el mismo casco de pelo verde, con perilla (ya la lleva)
CHARS[f'{T}:jack-wallside'] = adult('jack-wallside', body='corpulento')
# Tsunami: la melena rosa de pinchos de siempre, sin las gafas de bucear y con gafas negras de pasta
CHARS[f'{T}:hurley-kane'] = adult('hurley-kane', drop=('strap', 'rim', 'lens'), face={'glasses': OUTC, 'glasses_rect': True})
# Kidou: las rastas de siempre, más largas (le caen hasta los hombros), y gafas redondas de montura blanca con los cristales verdes
_kidou_lens = [L(ell(36, 76, 11, 10), 'rimw', 'f', ln=True), L(ell(64, 76, 11, 10), 'rimw', 'f', ln=True),
               L(ell(36, 76, 7.4, 6.8), 'lens', 'f', ln=True), L(ell(64, 76, 7.4, 6.8), 'lens', 'f', ln=True),
               L(ell(33, 73, 2.6, 2.2), 'lens_l', 'f', False), L(ell(61, 73, 2.6, 2.2), 'lens_l', 'f', False)]
CHARS[f'{T}:jude-sharp'] = adult('jude-sharp', drop=('strap', 'rim', 'lens', 'lens_l'), extra={
    'front': [L(outline([(12, 50), (2, 80), (4, 118, 1), (16, 104), (22, 116, 1), (24, 86), (20, 60)]), 'mid', 'b'),
              L(outline([(88, 50), (98, 80), (96, 118, 1), (84, 104), (78, 116, 1), (76, 86), (80, 60)]), 'mid', 'b')] + _kidou_lens,
    'side': [L(outline([(20, 60), (6, 90), (8, 124, 1), (20, 108), (28, 122, 1), (34, 92), (40, 70)]), 'mid', 'b'),
             L(ell(84, 76, 6, 9.4), 'rimw', 'f', ln=True), L(ell(85, 76, 3.6, 6.4), 'lens', 'f', ln=True)],
    'back': [L(outline([(8, 60), (2, 96), (6, 122, 1), (20, 110), (34, 124, 1), (50, 112), (66, 124, 1), (80, 110), (94, 122, 1), (98, 96), (92, 60)]), 'mid', 'b')]})
CHARS[f'{T}:jude-sharp']['pal'] = {**CHARS[f'{T}:jude-sharp']['pal'], 'rimw': WHITE}
CHARS[f'{T}:jude-sharp']['face'] = {**CHARS[f'{T}:jude-sharp']['face'], 'eyes': 'none'}
# Fubuki: el pelo lila de mechones en punta de siempre, sin la bufanda
CHARS[f'{T}:shawn-froste'] = adult('shawn-froste', drop=('scarf', 'scarf_d'))
# Gouenji y Sakuma: el mismo peinado de mayores (los pinchos de punta; la melena larga con el parche)
CHARS[f'{T}:axel-blaze'] = adult('axel-blaze')
CHARS[f'{T}:david-samford'] = adult('david-samford')
# Hiroto: la melena roja revuelta de Inazuma Japón (en el equipo no lleva gafas)
CHARS[f'{T}:xavier-foster'] = adult('ie3:xavier-foster')

# Kazemaru de mayor: ya no lleva la coleta alta; el pelo azul grisáceo, largo y liso, le tapa el ojo derecho con el flequillo
# y va recogido bajo en la nuca con una goma roja, del que cuelgan mechones hasta la espalda
CHARS[f'{T}:nathan-swift'] = {
    'body': 'delgado', 'pal': pal('#6a96a2', '#f6cfa8', iris='#7a4a22', band='#d84a2a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(14, 90), (4, 60), (6, 26), (24, 4), (50, -4), (76, 4), (94, 26), (96, 60), (86, 92), (82, 64), (18, 64)])),
              L(outline([(60, 2), (86, 14), (96, 44), (90, 84), (80, 50)]), 'shade', 'b', False),
              L(outline([(88, 84), (90, 52), (78, 24), (54, 12), (30, 16), (14, 36), (10, 70), (16, 56), (22, 66, 1), (28, 46), (40, 40), (50, 54), (54, 88, 1),
                         (60, 70), (66, 90, 1), (74, 66), (82, 96, 1)]), 'mid', 'f'),
              L(outline([(12, 60), (6, 100), (10, 112, 1), (20, 96), (20, 66)]), 'mid', 'f'),
              L(outline([(60, 24), (80, 30), (88, 50), (76, 46)]), 'shade', 'f', False), strand([(70, 22), (78, 60)], 'shade', 'f', 1.0)],
    'side': [L(outline([(54, 62), (58, 50), (80, 48), (92, 36), (88, 14), (66, -2), (36, -2), (14, 12), (4, 36), (4, 62), (14, 80), (10, 112, 1), (22, 96),
                        (26, 114, 1), (32, 92), (46, 76)])),
             L(outline([(6, 40), (28, 46), (30, 90), (12, 84)]), 'shade', 'b', False),
             L(ell(18, 74, 4, 3), 'band', 'f', ln=True),
             L(outline([(62, 4), (88, 16), (96, 42), (94, 70, 1), (86, 54), (82, 66, 1), (76, 44), (64, 30)]), 'mid', 'f')],
    'back': [L(outline([(12, 70), (6, 36), (20, 10), (50, 0), (80, 10), (94, 36), (88, 70), (64, 82), (36, 82)])),
             L(outline([(56, 4), (86, 16), (94, 44), (86, 70), (62, 80)]), 'shade', 'b', False),
             L(outline([(36, 78), (64, 78), (66, 98), (62, 120, 1), (56, 104), (50, 124, 1), (44, 104), (38, 120, 1), (34, 98)]), 'mid', 'f'),
             L(outline([(36, 76), (64, 76), (64, 82), (36, 82)]), 'band', 'f', ln=True),
             strand([(50, 4), (50, 74)], 'deep', 'b', 1.0), strand([(30, 20), (36, 74)], 'deep', 'b', 1.0), strand([(70, 20), (64, 74)], 'deep', 'b', 1.0)],
}

# Fudou de mayor: ya no lleva la cresta; melena castaña larga y en capas hasta los hombros, con pinchos de punta arriba,
# mechones que le caen por la frente y entre los ojos, y puntas abiertas por detrás; ojos verdes afilados
CHARS[f'{T}:caleb-stonewall'] = {
    'body': 'delgado', 'pal': pal('#5a3a1e', '#f8d4ac', iris='#3a6a5a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(14, 106), (0, 112, 1), (4, 92), (-6, 70, 1), (6, 62), (2, 34), (-8, 22, 1), (12, 18), (18, -6, 1), (32, 6), (44, -18, 1), (54, 2),
                         (68, -12, 1), (72, 6), (92, 2, 1), (90, 22), (106, 26, 1), (96, 40), (98, 64), (108, 74, 1), (96, 86), (100, 112, 1), (86, 104), (82, 66),
                         (18, 66)])),
              L(outline([(60, 2), (88, 14), (98, 44), (96, 96), (84, 60)]), 'shade', 'b', False),
              L(outline([(12, 74), (12, 44), (24, 22), (48, 14), (72, 20), (86, 38), (90, 74), (82, 58), (76, 66, 1), (70, 48), (60, 56, 1), (56, 40), (48, 84, 1),
                         (42, 52), (36, 66, 1), (28, 48), (20, 70, 1)]), 'mid', 'f'),
              L(outline([(56, 18), (78, 26), (86, 48), (72, 42)]), 'shade', 'f', False)],
    'side': [L(outline([(54, 62), (58, 50), (80, 50), (94, 36), (92, 16), (100, 2, 1), (78, 2), (70, -16, 1), (56, -2), (36, -16, 1), (28, 2), (4, -2, 1), (12, 16),
                        (-10, 26, 1), (4, 40), (-8, 60, 1), (6, 66), (0, 92, 1), (14, 86), (12, 110, 1), (26, 96), (36, 108, 1), (42, 88), (48, 76)])),
             L(outline([(4, 40), (26, 46), (32, 96), (12, 90)]), 'shade', 'b', False),
             L(outline([(64, 4), (90, 18), (96, 44), (94, 68, 1), (86, 52), (82, 64, 1), (76, 44), (64, 30)]), 'mid', 'f')],
    'back': [L(outline([(14, 106), (-2, 112, 1), (4, 90), (-8, 66, 1), (6, 56), (0, 30), (-8, 18, 1), (14, 16), (20, -8, 1), (34, 6), (46, -18, 1), (56, 4),
                        (70, -12, 1), (74, 6), (92, 0, 1), (90, 22), (108, 30, 1), (96, 46), (106, 70, 1), (96, 86), (102, 112, 1), (84, 104), (72, 116, 1),
                        (62, 104), (50, 118, 1), (38, 104), (28, 116, 1)])),
             L(outline([(56, 4), (88, 16), (98, 50), (96, 104), (70, 110), (72, 50)]), 'shade', 'b', False),
             strand([(28, 30), (22, 70), (26, 104)], 'deep', 'b', 1.0), strand([(50, 20), (50, 108)], 'deep', 'b', 1.0),
             strand([(72, 30), (78, 70), (74, 104)], 'deep', 'b', 1.0)],
}

# Someoka de mayor: el pelo rosa corto en pinchos de punta como una llama, más bajo por los lados; piel morena, cejas
# fruncidas y un lunar bajo el ojo
CHARS[f'{T}:kevin-dragonfly'] = {
    'body': 'delgado', 'pal': pal('#e88a90', '#b47a4e', iris='#1e1414', shade='#c4686e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': [(12, 60), (20, 46), (36, 40), (50, 46), (64, 40), (80, 46), (88, 60)]},
    'front': [L(outline([(14, 62), (12, 34), (18, 14), (24, -2, 1), (32, 8), (40, -10, 1), (48, 4), (56, -12, 1), (62, 4), (72, -6, 1), (76, 10), (84, 2, 1),
                         (86, 24), (88, 62), (78, 52), (22, 52)])),
              L(outline([(60, 4), (80, 12), (88, 40), (84, 60), (74, 38)]), 'shade', 'b', False),
              L(outline([(30, 10), (36, 2), (40, 24)]), 'light', 'b', False), L(outline([(52, 6), (58, 0), (60, 22)]), 'light', 'b', False),
              L(ell(70, 86, 1.6, 1.6), OUTC, 'f', False)],
    'side': [L(outline([(56, 52), (64, 44), (80, 40), (88, 26), (96, 12, 1), (78, 10), (74, -8, 1), (60, 2), (46, -12, 1), (40, 4), (22, -4, 1), (22, 12), (4, 10, 1),
                        (10, 28), (6, 52), (16, 70), (30, 64), (44, 58)])),
             L(outline([(8, 30), (26, 36), (26, 62), (12, 58)]), 'shade', 'b', False)],
    'back': [L(outline([(14, 76), (10, 40), (16, 14), (24, -4, 1), (32, 8), (40, -12, 1), (48, 4), (56, -12, 1), (62, 4), (74, -6, 1), (78, 10), (86, 2, 1),
                        (88, 40), (86, 76), (70, 70), (50, 76), (30, 70)])),
             L(outline([(56, 4), (82, 14), (88, 46), (84, 72), (64, 70)]), 'shade', 'b', False),
             L(outline([(34, 12), (40, 2), (46, 24), (40, 30)]), 'shade', 'b', False), L(outline([(56, 12), (62, 2), (66, 24), (60, 30)]), 'shade', 'b', False)],
}
