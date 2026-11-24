#!/usr/bin/env python3
"""rf5_nulo.py -- NULO EXACTO DENTRO DEL SIMULADOR (ESPEC E4; DICTAMEN tests 3 y 4). Todos los estadisticos de gate salen de la SIMULACION, nunca de filtrar posterior.
Familia A (F1,F2,F3,U13): por dia hay replicas base / VETO_UP (veto a todas las Up) / VETO_DN. Si b_policy_sim no acopla mercados, el resultado de un mercado bajo cualquier combinacion de vetos (vetoUp, vetoDn) se lee de la replica:
 (F,F)=base, (T,F)=VETO_UP, (F,T)=VETO_DN, (T,T)=sin entrada (0). Nulo: permutar el PAR (F5_0^Up, F5_0^Down) entre mercados dentro de dia x moneda; p = (1+#{T* >= T})/(K+1) (no .mean()), K<=1000 con parada secuencial de Besag-Clifford h=20 (p = h/L si para antes; firma chief 23-Nov), semilla 20261124.
F5_0 de un lado que la base no intenta sale de la replica donde el OTRO lado esta vetado (ahi si se intenta). `verifica_composicion` compara la composicion con la replica DIRECTA (F1/F2/F3/U13): si difiere (acople real, p.ej. MAXV/busy) el nulo se marca NO_EXACTO y NO es confirmatorio.
VIGENCIA (adenda interina 24-Nov, acople real medido en 17-Nov: b_policy_sim acopla los mercados por el estado global busy/MAXV): el p CONFIRMATORIO de AMBAS familias sale de la SIMULACION COMPLETA por replica (rf5_nulo_run.py corre A|K; `nulo_K_run` + SimNulo), con K_max 2000 (A) / 1500 (K), h = 20, semilla 20261124 (rf5_fronteras). `nulo_replicas` (composicion por tablas) queda como DIAGNOSTICO y con acople real sale NO_EXACTO.
Familia K: `nulo_K_run` re-simula con series Binance desplazadas circularmente (>=60 s) ; checkpoint durable por (dia, permutacion); Besag-Clifford h=20. Puro (sin IO) salvo checkpoint. 0 ordenes, 0 red."""
import os, sys, json, time
import numpy as np, pandas as pd
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HV)
import rf5_core as K5
SEMILLA = 20261124; REGLAS = ('F1', 'F2', 'F3', 'U13')

def tabla_mercados(R, F):
    """DataFrame por (dia, coin, mid): f_up, f_dn (F5_0; NaN = invalido/no intentado), y (pnl, cost) por combinacion de vetos: bb (base), vu (VETO_UP), vd (VETO_DN). R: filas de rf5A (bloq 0); F: rf5_f5_0 (pol base/VETO_*)."""
    R = R[R.bloq == 0]; F = F[F.bloq == 0]
    def uni(pol):
        X = R[(R.pol == pol)]; X = X.assign(pnl=X.pnl.where(X.q > 0, 0.0).fillna(0.0), cost=X.cost.where(X.q > 0, 0.0).fillna(0.0)); return X.groupby(['dia', 'mid'], as_index=False).agg(pnl=('pnl', 'sum'), cost=('cost', 'sum'), coin=('coin', 'first'))
    base = uni('base'); vu = uni('VETO_UP'); vd = uni('VETO_DN')
    def f5pol(pol, lado):
        X = F[(F.pol == pol) & (F.lado == lado)]; return X.groupby(['dia', 'mid']).f5_0.first()
    keys = pd.concat([F[['dia', 'mid', 'coin']].drop_duplicates(['dia', 'mid']), base[['dia', 'mid', 'coin']]]).drop_duplicates(['dia', 'mid']).reset_index(drop=True)
    idx = pd.MultiIndex.from_frame(keys[['dia', 'mid']])
    f_up = f5pol('base', 'YES').reindex(idx).fillna(f5pol('VETO_DN', 'YES').reindex(idx)); f_dn = f5pol('base', 'NO').reindex(idx).fillna(f5pol('VETO_UP', 'NO').reindex(idx))
    M = keys.assign(f_up=f_up.values.astype(float), f_dn=f_dn.values.astype(float))
    for nom, U in (('bb', base), ('vu', vu), ('vd', vd)):
        U2 = U.set_index(['dia', 'mid'])[['pnl', 'cost']].reindex(idx); M[f'pnl_{nom}'] = U2.pnl.fillna(0.0).values; M[f'cost_{nom}'] = U2.cost.fillna(0.0).values
    return M.sort_values(['dia', 'coin', 'mid']).reset_index(drop=True)

