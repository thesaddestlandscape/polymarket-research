#!/usr/bin/env python3
"""f3_evento_vacio.py (FN_132, 16-Nov) -- SOLO LECTURA, 0 ordenes. Estudio de eventos que SEPARA H1a (artefacto de validacion: los tomadores que nos golpean
habrian golpeado igual el nuevo mejor bid -> en forward el simulador los ve como barrido por debajo de L) de H1b (nuestra orden ATRAE el golpe: cotizacion rancia
cazada; sin nosotros no habria print -> ceguera real del simulador).
EVENTO: en un token 5m ETH/SOL/XRP el mejor bid BAJA de precio (v0[j] < v0[j-1]) a un nuevo mejor bid P' en [0,10; 0,29], con T=fin-t en [5; 295] s.
RESULTADO: dt = primer golpe vendedor al nuevo tope (print WS tsd=0 en el token a <= P' o tsd=1 en el complementario con 1-p <= P') tras el evento; P(dt <= W).
BRAZO B: hay una orden REAL de B viva en ese token exactamente a L = P' (t_ini <= t_j <= t_fuera, y aun no rellenada: t_j < primer print propio).
BRAZO B_debajo (CONTROL de seleccion de momento): B tiene orden viva no rellenada en el token por DEBAJO del nuevo tope (L < P') en [t_j-0,2 s, t_j+1 s]: mismos momentos elegidos por B, pero B no es el tope.
BRAZO noB: ninguna orden de B viva en el token ni en su complementario en [t_j-3 s, t_j+1 s] (libro y cinta LIMPIOS de nosotros).
Mismo reloj para eventos y prints (sa_ms; ms_<D>.npz via capt.Day, lectura del worktree dev SIN editar). Cluster = mercado (dia, mid).
Salida: eventos_<D>.pkl y f3_resumen.json."""
import os, sys, json, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'
sys.path.insert(0, '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/capturabilidad_A_R1ws'); import capt
DL = '/root/polymarket-research-datalogs/'
WS = (50, 100, 200, 500, 1000, 3000)
O = pd.read_csv(DL + 'calibracion_etiqueta/ordenes_b.csv', dtype={'tok': str}, usecols=['oid', 'tok', 'dia', 'precio', 't_ini', 't_fuera'])
INV = pd.read_pickle(H + 'inventario2.pkl')[['oid', 'tm3', 'cls', 'estructura']]
O = O.merge(INV, on='oid', how='left')
def corre(d):
    f = H + f'eventos_{d}.pkl'
    if os.path.exists(f): return pd.read_pickle(f)
    D = capt.Day(d); Od = O[O.dia == d]
    rows = []
    for k in range(len(D.toks)):
        if D.marco[k] != '5min' or D.act[k] not in ('ETH', 'SOL', 'XRP'): continue
        a, b = D.qb[k], D.qb[k + 1]
        if b - a < 2: continue
        qt = D.qt[a:b].astype(np.int64); v0 = D.v0[a:b].astype(float); v2 = D.v2[a:b].astype(float)
        j = np.where((v0[1:] < v0[:-1] - 0.005) & (v0[1:] >= 0.095) & (v0[1:] <= 0.295))[0] + 1
        if not len(j): continue
        T = D.fin[k] - qt[j] / 1000.0; ok = (T >= 5) & (T <= 295); j = j[ok]; T = T[ok]
        if not len(j): continue
        # golpes vendedores al bid de k (precio YES-equivalente)
        ht, hp = [], []
        aa, bb = D.tb[k], D.tb[k + 1]; m = D.tsd[aa:bb] == 0; ht.append(D.tt[aa:bb][m]); hp.append(D.tp[aa:bb][m].astype(float))
        kc = D.comp(k)
        if kc is not None:
            aa, bb = D.tb[kc], D.tb[kc + 1]; m = D.tsd[aa:bb] == 1; ht.append(D.tt[aa:bb][m]); hp.append(1 - D.tp[aa:bb][m].astype(float))
        ht = np.concatenate(ht).astype(np.int64); hp = np.concatenate(hp); o = np.argsort(ht, kind='stable'); ht = ht[o]; hp = hp[o]
        tok = D.toks[k]; tokc = D.toks[kc] if kc is not None else None
        Ok = Od[Od.tok == str(tok)]; Oc = Od[Od.tok == str(tokc)] if tokc is not None else Od.iloc[0:0]
        Oall = pd.concat([Ok, Oc]); oi = (Oall.t_ini.values * 1000).astype(np.int64); of = (Oall.t_fuera.values * 1000).astype(np.int64)
        for jj, TT in zip(j, T):
            t = int(qt[jj]); P = float(v0[jj])
            i0 = np.searchsorted(ht, t, side='right'); cand = np.where(hp[i0:i0 + 400] <= P + 0.0049)[0]
            dt = float(ht[i0 + cand[0]] - t) if len(cand) else np.inf
            liveB = Ok[(np.abs(Ok.precio - P) < 0.005) & (Ok.t_ini * 1000 <= t) & (Ok.t_fuera * 1000 >= t) & ~(Ok.tm3 <= t)]
            near = bool(((oi <= t + 1000) & (of >= t - 3000)).any())
            debB = Ok[(Ok.precio < P - 0.005) & (Ok.t_ini * 1000 <= t - 200) & (Ok.t_fuera * 1000 >= t + 1000) & ~(Ok.tm3 <= t + 1000)]
            brazo = 'B' if len(liveB) else ('B_debajo' if len(debB) else ('noB' if not near else 'mixto'))
            r = dict(dia=d, mid=D.mid[k], coin=D.act[k], k=k, t=t, T=float(TT), P=P, drop=float(v0[jj - 1] - P), sz=float(v2[jj]), dt=dt, brazo=brazo)
            if len(liveB):
                o1 = liveB.iloc[0]; r.update(oid=o1.oid, cls=o1.cls, estructura=o1.estructura, dt_fill_propio=(float(o1.tm3 - t) if np.isfinite(o1.tm3) else np.inf))
            rows.append(r)
    E = pd.DataFrame(rows); E.to_pickle(f); del D; return E
