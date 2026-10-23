"""PREREG_P3: AUC por senal (ELEGIR y MEDIR), logit en ELEGIR, umbrales de tasa 5/15 % sobre ticks validos de ELEGIR -> datos/sig_modelo_ELEGIR.json"""
import os, json, numpy as np, pandas as pd
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos'); DL = '/root/polymarket-research-datalogs/cola_vs_cruce/'
NOMS = ['SCANC', 'SFINO', 'SCAIDA', 'SVEL', 'SIMB', 'SFLUJO', 'SEDAD']
def auc(y, x):
    m = np.isfinite(x); y = y[m]; x = x[m]; n1 = y.sum(); n0 = len(y) - n1
    if n1 == 0 or n0 == 0: return np.nan
    r = pd.Series(x).rank().values; return (r[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0)
A = {}
for F in ('ELEGIR', 'MEDIR'):
    p = os.path.join(D, f'sigfill_{F}.csv')
    if os.path.exists(p): X = pd.read_csv(p); A[F] = X[X.fill == 1].dropna(subset=NOMS)
E = A['ELEGIR']; y = E.clase.isin(['X1', 'X2']).values.astype(float)
mu = E[NOMS].mean().values; sd = E[NOMS].std().values + 1e-12; Xz = (E[NOMS].values - mu) / sd
w = np.zeros(len(NOMS)); b0 = 0.0
for _ in range(3000):   # logistica por gradiente (sin regularizar), estandarizada
    z = Xz @ w + b0; pr = 1 / (1 + np.exp(-z)); gw = Xz.T @ (pr - y) / len(y); gb = (pr - y).mean(); w -= 0.5 * gw; b0 -= 0.5 * gb
for F, X in A.items():
    print(F, 'rellenos', len(X), 'cuota X2', round((X.clase == 'X2').mean(), 3), 'cuota X1uX2', round(X.clase.isin(['X1', 'X2']).mean(), 3))
    lg = ((X[NOMS].values - mu) / sd) @ w + b0
    for nm in NOMS + ['LOGIT']:
        x = lg if nm == 'LOGIT' else X[nm].values.astype(float)
        print(f'  {nm:7s} AUC X2 {auc((X.clase == "X2").values.astype(int), x):.3f}  AUC X1uX2 {auc(X.clase.isin(["X1","X2"]).values.astype(int), x):.3f}')
print('coef logit (estandarizados)', dict(zip(NOMS, np.round(w, 3))), 'b0', round(b0, 3))
Z = np.load(DL + 'sig_ELEGIR.npz'); T = np.concatenate([Z[k] for k in Z.files]).astype(float); T = T[np.isfinite(T[:, 1])]
um = {}
for j, nm in enumerate(NOMS):
    x = T[:, j]; x = x[np.isfinite(x)]; um[nm] = {'05': float(np.quantile(x, 0.95)), '15': float(np.quantile(x, 0.85))}
lgT = np.nan_to_num((T - mu) / sd) @ w + b0; um['LOGIT'] = {'05': float(np.quantile(lgT, 0.95)), '15': float(np.quantile(lgT, 0.85))}
json.dump(dict(mu=mu.tolist(), sd=sd.tolist(), coef=w.tolist(), b0=float(b0), umbral=um, n_ticks=int(len(T))), open(os.path.join(D, 'sig_modelo_ELEGIR.json'), 'w'), indent=1)
print('umbrales', {k: {a: round(b, 3) for a, b in v.items()} for k, v in um.items()}, 'ticks', len(T))
