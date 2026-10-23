#!/usr/bin/env python3
"""e2_eval.py MODO [var...] -- PREREG_E2 (sha 86ffe92c...). MODO tune: pierde L por celda en TUNE y elige; eval: criterios O1-O4,B0-B5 en EVAL con la celda elegida
(la lee de datos/e2_celda_elegida.json que escribe 'tune'). Semilla 20261023."""
import os, sys, json, hashlib, datetime
sys.dont_write_bytecode = True
AQ = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(AQ, '..', 'datos'); CVD = os.path.join(AQ, '../../cola_vs_cruce/datos'); CPD = os.path.join(AQ, '../../cola_posicion/datos')
assert hashlib.sha256(open(os.path.join(AQ, '..', 'prereg', 'PREREG_E2_ORDEN_DECIDIR.md'), 'rb').read()).hexdigest().startswith('86ffe92c14e58312')
import numpy as np, pandas as pd
from scipy import stats
rng = np.random.default_rng(20261023)
MODO = sys.argv[1]; VARS = sys.argv[2:] or ['base']
R = pd.read_csv(os.path.join(D, 'cal_real_pujas.csv'), dtype={'mid': str})
RO = json.load(open('/root/polymarket-research-datalogs/cola_posicion/ordenes_b.json'))
ts = lambda s: datetime.datetime.fromisoformat(s).timestamp()
LP, LC = 0.085, 0.055
ro = pd.DataFrame([dict(slug=x['slug'], n=x['n_orden'], precio=x['precio'], t_dec=x['t_dec'], t_live=x['t_dec'] + LP,
                        t_can_eff=(ts(x['t_cancel_int']) + LC) if 't_cancel_int' in x else np.nan,
                        filled=int(bool(x.get('lect') or x.get('pf') or x.get('tardio'))), t_fuera=ts(x['t_fuera'])) for x in RO])
ro['vida'] = ro.t_can_eff - ro.t_live
agg = ro.groupby('slug').agg(n_ord_r=('n', 'size'), fills_r=('filled', 'sum'))
R = R.join(agg, on='slug'); R['n_ord_r'] = R.n_ord_r.fillna(0)
BC = pd.read_csv(os.path.join(CVD, 'b_clase.csv'), dtype={'mid': str}).drop_duplicates(['tx', 'c']); BC['lado_s'] = BC.lado.map({'YES': 'Y', 'NO': 'N'})
CO = pd.read_csv(os.path.join(CPD, 'b_cola.csv'), dtype={'mid': str}); CO1 = CO[CO.es_primera == 1].dropna(subset=['t_print']).copy()
CO1['mid'] = CO1.mid.astype(float).astype(int).astype(str); tp = CO1.groupby('mid').agg(t_print=('t_print', 'min'), vida_ms=('vida_ms', 'min')); R = R.join(tp, on='mid')
fb = BC[BC.es_b == 1].groupby(['mid', 'lado_s']).agg(coste=('coste', 'sum'), pnl=('pnl', 'sum'), acc=('acc', 'sum'), cl=('cl_h1_0.005', 'first')).reset_index()
COMPLETA = ['t_stop', 'relleno']
def kappa(a, b):
    po = (a == b).mean(); pe = a.mean() * b.mean() + (1 - a.mean()) * (1 - b.mean()); return (po - pe) / (1 - pe) if pe < 1 else np.nan
def carga(var, tag):
    P = pd.read_csv(os.path.join(D, f'e2_{tag}_{var}_pujas.csv'), dtype={'mid': str}); O = pd.read_csv(os.path.join(D, f'e2_{tag}_{var}_ordenes.csv'), dtype={'mid': str}); return P, O
def juntar(P, O, cad, dobs, dias):
    p = P[(P.cad == cad) & (P.dobs == dobs)]; o = O[(O.cad == cad) & (O.dobs == dobs)]
    J = R[R.dia.isin(dias)].merge(p, on='mid', how='left', suffixes=('', '_s'))
    return J, p, o