def vetos(regla, coin, f_up, f_dn, c):
    """vectorizado: (vetoUp, vetoDn) por mercado segun K5.veta_f5 (invalido NaN => veta)."""
    def v(f):
        f = np.asarray(f, float); inv = ~np.isfinite(f); g = np.where(inv, np.inf, f); coins = np.asarray(coin)
        p20 = np.array([c['F2_p20'][x.lower()] for x in coins]); p80 = np.array([c['F3_p80'][x.lower()] for x in coins])
        if regla == 'F1': return inv | (g >= c['C1'])
        if regla == 'F2': return inv | ~(g < p20)
        if regla == 'F3': return inv | (g >= p80)
        if regla == 'U13': return inv | (g >= c['C1']) | (g >= p80)
        raise ValueError(regla)
    return v(f_up), v(f_dn)

def pnl_compuesto(M, vu_, vd_):
    """PnL por mercado bajo los vetos dados (leyendo la replica correspondiente)."""
    return np.where(~vu_ & ~vd_, M.pnl_bb.values, np.where(vu_ & ~vd_, M.pnl_vu.values, np.where(~vu_ & vd_, M.pnl_vd.values, 0.0)))

def T_stat(dd):
    dd = np.asarray(dd, float)
    return np.nan if len(dd) < 2 or np.std(dd, ddof=1) == 0 else float(np.mean(dd) / (np.std(dd, ddof=1) / np.sqrt(len(dd))))

def estadisticos(M, f_up, f_dn, c, reglas=REGLAS):
    """Delta_k por dia = (PnL(regla) - PnL(base)) / coste base del dia; T_k sobre dias."""
    dias = sorted(M.dia.unique()); di = M.dia.map({d: i for i, d in enumerate(dias)}).values; cost_d = np.bincount(di, M.cost_bb.values, minlength=len(dias)); pb = np.bincount(di, M.pnl_bb.values, minlength=len(dias)); out = {}
    for r in reglas:
        vu_, vd_ = vetos(r, M.coin.values, f_up, f_dn, c); pr = np.bincount(di, pnl_compuesto(M, vu_, vd_), minlength=len(dias)); dd = (pr - pb) / np.maximum(cost_d, 1e-12); out[r] = dict(T=T_stat(dd), dias=dd)
    return out

def verifica_composicion(R, F, c):
    """compara la composicion (replicas base/VETO_UP/VETO_DN) con la replica DIRECTA de cada regla, por mercado. Devuelve dict(por_regla{n_mercados, iguales, distintos, pnl_dif}, exacto: bool)."""
    M = tabla_mercados(R, F); out = {}; ok = True; R0 = R[R.bloq == 0]
    for r in REGLAS:
        X = R0[R0.pol == r]; X = X.assign(pnl=X.pnl.where(X.q > 0, 0.0).fillna(0.0), cost=X.cost.where(X.q > 0, 0.0).fillna(0.0)); U = X.groupby(['dia', 'mid']).agg(pnl=('pnl', 'sum'), cost=('cost', 'sum')).reindex(pd.MultiIndex.from_frame(M[['dia', 'mid']])).fillna(0.0)
        vu_, vd_ = vetos(r, M.coin.values, M.f_up.values, M.f_dn.values, c); comp = pnl_compuesto(M, vu_, vd_); dif = ~np.isclose(comp, U.pnl.values, rtol=0, atol=1e-12)
        out[r] = dict(n_mercados=int(len(M)), iguales=int((~dif).sum()), distintos=int(dif.sum()), pnl_dif=float(comp.sum() - U.pnl.sum())); ok &= bool(not dif.any())
    return dict(por_regla=out, exacto=ok)

