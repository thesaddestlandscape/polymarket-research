#!/usr/bin/env python3
"""ana_dec_v3.py TAG_NUEVO TAG_VIEJO DESDE HASTA [monedas] -- compara el resumen de ana_dec.py (dev, sin editar: se EJECUTA su fuente con OUT redirigido) para el sello VIEJO (dev out/<TAG_VIEJO>_*.pkl) y el sello v3 (calma_v3/out/<TAG_NUEVO>_*.pkl) sobre los
MISMOS dias (los que existen en ambos). Imprime ambas tablas y la comparacion de dEUR_vs_G0 / EV por variante. Campo sello_print: viejo = regla 1a transicion/t-63; nuevo = v3."""
import sys, os, io, glob, contextlib, re
import numpy as np, pandas as pd
DEVD = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/A3_guarda/ret_cinta_corregida/descomp/'; MINE = os.path.dirname(os.path.abspath(__file__)) + '/out/'
tn, tv, d0, d1 = sys.argv[1:5]; coins = sys.argv[5] if len(sys.argv) > 5 else 'SOL,XRP,ETH'
dias = sorted(set(re.search(r'(\d{4}-\d{2}-\d{2})', f).group(1) for f in glob.glob(MINE + f'{tn}_*.pkl')) & set(re.search(r'(\d{4}-\d{2}-\d{2})', f).group(1) for f in glob.glob(DEVD + f'out/{tv}_*.pkl')))
dias = [d for d in dias if d0 <= d <= d1]; print('dias comunes', dias, 'sello_print: nuevo=v3 (stamp_v3, engine legacy sin dedupe); viejo=regla 1a transicion/t-63')
src = open(DEVD + 'ana_dec.py').read(); assert "OUT = H + 'out/'" in src; T = {}
for nombre, outd, tag in (('VIEJO', DEVD + 'out/', tv), ('V3', MINE, tn)):
    tmp = MINE + f'_sel_{nombre}/'; os.makedirs(tmp, exist_ok=True)
    for f in glob.glob(tmp + '*'): os.remove(f)
    for d in dias: os.symlink(outd + f'{tag}_{d}.pkl', tmp + f'{tag}_{d}.pkl')
    s = src.replace("OUT = H + 'out/'", f"OUT = {tmp!r}"); buf = io.StringIO(); old = sys.argv
    sys.argv = ['ana_dec.py', coins, tag, d0, d1]
    with contextlib.redirect_stdout(buf): exec(compile(s, 'ana_dec.py', 'exec'), {'__file__': DEVD + 'ana_dec.py', '__name__': '__main__'})
    sys.argv = old; print(f'===== sello {nombre} ({tag})'); print(buf.getvalue()); T[nombre] = buf.getvalue()
