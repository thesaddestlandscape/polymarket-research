#!/usr/bin/env python3
"""rf5_nulo_run.py -- NULO POR RE-SIMULACION de RF5E-COMB (ESPEC E4; firma chief 23-Nov: Besag-Clifford secuencial h=20, p = h/L si para; si no (1+#)/(K+1), K<=1000). Estadistico (declarado): T_k = media/ee por DIAS de Delta_k,d = (PnL_k,d - PnL_base,d)/Coste_base,d (unidades de primer relleno, bloq 0, LO),
max-statistic sobre la familia (A: F1,F2,F3,U13; K: K1..K4). Cada permutacion j re-simula la politica con el veto F5 EXPLICITO por lados calculado con los F5_0 PERMUTADOS (el PAR Up/Down viaja junto, dentro de dia x moneda, RNG (semilla 20261124, dia, j)) y, en la familia K, con las series Binance
(V5/V6) desplazadas circularmente delta_perm(dia, j) >= 60 s. Motor rapido (rf5_rapido) construido UNA vez por dia y bloque de permutaciones; checkpoint durable JSONL (out/nulo_FAM_ckpt.jsonl, un dia x j por linea). 0 ordenes, 0 red.
MOTIVO DE LA SIMULACION COMPLETA (adenda interina 24-Nov sec.1; acople real medido en 17-Nov, out_rf5_ciego/acople_real_2026-11-17.json): b_policy_sim ACOPLA los mercados de un dia por el estado global busy/MAXV (ordenes vivas simultaneas), asi que el resultado de un mercado
depende de las decisiones en los demas y la composicion exacta por tablas (replicas base/VETO_UP/VETO_DN, rf5_nulo.nulo_replicas) sale NO_EXACTO. El p de AMBAS familias sale de re-simular el dia completo en cada replica (veto F5 explicito por lados con los F5_0 permutados; en K, ademas series Binance desplazadas).
K_max: familia K 1500, familia A 2000 (rf5_fronteras.K_MAX; adenda sec.6), h = 20, semilla 20261124. Prueba de identidad (`identidad DIA FAM`): la replica con el par F5_0 observado y desplazamiento 0 reproduce BIT A BIT la politica directa.
Uso:  rf5_nulo_run.py ensayo DIA FAM [N]   -> dia NO ciego (<=17-Nov): N permutaciones de un dia, SOLO tiempos y conteos (sin EV/PnL)
      rf5_nulo_run.py corre FAM [--K <K_max de la familia>] [--h 20] [--bloque 25]   -> mirada (6.o dia valido) o final (10.o): los dias los fija rf5_fronteras.decide_mirada; ESCRIBE p_max (solo con RF5_NULO_AUTORIZADO=1, autorizacion del chief)."""
import sys, os, json, time
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HV)
import numpy as np, pandas as pd
import rf5_run as RR, rf5_core as K5, rf5_nulo as NU, rf5_fronteras as FR
FAM = {'A': (K5.POLITICAS_NULO_A, ('F1', 'F2', 'F3', 'U13'), False), 'K': (K5.POLITICAS_NULO_K, ('K1', 'K2', 'K3', 'K4'), True)}

def unidades_dia(R):
    """(pnl, coste) del dia: unidades de primer relleno, rellenos solamente (cost/pnl NaN o q=0 => 0)."""
    if R is None or not len(R): return 0.0, 0.0
    q = R.q > 0; return float(R.pnl.where(q, 0.0).fillna(0.0).sum()), float(R.cost.where(q, 0.0).fillna(0.0).sum())

def delta_dia(pnl, cost, pnl_base, cost_base): return (pnl - pnl_base) / max(cost_base, 1e-12)

