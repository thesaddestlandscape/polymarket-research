#!/usr/bin/env python3
"""eval_inclusion_forward.py [--prueba D1,D2]  -- evaluador PASIVO diario del detector de INCLUSION congelado (PREREG_INCLUSION.md).
Solo lectura. Dias evaluables: D >= 2026-10-25 (posteriores a la congelacion 24-Oct 11:29Z) con /root/polymarket-research-datalogs/sa_r1/units2_D.csv.gz
(cadena R1 forward, cron 10:40Z). M1F: rasgos de units2 + r60f (binance_bookticker asof RECEPCION, regla de q_techo/s2_feat) + rpre (ventanas_bookticker).
M2: requiere b_seleccion_adversa/datos/units/units_D.pkl + datalogs/q_techo/att_D.csv.gz (si faltan: DATA_BLOCKED, missing != 0).
Salida: /root/polymarket-research-datalogs/detector_inclusion/dia_D.json + estado.json + informe.txt. --prueba: dias anteriores, NO cuentan (carpeta prueba/)."""
import sys, os, json, glob, pickle, argparse
import numpy as np, pandas as pd
ap = argparse.ArgumentParser(); ap.add_argument('--prueba', default=''); a = ap.parse_args()
DL = '/root/polymarket-research-datalogs/'; CONG = '/mnt/HC_Volume_106538179/agentes_datos/detector_ex_ante/'
OUT = DL + 'detector_inclusion/' + ('prueba/' if a.prueba else ''); os.makedirs(OUT, exist_ok=True)
VB = '/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/detector_regimen/datos/ventanas_bookticker.csv.gz'
PRIMER = '2026-10-25'; MIN_COB = 0.90; rng = np.random.default_rng(7)
MOD = {k: pickle.load(open(CONG + 'modelo_%s.pkl' % k, 'rb')) for k in ('M1F', 'M2')}
def r60_bn(df, dias):
    out = np.full(len(df), np.nan)
    fs = [DL + 'binance_bookticker_%s.csv' % d for d in dias if os.path.exists(DL + 'binance_bookticker_%s.csv' % d)]
    if not fs: return out
    X = pd.concat([pd.read_csv(f, usecols=['ts_recepcion_ms', 'activo', 'mid']) for f in fs])
    for coin in ('ETH', 'SOL', 'XRP'):
        S = X[X.activo == coin].sort_values('ts_recepcion_ms'); st = S.ts_recepcion_ms.values / 1000.0; sm = S.mid.values.astype(float)
        m = df.act.values == coin; tt = df.tobs.values[m]
        if not len(st) or not m.any(): continue
        i1 = np.searchsorted(st, tt, 'right') - 1; i0 = np.searchsorted(st, tt - 60, 'right') - 1
        ok = (i1 >= 0) & (i0 >= 0) & (tt - st[np.clip(i1, 0, None)] < 30) & ((tt - 60) - st[np.clip(i0, 0, None)] < 30)
        out[m] = np.where(ok, (sm[np.clip(i1, 0, None)] / sm[np.clip(i0, 0, None)] - 1) * 1e4, np.nan)
    return out
def metricas(df, flag):
    P = df.pnl.values; C = df.c.values; f = C[flag].sum() / C.sum()
    pl = np.array([P[rng.random(len(P)) < f].sum() for _ in range(2000)])
    return {'n': int(len(df)), 'n_top': int(flag.sum()), 'f_eur': float(f), 'EV_pob': float(P.sum() / C.sum()), 'EV_top': float(P[flag].sum() / max(C[flag].sum(), 1e-9)),
            'pnl_top': float(P[flag].sum()), 'exceso': float(P[flag].sum() - f * P.sum()), 'plac_null': [float(x) for x in np.percentile(pl, [50, 95])],
            'p_plac': float((pl >= P[flag].sum()).mean()), 'por_moneda': {c: {'n_top': int((flag & (df.act.values == c)).sum()),
             'brecha': float(P[flag & (df.act.values == c)].sum() / max(C[flag & (df.act.values == c)].sum(), 1e-9) - P[df.act.values == c].sum() / C[df.act.values == c].sum())} for c in ('ETH', 'SOL', 'XRP')}}
