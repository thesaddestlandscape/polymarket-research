#!/usr/bin/env python3
"""Arnes diario de PREREG_DB1 (sha 1d12afa2f22a1bbb3ccece15b2aec01f437d86b7ef83f2a23479708e1197e998): simulacion de G0, CXJ150 (aceptacion), H-DB1, H-DB2, descriptivos, inversiones y placebos.
DEV/solo lectura, 0 ordenes. NO modifica engine.py, passT.py ni rt_sim.py: LEE passT.py (sha comprobado), sustituye SOLO la lista de variantes, el modelo de relleno y 4 puntos de enganche, y lo
ejecuta con __file__ en este directorio (patron placebo_cxj150.py / rt_cxj150_cross.py). Las funciones qall/mid_at/cross_events/fill_v de rt_sim.py se extraen por AST (sha comprobado) y se
evaluan en el mismo espacio de nombres (cotas BASE/CROSS/STRICT/OPT/THIN del prereg sec. 3).
Uso (nice -n 19 ionice -c3, ulimit -v 3000000, fuera de 06:00-09:15Z; lo lanza eval_db1.py --producir):
  python3 -I passdb.py dia D            -> out/RX_<D>.pkl (rellenos de todas las variantes + extras RMR/salida), out/cov_<D>.json, out/excl_<D>.json, out/vida_<D>.json
  python3 -I passdb.py placebo D SEMILLA -> placebo/s<SEMILLA>/out/RX_<D>.pkl (solo PDB1_150, PDB2_150 BASE)
  python3 -I passdb.py test              -> comprueba que los parches aplican (sin ejecutar nada pesado)
Reloj: todo disparador por hora de RECEPCION (ticks Binance recv_ms; prints del WS del CLOB D.tt). Triggers: r1 de Binance a 1 s en bps con la funcion bnr de passT (frescura <= 15 s => NaN = G0)."""
import sys, os, re, json, ast, hashlib, time, gc
import numpy as np, pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'
Q11 = HERE + '../q11/'
PT = Q11 + 'toxicidad_thru1/passT.py'; RT = Q11 + 'redteam/rt_sim.py'; ENG = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/escalera_B/engine.py'
SHA = dict(PT='a8b9d7a0158fd0b0cf47582c499d6c1cc870269310c8ef4481482733d1c64038', RT='86b14afbf91b308ab6185e0060427047fc644a6a0ac33813127627ef507f652b',
           ENG='a7b8431a73952524917ffd90e65b2dcf2779fabd3c452bc0407d36e34b1e8feb')
DL = '/root/polymarket-research-datalogs/'
COINS = ('ETH', 'SOL', 'XRP'); FVS = ('CROSS', 'STRICT', 'OPT', 'THIN'); TRIG_BP = 1.0; WIN_MS = 1000
CHAIN_CONTRACTS = {'0xe111180000d2663c0091e4f400237545b87b996b', '0x4bfb41d5b3570defd03c39a9a4d8de6bd8b8982e', '0xc5d563a36ae78145c45a50134d48a1215220f80a'}
BAND_MAX = 0.20          # "bids de banda" de la rafaga (sec. 6): precio del bid <= 0,20 (cubre los niveles G.LEVELS hasta 0,19 con holgura de tick)
LSPEC = {'DB1': (150, 300, 1000), 'DB2': (150, 300, 1000), 'DBU': (150,), 'INV1': (150,), 'INV2': (150,)}
ARMS_FV = ('G0', 'DB1_150', 'DB2_150', 'DBU_150')       # variantes que ademas corren con las 4 cotas de relleno
BASE_VN = ['G0', 'CXJ150'] + [f'{a}_{l}' for a, ls in LSPEC.items() for l in ls]
MAIN_VN = BASE_VN + [f'{a}@{f}' for a in ARMS_FV for f in FVS]
PLA_VN = ['PDB1_150', 'PDB2_150']
def niveles_desde_fuente(eng=None):
    """LEVELS de engine.py leidos por AST (sin importarlo ni ejecutarlo) -> tupla."""
    t = ast.parse(open(eng or ENG).read())
    for n_ in t.body:
        if isinstance(n_, ast.Assign) and any(getattr(x, 'id', None) == 'LEVELS' for x in n_.targets): return tuple(float(x) for x in ast.literal_eval(n_.value))
    raise AssertionError('no encuentro LEVELS en engine.py')
