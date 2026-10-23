"""w_diag_b.py -- diagnostico descriptivo: fills de B NO explicados por un print en su nivel: ¿hay print a otro nivel en la ventana? por clase C1/C2/C3."""
import os, sys, runpy, numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__)); CVD = os.path.join(AQ, '../../cola_vs_cruce/datos'); D = os.path.join(AQ, '..', 'datos')
import gzip
SRCS = ['/root/polymarket-research-datalogs/cola_vs_cruce/', '/mnt/HC_Volume_106538179/datalogs_analisis_caches/colas_20oct/']
def prints(act, mid):
    for s in SRCS:
        p = f'{s}mk/{act}_{mid}.gz'
        if os.path.exists(p): break
    else: return None
    out = {'Y': [], 'N': []}
    with gzip.open(p, 'rt', errors='replace') as f:
        for ln in f:
            if ',T,' not in ln: continue
            c = ln.rstrip('\n').split(',')
            try: L, r, side, q, acc = c[0], int(c[2]), c[3], int(round(float(c[4]) * 1000)), float(c[5])
            except Exception: continue
            if side == 'SELL': out[L].append((r, q, acc))
            else: out['N' if L == 'Y' else 'Y'].append((r, 1000 - q, acc))
    return {L: np.array(sorted(v), float).reshape(-1, 3) for L, v in out.items()}
bc = pd.read_csv(os.path.join(CVD, 'b_clase.csv'), dtype={'mid': str}).drop_duplicates(['tx', 'c'])
bc = bc[bc.es_b == 1]
rows = []
for r in bc.itertuples():
    P = prints(r.act, r.mid)
    if P is None: continue
    L = 'Y' if r.lado == 'YES' else 'N'; a = P[L]; q = int(round(r.pc * 1000))
    w = (a[:, 0] >= (r.ts - 6) * 1000) & (a[:, 0] <= (r.ts + 1) * 1000)
    ex = (np.abs(a[:, 1] - q) <= 5) & w
    prints_win = a[w]
    deeper = (prints_win[:, 1] < q - 5).any() if len(prints_win) else False
    any_ = len(prints_win) > 0
    w2 = (a[:, 0] >= (r.ts - 12) * 1000) & (a[:, 0] <= (r.ts + 4) * 1000); ex2 = ((np.abs(a[:, 1] - q) <= 5) & w2).any()
    rows.append(dict(cl=r._asdict()['_13'] if False else None, expl=int(ex.any()), expl_ancho=int(ex2), print_otro_nivel=int(any_ and not ex.any()), deeper=int(deeper and not ex.any()), act=r.act, es_primera=1))
df = pd.DataFrame(rows)
print('B fills', len(df), 'explicados', df.expl.mean().round(3), 'con ventana ancha [-12,+4]', df.expl_ancho.mean().round(3), '| no explicados:', int((df.expl == 0).sum()), 'de ellos con algun print a OTRO nivel', int(df.print_otro_nivel.sum()), 'a nivel mas hondo', int(df.deeper.sum()))
print(df.groupby('act').expl.agg(['mean', 'size']).round(3))
