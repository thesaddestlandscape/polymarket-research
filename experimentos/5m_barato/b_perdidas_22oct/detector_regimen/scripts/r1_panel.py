#!/usr/bin/env python3
"""r1_panel.py <fuente: backfill|dic_ene|bookticker> - panel de unidades longshot proxy (PREREG_RTEND sec.2-3). Salida datos/panel_<fuente>.csv.gz y datos/ventanas_<fuente>.csv.gz (una fila por apertura con rasgos+clases)."""
import sys, os, glob, json, numpy as np, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import regimen_lib as L
try:
    from scipy.special import ndtr as Phi
except Exception:
    Phi = L.Phi
SRC = sys.argv[1]; HERE = os.path.dirname(os.path.abspath(__file__)); DAT = os.path.join(HERE, '..', 'datos')
OUT = '/root/polymarket-research-datalogs/regimen_5m'
z = np.load(f'{OUT}/barras_{SRC}.npz'); coins = sorted({k[:-3] for k in z.files if k.endswith('_m0')})
Bs = {c: L.base_series(int(z[c + '_m0']), z[c + '_P']) for c in coins}
# rejilla comun de aperturas (multiplo de 5 min), con 1500 min de calentamiento y 6 min de cola
lo = max(B['m0'] for B in Bs.values()) + 1500; hi = min(B['m0'] + B['n'] for B in Bs.values()) - 8
tm = np.arange((lo + 4) // 5 * 5, hi, 5)
# coherencia: signo de r60 en BTC,ETH,SOL,XRP
sg = []
for c in L.COH_COINS:
    if c in Bs:
        B = Bs[c]; r60 = (L.lp_at(B, tm - B['m0']) - L.lp_at(B, tm - 60 - B['m0'])); sg.append(np.sign(r60))
coh = np.abs(np.nansum(sg, axis=0)); cohn = np.sum([np.isfinite(s) for s in sg], axis=0); coh = np.where(cohn == len(sg), coh, np.nan)
rows = []; units = []
# D-class por moneda
for c in coins:
    B = Bs[c]; io = tm - B['m0']
    f = L.features_open(B, io)
    df = pd.DataFrame({'coin': c, 'tmin': tm, 'dia': tm // 1440, **f, 'COH': coh})
    erd = L.er_dia_prev_table(B, sorted(set(tm // 1440) | {tm.min() // 1440 - k for k in range(1, 16)}))
    dcl = L.d_class(erd); df['D'] = df.dia.map(dcl).fillna('NA'); df['ER_dia_prev'] = (df.dia - 1).map(erd)
    df = L.add_classes(df); rows.append(df)
    for T in (180, 120):
        iT = io + T // 60; ret = L.lp_at(B, iT) - L.lp_at(B, io); sT = L.rms(B, iT, 60); m = (300 - T) / 60
        zz = np.abs(ret) / (sT * np.sqrt(m)); q = Phi(-zz); fin = L.lp_at(B, io + 5) - L.lp_at(B, io)
        up_side = ret < 0                                  # el lado que va perdiendo es Up si el precio bajo
        win = np.where(up_side, fin >= 0, fin < 0).astype(float); win[~np.isfinite(fin) | ~np.isfinite(ret)] = np.nan
        u = pd.DataFrame({'coin': c, 'tmin': tm, 'T': T, 'ret_bps': ret * 1e4, 'z': zz, 'q': q, 'lado_up': up_side, 'win_proxy': win,
                          'rpre': f['rpre'], 'dia': tm // 1440})
        u = u[(u.q >= 0.10) & (u.q < 0.30) & np.isfinite(u.win_proxy) & np.isfinite(u.rpre) & (u.ret_bps != 0)]
        units.append(u)
W = pd.concat(rows, ignore_index=True); U = pd.concat(units, ignore_index=True)
cols = ['coin', 'tmin', 'dia', 'R', 'D', 'COH', 'ER60', 'VR240', 'VOLR', 'DAYT', 'ER_dia_prev', 'med_ER']
U = U.merge(W[cols], on=['coin', 'tmin', 'dia'], how='left')
# desenlace oficial para dic_ene (Jon-Becker)
if SRC == 'dic_ene':
    import pyarrow.parquet as pq
    off = {}
    for f in sorted(glob.glob('/root/jonbecker/data/polymarket/markets/markets_2[2-9]*.parquet')) + sorted(glob.glob('/root/jonbecker/data/polymarket/markets/markets_3*.parquet')):
        t = pq.read_table(f, columns=['slug', 'outcome_prices', 'closed']).to_pandas(); t = t[t.slug.str.contains('updown-5m', na=False) & t.closed]
        for s, p in zip(t.slug, t.outcome_prices):
            try:
                pr = json.loads(p); c = s.split('-')[0].upper(); ep = int(s.split('-')[-1])
                if pr[0] in ('1', '0', 1, 0, '1.0', '0.0') and pr[1] in ('1', '0', 1, 0, '1.0', '0.0'): off[(c, ep // 60)] = 1 if float(pr[0]) == 1 else 0
            except Exception: pass
    U['up_oficial'] = [off.get((c, t), np.nan) for c, t in zip(U.coin, U.tmin)]
    U['win_oficial'] = np.where(U.lado_up, U.up_oficial == 1, U.up_oficial == 0).astype(float); U.loc[U.up_oficial.isna(), 'win_oficial'] = np.nan
    print('oficial: ventanas con desenlace', len(off), 'unidades con oficial', int(U.win_oficial.notna().sum()), 'de', len(U), '; acuerdo proxy-oficial', float((U.win_oficial == U.win_proxy)[U.win_oficial.notna()].mean()))
W.to_csv(f'{DAT}/ventanas_{SRC}.csv.gz', index=False); U.to_csv(f'{DAT}/panel_{SRC}.csv.gz', index=False)
print(SRC, 'ventanas', len(W), 'unidades', len(U), 'dias', U.dia.nunique(), U.groupby('coin').size().to_dict(), flush=True)
