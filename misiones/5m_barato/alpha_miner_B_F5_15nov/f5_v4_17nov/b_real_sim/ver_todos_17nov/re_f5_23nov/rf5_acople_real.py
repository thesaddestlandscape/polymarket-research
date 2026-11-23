#!/usr/bin/env python3
"""rf5_acople_real.py DIA [N_MERCADOS] -- ESPEC E4 (a)+(b) sobre un dia NO CIEGO (<=17-Nov): (a) replay de un mercado AISLADO == dentro del dia (b_policy_sim acopla mercados por MAXV/busy?); (b) la composicion de replicas base/VETO_UP/VETO_DN
reproduce la replica directa de F3 (y F1,F2,U13)? Ademas cronometra una replica y una permutacion de la familia K (K1..K4 con series Binance desplazadas). SOLO CONTEOS e igualdades: no imprime PnL/EV. Escribe out_rf5_ciego/acople_real_DIA.json.
Se niega a correr un dia >= 18-Nov (ciego)."""
import sys, os, json, time
HV = os.path.dirname(os.path.abspath(__file__)) + '/'
d = sys.argv[1]; NM = int(sys.argv[2]) if len(sys.argv) > 2 else 30
if d >= '2026-11-18': raise SystemExit('dia ciego: prohibido')
os.environ.setdefault('RF5_OUT', HV + 'out_rf5_ciego/')
sys.path.insert(0, HV)
import numpy as np, pandas as pd
import rf5_run as RR, rf5_core as K5, rf5_nulo as NU
import b_policy_sim as BS, eng_v5 as EV, sec7_core as C
cortes = K5.lee_cortes(); E, info = EV.build(d); P = BS.params(); res = dict(dia=d, motor=info if isinstance(info, dict) else str(info)); t = {}
def replica(nombre, E_=None, veto=None):
    W = C.EngineBloqueo(E_ or E, activo=False); ctx = dict(W=W, serie=W._serie); t0 = time.time(); R, cov, HK = RR._replay(d, P, W, ctx, nombre, K5.POLITICAS_A, None, cortes, None, veto); t[nombre] = round(time.time() - t0, 1); return R, HK
with RR.desenlace_con_marcador() as unres:
    out = {}; f5 = []
    for n in ('base', 'F1', 'F2', 'F3', 'U13', 'VETO_UP', 'VETO_DN'):
        R, HK = replica(n); out[n] = RR._col(R, 0, unres) if len(R) else R; f5.append(RR.construye_f5tab(HK.f5_0, d, 0, n))
    RA = pd.concat([v for v in out.values() if len(v)], ignore_index=True); F = pd.concat(f5, ignore_index=True)
    comp = NU.verifica_composicion(RA, F, cortes); res['composicion_vs_replica_directa'] = comp
    # (a) aislado vs dentro del dia
    base = out['base']; mids = sorted(base.mid.astype(str).unique()); rng = np.random.default_rng(20261124); sel = list(rng.choice(mids, size=min(NM, len(mids)), replace=False)); igual = 0; dif = []
    ks_all = list(E.ks)
    def unidades(R): 
        X = R[R.q > 0]; return {(str(m), int(k)): (round(float(p), 12), round(float(c), 12)) for m, k, p, c in zip(X.mid, X.k, X.pnl, X.cost)}
    ub = unidades(base); ordenes_b = {(str(m), int(n)): (int(td), round(float(L), 4), float(q)) for m, n, td, L, q in zip(base.mid, base.n_ord, base.t_dec, base.L, base.q)}
    for mid in sel:
        E.ks = [k for k in ks_all if str(E.D.mid[k]) == mid]
        try: Ri, _ = replica('base')
        finally: E.ks = ks_all
        oi = {(str(m), int(n)): (int(td), round(float(L), 4), float(q)) for m, n, td, L, q in zip(Ri.mid, Ri.n_ord, Ri.t_dec, Ri.L, Ri.q)} if len(Ri) else {}
        ob = {k: v for k, v in ordenes_b.items() if k[0] == mid}
        (igual := igual + 1) if oi == ob else dif.append(mid)
    res['aislado_vs_dia'] = dict(mercados_probados=len(sel), identicos=igual, distintos=len(dif), mids_distintos=dif[:10], criterio='mismas ordenes (t_dec, L, q) por mercado')
res['segundos_replica'] = t; res['unres'] = len(unres)
# una permutacion de la familia K: series Binance desplazadas, K1..K4 (bloq 0), tiempos
import calendar
bsrc = RR.FB.carga_binance(d)
if bsrc:
    d0 = calendar.timegm(time.strptime(d, '%Y-%m-%d')) * 1000; bsh = {c_: NU.desplaza_circular(tt, pp, d0, NU.delta_perm(d, 1)) for c_, (tt, pp) in bsrc.items()}; tk = {}
    W = C.EngineBloqueo(E, activo=False); ctx = dict(W=W, serie=W._serie)
    for n in ('K1', 'K2', 'K3', 'K4'):
        t0 = time.time(); R, cov, HK = RR._replay(d, P, W, ctx, n, K5.POLITICAS_K, bsh, cortes, 1.0, None); tk[n] = round(time.time() - t0, 1)
    res['segundos_permutacion_K_1dia_K1a4'] = tk; res['segundos_permutacion_total'] = round(sum(tk.values()), 1)
json.dump(res, open(HV + f'out_rf5_ciego/acople_real_{d}.json', 'w'), indent=1, default=str); print(json.dumps(res, default=str)[:2500])
