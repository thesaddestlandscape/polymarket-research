"""F8 wf_f8.py: walk-forward expansivo P0/P1/P2 (HGB) + gate PREREG. Politica congelada por dia ANTES de evaluar (cuantil del TRAIN que retiene el 30 % del EUR).
Entrada: datalogs/f8_estructura/tabla.parquet. Salida: datos/f8_resultados.json, datos/f8_scores.parquet (en datalogs), datos/f8_resumen.txt"""
import json, os, sys, pickle
import numpy as np, pandas as pd
from sklearn.ensemble import HistGradientBoostingRegressor
DL = '/root/polymarket-research-datalogs/calibracion_etiqueta/'; OUTD = os.path.dirname(os.path.abspath(__file__)) + '/../datos/'
SEED = 20261025; rng = np.random.default_rng(SEED); NB = 5000; NPERM = 500; ZBONF = 2.13
V = pd.read_parquet(DL + 'tabla_cal_off1.parquet')
V = V.drop_duplicates(['mercado', 'lado', 't0_recv_ms'])
V['dia'] = pd.to_datetime(V.t0_recv_ms, unit='ms', utc=True).dt.strftime('%Y-%m-%d')
cov = {}
for d, g in V.groupby('dia'):
    f = g.relleno_pes == 1
    cov[d] = {'vidas': int(len(g)), 'censuradas': int(g.censurada.sum()), 'rellenas': int(f.sum()), 'rellenas_sin_desenlace': int((f & (g.gana.isna())).sum()),
              'vacias_gana_total': int(g.gana.isna().sum()), 'fill_rate': float(f.mean())}
V = V[V.censurada == 0].copy()
V = V[~((V.relleno_pes == 1) & V.gana.isna())].copy()          # rellena sin desenlace oficial: no evaluable (contada arriba); NO se filtran las no rellenas con gana vacio
V['c'] = 5.0 * V.bl; V['y'] = np.where(V.relleno_pes == 1, V.pnl_5acc_si_relleno.astype(float), 0.0)
V['sg'] = np.where(V.lado == 'YES', 1.0, -1.0); V['lado_i'] = (V.lado == 'YES').astype(int)
V['hora'] = pd.to_datetime(V.t0_recv_ms, unit='ms', utc=True).dt.hour
V['fin_sem'] = (pd.to_datetime(V.dia).dt.dayofweek >= 5).astype(int)
cm = {'ETH': 0, 'SOL': 1, 'XRP': 2}; V['coin_i'] = V.coin.map(cm)
for k in ('bn_r300ms_bps', 'bn_r5s_bps', 'bn_r60s_bps'): V[k + '_s'] = V[k] * V.sg
V['logQ0'] = np.log(V.Q0.clip(lower=0.01))
P0 = ['b', 'T_s', 'hora', 'coin_i', 'lado_i', 'fin_sem']
P1 = P0 + ['ba', 'as_', 'spread', 'Q0', 'logQ0', 'bn_r300ms_bps_s', 'bn_r5s_bps_s', 'bn_r60s_bps_s', 'bn_rng60_bps', 'bn_edad_ms']
P2 = P1 + ['pm_edad_ms', 'pm_n120', 'pm_usd120', 'pc_n120', 'pc_usd120', 'pc_edad_ms', 'fl_usd_all', 'fl_n_all', 'fl_acc_all', 'fl_usd_rep200', 'fl_usd_bot2000', 'fl_share_rep200', 'fl_share_bot2000']
FE = {'P0': P0, 'P1': P1, 'P2': P2}
KEEP = sorted(set(P2) | {'bl', 'dia', 'c', 'y', 'coin', 'cierre', 'mercado', 'lado', 't0_recv_ms', 'relleno_pes', 'fin_sem', 'hora', 'b', 'T_s', 'Q0', 'ba', 'spread', 'bn_r60s_bps_s', 'lado_i', 'coin_i'})
V = V[KEEP].copy()
for k in V.columns:
    if V[k].dtype == np.float64 and k not in ('c', 'y', 't0_recv_ms'): V[k] = V[k].astype(np.float32)
MAIN = V.coin.isin(['ETH', 'SOL', 'XRP']).values
dias = sorted(V.dia.unique()); EVAL = [d for d in dias if d >= '2026-10-08']
dstart = {d: int(pd.Timestamp(d, tz='UTC').timestamp()) for d in dias}
def corte(score, c, frac, top=True):
    o = np.argsort(-score if top else score); cs = np.cumsum(c[o]) / c.sum(); i = min(np.searchsorted(cs, frac), len(o) - 1)
    return score[o][i]
