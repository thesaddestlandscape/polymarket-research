#!/usr/bin/env python3
"""Ronda 3 V4 «comprar lo bueno»: resume las salidas de sim_dia3.py / rival_re.py (BTC, 06-18 Oct) con desenlace oficial.
Solo lectura. EV = Σpnl/Σcoste (ponderado por €); IC90 bootstrap por días y por cierre; sin 2 mejores días.
Uso: python3 -I analisis_r3.py [dir_salidas]"""
import sys, glob, os, json, math
import numpy as np, pandas as pd
O = sys.argv[1] if len(sys.argv) > 1 else '/mnt/HC_Volume_106538179/datalogs_analisis_caches/v4_comprar_lo_bueno/r3_out/'
rng = np.random.default_rng(7)
def fee(p): return 0.07 * p * (1 - p)
def boot(df, key, pnl='pnl', cost='coste', n=2000):
    g = df.groupby(key)[[pnl, cost]].sum(); a = g.values
    if len(a) < 2: return (np.nan, np.nan)
    idx = rng.integers(0, len(a), (n, len(a)))
    num, den = a[idx, 0].sum(1), a[idx, 1].sum(1)
    ok = den > 0
    r = num[ok] / den[ok]
    return (round(float(np.percentile(r, 5)), 3), round(float(np.percentile(r, 95)), 3))
def resumen(df, nombre, pnl='pnl', cost='coste'):
    if not len(df): print(f'{nombre}: n=0'); return
    ev = df[pnl].sum() / df[cost].sum() if df[cost].sum() > 0 else float('nan')
    byd = df.groupby('dia')[[pnl, cost]].sum(); byd['ev'] = byd[pnl] / byd[cost]
    top = byd[pnl].sort_values(ascending=False).index[:2]
    r2 = df[~df.dia.isin(top)]
    ev2 = r2[pnl].sum() / r2[cost].sum() if len(r2) and r2[cost].sum() > 0 else float('nan')
    print(f'{nombre}: n={len(df)} cierres={df.cierre.nunique()} dias={df.dia.nunique()} PnL={df[pnl].sum():+.2f} coste={df[cost].sum():.2f} EV_pond={ev:+.3f} '
          f'IC90 dias={boot(df, "dia", pnl, cost)} IC90 cierre={boot(df, "cierre", pnl, cost)} sin2mejoresDias={ev2:+.3f} dias+={int((byd[pnl] > 0).sum())}/{len(byd)}')
def mc_nulo(p, w, gana, n=5000):
    """P(sum w*(gana-p) >= observado) si P(gana)=precio p; w = acciones."""
    obs = float((w * (gana - p)).sum())
    sim = np.array([(w * ((rng.random(len(p)) < p).astype(float) - p)).sum() for _ in range(n)])
    return obs, float((sim >= obs).mean())

# ============ A. réplica V4 (BTC) con el simulador por RECEPCIÓN
V = pd.concat([pd.read_csv(f) for f in sorted(glob.glob(O + 'v4_*.csv')) if os.path.getsize(f) > 0], ignore_index=True)
V['cierre'] = V.cierre.astype(int)
print('===== A. V4 réplica BTC (sim por recepción, nivel 1): dias', V.dia.nunique(), 'señales', len(V))
for L in (150, 215, 250):
    d = V[V[f'acc{L}'] > 0].copy()
    d['coste'] = d[f'acc{L}'] * (d[f'p{L}'] + fee(d[f'p{L}'])); d['pnl'] = d[f'acc{L}'] * (d.gana.astype(float) - d[f'p{L}'] - fee(d[f'p{L}']))
    resumen(d, f'L{L} ejecutables ({len(d)}/{len(V)})')
    print(f'    acierto ejecutables {d.gana.mean():.3f} precio medio {d[f"p{L}"].mean():.3f} | NO ejecutables a L{L}: {len(V)-len(d)} acierto {V[V[f"acc{L}"]==0].gana.astype(float).mean():.3f}')

# ============ B. maker H23
M = pd.concat([pd.read_csv(f) for f in sorted(glob.glob(O + 'mk_*.csv')) if os.path.getsize(f) > 0], ignore_index=True)
M['gana'] = M.gana.astype(float)
M['pnl'] = M.lleno * M.gana - M.coste + M.rebate
print('\n===== B. Maker H23 (BTC, 1 por cierre y variante; rebate 20 % incluido; alta 68 ms)')
print('cierres con lado y libro:', M.cierre.nunique(), 'días', M.dia.nunique())
for (var, mq_, clk, lc), g in M[M.clk == 'rx'].groupby(['var', 'mq', 'clk', 'lc']):
    q = g[g.n_cotiz > 0]; f = g[g.lleno > 0]
    full = f[f.lleno >= 4.99]
    resumen(f, f'{var:8s} mq={mq_} clk={clk} cancel={lc:3d} | cotizadas {len(q)}/{len(g)} rellenadas {len(f)} ({100*len(f)/max(len(q),1):.0f} %) ; acierto rell. {f.gana.mean() if len(f) else float("nan"):.3f} vs precio {(f.coste.sum()/f.lleno.sum()) if len(f) else float("nan"):.3f}')
