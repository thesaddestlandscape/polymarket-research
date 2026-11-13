#!/usr/bin/env python3
"""esc_dec2_v3_dedupe.py DIA -- D (13-Nov): MIDE si el dedupe de cola de engine_v3 cambia algo en Calma-T1. Es esc_dec2_v3.py (sello v3, esc_dec2.py de dev SIN editar) con UNA sustitucion mas: el motor legacy engine.DayEng
pasa a engine_v3.DayEngV3(modo='legacy', dedupe=DEDUPE) -- mismos relojes (ex/ex); la UNICA diferencia entre DEDUPE=0 y 1 es el orden de los prints dentro de fill_segment_v3 (dedupe=False == engine.fill_segment original).
Entorno: DEDUPE=0|1 (obligatorio), CALMA_V3_OUT=<dir de salida> (obligatorio), EXTRA_SHIFT_MS (0 = dec2v3dd<DEDUPE>_<D>.pkl). Solo calculo, 0 ordenes. Lanzar con guard_rss.py, nice 19, fuera de 06-09Z."""
import sys, os
L2 = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + '/'; BASE = L2 + 'calma_v3/esc_dec2_v3.py'
dd = os.environ['DEDUPE']; assert dd in ('0', '1') and os.environ.get('CALMA_V3_OUT'), 'DEDUPE=0|1 y CALMA_V3_OUT obligatorios'
T = open(BASE).read(); ANCLA = "src = src[:i0] + NEW + src[i1:]"; assert T.count(ANCLA) == 1
PARCHE = ANCLA + f'''
A1 = "E = G.DayEng(d, 'chain', tape, bad); D = E.D"; assert src.count(A1) == 1
src = src.replace(A1, "sys.path.insert(0, %r); import engine_v3 as E3; E = E3.DayEngV3(d, 'chain', tape, bad, modo='legacy', dedupe=bool({dd})); D = E.D" % L2)
A2 = "TAGF = 'dec2v3' if XS == 0 else f'dec3v3s{{XS}}'"; assert src.count(A2) == 1
src = src.replace(A2, "TAGF = 'dec2v3dd{dd}' if XS == 0 else f'dec3v3dd{dd}s{{XS}}'")
'''
T = T.replace(ANCLA, PARCHE)
exec(compile(T, BASE, 'exec'), {'__file__': BASE, '__name__': '__main__'})
