"""El Dorado Equipo 02 (cs-el-dorado-team-02): sus modelos 3D de Inazuma Eleven GO 2: Chrono Stone como referencia (busto de
frente, perfil y espalda). El resto de la plantilla son jugadores de Protocolo Omega y del Raimon de GO, ya dibujados."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, strand  # noqa: F401
from chars_cs_protocol_omega import po
from heads import quad  # noqa: F401

DARK = (40, 44, 48, 255)

# Mecha Mark (Mecha Endou, portero): el robot copia de Endou; la cara es una placa de metal gris claro con juntas, ojos
# en dos ranuras oscuras y una sonrisa; pelo negro verdoso con un mechón en pico, y la cinta roja ancha con un
# interruptor ON/OFF al lado
CHARS['mecha-mark'] = po({
    'body': 'normal', 'pal': pal('#1e2622', '#c8cacc', iris='#1e1e1e', skin_d='#a8aaae', band='#d01e22', band_d='#a01418'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(14, 90), (8, 60), (12, 28), (30, 8), (44, 4), (60, -22, 1), (64, 6), (78, 10), (98, 4, 1), (88, 26), (92, 60), (86, 90), (80, 60), (20, 60)])),
              L(outline([(16, 64), (18, 86), (14, 96, 1), (24, 80)]), 'mid', 'f'), L(outline([(84, 64), (82, 86), (86, 96, 1), (76, 80)]), 'mid', 'f'),
              L(outline([(6, 60), (6, 34), (50, 30), (94, 34), (94, 60), (50, 56)]), 'band', 'f', ln=True),
              strand([(10, 44), (50, 40), (90, 44)], 'band_d', 'f', 1.0),
              L(outline([(70, 38), (78, 37), (78, 52), (70, 53)]), DARK, 'f', ln=True),
              L(outline([(28, 68), (44, 68), (44, 78), (28, 78)]), DARK, 'f', ln=True), L(outline([(56, 68), (72, 68), (72, 78), (56, 78)]), DARK, 'f', ln=True),
              L([(22, 84), (30, 90)], 'skin_d', 'f', False, False, 1.2), L([(78, 84), (70, 90)], 'skin_d', 'f', False, False, 1.2)],
    'side': [L(outline([(56, 60), (62, 34), (80, 28), (86, 10), (70, -2), (60, -24, 1), (54, -4), (30, 0), (10, 18), (4, 50), (12, 80), (28, 92), (44, 84)])),
             L(outline([(2, 60), (2, 34), (50, 28), (96, 32), (96, 58), (50, 56)]), 'band', 'f', ln=True),
             L(outline([(76, 68), (90, 68), (90, 78), (76, 78)]), DARK, 'f', ln=True)],
    'back': [L(outline([(14, 88), (8, 50), (14, 20), (34, 4), (50, 0), (60, -22, 1), (66, 2), (86, 18), (92, 50), (86, 88), (50, 96)])),
             L(outline([(4, 60), (4, 34), (50, 30), (96, 34), (96, 60), (50, 56)]), 'band', 'f', ln=True),
             L(outline([(44, 58), (40, 74), (48, 70), (52, 80), (58, 70), (56, 56)]), 'band_d', 'f', ln=True)],
})
