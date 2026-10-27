#!/usr/bin/env python3
"""f5_desagrega.py -- Frente 3: F5 de A1 (log1p tamano del ask del token propio, tercil ALTO = marcado) desagregado por
moneda x franja UTC x dia. Reutiliza los r_DIA.pkl de a1_rasgos.py (prints REALES de la poblacion, q real de m5_registro; sin etiqueta generativa).
Mismo walk-forward del PREREG_A1: test 09..23-Oct, train = dias anteriores desde 06-Oct, terciles del train, EXCESO = f*Sigma pnl - Sigma pnl marcados
(placebo sustractivo de misma fraccion de EUR). Variantes: P pooled (reproduce A1), C umbrales por moneda, CB umbrales por moneda x franja 6h
(placebo DENTRO de la celda moneda x franja x dia => elimina composicion de moneda/hora/dia). Solo lectura."""
import glob, json, sys, numpy as np, pandas as pd
from scipy import stats
DL = '/root/polymarket-research-datalogs/mitigar_as_25oct/'
X = pd.concat([pd.read_pickle(f)[['dia','coin','r','q','coste','pnl','F5','F5_250','bid','fin']] for f in sorted(glob.glob(DL+'r_2026-10-*.pkl'))], ignore_index=True)
X = X[X.dia >= '2026-10-06'].reset_index(drop=True)
X['hora'] = ((X.r // 3600000) % 24).astype(int); X['band'] = X.hora // 6
dias = sorted(X.dia.unique()); test = [d for d in dias if d >= '2026-10-09']
def terc(v, c): return np.where(v <= c[0], 0, np.where(v <= c[1], 1, 2))
def ic(e):
    e = np.asarray(e, float); n = len(e); h = stats.t.ppf(.95, n-1)*e.std(ddof=1)/np.sqrt(n); return [float(e.mean()-h), float(e.mean()+h)]
def resumen(e):
    e = np.asarray(e, float); s = np.sort(e)
    return dict(exc=float(e.sum()), ic90_dias=ic(e), dias_pos=int((e > 0).sum()), n_dias=len(e), sin2=float(s[:-2].sum()), sin3=float(s[:-3].sum()))
def flags(df, keys, feat='F5', modo='min', train_end=None):
    """Devuelve (flag por fila de test, nº filas sin celda valida). Umbrales y tercil elegido con el train del propio dia de test."""
    F = np.zeros(len(df), bool); miss = 0
    for d in test:
        tr = X[(X.dia < d) & np.isfinite(X[feat])]; ti = np.where(df.dia.values == d)[0]; te = df.iloc[ti]
        grp_tr = tr.groupby(keys) if keys else [((), tr)]; 
        thr = {}
        for k, g in grp_tr:
            if len(g) < 500: continue
            c = np.quantile(g[feat].values, [1/3, 2/3])
            if c[0] == c[1]: c = [c[0], np.nextafter(c[0], np.inf)]
            tt = terc(g[feat].values, c); ev = [g.pnl.values[tt == j].sum()/max(g.coste.values[tt == j].sum(), 1e-9) for j in range(3)]
            thr[k if isinstance(k, tuple) else (k,)] = (c, 2 if modo == 'alto' else (int(np.argmin(ev)) if modo == 'min' else int(np.argmax(ev))) if modo != 'bajo' else 0)
        kk = [tuple(x) if keys else () for x in (te[keys].values if keys else [()]*len(te))]
        v = te[feat].values
        for i, k, vv in zip(ti, kk, v):
            if k in thr and np.isfinite(vv):
                c, sel = thr[k]; F[i] = (terc(np.array([vv]), c)[0] == sel)
            else: miss += 1
    return F, miss
T = X[X.dia.isin(test)].reset_index(drop=True)
def exceso(df, F, cell):
    """exceso por (dia, celda) = f_cell*pnl_cell - pnl_marcados_cell; devuelve DataFrame."""
    d = df.assign(F=F, pf=np.where(F, df.pnl, 0.0), cf=np.where(F, df.coste, 0.0))
    g = d.groupby(['dia'] + cell).agg(pnl=('pnl','sum'), coste=('coste','sum'), pf=('pf','sum'), cf=('cf','sum'), n=('pnl','size'), nf=('F','sum')).reset_index()
    g['exc'] = g.cf/g.coste*g.pnl - g.pf; return g
def ev(g): return dict(ev_marc=float(g.pf.sum()/max(g.cf.sum(),1e-9)), ev_ret=float((g.pnl.sum()-g.pf.sum())/max((g.coste.sum()-g.cf.sum()),1e-9)), ev_todo=float(g.pnl.sum()/g.coste.sum()), coste=float(g.coste.sum()), n=int(g.n.sum()))
out = dict(n_total=int(len(X)), n_test=int(len(T)), dias=dias, test=test, coste_test=float(T.coste.sum()), ev_test=float(T.pnl.sum()/T.coste.sum()))
res = {}
# 0) reproduccion A1 (pooled, seleccion min EV, placebo pooled por dia)
F0, m0 = flags(T, [], modo='min'); g0 = exceso(T, F0, []); res['P_pooled'] = dict(**resumen(g0.groupby('dia').exc.sum().values), miss=m0, **ev(g0))
Fi, _ = flags(T, [], modo='max'); res['P_pooled']['inversion_exc'] = float(exceso(T, Fi, []).exc.sum())
# 1) contribucion por moneda / franja / hora de la regla POOLED (placebo pooled del dia => composicion incluida)
d0 = T.assign(F=F0, pf=np.where(F0, T.pnl, 0.0), cf=np.where(F0, T.coste, 0.0))
fd = d0.groupby('dia').apply(lambda g: g.cf.sum()/g.coste.sum(), include_groups=False)
d0['exc_i'] = d0.dia.map(fd).values*d0.pnl - d0.pf
for nom, key in (('moneda', 'coin'), ('franja', 'band'), ('hora', 'hora')):
    pc = d0.groupby([key, 'dia']).exc_i.sum().unstack(0).fillna(0)
    res[f'pooled_por_{nom}'] = {str(c): dict(**resumen(pc[c].values), coste=float(d0[d0[key]==c].coste.sum())) for c in pc.columns}
# 2) estratificadas: umbrales por celda y placebo dentro de la celda
for nom, keys, cell in (('C_moneda', ['coin'], ['coin']), ('CB_moneda_x_franja', ['coin','band'], ['coin','band'])):
    F, ms = flags(T, keys, modo='min'); g = exceso(T, F, cell); Fi2, _ = flags(T, keys, modo='max'); gi = exceso(T, Fi2, cell)
    r = dict(**resumen(g.groupby('dia').exc.sum().values), miss=ms, **ev(g), inversion_exc=float(gi.exc.sum()))
    r['por_celda'] = {str(k): dict(**resumen(h.groupby('dia').exc.sum().reindex(test).fillna(0).values), ev_marc=ev(h)['ev_marc'], ev_ret=ev(h)['ev_ret'], coste=ev(h)['coste'], n=ev(h)['n']) for k, h in g.groupby(cell)}
    res[nom] = r
    if nom == 'CB_moneda_x_franja':
        FCB = F
        # sin ETH / solo ETH
        for lab, msk in (('sin_ETH', T.coin != 'ETH'), ('solo_ETH', T.coin == 'ETH')):
            gg = g[(g.coin != 'ETH')] if lab == 'sin_ETH' else g[g.coin == 'ETH']
            res[nom][lab] = dict(**resumen(gg.groupby('dia').exc.sum().reindex(test).fillna(0).values), **ev(gg))
        # nivel de relleno (al mejor bid vs por debajo) en la regla CB
        for lab, msk in (('al_mejor_bid', (T.q-T.bid).abs() < 0.005), ('por_debajo_bid_tipoB', T.q < T.bid-0.005)):
            sub = T[msk.values]; Fs = F[msk.values]; gg = exceso(sub, Fs, cell)
            res[nom][lab] = dict(**resumen(gg.groupby('dia').exc.sum().reindex(test).fillna(0).values), **ev(gg))
        # latencia 250 ms
        F250, _ = flags(T, keys, feat='F5_250', modo='min'); g250 = exceso(T, F250, cell); res[nom]['tau250'] = dict(**resumen(g250.groupby('dia').exc.sum().reindex(test).fillna(0).values), **ev(g250))
        # placebo permutacion: baraja F5 dentro de coin x band x dia; mismos umbrales/tercil de train
        thr = {}
        rng = np.random.default_rng(20261027); Tv = T.F5.values.copy(); gid = pd.factorize(T[['dia','coin','band']].astype(str).agg('|'.join, axis=1))[0]
        # recuperar umbral/tercil por fila a partir de F (flag real) -> reconstruir: para permutar, necesito c y sel por fila
        # se rehace con flags sobre una copia de T con F5 barajada (usa umbrales del train real, que usa X, no T)
        perm = []
        ref = exceso(T, FCB, cell).exc.sum()
        T0 = T.copy()
        for b in range(100):
            o = np.lexsort((rng.random(len(T0)), gid)); Tp = T0.copy(); s = np.argsort(gid, kind='stable'); 
            Tp['F5'] = T0.F5.values[s][np.argsort(np.argsort(o))] if False else T0.F5.values
            # barajado dentro de grupo: permuta posiciones dentro de cada grupo
            idx = np.arange(len(T0)); perm_idx = idx.copy()
            for gi_, ids in pd.Series(idx).groupby(gid): 
                p = ids.values.copy(); rng.shuffle(p); perm_idx[ids.values] = p
            Tp['F5'] = T0.F5.values[perm_idx]
            # flags usando umbrales del train real
            Fp = np.zeros(len(Tp), bool)
            for d in test:
                tr = X[(X.dia < d) & np.isfinite(X.F5)]; thrd = {}
                for k, gtr in tr.groupby(['coin','band']):
                    if len(gtr) < 500: continue
                    c = np.quantile(gtr.F5.values, [1/3, 2/3]); tt = terc(gtr.F5.values, c)
                    evs = [gtr.pnl.values[tt==j].sum()/max(gtr.coste.values[tt==j].sum(),1e-9) for j in range(3)]; thrd[k] = (c, int(np.argmin(evs)))
                ti = np.where(Tp.dia.values == d)[0]
                for k, (c, sel) in thrd.items():
                    mk = ti[(Tp.coin.values[ti]==k[0]) & (Tp.band.values[ti]==k[1])]
                    v = Tp.F5.values[mk]; Fp[mk] = np.isfinite(v) & (terc(np.nan_to_num(v, nan=-9e18), c) == sel)
            perm.append(exceso(Tp, Fp, cell).exc.sum())
            if b % 20 == 0: print('perm', b, flush=True)
        perm = np.array(perm); res[nom]['placebo_perm'] = dict(real=float(ref), perm_media=float(perm.mean()), perm_sd=float(perm.std()), perm_p95=float(np.quantile(perm,.95)), p_unilateral=float((1+(perm>=ref).sum())/(1+len(perm))), n_perm=len(perm))
out['res'] = res
json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else 'f5_resultados.json', 'w'), indent=1, default=float)
def p(r): return f"exc {r['exc']:.0f} IC90d ({r['ic90_dias'][0]:.0f},{r['ic90_dias'][1]:.0f}) d+ {r['dias_pos']}/{r['n_dias']} sin2 {r['sin2']:.0f} sin3 {r['sin3']:.0f}"
for k, r in res.items():
    if 'exc' in r: print(k, p(r), {a: round(b, 4) for a, b in r.items() if a in ('ev_marc','ev_ret','ev_todo','inversion_exc','miss','coste','n')})
    else:
        for c, v in r.items(): print(k, c, p(v), 'coste', round(v['coste']))
    for sub in ('sin_ETH','solo_ETH','al_mejor_bid','por_debajo_bid_tipoB','tau250'):
        if isinstance(r, dict) and sub in r: print('  ', k, sub, p(r[sub]), {a: round(b, 4) for a, b in r[sub].items() if a in ('ev_marc','ev_ret','ev_todo')})
    if isinstance(r, dict) and 'por_celda' in r:
        for c, v in r['por_celda'].items(): print('   celda', c, p(v), 'ev_marc', round(v['ev_marc'],3), 'ev_ret', round(v['ev_ret'],3), 'coste', round(v['coste']), 'n', v['n'])
    if isinstance(r, dict) and 'placebo_perm' in r: print('  placebo', r['placebo_perm'])