def lado_ok(J): return J.lado_sim == J.real_lado
def orden_metricas(J, o, ro_):
    """metricas de orden en pujas completas con mismo lado y mercado simulado."""
    Jc = J[lado_ok(J) & J.fin_puja.isin(COMPLETA)]
    mids = set(Jc.mid)
    os_ = o[o.mid.isin(mids)]
    # sim
    n_sim = Jc.n_ord_s.fillna(0).values; n_real = Jc.n_ord_r.values
    out = dict(n_pujas=len(Jc), ord_sim=n_sim.mean(), ord_real=n_real.mean(), spearman=stats.spearmanr(n_sim, n_real).correlation)
    life_s = (os_.t_can_eff - os_.t_live).dropna(); slugs = set(Jc.slug)
    rr = ro_[ro_.slug.isin(slugs)]; life_r = rr.vida.dropna()
    out.update(vida_sim_med=life_s.median(), vida_real_med=life_r.median(), n_vida=(len(life_s), len(life_r)), ks=stats.ks_2samp(life_s, life_r).statistic)
    out.update(haz_sim=os_.filled.sum() / max(len(os_), 1), haz_real=rr.filled.sum() / max(len(rr), 1), fills=(int(os_.filled.sum()), int(rr.filled.sum())), ordenes=(len(os_), len(rr)))
    # por segundo vivo (vida cancelada o hasta relleno)
    ls = np.where(os_.filled == 1, np.where(os_.fill_r.notna(), os_.fill_r / 1000.0 - os_.t_live, 0), (os_.t_can_eff - os_.t_live)); ls = np.nan_to_num(ls, nan=0.0)
    lr = np.where(rr.filled == 1, rr.t_fuera - rr.t_live, rr.vida); lr = np.nan_to_num(lr, nan=0.0)
    out.update(hazs_sim=os_.filled.sum() / max(ls.sum(), 1e-9), hazs_real=rr.filled.sum() / max(lr.sum(), 1e-9))
    # primera orden
    f1s = os_.sort_values('n').groupby('mid').head(1).set_index('mid'); f1r = rr.sort_values('n').groupby('slug').head(1).set_index('slug')
    pr = [];
    for _, r in Jc.iterrows():
        if r.mid in f1s.index and r.slug in f1r.index: pr.append((f1s.loc[r.mid].precio == f1r.loc[r.slug].precio, abs(f1s.loc[r.mid].t_dec - f1r.loc[r.slug].t_dec)))
    pr = np.array(pr, float); out.update(o4_precio=pr[:, 0].mean() if len(pr) else np.nan, o4_t=(pr[:, 1] <= 1.0).mean() if len(pr) else np.nan, o4_n=len(pr))
    return out
def perdida(m): return abs(np.log(m['ord_sim'] / m['ord_real'])) + abs(np.log(m['haz_sim'] / m['haz_real'])) + abs(np.log(m['vida_sim_med'] / m['vida_real_med']))
def fmt(m): return ' '.join(f'{k}={v:.3f}' if isinstance(v, float) else f'{k}={v}' for k, v in m.items())

if MODO == 'tune':
    P, O = carga(VARS[0], 'tune'); res = []
    for (cad, dobs), _ in P.groupby(['cad', 'dobs']):
        J, p, o = juntar(P, O, cad, dobs, ['2026-10-20']); m = orden_metricas(J, o, ro); m['L'] = perdida(m); m.update(cad=cad, dobs=dobs)
        JJ = J[lado_ok(J)]; a, b = JJ.fill.fillna(0).values, JJ.rf_a.values; m.update(tasa_sim=a.mean(), tasa_real=b.mean(), kappa=kappa(a, b), b0=lado_ok(J).sum() / max(J.lado_sim.notna().sum(), 1))
        res.append(m); print(fmt(m))
    best = min(res, key=lambda m: m['L']); print('\nCELDA ELEGIDA (min L en TUNE):', best['cad'], best['dobs'], 'L=%.3f' % best['L'])
    json.dump(dict(cad=float(best['cad']), dobs=int(best['dobs'])), open(os.path.join(D, 'e2_celda_elegida.json'), 'w'))
    sys.exit()

