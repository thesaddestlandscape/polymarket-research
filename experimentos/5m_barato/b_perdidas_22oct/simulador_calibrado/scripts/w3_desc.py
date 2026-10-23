"""w3_desc.py -- W3 descriptivo (sin criterio): wallets vs B real, mismas unidades primeras-5 acc en banda (0,10-0,30], T 60-300, ETH/SOL/XRP."""
import os, glob, numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__)); CVD = os.path.join(AQ, '../../cola_vs_cruce/datos')
U = pd.concat([pd.read_csv(f, dtype={'mid': str}) for f in sorted(glob.glob(os.path.join(CVD, 'up_*.csv.gz')))])
rng = np.random.default_rng(20261023)
def fila(nm, s):
    s = s.dropna(subset=['gana']); c = s.coste.sum()
    if len(s) == 0: return dict(grupo=nm, n=0)
    g = s.groupby('dia')[['pnl', 'coste']].sum().values
    bs = [(g[i, 0].sum() / g[i, 1].sum()) for i in (rng.integers(0, len(g), len(g)) for _ in range(2000))]
    cl = s.groupby('cl_h1_0.005').coste.sum() / c
    return dict(grupo=nm, n=len(s), mercados=s.mid.nunique(), EV=round(s.pnl.sum() / c, 3), IC90_dias=f'({np.percentile(bs,5):+.2f},{np.percentile(bs,95):+.2f})', hit=round(s.gana.mean(), 3), p_med=round(s.pc.mean(), 3),
                T_med=round(s['T'].median(), 0), C1=round(cl.get('C1', 0), 2), C2=round(cl.get('C2', 0), 2), C3=round(cl.get('C3', 0), 2))
out = []
for per, dias in (('17-22', None), ('20-22', ['2026-10-20', '2026-10-21', '2026-10-22'])):
    V = U if dias is None else U[U.dia.isin(dias)]
    for nm, s in (('0xf074dc84', V[V.maker.str.startswith('0xf074dc84')]), ('0x0ab01745', V[V.maker.str.startswith('0x0ab01745')]), ('B real', V[V.es_b == 1]),
                  ('resto (n unidades)', V[(V.es_b == 0) & ~V.maker.str.startswith(('0xf074dc84', '0x0ab01745'))])):
        for act in ('ETH', 'TODAS'):
            ss = s if act == 'TODAS' else s[s.act == 'ETH']
            f = fila(nm, ss); f['periodo'] = per; f['moneda'] = act; out.append(f)
print(pd.DataFrame(out)[['periodo', 'moneda', 'grupo', 'n', 'mercados', 'EV', 'IC90_dias', 'hit', 'p_med', 'T_med', 'C1', 'C2', 'C3']].to_string(index=False))
