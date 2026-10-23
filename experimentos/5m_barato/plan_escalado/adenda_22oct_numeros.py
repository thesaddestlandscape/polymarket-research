# Numeros de ADENDA_22OCT_B_R3.md (22-Oct-2026). Solo lectura. Uso:
#   nice -n 19 ionice -c3 bash -c 'ulimit -v 3000000; python3 adenda_22oct_numeros.py > adenda_22oct_salida.txt'
# Parte 1: n EFECTIVO de entradas independientes/dia (unidad = cierre; Kish n_eff = sum m/(1+(m-1)*ICC)), B real y simulador R3/BASE.
# Parte 2: escalado por escenario con Kelly CORRECTO: g_Kelly = n_eff*EV^2/(2*sigma2), g_halfKelly = 3/8*n_eff*EV^2/sigma2
#          (el PLAN_MAESTRO usaba n*EV^2/sigma2: el doble de rapido). sigma2 por EUR de un relleno binario a p: (1-p)/p.
import csv, collections, glob, math
import numpy as np, pandas as pd
BASE = '/root/polymarket-research/experimentos/5m_barato/'
rng = np.random.default_rng(11)
P_MED = 0.208; SIG2 = (1 - P_MED) / P_MED; S_MIN = 5 * 0.21   # 5 acc minimo del exchange a ~0,21
print(f'sigma2 por EUR (p={P_MED}) = {SIG2:.2f}; stake minimo por relleno {S_MIN:.2f} $')

def icc(groups):
    N = sum(len(x) for x in groups); k = len(groups); mu = np.concatenate(groups).mean()
    msb = sum(len(x) * (x.mean() - mu) ** 2 for x in groups) / (k - 1)
    msw = sum(((x - x.mean()) ** 2).sum() for x in groups) / (N - k)
    n0 = (N - sum(len(x) ** 2 for x in groups) / N) / (k - 1)
    return (msb - msw) / (msb + (n0 - 1) * msw)
def neff(groups, r): return sum(len(x) / (1 + (len(x) - 1) * r) for x in groups)
def rep(groups, ndias, lab):
    r0 = icc(groups); ne0 = neff(groups, r0); rs, ns = [], []
    for _ in range(2000):
        g = [groups[i] for i in rng.integers(0, len(groups), len(groups))]
        try: r = min(max(icc(g), 0), 1)
        except ZeroDivisionError: continue
        rs.append(r); ns.append(neff(groups, r) / ndias)
    n = sum(len(x) for x in groups)
    print(f'{lab}: rellenos {n} ({n/ndias:.1f}/dia) cierres {len(groups)} ({len(groups)/ndias:.1f}/dia) ICC {r0:.3f} '
          f'IC90({np.quantile(rs,.05):.3f},{np.quantile(rs,.95):.3f}) n_eff/dia {ne0/ndias:.1f} IC90({np.quantile(ns,.05):.1f},{np.quantile(ns,.95):.1f}) DEFF {n/ne0:.2f}')

print('\n## 1. n efectivo')
F = BASE + 'contabilidad_wallet_dedicada/posiciones.csv'
R = [r for r in csv.DictReader(open(F)) if r['experimento'] == 'H47-B' and r['estado'].startswith('liquidada')]
co = sum(float(r['coste']) for r in R); pn = sum(float(r['pnl_realizado']) for r in R)
print(f'B real liquidadas {len(R)} coste {co:.2f} pnl {pn:+.2f} EVpond {pn/co:+.4f}')
cl = collections.defaultdict(list); byd = collections.defaultdict(lambda: [0.0, 0.0])
for r in R:
    cl[r['fin_mercado_utc']].append(1.0 if float(r['pnl_realizado']) > 0 else 0.0)
    byd[r['fin_mercado_utc'][:10]][0] += float(r['pnl_realizado']); byd[r['fin_mercado_utc'][:10]][1] += float(r['coste'])
