#!/usr/bin/env python3
"""b5_enlace.py -- EXPLORATORY: ¿la brecha CON-CONTRA diaria de la proxy (precio de modelo) acompana a la de los rellenos del maker y a la del ask real? (13 y 17 dias)."""
import sys, os, json, glob
import numpy as np, pandas as pd
DET = '/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/detector_regimen'
OUT = []
def P(*a):
    s = ' '.join(str(x) for x in a); OUT.append(s); print(s, flush=True)
# proxy diaria (bookticker, 24-Sep..22-Oct)
D = pd.read_csv(f'{DET}/datos/panel_bookticker.csv.gz', usecols=['coin', 'tmin', 'T', 'q', 'lado_up', 'win_proxy', 'rpre', 'dia'])
U = D[D.coin.isin(['ETH', 'SOL', 'XRP']) & (D['T'] == 180) & D.win_proxy.notna()].copy(); U['sd'] = np.where(U.lado_up, 1.0, -1.0)
U['cls'] = np.where(U.rpre.abs() < 7.7, 'NEU', np.where(np.sign(U.rpre) == U.sd, 'CON', 'CONTRA')); U['e'] = U.win_proxy - U.q
U['d'] = pd.to_datetime(U.dia * 86400, unit='s').dt.strftime('%Y-%m-%d')
def dl(g, num, den):
    a = g[g.cls == 'CON']; b = g[g.cls == 'CONTRA']
    return a[num].sum() / a[den].sum() - b[num].sum() / b[den].sum() if len(a) >= 20 and len(b) >= 20 else np.nan
prox = U.groupby('d').apply(lambda g: dl(g, 'e', 'q'), include_groups=False)
# maker
T = pd.read_pickle('/mnt/HC_Volume_106538179/agentes_datos/b_regimen/tab_reg.pkl'); T = T[T.cls.isin(['CON', 'CONTRA'])]
mk = T.groupby('dia').apply(lambda g: dl(g, 'p', 'c'), include_groups=False)
# maker en acierto-precio (hit - pc, ponderado EUR)
T['ex'] = (T.gana_f - T.pc) * T.c / T.pc
mk2 = T.groupby('dia').apply(lambda g: dl(g, 'ex', 'c'), include_groups=False)
# ask real por dia (de preal_resultados no hay serie; recalcular rapido)
sys.path.insert(0, DET + '/scripts'); import preal_analisis as PA
desen = json.load(open('/root/polymarket-research-datalogs/preal/desenl_cache.json'))
W = pd.read_csv(DET + '/datos/ventanas_bookticker.csv.gz', usecols=['coin', 'tmin', 'rpre'])
et = [pd.read_csv(f, usecols=['coin', 'tmin', 'rpre']) for f in sorted(glob.glob('/root/polymarket-research-datalogs/regimen_5m/etiquetas/regimen_*.csv.gz'))]
W = pd.concat([W] + et, ignore_index=True).drop_duplicates(['coin', 'tmin'], keep='first').rename(columns={'rpre': 'rpre_bar'})
X, dias = PA.carga(); Y = PA.prep(PA.largo(X, 180, 250), W, desen)
p, c = PA.precio_cols(Y, 'ask'); m = Y.coin.isin(['ETH', 'SOL', 'XRP']) & Y.vivo & ~Y.cruz & Y.ask.notna() & Y.ask.ge(0.10) & Y.ask.lt(0.30) & Y.gana.notna() & Y.cls.isin(['CON', 'CONTRA']) & p.notna()
A = Y[m].copy(); A['cst'] = c[m]; A['pnl'] = A.gana - A.cst
ask = A.groupby('dia').apply(lambda g: dl(g.assign(cls=g.cls), 'pnl', 'cst'), include_groups=False)
df = pd.DataFrame({'proxy_modelo': prox, 'maker_fill_EV': mk, 'maker_hit_menos_precio': mk2, 'ask_real': ask})
P(df.round(3).to_string())
from scipy.stats import spearmanr
for a, b in (('proxy_modelo', 'maker_fill_EV'), ('proxy_modelo', 'ask_real'), ('ask_real', 'maker_fill_EV'), ('proxy_modelo', 'maker_hit_menos_precio')):
    s = df[[a, b]].dropna(); r = spearmanr(s[a], s[b]); P(f'Spearman({a},{b}) n={len(s)} dias: {r.statistic:+.2f} p={r.pvalue:.3f}')
P('medias (dias comunes con maker):', df.dropna(subset=['maker_fill_EV']).mean().round(3).to_dict())
P('proxy_modelo en todo 24-Sep..22-Oct: media', round(float(prox.mean()), 3), 'sd diaria', round(float(prox.std()), 3), 'n', int(prox.notna().sum()), '| dias con Delta<0:', int((prox < 0).sum()))
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos', 'b5_resultados.txt'), 'w').write('\n'.join(OUT))
