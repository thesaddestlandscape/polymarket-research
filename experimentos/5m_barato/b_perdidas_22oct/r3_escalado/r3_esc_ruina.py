#!/usr/bin/env python3
"""r3_esc_ruina.py -- (1) capacidad de R3 en la POBLACION (b_seleccion_adversa/datos/ms_units.pkl, primeras 5 acc de otros makers, 17-21 Oct) por moneda x hora;
(2) techo anual por tamano K con escenarios de EV; (3) riesgo de ruina / capital por peldano (Monte Carlo con correlacion por cierre).
Solo lectura. Salida: datos/r3_esc_ruina.txt."""
import os, glob, json
import numpy as np, pandas as pd
AQUI = os.path.dirname(os.path.abspath(__file__)); DD = os.path.join(AQUI, 'datos')
POB = os.path.join(AQUI, '..', '..', 'b_seleccion_adversa', 'datos', 'ms_units.pkl')
out = []
def P(*a):
    t = ' '.join(str(x) for x in a); print(t); out.append(t)
# ---------- (1) poblacion
U = pd.read_pickle(POB); U = U[U.has5].copy()
A = (U.lvl15 <= 0.03) & (U.vol30ws >= 26) & (U.hora >= 4); U['r3'] = A.values
nd = U.dia.nunique()
P('## (1) Poblacion (otros makers, primeras 5 acc por maker-mercado-lado), ETH/SOL/XRP 5m banda 0,10-0,30, 17-21 Oct (21 parcial)')
R = U[U.r3]
P(f'R3: unidades/dia {len(R)/nd:.0f}; EUR/dia {R.c.sum()/nd:.0f}; mercados-lado distintos/dia {R.groupby(["dia","mkt","lado_c"]).ngroups/nd:.0f}; '
  f'cierres distintos/dia {R.groupby(["dia","fin"]).ngroups/nd:.0f}; makers distintos/dia {R.groupby(["dia","maker"]).ngroups/nd:.0f}')
P(f'Todo (sin regla): unidades/dia {len(U)/nd:.0f}; EUR/dia {U.c.sum()/nd:.0f}; mercados-lado/dia {U.groupby(["dia","mkt","lado_c"]).ngroups/nd:.0f}')
t = R.groupby('act').agg(u=('c', 'size'), eur=('c', 'sum'), pnl=('p', 'sum')); t['u'] /= nd; t['eur'] /= nd; t['ev'] = t.pnl / (t.eur * nd); P(t[['u', 'eur', 'ev']].round(3).to_string())
h = R.groupby(pd.cut(R.hora, [3.5, 8, 12, 16, 20, 24])).agg(u=('c', 'size'), eur=('c', 'sum'), pnl=('p', 'sum'))
h['ev'] = h.pnl / h.eur; h['u'] /= nd; h['eur'] /= nd; P(h[['u', 'eur', 'ev']].round(3).to_string())
# ---------- (2) techo anual
X = pd.concat([pd.read_csv(f) for f in sorted(glob.glob(os.path.join(DD, 'esc_2026-10-*.csv.gz')))], ignore_index=True)
full = X[X.dia != '2026-10-22']; nf = full.dia.nunique(); s = full[full.R3_fill == 1]
P('\n## (2) Techo anual de la politica R3 (1 puja por mercado, ETH/SOL/XRP, sin tope de vivas; simulador E1 dias completos 17-21)')
P(f'rellenos R3/dia {len(s)/nf:.0f}; cierres con relleno R3/dia {s.groupby(["dia","fin"]).ngroups/nf:.0f}')
base_cost = {}
for K in (5, 10, 20, 50):
    q = np.full(len(s), 5.0) if K == 5 else np.minimum(K, s.R3_V1)
    q = np.maximum(q, np.where(K == 5, 5.0, 0)) if K == 5 else np.maximum(q, 5.0)   # B rellena >= sus 5 primeras (cola al precio): suelo de 5
    base_cost[K] = float((q * s.R3_obj).sum() / nf)