rows = []
for d in EVAL:
    tr = V[MAIN & (V.dia < d).values & (V.cierre < dstart[d]).values]; ev = V[(V.dia == d).values]
    if tr.dia.nunique() < 3: continue
    for m, fs in FE.items():
        mod = HistGradientBoostingRegressor(max_depth=3, max_iter=200, learning_rate=0.05, min_samples_leaf=300, l2_regularization=1.0, early_stopping=False, random_state=SEED)
        mod.fit(tr[fs], tr.y / tr.c, sample_weight=tr.c)
        s_tr = mod.predict(tr[fs]); X = ev[fs].copy()
        if True: X.loc[~ev.coin.isin(['ETH', 'SOL', 'XRP']), 'coin_i'] = np.nan
        s_ev = mod.predict(X)
        cut = {q: corte(s_tr, tr.c.values, q) for q in (0.10, 0.30, 0.50)}; cut_low = corte(s_tr, tr.c.values, 0.30, top=False)
        o = pd.DataFrame({'idx': ev.index, 'dia': d, 'modelo': m, 'score': s_ev, 'cut10': cut[0.10], 'cut30': cut[0.30], 'cut50': cut[0.50], 'cutlow30': cut_low})
        rows.append(o)
S = pd.concat(rows, ignore_index=True)
S.to_parquet(DL + 'wfcal_scores_off1.parquet')
V2 = V.copy()
def boot_ci(x, nb=NB):
    x = np.asarray(x, float); m = np.array([rng.choice(x, len(x)).mean() for _ in range(nb)]); return float(np.percentile(m, 5)), float(np.percentile(m, 95))
def exceso_dia(sub, flag):
    f = sub.c.values[flag].sum() / sub.c.values.sum(); return sub.y.values[flag].sum() - f * sub.y.values.sum(), f
def evaluar(m, nivel, dmin, dmax, coins, wk_only=False, dedup=False, inv=False):
    s = S[(S.modelo == m)].set_index('idx'); df = V2.loc[s.index].join(s[['score', 'cut10', 'cut30', 'cut50', 'cutlow30']])
    df = df[(df.dia >= dmin) & (df.dia <= dmax) & df.coin.isin(coins)]
    if wk_only: df = df[df.fin_sem == 0]
    if dedup: df = df.sort_values('t0_recv_ms').drop_duplicates(['mercado', 'lado'], keep='first')
    flag = (df.score <= df.cutlow30).values if inv else (df.score >= df['cut%d' % nivel]).values
    df = df.assign(flag=flag)
    return df
def resumen(df, strat='A'):
    out = {}; dd = []
    ex_d = []; f_d = []
    contrib = np.zeros(len(df)); pos = {}
    for d, g in df.groupby('dia'):
        e, f = exceso_dia(g, g.flag.values); ex_d.append((d, e)); f_d.append(f)
    days = [d for d, _ in ex_d]; ex = np.array([e for _, e in ex_d])
    fday = df.dia.map(dict(zip(days, f_d))).values
    contr = df.y.values * (df.flag.values - fday)
    cs = pd.Series(contr).groupby(df.cierre.values).sum().values
    tot = ex.sum(); sd = ex.std(ddof=1) if len(ex) > 1 else np.nan
    out['n_vidas'] = int(len(df)); out['n_ret'] = int(df.flag.sum()); out['f_eur'] = float(df.c[df.flag].sum() / df.c.sum()); out['dias'] = len(days)
    out['exceso_total'] = float(tot); out['exceso_por_dia'] = {d: float(e) for d, e in ex_d}
    out['IC90_dias'] = boot_ci(ex) if len(ex) > 1 else None
    out['t_dias'] = float(ex.mean() / (sd / np.sqrt(len(ex)))) if sd and sd > 0 else None
    out['sin_mejor'] = float(tot - ex.max()); out['sin_2mejores'] = float(tot - np.sort(ex)[-2:].sum()) if len(ex) > 2 else None
    out['frac_dias_pos'] = float((ex > 0).mean())
    out['n_cierres'] = int(len(cs)); mb = np.array([cs[rng.integers(0, len(cs), len(cs))].sum() for _ in range(2000)]); out['IC90_cierre'] = [float(np.percentile(mb, 5)), float(np.percentile(mb, 95))]
    fl = df.relleno_pes.values == 1; r = df.flag.values
    out['contrib_por_eur_ret'] = float(df.y[df.flag].sum() / df.c[df.flag].sum()); out['contrib_por_eur_all'] = float(df.y.sum() / df.c.sum())
    out['p_relleno_ret'] = float(fl[r].mean()); out['p_relleno_all'] = float(fl.mean())
    cf = df.c.values * fl
    out['EV_relleno_ret'] = float(df.y.values[r & fl].sum() / cf[r].sum()) if cf[r].sum() > 0 else None; out['EV_relleno_all'] = float(df.y.values[fl].sum() / cf.sum())
    out['n_rellenas_ret'] = int((r & fl).sum())
    return out, days, ex
def placebo(df, strata_cols, global_f):
    """p de permutar los flags dentro de estratos; estadistico = exceso total (por dia si global_f False)"""
    st = pd.factorize(pd.MultiIndex.from_frame(df[strata_cols]) if len(strata_cols) > 1 else df[strata_cols[0]])[0]
    flag = df.flag.values; y = df.y.values; c = df.c.values; dia = pd.factorize(df.dia)[0]; nd = dia.max() + 1
    idx_s = np.lexsort((np.arange(len(df)), st))
    def stat(fl):
        if global_f:
            f = c[fl].sum() / c.sum(); return y[fl].sum() - f * y.sum()
        sy = np.bincount(dia, y * fl, nd); sc = np.bincount(dia, c * fl, nd); ty = np.bincount(dia, y, nd); tc = np.bincount(dia, c, nd)
        return float((sy - sc / tc * ty).sum())
    obs = stat(flag); null = np.empty(NPERM)
    for i in range(NPERM):
        r = rng.random(len(df)); po = np.lexsort((r, st)); fp = np.empty(len(df), bool); fp[idx_s] = flag[po]; null[i] = stat(fp)
    return float(obs), float((null >= obs).mean())