def Tobs_max(fam, Rbase, Robs, pols):
    """Tobs_max y Delta por dia/politica observados: Rbase (rf5A pol base, bloq 0, todos los dias) y Robs (rf5A para A | rf5K para K). pols: ('F1',..) | ('K1',..)."""
    dias = sorted(Rbase.dia.unique()); out = {}; b = {d: unidades_dia(Rbase[Rbase.dia == d]) for d in dias}
    for p in pols:
        X = Robs[(Robs.pol == p) & (Robs.bloq == 0)]; dd = [delta_dia(*unidades_dia(X[X.dia == d]), *b[d]) for d in dias]; out[p] = dict(T=NU.T_stat(dd), delta_dias=dd)
    return dict(Tmax=float(np.nanmax([v['T'] for v in out.values()])), por_politica=out, dias=dias)

def _sin_etiqueta(X):
    """la columna `pol` es solo la ETIQUETA de la replica (`F1_SET` frente a `F1`; hallazgo 24-Nov: era la unica columna distinta en las 19.542/2.956/17.600/17.493 filas de F1/F2/F3/U13): se excluye; todas las demas columnas (precio, tamaño, instante, motivo, pnl...) se comparan bit a bit."""
    return X.drop(columns=['pol'], errors='ignore').reset_index(drop=True)

def igual(A, B):
    """igualdad BIT A BIT de dos DataFrames de ordenes (mismas filas, orden y valores; `equals`), salvo la etiqueta `pol`."""
    return (len(A) == len(B)) and (len(A) == 0 or _sin_etiqueta(A).equals(_sin_etiqueta(B)))

def difiere(A, B, max_filas=3):
    """DIAGNOSTICO de una desigualdad: columnas distintas (con nº de filas distintas y primeras filas) o 'orden' si solo cambia el orden de filas."""
    A = _sin_etiqueta(A); B = _sin_etiqueta(B)
    if len(A) != len(B): return dict(longitud=[len(A), len(B)])
    if list(A.columns) != list(B.columns): return dict(columnas=[list(A.columns), list(B.columns)])
    out = {}
    for c in A.columns:
        x, y = A[c], B[c]; ne = ~((x == y) | (x.isna() & y.isna()))
        if ne.any(): out[c] = dict(n=int(ne.sum()), ejemplo=[[str(x[i]), str(y[i])] for i in list(ne[ne].index[:max_filas])])
    return out

def prepara_dia(d, E, P, W, ctx, cortes):
    """F5_0 por lado (base + replicas VETO_UP/VETO_DN para el lado que la base no intenta), tabla por mercado M y unidades de la base del dia: (M, base_dia, Rb)."""
    Rb, c, HKb = RR._replay(d, P, W, ctx, 'base', K5.POLITICAS_A, None, cortes, None, None); fb = RR.construye_f5tab(HKb.f5_0, d, 0, 'base')
    Rvu, c, HKu = RR._replay(d, P, W, ctx, 'VETO_UP', K5.POLITICAS_A, None, cortes, None, None); Rvd, c, HKd = RR._replay(d, P, W, ctx, 'VETO_DN', K5.POLITICAS_A, None, cortes, None, None)
    F = pd.concat([fb, RR.construye_f5tab(HKu.f5_0, d, 0, 'VETO_UP'), RR.construye_f5tab(HKd.f5_0, d, 0, 'VETO_DN')], ignore_index=True)
    M = NU.tabla_mercados(pd.concat([Rb.assign(dia=d, bloq=0, pol='base'), Rvu.assign(dia=d, bloq=0, pol='VETO_UP'), Rvd.assign(dia=d, bloq=0, pol='VETO_DN')], ignore_index=True), F)
    return M, {d: unidades_dia(Rb)}, Rb

