#!/usr/bin/env python3
"""Detector de huecos cortos (>=10 s) en libro5_tx, contrastado con el ritmo on-chain. Solo lectura.
Uso: detector_cortos.py YYYY-MM-DD  -> out/cortos_<dia>.json
Hueco = intervalo entre recepciones consecutivas de libro5_tx (rx unicos) con g>=10 s y g*lambda>=9.2 (Poisson p<1e-4; lambda = filas/s
en +-10 min alrededor, sin el hueco) Y con >=1 tx on-chain (tipo F, tokens vistos ese dia en libro5_tx, ts_est+2,25 s) dentro del hueco.
Clases: corto 10-60 s, largo >=60 s (compara con hole60 existente)."""
import glob, gzip, json, sys, numpy as np, pandas as pd
d = sys.argv[1]; N = '/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/calma_v3/huecos_causa_13nov/out/'
d0 = int(pd.Timestamp(d, tz='UTC').timestamp() * 1000); d1 = d0 + 86400000
P = []
for dd in (pd.Timestamp(d) + pd.Timedelta(days=i) for i in (-1, 0, 1)):
    for f in glob.glob(f'/mnt/HC_Volume_106538179/libro5_tx/libro5_tx_{dd:%Y-%m-%d}_*.csv*'):
        try: P.append(pd.read_csv(f, header=None, usecols=[1, 3], names=['tk', 'rx'], dtype={'tk': str, 'rx': 'int64'}, on_bad_lines='skip'))
        except Exception as e: print('err', f, e)
x = pd.concat(P); x = x[(x.rx >= d0 - 600000) & (x.rx < d1 + 600000)]
toks = set(x.tk); t = np.unique(x.rx.values)
oc = []
for f in sorted(glob.glob(f'/root/polymarket-research-datalogs/keep_onchain_re_as_b/onchain_fills_{d}*.csv.gz')):
    for c in pd.read_csv(f, usecols=['tipo', 'ts_est', 'tx', 'token_id'], dtype={'token_id': str}, chunksize=300000):
        oc.append(c[(c.tipo == 'F') & c.token_id.isin(toks)][['ts_est', 'tx']])
oc = pd.concat(oc).drop_duplicates('tx'); ot = np.sort((oc.ts_est.values * 1000 + 2250).astype('int64')); del oc
g = np.diff(t); idx = np.where(g >= 10000)[0]; H = []
for i in idx:
    a, b = int(t[i]), int(t[i + 1])
    if b < d0 or a >= d1: continue
    n = np.searchsorted(t, a) - np.searchsorted(t, a - 600000) + np.searchsorted(t, b + 600000) - np.searchsorted(t, b)
    lam = n / 1200.0; dur = (b - a) / 1000
    noc = int(np.searchsorted(ot, b) - np.searchsorted(ot, a))
    if dur * lam >= 9.2 and noc >= 1:
        H.append(dict(ini=pd.Timestamp(a, unit='ms').strftime('%H:%M:%S'), dur_s=round(dur, 1), lam=round(lam, 2), esperadas=round(dur * lam, 1), onchain_tx=noc))
cor = [h for h in H if h['dur_s'] < 60]; lar = [h for h in H if h['dur_s'] >= 60]
# minutos del hueco dentro de xx:50-xx:08 de horas 03,07,..,23 (hueco "4h") vs resto
def en4h(h):
    hh, mm = int(h['ini'][:2]), int(h['ini'][3:5]); return (hh % 4 == 3 and mm >= 50) or (hh % 4 == 0 and mm <= 8)
out = dict(dia=d, filas_rx_unicos=int(len(t)), n_cortos=len(cor), n_largos=len(lar), seg_cortos=round(sum(h['dur_s'] for h in cor)), seg_largos=round(sum(h['dur_s'] for h in lar)),
           cortos_en_ventana4h=sum(en4h(h) for h in cor), largos_en_ventana4h=sum(en4h(h) for h in lar), huecos=H)
json.dump(out, open(N + f'cortos_{d}.json', 'w'))
print(d, {k: v for k, v in out.items() if k != 'huecos'}, flush=True)
