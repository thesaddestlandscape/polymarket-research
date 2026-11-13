#!/usr/bin/env python3
"""chequeo_libro5tx.py DIA [--dir D] [--gap-ms 60000] -- comprobacion de ENTRADA del juez forward Calma v3: los libro5_tx del dia DIA (UTC) cubren las 24 h sin huecos > gap-ms y todos los gz abren (se leen enteros).
Lee libro5_tx_<d>_<pid>.csv.gz de d-1, d, d+1 (col 0 = t_ev en ms; los ficheros se nombran por dia de arranque y se solapan en la frontera); los .csv sin comprimir (dia en curso) se ignoran y se anotan.
Cobertura = union de eventos con t_ev en [00:00, 24:00) UTC de DIA; huecos = diferencias consecutivas, incluidos los bordes (primer evento - 00:00 y 24:00 - ultimo). ok = hay datos, 0 gz con error y max hueco <= gap-ms.
Salida JSON; rc 0 ok, 1 no ok, 2 uso. Solo lectura; sin red; sin ordenes."""
import os, sys, glob, json, gzip, argparse
import numpy as np, pandas as pd
DIR = '/mnt/HC_Volume_106538179/libro5_tx/'


def chequeo(dia, dirpath=DIR, gap_ms=60000):
    d0 = int(pd.Timestamp(dia, tz='UTC').timestamp()) * 1000; d1 = d0 + 86400000; dirpath = dirpath.rstrip('/') + '/'
    fich = []; raw = []; err = {}; partes = []
    for dd in (pd.Timestamp(dia) + pd.Timedelta(days=i) for i in (-1, 0, 1)):
        s = dd.strftime('%Y-%m-%d'); fich += sorted(glob.glob(dirpath + f'libro5_tx_{s}_*.csv.gz')); raw += sorted(glob.glob(dirpath + f'libro5_tx_{s}_*.csv'))
    for f in fich:
        try:
            with gzip.open(f, 'rb') as g:                                    # lectura completa: detecta gz truncado/corrupto
                for _ in iter(lambda: g.read(1 << 22), b''): pass
            x = pd.read_csv(f, header=None, usecols=[0], names=['t'], dtype={'t': 'int64'}, on_bad_lines='skip').t.values
            partes.append(x[(x >= d0) & (x < d1)])
        except (OSError, EOFError, ValueError, pd.errors.ParserError) as e: err[os.path.basename(f)] = f'{type(e).__name__}: {e}'
    t = np.unique(np.concatenate(partes)) if partes else np.empty(0, np.int64)
    r = dict(dia=dia, ficheros_gz=len(fich), ficheros_con_error=err, ficheros_sin_comprimir_ignorados=[os.path.basename(f) for f in raw], eventos_en_dia=int(len(t)), gap_max_permitido_ms=gap_ms)
    if len(t) == 0: r.update(ok=False, motivo='sin eventos del dia', gap_max_ms=None, huecos=[]); return r
    edges = np.concatenate([[d0], t, [d1]]); gaps = np.diff(edges); big = np.where(gaps > gap_ms)[0]
    r.update(primer_evento_utc=pd.Timestamp(int(t[0]), unit='ms', tz='UTC').isoformat(), ultimo_evento_utc=pd.Timestamp(int(t[-1]), unit='ms', tz='UTC').isoformat(), gap_max_ms=int(gaps.max()), n_huecos=int(len(big)),
             huecos=[dict(desde_utc=pd.Timestamp(int(edges[i]), unit='ms', tz='UTC').isoformat(), duracion_s=round(float(gaps[i]) / 1000, 1)) for i in big[:20]])
    r['ok'] = (not err) and len(big) == 0; r['motivo'] = None if r['ok'] else ('gz con error' if err else f'{len(big)} hueco(s) > {gap_ms} ms'); return r


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('dia'); ap.add_argument('--dir', default=DIR); ap.add_argument('--gap-ms', type=int, default=60000); a = ap.parse_args()
    r = chequeo(a.dia, a.dir, a.gap_ms); print(json.dumps(r, indent=1)); sys.exit(0 if r['ok'] else 1)