dias = sys.argv[1:] or ['2026-10-20', '2026-10-21', '2026-10-22', '2026-10-23']
E = pd.concat([corre(d) for d in dias], ignore_index=True)
def frac(g, W): return float((g.dt <= W).mean())
def boot(g, W, B=2000, seed=20261116):
    cl = g.dia + '|' + g.mid.astype(str); u = cl.unique(); idx = {c: np.where(cl.values == c)[0] for c in u}; x = (g.dt.values <= W).astype(float)
    rng = np.random.default_rng(seed); s = []
    for _ in range(B):
        pick = rng.integers(len(u), size=len(u)); ii = np.concatenate([idx[u[p]] for p in pick]); s.append(x[ii].mean())
    return [round(float(np.quantile(s, .05)), 4), round(float(np.quantile(s, .95)), 4)]
res = dict(n_eventos={k: int(v) for k, v in E.brazo.value_counts().items()})
E['szb'] = pd.cut(E.sz, [0, 6, 15, 1e9], labels=['<=6', '6-15', '>15'])
for br in ('B', 'B_debajo', 'noB'):
    g = E[E.brazo == br]
    res[br] = dict(n=len(g), mercados=int((g.dia + g.mid.astype(str)).nunique()), P_W={W: round(frac(g, W), 4) for W in WS}, IC90_W={W: boot(g, W) for W in (100, 500, 1000)},
                   por_tam={str(s): dict(n=len(h), P100=round(frac(h, 100), 4), P500=round(frac(h, 500), 4)) for s, h in g.groupby('szb', observed=True)},
                   por_moneda={c: dict(n=len(h), P100=round(frac(h, 100), 4), P500=round(frac(h, 500), 4)) for c, h in g.groupby('coin')})
gB = E[E.brazo == 'B']
res['B_detalle'] = dict(relleno_propio_W={W: round(float((gB.dt_fill_propio <= W).mean()), 4) for W in WS}, por_cls=gB.cls.fillna('TN').value_counts().to_dict())
# emparejado noB a la distribucion de B por (moneda, tam, T en 4 tramos)
E['Tb'] = pd.cut(E['T'], [0, 60, 150, 240, 300], labels=False)
wB = gB.assign(Tb=E.loc[gB.index, 'Tb']).groupby(['coin', 'szb', 'Tb'], observed=True).size()
gN = E[E.brazo == 'noB']; cellN = gN.groupby(['coin', 'szb', 'Tb'], observed=True)
pm = {}
for W in (100, 500, 1000):
    num = den = 0.0
    for key, nB in wB.items():
        if key in cellN.groups: h = cellN.get_group(key); num += nB * frac(h, W); den += nB
    pm[W] = round(num / den, 4) if den else None
res['noB_emparejado_a_B'] = pm
json.dump(res, open(H + 'f3_resumen.json', 'w'), indent=1, default=str); print(json.dumps(res, indent=1, default=str))
