#!/usr/bin/env python3
"""cal_eval.py -- PREREG_E1 criterios B0-B4. Entrada datos/cal_sim.csv, cal_real_pujas.csv, b_clase.csv, b_cola.csv. Semilla 20261023."""
import os, sys, hashlib
AQ = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(AQ, '..', 'datos'); CVD = os.path.join(AQ, '../../cola_vs_cruce/datos'); CPD = os.path.join(AQ, '../../cola_posicion/datos')
assert hashlib.sha256(open(os.path.join(AQ, '..', 'prereg', 'PREREG_E1_CALIBRACION.md'), 'rb').read()).hexdigest().startswith('001c130d2e5a1d73')
import numpy as np, pandas as pd
from scipy import stats
rng = np.random.default_rng(20261023)
S = pd.read_csv(os.path.join(D, 'cal_sim.csv'), dtype={'mid': str}); R = pd.read_csv(os.path.join(D, 'cal_real_pujas.csv'), dtype={'mid': str})
BC = pd.read_csv(os.path.join(CVD, 'b_clase.csv'), dtype={'mid': str}).drop_duplicates(['tx', 'c'])
CO = pd.read_csv(os.path.join(CPD, 'b_cola.csv'), dtype={'mid': str})
BC['lado_s'] = BC.lado.map({'YES': 'Y', 'NO': 'N'})
MODE = sys.argv[1] if len(sys.argv) > 1 else 'a'            # a: rf_a (ledger puja_fin.rellenos) | u: union
RF = 'rf_a' if MODE == 'a' else 'rf_union'
# tiempo de relleno real: primer print que relleno por puja (mid, lado): t_print ms (recepcion) y vida_ms
CO1 = CO[CO.es_primera == 1].dropna(subset=['t_print']).copy()
CO1['mid'] = CO1.mid.astype(float).astype(int).astype(str)
tp = CO1.groupby('mid').agg(t_print=('t_print', 'min'), vida_ms=('vida_ms', 'min'))
R = R.join(tp, on='mid')
# fills reales (on-chain) por puja
fb = BC[BC.es_b == 1].groupby(['mid', 'lado_s']).agg(coste=('coste', 'sum'), pnl=('pnl', 'sum'), acc=('acc', 'sum'), cl=('cl_h1_0.005', 'first')).reset_index()
def kappa(a, b):
    po = (a == b).mean(); pe = a.mean() * b.mean() + (1 - a.mean()) * (1 - b.mean()); return (po - pe) / (1 - pe) if pe < 1 else np.nan
def cell_table(dias):
    out = []
    for (lc, al), s in S.groupby(['lat_can', 'alloc']):
        J = R[R.dia.isin(dias)].merge(s, on='mid', suffixes=('', '_s')); J = J[J.lado_sim == J.real_lado]
        a, b = J.fill.values, J[RF].values
        out.append(dict(lat_can=lc, alloc=al, n=len(J), tasa_sim=a.mean(), tasa_real=b.mean(), acu=(a == b).mean(), kappa=kappa(a, b),
                        recall=a[b == 1].mean(), prec=b[a == 1].mean()))
    return pd.DataFrame(out)
