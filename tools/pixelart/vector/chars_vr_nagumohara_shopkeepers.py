"""Vendedores de South Cirrus (vr-nagumohara-shopkeepers, Nagumohara Shopkeepers): los dueños de las tiendas del pueblo de
Nagumohara (adultos y abuelos), con sus modelos 3D de Inazuma Eleven: Victory Road (英雄たちのヴィクトリーロード) como
referencia. No comparten ningún jugador con vr-nagumohara; cada uno tiene un solo modelo y ningún id coge por prefijo el
dibujo de otro personaje."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from chars_vr_keizen_arashiyama import WHITE, cloud, fr, lash_side, lashes
from chars_vr_meiran_gakuin import back_cap, back_shade, bangs, cap, cap_shade, side_cap
from chars_vr_nagumohara import blush
from heads import quad  # noqa: F401

GOLD = (224, 172, 48, 255)


def wrinkles(y=84):
    """Arrugas de mayor: rayitas en las mejillas y bajo los ojos."""
    return [L(quad((27, y), (30, y + 5), (29, y + 10)), OUTC, 'f', False, False, 1.0), L(quad((73, y), (70, y + 5), (71, y + 10)), OUTC, 'f', False, False, 1.0),
            L(quad((30, 80), (34, 82), (40, 81)), OUTC, 'f', False, False, 0.9), L(quad((70, 80), (66, 82), (60, 81)), OUTC, 'f', False, False, 0.9)]


# Terra Hillcroft (Miyazono Masako): media melena castaño rojizo ahuecada y redonda, con raya en medio, que se curva hacia
# dentro bajo las orejas; cejas marcadas, ojos castaño verdoso con pestañas, pendientes morados largos y una sonrisa
CHARS['terra-hillcroft'] = {
    'body': 'chica', 'pal': pal('#8a4848', '#fce4d4', iris='#7a7046', shade='#6e3636', deep='#522626', ear='#7a4ab0'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(12, 76), (16, 58), (24, 46), (40, 40), (50, 44), (60, 40), (76, 46), (84, 58), (88, 76)]},
    'front': [L(outline([(16, 60), (2, 74), (2, 90), (14, 96), (20, 86)])), L(outline([(84, 60), (98, 74), (98, 90), (86, 96), (80, 86)])),
              L(outline([(12, 78), (2, 50), (10, 20), (30, 4), (50, 0), (70, 4), (90, 20), (98, 50), (88, 78), (82, 60), (18, 60)])),
              L(outline([(60, 4), (86, 16), (98, 48), (90, 74), (80, 44)]), 'shade', 'b', False), strand([(50, 2), (50, 40)], 'deep', 'b', 1.2),
              L(outline([(16, 84), (18, 84), (18, 96), (16, 96)]), 'ear', 'f', ln=True), L(outline([(82, 84), (84, 84), (84, 96), (82, 96)]), 'ear', 'f', ln=True)] + lashes(dx=7.6),
    'side': [L(outline([(54, 62), (58, 50), (80, 42), (90, 28), (88, 10), (66, -4), (36, -4), (12, 8), (-2, 36), (-2, 66), (10, 84), (28, 90), (40, 86), (48, 72)])),
             L(outline([(0, 40), (24, 46), (30, 84), (10, 84)]), 'shade', 'b', False),
             L(outline([(46, 82), (48, 82), (48, 94), (46, 94)]), 'ear', 'f', ln=True)] + lash_side(),
    'back': [L(outline([(10, 80), (-2, 50), (8, 18), (30, 2), (50, -2), (70, 2), (92, 18), (102, 50), (90, 80), (70, 90), (50, 86), (30, 90)])),
             L(outline([(58, 0), (86, 14), (100, 48), (90, 80), (66, 88)]), 'shade', 'b', False),
             L(outline([(14, 84), (16, 84), (16, 96), (14, 96)]), 'ear', 'f', ln=True), L(outline([(84, 84), (86, 84), (86, 96), (84, 96)]), 'ear', 'f', ln=True)],
}

# Marlin Sharkey (Samekawa Hayate): pescadero mayor de piel curtida; pelo verde petróleo muy oscuro en pinchos hacia
# arriba, con un hachimaki blanco retorcido como una cuerda alrededor de la frente y el nudo detrás; ojos claros
# entornados y fruncidos, nariz grande, arrugas y barba de tres días
CHARS['marlin-sharkey'] = {
    'body': 'normal', 'pal': pal('#2a4a58', '#c88a5e', iris='#9aa0c8', shade='#1e3842', deep='#142830', band='#f0eeea', band_d='#bab4b0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'nose': (50, 86, 4), 'eye_y': 74, 'hairline': False},
    'front': [L(outline([(16, 64), (12, 40), (4, 24, 1), (20, 24), (14, 6, 1), (32, 14), (34, -8, 1), (46, 8), (56, -12, 1), (60, 6), (76, -4, 1), (74, 14), (92, 12, 1),
                         (86, 26), (100, 34, 1), (88, 42), (86, 64), (50, 60)])),
              L(outline([(58, 0), (76, -2), (74, 16), (90, 18), (88, 40), (76, 30)]), 'shade', 'b', False),
              L(outline([(8, 64), (10, 50), (50, 44), (90, 50), (92, 64), (50, 60)]), 'band', 'f', ln=True),
              L(quad((14, 52), (20, 62), (26, 52)), 'band_d', 'f', False, False, 1.4), L(quad((30, 50), (36, 60), (42, 48)), 'band_d', 'f', False, False, 1.4),
              L(quad((48, 48), (54, 58), (60, 48)), 'band_d', 'f', False, False, 1.4), L(quad((64, 48), (70, 60), (76, 50)), 'band_d', 'f', False, False, 1.4),
              L(quad((80, 52), (84, 62), (90, 54)), 'band_d', 'f', False, False, 1.4)] + wrinkles(86),
    'side': [L(outline([(54, 56), (60, 46), (82, 42), (96, 30), (108, 22, 1), (92, 14), (100, -2, 1), (80, 4), (78, -16, 1), (62, 0), (44, -14, 1), (36, 4), (14, -2, 1),
                        (16, 18), (-4, 24, 1), (8, 36), (6, 60), (20, 78), (38, 76), (48, 66)])),
             L(outline([(4, 54), (8, 40), (50, 40), (92, 44), (94, 58), (50, 56)]), 'band', 'f', ln=True),
             L(outline([(8, 46), (-14, 40), (-20, 54), (-8, 56)]), 'band', 'f', ln=True), L(outline([(6, 50), (-10, 64), (-4, 72), (8, 58)]), 'band', 'f', ln=True)],
    'back': [L(outline([(14, 78), (10, 40), (2, 26, 1), (18, 24), (12, 6, 1), (30, 14), (32, -8, 1), (46, 8), (56, -12, 1), (62, 6), (78, -4, 1), (76, 14), (94, 12, 1),
                        (88, 26), (100, 34, 1), (90, 42), (86, 78), (50, 84)])),
             L(outline([(58, 0), (78, -2), (76, 16), (92, 16), (90, 44), (86, 76), (64, 82)]), 'shade', 'b', False),
             L(outline([(8, 58), (10, 44), (50, 50), (90, 44), (92, 58), (50, 64)]), 'band', 'f', ln=True),
             L(outline([(44, 52), (30, 50), (28, 64), (42, 66), (40, 78), (52, 80), (56, 64)]), 'band', 'f', ln=True)],
}

# Mirina Mackrell (Saba Mirin): pelo castaño oscuro ahuecado en un tupé redondo, con dos mechones que le caen en curva por
# la frente, y una coleta baja larga atada con una goma roja; cejas finas, ojos azules y sonrisa
CHARS['mirina-mackrell'] = {
    'body': 'chica', 'pal': pal('#5a3628', '#fce4d4', iris='#3a5a9a', shade='#46281e', deep='#321c14', tie='#a82a2a'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(12, 76), (16, 60), (24, 52), (36, 48), (44, 56), (50, 48), (56, 56), (64, 48), (76, 52), (84, 60), (88, 76)]},
    'front': [L(outline([(12, 84), (4, 50), (8, 22), (28, 4), (50, -2), (72, 4), (92, 22), (96, 50), (88, 84), (82, 62), (18, 62)])),
              L(outline([(60, 2), (86, 16), (96, 48), (90, 80), (80, 44)]), 'shade', 'b', False),
              fr([(26, 52), (34, 44), (46, 46), (42, 54), (36, 62, 1), (34, 52)]), fr([(74, 52), (66, 44), (54, 46), (58, 54), (64, 62, 1), (66, 52)])] + lashes(),
    'side': [L(rope((24, 80), (6, 96), (-6, 118), 8)), L(ell(22, 82, 4, 4), 'tie', 'b', ln=True),
             L(outline([(54, 62), (58, 50), (80, 42), (92, 26), (90, 8), (68, -6), (36, -6), (12, 6), (0, 34), (2, 66), (14, 82), (28, 88), (42, 84), (48, 72)])),
             L(outline([(70, 12), (92, 22), (94, 44), (80, 52), (76, 34)]), 'mid', 'f'),
             L(outline([(4, 40), (24, 46), (28, 80), (10, 78)]), 'shade', 'b', False)] + lash_side(),
    'back': [L(outline([(10, 84), (4, 50), (8, 20), (28, 2), (50, -4), (72, 2), (92, 20), (96, 50), (90, 84), (50, 90)])),
             back_shade(-2, 88),
             L(rope((50, 84), (46, 100), (48, 120), 8)), L(ell(50, 86, 5, 3), 'tie', 'f', ln=True)],
}

# Alvaro Ventura (Hayakaze Toshinobu): piel morena; gorra turquesa del revés con un mechón rubio que asoma por el hueco de
# delante, pelo rubio hasta el cuello por detrás y patillas largas; cejas rubias, ojos claros y sonrisa enorme de dientes
CHARS['alvaro-ventura'] = {
    'body': 'normal', 'pal': pal('#f0b44a', '#a06a46', iris='#4a5a9a', shade='#cc9032', deep='#a87020', hat='#2ab4c8', hat_d='#1e8a9a'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 95, 'big_ears': 2, 'ear_out': 3,
             'hairline': [(12, 70), (16, 58), (30, 54), (50, 56), (70, 54), (84, 58), (88, 70)]},
    'front': [L(outline([(16, 62), (8, 90), (14, 104, 1), (20, 88)])), L(outline([(84, 62), (92, 90), (86, 104, 1), (80, 88)])),
              L(outline([(14, 70), (12, 52), (88, 52), (86, 70), (80, 60), (20, 60)])),
              L(outline([(10, 54), (10, 30), (24, 10), (50, 2), (76, 10), (90, 30), (90, 54), (50, 50)]), 'hat', 'f', ln=True),
              L(outline([(60, 6), (78, 14), (88, 34), (88, 52), (76, 50), (74, 28)]), 'hat_d', 'f', False),
              L(quad((10, 52), (50, 44), (90, 52)), 'hat_d', 'f', False, False, 2.0),
              L(outline([(36, 52), (34, 30), (42, 14), (52, 8, 1), (48, 24), (60, 20, 1), (54, 36), (58, 52)]), 'mid', 'f', ln=True),
              L(outline([(26, 64), (32, 60), (44, 64), (42, 68), (30, 68)]), 'mid', 'f', ln=True), L(outline([(74, 64), (68, 60), (56, 64), (58, 68), (70, 68)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(54, 62), (58, 54), (84, 54), (88, 40), (40, 40), (14, 44), (2, 70), (6, 96, 1), (20, 84), (30, 96, 1), (40, 80), (48, 70)])),
             L(outline([(14, 52), (12, 30), (30, 10), (56, 6), (82, 14), (92, 34), (90, 48), (50, 46)]), 'hat', 'f', ln=True),
             L(outline([(16, 46), (2, 50), (-20, 60, 1), (0, 40), (16, 38)]), 'hat_d', 'f', ln=True),
             L(outline([(88, 22), (98, 12, 1), (96, 26), (106, 30, 1), (92, 34)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(14, 60), (10, 80), (14, 100, 1), (26, 88), (38, 102, 1), (50, 90), (62, 102, 1), (74, 88), (86, 100, 1), (90, 80), (86, 60)])),
             L(outline([(10, 62), (10, 30), (24, 10), (50, 2), (76, 10), (90, 30), (90, 62), (50, 58)]), 'hat', 'f', ln=True),
             L(outline([(28, 62), (30, 48), (70, 48), (72, 62)]), 'hat_d', 'f', False),
             L(outline([(40, 50), (50, 44), (60, 50), (50, 56)]), 'mid', 'f', ln=True)],
}

# Yelena Poplawska (Yumoto Tsukimi, capitana): pañuelo rojo atado en la cabeza como un triángulo, con la punta hacia atrás
# y hacia los lados; por debajo, pelo castaño corto hasta la nuca con las patillas largas; ojos marrones y una sonrisa
CHARS['yelena-poplawska'] = {
    'body': 'chica', 'pal': pal('#5a3a26', '#fce0c8', iris='#5a3a22', shade='#462c1c', deep='#321e12', cloth='#b8263a', cloth_d='#901c2c'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(16, 52), (8, 80), (12, 100, 1), (22, 84), (24, 66)])), L(outline([(84, 52), (92, 80), (88, 100, 1), (78, 84), (76, 66)])),
              L(outline([(12, 66), (12, 44), (88, 44), (88, 66), (80, 56), (20, 56)])),
              L(outline([(0, 56, 1), (14, 30), (32, 12), (50, 6), (68, 12), (86, 30), (100, 56, 1), (80, 52), (50, 50), (20, 52)]), 'cloth', 'f', ln=True),
              L(outline([(62, 10), (82, 26), (96, 52), (80, 50), (74, 30)]), 'cloth_d', 'f', False)] + lashes(),
    'side': [L(outline([(54, 62), (58, 52), (80, 50), (84, 40), (40, 30), (14, 36), (4, 60), (8, 82), (24, 92), (40, 88), (48, 74)])),
             L(outline([(86, 50), (90, 26), (70, 6), (40, 2), (14, 14), (-20, 30, 1), (0, 40), (20, 44), (50, 42), (70, 46)]), 'cloth', 'f', ln=True),
             L(outline([(14, 18), (-20, 30, 1), (0, 40), (18, 40)]), 'cloth_d', 'f', False)] + lash_side(),
    'back': [L(outline([(14, 60), (10, 80), (16, 98, 1), (30, 88), (40, 98, 1), (50, 88), (60, 98, 1), (70, 88), (84, 98, 1), (90, 80), (86, 60)])),
             L(outline([(-8, 40, 1), (10, 20), (30, 8), (50, 4), (70, 8), (90, 20), (108, 40, 1), (86, 52), (50, 70, 1), (14, 52)]), 'cloth', 'f', ln=True),
             L(outline([(50, 20), (86, 30), (86, 50), (50, 68)]), 'cloth_d', 'f', False)],
}

# Lorcan Oxfield (Ushida Takeomi): grandote; pelo morado muy oscuro abundante y despeinado, unido a una barba enorme y
# un bigote grueso que le tapan media cara; piel morena, ojos pequeños castaños y nariz ancha
CHARS['lorcan-oxfield'] = {
    'body': 'corpulento', 'pal': pal('#3e3248', '#c08a62', iris='#5a3a2a', shade='#2e2436', deep='#201826'),
    'face': {'eyes': 'round', 'brows': True, 'mouth': 'none', 'nose': (50, 84, 4.4), 'hairline': [(10, 70), (16, 56), (30, 52), (50, 54), (70, 52), (84, 56), (90, 70)]},
    'front': [L(outline([(14, 72), (2, 66, 1), (6, 44), (2, 26), (16, 6), (40, -6), (60, -6), (84, 6), (98, 26), (94, 44), (98, 66, 1), (86, 72), (82, 58), (18, 58)])),
              L(outline([(60, -2), (86, 8), (96, 36), (92, 62), (80, 40)]), 'shade', 'b', False),
              L(outline([(14, 70), (20, 70), (24, 92), (36, 104), (50, 106), (64, 104), (76, 92), (80, 70), (86, 70), (88, 100), (78, 118), (60, 126), (50, 128), (40, 126),
                         (22, 118), (12, 100)]), 'mid', 'f', ln=True),
              L(outline([(28, 94), (40, 88), (50, 92), (60, 88), (72, 94), (66, 100), (50, 98), (34, 100)]), 'mid', 'f', ln=True),
              L(quad((40, 104), (50, 108), (60, 104)), (150, 70, 70, 255), 'f', False, False, 1.4)],
    'side': [L(outline([(54, 60), (58, 50), (82, 42), (92, 28), (88, 8), (66, -6), (36, -6), (12, 6), (-2, 34), (0, 62), (8, 82), (26, 90), (40, 84), (48, 70)])),
             L(outline([(4, 36), (24, 42), (28, 80), (10, 78)]), 'shade', 'b', False),
             L(outline([(50, 70), (58, 72), (62, 92), (72, 102), (86, 96), (92, 90), (96, 100), (90, 116), (72, 124), (56, 118), (48, 96)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(10, 84), (0, 50), (6, 20), (30, 0), (50, -6), (70, 0), (94, 20), (100, 50), (90, 84), (50, 92)])),
             back_shade(-4, 88),
             L(outline([(6, 88), (14, 106), (24, 100), (8, 84)]), 'mid', 'b', ln=True), L(outline([(94, 88), (86, 106), (76, 100), (92, 84)]), 'mid', 'b', ln=True)],
}

# Cinnamon Dougherty (Kitano Kaori): pelo castaño ahuecado con raya a un lado que deja la frente en arco, y los lados
# recogidos en dos rollos grandes junto a las orejas; gafas marrones redondeadas, ojos ámbar y sonrisa
CHARS['cinnamon-dougherty'] = {
    'body': 'chica', 'pal': pal('#a0682e', '#fce4d4', iris='#b07a1e', shade='#82521e', deep='#643e14', roll='#86561e'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 95, 'glasses': (120, 70, 40, 255), 'glasses_rect': True,
             'hairline': [(12, 70), (16, 54), (26, 42), (34, 32), (46, 28), (58, 32), (68, 42), (78, 52), (88, 70)]},
    'front': [L(cloud(8, 74, 14, 14, 5, 0.3), 'roll'), L(cloud(92, 74, 14, 14, 5, 0.6), 'roll'),
              L(outline([(12, 70), (8, 42), (18, 16), (40, 2), (62, 2), (82, 16), (92, 42), (88, 70), (82, 56), (18, 56)])),
              L(outline([(58, 4), (82, 18), (92, 46), (88, 66), (78, 44)]), 'shade', 'b', False),
              fr([(12, 64), (14, 42), (24, 30), (34, 34), (26, 46), (18, 66, 1)]), fr([(88, 62), (84, 42), (70, 32), (60, 32), (72, 44), (80, 66, 1)])],
    'side': [L(cloud(16, 70, 22, 16, 5, 0.3), 'roll'),
             L(outline([(54, 62), (58, 50), (80, 42), (90, 28), (88, 10), (66, -4), (36, -4), (12, 8), (0, 36), (4, 58), (20, 62), (40, 60), (48, 66)])),
             L(outline([(68, 8), (90, 20), (94, 40), (82, 42), (78, 26)]), 'mid', 'f')],
    'back': [L(outline([(12, 74), (8, 42), (18, 16), (40, 2), (62, 2), (82, 16), (92, 42), (88, 74), (50, 80)])),
             back_shade(2, 76), L(cloud(50, 80, 50, 16, 7, 0.2), 'roll'),
             strand([(30, 72), (30, 92)], 'deep', 'f', 1.0), strand([(50, 72), (50, 94)], 'deep', 'f', 1.0), strand([(70, 72), (70, 92)], 'deep', 'f', 1.0)],
}

# Primavera Bluefield (Aota Harumi): abuelita bajita; pelo gris claro en una melena ahuecada en forma de campana, con
# flequillo recto y las puntas más oscuras; dos horquillas en forma de hueso junto a los ojos, ojos granate y una sonrisa
CHARS['primavera-bluefield'] = {
    'body': 'bajito', 'pal': pal('#c8c8bc', '#fce4d4', iris='#8a2a4a', shade='#a8a69a', deep='#8a8478', tip='#8a7a74', clip='#a89a6a'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(10, 96), (-6, 90), (0, 60), (10, 24), (30, 6), (50, 0), (70, 6), (90, 24), (100, 60), (106, 90), (90, 96), (82, 80), (82, 62), (18, 62), (18, 80)])),
              L(outline([(-6, 90), (0, 76), (18, 80), (10, 96)]), 'tip', 'b', False), L(outline([(106, 90), (100, 76), (82, 80), (90, 96)]), 'tip', 'b', False),
              L(outline([(60, 4), (84, 14), (98, 50), (100, 76), (84, 64)]), 'shade', 'b', False),
              bangs(62, 16, 84, 6, 28, 'mid', 0),
              L(outline([(26, 78), (32, 74), (34, 80), (28, 84)]), 'clip', 'f', ln=True), L(outline([(74, 78), (68, 74), (66, 80), (72, 84)]), 'clip', 'f', ln=True)]
             + blush(88, 26, 4),
    'side': [L(outline([(54, 66), (58, 54), (72, 52), (82, 60), (88, 50), (90, 24), (76, 2), (50, -6), (20, 2), (0, 30), (-8, 70), (-4, 96), (30, 98), (44, 92), (48, 80)])),
             L(outline([(-8, 72), (24, 76), (40, 92), (30, 98), (-4, 96)]), 'tip', 'b', False),
             L(outline([(78, 76), (84, 72), (86, 80), (80, 82)]), 'clip', 'f', ln=True)],
    'back': [L(outline([(-6, 92), (0, 60), (10, 22), (30, 4), (50, -2), (70, 4), (90, 22), (100, 60), (106, 92), (50, 100)])),
             L(outline([(-2, 70), (50, 74), (102, 70), (106, 92), (50, 100), (-6, 92)]), 'tip', 'b', False),
             strand([(50, 0), (50, 70)], 'deep', 'b', 1.0)],
}

# Gibson Forte (Otode Takehito): adulto; media melena castaña ondulada con raya en medio, más oscura en las puntas que se
# abren a los lados; cejas gruesas y arqueadas, ojos entornados ámbar, nariz larga, bigote fino y perilla
CHARS['gibson-forte'] = {
    'body': 'normal', 'pal': pal('#5a3a26', '#fcd8bc', iris='#a8862a', shade='#46281a', deep='#2e1a10'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 97, 'nose': (50, 86, 3.4),
             'hairline': [(12, 76), (16, 56), (26, 44), (40, 38), (50, 34), (60, 38), (74, 44), (84, 56), (88, 76)]},
    'front': [L(outline([(16, 58), (-2, 78), (-12, 92, 1), (4, 92), (8, 102, 1), (22, 90)])), L(outline([(84, 58), (102, 78), (112, 92, 1), (96, 92), (92, 102, 1), (78, 90)])),
              cap(0, 44, 62, 6), cap_shade(0), strand([(50, 2), (50, 34)], 'deep', 'b', 1.2),
              fr([(48, 34), (36, 42), (28, 56), (26, 72, 1), (34, 54)]),
              L(quad((42, 92), (50, 90), (58, 92)), 'mid', 'f', False, False, 1.4),
              L(outline([(46, 104), (54, 104), (50, 112, 1)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(54, 62), (58, 50), (80, 42), (90, 28), (86, 10), (66, -4), (36, -4), (12, 8), (-2, 36), (-4, 66), (-12, 84, 1), (6, 84), (10, 98, 1), (24, 88),
                        (40, 84), (48, 72)])),
             L(outline([(4, 40), (24, 46), (28, 82), (6, 82)]), 'shade', 'b', False),
             L(outline([(84, 104), (88, 104), (86, 112, 1)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(8, 80), (2, 42), (14, 14), (40, -2), (60, -2), (86, 14), (98, 42), (92, 80), (110, 94, 1), (90, 92), (84, 102, 1), (70, 92), (50, 96), (30, 92),
                        (16, 102, 1), (10, 92), (-10, 94, 1)])),
             back_shade(-2, 90)],
}

# Love Stirling (Ai Tsumugu): media melena rosa malva ondulada hasta el cuello, con flequillo de lado en mechones; ojos
# granate con mucho delineado y pestañas, y una sonrisa tranquila
CHARS['love-stirling'] = {
    'body': 'chica', 'pal': pal('#b86a98', '#fce8dc', iris='#9a3a5a', shade='#985480', deep='#784064'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(12, 76), (16, 58), (26, 48), (40, 46), (56, 44), (72, 48), (84, 58), (88, 76)]},
    'front': [L(outline([(16, 58), (4, 80), (8, 94), (2, 104, 1), (16, 100), (22, 104, 1), (24, 86)])), L(outline([(84, 58), (96, 80), (92, 94), (98, 104, 1), (84, 100), (78, 104, 1), (76, 86)])),
              cap(2, 44, 62, 4), cap_shade(2),
              fr([(12, 64), (14, 42), (28, 30), (50, 26), (66, 32), (60, 42), (50, 50), (42, 64, 1), (40, 50), (30, 56), (22, 70, 1)])] + lashes(n=2),
    'side': [L(outline([(54, 62), (58, 50), (80, 42), (90, 28), (86, 12), (66, 0), (40, 0), (18, 10), (2, 36), (0, 66), (-6, 88), (2, 102, 1), (14, 94), (24, 104, 1),
                        (32, 92), (44, 84), (50, 72)])),
             L(outline([(4, 40), (26, 46), (30, 84), (8, 84)]), 'shade', 'b', False),
             L(outline([(68, 40), (86, 44), (88, 60, 1), (76, 54)]), 'mid', 'f')] + lash_side(),
    'back': [L(outline([(8, 84), (6, 42), (16, 16), (40, 2), (60, 2), (84, 16), (94, 42), (92, 84), (98, 102, 1), (82, 98), (70, 106, 1), (58, 96), (44, 106, 1), (32, 96),
                        (18, 104, 1), (2, 100, 1)])),
             back_shade(2, 92)],
}

# Sheila Threadwell (Ishiuri Kiri): señora mayor de pelo lila muy rizado y ahuecado, en una melena redonda de rizos; ojos
# azules con sombra lila, nariz respingona, labios rojos con una sonrisa pícara, arrugas y aros dorados en las orejas
CHARS['sheila-threadwell'] = {
    'body': 'chica', 'pal': pal('#c4a4cc', '#f8d4bc', iris='#3a6ab8', shade='#a484ac', deep='#84648c'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'lips', 'mouth_y': 96, 'nose': (50, 86, 3), 'hairline': [(10, 74), (14, 56), (26, 42), (44, 38), (60, 34), (76, 44), (86, 56), (90, 74)]},
    'front': [L(cloud(50, 40, 58, 46, 10, 0.2)), L(cloud(10, 76, 12, 14, 4, 0.3)), L(cloud(90, 76, 12, 14, 4, 0.6)),
              L(cloud(66, 30, 26, 22, 6, 0.4), 'shade', 'b', False),
              L(ell(16, 92, 4, 5), GOLD, 'f', ln=True), L(ell(84, 92, 4, 5), GOLD, 'f', ln=True)] + wrinkles(88),
    'side': [L(cloud(40, 40, 52, 46, 10, 0.2)), L(cloud(20, 74, 18, 16, 5, 0.3), 'shade', 'b', False),
             L(ell(46, 88, 4, 5), GOLD, 'f', ln=True)],
    'back': [L(cloud(50, 44, 58, 50, 10, 0.2)), L(cloud(50, 80, 36, 14, 6, 0.3), 'shade', 'b', False)],
}

# He Liu (Ryuu Kaku): abuelo fornido; pelo gris verdoso recogido en un moño alto con un lazo amarillo, con las patillas en
# punta; cejas grises enormes y fruncidas, ojos naranjas afilados, una tirita en la nariz, arrugas y una perilla gris
CHARS['he-liu'] = {
    'body': 'corpulento', 'pal': pal('#6a6e62', '#f0aa7c', iris='#c8661e', shade='#54584c', deep='#3e4238', bow='#e8b43a', tape='#f4e4d4'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'big_ears': 3, 'ear_out': 4,
             'hairline': [(12, 70), (14, 56), (24, 44), (40, 36), (50, 34), (60, 36), (76, 44), (86, 56), (88, 70)]},
    'front': [L(outline([(14, 76), (10, 44), (20, 22), (40, 12), (60, 12), (80, 22), (90, 44), (86, 76), (80, 60), (20, 60)])),
              L(outline([(16, 70), (10, 84, 1), (20, 76)])), L(outline([(84, 70), (90, 84, 1), (80, 76)])),
              L(cloud(50, 4, 12, 10, 4, 0.3)), L(outline([(48, 8), (60, -6), (72, -4), (64, 8), (56, 12)]), 'bow', 'f', ln=True),
              L(outline([(58, 14), (80, 24), (90, 46), (86, 70), (78, 44)]), 'shade', 'b', False),
              L(outline([(22, 66), (32, 58), (46, 64), (44, 70), (30, 72)]), 'mid', 'f', ln=True), L(outline([(78, 66), (68, 58), (54, 64), (56, 70), (70, 72)]), 'mid', 'f', ln=True),
              L(outline([(42, 82), (58, 82), (58, 88), (42, 88)]), 'tape', 'f', ln=True),
              L(outline([(46, 104), (54, 104), (50, 114, 1)]), 'mid', 'f', ln=True)] + wrinkles(88),
    'side': [L(outline([(54, 62), (58, 50), (80, 44), (90, 30), (84, 14), (66, 6), (40, 6), (18, 14), (6, 36), (6, 62), (18, 80), (34, 82), (46, 74)])),
             L(outline([(50, 70), (44, 84, 1), (54, 76)])), L(cloud(46, -2, 12, 10, 4, 0.3)),
             L(outline([(44, 2), (30, -12), (40, -16), (50, -4)]), 'bow', 'f', ln=True),
             L(outline([(72, 64), (82, 58), (90, 64), (78, 70)]), 'mid', 'f', ln=True),
             L(outline([(82, 104), (88, 104), (86, 116, 1)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(14, 80), (10, 44), (20, 20), (40, 10), (60, 10), (80, 20), (90, 44), (86, 80), (50, 86)])),
             L(outline([(58, 12), (80, 22), (90, 46), (86, 78), (62, 84)]), 'shade', 'b', False),
             L(cloud(50, 2, 12, 10, 4, 0.3)), L(outline([(50, 8), (30, -2), (28, 10), (40, 12)]), 'bow', 'f', ln=True),
             L(outline([(50, 8), (70, -2), (72, 10), (60, 12)]), 'bow', 'f', ln=True)],
}

# Brandy Ryehart (Matsutake Umeyo): mujer grandota de cara redonda; pelo negro largo con raya en medio, recogido en una
# coleta baja a un lado con una goma amarilla; cejas negras muy gruesas, ojos cerrados de risa, mofletes rosados y la boca
# muy abierta de carcajada
CHARS['brandy-ryehart'] = {
    'body': 'corpulento', 'pal': pal('#1e1a20', '#fcd6b8', shade='#161216', deep='#0e0a0e', tie='#e8b43a'),
    'face': {'eyes': 'closed', 'brows': False, 'mouth': 'grin', 'mouth_w': 13, 'mouth_y': 96, 'nose': (50, 86, 2.8),
             'face_front': outline([(14, 50), (50, 44), (86, 50), (94, 78), (88, 100), (68, 112), (50, 114), (32, 112), (12, 100), (6, 78)]),
             'hairline': [(10, 76), (14, 56), (24, 44), (40, 38), (50, 34), (60, 38), (76, 44), (86, 56), (90, 76)]},
    'front': [L(outline([(14, 70), (2, 90), (0, 112, 1), (12, 108), (20, 96)])), L(ell(6, 110, 5, 3.6), 'tie', 'f', ln=True),
              cap(0, 44, 60, 6), cap_shade(0), strand([(50, 2), (50, 34)], 'deep', 'b', 1.2),
              L(outline([(26, 64), (32, 60), (42, 63), (41, 67), (31, 66)]), 'mid', 'f', ln=True), L(outline([(74, 64), (68, 60), (58, 63), (59, 67), (69, 66)]), 'mid', 'f', ln=True)]
             + blush(86, 24, 4.6),
    'side': [L(outline([(54, 62), (58, 50), (80, 42), (90, 28), (86, 10), (66, -4), (36, -4), (12, 8), (-2, 36), (0, 66), (10, 84), (30, 96), (46, 104), (56, 110, 1),
                        (44, 96), (36, 84), (46, 74)])),
             L(ell(52, 104, 4, 5), 'tie', 'f', ln=True),
             L(outline([(72, 62), (82, 56), (90, 62), (78, 68)]), 'mid', 'f', ln=True),
             L(ell(84, 86, 4, 2.4), (244, 168, 150, 255), 'f', False)],
    'back': [L(outline([(8, 84), (2, 42), (14, 14), (40, -2), (60, -2), (86, 14), (98, 42), (94, 84), (70, 96), (50, 100), (30, 96)])),
             back_shade(-2, 92), strand([(50, 0), (50, 96)], 'deep', 'b', 1.0)],
}

# Newman Wiford (Sarai Shinta): pelo azul marino corto y liso con la raya a un lado y brillos plateados, las patillas
# grises; gafas plateadas cuadradas, ojos entornados grises y una sonrisa
CHARS['newman-wiford'] = {
    'body': 'delgado', 'pal': pal('#1e2a4a', '#f0c49c', iris='#5a6a7a', shade='#16203a', deep='#0e1628', silver='#a8b4c8'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 96, 'glasses': (180, 190, 204, 255), 'glasses_rect': True,
             'hairline': [(12, 70), (16, 56), (28, 48), (44, 44), (56, 40), (72, 46), (84, 56), (88, 70)]},
    'front': [L(outline([(14, 74), (8, 42), (18, 16), (40, 2), (62, 2), (82, 16), (92, 42), (88, 74), (82, 58), (18, 58)])),
              L(outline([(58, 4), (82, 18), (92, 46), (88, 68), (78, 44)]), 'shade', 'b', False),
              L(outline([(16, 58), (20, 64), (20, 76), (16, 74)]), 'silver', 'f', False), L(outline([(84, 58), (80, 64), (80, 76), (84, 74)]), 'silver', 'f', False),
              L(quad((24, 34), (34, 18), (50, 10)), 'silver', 'b', False, False, 2.0), L(quad((62, 14), (74, 20), (82, 34)), 'silver', 'b', False, False, 2.0)],
    'side': [L(outline([(54, 62), (58, 50), (80, 42), (90, 28), (86, 10), (66, -2), (40, -2), (18, 8), (4, 32), (4, 60), (16, 78), (32, 82), (46, 74)])),
             L(outline([(4, 36), (24, 42), (28, 76), (10, 74)]), 'shade', 'b', False),
             L(outline([(54, 62), (60, 66), (60, 76), (54, 74)]), 'silver', 'f', False),
             L(quad((30, 14), (50, 4), (70, 8)), 'silver', 'b', False, False, 2.0)],
    'back': [L(outline([(14, 82), (10, 40), (20, 14), (40, 2), (60, 2), (82, 14), (90, 40), (86, 82), (50, 88)])),
             back_shade(2, 86), L(quad((30, 14), (40, 30), (40, 50)), 'silver', 'b', False, False, 2.0)],
}

# Vera Presswell (Aramine Kiyoko): señora; media melena negra azulada ahuecada, con la raya a un lado y la frente al aire,
# que se vuelve hacia fuera en las puntas a la altura del cuello; sombra de ojos azul, ojos azules y una sonrisa
CHARS['vera-presswell'] = {
    'body': 'chica', 'pal': pal('#2e3a40', '#fce4d4', iris='#4a6a9a', shade='#222a30', deep='#161c20', eye='#6aa8d8'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(12, 70), (14, 54), (22, 40), (30, 32), (40, 28), (54, 32), (68, 42), (82, 52), (88, 70)]},
    'front': [L(outline([(16, 60), (2, 80), (-4, 96), (12, 100), (24, 90), (22, 76)])), L(outline([(84, 60), (98, 80), (104, 96), (88, 100), (76, 90), (78, 76)])),
              cap(-2, 44, 62, 4), cap_shade(-2),
              fr([(12, 66), (14, 44), (22, 34), (32, 34), (24, 44), (20, 70, 1)]),
              L(quad((28, 70), (36, 66), (44, 70)), 'eye', 'f', False, False, 1.8), L(quad((72, 70), (64, 66), (56, 70)), 'eye', 'f', False, False, 1.8)] + lashes(),
    'side': [L(outline([(54, 62), (58, 50), (80, 42), (92, 26), (88, 6), (66, -8), (36, -6), (12, 6), (-2, 36), (0, 70), (-6, 90), (8, 100), (30, 98), (44, 90), (48, 76)])),
             L(outline([(70, 6), (94, 18), (96, 40), (84, 44), (80, 26)]), 'mid', 'f'),
             L(outline([(4, 40), (24, 46), (28, 86), (6, 88)]), 'shade', 'b', False)] + lash_side(),
    'back': [L(outline([(8, 80), (4, 42), (14, 14), (40, -4), (60, -4), (86, 14), (96, 42), (92, 80), (104, 96), (88, 102), (50, 98), (12, 102), (-4, 96)])),
             back_shade(-4, 92)],
}

# Pattie Whitfield (Shirota Manbee): abuelo bajito de cara enorme y redonda; calvo, con un ricito blanco en forma de brote
# en lo alto y el pelo blanco a los lados y la nuca; orejas grandes, ojos pequeños de sonrisa, mofletes rosados, nariz
# chata rosada y arrugas
_pattie_face = outline([(10, 40), (50, 26), (90, 40), (102, 74), (96, 102), (72, 116), (50, 118), (28, 116), (4, 102), (-2, 74)])
CHARS['pattie-whitfield'] = {
    'body': 'corpulento', 'pal': pal('#eef0f0', '#fce0d0', iris='#2a2a2a', shade='#c8cccc', deep='#a8aaaa', nose='#f0a090'),
    'face': {'eyes': 'dot', 'brows': True, 'mouth': 'smile', 'mouth_w': 12, 'mouth_y': 100, 'eye_y': 80, 'nose': (50, 88, 4), 'face_front': _pattie_face,
             'big_ears': 3, 'ear_out': 14, 'hairline': False},
    'front': [L(outline([(2, 56), (6, 40), (14, 34), (12, 60), (6, 76)]), 'mid', 'f', ln=True), L(outline([(98, 56), (94, 40), (86, 34), (88, 60), (94, 76)]), 'mid', 'f', ln=True),
              L(outline([(50, 28), (40, 22), (36, 14), (44, 16), (50, 22), (56, 16), (64, 14), (60, 22)]), 'mid', 'f', ln=True),
              L(ell(50, 88, 4.4, 3.2), 'nose', 'f', ln=True)] + blush(92, 20, 5) + wrinkles(90),
    'side': [L(outline([(10, 36), (30, 30), (40, 40), (36, 72), (24, 88), (8, 86), (0, 60)]), 'mid'),
             L(outline([(0, 60), (30, 54), (36, 72), (24, 88), (8, 86)]), 'shade', 'b', False),
             L(outline([(60, 22), (54, 12), (62, 8), (66, 18)]), 'mid', 'f', ln=True),
             L(ell(90, 90, 3.4, 3), 'nose', 'f', ln=True)],
    'back': [L(outline([(10, 82), (8, 48), (30, 56), (50, 58), (70, 56), (92, 48), (90, 82), (50, 92)])),
             L(outline([(8, 66), (50, 74), (92, 66), (90, 82), (50, 92), (10, 82)]), 'shade', 'b', False),
             L(outline([(50, 22), (40, 14), (36, 6), (46, 10), (50, 16), (56, 10), (64, 6), (60, 14)]), 'mid', 'f', ln=True)],
}
