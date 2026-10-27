#!/usr/bin/env python3
"""RE-CENSO c2: distribucion, concentracion, quien paga, descomposicion y persistencia walk-forward (PREREG_E01). Solo lectura de A_/W_ parquet."""
import glob, sys, json
import numpy as np, pandas as pd
from archivo_volumen import VOL  # noqa

IN = VOL / 'agentes_datos' / 're_censo'
SEL = ['2026-10-%02d' % d for d in range(5, 15)]; TEST = ['2026-10-%02d' % d for d in range(15, 26)]
B_WALLET = '0x659a40ff9920febc5a66836213040924343d297f'
CONOC = {'0xb0f85baa': 'pspspsps5', '0x32ed2e54': 'mo-money', '0x21f4': '0x21f4', '0xe290': '0xe290', '0x86b1': '0x86b1',
         '0x0ab0': '0x0ab0', '0xf074': '0xf074'}
PBL = ['<.01', '.01-.05', '.05-.10', '.10-.20', '.20-.30', '.30-.50', '.50-.70', '.70-.90', '.90-.99', '>.99']
TBL = ['post', '0-10', '10-60', '60-150', '150-300', '>300']
D, P, W = [], [], []
for f in sorted(glob.glob(str(IN / 'A_*.parquet'))):
    a = pd.read_parquet(f); dia = a.dia.iloc[0]
    a['w'] = a.w.astype(str)
    D.append(a.groupby('w')[['pnl', 'fee', 'reb', 'usd', 'n', 'usd_sin']].sum().assign(dia=dia).reset_index())
    P.append(a.groupby(['w', 'rol', 'pb', 'tb', 'act'])[['pnl', 'fee', 'reb', 'usd', 'n']].sum().reset_index())
    if len(P) >= 4:
        P = [pd.concat(P).groupby(['w', 'rol', 'pb', 'tb', 'act'])[['pnl', 'fee', 'reb', 'usd', 'n']].sum().reset_index()]
for f in sorted(glob.glob(str(IN / 'W_*.parquet'))):
    W.append(pd.read_parquet(f))
D = pd.concat(D); P = pd.concat(P).groupby(['w', 'rol', 'pb', 'tb', 'act'])[['pnl', 'fee', 'reb', 'usd', 'n']].sum().reset_index()
W = pd.concat(W).groupby('w')[['n_mkt', 'n_mkt_2lados']].sum()
dias = sorted(D.dia.unique()); print('dias', len(dias), dias[0], dias[-1])
D['net'] = D.pnl - D.fee + D.reb; D['net_sinreb'] = D.pnl - D.fee
cob = 1 - D.usd_sin.sum() / D.usd.sum(); print('cobertura desenlace en USD: %.5f' % cob)
tot = D.groupby('w').agg(net=('net', 'sum'), net_sinreb=('net_sinreb', 'sum'), pnl=('pnl', 'sum'), fee=('fee', 'sum'), reb=('reb', 'sum'),
                         usd=('usd', 'sum'), n=('n', 'sum'), dias=('dia', 'nunique'), dpos=('net', lambda s: int((s > 0).sum())))
tot = tot[tot.index != B_WALLET]
print('\n== Q1 distribucion (periodo completo) ==')
print('wallets', len(tot), '| net>0', int((tot.net > 0).sum()), '| net_sinreb>0', int((tot.net_sinreb > 0).sum()))
for th in (100, 1000, 10000):
    print('  net > %d $: %d' % (th, int((tot.net > th).sum())))
for nd in (5, 10, 15):
    m = (tot.dias >= nd)
    print('  activas >=%d dias: %d; de ellas net>0 %d; con dias+ >= 70%% de sus dias %d' % (nd, int(m.sum()), int((m & (tot.net > 0)).sum()), int((m & (tot.dpos >= 0.7 * tot.dias) & (tot.net > 0)).sum())))
G = tot[tot.net > 0].sort_values('net', ascending=False); L = tot[tot.net < 0]
print('  beneficio de las ganadoras %.0f $ | perdidas de las perdedoras %.0f $ | neto total %.0f $ | fees totales %.0f | rebate est. %.0f' % (G.net.sum(), L.net.sum(), tot.net.sum(), tot.fee.sum(), tot.reb.sum()))
for k in (1, 10, 100, 1000):
    print('  top-%d ganadoras = %.1f %% del beneficio ganador' % (k, 100 * G.net.head(k).sum() / G.net.sum()))
