#!/usr/bin/env python3
"""registro_robusto.py - rehace m{5,15}_registro_D.csv.gz REUTILIZANDO extraer_registro_15m.extraer() (no se reescribe), tolerando la corrupcion
a media corriente de un maker_ms (zlib.error 'invalid stored block lengths' / 'invalid compressed data'), que el extractor original NO captura
(solo EOFError/OSError) y que mato la extraccion del 22-Oct dejando m{5,15}_registro_2026-10-22.csv.tmp truncado. Aqui zlib.error se trata como
fin de fichero de ESE crudo (se pierden solo sus filas posteriores al corte) y se anota. Uso: registro_robusto.py DIA --marco 5min|15min"""
import sys, gzip, zlib, argparse, time, json
sys.path.insert(0, '/root/polymarket-research')
import extraer_registro_15m as ER
from archivo_volumen import VOL
import infra_lib as L
class _Tol:
    def __init__(s, h): s.h = h
    def __enter__(s): return s
    def __exit__(s, *a): s.h.close()
    def __iter__(s):
        try: yield from s.h
        except zlib.error: ER_CORTES.append(1); raise EOFError('zlib mid-stream')
class _G:
    def open(s, f, mode='rb', **kw):
        h = gzip.open(f, mode, **kw); return _Tol(h) if 'r' in mode else h
ER_CORTES = []
if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('dia'); ap.add_argument('--marco', choices=('15min', '5min'), required=True); a = ap.parse_args()
    ER.gzip = _G(); ER.MARCO, ER.PREF = a.marco, {'15min': 'm15', '5min': 'm5'}[a.marco]; ER.OUT = VOL / f'{ER.PREF}_registro'
    t0 = time.time(); ER.extraer(a.dia, forzar=True)
    dst = ER.OUT / f'{ER.PREF}_registro_{a.dia}.csv.gz'
    L.atomic_json(L.INFRA / 'runs' / f'registro_{ER.PREF}_{a.dia}.json', dict(dia=a.dia, marco=a.marco, cortes_zlib_midstream=len(ER_CORTES), existe=dst.exists(), bytes=dst.stat().st_size if dst.exists() else None, segundos=time.time() - t0, fin=L.now()))
    print('cortes zlib a media corriente tolerados:', len(ER_CORTES))
