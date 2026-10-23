#!/usr/bin/env python3
"""btc_cosechadores.py -- ledger BTC 5m 17-21 Oct de 0x21f4c1a1 / 0xaa1a4f31 / 0x41e2e1cc (VOL/m5_onchain, filas F con maker == wallet;
taker == exchange => orden tomadora propia). Mapa token->mercado de datalogs/sa_ms/btc_ms_D.npz; desenlace maker_ms_desenlaces_cache.json.
Salida ../datos/btc_cosech_fills.csv.gz y ../datos/btc_cosech.txt (descriptivo)."""
import os, gzip, json, numpy as np, pandas as pd
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos')
EXCH = '0xe111180000d2663c0091e4f400237545b87b996b'
WS = {'0x21f4c1a1be34a39a7bc20985df4b7e5a39fb691d', '0xaa1a4f31c010d4a63fc49770d4ca2d69ea370602', '0x41e2e1ccf1e4940029af02259a31c6b89b9fa354'}
DES = json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
rows = []
for d in ['2026-10-%02d' % i for i in range(17, 22)]:
    z = np.load(f'/root/polymarket-research-datalogs/sa_ms/btc_ms_{d}.npz')
    tm = {}
    for t, (act, marco, mid, fin, lado) in zip(z['tokens'], z['tmap']):
        if str(marco) == '5min': tm[str(t)] = (str(mid), int(pd.Timestamp(str(fin)).timestamp()), str(lado))
    with gzip.open(f'/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_{d}.csv.gz', 'rt') as f:
        for ln in f:
            c = ln.rstrip('\n').split(',')
            if c[0] != 'F' or len(c) < 13: continue
            w = c[6].lower()
            if w not in WS: continue
            k = tm.get(c[9])
            if k is None: continue
            rows.append((d, float(c[2]), c[3], int(c[4]), w, 'T' if c[7].lower() == EXCH else 'M', int(c[8]), k[0], k[1], k[2], float(c[10]), float(c[11]), float(c[12] or 0)))
    print(d, len(rows), flush=True)
F = pd.DataFrame(rows, columns=['dia', 'ts', 'tx', 'li', 'wallet', 'rol', 'side', 'mid', 'fin', 'lado', 'ma', 'ta', 'fee'])
F['des'] = F.mid.map(DES)
buy = F.side == 0
F['acc'] = np.where(buy, F.ta, F.ma); F['usd'] = np.where(buy, F.ma, F.ta)
F['lado_ef'] = np.where(buy, F.lado, np.where(F.lado == 'YES', 'NO', 'YES')); F['cost_ef'] = np.where(buy, F.usd, F.acc - F.usd)
F['fee_usd'] = np.where(F.rol == 'T', F.fee, 0.0); F['T'] = F.fin - F.ts
F.to_csv(os.path.join(OUT, 'btc_cosech_fills.csv.gz'), index=False, compression='gzip')
out = []
cov = F.drop_duplicates('mid').des.notna().mean(); out.append(f'cobertura desenlace (mercados) {cov:.3f}')
F = F[F.des.notna()]
for w, x in F.groupby('wallet'):
    g = x.groupby(['mid', 'lado_ef']).agg(Q=('acc', 'sum'), C=('cost_ef', 'sum'), fee=('fee_usd', 'sum')).unstack(fill_value=0)
    g.columns = [f'{a}_{b}' for a, b in g.columns]
    for c in ('Q_YES', 'Q_NO', 'C_YES', 'C_NO', 'fee_YES', 'fee_NO'):
        if c not in g: g[c] = 0.0
    des = x.drop_duplicates('mid').set_index('mid').des; dia = x.drop_duplicates('mid').set_index('mid').dia
    g['vol'] = g.C_YES + g.C_NO; g['pago'] = np.where(des.reindex(g.index) == 'YES', g.Q_YES, g.Q_NO); g['fee'] = g.fee_YES + g.fee_NO
    g['pnl'] = g.pago - g.vol - g.fee; g['Qp'] = np.minimum(g.Q_YES, g.Q_NO)
    pc = np.where(g.Qp > 0, g.C_YES / g.Q_YES.where(g.Q_YES > 0, 1) + g.C_NO / g.Q_NO.where(g.Q_NO > 0, 1), np.nan)
    g['par'] = g.Qp * (1 - np.nan_to_num(pc)); g['res'] = g.pnl + g.fee - g.par; g['dia'] = dia.reindex(g.index)
    g['res_frac'] = np.abs(g.Q_YES - g.Q_NO) / (g.Q_YES + g.Q_NO)
    byd = (g.groupby('dia').pnl.sum() / g.groupby('dia').vol.sum()).round(4).to_dict()
    mk = x[x.rol == 'M'].cost_ef.sum() / x.cost_ef.sum()
    # reequilibrado e inventario
    red = []; mx = []
    for mid, z in x.sort_values(['ts', 'li']).groupby('mid'):
        s = np.where(z.lado_ef == 'YES', 1.0, -1.0) * z.acc.values; I = np.cumsum(s); mx.append(np.abs(I).max())
        red += [int(np.sign(s[i]) != np.sign(I[i - 1])) for i in range(1, len(s)) if I[i - 1] != 0]
    out.append(f"{w[:10]}: merc {len(g)} vol {g.vol.sum():,.0f} $ | PnL/vol {g.pnl.sum()/g.vol.sum():+.4f} | par {g.par.sum()/g.vol.sum():+.4f} residuo {g.res.sum()/g.vol.sum():+.4f} comision {-g.fee.sum()/g.vol.sum():+.4f} | maker {mk:.2f} | ventas {(x.side==1).mean():.2f} | coste par med {np.nanmedian(pc):.3f} | res_frac med {g.res_frac.median():.2f} | max|I| med {np.median(mx):.0f} | P(reduce |I|) {np.mean(red):.3f} | acc/relleno med {x.acc.median():.1f} | T 10/50/90 {np.percentile(x['T'],[10,50,90]).round(0).tolist()} | por dia {byd}")
txt = '\n'.join(out); print(txt); open(os.path.join(OUT, 'btc_cosech.txt'), 'w').write(txt + '\n')
