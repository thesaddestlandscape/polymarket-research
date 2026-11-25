#!/usr/bin/env python3
"""t3_v2_gate.py -- copia VERSIONADA del juez forward_v2.py (no se edita el original ni su prereg; el sha del prereg se verifica). SPEC_F5_V4_17nov.md T1(b), T2, T3.
Mismas 8 condiciones, mismos cortes C0/C1 del TRAIN y mismas formulas; cambios SOLO: grupo de monedas parametrizable (--coins ETH,SOL,XRP | BTC), filtro opcional de clase causal pura (--pura: excluye indet/mixta; t = r-100 ms), salida a esta carpeta, sin Telegram.
Uso: python3 -I t3_v2_gate.py --coins ETH,SOL,XRP [--pura] [--desde 2026-11-04] [--tag NOMBRE]. Salida: V2_<tag>.md y V2_<tag>.json (cifras por dia y totales; EV por EUR y por unidad mercado-lado)."""
import glob, hashlib, json, os, sys
import numpy as np, pandas as pd
from scipy import stats
HERE = os.path.dirname(os.path.abspath(__file__)); AQ = '/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/mitigar_as_25oct/forward'; DL = '/root/polymarket-research-datalogs/mitigar_as_25oct/forward/'; CACHE = HERE + '/cache/'
assert hashlib.sha256(open(AQ + '/PREREG_FWD_V2.md', 'rb').read()).hexdigest() == open(AQ + '/PREREG_FWD_V2.sha256').read().split()[0], 'prereg V2 alterado'
C0, C1 = 3.526360511779785, 4.717426776885986
F2E = np.array(json.load(open(AQ + '/regla_congelada.json'))['F2_deciles_train'])
def cell_f2(F2): return np.where(np.isfinite(F2), np.searchsorted(F2E, np.nan_to_num(F2), 'right'), -1)
arg = lambda k, dflt: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else dflt
desde = arg('--desde', '2026-11-04'); hasta = arg('--hasta', '2026-11-14'); COINS = tuple(arg('--coins', 'ETH,SOL,XRP').split(',')); PURA = '--pura' in sys.argv; TAG = arg('--tag', ('_'.join(COINS)) + ('_pura' if PURA else '_base'))
def t_ic(x):
    x = np.asarray(x, float); n = len(x)
    if n < 3: return np.nan, np.nan, np.nan
    se = x.std(ddof=1) / np.sqrt(n); t = x.mean() / se if se > 0 else np.nan
    return x.mean() - stats.t.ppf(0.95, n - 1) * se, stats.t.sf(t, n - 1), x.mean()
