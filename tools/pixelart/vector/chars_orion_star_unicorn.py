"""Star Unicorn (orion-star-unicorn): la selección de Estados Unidos de Orion no Kokuin. La wiki lista a casi todos con su
forma de Orion (Kid_OK, Ted_OK...) y a Domon e Ichinose con la de Ares (Domon_AT, Ichinose_AT); Rob y Bob solo salen en el
juego, sin forma de Orion (van con sus dibujos de siempre).
Los modelos 3D de Orion (オリオンの刻印) de los americanos son iguales que los de Victory Road con los que se dibujó el Unicorn
de IE3: se reutilizan esos dibujos, retocando lo que no cuadraba (cejas y ojos de Ted y Tony). Domon de Ares sí cambia
(pinchos más altos, nuca rapada más oscura, ojos afilados) y se dibuja aparte. Todos van como 'orion:<id>'."""
import copy

from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from heads import quad  # noqa: F401

O = 'orion'
for _pid in ('billy-dash', 'drake-dynamo', 'steve-woodmark', 'erik-eagle', 'shane-pierce', 'mark-krueger', 'dylan-keats', 'gabriel-jax',
             'alex-hawke', 'corey-washington', 'bob-bobbins', 'petie-pooma', 'norbert-poindexter'):
    CHARS[f'{O}:{_pid}'] = CHARS[_pid]

# Ted Bryan: en el modelo los ojos son grandes, blancos y de pupila negra, con las cejas muy fruncidas
CHARS[f'{O}:ted-bryant'] = copy.deepcopy(CHARS['ted-bryant'])
CHARS[f'{O}:ted-bryant']['face'].update({'eyes': 'big', 'brows': 'angry'})
# Tony Stridas: cejas rubias fruncidas sobre los ojos blancos redondos
CHARS[f'{O}:tony-strider'] = copy.deepcopy(CHARS['tony-strider'])
CHARS[f'{O}:tony-strider']['front'] += [L([(28, 65), (42, 70)], OUTC, 'f', False, False, 2.2), L([(72, 65), (58, 70)], OUTC, 'f', False, False, 2.2)]

# Domon Asuka (Ares): pelo gris verdoso de pinchos altos de punta hacia arriba y algo hacia atrás, con unos mechones en
# punta que le caen por la frente; los lados cortos hasta lo alto de la oreja y la nuca rapada, más oscura; piel tostada,
# cara alargada, ojos afilados y la boca recta
CHARS[f'{O}:bobby-shearer'] = {
    'body': 'delgado', 'pal': pal('#9aaca6', '#e0a462', iris='#3a2a20', shade='#707a78', deep='#585e5e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 97,
             'hairline': [(12, 66), (17, 56), (24, 58), (28, 48), (36, 52), (41, 44), (46, 58), (50, 46), (56, 56), (62, 46), (68, 54), (74, 50), (80, 58),
                          (88, 66)]},
    'front': [L(outline([(16, 66), (12, 46), (14, 28), (8, 18, 1), (18, 14), (14, -4, 1), (25, 5), (26, -14, 1), (35, 1), (41, -18, 1), (47, -1), (55, -16, 1),
                         (59, 0), (67, -12, 1), (69, 4), (82, -4, 1), (79, 12), (92, 10, 1), (85, 26), (88, 46), (84, 66), (80, 52), (20, 52)])),
              L(outline([(60, 0), (82, -4), (79, 12), (92, 10), (85, 26), (88, 46), (84, 64), (72, 40), (64, 20)]), 'shade', 'b', False),
              strand([(30, 8), (36, 30)], 'deep', 'b', 1.0), strand([(48, 2), (50, 26)], 'deep', 'b', 1.0), strand([(66, 8), (62, 30)], 'deep', 'b', 1.0)],
    'side': [L(outline([(80, 50), (84, 40), (92, 36, 1), (85, 29), (94, 16, 1), (81, 13), (86, -4, 1), (72, 4), (71, -16, 1), (60, -1), (52, -18, 1), (45, -1),
                        (30, -8, 1), (30, 7), (6, 4, 1), (18, 18), (4, 30, 1), (8, 50), (12, 70), (20, 82), (32, 84), (38, 72), (42, 60), (54, 58), (66, 60), (74, 54)])),
             L(outline([(6, 36), (30, 42), (46, 54), (40, 64), (36, 76), (32, 84), (20, 82), (12, 70), (8, 50)]), 'shade', 'b', False),
             strand([(40, 4), (60, 18), (78, 24)], 'deep', 'b', 1.0), strand([(28, 12), (44, 26)], 'deep', 'b', 1.0)],
    'back': [L(outline([(18, 80), (14, 56), (14, 30), (8, 18, 1), (18, 12), (15, -4, 1), (28, 4), (31, -14, 1), (42, 0), (50, -18, 1), (57, 0), (67, -12, 1), (71, 4),
                        (85, -3, 1), (80, 14), (92, 18, 1), (86, 30), (86, 56), (82, 80), (50, 88)])),
             L(outline([(14, 48), (34, 40), (50, 44), (66, 40), (86, 48), (84, 80), (50, 88), (18, 80)]), 'shade', 'b', False),
             L(outline([(60, 2), (85, -3), (80, 14), (92, 18), (86, 30), (86, 46), (68, 40)]), 'deep', 'b', False)],
}
