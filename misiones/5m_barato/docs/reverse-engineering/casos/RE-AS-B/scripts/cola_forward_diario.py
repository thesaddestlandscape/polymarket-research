#!/usr/bin/env python3
"""cola_forward_diario.py [--dia D] [--outdir DIR] [--fwd-desde D0]   (RE-AS-B Tarea B; REGLA CONGELADA en PREREG_COLA_FORWARD.md)
SOLO LECTURA de vida_puja_virtual/vpv_D.csv.gz + maker_ms_desenlaces_cache.json; escribe SOLO en --outdir (por defecto
/root/polymarket-research-datalogs/cola_forward/): cola_fwd_D.csv.gz (unidades del dia, atomico, idempotente) e informe_cola_forward.json.
Sin cron instalado. python3 -I. Por defecto D = ayer UTC. Imprime n/EV/IC por celda y el estado del gate."""
import sys, os, json, gzip, argparse, datetime, numpy as np, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import cola_lib as C
ap = argparse.ArgumentParser(); ap.add_argument('--dia'); ap.add_argument('--outdir', default='/root/polymarket-research-datalogs/cola_forward/')
ap.add_argument('--fwd-desde', default='2026-10-27'); ap.add_argument('--sin-procesar', action='store_true'); a = ap.parse_args()
os.makedirs(a.outdir, exist_ok=True); rng = np.random.default_rng(C.SEED)
COV_MIN, Q_P, Q_S1 = 0.95, 100.0, 25.0; BCOINS = ('ETH', 'SOL', 'XRP')
if not a.sin_procesar:
    d = a.dia or (datetime.datetime.utcnow() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    f = C.VPV % d
    if not os.path.exists(f): print('SIN FICHERO vpv', d, '-> dia no procesado (missing != 0)'); 
    else:
        X = C.cargar_vpv([d]); cob = float(X.gana.notna().mean()); print('dia %s vidas %d cobertura gana %.4f' % (d, len(X), cob))
        if cob < COV_MIN: print('INCOMPLETO: cobertura < %.2f -> dia NO entra' % COV_MIN); json.dump({'dia': d, 'cobertura': cob}, open(os.path.join(a.outdir, 'incompleto_%s.json' % d), 'w'))
        else:
            Q = C.unidades(X)[['dia', 'mercado', 'coin', 'lado', 'cierre', 'b', 'Q0', 'pnl', 'cost']]
            out = os.path.join(a.outdir, 'cola_fwd_%s.csv.gz' % d); Q.to_csv(out + '.tmp', index=False, compression='gzip'); os.replace(out + '.tmp', out)
            print('unidades del dia (primer relleno pes por mercado-lado): %d -> %s' % (len(Q), out))
fs = sorted(g for g in os.listdir(a.outdir) if g.startswith('cola_fwd_') and g[9:19] >= a.fwd_desde)
inc = sorted(g[10:20] for g in os.listdir(a.outdir) if g.startswith('incompleto_') and g[11:21] >= a.fwd_desde)
if not fs: print('Sin dias forward >= %s; incompletos %s' % (a.fwd_desde, inc)); sys.exit(0)
Q = pd.concat([pd.read_csv(os.path.join(a.outdir, g)) for g in fs], ignore_index=True)
Q['bk'] = pd.cut(Q.b, C.BK_EDGES, labels=C.BK_LAB)
cells = {'P  Q0>100 (cualquier moneda)': Q.Q0 > Q_P, 'S1 Q0>25 & ETH/SOL/XRP': (Q.Q0 > Q_S1) & Q.coin.isin(BCOINS), 'S2 BTC & Q0>100': (Q.coin == 'BTC') & (Q.Q0 > Q_P),
         'C  Q0<=25 (donde vive B)': Q.Q0 <= Q_S1, 'ALL': Q.Q0 > -1}
dias = sorted(Q.dia.unique()); print('\ndias forward con datos: %d %s | incompletos: %s' % (len(dias), dias, inc))
def ic_dias(q):
    g = q.groupby('dia').agg(p=('pnl', 'sum'), c=('cost', 'sum')); P, Cc = g.p.values, g.c.values; n = len(g)
    if n < 3: return (np.nan, np.nan)
    v = [P[s].sum() / Cc[s].sum() for s in (rng.integers(0, n, n) for _ in range(C.R))]; return tuple(np.percentile(v, [5, 95]))
res = {}
for nm, m in cells.items():
    q = Q[m]; print('\n== %s' % nm); print(C.linea('acumulado', q, rng))
    if len(q):
        lo, hi = ic_dias(q); print('    IC90 por DIAS (bootstrap de %d dias): (%+.3f,%+.3f)%s' % (q.dia.nunique(), lo, hi, '' if q.dia.nunique() >= 10 else ' [<10 dias: NO informativo]'))
        bd = {d: (len(h), round(float(h.pnl.sum() / h.cost.sum()), 4)) for d, h in q.groupby('dia')}; print('    por dia:', bd)
        e2 = sorted(bd, key=lambda d: -bd[d][1])[:2]; r = q[~q.dia.isin(e2)]
        if len(r) and q.dia.nunique() > 2: print('    sin 2 mejores dias %s: n=%d EVw=%+.4f' % (e2, len(r), r.pnl.sum() / r.cost.sum()))
        res[nm] = dict(n=int(len(q)), dias=int(q.dia.nunique()), evw=float(q.pnl.sum() / q.cost.sum()), ic_dias=[float(lo), float(hi)])
# placebo de permutacion de la etiqueta de cola dentro de dia x moneda x bucket (celda P)
mP = cells['P  Q0>100 (cualquier moneda)']
if mP.sum() >= 3:
    obs = Q[mP].pnl.sum() / Q[mP].cost.sum(); grp = Q.groupby(['dia', 'coin', 'bk'], observed=True).indices; nP = {k: int(mP.values[v].sum()) for k, v in grp.items()}
    pn = Q.pnl.values; cs = Q.cost.values; sim = []
    for _ in range(1000):
        tp = tc = 0.0
        for k, v in grp.items():
            if nP[k] == 0: continue
            s = rng.choice(v, nP[k], replace=False); tp += pn[s].sum(); tc += cs[s].sum()
        sim.append(tp / tc)
    sim = np.array(sim); pval = float((sim >= obs).mean()); print('\nPLACEBO permutacion cola (dia x moneda x bucket): obs %+.4f | placebo media %+.4f p95 %+.4f | p(placebo>=obs)=%.3f' % (obs, sim.mean(), np.percentile(sim, 95), pval))
else: pval = np.nan
# contraste ajustado Q0>25 vs <=25 estratificado por moneda x bucket (pesos = coste del grupo bajo)
hi_, lo_ = Q[Q.Q0 > Q_S1], Q[Q.Q0 <= Q_S1]; ws = []; 
for k, h in lo_.groupby(['coin', 'bk'], observed=True):
    g = hi_[(hi_.coin == k[0]) & (hi_.bk == k[1])]
    if len(g) >= 3 and len(h) >= 3: ws.append((h.cost.sum(), g.pnl.sum() / g.cost.sum(), h.pnl.sum() / h.cost.sum()))
if ws:
    w = np.array(ws); dlt = (w[:, 0] * (w[:, 1] - w[:, 2])).sum() / w[:, 0].sum(); print('CONTRASTE ajustado (Q0>25 menos Q0<=25, celdas moneda x bucket con n>=3 en ambos, pesos coste bajo): %+.4f sobre %d celdas' % (dlt, len(ws)))
# gate
P = res.get('P  Q0>100 (cualquier moneda)')
if P is None: est = 'PENDIENTE (sin unidades en la celda P)'
else:
    qP = Q[mP]; e2 = sorted(qP.dia.unique(), key=lambda d: -(qP[qP.dia == d].pnl.sum() / qP[qP.dia == d].cost.sum()))[:2]; r = qP[~qP.dia.isin(e2)]
    ic_c = C.ic90(qP, rng); ok = (P['n'] >= C.NMIN and P['dias'] >= 10 and P['evw'] > 0 and P['ic_dias'][0] > 0 and ic_c[0] > 0 and len(r) > 0 and r.pnl.sum() > 0 and pval < 0.05)
    est = 'CUMPLE (elegible para PROPUESTA de regla de cola; no es prueba de rentabilidad)' if ok else ('REFUTADA (>=10 dias y IC90 por dias superior < 0)' if (P['dias'] >= 10 and P['ic_dias'][1] < 0) else 'PENDIENTE (n=%d/40, dias=%d/10, EVw=%+.3f)' % (P['n'], P['dias'], P['evw']))
print('\nGATE celda P: %s' % est)
json.dump({'dias': dias, 'incompletos': inc, 'celdas': res, 'p_placebo': pval, 'gate': est}, open(os.path.join(a.outdir, 'informe_cola_forward.json.tmp'), 'w')); os.replace(os.path.join(a.outdir, 'informe_cola_forward.json.tmp'), os.path.join(a.outdir, 'informe_cola_forward.json'))