def check_band(levels, R=None):
    """Coherencia fallo-ruidoso: ningun nivel de NINGUNA variante (G0, brazos, @CROSS/@STRICT/@OPT/@THIN) pasa de BAND_MAX (la banda de la rafaga, sec. 6, filtra bids <= BAND_MAX)."""
    assert len(levels) and max(levels) <= BAND_MAX + 1e-9, f'LEVELS {levels} > BAND_MAX {BAND_MAX}'
    if R is not None and len(R):
        mx = R.groupby('var').L.max(); mal = mx[mx > BAND_MAX + 1e-9]
        assert mal.empty, f'variantes con L > BAND_MAX {BAND_MAX}: {mal.to_dict()}'
def sha_f(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
def atomic_json(path, obj):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True); tmp = path + '.tmp'
    with open(tmp, 'w') as f: f.write(json.dumps(obj, indent=1, default=float)); f.flush(); os.fsync(f.fileno())
    os.replace(tmp, path)
def shift_ms(seed, d):   # = placebo_cxj150.shift_ms (UNA s por (semilla, dia), comun a las 3 monedas)
    return int(np.random.default_rng(seed * 100003 + int(d.replace('-', ''))).integers(60, 86341)) * 1000
def koff(seed, d):       # desfase entero de cierres k ~ U{1..287}, UNA k por semilla y dia
    return int(np.random.default_rng(seed * 100003 + int(d.replace('-', '')) + 7).integers(1, 288))
def circ_shift(a, day0, s_ms):
    """tau' = D0 + ((tau - D0 + s) mod 86400 s) sobre los disparos DEL DIA (los del dia anterior no entran)."""
    a = np.asarray(a, np.int64); a = a[(a >= day0) & (a < day0 + 86400000)]
    return np.sort(day0 + ((a - day0 + s_ms) % 86400000))
def first_after(arr, t0, t1):
    i = np.searchsorted(arr, t0, side='left'); return int(arr[i]) if i < len(arr) and arr[i] <= t1 else None
def recent(tr, tq):
    """True donde hubo disparo con hora de recepcion en (tq-1000, tq] = (t-1300, t-300] (sec. 2 (i) y (iii): re-arma tras 1000 ms seguidos sin disparo)."""
    return (np.searchsorted(tr, tq, side='right') - np.searchsorted(tr, tq - 1000, side='right')) > 0
def union_sorted(a, b): return np.sort(np.concatenate([np.asarray(a, np.int64), np.asarray(b, np.int64)]))
# ------------------------------------------------------------------ salud Binance (sec. 4 + ADDENDUM1 secc. A, R1-R6)
ADD1_SHA = 'b083b7a58c9dda13e673675ea2366c50f0cdb74e2ded972c469509298690bd1d'     # PREREG_DB1_ADDENDUM1.md (congelado 10-Nov)
MIN_HORAS_DIA = 12; G_COIN = 30; G_UNION = 10; G_UNION_LARGO = 300; PAD_FIN = 15     # R2 (segundos), R4 (hueco prolongado), R3 (fin de hueco + 15 s)
HUECOS_BENIGNOS = ('arranque', 'lock_tomado', 'conexion')        # R5: cualquier otro evento de binance_huecos_<D>.csv excluye su hora
def eventos_huecos(d, day0):
    """R5: filas de binance_huecos_<D>.csv con evento NO benigno -> [(evento, segundo_del_dia)]; None si el fichero no existe (missing != 'sin eventos')."""
    f = DL + f'binance_huecos_{d}.csv'
    if not os.path.exists(f): return None
    h = pd.read_csv(f, dtype={'evento': str}); out = []
    for e, t in zip(h.evento.values, h.t_ms.values):
        if str(e) in HUECOS_BENIGNOS or not (t == t): continue
        sd = (int(t) - day0) // 1000
        if 0 <= sd < 86400: out.append((str(e), int(sd)))
    return out
