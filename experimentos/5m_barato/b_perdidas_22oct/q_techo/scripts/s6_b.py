#!/usr/bin/env python3
"""s6_b.py -- PREREG Q-TECHO seccion 6: reglas que solo necesitan (moneda, lado, precio, instante) aplicadas a las posiciones REALES de B (H47-B, 202, 20-23 Oct). Descriptivo (n bajo)."""
import sys, glob, os
import numpy as np, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from qlib import *
DL = '/root/polymarket-research-datalogs/'; OUT = []
def P(*a):
    s = ' '.join(str(x) for x in a); OUT.append(s); print(s, flush=True)
p = pd.read_csv('/root/polymarket-research/experimentos/5m_barato/contabilidad_wallet_dedicada/posiciones.csv'); p = p[p.experimento == 'H47-B'].copy()
p = p[p.estado.isin(['liquidada_ganada', 'liquidada_perdida'])].copy()
p['act'] = p.mercado.str.split('-').str[0].str.upper(); p['sg'] = np.where(p.outcome == 'Up', 1.0, -1.0); p['lado_c'] = np.where(p.sg > 0, 'YES', 'NO')
p['ts'] = (pd.to_datetime(p.fecha_primer_fill_utc, utc=True) - pd.Timestamp('1970-01-01', tz='UTC')).dt.total_seconds(); p['fin'] = p.mercado.str.rsplit('-', n=1).str[1].astype(int) + 300
p['pc'] = p.precio_medio; p['c'] = p.coste; p['p'] = p.pnl_realizado; p['gana_f'] = (p.estado == 'liquidada_ganada').astype(float); p['cierre'] = p.fin; p['dia'] = p.fecha_primer_fill_utc.str[:10]; p['tobs'] = p.ts - 4
p = p[p.act.isin(COINS)].reset_index(drop=True)
# Binance r60f
r60 = np.full(len(p), np.nan)
for coin in COINS:
    parts = []
    for f in sorted(glob.glob(DL + 'binance_bookticker_2026-10-*.csv')):
        if '2026-10-19' <= f[-14:-4] <= '2026-10-23':
            x = pd.read_csv(f, usecols=['ts_recepcion_ms', 'activo', 'mid']); parts.append(x[x.activo == coin][['ts_recepcion_ms', 'mid']])
    S = pd.concat(parts).sort_values('ts_recepcion_ms'); st = S.ts_recepcion_ms.values / 1000.0; sm = S.mid.values.astype(float)
    m = (p.act.values == coin); tt = p.tobs.values[m]; i1 = np.searchsorted(st, tt, 'right') - 1; i0 = np.searchsorted(st, tt - 60, 'right') - 1
    ok = (i1 >= 0) & (i0 >= 0) & (tt - st[np.clip(i1, 0, None)] < 30) & ((tt - 60) - st[np.clip(i0, 0, None)] < 30)
    r60[m] = np.where(ok, (sm[np.clip(i1, 0, None)] / sm[np.clip(i0, 0, None)] - 1) * 1e4, np.nan)
p['r60f'] = r60 * p.sg
VB = '/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/detector_regimen/datos/ventanas_bookticker.csv.gz'
V = [pd.read_csv(VB, usecols=['coin', 'tmin', 'rpre'])] + [pd.read_csv(f, usecols=['coin', 'tmin', 'rpre']) for f in sorted(glob.glob(DL + 'regimen_5m/etiquetas/regimen_*.csv.gz'))]
V = pd.concat(V, ignore_index=True).drop_duplicates(['coin', 'tmin'], keep='first').rename(columns={'coin': 'act'})
p['tmin'] = (p.fin - 300) // 60; p = p.merge(V, on=['act', 'tmin'], how='left'); p['rpre_s'] = p.rpre * p.sg; p['CON'] = np.where(p.rpre_s.isna(), np.nan, (p.rpre_s >= 7.7).astype(float))
P(f'# B real H47-B liquidadas n={len(p)}, EUR {p.c.sum():.1f}, PnL {p.p.sum():+.2f}, EV {p.p.sum()/p.c.sum():+.4f}, hit {p.gana_f.mean():.3f}; dias {p.dia.value_counts().sort_index().to_dict()}; cobertura r60f {p.r60f.notna().mean():.3f} rpre {p.rpre.notna().mean():.3f}')
cl = clus(p)
def rep(nom, skip):
    s = stats(p, skip); lo, hi = boot(-p.p.values * skip, cl); P(f'{nom}: skip {s["n_skip"]}/{s["n"]} ret {s["ret"]:.3f} EV_all {s["ev_all"]:+.3f} EV_ret {s["ev_ret"]:+.3f} EV_skip {s["ev_skip"]:+.3f} dPnL {s["dpnl"]:+.2f} IC90 cierre [{lo:+.2f},{hi:+.2f}]')
T = pd.read_pickle(DL + 'q_techo/tab.pkl'); T = T[T.act.isin(COINS)]
mp = {a: MapQ().fit(T[T.act == a]) for a in COINS}; p['q_MAP'] = np.concatenate([mp[a].predict(p[p.act == a]) for a in COINS])[np.argsort(np.concatenate([np.where(p.act.values == a)[0] for a in COINS]))]
P('MAP (tramo x moneda, 13 dias):', {a: {i: round(v, 4) for i, v in mp[a].tab.items()} for a in COINS})
import json
thr = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos', 'congelado_desc.json')))['r60thr']
rep('R_r60 (umbral DESC)', (p.r60f.values <= p.act.map(thr).values) & p.r60f.notna().values)
rep('R0 (CON)', p.CON.values == 1)
for m in (0.0, 0.01, 0.02, 0.04): rep(f'MAP techo m={m}', p.pc.values > p.q_MAP.values - m)
P('posiciones B por dia (EV):', {d: (round(g.p.sum() / g.c.sum(), 3), len(g)) for d, g in p.groupby('dia')})
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos', 'b_descriptivo.txt'), 'w').write('\n'.join(OUT))