tune = cell_table(['2026-10-20']); print(f'== modo {RF}. TUNE 20-Oct: rejilla (cada celda: n pujas, tasa, acuerdo, kappa)'); print(tune.round(3).to_string(index=False))
tb = tune.sort_values(['kappa', 'tasa_sim'], ascending=[False, True])
tb['dtasa'] = (tb.tasa_sim - tb.tasa_real).abs(); best = tune.assign(dtasa=(tune.tasa_sim - tune.tasa_real).abs()).sort_values(['kappa', 'dtasa'], ascending=[False, True]).iloc[0]
print('\ncelda elegida en TUNE:', int(best.lat_can), best.alloc)
EV_DIAS = ['2026-10-21', '2026-10-22']
def evalua(lc, al, dias, nombre):
    s = S[(S.lat_can == lc) & (S.alloc == al)]
    J = R[R.dia.isin(dias)].merge(s, on='mid', suffixes=('', '_s'))
    n_all = len(J); J = J[J.lado_sim == J.real_lado].copy()
    print(f'\n######## {nombre}: lat_can={lc} alloc={al}  dias={dias}  pujas con mercado en sim {n_all}; mismo lado {len(J)} (B0 = {len(J)/max(n_all,1):.3f})')
    a, b = J.fill.values, J[RF].values
    ci = lambda f: np.percentile([f(rng.integers(0, len(J), len(J))) for _ in range(2000)], [5, 95])
    f_tasa = lambda i: a[i].mean() - b[i].mean()
    print(f'B1 tasa sim {a.mean():.3f} real {b.mean():.3f}  diff {a.mean()-b.mean():+.3f} IC90 mercados {np.round(ci(f_tasa),3)}')
    print(f'B2 exactitud {(a==b).mean():.3f}  kappa {kappa(a,b):.3f} IC90 {np.round(ci(lambda i: kappa(a[i],b[i])),3)}  recall {a[b==1].mean():.3f}  precision {b[a==1].mean():.3f}  (tabla sim/real: 11={int(((a==1)&(b==1)).sum())} 10={int(((a==1)&(b==0)).sum())} 01={int(((a==0)&(b==1)).sum())} 00={int(((a==0)&(b==0)).sum())})')
    # B3 edad
    J['age_sim'] = (J.r - J.tl) / 1000.0; J['age_real'] = J.vida_ms / 1000.0
    fs = J[J.fill == 1].age_sim.dropna(); fr = J[(J[RF] == 1)].age_real.dropna()
    ks = stats.ks_2samp(fs, fr)
    print(f'B3 edad al relleno: sim n={len(fs)} mediana {fs.median():.2f}s p25/p75 {fs.quantile(.25):.2f}/{fs.quantile(.75):.2f} | real n={len(fr)} mediana {fr.median():.2f}s p25/p75 {fr.quantile(.25):.2f}/{fr.quantile(.75):.2f} | KS D={ks.statistic:.3f} p={ks.pvalue:.3f} |dmed|={abs(fs.median()-fr.median()):.2f}s')
    # tiempo de relleno absoluto en pares
    P = J[(J.fill == 1) & (J[RF] == 1)].dropna(subset=['r', 't_print'])
    dt = (P.r - P.t_print) / 1000.0
    print(f'   pares con relleno en ambos y t_print real: n={len(P)}  |t_sim-t_real|<=1s: {(dt.abs()<=1).mean():.3f} (<=0,3s {(dt.abs()<=0.3).mean():.3f}); dif mediana {dt.median():+.2f}s p10/p90 {dt.quantile(.1):+.2f}/{dt.quantile(.9):+.2f}')
    # B4 EV
    J['coste_s'] = np.where(J.fill == 1, J.acc * J.p, 0.0); J['pnl_s'] = np.where(J.fill == 1, J.acc * J.gana - J.acc * J.p, 0.0)
    J = J.merge(fb, left_on=['mid', 'real_lado'], right_on=['mid', 'lado_s'], how='left', suffixes=('', '_r'))
    J['coste_r'] = J.coste.fillna(0.0); J['pnl_r'] = J.pnl.fillna(0.0)
    evs = lambda i: J.pnl_s.values[i].sum() / max(J.coste_s.values[i].sum(), 1e-9); evr = lambda i: J.pnl_r.values[i].sum() / max(J.coste_r.values[i].sum(), 1e-9)
    allI = np.arange(len(J)); d = lambda i: evs(i) - evr(i)
    print(f'B4 EV sim {evs(allI):+.3f} (coste {J.coste_s.sum():.1f}, pnl {J.pnl_s.sum():+.2f}) | real on-chain {evr(allI):+.3f} (coste {J.coste_r.sum():.1f}, pnl {J.pnl_r.sum():+.2f}) | diff {d(allI):+.3f} IC90 mercados {np.round(ci(d),3)}')
    for nm, m in (('ambos', (J.fill == 1) & (J.coste_r > 0)), ('solo sim', (J.fill == 1) & (J.coste_r == 0)), ('solo real', (J.fill == 0) & (J.coste_r > 0))):
        s = J[m]; ps = s.pnl_s.sum() if nm != 'solo real' else s.pnl_r.sum(); cs = s.coste_s.sum() if nm != 'solo real' else s.coste_r.sum()
        extra = ''
        if nm == 'ambos': extra = f' | EV real mismos {s.pnl_r.sum()/max(s.coste_r.sum(),1e-9):+.3f}; precio sim {s.p.mean():.3f} real {(s.coste_r/s.acc_r.replace(0,np.nan)).mean():.3f}'
        print(f'   {nm:9s} n={len(s):3d} coste {cs:7.1f} pnl {ps:+7.2f} EV {ps/max(cs,1e-9):+.3f} hit {s.gana.mean() if len(s) else float("nan"):.3f}{extra}')
    # mezcla de clases
    ms = J[J.fill == 1].groupby('clase').coste_s.sum(); ms = ms / ms.sum(); mr = J[J.coste_r > 0].groupby('cl').coste_r.sum(); mr = mr / mr.sum()
    print('   cuotas de coste sim X1/X2/X3:', ms.round(3).to_dict(), '| real C1/C2/C3:', mr.round(3).to_dict())
    # por moneda
    for act, g in J.groupby('act'):
        print(f'   {act}: n={len(g)} tasa sim {g.fill.mean():.3f} real {g[RF].mean():.3f} acuerdo {(g.fill==g[RF]).mean():.3f} EV sim {g.pnl_s.sum()/max(g.coste_s.sum(),1e-9):+.3f} real {g.pnl_r.sum()/max(g.coste_r.sum(),1e-9):+.3f}')
    return J
evalua(int(best.lat_can), best.alloc, EV_DIAS, 'EVAL celda elegida')
evalua(280, 'prop', EV_DIAS, 'EVAL B_FIEL nominal')
evalua(280, 'prop', ['2026-10-20'], 'TUNE B_FIEL nominal (referencia)')
evalua(int(best.lat_can), best.alloc, ['2026-10-20', '2026-10-21', '2026-10-22'], 'TODOS los dias celda elegida (descriptivo)')