print('B EV por dia', {d: round(a / b, 3) for d, (a, b) in sorted(byd.items())})
EV_B = pn / co
cp = collections.defaultdict(lambda: [0.0, 0.0])
for r in R: cp[r['fin_mercado_utc']][0] += float(r['pnl_realizado']); cp[r['fin_mercado_utc']][1] += float(r['coste'])
A = np.array([v[0] for v in cp.values()]); Bc = np.array([v[1] for v in cp.values()]); ii = rng.integers(0, len(A), (4000, len(A)))
e = A[ii].sum(1) / Bc[ii].sum(1); print(f'B EV IC90 por cierre ({np.quantile(e,.05):+.3f},{np.quantile(e,.95):+.3f})')
G = [np.array(v) for v in cl.values()]
rep(G, 2.15, 'B real 20-Oct 11:40Z..22-Oct 15:45Z (~2,15 dias calendario, ~7 h activas/dia)')
for d in ('2026-10-21', '2026-10-22'):
    g = [np.array(v) for k, v in cl.items() if k.startswith(d)]
    print(f'  {d} completo: rellenos {sum(len(x) for x in g)} cierres {len(g)} n_eff(ICC .261) {neff(g,.261):.1f} (ICC .04 {neff(g,.04):.1f}; .45 {neff(g,.45):.1f}; 1 = {len(g)})')
Bq = pd.read_csv(BASE + 'b_perdidas_22oct/r3_escalado/datos/b_real_r3.csv')
Bq['fin'] = Bq.mercado.str.split('-').str[-1].astype(int) + 300
for lab, s in (('B real con print', Bq), ('B real R3 verdadero', Bq[Bq.r3 == 1])):
    print(f'{lab}: rellenos {len(s)} cierres {s.fin.nunique()} por dia {s.groupby("dia").size().to_dict()} cierres/dia {s.groupby("dia").fin.nunique().to_dict()} EV {s.pnl.sum()/s.coste.sum():+.3f}')
X = pd.concat([pd.read_csv(f) for f in sorted(glob.glob(BASE + 'b_perdidas_22oct/r3_escalado/datos/esc_2026-10-*.csv.gz'))], ignore_index=True)
X = X[X.dia < '2026-10-22']
for pol in ('BASE', 'R3'):
    s = X[X[f'{pol}_fill'] == 1]
    rep([g.gana.values.astype(float) for _, g in s.groupby(['dia', 'fin'])], 5, f'simulador {pol} 17-21 (capacidad, 1 puja por mercado-lado)')
    # sobredispersion entre dias (efecto direccion del dia)
    c = s.assign(coste=5 * s[f'{pol}_obj'], pnl=5 * (s.gana - s[f'{pol}_obj'])).groupby(['dia', 'fin'])[['pnl', 'coste']].sum().reset_index()
    ev_d, vw = [], []
    for d, gd in c.groupby('dia'):
        a, b = gd.pnl.values, gd.coste.values; ev_d.append(a.sum() / b.sum())
        i = rng.integers(0, len(a), (3000, len(a))); vw.append(np.var(a[i].sum(1) / b[i].sum(1)))
    print(f'  EV diario {np.round(ev_d,3).tolist()} var entre dias / var esperada iid por cierre = {np.var(ev_d,ddof=1)/np.mean(vw):.2f} (5 dias: estimacion debil)')

print('\n## 2. Escalado por escenario (Kelly correcto; s_min 1,05 $; techo de profundidad K=20 -> coste medio 2,44 $/relleno, EV -0,017; R3_escalado §4.1)')
S_CAP = 317 / 130; DET = 0.017
def g_exacto(f, ev, b=SIG2):   # log-crecimiento por relleno binario (ignora la correlacion: favorable al apostador)
    q = P_MED * (1 + ev); return q * math.log(1 + f * b) + (1 - q) * math.log(1 - f)