RES = {}; CO3 = ['ETH', 'SOL', 'XRP']
def bloque(nombre, dmin, dmax):
    R = {}
    for m in FE:
        r = {}
        for nivel in (30, 10, 50):
            df = evaluar(m, nivel, dmin, dmax, CO3)
            if nivel == 30:
                res, days, ex = resumen(df); r['L30'] = res; r['_ex_dia'] = ex.tolist(); r['_dias'] = days
                po = placebo(df, ['dia', 'coin', 'hora'], False); r['placebo_dia_moneda_hora'] = {'obs': po[0], 'p': po[1]}
                pb = placebo(df, ['coin', 'hora'], True); r['placebo_moneda_hora'] = {'obs': pb[0], 'p': pb[1]}
                di = evaluar(m, nivel, dmin, dmax, CO3, inv=True); ri, _, exi = resumen(di); r['inversion'] = {'exceso_total': ri['exceso_total'], 'IC90_dias': ri['IC90_dias'], 'f_eur': ri['f_eur']}
                dw = evaluar(m, nivel, dmin, dmax, CO3, wk_only=True); rw, _, _ = resumen(dw); r['laborables'] = {k: rw[k] for k in ('dias', 'exceso_total', 'IC90_dias', 't_dias', 'frac_dias_pos')}
                dd = evaluar(m, nivel, dmin, dmax, CO3, dedup=True); rd, _, _ = resumen(dd); r['dedup_1_por_mercado_lado'] = {k: rd[k] for k in ('n_vidas', 'n_ret', 'exceso_total', 'IC90_dias', 'IC90_cierre', 't_dias', 'frac_dias_pos', 'EV_relleno_ret', 'EV_relleno_all')}
                for cn in ('BTC', 'DOGE', 'BNB'):
                    dc = evaluar(m, nivel, dmin, dmax, [cn]); rc, _, _ = resumen(dc); r['replica_' + cn] = {k: rc[k] for k in ('n_vidas', 'n_ret', 'exceso_total', 'IC90_dias', 'frac_dias_pos', 'EV_relleno_ret', 'EV_relleno_all')}
            else:
                res, _, _ = resumen(df); r['L%d' % nivel] = {k: res[k] for k in ('f_eur', 'exceso_total', 'IC90_dias', 't_dias', 'frac_dias_pos', 'contrib_por_eur_ret', 'contrib_por_eur_all', 'EV_relleno_ret', 'EV_relleno_all')}
        R[m] = r
    # P2 anade a P1: diferencia de exceso diario
    a = np.array(R['P2']['_ex_dia']); b = np.array(R['P1']['_ex_dia']); R['P2_menos_P1'] = {'dif_total': float((a - b).sum()), 'IC90_dias': boot_ci(a - b), 'dias_pos': float(((a - b) > 0).mean())}
    # gate
    for m in FE:
        r = R[m]; L = r['L30']
        g = {'exceso>0': L['exceso_total'] > 0, 'IC90_dias>0': (L['IC90_dias'] or [0])[0] > 0, 't>=2.13': (L['t_dias'] or 0) >= ZBONF,
             'sin_mejor>0': L['sin_mejor'] > 0, 'sin_2mejores>0': (L['sin_2mejores'] or -1) > 0, 'dias+>=60%': L['frac_dias_pos'] >= 0.60, 'IC90_cierre>0': L['IC90_cierre'][0] > 0,
             'placebo_p<0.05': r['placebo_dia_moneda_hora']['p'] < 0.05, 'inversion<0': r['inversion']['exceso_total'] < 0,
             'laborables>0_y_IC>0': r['laborables']['exceso_total'] > 0 and (r['laborables']['IC90_dias'] or [0])[0] > 0, 'placebo_moneda_hora<0.05': r['placebo_moneda_hora']['p'] < 0.05,
             'EV_relleno_ret>=all': (L['EV_relleno_ret'] or -9) >= L['EV_relleno_all']}
        r['gate'] = g; r['PASA'] = bool(all(g.values()))
    RES[nombre] = R
bloque('GATE_16_24', '2026-10-16', '2026-10-24')
bloque('LIMPIO_22_24', '2026-10-22', '2026-10-24')
bloque('EXPLORATORY_08_21', '2026-10-08', '2026-10-21')
bloque('TODO_08_24', '2026-10-08', '2026-10-24')
RES['cobertura_por_dia'] = cov
json.dump(RES, open(OUTD + 'wfcal_resultados_off1.json', 'w'), indent=1, default=float)
print('ok')