# rol dominante por wallet
rol = P.groupby(['w', 'rol']).usd.sum().unstack(fill_value=0); rol['fM'] = rol.get('M', 0) / (rol.get('M', 0) + rol.get('T', 0))
tot = tot.join(rol['fM']); tot['tipo'] = np.where(tot.fM >= 0.8, 'maker', np.where(tot.fM <= 0.2, 'tomador', 'hibrido'))
tot['dec'] = pd.qcut(tot.usd.rank(method='first'), 10, labels=False)
print('\n== quien paga / quien gana por tipo y decil de volumen ==')
print(tot.groupby('tipo').agg(n=('net', 'size'), ganadoras=('net', lambda s: int((s > 0).sum())), net=('net', 'sum'), pnl=('pnl', 'sum'), fee=('fee', 'sum'), reb=('reb', 'sum'), usd=('usd', 'sum')).round(0).to_string())
print(tot.groupby('dec').agg(n=('net', 'size'), ganadoras=('net', lambda s: int((s > 0).sum())), net=('net', 'sum'), usd=('usd', 'sum'), usd_med=('usd', 'median')).round(0).to_string())
print('\n== descomposicion por rol x banda (todas las wallets): pnl direccional, fee, rebate, EV/€ ==')
pr = P.groupby(['rol', 'pb'])[['pnl', 'fee', 'reb', 'usd']].sum(); pr['ev'] = (pr.pnl - pr.fee) / pr.usd; pr['ev_reb'] = (pr.pnl - pr.fee + pr.reb) / pr.usd
pr.index = [(r, PBL[int(b)]) for r, b in pr.index]; print(pr.round(4).to_string())
print('\n== por rol x tramo T ==')
pt = P.groupby(['rol', 'tb'])[['pnl', 'fee', 'reb', 'usd']].sum(); pt['ev'] = (pt.pnl - pt.fee) / pt.usd
pt.index = [(r, TBL[int(b)]) for r, b in pt.index]; print(pt.round(4).to_string())
# ---- Q2 persistencia
ds = D[D.dia.isin(SEL)]; dt = D[D.dia.isin(TEST)]
def zt(x):
    g = x.groupby('w').net
    m = g.mean(); s = g.std(ddof=1); n = g.size()
    return pd.DataFrame({'net': g.sum(), 'z': m / (s / np.sqrt(n)), 'nd': n, 'usd': x.groupby('w').usd.sum()})
S = zt(ds); T = zt(dt)
S = S[S.index != B_WALLET]
ros = S[(S.net > 0) & (S.z >= 2) & (S.nd >= 4)].index
print('\n== Q2 persistencia: roster SEL (net>0, z>=2, >=4 dias) n=%d de %d activas en SEL' % (len(ros), len(S)))
Tm = T.reindex(S.index)
act = Tm.net.notna()
r_net = Tm.loc[ros].net.fillna(0).sum(); r_pos = (Tm.loc[ros].net.fillna(0) > 0).mean(); r_act = Tm.loc[ros].net.notna().mean()
dec = pd.qcut(S.usd.rank(method='first'), 10, labels=False)
rng = np.random.default_rng(20261026); pn, pp = [], []
rd = dec.loc[ros].value_counts()
for _ in range(1000):
    pick = np.concatenate([rng.choice(dec.index[dec == k], size=c, replace=False) for k, c in rd.items()])
    v = Tm.loc[pick].net.fillna(0); pn.append(v.sum()); pp.append((v > 0).mean())
pn = np.array(pn); pp = np.array(pp)
print('  roster TEST: net %.0f $ | frac net>0 %.3f | activas en TEST %.3f' % (r_net, r_pos, r_act))
print('  placebo (decil de volumen): net media %.0f p95 %.0f | frac>0 media %.3f p95 %.3f | p(net)=%.4f p(frac)=%.4f' % (
    pn.mean(), np.percentile(pn, 95), pp.mean(), np.percentile(pp, 95), (pn >= r_net).mean(), (pp >= r_pos).mean()))
from math import erf, sqrt
cand = T.loc[T.index.intersection(ros)].copy(); cand = cand[cand.nd >= 4]
cand['p'] = 1 - 0.5 * (1 + cand.z.apply(lambda z: erf(z / sqrt(2)) if np.isfinite(z) else -1))
cand = cand.sort_values('p'); m = len(cand); k = 0
for i, pv in enumerate(cand.p.values, 1):
    if pv <= 0.10 * i / m: k = i
cand['bh'] = np.arange(1, m + 1) <= k
print('  candidatas BH q=0,10 en TEST (z unilateral, roster SEL): %d de %d' % (k, m))
# perfil de mecanismo de las persistentes
pers = cand[cand.bh].index.tolist()
out = []
for w in pers + [x for x in tot.index if any(x.startswith(c) for c in CONOC)]:
    q = P[P.w == w]
    if not len(q): continue
    u = q.usd.sum()
    top_pb = q.groupby('pb').usd.sum().idxmax(); top_tb = q.groupby('tb').usd.sum().idxmax(); top_act = q.groupby('act').usd.sum().idxmax()
    out.append(dict(w=w, etiqueta=next((v for c, v in CONOC.items() if w.startswith(c)), ''), persistente=w in pers,
                    net_total=round(float(tot.net.get(w, np.nan)), 1), net_SEL=round(float(S.net.get(w, np.nan)), 1), net_TEST=round(float(T.net.get(w, np.nan)), 1),
                    usd=round(u), fM=round(float(q[q.rol == 'M'].usd.sum() / u), 3), reb_frac=round(float(q.reb.sum() / max(1e-9, tot.net.get(w, np.nan))), 3),
                    banda=PBL[int(top_pb)], T=TBL[int(top_tb)], moneda=top_act, usd_por_fill=round(u / q.n.sum(), 2),
                    dos_lados=round(float(W.n_mkt_2lados.get(w, 0) / max(1, W.n_mkt.get(w, 1))), 3), dias=int(tot.dias.get(w, 0))))
O = pd.DataFrame(out)
print('\n== perfil de persistentes BH + conocidas ==')
print(O.to_string(index=False) if len(O) else 'ninguna')
O.to_csv(sys.argv[1] if len(sys.argv) > 1 else '/dev/null', index=False)