CEL = json.load(open(os.path.join(D, 'e2_celda_elegida.json'))); cad, dobs = CEL['cad'], CEL['dobs']
EV_DIAS = ['2026-10-21', '2026-10-22']; RF = 'rf_a'
for var in VARS:
    P, O = carga(var, 'eval'); J, p, o = juntar(P, O, cad, dobs, EV_DIAS)
    n_sim_mkt = int(J.lado_sim.notna().sum() + 0); nR = len(J)
    print(f'\n################ EVAL var={var} cad={cad} dobs={dobs} dias={EV_DIAS}  pujas reales {nR}; con puja en el sim {n_sim_mkt}; mismo lado {int(lado_ok(J).sum())}')
    print(f'B0 lado coincide {lado_ok(J).sum()/max(nR,1):.3f} (sobre todas las reales) | {lado_ok(J).sum()/max(n_sim_mkt,1):.3f} (sobre las que el sim abre)')
    m = orden_metricas(J, o, ro); print('ORDEN:', fmt(m))
    JJ = J[lado_ok(J)].copy(); a, b = JJ.fill.fillna(0).values, JJ[RF].values
    ci = lambda f, n: np.percentile([f(rng.integers(0, n, n)) for _ in range(2000)], [5, 95])
    print(f'B1 tasa sim {a.mean():.3f} real {b.mean():.3f} diff {a.mean()-b.mean():+.3f} IC90 {np.round(ci(lambda i: a[i].mean()-b[i].mean(), len(a)),3)}')
    print(f'B2 exactitud {(a==b).mean():.3f} kappa {kappa(a,b):.3f} IC90 {np.round(ci(lambda i: kappa(a[i],b[i]), len(a)),3)} recall {a[b==1].mean():.3f} precision {b[a==1].mean():.3f} (11={int(((a==1)&(b==1)).sum())} 10={int(((a==1)&(b==0)).sum())} 01={int(((a==0)&(b==1)).sum())} 00={int(((a==0)&(b==0)).sum())})')
    JJ['age_sim'] = (JJ.r - JJ.tl) / 1000.0; JJ['age_real'] = JJ.vida_ms / 1000.0
    fs = JJ[JJ.fill == 1].age_sim.dropna(); fr = JJ[JJ[RF] == 1].age_real.dropna(); ks = stats.ks_2samp(fs, fr)
    Pp = JJ[(JJ.fill == 1) & (JJ[RF] == 1)].dropna(subset=['r', 't_print']); dt = (Pp.r - Pp.t_print) / 1000.0
    print(f'B3 edad sim n={len(fs)} med {fs.median():.2f}s | real n={len(fr)} med {fr.median():.2f}s | KS D={ks.statistic:.3f} p={ks.pvalue:.3f} |dmed|={abs(fs.median()-fr.median()):.2f}s | pares n={len(Pp)} |dt|<=1s {(dt.abs()<=1).mean():.3f}')
    JJ['coste_s'] = np.where(JJ.fill == 1, JJ.acc * JJ.p, 0.0); JJ['pnl_s'] = np.where(JJ.fill == 1, JJ.acc * JJ.gana - JJ.acc * JJ.p, 0.0)
    JJ = JJ.merge(fb, left_on=['mid', 'real_lado'], right_on=['mid', 'lado_s'], how='left', suffixes=('', '_r')); JJ['coste_r'] = JJ.coste.fillna(0.0); JJ['pnl_r'] = JJ.pnl.fillna(0.0)
    evs = lambda i: JJ.pnl_s.values[i].sum() / max(JJ.coste_s.values[i].sum(), 1e-9); evr = lambda i: JJ.pnl_r.values[i].sum() / max(JJ.coste_r.values[i].sum(), 1e-9)
    allI = np.arange(len(JJ)); dd = lambda i: evs(i) - evr(i)
    print(f'B4 EV sim {evs(allI):+.3f} (coste {JJ.coste_s.sum():.1f}) | real on-chain {evr(allI):+.3f} (coste {JJ.coste_r.sum():.1f}) | diff {dd(allI):+.3f} IC90 {np.round(ci(dd, len(JJ)),3)}')
    ms = JJ[JJ.fill == 1].groupby('clase').coste_s.sum(); ms = ms / ms.sum(); mr = JJ[JJ.coste_r > 0].groupby('cl').coste_r.sum(); mr = mr / mr.sum()
    dq = {c: abs(ms.get(c, 0) - mr.get(c, 0)) for c in ('C1', 'C2', 'C3')}
    print('   cuotas coste sim', ms.round(3).to_dict(), '| on-chain', mr.round(3).to_dict(), '| |d|', {k: round(v, 3) for k, v in dq.items()})
    for nm, mm in (('ambos', (JJ.fill == 1) & (JJ.coste_r > 0)), ('solo sim', (JJ.fill == 1) & (JJ.coste_r == 0)), ('solo real', (JJ.fill != 1) & (JJ.coste_r > 0))):
        s = JJ[mm]; ps = s.pnl_s.sum() if nm != 'solo real' else s.pnl_r.sum(); cs = s.coste_s.sum() if nm != 'solo real' else s.coste_r.sum()
        print(f'   {nm:9s} n={len(s):3d} EV {ps/max(cs,1e-9):+.3f}')
    b5 = []
    for act, g in JJ.groupby('act'):
        es = g.pnl_s.sum() / max(g.coste_s.sum(), 1e-9); er = g.pnl_r.sum() / max(g.coste_r.sum(), 1e-9)
        gi = np.arange(len(g)); f = lambda i: (g.pnl_s.values[i].sum() / max(g.coste_s.values[i].sum(), 1e-9)) - (g.pnl_r.values[i].sum() / max(g.coste_r.values[i].sum(), 1e-9))
        ic = np.round(ci(f, len(g)), 3); ok = ((np.sign(es) == np.sign(er)) if abs(er) > 0.05 else (abs(es - er) <= 0.10)) and abs(es - er) <= 0.30
        b5.append(ok); print(f'   B5 {act}: n={len(g)} tasa sim {g.fill.mean():.3f} real {g[RF].mean():.3f} EV sim {es:+.3f} real {er:+.3f} dEV {es-er:+.3f} IC90 {ic} -> {"PASA" if ok else "FALLA"}')
    crit = {'O1': (0.85 <= m['ord_sim'] / m['ord_real'] <= 1.15) and m['spearman'] >= 0.60, 'O2': abs(np.log(m['vida_sim_med'] / m['vida_real_med'])) <= np.log(1.25) and m['ks'] <= 0.15,
            'O3': (0.80 <= m['haz_sim'] / m['haz_real'] <= 1.25) and (0.80 <= m['hazs_sim'] / m['hazs_real'] <= 1.25), 'O4': m['o4_precio'] >= 0.85 and m['o4_t'] >= 0.70,
            'B0': lado_ok(J).sum() / max(n_sim_mkt, 1) >= 0.90, 'B1': abs(a.mean() - b.mean()) <= 0.05, 'B2': (a == b).mean() >= 0.80 and kappa(a, b) >= 0.60 and a[b == 1].mean() >= 0.75 and b[a == 1].mean() >= 0.75,
            'B3': ks.statistic <= 0.15 and abs(fs.median() - fr.median()) <= 0.5 and (dt.abs() <= 1).mean() >= 0.70, 'B4': abs(dd(allI)) <= 0.10 and all(v <= 0.10 for v in dq.values()), 'B5': all(b5)}
    print('CRITERIOS:', {k: ('PASA' if v else 'FALLA') for k, v in crit.items()})