def clase_prints(d, r):
    z = np.load(CACHE + f'clases_{d}.npz'); cls = z['cls']; day0 = int(pd.Timestamp(d + 'T00:00:00Z').value // 10**6); B = ((np.asarray(r, np.int64) - 100 - day0) // 10_000).astype(np.int64)
    return np.where((B >= 0) & (B < len(cls)), cls[np.clip(B, 0, len(cls) - 1)], 'indet').astype(str)
dias, malos, filas, cier = [], [], [], []; excl = []
for p in sorted(glob.glob(DL + 'prints_2026-*.pkl')):
    d = os.path.basename(p)[7:17]
    if d < desde or d > hasta: continue
    try: man = json.load(open(DL + f'manifest_{d}.json')); c = man['cobertura']
    except Exception: malos.append((d, 'sin manifiesto')); continue
    if man.get('estado') != 'COMPLETE' or c['cobertura_desenlace_coste'] < 0.995 or c['F5_valido'] < 0.98: malos.append((d, f"cob {c.get('cobertura_desenlace_coste')} F5 {c.get('F5_valido')}")); continue
    F = pd.read_pickle(p)[['coin', 'F5', 'F2', 'hora', 'pnl', 'coste', 'fin', 'r', 'mid', 'lado_m']]; G = F[F.coin.isin(COINS)].copy()
    cl = clase_prints(d, G.r.values) if PURA or '--clase' in sys.argv else None
    if cl is not None:
        G['clase'] = cl; excl.append(dict(dia=d, prints=int(len(G)), coste=float(G.coste.sum()), **{f'prints_{k}': int((cl == k).sum()) for k in ('lo', 'hi', 'mixta', 'indet')}, **{f'coste_{k}': float(G.coste[cl == k].sum()) for k in ('lo', 'hi', 'mixta', 'indet')}))
        if PURA: G = G[np.isin(cl, ('lo', 'hi'))]
    f5, pn, co = G.F5.values, G.pnl.values, G.coste.values; ok = np.isfinite(f5)
    ter = {'bajo': ok & (f5 <= C0), 'medio': ok & (f5 > C0) & (f5 <= C1), 'alto': ok & (f5 > C1)}
    r = dict(dia=d)
    for t, m in ter.items():
        fd = co[m].sum() / co.sum(); r['exc_' + t] = fd * pn.sum() - pn[m].sum(); r['pnl_' + t] = pn[m].sum(); r['co_' + t] = co[m].sum(); r['n_' + t] = int(m.sum())
        u = pd.DataFrame({'mid': G.mid.values[m], 'lado': G.lado_m.values[m], 'p': pn[m], 'c': co[m]}).groupby(['mid', 'lado']).agg(p=('p', 'sum'), c=('c', 'sum')); r['uni_' + t] = (u.p / u.c).tolist()
    cell = pd.Series(cell_f2(G.F2.values).astype(str)) + '|' + pd.Series(G.coin.values) + '|' + pd.Series(G.hora.values.astype(str))
    es = 0.0
    for _, gg in pd.DataFrame({'c': cell.values, 'pnl': pn, 'co': co, 'm': ter['alto']}).groupby('c'):
        cs = gg.co.sum()
        if cs > 0: es += gg.co[gg.m].sum() / cs * gg.pnl.sum() - gg.pnl[gg.m].sum()
    r['exc_rt'] = es
    fd = co[ter['alto']].sum() / co.sum(); e = pd.DataFrame({'fin': G.fin.values, 'e': fd * pn - np.where(ter['alto'], pn, 0)}).groupby('fin').e.sum()
    cier += [(d, k, v) for k, v in e.items()]; filas.append(r); dias.append(d)
R = pd.DataFrame(filas); n = len(R); out = dict(tag=TAG, coins=COINS, pura=PURA, desde=desde, dias=dias, malos=malos, n_dias=n)
L = [f"# V2 gate (copia versionada, F5-V4 17-Nov) grupo {COINS} {'SOLO clase causal pura' if PURA else '(sin filtro de clase)'} desde {desde}", f"Dias validos: {n} {dias}", f"Dias malos/excluidos: {malos}", '']
if excl:
    E = pd.DataFrame(excl); tot = E[[c for c in E.columns if c.startswith(('prints', 'coste'))]].sum(); out['exclusion_clase'] = {k: float(v) for k, v in tot.items()}; out['exclusion_clase_por_dia'] = excl
    L.append(f"Clase causal por print (t=r-100 ms): prints {int(tot.prints)} | lo {int(tot.prints_lo)} hi {int(tot.prints_hi)} mixta {int(tot.prints_mixta)} indet {int(tot.prints_indet)} | EUR excluidos (mixta+indet) {(tot.coste_mixta + tot.coste_indet) / tot.coste * 100:.2f} % del coste; prints excluidos {(tot.prints_mixta + tot.prints_indet) / tot.prints * 100:.2f} %"); L.append('')
if n < 3: L.append('Insuficiente (<3 dias).')
else:
    ev = {t: R['pnl_' + t].sum() / R['co_' + t].sum() for t in ('bajo', 'medio', 'alto')}; evu = {t: float(np.mean(np.concatenate(R['uni_' + t].values))) for t in ('bajo', 'medio', 'alto')}
    dba = R.pnl_bajo / R.co_bajo - R.pnl_alto / R.co_alto
    ic1, p1, m1 = t_ic(R.exc_alto); s2 = R.exc_alto.sort_values(); sin2 = s2.iloc[:-2].sum()
    rng = np.random.default_rng(20261104); Cc = pd.DataFrame(cier, columns=['d', 'k', 'v']).groupby('k').v.sum().values
    bs = np.array([rng.choice(Cc, len(Cc)).sum() for _ in range(1000)]); icc = np.percentile(bs, 5)
    icd, _, mdd = t_ic(dba); icr, _, _ = t_ic(R.exc_rt)
    g = {'1_exc_alto>0 IC90 dias inf>0': bool(R.exc_alto.sum() > 0 and ic1 > 0), '2_p<0,05': bool(p1 < 0.05), '3_sin2mejores>0': bool(sin2 > 0), '4_exc_bajo<0': bool(R.exc_bajo.sum() < 0),
         '5_monotonia': bool(ev['bajo'] > ev['medio'] > ev['alto'] and (dba > 0).mean() >= 2 / 3 and icd > 0), '6_IC90 cierre inf>0': bool(icc > 0), '7_dias exc_alto>0 >=2/3': bool((R.exc_alto > 0).mean() >= 2 / 3), 'RT_base F2xmonedaxhora SumEXCESO>0 (literal del prereg)': bool(R.exc_rt.sum() > 0)}
    gate = all(g.values()); co_t = {t: float(R['co_' + t].sum()) for t in ('bajo', 'medio', 'alto')}
    L += [f"EV bajo/medio/alto (pond. EUR): {ev['bajo']:+.3f} / {ev['medio']:+.3f} / {ev['alto']:+.3f}   | EV por unidad mercado-lado: {evu['bajo']:+.3f} / {evu['medio']:+.3f} / {evu['alto']:+.3f}",
          f"coste EUR bajo/medio/alto {co_t['bajo']:.0f} / {co_t['medio']:.0f} / {co_t['alto']:.0f}; prints {int(R.n_bajo.sum())} / {int(R.n_medio.sum())} / {int(R.n_alto.sum())}",
          f"exceso alto {R.exc_alto.sum():+.0f} (IC90 dias inf {ic1:+.0f}, p {p1:.4f}, sin 2 mejores {sin2:+.0f}, dias+ {(R.exc_alto>0).sum()}/{n}), exceso bajo {R.exc_bajo.sum():+.0f}",
          f"bajo-alto por dia {mdd:+.3f} (IC90 inf {icd:+.3f}; dias+ {(dba>0).sum()}/{n}); IC90 cierre exceso alto inf {icc:+.0f}", '', f"RT (base F2xmonedaxhora) exceso {R.exc_rt.sum():+.0f} (IC90 dias inf {icr:+.0f}, dias+ {(R.exc_rt>0).sum()}/{n})", '', '## Gate (incluye placebo RT)'] + [f"- {k}: {'SI' if v else 'no'}" for k, v in g.items()]
    L.append(f"**{'LISTO: gate cumplido (incl. RT) si n>=10' if gate and n >= 10 else 'EN CURSO / no cumple'}**")
    out.update(ev=ev, ev_unidad=evu, coste=co_t, exc_alto=float(R.exc_alto.sum()), ic90_dias_inf=float(ic1), p=float(p1), sin2=float(sin2), dias_pos=int((R.exc_alto > 0).sum()), exc_bajo=float(R.exc_bajo.sum()), bajo_alto_dia=float(mdd), ic90_bajo_alto_inf=float(icd), dias_pos_ba=int((dba > 0).sum()),
               ic90_cierre_inf=float(icc), rt=float(R.exc_rt.sum()), rt_ic90_inf=float(icr), rt_dias_pos=int((R.exc_rt > 0).sum()), gate=g, gate_ok=bool(gate), por_dia={r.dia: dict(exc_alto=float(r.exc_alto), exc_bajo=float(r.exc_bajo), co_bajo=float(r.co_bajo), co_medio=float(r.co_medio), co_alto=float(r.co_alto), pnl_bajo=float(r.pnl_bajo), pnl_medio=float(r.pnl_medio), pnl_alto=float(r.pnl_alto)) for r in R.itertuples()})
open(HERE + f'/V2_{TAG}.md', 'w').write('\n'.join(L)); json.dump(out, open(HERE + f'/V2_{TAG}.json', 'w'), indent=1, default=str); print('\n'.join(L))