ESC = [  # nombre, EV, rellenos/dia capturados, DEFF
    ('B actual pesimista (sim BASE)', -0.18, 73, 1.27),
    ('B actual base (real, fresco)', EV_B, 73, 1.27),
    ('B actual base +rebate (si se paga)', EV_B + 0.011, 73, 1.27),
    ('B actual optimista (=gate)', 0.05, 73, 1.27),
    ('B 24 h optimista (=gate, cap. sim)', 0.05, 560, 1.58),
    ('R3 pesimista (politica sim)', -0.041, 26, 1.20),
    ('R3 base retencion (+0,03)', 0.03, 50, 1.25),
    ('R3 base recalibrado (+0,07)', 0.07, 50, 1.25),
    ('R3 base recal. cap. completa', 0.07, 130, 1.32),
    ('R3 optimista (+0,11) cap. completa', 0.11, 130, 1.32),
    ('R3 cota alta IC (+0,35) cap. compl.', 0.35, 130, 1.32),
]
print('esc | EV | rell/dia | n_eff/dia | f*Kelly/relleno | W_min Kelly / 1/2K $ | g(5$, f=21%) | g Kelly %/d | g 1/2K %/d | dias W_min->techo K20 (K/half) | '
      'dias 5$->techo sin minimo (K/half) | EUR/anio en techo K20 | stake 200k $/relleno (acc) | cabe K20?')
for nom, ev, n, deff in ESC:
    ne = n / deff
    if ev <= 0:
        print(f'{nom} | {ev:+.3f} | {n} | {ne:.0f} | 0 | inf | {g_exacto(S_MIN/5, ev):+.3f} | 0 | 0 | nunca | nunca | 0 | — | —'); continue
    f = ev / (SIG2 * deff); wK = S_MIN / f; wH = 2 * wK
    gK = ne * ev ** 2 / (2 * SIG2); gH = 0.75 * gK
    dK = math.log(S_CAP / S_MIN) / gK; dH = math.log(S_CAP / S_MIN) / gH
    wcap = S_CAP / f; d5K = math.log(wcap / 5) / gK; d5H = math.log(2 * wcap / 5) / gH
    anual = n * S_CAP * max(ev - DET, 0) * 365
    s200 = 200000 / ((ev - DET) * 365 * n) if ev > DET else float('inf')
    print(f'{nom} | {ev:+.3f} | {n} | {ne:.0f} | {100*f:.2f} % | {wK:.0f} / {wH:.0f} | {g_exacto(S_MIN/5, ev):+.3f} | {100*gK:.2f} | {100*gH:.2f} | '
          f'{dK:.0f} / {dH:.0f} | {d5K:.0f} / {d5H:.0f} | {anual:,.0f} | {s200:.0f} ({s200/0.21:.0f}) | {"si" if s200 <= S_CAP else "NO x%.0f" % (s200/S_CAP)}')

print('\n## 3. Que haria falta (techo K=20, 2,44 $/relleno, deterioro 0,017)')
for ev in (0.05, 0.07, 0.11, 0.20, 0.35):
    n200 = 200000 / (365 * S_CAP * (ev - DET)); n20 = 20000 / (365 * S_CAP * (ev - DET))
    print(f'EV {ev:+.2f}: rellenos/dia para 200 k = {n200:,.0f} (x{n200/130:.0f} la capacidad R3 de 3 alts; ~{n200/43.5:.0f} moneda-marco a 43,5 R3/dia) ; para 20 k (10 %) = {n20:,.0f} (x{n20/130:.1f})')
print('EV necesario para que R3 a capacidad completa (130/dia, K20) de 20 k: %.3f ; 50 k: %.3f ; 200 k: %.3f' % tuple(DET + x / (365 * S_CAP * 130) for x in (20000, 50000, 200000)))

print('\n## 4. Correccion del PLAN_MAESTRO ADENDA 20-Oct (sigma2 4,2; dias desde 2 EUR hasta stake final)')
for n, ev in ((2.8, .08), (2.8, .04), (10, .08), (20, .08), (50, .08), (50, .04)):
    sf = 200000 / (ev * 365 * n); L = math.log(sf / 2)
    gp = n * ev ** 2 / 4.2; gK = gp / 2; gH = 0.375 * n * ev ** 2 / 4.2
    print(f'n {n} EV {ev}: stake {sf:.0f} | plan Kelly {L/gp:.0f} d (g {100*gp:.2f}%) | correcto Kelly {L/gK:.0f} d (g {100*gK:.2f}%) | correcto 1/2K {L/gH:.0f} d')