def salud_binance(d, bad_h, xfile):
    """Ocupacion por segundo y moneda (ticks de recepcion) -> salud_desde_occ (ADDENDUM1: huecos de silencio, no densidad)."""
    day0 = int(pd.Timestamp(d, tz='UTC').timestamp()) * 1000; occ = {c: np.zeros(86400, bool) for c in COINS}; n = {c: 0 for c in COINS}
    for ch in pd.read_csv(xfile, header=None, usecols=[2, 7], names=['sym', 'recv'], dtype={'sym': 'category', 'recv': 'int64'}, chunksize=1500000):
        for sym, g in ch.groupby('sym', observed=True):
            c = str(sym)[:-4]
            if c not in occ: continue
            s = (g.recv.values - day0) // 1000; s = s[(s >= 0) & (s < 86400)]; occ[c][s] = True; n[c] += len(s)
    return salud_desde_occ(occ, n, bad_h, eventos_huecos(d, day0))
def horas_de_mercado(fin):
    """horas UTC (0-23) de [fin-300, fin] de cada mercado (fin en segundos): las dos que mira engine.sane -> (h_apertura, h_cierre)."""
    f = np.asarray(fin, np.int64); return ((f - 300) // 3600) % 24, (f // 3600) % 24
def mascara_excluidas(fin, horas):
    """True donde el mercado cae en una hora excluida (apertura o cierre), identico a engine.sane con _EXTRA_BAD = horas (ADDENDUM3 (a): la exclusion de Binance es un FILTRO posterior)."""
    h1, h2 = horas_de_mercado(fin); hs = [int(h) for h in horas]; return np.isin(h1, hs) | np.isin(h2, hs)
def _huecos_de(occ_bool, G):
    """[(s1, s2)] pares de segundos ocupados consecutivos con s2 - s1 > G; los bordes del dia cuentan (0 y 86400), como en el criterio anterior. Precision 1 s."""
    idx = np.flatnonzero(occ_bool); a = np.concatenate([[0], idx, [86400]]); dd = np.diff(a); m = dd > G
    return [(int(x), int(y)) for x, y in zip(a[:-1][m], a[1:][m])]
def _horas(s1, s2):
    """R3: horas UTC que contiene [inicio del hueco, fin del hueco + 15 s]."""
    return set(range(int(s1) // 3600, min(int(s2) + PAD_FIN, 86399) // 3600 + 1))
def _excl(occ, sanas, G, ev):
    U = np.zeros(86400, bool)
    for c in COINS: U |= occ[c]
    por_moneda = {c: _huecos_de(occ[c], G) for c in COINS}; un = _huecos_de(U, G_UNION); un_largo = _huecos_de(U, G_UNION_LARGO)
    hs = set(); [hs.update(_horas(a, b)) for gs in por_moneda.values() for a, b in gs]; [hs.update(_horas(a, b)) for a, b in un]
    he = set(); [he.update(_horas(sd, sd)) for _, sd in (ev or [])]
    h300 = set(); [h300.update(_horas(a, b)) for a, b in un_largo]
    S = set(sanas); return dict(hueco=sorted(hs & S), eventos=sorted(he & S), union300=sorted(h300 & S), n_moneda={c: len(g) for c, g in por_moneda.items()}, n_union=len(un),
                                max_gap_s={c: int(np.diff(np.concatenate([[0], np.flatnonzero(occ[c]), [86400]])).max()) for c in COINS})
def salud_desde_occ(occ, n, bad_h, eventos=None):
    """ADDENDUM1 (sha ADD1_SHA). R1: cobertura solo informativa. R2: hueco por moneda > 30 s o de la UNION > 10 s (ticks de recepcion, 1 s de precision, bordes del dia incluidos).
    R3: sale la HORA que contiene [inicio, fin+15 s]. R5: eventos no benignos de binance_huecos (eventos=None = fichero ausente -> se anota, no se inventa). R4 (lectura ADDENDUM3 §B, borrador del validator): cuentan SOLO las horas excluidas por Binance (<= 3 por hueco/evento y <= 2 con hueco de union > 300 s); las horas bad tx_ws salen sin
    mas (B2) y el dia cuenta si quedan >= MIN_HORAS_DIA (12) horas tras tx_ws y Binance (B3). R6: se guardan las horas excluidas con G=15 y G=60 (sensibilidad, informativa)."""
    sanas = [h for h in range(24) if h not in set(bad_h)]; hsec = np.repeat(np.arange(24), 3600)
    ev = _excl(occ, sanas, G_COIN, eventos); excl = sorted(set(ev['hueco']) | set(ev['eventos'])); resto = [h for h in sanas if h not in excl]; m = np.isin(hsec, resto)
    cov = {c: (float(occ[c][m].mean()) if m.any() else float('nan')) for c in COINS}; mn = min(cov.values()) if resto else float('nan')
    alt = {str(G): sorted(set(_excl(occ, sanas, G, eventos)['hueco']) | set(ev['eventos'])) for G in (15, 60)}
    mot = []
    if len(resto) < MIN_HORAS_DIA: mot.append(f'quedan {len(resto)} horas tras tx_ws y Binance < {MIN_HORAS_DIA}')
    if len(ev['union300']) > 2: mot.append(f"{len(ev['union300'])} horas con hueco de union > {G_UNION_LARGO} s (> 2)")
    if len(excl) >= 4: mot.append(f'{len(excl)} horas excluidas por hueco (>= 4)')
    return dict(regla='ADDENDUM1', lectura_r4='ADDENDUM3-B', addendum1_sha=ADD1_SHA, horas_sanas=len(sanas), horas_bad_txws=sorted(set(bad_h)), horas_restantes=len(resto), horas_excluidas=excl, horas_excluidas_hueco=excl, horas_excluidas_eventos=ev['eventos'], horas_hueco_union_gt300s=ev['union300'],
                huecos_por_moneda_gt30s=ev['n_moneda'], huecos_union_gt10s=ev['n_union'], max_gap_s=ev['max_gap_s'], huecos_csv=('ausente' if eventos is None else f'{len(eventos)} eventos no benignos'),
                excl_sensibilidad_R6=alt, cobertura=cov, cobertura_min=mn, ticks=n, valido=not mot, motivo='; '.join('Binance ' + x for x in mot))
# ------------------------------------------------------------------ parche de passT
def extraer_rt():
    src = open(RT).read(); assert sha_f(RT) == SHA['RT'], 'rt_sim.py distinto del registrado'; tree = ast.parse(src); keep = []
    for n_ in tree.body:
        if isinstance(n_, ast.FunctionDef) and n_.name in ('qall', 'mid_at', 'cross_events', 'fill_v'): keep.append(n_)
    assert len(keep) == 4, 'no encuentro qall/mid_at/cross_events/fill_v en rt_sim.py'
    return compile(ast.Module(keep, []), 'rt_sim_funciones', 'exec')
REEMPL = [  # (viejo, nuevo): cada viejo debe aparecer EXACTAMENTE una vez en passT.py
    ("def first_after(arr, t0, t1):", "_DBH = _db_prepare(globals())\ndef first_after(arr, t0, t1):"),
    ("E.tape = G.Tape('chain', D, tp.drop(columns=['k', 'tm'])); KEY = {}", "_TPX = tp[['k', 'tx', 'log_index', 'tm']].copy(); E.tape = G.Tape('chain', D, tp.drop(columns=['k', 'tm'])); KEY = {}"),
    ("q, tf, _ = E.run_segment(k, L, t_arr, t_end, rem, 'BASE')", "q, tf = _FVX(k, L, t_arr, t_end, rem)"),
    ("        for name in VN:\n            can, cf = specs[name]\n", "        specs.update(_DB_SPECS(k, L, g, base, Gm, coin, lado, tq))\n        for name in VN:\n            can, cf = specs[name]; _SETFV(name)\n"),
    ("            for (si, t, t_arr, t_end, q, tf, canc) in run_var(k, L, g, can, Gm, fin, cf):\n", "            for (si, t, t_arr, t_end, q, tf, canc) in run_var(k, L, g, can, Gm, fin, cf):\n                _ACC(name, t_arr, t_end, k)\n"),
]
def parchear(vn):
    assert sha_f(PT) == SHA['PT'], 'passT.py distinto del registrado'; assert sha_f(ENG) == SHA['ENG'], 'engine.py distinto del registrado'
    src = open(PT).read()
    for a, b in REEMPL:
        assert src.count(a) == 1, f'marca no encontrada (o repetida) en passT.py: {a[:60]!r}'; src = src.replace(a, b)
    src, n = re.subn(r"^VN = .*$", "VN = list(_VN)", src, flags=re.M); assert n == 1, 'no encuentro VN'
    return src
class Ctx:
    """Estado compartido entre el codigo parcheado de passT y el arnes (triggers por moneda/token, modelo de relleno, vida de las ordenes)."""
    def __init__(s, d, seed=None): s.d = d; s.seed = seed; s.fv = 'BASE'; s.vida = {}; s._pr = {}; s.ns = None; s.miss_pla = 0
    def prepare(s, g):
        s.ns = g; D = s.D = g['D']; XS = g['XS']; bnr = g['bnr']; s.day0 = int(g['day0']); s.TR = {}
        for coin in COINS:
            A = XS.get(coin)
            if A is None: s.TR[coin] = dict(up=np.empty(0, np.int64), dn=np.empty(0, np.int64)); continue
            t = A[0]
            with np.errstate(invalid='ignore'): r1 = bnr(coin, t, WIN_MS)
            up = t[r1 >= TRIG_BP]; dn = t[r1 <= -TRIG_BP]
            if s.seed is not None: sh = shift_ms(s.seed, s.d); up = circ_shift(up, s.day0, sh); dn = circ_shift(dn, s.day0, sh)
            s.TR[coin] = dict(up=up, dn=dn)
        s.kmap = {(D.act[i], int(D.fin[i]), D.lado[i]): i for i in range(len(D.toks)) if D.marco[i] == '5min'}
        return True
    def _side(s, kk, sd):
        D = s.D
        if kk is None: return np.empty(0, np.int64)
        a, b = D.tb[kk], D.tb[kk + 1]; return D.tt[a:b][D.tsd[a:b] == sd].astype(np.int64)
    def prints(s, k):
        """(contra L, a favor de L) por recepcion WS: contra = el tomador VENDE L (tsd 0 en k) o COMPRA el complementario (tsd 1 en comp); a favor = el opuesto (inversion)."""
        if k in s._pr: return s._pr[k]
        kc = s.D.comp(k); ag = union_sorted(s._side(k, 0), s._side(kc, 1)); fa = union_sorted(s._side(k, 1), s._side(kc, 0)); s._pr[k] = (ag, fa); return s._pr[k]
    def prints_placebo(s, k):
        """DB2 placebo: prints contra L del MISMO activo y lado de otro cierre del mismo dia (desfase entero de cierres), alineados por tiempo hasta el cierre."""
        D = s.D; act = D.act[k]; fin = int(D.fin[k]); lado = D.lado[k]; opp = 'NO' if lado == 'YES' else 'YES'; f0 = s.day0 // 1000
        f2 = f0 + ((fin - f0 + 300 * koff(s.seed, s.d)) % 86400)
        k2 = s.kmap.get((act, f2, lado)); kc2 = s.kmap.get((act, f2, opp))
        if k2 is None or kc2 is None: s.miss_pla += 1; return np.empty(0, np.int64)
        return np.sort(union_sorted(s._side(k2, 0), s._side(kc2, 1)) + (fin - f2) * 1000)
    def db_specs(s, k, L, g, base, Gm, coin, lado, tq):
        TR = s.TR[coin]; adv = TR['dn'] if lado == 'YES' else TR['up']; fav = TR['up'] if lado == 'YES' else TR['dn']
        def canc(tr, l):
            def f(t0, t1):
                tb = first_after(tr, t0, t1); return None if tb is None else tb + l
            return f
        out = {}
        if s.seed is not None:
            out['PDB1_150'] = (base & ~recent(adv, tq), canc(adv, 150)); p2 = s.prints_placebo(k); out['PDB2_150'] = (base & ~recent(p2, tq), canc(p2, 150)); return out
        ag, fa = s.prints(k); trs = dict(DB1=adv, DB2=ag, DBU=union_sorted(adv, ag), INV1=fav, INV2=fa)
        for a, ls in LSPEC.items():
            for l in ls: out[f'{a}_{l}'] = (base & ~recent(trs[a], tq), canc(trs[a], l))
        out['G0'] = (base, None)
        for a in ARMS_FV:
            for f in FVS: out[f'{a}@{f}'] = out[a]
        return out
    def setfv(s, name): s.fv = name.split('@')[1] if '@' in name else 'BASE'
    def acc(s, name, t_arr, t_end, k):
        """vida (ms de orden viva) por (variante, mercado, lado): vida[variante]['ACT|fin|LADO'] (apartado C: P(relleno) x EV|relleno, dPnL incondicional)."""
        key = f'{s.D.act[k]}|{int(s.D.fin[k])}|{s.D.lado[k]}'; v = s.vida.setdefault(name, {}); v[key] = v.get(key, 0) + int(t_end - t_arr)
    def fvx(s, k, L, t_arr, t_end, rem): return s.ns['fill_v'](k, L, t_arr, t_end, rem, s.fv)
# ------------------------------------------------------------------ extras (sec. 6): rafaga, markout, valor de salida; validacion del lado del print (sec. 2 DB2)
def cargar_chain(d, D):
    """filas MAKER del on-chain (taker != contrato del exchange) de tokens 5m del dia -> DataFrame(tx, li, bloque, taker, side, kidx, pr, sz, ts_ms)."""
    f = DL + f'onchain_fills_{d}.csv.gz'
    if not os.path.exists(f): return None
    out = []; cols = ['tipo', 'bloque', 'ts_est', 'tx', 'log_index', 'taker', 'side', 'token_id', 'maker_amt', 'taker_amt']
    for ch in pd.read_csv(f, usecols=cols, dtype={'token_id': str, 'taker': str, 'tx': str}, chunksize=1000000):
        ch = ch[(ch.tipo == 'F') & ~ch.taker.isin(CHAIN_CONTRACTS)]; ch = ch.assign(kidx=ch.token_id.map(D.tokidx)); ch = ch[ch.kidx.notna()]
        if len(ch): out.append(ch)
    if not out: return pd.DataFrame()
    C = pd.concat(out, ignore_index=True); C['kidx'] = C.kidx.astype(int); s0 = C.side.values == 0
    C['pr'] = np.where(s0, C.maker_amt / C.taker_amt, C.taker_amt / C.maker_amt); C['sz'] = np.where(s0, C.taker_amt, C.maker_amt); C['ts_ms'] = (C.ts_est * 1000).astype('int64')
    return C.rename(columns={'log_index': 'li'})
def validar_lado(C, D, ks):
    """concordancia del lado del print WS (tsd: 0 = tomador vende) con el on-chain (fila maker: side 0 = bid => tomador vende) por (token, precio, tamano) y hora <= 10 s."""
    if C is None or not len(C): return dict(n_ws=0, n_match=0, concordancia=float('nan'), valido=False, motivo='sin on-chain')
    kset = set(ks); m = np.isin(D.tk, list(kset)); W = pd.DataFrame(dict(kidx=D.tk[m].astype('int64'), t=D.tt[m].astype('int64'), pr=np.round(D.tp[m].astype(np.float64), 2), sz=np.round(D.tsz[m].astype(np.float64), 2), sd=D.tsd[m]))
    Cc = C[C.kidx.isin(kset)].assign(pr=lambda x: x.pr.round(2), sz=lambda x: x.sz.round(2))[['kidx', 'pr', 'sz', 'ts_ms', 'side']].sort_values('ts_ms'); W = W.sort_values('t')
    M = pd.merge_asof(W, Cc, left_on='t', right_on='ts_ms', by=['kidx', 'pr', 'sz'], direction='nearest', tolerance=10000); ok = M.side.notna(); conc = float((M.sd[ok] == M.side[ok]).mean()) if ok.any() else float('nan')
    return dict(n_ws=int(len(W)), n_match=int(ok.sum()), tasa_match=float(ok.mean()) if len(W) else float('nan'), concordancia=conc, valido=bool(ok.sum() >= 1000 and conc == conc and conc >= 0.95),
                motivo='' if (ok.sum() >= 1000 and conc == conc and conc >= 0.95) else f'lado del print: concordancia {conc} con {int(ok.sum())} casados (< 0,95 o < 1000)')
TICK = 0.01
def sv_delta(q, bid, bsz, gana, propios=(), tick=TICK):
    """pnl(vender al mejor bid) - pnl(mantener a resolucion): acciones vendibles = min(q, profundidad visible) con minimo 5 acciones; comision de tomador 0,07*p*(1-p) por accion (feeSchedule cripto).
    El bid se redondea al tick (ruido float). Autocruce: si el bid redondeado cae en un nivel de NUESTRA escalera (`propios`) el mejor bid puede ser nuestra propia orden (no se casa consigo misma): conservador, delta 0 (mantener)."""
    bt = round(round(float(bid) / tick) * tick, 6)
    if not (bt > 0.0) or bt in {round(float(x), 6) for x in propios}: return 0.0
    qs = np.floor(min(q, bsz) * 100 + 1e-9) / 100
    return 0.0 if qs < 5.0 - 1e-9 else float(qs * (bt - gana) - 0.07 * bt * (1 - bt) * qs)
def extras(ns, R, C):
    """columnas extra de R (variantes planas, BASE): pnl_nr/reb, burst (sec. 6), mk1/mk5/mk30 (mid de L a +1/+5/+30 s menos el precio de relleno), sv150/500/1000 (pnl(vender al mejor bid en tf+delta) - pnl(mantener))."""
    D = ns['D']; TPX = ns['_TPX']; propios = tuple(getattr(ns.get('G'), 'LEVELS', ())); R['pnl_nr'] = R.q * (R.gana - R.L); R['reb'] = R.pnl - R.pnl_nr
    if len(R) == 0:
        for c in ('burst', 'burst_known', 'mk1', 'mk5', 'mk30', 'sv150', 'sv500', 'sv1000'): R[c] = []
        return R
    if C is not None and len(C):
        Cb = C[(C.side == 0) & (C.pr <= BAND_MAX + 0.0049)].copy(); Cb['mid'] = Cb.kidx.map(lambda i: D.mid[i]); nt = Cb.groupby(['bloque', 'mid']).taker.nunique(); rafagas = set(nt[nt >= 2].index)
        bl = {(a, b): c for a, b, c in zip(C.tx.values, C.li.values, C.bloque.values)}; idx = {}
        for kk, tx, li, tm in zip(TPX.k.values, TPX.tx.values, TPX.log_index.values, TPX.tm.values): idx.setdefault((int(kk), int(tm)), []).append((tx, li))
    else: rafagas = set(); bl = {}; idx = {}
    cols = {c: [] for c in ('burst', 'burst_known', 'mk1', 'mk5', 'mk30', 'sv150', 'sv500', 'sv1000')}
    for r in R.itertuples():
        k = int(r.k); tf = int(r.tf); rows = idx.get((k, tf), []); bks = [bl.get((a, b)) for a, b in rows]
        kn = any(x is not None for x in bks); cols['burst_known'].append(kn); cols['burst'].append(float(any((x, D.mid[k]) in rafagas for x in bks if x is not None)) if kn else float('nan'))   # burst DESCONOCIDO = NaN, no False
        for nm, dt_ in (('mk1', 1000), ('mk5', 5000), ('mk30', 30000)):
            b = D.book(k, tf + dt_); cols[nm].append(((b[0] + b[1]) / 2 - r.L) if (b is not None and np.isfinite(b[0]) and np.isfinite(b[1])) else np.nan)
        for nm, dt_ in (('sv150', 150), ('sv500', 500), ('sv1000', 1000)):
            b = D.book(k, tf + dt_)
            if b is None: cols[nm].append(np.nan); continue      # sin libro = dato FALTANTE (no 0)
            if not np.isfinite(b[0]) or b[0] <= 0.0: cols[nm].append(0.0); continue      # libro sin bid = no se puede vender: delta 0
            cols[nm].append(sv_delta(float(r.q), float(b[0]), float(b[2]), float(r.gana), propios))
    for c, v in cols.items(): R[c] = v
    return R
# ------------------------------------------------------------------ ejecucion
def fichero_ficticio(od):
    """passT.py calcula OUT = dirname(__file__) + '/out/': el __file__ ficticio debe colgar del PADRE de `od` (od = .../out/) para que OUT == od (bug 10-Nov: con od + 'passdb_run.py' salia .../out/out/)."""
    return os.path.dirname(os.path.dirname(od)) + '/passdb_run.py'
def correr(d, seed=None):
    T0 = time.time(); main = seed is None; od = HERE + 'out/' if main else HERE + f'placebo/s{seed}/out/'; os.makedirs(od, exist_ok=True)
    if os.path.exists(od + f'RX_{d}.pkl'): print('ya', d, seed); return
    for f in (od + f'RT_{d}.pkl', od + f'SEGT_{d}.pkl'):
        if os.path.exists(f): os.remove(f)    # restos de una corrida interrumpida (la clave de idempotencia es RX_<D>.pkl)
    sys.path.insert(0, Q11 + 'barrido_multi'); import bfeat
    PBd = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/precursores_barrido/out/'
    if main:
        badj = json.load(open(PBd + f'bad_{d}.json'))['bad']; bad_h = [int(h) for dd, h in badj if dd == d]; xf = bfeat.xfile(d)
        if not xf: raise SystemExit(f'ERROR_DATOS: falta x_{d}')
        sal = salud_binance(d, bad_h, xf); excl = {'dia': d, 'horas_excluidas': sal['horas_excluidas']}; atomic_json(HERE + f'out/excl_{d}.json', excl)
    else:
        sal = None
    ctx = Ctx(d, seed); vn = MAIN_VN if main else PLA_VN
    check_band(niveles_desde_fuente())
    src = parchear(vn); sys.argv = ['passT.py', d]
    ns = {'__file__': fichero_ficticio(od), '__name__': '__main__', '_VN': vn, '_db_prepare': ctx.prepare, '_DB_SPECS': ctx.db_specs,
          '_SETFV': ctx.setfv, '_ACC': ctx.acc, '_FVX': ctx.fvx}
    exec(extraer_rt(), ns)    # qall, mid_at, cross_events, fill_v (rt_sim.py, sin editar) en el mismo espacio que passT
    exec(compile(src, 'passT_parcheado', 'exec'), ns)
    R = ns['R']; D = ns['D']; E = ns['E']; ks = ns['ks']; check_band(tuple(ns['G'].LEVELS), R)
    R = R.copy(); R['pnl_nr'] = R.q * (R.gana - R.L); R['reb'] = R.pnl - R.pnl_nr
    if main:
        C = cargar_chain(d, D); Rp = R[~R['var'].str.contains('@')].copy(); Rp = extras(ns, Rp, C); Rc = R[R['var'].str.contains('@')]
        R = pd.concat([Rp, Rc], ignore_index=True)
        hx = excl['horas_excluidas']; fuera = lambda k: not bool(mascara_excluidas([int(D.fin[k])], hx)[0])      # la exclusion de Binance se aplica DESPUES (filtro), RX trae todas las horas buenas de tx_ws
        tot = [k for k in E.ks if E.sane(k) == 'ok' and fuera(k)]; ksf = [k for k in ks if fuera(k)]; vl = validar_lado(C, D, ksf)
        cov = dict(dia=d, tokens_ok=len(tot), tokens_con_desenlace=len(ksf), cobertura_desenlace=(len(ksf) / len(tot) if tot else float('nan')), binance=sal, lado_print=vl,
                   burst_known=float(Rp.burst_known.mean()) if len(Rp) else float('nan'), segundos=round(time.time() - T0, 1),
                   eval_sha=sha_f(__file__))
        atomic_json(HERE + f'out/cov_{d}.json', cov); atomic_json(HERE + f'out/vida_{d}.json', ctx.vida)
    else: atomic_json(od + f'cov_{d}.json', dict(dia=d, seed=seed, fills_no_emparejables=ctx.miss_pla, segundos=round(time.time() - T0, 1)))
    tmp = od + f'RX_{d}.pkl.tmp'; R.to_pickle(tmp); os.replace(tmp, od + f'RX_{d}.pkl')
    for f in (od + f'RT_{d}.pkl', od + f'SEGT_{d}.pkl'):
        if os.path.exists(f): os.remove(f)
    print('ok', d, seed, {v: (len(x), round(float(x.pnl.sum()), 1)) for v, x in R.groupby('var', sort=False) if '@' not in v}, round(time.time() - T0, 1), 's', flush=True)
if __name__ == '__main__':
    a = sys.argv[1:]
    if a[0] == 'test': parchear(MAIN_VN); extraer_rt(); print('parches OK sobre passT.py/rt_sim.py registrados; variantes:', len(MAIN_VN))
    elif a[0] == 'dia': assert re.fullmatch(r'\d{4}-\d\d-\d\d', a[1]); correr(a[1])
    elif a[0] == 'placebo': assert re.fullmatch(r'\d{4}-\d\d-\d\d', a[1]); correr(a[1], int(a[2]))