def evaluar(D):
    f2 = DL + 'sa_r1/units2_%s.csv.gz' % D
    if not os.path.exists(f2): return {'dia': D, 'estado': 'SIN_UNITS2'}
    U = pd.read_csv(f2); U = U[U.act.isin(['ETH', 'SOL', 'XRP'])].copy()
    U['coin'] = U.act.map({'ETH': 0, 'SOL': 1, 'XRP': 2}); U['lado'] = (U.lado_c == 'YES').astype(int); U['sg'] = np.where(U.lado == 1, 1.0, -1.0)
    U['depth_ticks'] = (U.bb - U.pc) / 0.01; U['gap15'] = U.b15 - U.bb; U['tobs'] = U.ts - 4.0
    d0 = (pd.Timestamp(D) - pd.Timedelta(days=1)).strftime('%Y-%m-%d'); U['r60f'] = r60_bn(U, [d0, D]) * U.sg
    V = pd.read_csv(VB, usecols=['coin', 'tmin', 'rpre']); U['tmin'] = ((U.fin.values - 300) // 60).astype(np.int64)
    U = U.merge(V.rename(columns={'coin': 'act'}), on=['act', 'tmin'], how='left'); U['rpre_s'] = U.rpre * U.sg
    fp = DL + 'etiquetado_pasivo_B/poblacion/pob_%s.csv.gz' % D          # respaldo: rpre_bps (ya con signo del lado) del etiquetador L1b
    if os.path.exists(fp):
        Pb = pd.read_csv(fp, usecols=['maker', 'mid', 'lado', 'rpre_bps']).rename(columns={'lado': 'lado_c'})
        U['_k'] = U.maker.astype(str) + '|' + U.mkt.astype(str) + '|' + U.lado_c
        Pb['_k'] = Pb.maker.astype(str) + '|' + Pb['mid'].astype(str) + '|' + Pb.lado_c
        mp = dict(zip(Pb._k, Pb.rpre_bps)); alt = U._k.map(mp)
        res_cmp = (U.rpre_s.notna() & alt.notna()); U['_rpre_coinc'] = float(np.corrcoef(U.rpre_s[res_cmp], alt[res_cmp])[0, 1]) if res_cmp.sum() > 50 else np.nan
        U['rpre_s'] = U.rpre_s.fillna(alt)
    U['CON'] = np.where(U.rpre_s.isna(), np.nan, (U.rpre_s >= 7.7).astype(float)); U['pnl'] = U.p
    res = {'dia': D, 'corr_rpre_ventanas_vs_pob': float(U['_rpre_coinc'].iloc[0]) if '_rpre_coinc' in U and len(U) else None, 'cobertura': {k: float(U[k].notna().mean()) for k in ('r60f', 'rpre_s', 'bb', 'b15', 'vol30ws')}}
    mf = MOD['M1F']
    if min(res['cobertura'].values()) < MIN_COB: res['M1F'] = {'estado': 'DATA_BLOCKED', 'motivo': 'cobertura < %.2f' % MIN_COB}
    else:
        ev = mf['modelo'].predict_proba(U[mf['feats']])[:, 1] / U.pc.values - 1; res['M1F'] = metricas(U, ev >= mf['corte_ev']); res['M1F']['estado'] = 'OK'
        res['deriva_medianas'] = {k: float(np.nanmedian(U[k])) for k in mf['feats'] if k not in ('coin', 'lado')}
    up = '/root/polymarket-research/experimentos/5m_barato/b_seleccion_adversa/datos/units/units_%s.pkl' % D; at = DL + 'q_techo/att_%s.csv.gz' % D
    res['M2'] = {'estado': 'DATA_BLOCKED', 'motivo': 'faltan units_D.pkl (build_units) y/o att_D (s1_attach): rasgos FULL no se producen en forward'} if not (os.path.exists(up) and os.path.exists(at)) else {'estado': 'PENDIENTE_CABLEAR'}
    return res
dias = a.prueba.split(',') if a.prueba else sorted(os.path.basename(f)[7:17] for f in glob.glob(DL + 'sa_r1/units2_*.csv.gz') if os.path.basename(f)[7:17] >= PRIMER)
for D in dias:
    if not a.prueba and os.path.exists(OUT + 'dia_%s.json' % D): continue      # idempotente: un dia evaluado no se recalcula
    r = evaluar(D); json.dump(r, open(OUT + 'dia_%s.json' % D, 'w'), indent=1)
# gate acumulado (PREREG_INCLUSION.md sec. 3)
R = [json.load(open(f)) for f in sorted(glob.glob(OUT + 'dia_*.json'))]
lin = []
for nm in ('M1F', 'M2'):
    ok = [r for r in R if r.get(nm, {}).get('estado') == 'OK']
    if not ok: lin.append('%s: 0 dias evaluables (%s)' % (nm, ', '.join(sorted({r.get(nm, {}).get('estado', r.get('estado', '?')) for r in R})) or 'sin dias')); continue
    ex = np.array([r[nm]['exceso'] for r in ok]); br = np.array([r[nm]['EV_top'] - r[nm]['EV_pob'] for r in ok]); ntop = sum(r[nm]['n_top'] for r in ok)
    bs = lambda x: np.percentile([rng.choice(x, len(x)).mean() for _ in range(5000)], 5)
    pp = 1 - np.prod([1 - r[nm]['p_plac'] for r in ok]) if False else float(np.mean([r[nm]['p_plac'] for r in ok]))
    crit = {'dias>=15': len(ok) >= 15, 'n_top>=3000': ntop >= 3000, 'exceso>0': ex.sum() > 0, 'IC90dia_exceso_lo>0': bs(ex) > 0, 'sin2mejores>0': np.sort(ex)[:-2].sum() > 0 if len(ex) > 2 else False,
            'brecha>=0.03': br.mean() >= 0.03, 'IC90dia_brecha_lo>0': bs(br) > 0, 'dias+>=60%': (ex > 0).mean() >= 0.60}
    est = 'ACUMULANDO' if len(ok) < 15 else ('PASA (candidata; requiere OK Javi)' if all(crit.values()) else 'REFUTADO (falsador sec. 4)')
    lin.append('%s: dias %d, n_top %d, exceso %+.1f, brecha media %+.4f, p_plac medio %.3f -> %s | %s' % (nm, len(ok), ntop, ex.sum(), br.mean(), pp, est, crit))
txt = '\n'.join(lin); open(OUT + 'informe.txt', 'w').write(txt + '\n'); print(txt)