class SimNulo:
    """sim_bloque(dia, [(j, delta_ms), ...]) -> {j: {pol: Delta_dia}}: construye el motor del dia UNA vez y simula cada permutacion (4 replays por permutacion).
    TABLA F5_0 POR POLITICA (hallazgo 24-Nov, prueba de identidad en 17-Nov): con acople real (busy/MAXV) el instante de la PRIMERA alta intentada de un lado -- y por tanto su F5_0 -- depende de la politica (K1 intenta lados que la base no intenta: 8.272 ordenes directas frente a 8.201 con el par de la base).
    Por eso cada politica usa SU PROPIA tabla F5_0 observada: la de su replica directa (HK.f5_0) y, para los lados que esa replica no intenta, la de las replicas base/VETO_UP/VETO_DN (relleno inocuo: bajo la identidad esos lados tampoco se intentan). La permutacion pi (dentro de dia x moneda; el PAR Up/Down viaja junto) es UNA sola por (dia, j) y compartida por todas las politicas.
    Con pi = identidad cada replica reproduce BIT A BIT su politica directa (`identidad`)."""
    def __init__(self, fam, base_dia, M_dia, cortes, tp):
        self.pol_tabla, self.pols, self.con_binance = FAM[fam]; self.fam = fam; self.base_dia = base_dia; self.M_dia = M_dia; self.cortes = cortes; self.tp = tp
        self.directas = K5.POLITICAS_A if fam == 'A' else K5.POLITICAS_K
    def _ctx(self, d, pre=None):
        """pre = (E, P, W, ctx) ya construidos (evita construir E dos veces: 2 x ~3 GB reventaba el ulimit -v 5 GB en la prueba de identidad)."""
        import b_policy_sim as BS, eng_v5 as EV, calendar
        if pre is None: E, info = EV.build(d); P = BS.params(); W = RR.motor(E, False); ctx = dict(W=W, serie=W._serie)
        else: E, P, W, ctx = pre
        mid_k = {}; coin_de = {}; D = E.D
        for k in E.ks:
            if E.sane(k) != 'ok': continue
            mid_k.setdefault(D.mid[k], {})[D.lado[k]] = k; coin_de[D.mid[k]] = str(D.act[k]).lower()
        mid_k = {m: (v['YES'], v['NO']) for m, v in mid_k.items() if 'YES' in v and 'NO' in v}; bsrc = RR.FB.carga_binance(d) if self.con_binance else None
        if self.con_binance and not bsrc: raise RuntimeError('DATA_BLOCKED: sin m5_registro Binance para %s' % d)
        d0 = calendar.timegm(time.strptime(d, '%Y-%m-%d')) * 1000
        return E, P, W, ctx, mid_k, coin_de, bsrc, d0
    def tablas(self, d, P, W, ctx, mid_k, bsrc):
        """{pol_nulo: {mid: (f_up, f_dn)}} (ver docstring de la clase) + las ordenes de cada replica directa {pol: DataFrame} (para la prueba de identidad)."""
        M = self.M_dia[self.M_dia.mid.isin(mid_k)]; fill = {m: (float(a), float(b)) for m, a, b in zip(M.mid, M.f_up, M.f_dn)}; T = {}; D = {}
        for nombre in self.pols_nulo():
            dire = nombre[:-4]; R, c, HK = RR._replay(d, P, W, ctx, dire, self.directas, bsrc, self.cortes, self.tp if bsrc else None, None); D[dire] = R; t = {}
            for mid, (ku, kd) in mid_k.items():
                fu = HK.f5_0.get((mid, int(ku))); fd = HK.f5_0.get((mid, int(kd))); a, b = fill.get(mid, (float('nan'), float('nan')))
                t[mid] = (float(fu['f5_0']) if fu is not None else a, float(fd['f5_0']) if fd is not None else b)
            T[nombre] = t
        return T, D
    def replica(self, d, P, W, ctx, nombre, pares, mid_k, coin_de, bsh):
        """UNA replica (politica `nombre` del nulo) con el veto explicito por lados de `pares` y las series Binance `bsh` (None en A). Devuelve el DataFrame de ordenes del simulador completo."""
        regla = K5.REGLA_DE_K.get(nombre, nombre[:-4]); vs = NU.veto_set_de_pares(regla, pares, mid_k, coin_de, self.cortes)
        R, c, HK = RR._replay(d, P, W, ctx, nombre, self.pol_tabla, bsh, self.cortes, self.tp if bsh else None, vs); return R
    def __call__(self, d, lista, pre=None):
        E, P, W, ctx, mid_k, coin_de, bsrc, d0 = self._ctx(d, pre); out = {}; M = self.M_dia[self.M_dia.mid.isin(mid_k)]
        with RR.desenlace_con_marcador():
            T, _ = self.tablas(d, P, W, ctx, mid_k, bsrc)
            for j, delta in lista:
                asig = NU.permuta_asignacion(M, NU.rng_perm(d, j)); [asig.setdefault(m_, m_) for m_ in mid_k]      # mercados que ninguna replica de F5 intento (fuera de M) conservan su tabla: nunca quedan sin veto
                bsh = {c: NU.desplaza_circular(tt, pp, d0, delta) for c, (tt, pp) in bsrc.items()} if bsrc else None; r_j = {}
                for nombre in self.pols_nulo():
                    pares = {a: T[nombre][b] for a, b in asig.items()}; pn, co = unidades_dia(self.replica(d, P, W, ctx, nombre, pares, mid_k, coin_de, bsh)); r_j[nombre[:-4]] = delta_dia(pn, co, *self.base_dia[d])
                out[j] = r_j
        return out
    def identidad(self, d, pre=None):
        """PRUEBA DE IDENTIDAD (ADENDA interina sec.1): con pi = identidad (cada mercado conserva su propia tabla F5_0) y sin desplazar las series, la replica del nulo reproduce BIT A BIT la politica directa (F1..U13 | K1..K4) en el simulador completo. Devuelve {pol: dict(igual, ordenes_directa, ordenes_set)}."""
        E, P, W, ctx, mid_k, coin_de, bsrc, d0 = self._ctx(d, pre); res = {}
        with RR.desenlace_con_marcador():
            T, D = self.tablas(d, P, W, ctx, mid_k, bsrc)
            for nombre in self.pols_nulo():
                dire = nombre[:-4]; Rs = self.replica(d, P, W, ctx, nombre, T[nombre], mid_k, coin_de, bsrc)
                ig = bool(igual(Rs, D[dire])); res[dire] = dict(igual=ig, ordenes_directa=int(len(D[dire])), ordenes_set=int(len(Rs)), **({} if ig else dict(difiere=difiere(Rs, D[dire]))))
        return res
    def pols_nulo(self): return list(self.pol_tabla)