# tabla clave: primario = join mq -0.05, clk rx, lc 60
P = M[(M['var'] == 'join') & (M.mq == -0.05) & (M.clk == 'rx') & (M.lc == 60) & (M.lleno > 0)]
print('\nPrimario (preregistrado: join, margen>=-0,05, relleno por recepción, cancelación 60 ms):')
resumen(P, 'primario')
if len(P):
    o, pv = mc_nulo((P.coste / P.lleno).values, P.lleno.values, P.gana.values); print('   desviación sobre precio (acc·(gana−p)) = %+.2f ; P(>= | acierto=precio) = %.3f' % (o, pv))
    # relleno antes/después del evento V4 (solo cierres con evento V4)
    pe = P.dropna(subset=['v4_t0']); 
    if len(pe): print('   con evento V4 en el cierre:', len(pe), '| rellena ANTES del t0 V4:', int((pe.t_relleno < pe.v4_t0).sum()), 'DESPUÉS:', int((pe.t_relleno >= pe.v4_t0).sum()))
    print('   T restante del relleno P10/50/90:', np.percentile(P.T_rel.dropna(), [10, 50, 90]).round(0))
# emparejado maker vs tomador V4 L215 en los cierres con evento
Vk = V.set_index('cierre')
rows = []
for c, g in M[(M['var'] == 'join') & (M.mq == -0.05) & (M.clk == 'rx') & (M.lc == 60)].groupby('cierre'):
    if c in Vk.index:
        v = Vk.loc[c]; g = g.iloc[0]
        rows.append(dict(cierre=c, dia=g.dia, tom=(v.acc215 > 0), tom_pnl=v.acc215 * (float(v.gana) - v.p215 - fee(v.p215)) if v.acc215 > 0 else 0.0, mk_fill=g.lleno > 0, mk_pnl=g.pnl, gana=float(v.gana)))
if rows:
    R = pd.DataFrame(rows)
    print('\nEmparejado en los cierres con evento V4 (n=%d): tomador L215 ejecuta %d (PnL %+.2f) ; maker H23 primario rellena %d (PnL %+.2f)' % (len(R), R.tom.sum(), R.tom_pnl.sum(), R.mk_fill.sum(), R.mk_pnl.sum()))
    print('   maker rellena y GANA %d/%d ; tomador no ejecuta y GANA %d/%d (las "buenas" perdidas); maker rellena de ellas: %d' % (
        R[R.mk_fill].gana.sum(), R.mk_fill.sum(), R[~R.tom].gana.sum(), (~R.tom).sum(), R[(~R.tom) & R.mk_fill].shape[0]))
    print('   de las no ejecutables a 215 ms que ganan, el maker rellena %d/%d' % (R[(~R.tom) & (R.gana == 1) & R.mk_fill].shape[0], R[(~R.tom) & (R.gana == 1)].shape[0]))