def nulo_replicas(R, F, c, K=1000, seed=SEMILLA, h=20):
    """T_obs por regla y p_max = (1+#{max_k T*_k >= max_k T_k})/(K+1) con permutacion del PAR (f_up,f_dn) entre mercados dentro de dia x moneda. K>=1000 (menos solo en tests)."""
    M = tabla_mercados(R, F); comp = verifica_composicion(R, F, c); obs = estadisticos(M, M.f_up.values, M.f_dn.values, c); Tobs = {r: obs[r]['T'] for r in REGLAS}; Tmax_obs = float(np.nanmax(list(Tobs.values())))
    grp = M.groupby(['dia', 'coin']).indices; G = [np.asarray(v) for v in grp.values()]; rng = np.random.default_rng(seed); cnt = 0; fu = M.f_up.values; fd = M.f_dn.values; n_perm = 0
    for _ in range(K):
        pu = fu.copy(); pd_ = fd.copy()
        for g in G: o = g[rng.permutation(len(g))]; pu[g] = fu[o]; pd_[g] = fd[o]            # el par viaja junto
        st = estadisticos(M, pu, pd_, c); cnt += int(np.nanmax([st[r]['T'] for r in REGLAS]) >= Tmax_obs); n_perm += 1
        if h and cnt >= h: break                                  # Besag-Clifford (FIRMA chief 23-Nov): parada secuencial con h exceedances
    return dict(T_obs=Tobs, T_max_obs=Tmax_obs, K=K, n_perm=n_perm, h=h, exceden=cnt, p_max=besag_clifford(cnt, n_perm, K, h), semilla=seed, composicion=comp, exacto=comp['exacto'], estado=('EXACTO' if comp['exacto'] else 'NO_EXACTO_ACOPLE (no confirmatorio)'))

# ------------------------------------------------------------------ familia K: desplazamiento circular + re-simulacion
def desplaza_circular(t, p, day_start_ms, delta_ms, dia_ms=86400000):
    """desplaza los instantes circularmente dentro del dia (t' = day_start + (t - day_start + delta) mod dia), reordena por tiempo y devuelve (t', p'). delta >= 60 s. El punto de corte crea a lo sumo 1 retorno artificial (declarado)."""
    t = np.asarray(t, np.int64); p = np.asarray(p, float); t2 = day_start_ms + (t - day_start_ms + int(delta_ms)) % dia_ms; o = np.argsort(t2, kind='stable'); return t2[o], p[o]

def delta_perm(dia, j, seed=SEMILLA, minimo_ms=60000, dia_ms=86400000):
    """desplazamiento determinista por (dia, permutacion): reproducible y reanudable. delta in [60 s, dia-60 s]."""
    h = int.from_bytes(__import__('hashlib').sha256(f'{seed}|{dia}|{j}'.encode()).digest()[:8], 'big'); return int(minimo_ms + h % (dia_ms - 2 * minimo_ms))

def besag_clifford(exceden, n_perm, K, h=20):
    """p con parada secuencial: si exceden alcanza h antes de K => p = h / n_perm; si no, p = (1+exceden)/(K+1)."""
    return (exceden / n_perm) if (exceden >= h and n_perm < K) else ((1 + exceden) / (K + 1))

def _lee_ckpt(ckpt):
    """checkpoint JSONL: una linea por (dia, j). Se descartan lineas corruptas/truncadas y duplicados (gana la primera). Devuelve {(dia, j): valor}."""
    hechos = {}
    if os.path.exists(ckpt):
        for ln in open(ckpt):
            try: r = json.loads(ln); k = (r['dia'], int(r['j']))
            except Exception: continue
            hechos.setdefault(k, r['d'])
    return hechos

