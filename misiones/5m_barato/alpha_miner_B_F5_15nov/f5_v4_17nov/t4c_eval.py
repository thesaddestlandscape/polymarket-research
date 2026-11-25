#!/usr/bin/env python3
"""t4c_eval.py --grid | --hyst W,C,rho,nmin | --final W,C,rho,nmin,H  (17-Nov, feedback de Javi a INFORME_1b; reutiliza t4b_eval/suelo_causal sin tocarlos). Misma particion: dev <= 2026-10-25, hold-out > 25-Oct. 0 ordenes, nada en data/.
--grid : rejilla ampliada W {2,3,5,8,12,20,30} x C {26..34} x rho {0,02..0,1} x nmin {1..15}, H=1 (H=1 = ya sin permanencia; H<1 no existe), metricas en dev Y hold-out; meseta por MINIMAX en vecindad (+-1 paso en los 4 ejes).
--hyst  : barrido de permanencia X=H de entrada (salida inmediata) en los parametros dados: episodios/dia (cancelaciones), lo-en-hi, nolo-en-lo, retraso.
--final : tablas de las 4 verdades/efectos con el detector dado: (2) verdad independiente: (a) clase T2 de FUTURO (cls_fut, p5 de 5 min por delante: otra estadistica) y (b) verdad por DESENLACE (EV de la regla F5 y gradiente bajo-alto por estado);
         (3) simulacion operativa con latencias de paquete_l 13-Nov (B2,B3,B5, n=313): alta ex-envio p50 ~35 ms (B2 p90 147), cancelacion ex-envio p50 32-34 ms (B2 p90 111): estado desplazado L ms; cancelaciones/dia = transiciones lo->nolo; (4a) 215 rellenos reales de B."""
import os, sys, json, itertools, numpy as np, pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); import suelo_causal as SC; import t4b_eval as T
from scipy import stats
C0, C1 = 3.526360511779785, 4.717426776885986
def st_fn(p): return lambda D: SC.estado_lo(SC.lo_crudo(D.S, p), p)
def met(dias, p):
    A = T.agrega([T.metricas_dia(D, SC.estado_lo(SC.lo_crudo(D.S, p), p)) for D in dias]); return A
def fila(p, A): return dict(W=p.W, C=p.C, rho=p.rho, nmin=p.nmin, H=p.H, score=A['lo_en_hi'] + A['nolo_en_lo'], lo_en_hi=A['lo_en_hi'], nolo_en_lo=A['nolo_en_lo'], ep_lo_en_hi=A['ep_lo_en_hi'], ep_nolo_en_lo=A['ep_nolo_en_lo'], lohi_miss=A['lohi_miss'], lohi_n=A['lohi_n'], lohi_p50=T.pq(A['lohi'], 50), lohi_p90=T.pq(A['lohi'], 90), hilo_p50=T.pq(A['hilo'], 50), hilo_p90=T.pq(A['hilo'], 90), dias=A['dias'])
AX = dict(W=(2, 3, 5, 8, 12, 20, 30), C=(26, 28, 30, 32, 34), rho=(0.02, 0.035, 0.05, 0.07, 0.1), nmin=(1, 2, 3, 5, 7, 10, 15))
def grid(dev, ho):
    R = {}
    for W, C, rho, nmin in itertools.product(*AX.values()):
        p = SC.ParamsDetector(W, C, rho, nmin, 1); R[(W, C, rho, nmin)] = (fila(p, met(dev, p)), fila(p, met(ho, p)))
    return R
def vecinos(k):
    ks = list(AX); out = []
    for d in itertools.product((-1, 0, 1), repeat=4):
        kk = []
        for (name, v), x in zip(AX.items(), d):
            i = v.index(k[ks.index(name)]) + x
            if not (0 <= i < len(v)): break
            kk.append(v[i])
        else: out.append(tuple(kk))
    return out
def meseta(R):
    rob = {k: max(R[v][0]['score'] for v in vecinos(k)) for k in R}; best = min(rob, key=lambda k: (rob[k], R[k][0]['score'])); sb = R[best][0]['score']
    pl = [k for k in R if rob[k] <= 1.5 * rob[best]]; return best, rob, pl
