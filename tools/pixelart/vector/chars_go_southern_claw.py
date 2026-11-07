"""Garras del Sur (go-southern-claw): sus modelos 3D de Inazuma Eleven GO como referencia (busto de frente, perfil y espalda)."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, strand  # noqa: F401
from heads import quad  # noqa: F401
from chars_go_raimon import fringe

# Los demás jugadores están en chars_go_demon_s_horn.py (Cuerno Demoníaco junta a los de Garras del Sur y Colmillos del Norte).

# Jared Dapplegrey: grandullón de cara redonda con el pelo rojo en un cono altísimo terminado en punta, como una llama, y
# dos mechones blancos en punta sobre las orejas; ojos cerrados de enfado y boca torcida
CHARS['jared-dapplegrey'] = {
    'body': 'corpulento', 'pal': pal('#b8303a', '#f4d0a8', iris='#1e1414', horn='#f4f0ec'),
    'face': {'eyes': 'closed', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100, 'face_front': blob([(10, 54), (50, 44), (90, 54), (96, 80), (88, 104),
                                                                                                         (66, 114), (34, 114), (12, 104), (4, 80)]),
             'hairline': False},
    'front': [L(outline([(14, 80), (8, 50), (20, 20), (36, 0), (50, -36, 1), (64, 0), (80, 20), (92, 50), (86, 80), (80, 60), (20, 60)])),
              L(outline([(56, -20), (78, 18), (90, 50), (84, 74), (76, 40), (62, 10)]), 'shade', 'b', False),
              fringe([(12, 66), (14, 44), (28, 30), (50, 26), (72, 30), (86, 44), (88, 66), (78, 58), (68, 62), (60, 54), (50, 60), (40, 54), (32, 62), (22, 58)]),
              L(outline([(12, 56), (2, 40, 1), (18, 48)]), 'horn', 'f', ln=True), L(outline([(88, 56), (98, 40, 1), (82, 48)]), 'horn', 'f', ln=True)],
    'side': [L(outline([(56, 60), (64, 46), (84, 46), (92, 30), (86, 10), (100, -40, 1), (60, -6), (36, -8), (14, 10), (4, 40), (4, 70), (16, 90), (34, 92), (46, 74)])),
             L(outline([(6, 40), (26, 44), (30, 84), (12, 84)]), 'shade', 'b', False),
             L(outline([(48, 52), (40, 30, 1), (58, 44)]), 'horn', 'f', ln=True)],
    'back': [L(outline([(14, 80), (8, 50), (20, 20), (36, 0), (50, -36, 1), (64, 0), (80, 20), (92, 50), (86, 80), (70, 92), (50, 98, 1), (30, 92)])),
             L(outline([(56, -20), (80, 20), (92, 50), (86, 78), (62, 90)]), 'shade', 'b', False),
             L(outline([(10, 56), (0, 36, 1), (18, 46)]), 'horn', 'f', ln=True), L(outline([(90, 56), (100, 36, 1), (82, 46)]), 'horn', 'f', ln=True)],
}

# Gamal Everlast: media melena castaño rojizo lisa con flequillo recto y mechones largos delante de las orejas que acaban en
# punta; ojos azul violeta afilados y media sonrisa
CHARS['gamal-everlast'] = {
    'body': 'chica', 'pal': pal('#7a3a28', '#fce4cc', iris='#4a4aa8'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 96), (2, 92), (4, 60), (6, 30), (20, 8), (50, 0), (80, 8), (94, 30), (96, 60), (98, 92), (86, 96), (82, 62), (18, 62)])),
              L(outline([(60, 4), (86, 16), (96, 50), (96, 90), (86, 80), (80, 40)]), 'shade', 'b', False),
              L(outline([(14, 60), (10, 90), (14, 112, 1), (20, 92), (22, 64)]), 'mid', 'f', ln=True),
              L(outline([(86, 60), (90, 90), (86, 112, 1), (80, 92), (78, 64)]), 'mid', 'f', ln=True),
              fringe([(10, 62), (12, 36), (26, 16), (50, 8), (74, 16), (88, 36), (90, 62), (82, 60), (82, 52), (66, 50), (50, 52), (34, 50), (18, 52), (18, 60)])],
    'side': [L(outline([(56, 62), (60, 50), (82, 50), (94, 34), (88, 12), (66, -2), (36, -2), (14, 10), (2, 36), (0, 70), (2, 94), (20, 98), (36, 92), (48, 76)])),
             L(outline([(2, 40), (28, 44), (34, 88), (8, 92)]), 'shade', 'b', False),
             strand([(10, 70), (12, 92)], 'deep', 'b', 1.0), strand([(24, 70), (26, 94)], 'deep', 'b', 1.0),
             fringe([(64, 2), (90, 16), (96, 40), (92, 54, 1), (82, 52), (74, 40)]),
             L(outline([(56, 62), (60, 90), (58, 112, 1), (52, 92), (50, 66)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(14, 96), (2, 92), (4, 60), (6, 30), (20, 8), (50, 0), (80, 8), (94, 30), (96, 60), (98, 92), (86, 96), (76, 90), (66, 98), (56, 90), (46, 98),
                        (36, 90), (26, 98)])),
             L(outline([(56, 4), (86, 16), (96, 50), (96, 92), (66, 94), (70, 40)]), 'shade', 'b', False),
             strand([(4, 60), (50, 50), (96, 60)], 'deep', 'b', 1.0)],
}

# Solomon Roundhay: piel bronceada, pelo crema muy claro de pinchos gruesos de punta hacia arriba y los lados, y unas gafas
# rectangulares de pasta marrón; cejas fruncidas
CHARS['solomon-roundhay'] = {
    'body': 'normal', 'pal': pal('#f6ecd4', '#e8a868', iris='#1e1414', shade='#c8a89a', deep='#a88a7a', frame=(110, 80, 50, 255)),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100, 'hairline': False, 'glasses': (110, 80, 50, 255), 'glasses_rect': True},
    'front': [L(outline([(16, 74), (0, 70, 1), (10, 56), (-8, 40, 1), (8, 34), (2, 10, 1), (22, 14), (26, -10, 1), (40, 4), (50, -18, 1), (60, 2), (78, -10, 1),
                         (78, 10), (100, 6, 1), (90, 28), (110, 36, 1), (92, 50), (104, 66, 1), (86, 70), (82, 54), (18, 54)])),
              L(outline([(60, 2), (86, 14), (96, 44), (88, 66), (78, 40)]), 'shade', 'b', False),
              fringe([(14, 62), (16, 40), (30, 26), (50, 20), (70, 26), (84, 40), (86, 62), (76, 52), (68, 60, 1), (62, 48), (52, 58, 1), (46, 46), (36, 56, 1), (30, 46),
                      (22, 58, 1)])],
    'side': [L(outline([(56, 58), (62, 46), (84, 46), (94, 30), (90, 12), (102, 0, 1), (78, 2), (70, -16, 1), (56, -2), (36, -14, 1), (30, 4), (4, -2, 1), (12, 18),
                        (-12, 30, 1), (6, 40), (-8, 56, 1), (8, 60), (0, 78, 1), (18, 76), (22, 90, 1), (34, 78), (46, 70)]), 'shade'),
             L(outline([(36, -2), (56, -2), (78, 2), (92, 18), (88, 30), (60, 26), (40, 14)]), 'mid', 'b', False)],
    'back': [L(outline([(16, 82), (0, 84, 1), (8, 66), (-8, 52, 1), (8, 44), (0, 20, 1), (18, 20), (22, -4, 1), (36, 8), (48, -16, 1), (56, 4), (74, -8, 1), (74, 10),
                        (98, 6, 1), (88, 26), (108, 32, 1), (92, 48), (106, 62, 1), (90, 66), (98, 84, 1), (82, 82), (50, 90)]), 'shade'),
             L(outline([(8, 44), (0, 20, 1), (18, 20), (22, -4, 1), (36, 8), (48, -16, 1), (56, 4), (74, -8, 1), (74, 10), (98, 6, 1), (88, 26), (90, 40), (50, 34)]),
               'mid', 'b', False)],
}
