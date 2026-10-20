#!/usr/bin/env python3
"""h23_analisis.py -- agrega el replay H23 (h23_D.csv) por brazo/variante/cola/latencia. EV PONDERADO por € (Σpnl/Σcoste) + por unidad, IC90 por DIAS
(bootstrap de dias), sin los 2 mejores dias, cobertura, capacidad, estudio del desplome (exploratorio) y falso disparo del kill de brazo.
Uso: python3 -I h23_analisis.py [dir_cache] > salida.txt   (solo lectura)"""
import glob, os, sys, json
import numpy as np, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import h23_regla as R
O = sys.argv[1] if len(sys.argv) > 1 else '/mnt/HC_Volume_106538179/datalogs_analisis_caches/h23_maker/'
fs = sorted(f for f in glob.glob(O + 'h23_20*.csv') if os.path.getsize(f) > 0)
M = pd.concat([pd.read_csv(f) for f in fs], ignore_index=True)
cob = [json.load(open(f)) for f in sorted(glob.glob(O + 'h23_cobertura_*.json'))]
print('DIAS', sorted(M.dia.unique()), '| cobertura por dia (cierres_grupo/con_lado/con_libro/errores):',
      [(c['dia'][5:], c['cierres_grupo'], c['con_lado'], c['con_libro'], c['errores']) for c in cob])
M['gana_f'] = M.gana.astype(float)                      # NaN si sin desenlace (missing, no 0)
sin_des = M[M.gana.isna() & (M.lleno > 0)].cierre.nunique()
print('rellenos sin desenlace oficial (missing):', sin_des)
M['pnl'] = M.lleno * M.gana_f - M.coste + M.rebate
rng = np.random.default_rng(7)

def ev_dias(g):
    """g: filas con relleno. EV pond (Σpnl/Σcoste), por unidad, IC90 por dias (bootstrap de dias), sin 2 mejores dias."""
    if not len(g): return dict(n=0)
    pd_ = g.groupby('dia').agg(p=('pnl', 'sum'), c=('coste', 'sum'))
    ev = g.pnl.sum() / g.coste.sum()
    unit = (g.pnl / g.coste).mean()
    boots = []
    D = pd_.values
    for _ in range(3000):
        k = D[rng.integers(0, len(D), len(D))]
        boots.append(k[:, 0].sum() / k[:, 1].sum() if k[:, 1].sum() > 0 else np.nan)
    lo, hi = np.nanpercentile(boots, [5, 95])
    s2 = pd_.sort_values('p', ascending=False).iloc[2:]
    ev2 = s2.p.sum() / s2.c.sum() if len(s2) and s2.c.sum() > 0 else float('nan')
    acc = g.gana_f.mean(); precio = g.coste.sum() / g.lleno.sum()
    return dict(n=len(g), dias=g.dia.nunique(), pnl=g.pnl.sum(), coste=g.coste.sum(), ev_pond=ev, ev_unit=unit, ic90=(lo, hi), sin2=ev2,
                acierto=acc, precio=precio, dias_pos=int((pd_.p > 0).sum()))

def fmt(d):
    if d['n'] == 0: return 'n=0'
    return ('n=%d dias=%d (+%d) PnL=%+.2f coste=%.2f EV_pond=%+.3f EV_unit=%+.3f IC90dias=(%+.2f,%+.2f) sin2mejoresDias=%+.3f acierto=%.3f vs precio=%.3f'
            % (d['n'], d['dias'], d['dias_pos'], d['pnl'], d['coste'], d['ev_pond'], d['ev_unit'], d['ic90'][0], d['ic90'][1], d['sin2'], d['acierto'], d['precio']))

ndias = M.dia.nunique()
print('\n===== TABLA PRINCIPAL (BTC, 1 posicion por cierre y variante, rebate 20 %, reloj RECEPCION). cola base = central; rango [opt, cons] =====')
res = {}
for (brazo, var, cola, lp, lc), g in M.groupby(['brazo', 'var', 'cola', 'lat_post', 'lat_cancel']):
    q = g[g.n_cotiz > 0]; f = g[(g.lleno > 0) & g.gana.notna()]
    d = ev_dias(f); res[(brazo, var, cola, lp, lc)] = (d, len(q), len(f))
    print(f'{brazo} {var:4s} cola={cola:4s} alta={lp:3d} cancel={lc:3d} | cotizados {len(q)} rellenos {len(f)} ({100*len(f)/max(len(q),1):.0f} %) | {fmt(d)}')