def main(argv):
    modo = argv[0]
    if modo == 'ensayo':
        d, fam = argv[1], argv[2]; n = int(argv[3]) if len(argv) > 3 else 2
        if d >= '2026-11-18': raise SystemExit('dia ciego: prohibido')
        import b_policy_sim as BS, eng_v5 as EV
        cortes = K5.lee_cortes(); tp = RR.t_proc(); E, info = EV.build(d); P = BS.params(); W = RR.motor(E, False); ctx = dict(W=W, serie=W._serie); t0 = time.time()
        M, base_dia, Rb = prepara_dia(d, E, P, W, ctx, cortes); t_prep = round(time.time() - t0, 1)
        sim = SimNulo(fam, base_dia, M, cortes, tp); t1 = time.time(); r = sim(d, [(j, NU.delta_perm(d, j)) for j in range(n)], (E, P, W, ctx)); seg = round(time.time() - t1, 1)
        res = dict(dia=d, familia=fam, permutaciones=n, politicas_por_permutacion=len(sim.pols_nulo()), segundos_prep_base_y_vetos=t_prep, segundos_total_permutaciones_incl_build_E=seg, segundos_por_dia_replica=round(seg / (n * len(sim.pols_nulo())), 1), n_deltas=sum(len(v) for v in r.values()))
        json.dump(res, open(RR.OUT + f'nulo_ensayo_{fam}_{d}.json', 'w'), indent=1); print(json.dumps(res)); return 0
    if modo == 'identidad':      # DIA FAM: dia NO ciego; prueba de identidad bit a bit (solo igualdades y conteos, sin EV/PnL)
        d, fam = argv[1], argv[2]
        if d >= '2026-11-18': raise SystemExit('dia ciego: prohibido')
        import b_policy_sim as BS, eng_v5 as EV
        cortes = K5.lee_cortes(); tp = RR.t_proc(); E, info = EV.build(d); P = BS.params(); W = RR.motor(E, False); ctx = dict(W=W, serie=W._serie); M, base_dia, Rb = prepara_dia(d, E, P, W, ctx, cortes)
        r = SimNulo(fam, base_dia, M, cortes, tp).identidad(d, (E, P, W, ctx)); res = dict(dia=d, familia=fam, identidad=r, todo_igual=bool(all(v['igual'] for v in r.values()))); json.dump(res, open(RR.OUT + f'nulo_identidad_{fam}_{d}.json', 'w'), indent=1); print(json.dumps(res)); return 0
    if modo == 'corre':
        if os.environ.get('RF5_NULO_AUTORIZADO') != '1': raise SystemExit('BLOQUEADO: el nulo por re-simulacion escribe p_max (EV): solo en la mirada con autorizacion del chief (RF5_NULO_AUTORIZADO=1)')
        fam = argv[1]; K = int(argv[argv.index('--K') + 1]) if '--K' in argv else FR.k_max(fam); h = int(argv[argv.index('--h') + 1]) if '--h' in argv else FR.H_BC; bl = int(argv[argv.index('--bloque') + 1]) if '--bloque' in argv else 25
        dec = FR.decide_mirada(RR.estado())          # dias EXACTOS de la mirada (6 primeros validos | 10 primeros): nunca por argumento
        if dec['mirada'] == 0 or min(dec['dias']) < '2026-11-18': raise SystemExit(f"BLOQUEADO: sin mirada habilitada ({dec['nombre']}: {dec['motivo']})")
        dias = dec['dias']; fk = 'K1_K4' if fam == 'K' else 'A'
        if not FR.resolucion_ok(fk, dec['mirada'], k=K): raise SystemExit(f'BLOQUEADO: K_max={K} < 5/umbral de la mirada {dec["mirada"]} ({fk}): sin resolucion para rechazar')
        cortes = K5.lee_cortes(); tp = RR.t_proc(); RA = pd.concat([pd.read_pickle(RR.OUT + f'rf5A_{d}.pkl') for d in dias], ignore_index=True); FA = pd.concat([pd.read_pickle(RR.OUT + f'rf5_f5_0_{d}.pkl') for d in dias], ignore_index=True)
        Robs = RA if fam == 'A' else pd.concat([pd.read_pickle(RR.OUT + f'rf5K_{d}.pkl') for d in dias], ignore_index=True); Rb = RA[(RA.bloq == 0) & (RA.pol == 'base')]
        obs = Tobs_max(fam, Rb, Robs, FAM[fam][1]); M = NU.tabla_mercados(RA, FA); base = {d: unidades_dia(Rb[Rb.dia == d]) for d in dias}
        cache = {}
        def sim_bloque(d, lista): return SimNulo(fam, base, M[M.dia == d], cortes, tp)(d, lista)
        r = NU.nulo_K_run(dias, obs['Tmax'], None, RR.OUT + f'nulo_{fam}_ckpt.jsonl', K=K, h=h, sim_bloque=sim_bloque, bloque=bl); r.update(familia=fam, T_max_obs=obs['Tmax'], dias=dias, mirada=dec['mirada'], K_max=K, umbral_p=FR.umbral_p(fk, dec['mirada']), estado='NULO_RESIMULADO_EXACTO')
        json.dump(r, open(RR.OUT + f'nulo_{fam}_resultado.json', 'w'), indent=1, default=str); print(json.dumps(r, default=str)); return 0
    raise SystemExit(__doc__)

if __name__ == '__main__': sys.exit(main(sys.argv[1:]))