def hyst(dev, ho, W, C, rho, nmin):
    out = []
    for H in (1, 2, 3, 5, 10, 20, 30, 60):
        p = SC.ParamsDetector(W, C, rho, nmin, H); out.append((fila(p, met(dev, p)), fila(p, met(ho, p)), ))
        for nm, grp in (('dev', dev), ('ho', ho)):
            st = [SC.estado_lo(SC.lo_crudo(D.S, p), p) for D in grp]; out[-1][0 if nm == 'dev' else 1]['cancel_dia'] = float(np.mean([(np.diff(s.astype(int)) == -1).sum() for s in st])); out[-1][0 if nm == 'dev' else 1]['altas_dia'] = float(np.mean([(np.diff(s.astype(int)) == 1).sum() for s in st]))
    return out
# ---------------- verdades independientes
def truth_t2(D):
    z = np.load(HERE + f'/cache/clases_{D.d}.npz', allow_pickle=True)['cls_fut'].astype(str); v = np.full(8640, -1, np.int8); v[z == 'lo'] = 1; v[z == 'hi'] = 0; return v
def conc(D, st, v):
    """confusion por segundo estado x verdad (lo/hi) y retraso vs transiciones de esa verdad (tramos >=3 bins)."""
    vs = np.repeat(v, 10); return dict(lo_lo=int((st & (vs == 1)).sum()), lo_hi=int((st & (vs == 0)).sum()), nolo_lo=int((~st & (vs == 1)).sum()), nolo_hi=int((~st & (vs == 0)).sum()), n_unk=int((vs < 0).sum()))
def retraso_vs(D, st, v):
    v2 = v.copy()
    for val in (0, 1):
        m = v2 == val; d = np.diff(np.concatenate([[0], m.astype(int), [0]])); a, b = np.where(d == 1)[0], np.where(d == -1)[0]
        for x, y in zip(a, b):
            if y - x < 3: v2[x:y] = -1
    class _D: pass
    X = _D(); X.tr = T.transiciones(v2); X.vs = np.repeat(v2, 10); return T.metricas_dia(X, st)
# ---------------- poblacion F5 (tipo B) con tercil
def pob_B(d):
    ps = []
    for pk in (T.EXPC + f'{d}_pob_add3.pkl.gz', T.C4 + f'btc_pob_{d}.pkl.gz'):
        if os.path.exists(pk):
            try: ps.append(pd.read_pickle(pk, compression='gzip')[['r_ex', 'q', 'F5_p60', 'bid_p60', 'cat_p60', 'coste', 'pnl']])
            except Exception: pass
    if not ps: return None
    X = pd.concat(ps, ignore_index=True); m = (X.cat_p60 == 0) & np.isfinite(X.F5_p60) & np.isfinite(X.bid_p60) & ((X.bid_p60 - X.q) >= 0.0099 - 1e-12); X = X[m].copy()
    X['ter'] = np.where(X.F5_p60 <= C0, 'bajo', np.where(X.F5_p60 > C1, 'alto', 'medio')); return X