print('\n===== CAPACIDAD (central: base, alta 79, cancel 60) =====')
for brazo in ('A', 'B'):
    f = M[(M.brazo == brazo) & (M['var'] == 'join') & (M.cola == 'base') & (M.lat_post == 79) & (M.lat_cancel == 60) & (M.lleno > 0)]
    print(f'{brazo}: rellenos/dia {len(f)/ndias:.2f} | coste/dia {f.coste.sum()/ndias:.2f} € | PnL/dia {f.pnl.sum()/ndias:+.2f} € ({ndias} dias del replay)')

print('\n===== DESPLOME (EXPLORATORIO, post hoc: NO cambia la regla). Primario A join base alta79 cancel60 =====')
f = M[(M.brazo == 'A') & (M['var'] == 'join') & (M.cola == 'base') & (M.lat_post == 79) & (M.lat_cancel == 60) & (M.lleno > 0) & M.gana.notna()].copy()
f['caida_pre'] = f.bid5_max_1s_pre - f.bid5_rel            # el bid del 5m ya venia cayendo en el 1 s previo al relleno (causal)
f['mk5'] = f.bid5_p5 - f.p_rel                             # markout a +5 s (hindsight; solo describe)
f['b15_baja'] = f.bid15_m1s - f.bid15_rel                   # la cota bajo en el 1 s previo (causal)
for nombre, mask in [('bid5 caia >=2c en 1 s previo', f.caida_pre >= 0.02 - 1e-9), ('bid5 NO caia', f.caida_pre < 0.02 - 1e-9),
                     ('bid15 bajo >=1c en 1 s previo', f.b15_baja >= 0.01 - 1e-9), ('bid15 NO bajo', f.b15_baja < 0.01 - 1e-9),
                     ('markout +5 s <= -2c (hindsight)', f.mk5 <= -0.02 + 1e-9), ('markout +5 s > -2c o missing', ~(f.mk5 <= -0.02 + 1e-9))]:
    print(f'  {nombre:36s} {fmt(ev_dias(f[mask]))}')

print('\n===== CONTROL: cancelar vs NO cancelar (A, base, alta 79) =====')
for var in ('join', 'nc'):
    d, nq, nf = res.get(('A', var, 'base', 79, 60), (dict(n=0), 0, 0)); print(f'  {var:4s} cotizados {nq} rellenos {nf} | {fmt(d)}')

print('\n===== FALSO DISPARO del kill de brazo (n>=%d rellenos y EV_pond sin 2 mejores dias < %.2f), bootstrap secuencial 60 rellenos, 2000 sim =====' % (
    R.CONFIG['kill_brazo']['n_rellenos'], R.CONFIG['kill_brazo']['ev_pond_sin2mejores_max']))
def sim_kill(g, nulo):
    """g: rellenos del brazo (pnl, coste, dia). nulo=True: reasigna acierto ~ Bernoulli(precio) (EV≈rebate: sin edge)."""
    P, C, Dd = g.pnl.values.copy(), g.coste.values, g.dia.values
    if nulo:
        pr = (g.coste / g.lleno).values
        P = g.lleno.values * (rng.random(len(g)) < pr) - C + g.rebate.values
    return P, C, Dd
for brazo in ('A', 'B'):
    f = M[(M.brazo == brazo) & (M['var'] == 'join') & (M.cola == 'base') & (M.lat_post == 79) & (M.lat_cancel == 60) & (M.lleno > 0) & M.gana.notna()]
    if len(f) < 8: print(f'  {brazo}: n={len(f)} insuficiente'); continue
    for etiqueta, nulo in (('con el edge observado (remuestreo)', False), ('sin edge (acierto=precio)', True)):
        dis = 0
        for _ in range(2000):
            idx = rng.integers(0, len(f), 60); g = f.iloc[idx]
            P, C, Dd = sim_kill(g, nulo)
            dd = rng.integers(0, 13, 60); dd.sort()          # reparte los 60 rellenos en ~13 dias ficticios
            hit = False
            for n in range(R.CONFIG['kill_brazo']['n_rellenos'], 61):
                df = pd.DataFrame(dict(p=P[:n], c=C[:n], d=dd[:n])).groupby('d').sum().sort_values('p', ascending=False).iloc[2:]
                if len(df) and df.c.sum() > 0 and df.p.sum() / df.c.sum() < R.CONFIG['kill_brazo']['ev_pond_sin2mejores_max']: hit = True; break
            dis += hit
        print(f'  {brazo} {etiqueta:38s}: kill dispara en {100*dis/2000:.1f} % de las secuencias de 60 rellenos')
