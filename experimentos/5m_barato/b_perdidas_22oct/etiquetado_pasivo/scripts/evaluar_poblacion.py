#!/usr/bin/env python3
"""evaluar_poblacion.py -- gate de PREREG_L1 aplicado a la POBLACION etiquetada por etiquetar_poblacion.py (PREREG_L1b parte A). Solo lectura.
Unidad = (mercado, lado, cubo de precio 0,05). Reutiliza ev/delta_ic/placebo/bloque de evaluar_gate.py (mismo codigo, importado). Backfill 17-22 Oct = descriptivo (forward=0)."""
import os, sys, glob, hashlib, importlib.util
import numpy as np, pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get('L1B_OUT', '/root/polymarket-research-datalogs/etiquetado_pasivo_B/poblacion')
assert hashlib.sha256(open(os.path.join(HERE, '..', 'PREREG_L1b.md'), 'rb').read()).hexdigest().startswith('93cdda53'), 'PREREG_L1b.md modificado'
_sp = importlib.util.spec_from_file_location('evg', os.path.join(HERE, 'evaluar_gate.py')); G = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(G)   # asserta sha de PREREG_L1


def cargar():
    L = pd.concat([pd.read_csv(f, dtype={'mid': str}) for f in sorted(glob.glob(os.path.join(OUT, 'pob_*.csv.gz')))], ignore_index=True)
    n0 = len(L); L = L[L.gana_lado.notna() & L.pnl.notna() & L.coste.notna()].copy()      # sin desenlace = missing, no 0
    L['cubo'] = (L.precio / 0.05).round().astype(int)
    L['wc'] = L.precio * L.coste
    A = L.groupby(['dia', 'mercado', 'coin', 'lado', 'cubo', 'fin_s', 'forward', 'clase_rpre', 'h_w1'], as_index=False).agg(coste=('coste', 'sum'), pnl=('pnl', 'sum'), wc=('wc', 'sum'), n_unid=('id', 'size'))
    A['precio'] = A.wc / A.coste
    A['grupo'] = np.where(A.h_w1 == 1, 1, np.where(A.clase_rpre.isin(['a_favor', 'en_contra']), 0, -1))
    return A[A.grupo >= 0], n0 - len(L), L


def main():
    P, n_sin, L = cargar()
    print(f'unidades fuente sin desenlace (missing, excluidas): {n_sin}; celdas (mercado,lado,bucket) usables: {len(P)}')
    G.bloque(P[P.forward == 0], 'BACKFILL 17-22 Oct (poblacion pop_units; visto en W1: DESCRIPTIVO, NO decide)') if len(P[P.forward == 0]) else None
    F = P[P.forward == 1]
    if len(F) == 0: print('--- FORWARD (>= 2026-10-23): 0 celdas todavia (R1 escribe el dia D a las 10:40Z de D+1)\nESTADO: NO EVALUABLE'); return
    r = G.bloque(F, 'FORWARD >= 2026-10-23 (decide)')
    for c, g in F.groupby('coin'): print(f'   [{c}] celdas={len(g)} EV h1={G.ev(g[g.grupo == 1]):+.3f} h0={G.ev(g[g.grupo == 0]):+.3f}  (descriptivo)')
    nd = F.dia.nunique(); n1 = int((F.grupo == 1).sum())
    print(f'\nGATE L1b-A: dias forward = {nd}/10 ; celdas h_w1=1 = {n1}/40')
    if r is None or nd < 10 or n1 < 40: print('ESTADO: NO EVALUABLE (faltan dias y/o n). No cambiar B.'); return
    ok = [('Delta<0 e IC90 cierre sup<0', r['hi'] < 0), ('PnL(h1)<0 y placebo p<0,05', r['pnl1'] < 0 and r['pl_p'] < 0.05), ('sin 2 mejores dias mismo signo', r['d2'] < 0), ('>=60 % dias Delta<0', r['frac'] >= 0.6)]
    for k, v in ok: print(f'  [{"OK" if v else "NO"}] {k}')
    refut = r['delta'] >= 0 or r['lo'] <= 0 <= r['hi'] or r['pnl1'] >= 0
    print('ESTADO:', 'CONFIRMADA en poblacion (apoyo a H-L1; NO cambia B por si sola)' if all(v for _, v in ok) else ('REFUTADA en poblacion' if refut else 'NO CUMPLE (inconcluso)'))


if __name__ == '__main__':
    main()
