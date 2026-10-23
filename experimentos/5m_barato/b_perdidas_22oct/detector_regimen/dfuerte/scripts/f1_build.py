#!/usr/bin/env python3
"""f1_build.py <backfill|dic_ene|y2025|reciente> - tabla de unidades (T=180,120) con rasgos D-FUERTE. Salida datalogs/regimen_5m/dfuerte/units_<src>.pkl (+ windows_<src>.pkl para 'reciente')."""
import sys, os, numpy as np, pandas as pd, warnings, time
warnings.filterwarnings('ignore')
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import dfuerte_lib as DL
SRC = sys.argv[1]; OUT = '/root/polymarket-research-datalogs/regimen_5m'
z = np.load(f'{OUT}/full_{SRC}.npz'); coins = sorted({k[:-3] for k in z.files if k.endswith('_m0')}, key=DL.ALLC.index)
Z = {c: (int(z[c + '_m0']), z[c + '_X']) for c in coins}
t0 = time.time(); W = DL.all_features(Z, coins); print(SRC, 'ventanas', len(W), 'monedas', coins, 'seg', round(time.time() - t0), flush=True)
U = pd.concat([DL.to_units(W, T) for T in (180, 120)], ignore_index=True)
if SRC == 'dic_ene':   # desenlace oficial Jon-Becker (de r1_panel, T-independiente por ventana)
    P = pd.read_csv(os.path.join(HERE, '..', '..', 'datos', 'panel_dic_ene.csv.gz'), usecols=['coin', 'tmin', 'T', 'win_oficial']).drop_duplicates(['coin', 'tmin', 'T'])
    U = U.merge(P, on=['coin', 'tmin', 'T'], how='left')
else: U['win_oficial'] = np.nan
keep = [c for c in U.columns if c not in ('z15raw', 'z60raw')]
U[keep].to_pickle(f'{OUT}/dfuerte/units_{SRC}.pkl')
if SRC == 'reciente': W.to_pickle(f'{OUT}/dfuerte/windows_{SRC}.pkl')
print('unidades', len(U), U.groupby(['T', 'con']).size().to_dict(), 'dias', U.dia.nunique(), 'NaN medio rasgos', round(float(U[DL.FEATS].isna().mean().mean()), 4), flush=True)
print(U[DL.FEATS].isna().mean().sort_values(ascending=False).head(8).round(3).to_dict())
