import sys, json, os, numpy as np, pandas as pd
sys.path.insert(0,'/root/polymarket-research/experimentos/5m_barato/db1'); sys.path.insert(0,'/root/polymarket-research/experimentos/5m_barato/q11')
import eval_db1 as E, eval_thru1 as E1, passdb as P
Q = E.QUEMADOS; R = E.cargar(Q); g0 = E.nr(E.V(R,'G0'))
nseeds = int(sys.argv[1]) if len(sys.argv)>1 else 99
out = {}
for arm in ('DB1','DB2'):
    c = E.ARMS[arm]; d_obs = float(E1.dser(E.nr(E.V(R,c['v'])), g0).sum()); n_obs = len(E.V(R,c['v'])); perm=[]; ns=[]; falt=[]; missing=[]
    for s in range(1, nseeds+1):
        faltan = [d for d in Q if not os.path.exists(P.HERE+f'placebo/s{s}/out/RX_{d}.pkl')]
        if faltan: missing.append((s,faltan)); continue
        Pp = E.cargar(Q, E.PLA+f's{s}/out/', d_ex=E.OUT); x = E.nr(E.V(Pp, c['pla']))
        perm.append(float(E1.dser(x, g0).sum())); ns.append(len(x))
        if arm=='DB2': falt.append(sum(json.load(open(E.PLA+f's{s}/out/cov_{d}.json'))['fills_no_emparejables'] for d in Q))
    perm=np.array(perm); m,p = E.pvalor(d_obs, perm) if len(perm) else (float('nan'),float('nan'))
    o = dict(arm=arm, n_semillas_completas=len(perm), semillas_incompletas=len(missing), d_obs=d_obs, n_real=n_obs, nulo_media=m, nulo_sd=float(perm.std(ddof=1)) if len(perm)>1 else None, nulo_min=float(perm.min()), nulo_max=float(perm.max()),
             nulo_pcts={q: float(np.percentile(perm,q)) for q in (5,25,50,75,95)}, n_por_semilla=dict(min=min(ns), media=float(np.mean(ns)), max=max(ns)), cobertura_vs_real=float(np.mean(ns)/n_obs), nan_en_perm=int(np.isnan(perm).sum()),
             semillas_distintas=len(set(np.round(perm,6))), p_formal=p)
    if arm=='DB2': o['fills_no_emparejables_por_semilla_(misses de prints_placebo)']=dict(min=min(falt), media=float(np.mean(falt)), max=max(falt))
    out[arm]=o
json.dump(out, open(sys.argv[2] if len(sys.argv)>2 else '/dev/stdout','w'), indent=1, default=float) if len(sys.argv)>2 else print(json.dumps(out, indent=1, default=float))
