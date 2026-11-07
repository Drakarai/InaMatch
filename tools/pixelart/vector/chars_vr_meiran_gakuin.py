"""Academia Orchid (vr-meiran-gakuin, Meiran Gakuin): todas chicas, con sus modelos 3D de Inazuma Eleven: Victory Road
(英雄たちのヴィクトリーロード) como referencia (busto de frente, perfil y espalda). Cada una tiene un solo modelo; ningún id coge
por prefijo el dibujo de otro personaje."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from chars_vr_keizen_arashiyama import WHITE, cloud, fr, lash_side, lashes
from heads import quad  # noqa: F401


def bangs(y, x0=14, x1=86, n=5, top=30, c='mid', jag=6):
    """Flequillo recto (o en picos con jag) hasta la altura y."""
    pts = [(x0 - 2, y + 2), (x0, top + 12), (x0 + 14, top), (50, top - 4), (x1 - 14, top), (x1, top + 12), (x1 + 2, y + 2)]
    for i in range(n):
        x = x1 - (i + 0.5) * (x1 - x0) / n
        pts += [(x + (x1 - x0) / n * 0.35, y - jag), (x, y, 1)] if jag else [(x, y)]
    return L(outline(pts), c, 'f')


def cap(top=4, side=44, lo=62, w=0):
    """Casquete de pelo de frente (hasta la línea lo, que tapa la cara el contorno de la cara)."""
    return L(outline([(12 - w, lo + 16), (8 - w, side), (18 - w, 18 + top), (40, 4 + top), (60, 4 + top), (82 + w, 18 + top), (92 + w, side), (88 + w, lo + 16),
                      (82, lo), (18, lo)]))


def cap_shade(top=4, lo=74):
    return L(outline([(58, 6 + top), (82, 20 + top), (92, 46), (88, lo), (78, 44)]), 'shade', 'b', False)


def side_cap(top=0, lo=62, back=(4, 66)):
    """Casquete de perfil: de la frente a la nuca, con la oreja al aire."""
    return L(outline([(54, lo), (58, 50), (80, 42 + top * 0.5), (90, 28), (86, 12 + top), (66, 0 + top), (40, 0 + top), (18, 10 + top), (4, 36), back, (14, 84),
                      (28, 90), (42, 84), (48, 72)]))


def back_cap(top=2, lo=84):
    return L(outline([(12, lo), (8, 42), (18, 16 + top), (40, 2 + top), (60, 2 + top), (82, 16 + top), (92, 42), (88, lo), (50, lo + 6)]))


def back_shade(top=2, lo=84):
    return L(outline([(58, 4 + top), (84, 18 + top), (94, 50), (90, lo), (64, lo + 6)]), 'shade', 'b', False)


def long_front(y=110, flare=6, x0=16, x1=84, top=60, c='mid'):
    """Los dos mechones largos que caen por detrás de la cara hasta y."""
    return [L(outline([(x0, top), (x0 - 10, y - 30), (x0 - 10 - flare, y, 1), (x0 + 2, y - 8), (x0 + 6, y - 30)]), c),
            L(outline([(x1, top), (x1 + 10, y - 30), (x1 + 10 + flare, y, 1), (x1 - 2, y - 8), (x1 - 6, y - 30)]), c)]


def long_side(y=116, x=-4, c='mid'):
    """La melena larga de perfil, por detrás de la oreja hasta y."""
    return L(outline([(20, 10), (4, 34), (x, 70), (x - 4, y, 1), (10, y - 8), (20, y - 2, 1), (30, y - 20), (40, 86), (44, 70), (30, 40)]), c)


def long_back(y=116, flare=6, ends=4, c='mid'):
    """Melena larga de espaldas hasta y, con ends puntas abajo."""
    pts = [(10, 40), (2 - flare * 0.3, 80), (0 - flare, y, 1)]
    for i in range(ends):
        x = (i + 1) * 100 / (ends + 1)
        pts += [(x - 8, y - 8), (x, y + 4, 1)]
    pts += [(100 + flare, y, 1), (98 + flare * 0.3, 80), (90, 40), (80, 16), (50, 2), (20, 16)]
    return L(outline(pts), c)


# Lilia Charmont (Mikagami Seren, portera): pelo castaño claro largo y esponjoso hasta los hombros, con raya en medio y el
# flequillo partido; dos orejas de conejo largas (blancas por fuera, rosas por dentro) le salen de arriba y le caen por detrás
# de los hombros, con dos pinzas naranjas; ojos rosas grandes y la boca pequeña seria
CHARS['lilia-charmont'] = {
    'body': 'chica', 'pal': pal('#c8a68c', '#fce4d4', iris='#e07a8a', shade='#a88670', deep='#866652', ear=WHITE, pink='#f0a2b4', clip='#e8642a'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'frown', 'mouth_y': 95, 'nose': (50, 85, 1.6),
             'hairline': [(12, 76), (16, 58), (26, 48), (40, 44), (50, 54), (60, 44), (74, 48), (84, 58), (88, 76)]},
    'front': [L(outline([(22, 22), (8, 30), (-6, 70), (-8, 110), (2, 112), (10, 70), (20, 40)]), 'ear', 'b', ln=True),
              L(outline([(78, 22), (92, 30), (106, 70), (108, 110), (98, 112), (90, 70), (80, 40)]), 'ear', 'b', ln=True),
              L(outline([(16, 32), (2, 70), (0, 104), (4, 104), (10, 70), (20, 40)]), 'pink', 'b', False),
              L(outline([(84, 32), (98, 70), (100, 104), (96, 104), (90, 70), (80, 40)]), 'pink', 'b', False),
              L(outline([(16, 60), (6, 90), (8, 112, 1), (18, 104), (24, 84)])), L(outline([(84, 60), (94, 90), (92, 112, 1), (82, 104), (76, 84)])),
              cap(2, 44, 62, 4), cap_shade(2),
              L(outline([(16, 30), (24, 24), (30, 48), (24, 66), (14, 50)]), 'pink', 'f', ln=True), L(outline([(84, 30), (76, 24), (70, 48), (76, 66), (86, 50)]), 'pink', 'f', ln=True),
              L(ell(24, 14, 4, 3.4), 'clip', 'f', ln=True), L(ell(76, 14, 4, 3.4), 'clip', 'f', ln=True)] + lashes(dx=7.4),
    'side': [L(outline([(46, 6), (30, 20), (6, 60), (-12, 100), (-6, 106), (12, 72), (36, 30)]), 'ear', 'b', ln=True),
             L(outline([(40, 16), (26, 30), (6, 66), (-6, 96), (-2, 98), (12, 70), (36, 30)]), 'pink', 'b', False),
             side_cap(0, 62, (2, 70)), long_side(110, 0),
             L(outline([(4, 40), (26, 46), (30, 84), (10, 84)]), 'shade', 'b', False),
             L(ell(52, 4, 4, 3.4), 'clip', 'f', ln=True)] + lash_side(),
    'back': [long_back(108, 6, 4), back_cap(2, 84), back_shade(2, 100),
             L(outline([(26, 6), (14, 30), (10, 70), (8, 104), (18, 104), (22, 70), (30, 30)]), 'ear', 'f', ln=True),
             L(outline([(74, 6), (86, 30), (90, 70), (92, 104), (82, 104), (78, 70), (70, 30)]), 'ear', 'f', ln=True),
             L(ell(22, 6, 4, 3.4), 'clip', 'f', ln=True), L(ell(78, 6, 4, 3.4), 'clip', 'f', ln=True)],
}

# Evelyn Hale (Anegasaki Seiko): melena celeste hasta los hombros, con las puntas rizadas hacia dentro y franjas blancas que
# la cruzan (en el flequillo y por detrás); flequillo de lado; ojos azules con pestañas y una sonrisa con los dientes
CHARS['evelyn-hale'] = {
    'body': 'chica', 'pal': pal('#6cc0e2', '#fce4d4', iris='#3a6ab8', shade='#4a9ac0', deep='#3a7a9c', white=WHITE),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'grin', 'mouth_y': 94,
             'hairline': [(12, 76), (16, 58), (24, 50), (40, 46), (56, 44), (72, 48), (84, 58), (88, 76)]},
    'front': [L(outline([(16, 60), (4, 92), (8, 110), (20, 112, 1), (18, 96), (24, 80)])), L(outline([(84, 60), (96, 92), (92, 110), (80, 112, 1), (82, 96), (76, 80)])),
              L(outline([(6, 98), (8, 110), (20, 112, 1), (16, 100)]), 'white', 'b', False),
              cap(2, 44, 62, 2), cap_shade(2),
              fr([(12, 64), (14, 42), (28, 30), (50, 26), (72, 30), (86, 42), (88, 62), (80, 54), (66, 50), (54, 52), (40, 58), (30, 64, 1), (24, 56)]),
              L(outline([(14, 58), (18, 50), (34, 48), (52, 46), (66, 48), (54, 54), (36, 58), (28, 64, 1), (22, 56)]), 'white', 'f', False)] + lashes(),
    'side': [side_cap(0, 62, (2, 70)), L(outline([(4, 60), (0, 86), (6, 100), (20, 100, 1), (14, 88), (24, 84)])),
             L(outline([(10, 40), (30, 30), (56, 34), (54, 42), (32, 40), (14, 50)]), 'white', 'b', False),
             L(outline([(2, 88), (6, 100), (20, 100, 1), (12, 92)]), 'white', 'b', False),
             L(outline([(70, 42), (88, 50), (92, 64, 1), (80, 56)]), 'mid', 'f')] + lash_side(),
    'back': [L(outline([(10, 84), (8, 42), (18, 16), (40, 2), (60, 2), (82, 16), (92, 42), (92, 84), (96, 98), (82, 104, 1), (70, 96), (50, 100), (30, 96), (18, 104, 1),
                        (4, 98)])),
             back_shade(2, 92),
             L(outline([(10, 40), (30, 30), (50, 28), (70, 30), (90, 40), (90, 50), (70, 40), (50, 38), (30, 40), (10, 50)]), 'white', 'b', False)],
}

# Margie Frostveil (Hinagiku Himari): pelo largo rubio oliva hasta el pecho, más oscuro (castaño) en las puntas, con un
# flequillo crema claro de mechones rizados; ojos grandes gris azulado con pestañas gruesas, nariz rosa y una sonrisita
CHARS['margie-frostveil'] = {
    'body': 'chica', 'pal': pal('#b8b47c', '#fce4d4', iris='#4a5a7a', shade='#9a9662', deep='#7a7648', cream='#f4ecca', tip='#8a6a4a'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'nose': (50, 85, 2),
             'hairline': [(12, 76), (16, 58), (28, 50), (50, 54), (72, 50), (84, 58), (88, 76)]},
    'front': long_front(116, 6) + [
              L(outline([(4, 100), (-2, 116, 1), (12, 108)]), 'tip', 'b', False), L(outline([(96, 100), (102, 116, 1), (88, 108)]), 'tip', 'b', False),
              cap(2, 44, 62, 2), cap_shade(2),
              fr([(20, 62), (22, 44), (34, 36), (50, 34), (66, 36), (78, 44), (80, 62), (70, 52), (62, 58, 1), (56, 48), (48, 56, 1), (42, 46), (32, 56, 1), (28, 50)], 'cream'),
              strand([(40, 40), (36, 46), (40, 50)], 'deep', 'f', 1.0), strand([(56, 38), (60, 44), (56, 48)], 'deep', 'f', 1.0)] + lashes(dx=7.6, n=2),
    'side': [side_cap(0, 62, (2, 70)), long_side(110, -4), L(outline([(-6, 92), (-8, 110, 1), (10, 102), (20, 108, 1), (24, 96)]), 'tip', 'b', False),
             L(outline([(4, 40), (26, 46), (30, 84), (10, 84)]), 'shade', 'b', False),
             L(outline([(70, 40), (86, 46), (92, 60, 1), (80, 54)]), 'cream', 'f')] + lash_side(),
    'back': [long_back(110, 6, 4), back_shade(2, 104),
             L(outline([(0, 94), (-6, 110, 1), (14, 106), (34, 114, 1), (50, 104), (66, 114, 1), (86, 106), (106, 110, 1), (100, 94), (50, 98)]), 'tip', 'b', False)],
}

# Elara Silvane (Ginshou Kirei): pelo negro grisáceo largo y liso con flequillo recto, un mechón plateado a un lado y dos
# trencitas finas delante de las orejas atadas con cinta plateada; las puntas de los lados se levantan como cuernos a la
# altura de las orejas y lleva una coletita en punta arriba atrás; ojos entornados con pestañas y la boca seria
CHARS['elara-silvane'] = {
    'body': 'chica', 'pal': pal('#3e3e44', '#fce8dc', iris='#b0a866', shade='#2e2e32', deep='#1e1e22', silver='#bcbcc2'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 95, 'hairline': False},
    'front': long_front(124, 4) + [
              L(outline([(16, 52), (-4, 50), (-14, 56, 1), (-2, 60), (16, 62)])), L(outline([(84, 52), (104, 50), (114, 56, 1), (102, 60), (84, 62)])),
              cap(2, 44, 62, 2), cap_shade(2),
              L(outline([(74, 30), (86, 44), (90, 70), (86, 100), (80, 70), (74, 50)]), 'silver', 'f', ln=True),
              bangs(62, 14, 86, 6, 30, 'mid', 0),
              L(rope((22, 64), (20, 84), (22, 104), 3.6), 'deep', 'f'), L(rope((78, 64), (80, 84), (78, 104), 3.6), 'deep', 'f'),
              L(ell(22, 92, 3, 2), 'silver', 'f', False), L(ell(78, 92, 3, 2), 'silver', 'f', False)] + lashes(n=2),
    'side': [L(outline([(26, 14), (4, 4, 1), (16, 0), (6, -10, 1), (24, -2), (24, -16, 1), (36, 4)])),
             side_cap(0, 62, (2, 70)), long_side(124, -6),
             L(outline([(4, 40), (26, 46), (30, 84), (10, 84)]), 'shade', 'b', False),
             L(outline([(62, 4), (88, 14), (96, 40), (92, 62), (78, 60), (80, 42)]), 'mid', 'f'),
             L(rope((60, 62), (60, 82), (62, 102), 3.6), 'deep', 'f'), L(ell(61, 92, 3, 2), 'silver', 'f', False)] + lash_side(),
    'back': [long_back(124, 4, 4), back_cap(2, 84), back_shade(2, 116),
             L(outline([(16, 54), (-4, 50), (-14, 56, 1), (-2, 60), (16, 64)])), L(outline([(84, 54), (104, 50), (114, 56, 1), (102, 60), (84, 64)])),
             L(outline([(50, 14), (36, 0, 1), (46, 2), (44, -10, 1), (54, 0), (62, -6, 1), (60, 10)]))],
}

# Amara Winslow (Shinomiya Kasane): pelo morado lavanda largo y liso hasta la espalda, con raya en medio y mechones que le
# cruzan la frente; las puntas de los lados se curvan hacia fuera a la altura de las orejas; ojos verdes con pestañas
CHARS['amara-winslow'] = {
    'body': 'chica', 'pal': pal('#8e76c8', '#fce4d4', iris='#6aaa90', shade='#7460a8', deep='#5a4a88'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'line', 'mouth_y': 95,
             'hairline': [(12, 76), (16, 58), (28, 48), (44, 42), (50, 36), (56, 42), (72, 48), (84, 58), (88, 76)]},
    'front': long_front(124, 4) + [
              L(outline([(14, 66), (0, 64), (-14, 58, 1), (-2, 70), (12, 76)])), L(outline([(86, 66), (100, 64), (114, 58, 1), (102, 70), (88, 76)])),
              cap(2, 44, 62, 2), cap_shade(2), strand([(50, 6), (50, 36)], 'deep', 'b', 1.2),
              fr([(48, 38), (40, 50), (30, 66), (26, 86, 1), (34, 64), (44, 50)]), fr([(52, 38), (60, 50), (70, 66), (74, 86, 1), (66, 64), (56, 50)])] + lashes(n=2),
    'side': [side_cap(0, 62, (2, 70)), long_side(126, -8),
             L(outline([(4, 40), (26, 46), (30, 84), (10, 84)]), 'shade', 'b', False),
             L(outline([(60, 44), (72, 52), (70, 72), (62, 88, 1), (64, 64)]), 'mid', 'f'),
             L(outline([(10, 64), (0, 60), (-14, 54, 1), (-2, 68), (10, 74)]))] + lash_side(),
    'back': [long_back(126, 4, 4), back_shade(2, 118),
             L(outline([(12, 64), (-2, 62), (-16, 56, 1), (-4, 70), (12, 76)])), L(outline([(88, 64), (102, 62), (116, 56, 1), (104, 70), (88, 76)]))],
}

# Selene Trance (Kisui Miyona): pelo verde azulado en forma de capucha redonda que le tapa la cabeza, con un rizo grande en
# espiral sobre la frente y mechones oscuros que le enmarcan la cara hasta la barbilla; ojos amarillos adormilados y rubor
CHARS['selene-trance'] = {
    'body': 'chica', 'pal': pal('#3a9ca8', '#fce8dc', iris='#d8bc3a', shade='#2e7e88', deep='#1e5a62', blush='#f4aaaa'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'frown', 'mouth_y': 95,
             'hairline': [(12, 80), (16, 60), (24, 50), (40, 48), (60, 46), (76, 50), (84, 60), (88, 80)]},
    'front': [L(outline([(12, 66), (2, 96), (6, 114, 1), (18, 104), (22, 84)])), L(outline([(88, 66), (98, 96), (94, 114, 1), (82, 104), (78, 84)])),
              L(outline([(10, 88), (4, 44), (16, 14), (40, 0), (62, 0), (84, 14), (96, 44), (90, 88), (82, 62), (18, 62)])),
              L(outline([(58, 4), (84, 18), (96, 46), (90, 82), (78, 44)]), 'shade', 'b', False),
              fr([(24, 54), (22, 36), (32, 22), (46, 18), (58, 22), (60, 32), (50, 36), (42, 32), (40, 42), (48, 46), (40, 52), (30, 50)]),
              strand([(46, 22), (34, 28), (38, 40), (46, 38)], 'deep', 'f', 1.4),
              L(outline([(18, 62), (24, 76), (24, 102, 1), (20, 80)]), 'deep', 'f'), L(outline([(82, 62), (76, 76), (76, 102, 1), (80, 80)]), 'deep', 'f'),
              L(ell(28, 86, 4, 2.4), 'blush', 'f', False), L(ell(72, 86, 4, 2.4), 'blush', 'f', False)],
    'side': [L(outline([(54, 62), (58, 50), (80, 42), (90, 28), (86, 10), (66, -2), (40, -2), (16, 10), (2, 40), (2, 74), (8, 96), (20, 108, 1), (24, 92), (40, 86),
                        (48, 72)])),
             L(outline([(4, 40), (26, 46), (30, 86), (8, 84)]), 'shade', 'b', False),
             L(outline([(62, 6), (84, 16), (94, 40), (88, 52), (76, 44), (70, 30)]), 'mid', 'f'),
             L(outline([(60, 50), (68, 70), (68, 104, 1), (62, 78)]), 'deep', 'f')],
    'back': [L(outline([(10, 92), (4, 44), (16, 14), (40, 0), (62, 0), (84, 14), (96, 44), (90, 92), (70, 100), (50, 96), (30, 100)])),
             back_shade(0, 96),
             strand([(30, 20), (24, 60), (30, 96)], 'deep', 'b', 1.6), strand([(50, 4), (46, 50), (50, 94)], 'deep', 'b', 1.6), strand([(70, 20), (74, 60), (70, 96)], 'deep', 'b', 1.6)],
}

# Galia Flair (Tenjou Amami): piel morena clara; pelo azul marino recogido en una coleta alta con un lazo dorado, con el
# flequillo revuelto y mechones que salen a los lados y se enroscan; ojos lila con pestañas largas y sonrisa
CHARS['galia-flair'] = {
    'body': 'chica', 'pal': pal('#3a4a8e', '#d0946e', iris='#9a6aaa', shade='#2e3a72', deep='#222a54', gold='#e8c064'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(12, 76), (18, 56), (26, 50), (34, 56), (42, 46), (50, 54), (58, 46), (66, 56), (74, 50), (82, 56), (88, 76)]},
    'front': [L(rope((14, 62), (-12, 66), (-18, 92), 5)), L(rope((86, 62), (112, 66), (118, 92), 5)),
              L(outline([(16, 66), (10, 90), (12, 110, 1), (20, 94)])), L(outline([(84, 66), (90, 90), (88, 110, 1), (80, 94)])),
              L(outline([(40, 10), (32, -6), (40, -14), (60, -14), (68, -6), (60, 10)]), 'gold', 'b', ln=True),
              cap(2, 44, 62, 2), cap_shade(2), L(ell(50, 8, 6, 3), 'deep', 'b', False),
              fr([(14, 62), (16, 42), (30, 30), (50, 26), (70, 30), (84, 42), (86, 62), (78, 52), (70, 62, 1), (64, 48), (54, 60, 1), (48, 46), (38, 62, 1), (34, 48),
                  (24, 60, 1)])] + lashes(dx=7.6, n=2),
    'side': [L(outline([(40, 0), (30, -16), (14, -14), (2, 6), (-6, 40), (-2, 70), (8, 80, 1), (10, 60), (20, 30), (34, 14)])),
             L(outline([(34, 2), (22, -10), (12, -6), (6, 20), (2, 50), (12, 30), (24, 12)]), 'gold', 'b', ln=True),
             side_cap(0, 62, (6, 64)), L(ell(36, 4, 3, 5), 'deep', 'b', False),
             L(outline([(4, 40), (26, 46), (30, 80), (10, 78)]), 'shade', 'b', False),
             L(rope((60, 60), (64, 84), (58, 104), 4), 'mid', 'f')] + lash_side(),
    'back': [L(outline([(36, 10), (26, 40), (24, 80), (30, 110), (50, 120, 1), (70, 110), (76, 80), (74, 40), (64, 10)])),
             back_cap(2, 84), back_shade(2, 84),
             L(rope((14, 64), (-12, 68), (-18, 94), 5)), L(rope((86, 64), (112, 68), (118, 94), 5)),
             L(outline([(36, 14), (28, 30), (30, 60), (40, 30), (50, 16)]), 'gold', 'f', ln=True),
             L(outline([(44, 16), (30, 70), (36, 112), (50, 120, 1), (64, 112), (70, 70), (56, 16)])),
             L(ell(50, 12, 8, 4), 'deep', 'f', False)],
}

# Eliza Florence (Kamurigi Eliza): media melena castaña con raya a un lado que deja la frente, hasta la mandíbula y con las
# puntas abiertas hacia fuera; cejas marcadas, ojos rojos y una sonrisa ladeada
CHARS['eliza-florence'] = {
    'body': 'chica', 'pal': pal('#a27c52', '#fcdcc4', iris='#b03636', shade='#86643e', deep='#6a4c2c'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(12, 76), (16, 56), (24, 44), (36, 36), (44, 30), (56, 34), (72, 42), (84, 56), (88, 76)]},
    'front': [L(outline([(16, 60), (2, 84), (-6, 100, 1), (10, 98), (22, 90)])), L(outline([(84, 60), (98, 84), (106, 100, 1), (90, 98), (78, 90)])),
              cap(2, 44, 62, 2), cap_shade(2), strand([(44, 4), (44, 30)], 'deep', 'b', 1.0)] + lashes(),
    'side': [L(outline([(54, 62), (58, 50), (80, 42), (90, 28), (86, 12), (66, 0), (40, 0), (18, 10), (4, 36), (2, 66), (-6, 88), (-8, 100, 1), (12, 96), (30, 98, 1),
                        (36, 88), (46, 76)])),
             L(outline([(4, 40), (26, 46), (32, 90), (6, 92)]), 'shade', 'b', False)] + lash_side(),
    'back': [L(outline([(10, 78), (8, 42), (18, 16), (40, 2), (60, 2), (82, 16), (92, 42), (90, 78), (104, 96, 1), (80, 96), (50, 100), (20, 96), (-4, 96, 1)])),
             back_shade(2, 92)],
}

# Elyse Reign (Housen Ranka, capitana): pelo malva en una melena enorme y redonda como una capucha que le cae hasta los
# hombros y se abomba hacia fuera en las puntas, con un rizo arriba; antifaz dorado y blanco con una flor de lis en medio y
# dos antenas doradas en lo alto; ojos morados
CHARS['elyse-reign'] = {
    'body': 'chica', 'pal': pal('#9a5a7c', '#fce4d4', iris='#8a3a7a', shade='#7c4662', deep='#5e344a', gold='#d8b04a', mask=WHITE),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'frown', 'mouth_y': 95,
             'hairline': [(12, 76), (16, 58), (28, 48), (40, 42), (50, 46), (60, 42), (72, 48), (84, 58), (88, 76)]},
    'front': [L(rope((40, 8), (30, -10), (24, -26), 2.4), 'gold', 'b'), L(rope((60, 8), (70, -10), (76, -26), 2.4), 'gold', 'b'),
              L(outline([(14, 60), (-2, 84), (-6, 104), (8, 112), (24, 108), (26, 92), (22, 76)])), L(outline([(86, 60), (102, 84), (106, 104), (92, 112), (76, 108), (74, 92), (78, 76)])),
              L(outline([(12, 80), (6, 42), (16, 14), (40, 0), (62, 0), (84, 14), (94, 42), (88, 80), (82, 60), (18, 60)])),
              L(outline([(58, 4), (84, 18), (94, 46), (88, 76), (78, 44)]), 'shade', 'b', False),
              strand([(46, 10), (40, 18), (48, 24), (54, 16)], 'deep', 'b', 1.2),
              L(outline([(20, 70), (16, 62, 1), (30, 64), (42, 68), (50, 64), (58, 68), (70, 64), (84, 62, 1), (80, 70), (72, 84), (58, 82), (50, 78), (42, 82), (28, 84)]),
                'mask', 'f', ln=True),
              L(outline([(22, 70), (30, 66), (42, 70), (40, 80), (28, 82)]), 'gold', 'f', False), L(outline([(78, 70), (70, 66), (58, 70), (60, 80), (72, 82)]), 'gold', 'f', False),
              L(ell(34, 75, 4.4, 4.6), (30, 22, 30, 255), 'f', False), L(ell(66, 75, 4.4, 4.6), (30, 22, 30, 255), 'f', False),
              L(ell(34, 75, 2.6, 3.2), 'iris', 'f', False), L(ell(66, 75, 2.6, 3.2), 'iris', 'f', False),
              L(outline([(50, 70), (46, 62), (50, 54, 1), (54, 62)]), 'gold', 'f', ln=True)],
    'side': [L(rope((48, 2), (44, -14), (38, -28), 2.4), 'gold', 'b'),
             L(outline([(54, 62), (58, 50), (80, 42), (90, 28), (86, 10), (66, -2), (40, -2), (16, 10), (2, 40), (-4, 80), (-6, 104), (8, 112), (30, 110), (34, 94),
                        (44, 82), (50, 72)])),
             L(outline([(4, 40), (26, 46), (30, 100), (6, 104)]), 'shade', 'b', False),
             L(outline([(76, 62), (84, 58, 1), (94, 66), (90, 82), (78, 80)]), 'mask', 'f', ln=True),
             L(outline([(78, 64), (88, 64), (90, 78), (80, 78)]), 'gold', 'f', False), L(ell(85, 72, 2.4, 3.4), 'iris', 'f', False)],
    'back': [L(rope((40, 6), (30, -10), (24, -26), 2.4), 'gold', 'b'), L(rope((60, 6), (70, -10), (76, -26), 2.4), 'gold', 'b'),
             L(outline([(10, 80), (6, 42), (16, 14), (40, 0), (62, 0), (84, 14), (94, 42), (94, 80), (106, 100), (96, 112), (50, 112), (4, 112), (-6, 100)])),
             L(outline([(-4, 92), (50, 86), (104, 92), (106, 100), (96, 112), (4, 112), (-6, 100)]), 'shade', 'b', False),
             back_shade(0, 84)],
}

# Adelina Gearhart (Ayanokouji Misao): pelo castaño claro largo y ondulado hasta el pecho, crema claro por dentro, con
# flequillo recto y una diadema azul; gafas doradas de cristal hexagonal, ojos verdes, mofletes sonrosados y boca pequeña
CHARS['adelina-gearhart'] = {
    'body': 'chica', 'pal': pal('#b89272', '#fce4d4', iris='#4a6a3a', shade='#9a7658', deep='#7a5a40', cream='#eed8b2', band='#3a54b2', blush='#f4a888'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'frown', 'mouth_y': 95, 'glasses': (200, 160, 64, 255), 'glasses_rect': True,
             'hairline': [(12, 76), (16, 58), (24, 50), (50, 48), (76, 50), (84, 58), (88, 76)]},
    'front': [L(outline([(16, 58), (2, 90), (-4, 112, 1), (14, 106), (22, 84)]), 'cream'), L(outline([(84, 58), (98, 90), (104, 112, 1), (86, 106), (78, 84)]), 'cream'),
              L(outline([(14, 56), (2, 74), (-6, 112, 1), (-2, 90), (8, 70)])), L(outline([(86, 56), (98, 74), (106, 112, 1), (102, 90), (92, 70)])),
              cap(2, 44, 62, 2), cap_shade(2),
              L(quad((12, 40), (50, 0), (88, 40)), 'band', 'f', False, False, 3.4),
              bangs(62, 18, 82, 5, 30, 'mid', 0),
              L(ell(26, 86, 4.4, 2.6), 'blush', 'f', False), L(ell(74, 86, 4.4, 2.6), 'blush', 'f', False)],
    'side': [side_cap(0, 62, (2, 70)), long_side(112, -6), L(outline([(30, 50), (40, 84), (36, 104, 1), (24, 80)]), 'cream', 'b', False),
             L(outline([(4, 40), (26, 46), (30, 84), (10, 84)]), 'shade', 'b', False),
             L(quad((60, 0), (66, 20), (72, 46)), 'band', 'f', False, False, 3.4),
             L(outline([(72, 42), (90, 44), (92, 62), (80, 60)]), 'mid', 'f'),
             L(ell(80, 86, 3.4, 2.4), 'blush', 'f', False)],
    'back': [long_back(112, 6, 4), back_shade(2, 104),
             L(outline([(40, 40), (30, 70), (36, 100), (50, 108, 1), (64, 100), (70, 70), (60, 40)]), 'shade', 'b', False)],
}

# Clarisse Luxe (Kiyomizu Chizuru): pelo carmesí con corte hime: flequillo recto, mechones laterales hasta el pecho y una
# coleta corta atada por detrás con los lados recogidos en lazadas; piel muy clara, ojos rosas con pestañas y puntitos
# debajo, y una sonrisa
CHARS['clarisse-luxe'] = {
    'body': 'chica', 'pal': pal('#a8264e', '#fcece4', iris='#d07aa0', shade='#881c3e', deep='#64142c'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(14, 56), (-2, 54), (-10, 62, 1), (2, 66), (14, 66)])), L(outline([(86, 56), (102, 54), (110, 62, 1), (98, 66), (86, 66)])),
              L(cloud(6, 54, 9, 10, 4)), L(cloud(94, 54, 9, 10, 4, 0.4)),
              L(outline([(18, 62), (12, 90), (14, 116, 1), (22, 96), (24, 74)])), L(outline([(82, 62), (88, 90), (86, 116, 1), (78, 96), (76, 74)])),
              cap(2, 44, 62, 2), cap_shade(2),
              bangs(64, 16, 84, 6, 30, 'mid', 0),
              L(outline([(18, 62), (24, 66), (26, 104, 1), (20, 80)]), 'mid', 'f'), L(outline([(82, 62), (76, 66), (74, 104, 1), (80, 80)]), 'mid', 'f'),
              L(ell(30, 86, 0.9, 0.9), OUTC, 'f', False), L(ell(34, 87, 0.9, 0.9), OUTC, 'f', False),
              L(ell(70, 86, 0.9, 0.9), OUTC, 'f', False), L(ell(66, 87, 0.9, 0.9), OUTC, 'f', False)] + lashes(dx=7.6),
    'side': [L(outline([(16, 46), (0, 52), (-8, 74), (2, 96, 1), (8, 74), (14, 64)])), L(outline([(16, 52), (-6, 50), (-10, 62), (8, 60)])),
             side_cap(0, 62, (6, 64)),
             L(outline([(4, 40), (26, 46), (30, 80), (10, 78)]), 'shade', 'b', False),
             L(outline([(68, 4), (90, 16), (94, 40), (92, 60), (82, 60), (80, 40)]), 'mid', 'f'),
             L(outline([(62, 60), (68, 70), (70, 112, 1), (62, 84)]), 'mid', 'f')] + lash_side(),
    'back': [back_cap(2, 84), back_shade(2, 84),
             L(outline([(50, 66), (26, 58), (-2, 60), (-8, 74), (8, 80), (30, 74), (50, 70)])), L(outline([(50, 66), (74, 58), (102, 60), (108, 74), (92, 80), (70, 74), (50, 70)])),
             L(outline([(46, 68), (40, 90), (36, 114, 1), (50, 100), (60, 116, 1), (60, 90), (54, 68)])),
             L(outline([(42, 62), (58, 62), (58, 72), (42, 72)]), (200, 160, 80, 255), 'f', ln=True)],
}

# Talia Jester (Kazakari Emiri, portera suplente): pelo rojo anaranjado en dos rulos enormes que le abomban la cabeza por
# arriba y dos coletas rizadas a los lados que se abren en puntas como llamas sobre los hombros, con lazos amarillos; ojos
# naranjas maquillados y una sonrisa de dientes
CHARS['talia-jester'] = {
    'body': 'chica', 'pal': pal('#e85a2c', '#fce4d4', iris='#d8641c', shade='#c4441c', deep='#9a3010', bow='#f0d040'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'grin', 'mouth_y': 95,
             'hairline': [(12, 76), (16, 58), (26, 50), (40, 46), (50, 54), (60, 46), (74, 50), (84, 58), (88, 76)]},
    'front': [L(outline([(16, 72), (-6, 82), (-16, 100, 1), (-4, 98), (-12, 112, 1), (6, 106), (14, 114, 1), (22, 96)])),
              L(outline([(84, 72), (106, 82), (116, 100, 1), (104, 98), (112, 112, 1), (94, 106), (86, 114, 1), (78, 96)])),
              L(outline([(14, 76), (6, 66), (8, 80)]), 'bow', 'f', ln=True), L(outline([(86, 76), (94, 66), (92, 80)]), 'bow', 'f', ln=True),
              cap(0, 44, 62, 4), cap_shade(0),
              L(cloud(30, 22, 22, 18, 5, 0.3)), L(cloud(70, 22, 22, 18, 5, 0.7)),
              L(outline([(60, 10), (84, 18), (92, 36), (80, 40), (70, 28)]), 'shade', 'b', False),
              fr([(24, 56), (30, 44), (44, 40), (50, 50), (56, 40), (70, 44), (76, 56), (64, 50), (56, 56, 1), (50, 48), (44, 56, 1), (36, 50)])] + lashes(dx=7.6),
    'side': [L(outline([(24, 76), (6, 86), (-4, 104, 1), (8, 100), (4, 114, 1), (22, 106), (30, 112, 1), (36, 94)])),
             side_cap(-6, 62, (2, 66)), L(cloud(40, 8, 30, 18, 6, 0.3)),
             L(outline([(4, 40), (26, 46), (30, 80), (10, 78)]), 'shade', 'b', False),
             L(outline([(28, 80), (22, 70), (20, 84)]), 'bow', 'f', ln=True)] + lash_side(),
    'back': [L(outline([(16, 76), (-6, 86), (-16, 104, 1), (-4, 100), (-12, 114, 1), (6, 108), (14, 116, 1), (24, 98)])),
             L(outline([(84, 76), (106, 86), (116, 104, 1), (104, 100), (112, 114, 1), (94, 108), (86, 116, 1), (76, 98)])),
             back_cap(-2, 84), L(cloud(30, 20, 24, 18, 5, 0.3)), L(cloud(70, 20, 24, 18, 5, 0.7)),
             back_shade(0, 84), strand([(50, 8), (50, 80)], 'deep', 'b', 1.2)],
}

# Celina Lavelle (Miyabina Reika): pelo naranja largo y ondulado hasta los hombros, con mechones de lado que se le curvan
# sobre la frente y la dejan al aire; ojos castaño dorado con pestañas y la boca seria
CHARS['celina-lavelle'] = {
    'body': 'chica', 'pal': pal('#e88a4c', '#fcece0', iris='#9a7a3a', shade='#c66e34', deep='#a05424'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'frown', 'mouth_y': 95,
             'hairline': [(12, 76), (16, 58), (24, 46), (40, 40), (56, 40), (72, 44), (84, 58), (88, 76)]},
    'front': [L(outline([(16, 60), (6, 84), (10, 100), (2, 116, 1), (16, 106), (24, 86)])), L(outline([(84, 60), (94, 84), (90, 100), (98, 116, 1), (84, 106), (76, 86)])),
              cap(2, 44, 62, 2), cap_shade(2),
              fr([(14, 64), (16, 44), (26, 34), (40, 30), (34, 40), (24, 52), (20, 68, 1)]), fr([(86, 64), (84, 44), (72, 34), (60, 32), (68, 42), (78, 52), (80, 70, 1)]),
              strand([(46, 6), (52, 30)], 'deep', 'b', 1.0)] + lashes(dx=7.6),
    'side': [side_cap(0, 62, (2, 70)), long_side(106, -4),
             L(outline([(4, 40), (26, 46), (30, 84), (10, 84)]), 'shade', 'b', False),
             L(outline([(68, 40), (86, 44), (88, 58, 1), (76, 52)]), 'mid', 'f')] + lash_side(),
    'back': [long_back(108, 6, 4), back_shade(2, 100), strand([(50, 4), (50, 100)], 'deep', 'b', 1.0)],
}

# Kiyora Asakiri (Asagiri Kiyora): pelo largo en dos tonos: la parte de arriba rubia con dos mechones largos y planos que
# salen hacia los lados como un lazo enorme, y el resto castaño oliva que le cae liso hasta la cintura; rayas rojas en los
# ojos, ojos turquesa y la boca seria
CHARS['kiyora-asakiri'] = {
    'body': 'chica', 'pal': pal('#8a7c4c', '#fcdcc4', iris='#3aa8a0', shade='#6e623a', deep='#544a2a', blond='#f0c874', blond_d='#d4a84e', red='#d43a3a'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'frown', 'mouth_y': 95,
             'hairline': [(12, 76), (16, 58), (24, 48), (36, 44), (44, 52), (50, 40), (56, 52), (64, 44), (76, 48), (84, 58), (88, 76)]},
    'front': long_front(130, 4) + [
              cap(2, 44, 62, 2), L(outline([(16, 40), (24, 18), (44, 6), (56, 6), (60, 30), (50, 40), (36, 34), (24, 46)]), 'blond', 'b', False),
              L(outline([(84, 40), (76, 18), (60, 6), (56, 30), (66, 34), (76, 46)]), 'blond_d', 'b', False),
              L(outline([(40, 10), (20, 14), (-10, 40), (-16, 56, 1), (0, 52), (24, 30), (44, 22)]), 'blond', 'f', ln=True),
              L(outline([(60, 10), (80, 14), (110, 40), (116, 56, 1), (100, 52), (76, 30), (56, 22)]), 'blond', 'f', ln=True),
              L(outline([(46, 40), (40, 50), (36, 62, 1), (44, 52), (52, 46)]), 'blond', 'f'), L(outline([(56, 40), (62, 50), (66, 62, 1), (58, 52)]), 'blond', 'f'),
              L([(26, 74), (30, 82)], 'red', 'f', False, False, 1.4), L([(74, 74), (70, 82)], 'red', 'f', False, False, 1.4)] + lashes(),
    'side': [long_side(132, -10), side_cap(0, 62, (4, 66)),
             L(outline([(40, 6), (60, 4), (86, 14), (90, 30), (70, 26), (50, 20), (36, 20)]), 'blond', 'b', False),
             L(outline([(44, 8), (20, 6), (-14, 26), (-30, 44, 1), (-10, 42), (16, 24), (40, 22)]), 'blond', 'f', ln=True),
             L(outline([(44, 14), (24, 24), (-6, 56), (-12, 74, 1), (4, 64), (28, 34), (46, 24)]), 'blond_d', 'f', ln=True),
             L(outline([(4, 40), (26, 46), (30, 84), (10, 84)]), 'shade', 'b', False),
             L([(80, 72), (84, 80)], 'red', 'f', False, False, 1.4)] + lash_side(),
    'back': [long_back(132, 4, 4), back_shade(2, 124),
             L(outline([(40, 4), (20, 10), (-12, 34), (-20, 52, 1), (0, 46), (26, 26), (46, 18)]), 'blond', 'f', ln=True),
             L(outline([(60, 4), (80, 10), (112, 34), (120, 52, 1), (100, 46), (74, 26), (54, 18)]), 'blond', 'f', ln=True),
             L(outline([(40, 8), (24, 30), (16, 80), (20, 120, 1), (34, 80), (44, 30)]), 'blond_d', 'f', ln=True),
             L(outline([(60, 8), (76, 30), (84, 80), (80, 120, 1), (66, 80), (56, 30)]), 'blond_d', 'f', ln=True)],
}

# Lenora Graves (Misono Rena): pelo azul con flequillo recto y mechones largos a los lados que acaban en tirabuzones a la
# altura de los hombros; ojos rojos con sombra azul y una sonrisa traviesa
CHARS['lenora-graves'] = {
    'body': 'chica', 'pal': pal('#3a6ab2', '#fcece4', iris='#d42424', shade='#2e5490', deep='#223e6c'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(16, 62), (-2, 80), (-14, 96), (-6, 104), (8, 96), (20, 84)])), L(outline([(84, 62), (102, 80), (114, 96), (106, 104), (92, 96), (80, 84)])),
              L(ell(-8, 104, 7, 6), 'mid', 'b', ln=True), L(ell(108, 104, 7, 6), 'mid', 'b', ln=True),
              cap(0, 44, 62, 4), cap_shade(0),
              bangs(62, 16, 84, 5, 30, 'mid', 0),
              L(outline([(18, 62), (26, 68), (26, 92, 1), (20, 78)]), 'mid', 'f'), L(outline([(82, 62), (74, 68), (74, 92, 1), (80, 78)]), 'mid', 'f')] + lashes(),
    'side': [L(outline([(24, 70), (10, 86), (0, 100), (8, 106), (20, 96), (32, 84)])), L(ell(4, 104, 7, 6), 'mid', 'b', ln=True), L(ell(18, 110, 6, 5), 'mid', 'b', ln=True),
             side_cap(-2, 62, (4, 66)),
             L(outline([(4, 40), (26, 46), (30, 80), (10, 78)]), 'shade', 'b', False),
             L(outline([(68, 4), (90, 16), (94, 40), (92, 60), (82, 60), (80, 40)]), 'mid', 'f'),
             L(outline([(62, 60), (68, 70), (68, 96, 1), (62, 80)]), 'mid', 'f')] + lash_side(),
    'back': [back_cap(0, 88), back_shade(0, 88),
             L(outline([(14, 70), (-4, 84), (-14, 98), (-6, 106), (8, 98), (22, 88)])), L(outline([(86, 70), (104, 84), (114, 98), (106, 106), (92, 98), (78, 88)])),
             L(ell(-8, 104, 7, 6), 'mid', 'b', ln=True), L(ell(108, 104, 7, 6), 'mid', 'b', ln=True)]
}

# Liliane Alban (Shirayuri Sakiha): pelo rosa claro muy abundante y ondulado que le cae hasta el pecho, con un lazo blanco
# grande en lo alto; ojos cerrados de sonrisa, labios fruncidos y mofletes sonrosados
CHARS['liliane-alban'] = {
    'body': 'chica', 'pal': pal('#f0aab6', '#fce8dc', shade='#d68a98', deep='#b86c7a', bow=WHITE, blush='#f4a0a0'),
    'face': {'eyes': 'closed', 'brows': True, 'mouth': 'line', 'mouth_w': 5, 'mouth_y': 95,
             'hairline': [(12, 76), (16, 58), (26, 46), (40, 40), (56, 42), (72, 46), (84, 58), (88, 76)]},
    'front': [L(outline([(26, 8), (14, -10), (22, -16), (40, -6), (48, 4)]), 'bow', 'b', ln=True), L(outline([(74, 8), (86, -10), (78, -16), (60, -6), (52, 4)]), 'bow', 'b', ln=True),
              L(outline([(16, 56), (-2, 76), (2, 96), (-6, 114, 1), (12, 108), (24, 86)])), L(outline([(84, 56), (102, 76), (98, 96), (106, 114, 1), (88, 108), (76, 86)])),
              cap(0, 44, 62, 6), cap_shade(0),
              fr([(14, 66), (12, 42), (26, 28), (44, 26), (34, 36), (24, 50), (22, 70, 1)]), fr([(86, 66), (88, 42), (76, 30), (58, 28), (68, 38), (78, 50), (78, 70, 1)]),
              L(ell(50, 6, 3, 3), 'bow', 'f', ln=True),
              L(ell(28, 86, 4.4, 2.4), 'blush', 'f', False), L(ell(72, 86, 4.4, 2.4), 'blush', 'f', False),
              L(ell(50, 95, 2.4, 1.8), (220, 110, 120, 255), 'f', False)],
    'side': [L(outline([(48, 0), (40, -16), (50, -20), (60, -4)]), 'bow', 'b', ln=True),
             side_cap(-2, 62, (2, 70)), L(outline([(10, 30), (-8, 60), (-12, 100), (-2, 112, 1), (10, 96), (22, 106, 1), (32, 86), (40, 74), (30, 40)])),
             L(outline([(-4, 50), (14, 54), (24, 96), (2, 100)]), 'shade', 'b', False),
             L(outline([(68, 40), (86, 48), (88, 62, 1), (76, 56)]), 'mid', 'f')],
    'back': [long_back(112, 8, 4), back_shade(0, 104),
             L(outline([(48, 8), (36, -8), (24, -10), (22, 2), (36, 10)]), 'bow', 'f', ln=True), L(outline([(52, 8), (64, -8), (76, -10), (78, 2), (64, 10)]), 'bow', 'f', ln=True),
             L(outline([(50, 30), (40, 20), (32, 30), (50, 60), (68, 30), (60, 20)]), 'shade', 'b', False)],
}