def sec_de(ms, day0, L): return np.clip((ms - L - day0) // 1000, 0, 86399).astype(np.int64)
def ev(p, c): return float(p / c) if c > 0 else float('nan')
def desenlace(dias, stfn, L=0, off=0):
    """por dia: EV pond. de la regla (bajo) y gradiente bajo-alto, en estado lo vs nolo (estado desplazado L ms; tiempo del print = r_ex-off). -> lista de dict por dia."""
    rows = []
    for D in dias:
        X = pob_B(D.d)
        if X is None or len(X) == 0: continue
        day0 = int(pd.Timestamp(D.d + 'T00:00:00Z').value // 10**6); ms = X.r_ex.values.astype(np.int64) - off; ok = (ms - day0 >= 0) & (ms - day0 < 86400000); s = sec_de(ms, day0, L); st = stfn(D)[s] & ok
        r = dict(dia=D.d)
        for nm, m in (('lo', st), ('nolo', ~st & ok)):
            for t in ('bajo', 'alto'):
                mm = m & (X.ter.values == t); r[f'c_{nm}_{t}'] = float(X.coste.values[mm].sum()); r[f'p_{nm}_{t}'] = float(X.pnl.values[mm].sum()); r[f'n_{nm}_{t}'] = int(mm.sum())
        rows.append(r)
    return rows
def ic_dias(x):
    x = np.asarray(x, float); x = x[np.isfinite(x)]; n = len(x)
    if n < 3: return None
    se = x.std(ddof=1) / np.sqrt(n); return round(float(x.mean() - stats.t.ppf(.95, n - 1) * se), 3), round(float(x.mean() + stats.t.ppf(.95, n - 1) * se), 3), round(float(x.mean()), 3), n
def res_desenlace(nm, rows):
    S = lambda k: sum(r[k] for r in rows)
    dEV = [ev(r['p_lo_bajo'], r['c_lo_bajo']) - ev(r['p_nolo_bajo'], r['c_nolo_bajo']) for r in rows]
    grad = [ev(r['p_lo_bajo'], r['c_lo_bajo']) - ev(r['p_lo_alto'], r['c_lo_alto']) for r in rows]; gradn = [ev(r['p_nolo_bajo'], r['c_nolo_bajo']) - ev(r['p_nolo_alto'], r['c_nolo_alto']) for r in rows]
    return (f"{nm:<22} regla(bajo): EV lo {ev(S('p_lo_bajo'), S('c_lo_bajo')):+.3f} (n={S('n_lo_bajo')}, {S('c_lo_bajo'):.0f} EUR) | nolo {ev(S('p_nolo_bajo'), S('c_nolo_bajo')):+.3f} (n={S('n_nolo_bajo')}, {S('c_nolo_bajo'):.0f} EUR) | dias {len(rows)} | EV lo-nolo por dia IC90 {ic_dias(dEV)} | gradiente bajo-alto lo {ic_dias(grad)} nolo {ic_dias(gradn)}")
if __name__ == '__main__':
    arg = lambda k, d=None: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
    SUF = ''
    if '--ax2' in sys.argv: AX.update(W=(6, 8, 10, 12, 15, 20, 30), C=(30, 34, 40, 50), rho=(0.07, 0.1, 0.15, 0.2, 0.3), nmin=(1, 3, 5, 10)); SUF = '2'
    DAYS = [T.Dia(d) for d in T.DIAS]; dev = [D for D in DAYS if D.d <= T.CORTE]; ho = [D for D in DAYS if D.d > T.CORTE]
    if '--grid' in sys.argv:
        R = grid(dev, ho); best, rob, pl = meseta(R); json.dump([dict(k=list(k), dev=v[0], ho=v[1], robust_dev=rob[k]) for k, v in R.items()], open(HERE + f'/T4c_grid{SUF}.json', 'w'))
        from scipy.stats import spearmanr
        sd = [R[k][0]['score'] for k in R]; sh = [R[k][1]['score'] for k in R]; L = [f'# T4c rejilla ampliada ({len(R)} configs H=1) dev {len(dev)} dias / hold-out {len(ho)}; Spearman score dev vs hold-out {spearmanr(sd, sh)[0]:.3f}']
        ks = sorted(R, key=lambda k: R[k][0]['score']); L.append('top 10 por score dev (lo_en_hi+nolo_en_lo s): ' + '; '.join(f"{k} dev {R[k][0]['score']} ho {R[k][1]['score']}" for k in ks[:10]))
        L.append(f"minimax (vecindad +-1): mejor {best} robust {rob[best]} (score dev {R[best][0]['score']}, ho {R[best][1]['score']}); meseta = {len(pl)} configs con robust <= 1,5x")
        for ax, i in (('W', 0), ('C', 1), ('rho', 2), ('nmin', 3)): L.append(f"  meseta {ax}: {sorted(set(k[i] for k in pl))}")
        for nm, i in (('dev', 0), ('hold-out', 1)): L.append(f"  meseta en {nm}: score min/med/max {min(R[k][i]['score'] for k in pl)}/{int(np.median([R[k][i]['score'] for k in pl]))}/{max(R[k][i]['score'] for k in pl)}; lo_en_hi {min(R[k][i]['lo_en_hi'] for k in pl)}/{int(np.median([R[k][i]['lo_en_hi'] for k in pl]))}/{max(R[k][i]['lo_en_hi'] for k in pl)}; nolo_en_lo {min(R[k][i]['nolo_en_lo'] for k in pl)}/{int(np.median([R[k][i]['nolo_en_lo'] for k in pl]))}/{max(R[k][i]['nolo_en_lo'] for k in pl)}; lohi p90 {min(R[k][i]['lohi_p90'] for k in pl)}/{np.median([R[k][i]['lohi_p90'] for k in pl]):.0f}/{max(R[k][i]['lohi_p90'] for k in pl):.0f}; lohi_miss max {max(R[k][i]['lohi_miss'] for k in pl)}")
        old = (5, 30, 0.05, 10); L.append(f"punto 1b {old}: dev {R[old][0]['score']} ho {R[old][1]['score']}, robust {rob[old]}; en meseta: {old in pl}") if old in R else None; open(HERE + f'/T4c_grid{SUF}.txt', 'w').write('\n'.join(L) + '\n'); print('\n'.join(L)); sys.exit(0)
    if '--hyst' in sys.argv:
        W, C, rho, nmin = [float(x) for x in arg('--hyst').split(',')]; o = hyst(dev, ho, int(W), int(C), rho, int(nmin)); L = [f'# T4c permanencia de entrada X=H s (salida inmediata) W{int(W)} C{int(C)} rho{rho} nmin{int(nmin)}']
        for a, b in o: L.append(f"X={a['H']:>2}  DEV score {a['score']} lo_en_hi {a['lo_en_hi']} nolo_en_lo {a['nolo_en_lo']} ep_nolo_en_lo/dia {a['ep_nolo_en_lo'] / a['dias']:.1f} cancel/dia {a['cancel_dia']:.1f} lohi p50/p90 {a['lohi_p50']}/{a['lohi_p90']} miss {a['lohi_miss']} hilo p50/p90 {a['hilo_p50']}/{a['hilo_p90']} | HO score {b['score']} lo_en_hi {b['lo_en_hi']} nolo_en_lo {b['nolo_en_lo']} ep_nolo_en_lo/dia {b['ep_nolo_en_lo'] / b['dias']:.1f} cancel/dia {b['cancel_dia']:.1f} lohi p90 {b['lohi_p90']} hilo p50/p90 {b['hilo_p50']}/{b['hilo_p90']}")
        open(HERE + '/T4c_hyst.txt', 'w').write('\n'.join(L) + '\n'); print('\n'.join(L)); sys.exit(0)
    ps = [float(x) for x in arg('--final').split(',')]; p = SC.ParamsDetector(int(ps[0]), int(ps[1]), ps[2], int(ps[3]), int(ps[4])); L = [f'# T4c final detector {p!r}; dev {len(dev)} / hold-out {len(ho)} dias']
    stf = st_fn(p); stp = lambda D: D.st_p5; stv = lambda D: (D.vs == 1)
    L.append('## 2a. Verdad T2 de futuro (cls_fut: p5 de las filas en [t, t+5 min), otra estadistica que f(d<30 ms)); confusion en segundos y retraso vs sus transiciones')
    for nm, grp in (('DEV', dev), ('HOLD-OUT', ho), ('TODOS', DAYS)):
        for dn, fn in (('p5 10 min', stp), (repr(p), stf)):
            C = {}; rs = []
            for D in grp:
                v = truth_t2(D); c = conc(D, fn(D), v); C = {k: C.get(k, 0) + x for k, x in c.items()}; rs.append(retraso_vs(D, fn(D), v))
            A = T.agrega(rs); acc = (C['lo_lo'] + C['nolo_hi']) / max(C['lo_lo'] + C['nolo_hi'] + C['lo_hi'] + C['nolo_lo'], 1)
            L.append(f"{nm:<9}{dn:<24} concordancia {100 * acc:.2f} % | lo_lo {C['lo_lo']} lo_hi {C['lo_hi']} nolo_lo {C['nolo_lo']} nolo_hi {C['nolo_hi']} (s sin verdad {C['n_unk']}) | transiciones lohi {A['lohi_n']} det {A['lohi_n'] - A['lohi_miss']} p50/p90 {T.pq(A['lohi'], 50)}/{T.pq(A['lohi'], 90)} s | hilo {A['hilo_n']} det {A['hilo_n'] - A['hilo_miss']} p50/p90 {T.pq(A['hilo'], 50)}/{T.pq(A['hilo'], 90)} s")
    L.append('## 2b. Verdad por DESENLACE: EV realizado de la regla F5 (tercil bajo, tipo B, p60) y gradiente bajo-alto segun estado (poblacion ajena censurada; t = r_ex-83 ms)')
    for nm, grp in (('DEV', dev), ('HOLD-OUT', ho), ('TODOS', DAYS)):
        for dn, fn in (('verdad d<30 ms', stv), ('p5 10 min', stp), (repr(p), stf)): L.append(f'{nm:<9}' + res_desenlace(dn, desenlace(grp, fn, 0, 83)))
    L.append('## 3. Simulacion operativa con latencias reales (paquete_l B2/B3/B5, 13-Nov, n=313): estado desplazado L ms (alta/cancelacion ex-envio p50 ~35 ms; p90 hasta 111-147 ms en B2); tiempo del relleno = r_ex')
    for Lms in (35, 110, 150):
        for dn, fn in (('p5 10 min', stp), (repr(p), stf)):
            rows = []
            for D in DAYS:
                X = pob_B(D.d)
                if X is None or len(X) == 0: continue
                day0 = int(pd.Timestamp(D.d + 'T00:00:00Z').value // 10**6); s = sec_de(X.r_ex.values.astype(np.int64), day0, Lms); live = fn(D)[s]; tru = D.vs[s]; rl = (X.ter.values == 'bajo'); c = X.coste.values; pn = X.pnl.values
                m = live & (tru == 0) & rl; rows.append((int(m.sum()), float(c[m].sum()), float(pn[m].sum()), int((live & rl).sum()), float(c[live & rl].sum()), float(pn[live & rl].sum())))
            a = np.array(rows); L.append(f"L={Lms:>3} ms {dn:<24} prints regla vivos con verdad hi: n={int(a[:, 0].sum())}, {a[:, 1].sum():.0f} EUR, pnl {a[:, 2].sum():+.0f} (de {int(a[:, 3].sum())} prints vivos, {a[:, 4].sum():.0f} EUR, pnl {a[:, 5].sum():+.0f}; {len(rows)} dias)")
    can = [(np.diff(fn_(D).astype(int)) == -1).sum() for D in DAYS for fn_ in (stf,)]; alt = [(np.diff(stf(D).astype(int)) == 1).sum() for D in DAYS]; can5 = [(np.diff(D.st_p5.astype(int)) == -1).sum() for D in DAYS]
    L.append(f"cancelaciones/dia (transiciones lo->nolo, cota superior: supone orden viva en cada lo): detector {np.mean(can):.1f} (min {min(can)}, max {max(can)}); altas/dia {np.mean(alt):.1f}; p5 10 min {np.mean(can5):.1f}")
    L.append('## 4a. 215 rellenos reales de B (20-23 Oct, E1; tm3 = sello v4 del relleno; pnl = size*(gana-precio)); n pequeno')
    Fb = pd.read_pickle(HERE + '/B_fills_v4.pkl'); Fb['tm3'] = Fb.tm3.astype('int64') if 'tm3' in Fb else None
    assert Fb.tm3.notna().all() and len(Fb) == 215
    Fb['pnl'] = Fb['size'] * (Fb.gana - Fb.precio); Fb['coste'] = Fb['size'] * Fb.precio; byd = {D.d: D for D in DAYS}
    for Lms in (0, 35, 110):
        for dn, fn in (('p5 10 min', stp), (repr(p), stf), ('verdad d<30', None)):
            c = {}
            for d, g in Fb.groupby('dia'):
                D = byd[d]; day0 = int(pd.Timestamp(d + 'T00:00:00Z').value // 10**6); s = sec_de(g.tm3.values.astype(np.int64), day0, Lms); st = (D.vs[s] == 1) if fn is None else fn(D)[s]; tr = D.vs[s]
                for nm, m in (('lo', st), ('nolo', ~st)):
                    for tv, tn in ((1, 'verdadlo'), (0, 'verdadhi'), (-1, 'verdadamb')):
                        mm = m & (tr == tv); k = f'{nm}/{tn}'; a = c.get(k, [0, 0., 0.]); c[k] = [a[0] + int(mm.sum()), a[1] + float(g.coste.values[mm].sum()), a[2] + float(g.pnl.values[mm].sum())]
            L.append(f"L={Lms:>3} {dn:<24} " + ' | '.join(f"{k} n={v[0]} {v[1]:.1f} EUR pnl {v[2]:+.2f}" for k, v in c.items() if v[0]))
    L.append(f"B total n=215, coste {Fb.coste.sum():.1f} EUR, pnl {Fb.pnl.sum():+.2f}")
    open(HERE + '/T4c_final.txt', 'w').write('\n'.join(L) + '\n'); print('\n'.join(x[:900] for x in L))