def nulo_K_run(dias, Tobs_max, sim_dia, ckpt, K=1000, h=20, seed=SEMILLA, sim_bloque=None, bloque=1):
    """Nulo por RE-SIMULACION con parada secuencial de Besag-Clifford (h exceedances => p = h/L; si no, (1+#)/(K+1) con K<=1000). Una permutacion j = para cada dia, sim_dia(dia, delta_ms, j) -> {pol: Delta/EUR del dia (vs base)} con las series Binance desplazadas
    circularmente delta_perm(dia, j) (y los F5_0 permutados con semilla (dia, j) dentro de la simulacion). T_k = T_stat(Delta_k,d sobre dias); estadistico del nulo = max_k T_k >= Tobs_max.
    sim_bloque(dia, [(j, delta), ...]) -> {j: {pol: Delta}} (opcional): simula varias permutaciones de un dia con el motor construido UNA vez (bloque de permutaciones). Checkpoint durable (JSONL, fsync) por (dia, j): al reanudar se saltan las hechas y no se duplica ninguna.
    Devuelve dict(p_max, n_perm, exceden, parada, K, h, semilla)."""
    hechos = _lee_ckpt(ckpt); exc = 0; n = 0; bloque = max(1, int(bloque))
    def guarda(d, j, v):
        hechos[(d, j)] = v
        with open(ckpt, 'a') as f: f.write(json.dumps(dict(dia=d, j=j, d=v)) + '\n'); f.flush(); os.fsync(f.fileno())
    for j0 in range(0, K, bloque):
        js = list(range(j0, min(K, j0 + bloque)))
        for d in dias:
            pend = [j for j in js if (d, j) not in hechos]
            if not pend: continue
            if sim_bloque is not None:
                out = sim_bloque(d, [(j, delta_perm(d, j, seed)) for j in pend])
                for j in pend: guarda(d, j, out[j])
            else:
                for j in pend: guarda(d, j, sim_dia(d, delta_perm(d, j, seed), j))
        for j in js:
            res = {d: hechos[(d, j)] for d in dias}; pols = sorted(next(iter(res.values())).keys()); T = [T_stat([res[d][p] for d in dias]) for p in pols]
            exc += int(np.nanmax(T) >= Tobs_max); n += 1
            if h and exc >= h: break
        if h and exc >= h: break
    return dict(p_max=besag_clifford(exc, n, K, h), n_perm=n, exceden=exc, K=K, h=h, parada=('besag_clifford' if (h and exc >= h and n < K) else 'K_completo'), semilla=seed)

def rng_perm(dia, j, seed=SEMILLA):
    """RNG determinista por (dia, permutacion): reproducible y reanudable."""
    import hashlib
    return np.random.default_rng(int.from_bytes(hashlib.sha256(f'{seed}|perm|{dia}|{j}'.encode()).digest()[:8], 'big'))

def permuta_asignacion(M, rng):
    """M: DataFrame con (coin, mid) de UN dia. Devuelve {mid_destino: mid_origen}: permutacion de mercados DENTRO de la moneda (el PAR (f_up, f_dn) viaja junto). Una sola permutacion pi compartida por todas las politicas (cada una aplica su propia tabla F5_0 observada)."""
    out = {}
    for coin, g in M.groupby('coin'):
        mids = g.mid.values; o = rng.permutation(len(g))
        for a, b in zip(mids, o): out[a] = mids[b]
    return out

def permuta_pares(M, rng):
    """M: DataFrame con (coin, mid, f_up, f_dn) de UN dia. Devuelve {mid: (f_up, f_dn)} con el PAR permutado entre mercados dentro de la moneda (el par viaja junto: conserva la dependencia Up/Down)."""
    asig = permuta_asignacion(M, rng); fu = dict(zip(M.mid, M.f_up)); fd = dict(zip(M.mid, M.f_dn))
    return {a: (float(fu[b]), float(fd[b])) for a, b in asig.items()}

def veto_set_de_pares(regla, pares, mid_k, coin_de, cortes):
    """veto explicito {(mid,k)} para la regla segun el par asignado a cada mercado. mid_k = {mid: (ku, kd)}; coin_de = {mid: coin}. F5_0 no finito => veta (K5.veta_f5)."""
    v = set()
    for mid, (fu, fd) in pares.items():
        ku, kd = mid_k[mid]; c = coin_de[mid]
        for k, f in ((ku, fu), (kd, fd)):
            if K5.veta_f5(regla, c, (None if not np.isfinite(f) else f), cortes): v.add((mid, int(k)))
    return v