# ============ C. precursores (feat) con partición cronológica 06-12 / 13-18
fs = sorted(glob.glob(O + 'feat_*.csv.gz'))
if fs:
    F = pd.concat([pd.read_csv(f) for f in fs], ignore_index=True)
    F['gana'] = F.gana.astype(float); F['cierre'] = F.cierre.astype(int)
    print('\n===== C. Precursores (instantes con margen>=-0,10, sin libro cruzado): filas', len(F), 'cierres', F.cierre.nunique())
    F['llena'] = F.acc_e215 > 0
    F['p'] = F.ask_e215; F['pnl'] = F.acc_e215 * (F.gana - F.p - fee(F.p)); F['coste'] = F.acc_e215 * (F.p + fee(F.p))
    F['dia'] = F.dia.astype(str)
    F['fase'] = np.where(F.dia <= '2026-10-12', 'DESC', 'TEST')
    # 1 instante por cierre y regla: el PRIMERO que la cumple
    def regla(nombre, mask):
        d = F[mask].sort_values('t').groupby('cierre', as_index=False).first()
        for fase in ('DESC', 'TEST', 'TODO'):
            x = d if fase == 'TODO' else d[d.fase == fase]
            e = x[x.llena]
            resumen(e, f'{nombre} [{fase}] disparos {len(x)} ejecutables {len(e)} ({100*len(e)/max(len(x),1):.0f} %); acierto {e.gana.mean() if len(e) else float("nan"):.3f} precio {e.p.mean() if len(e) else float("nan"):.3f}')
    regla('m>=0,05 (V4, 1er instante)', F.sen == 1)
    for th in (-0.03, -0.01, 0.0, 0.02):
        regla(f'm>={th}', F.m >= th)
        regla(f'm>={th} & Binance r250>=+0,5bp', (F.m >= th) & (F.r250 >= 0.5))
        regla(f'm>={th} & Binance r1000>=+1bp', (F.m >= th) & (F.r1000 >= 1.0))
        regla(f'm>={th} & Δbid15 1 s>=+1c', (F.m >= th) & (F.db15_1s >= 0.01))
    # AUC cronológico de "condición V4 en los próximos 500 ms" (ev500) para instantes con m en [-0,10,0,05)
    pre = F[(F.sen == 0) & (F.m < 0.05)].copy()
    cols = ['m', 'r250', 'r500', 'r1000', 'db15_1s', 'da5_1s', 'asz5', 'bsz15']
    pre = pre.dropna(subset=cols)
    def auc(y, s):
        r = pd.Series(s).rank().values; n1 = y.sum(); n0 = len(y) - n1
        return (r[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0) if n1 and n0 else np.nan
    tr, te = pre[pre.fase == 'DESC'], pre[pre.fase == 'TEST']
    print('\nev500 (¿se cumple la condición V4 en los próximos 500 ms?) tasa base DESC %.4f TEST %.4f (filas %d / %d)' % (tr.ev500.mean(), te.ev500.mean(), len(tr), len(te)))
    for c in cols:
        a_tr = auc(tr.ev500.values.astype(int), tr[c].values); a_te = auc(te.ev500.values.astype(int), te[c].values)
        print(f'   AUC {c:8s} DESC {a_tr:.3f} TEST {a_te:.3f}')
    try:
        raise ImportError('GBM omitido (limite de hilos con ulimit)')
        from sklearn.ensemble import HistGradientBoostingClassifier as H
        m_ = H(max_iter=80, learning_rate=0.1, max_depth=3, random_state=0).fit(tr[cols], tr.ev500.astype(int))
        print('   GBM(8 rasgos) AUC TEST %.3f' % auc(te.ev500.values.astype(int), m_.predict_proba(te[cols])[:, 1]))
        pt = te.assign(s=m_.predict_proba(te[cols])[:, 1])
        for q in (0.5, 0.9, 0.99):
            th = pt.s.quantile(q); x = pt[pt.s >= th]
            print(f'      top {100-100*q:.0f} %: tasa ev500 {x.ev500.mean():.4f} (base {te.ev500.mean():.4f}) filas {len(x)} cierres {x.cierre.nunique()}')
    except Exception as e:
        print('   (sin sklearn:', e, ')')

# ============ D. rival
rs = sorted(glob.glob(O + 'rival_*.csv'))
if rs:
    Rv = pd.concat([pd.read_csv(f) for f in rs], ignore_index=True)
    Rv = Rv[Rv.match == 1].copy()
    real = Rv[Rv.placebo == 0]; pl = Rv[Rv.placebo == 1]
    print('\n===== D. Rival (órdenes tomadoras casadas con el WS):', len(real), 'reales,', len(pl), 'placebo; por wallet', real.w.value_counts().to_dict())
    for c in ['E250', 'E1000', 'R250', 'R1000', 'E_fwd150', 's5_da1s', 's15_db1s', 's5_ask', 's15_bid']:
        if c in Rv:
            a = real[c].dropna(); b = pl[c].dropna()
            print(f'   {c:9s} real P25/50/75 {np.percentile(a,[25,50,75]).round(3) if len(a) else None} | placebo {np.percentile(b,[25,50,75]).round(3) if len(b) else None}')
    for df in (real, pl):
        df['marg'] = df.s15_bid - df.s5_ask - fee(df.s5_ask)
    print('   margen V4 en el envío acotado (ex-150): real  P(>=0,05)=%.3f P(>=0)=%.3f P(>=-0,05)=%.3f | placebo %.3f %.3f %.3f' % (
        (real.marg >= .05).mean(), (real.marg >= 0).mean(), (real.marg >= -.05).mean(), (pl.marg >= .05).mean(), (pl.marg >= 0).mean(), (pl.marg >= -.05).mean()))
    real['pnl'] = real.acc * (real.gana.astype(float) - real.p - fee(real.p)); real['coste'] = real.acc * (real.p + fee(real.p))
    for w, g in real.groupby('w'):
        g = g.dropna(subset=['marg'])
        for lo, hi in ((-9, -0.05), (-0.05, 0), (0, 0.05), (0.05, 9)):
            x = g[(g.marg >= lo) & (g.marg < hi)]
            if len(x): print(f'   {w} margen [{lo},{hi}) fills {len(x)} coste {x.coste.sum():.0f} $ EV_pond {x.pnl.sum()/x.coste.sum():+.3f}')