dEV = {5: 0.0, 10: -0.010, 20: -0.017, 50: -0.066}   # deterioro de EV con K medido en el simulador (r3_esc_an.txt, V1)
P('K  EUR/dia  | anual EV cons 0 | base +0,03 | optimista +0,11 (todo con el deterioro por K del simulador; rebate +0,011 aparte)')
TA = {}
for K, c in base_cost.items():
    row = {nm: c * max(e + dEV[K], 0 if nm != 'cons' else 0) * 365 for nm, e in (('cons', 0.0), ('base', 0.03), ('opt', 0.11))}
    row['rebate'] = c * 0.011 * 365; TA[K] = dict(eur_dia=c, **row)
    P(f'{K:2d} {c:7.1f} | {row["cons"]:8.0f} | {row["base"]:8.0f} | {row["opt"]:8.0f} | rebate {row["rebate"]:6.0f}')
# ---------- (3) ruina / capital
P('\n## (3) Riesgo de ruina y capital por peldano (Monte Carlo 20.000 trayectorias)')
cl = s.groupby(['dia', 'fin']).size().values          # tamanos de racimo (rellenos R3 por cierre) empiricos
P(f'racimo por cierre: media {cl.mean():.2f}, P(>=2) {(cl >= 2).mean():.2f}, max {cl.max()}')
p = 0.21; rho = 0.333                                 # precio medio; rho calibrado a la concordancia 0,774 de B real (tandas/INFORME.md)
def sim(K, e, N, caps, nsim=20000, seed=1):
    r = np.random.default_rng(seed); q = p * (1 + e)
    pnl = np.zeros(nsim); peak = np.zeros(nsim); mdd = np.zeros(nsim); done = 0
    while done < N:
        m = r.choice(cl, nsim)                        # rellenos de este cierre
        com = r.random(nsim) < q                      # resultado comun del cierre
        g = np.zeros(nsim)
        for j in range(m.max()):
            act = m > j; own = r.random(nsim) < q; usec = r.random(nsim) < np.sqrt(rho)
            w = np.where(usec, com, own); g += act * K * (np.where(w, 1 - p, -p))
        pnl += g; peak = np.maximum(peak, pnl); mdd = np.maximum(mdd, peak - pnl); done += m.mean()
    return {C: float((mdd >= C).mean()) for C in caps}, float(np.quantile(mdd, .9)), float(np.quantile(mdd, .95)), float(pnl.mean()), float(pnl.std())
RU = {}
for K, N in ((5, 300), (5, 1000), (10, 500), (25, 1000), (50, 1000)):
    for e in (-0.05, 0.0, 0.05, 0.10):
        caps = (5.12, 10, 20, 50, 100, 200, 400)
        pr, q90, q95, mu, sd = sim(K, e, N, caps)
        RU[f'K{K}_N{N}_e{e}'] = dict(p_dd=pr, q90=q90, q95=q95, mu=mu, sd=sd)
        P(f'K={K:2d} N={N:4d} e={e:+.2f}: P(DD>=5,12$) {pr[5.12]:.2f} P(DD>=20$) {pr[20]:.2f} P(DD>=50$) {pr[50]:.2f} P(DD>=100$) {pr[100]:.2f} | DD P90 {q90:6.1f} P95 {q95:6.1f} $ | PnL medio {mu:+7.1f} sd {sd:6.1f}')
# potencia: con N rellenos, P(EV observado con IC90 > 0) si EV real e
P('\nPotencia (aprox. normal, efecto racimo incluido): N para que el IC90 del EV excluya 0 con prob. 0,8 si EV real = e')
sig = np.sqrt(p * (1 - p)) / p; deff = 1 + (cl.mean() - 1) * rho
for e in (0.03, 0.05, 0.10, 0.15):
    n = ((1.645 + 0.84) * sig / e) ** 2 * deff; P(f'  e={e:+.2f}: N ~ {n:,.0f} rellenos (~{n/ (len(s)/nf):.0f} dias a la capacidad R3 completa; ~{n/37:.0f} dias al ritmo de B real ~37/dia)')
json.dump(dict(techo=TA, ruina=RU), open(os.path.join(DD, 'r3_esc_ruina.json'), 'w'), indent=1)
open(os.path.join(DD, 'r3_esc_ruina.txt'), 'w').write('\n'.join(out) + '\n')
