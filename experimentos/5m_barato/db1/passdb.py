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
# ------------------------------------------------------------------ salud Binance (sec. 4)
def salud_binance(d, bad_h, xfile):
    """Cobertura por moneda (segundos de horas sanas con >=1 tick de recepcion) y huecos de la UNION de las 3 monedas > 60 s: las horas que cruza un hueco salen (sec. 4). -> dict (valido si min cobertura >= 0,95)."""
    day0 = int(pd.Timestamp(d, tz='UTC').timestamp()) * 1000; occ = {c: np.zeros(86400, bool) for c in COINS}; n = {c: 0 for c in COINS}
    for ch in pd.read_csv(xfile, header=None, usecols=[2, 7], names=['sym', 'recv'], dtype={'sym': 'category', 'recv': 'int64'}, chunksize=1500000):
        for sym, g in ch.groupby('sym', observed=True):
            c = str(sym)[:-4]
            if c not in occ: continue
            s = (g.recv.values - day0) // 1000; s = s[(s >= 0) & (s < 86400)]; occ[c][s] = True; n[c] += len(s)
    return salud_desde_occ(occ, n, bad_h)
def salud_desde_occ(occ, n, bad_h):
    sanas = [h for h in range(24) if h not in set(bad_h)]; U = np.zeros(86400, bool)
    for c in COINS: U |= occ[c]
    hsec = np.repeat(np.arange(24), 3600); excl = set(); huecos = []; i = 0
    while i < 86400:
        if U[i]: i += 1; continue
        j = i
        while j < 86400 and not U[j]: j += 1
        if j - i > 60:
            hs = sorted(set(hsec[i:j].tolist()) & set(sanas)); huecos.append((int(i), int(j), hs)); excl |= set(hs)
        i = j
    resto = [h for h in sanas if h not in excl]; m = np.isin(hsec, resto)
    cov = {c: (float(occ[c][m].mean()) if m.any() else float('nan')) for c in COINS}
    mn = min(cov.values()) if resto else float('nan')
    return dict(horas_sanas=len(sanas), horas_excluidas=sorted(excl), huecos_union_gt60s=len(huecos), cobertura=cov, cobertura_min=mn, ticks=n,
                valido=bool(resto and mn == mn and mn >= 0.95), motivo='' if (resto and mn == mn and mn >= 0.95) else f'Binance bnreg cobertura min {mn} < 0,95 o sin horas sanas')
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
    ("bad = {tuple(x) for x in json.load(open(PB + f'bad_{d}.json'))['bad']}", "bad = {tuple(x) for x in json.load(open(PB + f'bad_{d}.json'))['bad']} | _EXTRA_BAD"),
    ("q, tf, _ = E.run_segment(k, L, t_arr, t_end, rem, 'BASE')", "q, tf = _FVX(k, L, t_arr, t_end, rem)"),
    ("        for name in VN:\n            can, cf = specs[name]\n", "        specs.update(_DB_SPECS(k, L, g, base, Gm, coin, lado, tq))\n        for name in VN:\n            can, cf = specs[name]; _SETFV(name)\n"),
    ("            for (si, t, t_arr, t_end, q, tf, canc) in run_var(k, L, g, can, Gm, fin, cf):\n", "            for (si, t, t_arr, t_end, q, tf, canc) in run_var(k, L, g, can, Gm, fin, cf):\n                _ACC(name, t_arr, t_end)\n"),
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
    def acc(s, name, t_arr, t_end): s.vida[name] = s.vida.get(name, 0) + int(t_end - t_arr)
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
    kset = set(ks); m = np.isin(D.tk, list(kset)); W = pd.DataFrame(dict(kidx=D.tk[m], t=D.tt[m].astype('int64'), pr=np.round(D.tp[m].astype(np.float64), 2), sz=np.round(D.tsz[m].astype(np.float64), 2), sd=D.tsd[m]))
    Cc = C[C.kidx.isin(kset)].assign(pr=lambda x: x.pr.round(2), sz=lambda x: x.sz.round(2))[['kidx', 'pr', 'sz', 'ts_ms', 'side']].sort_values('ts_ms'); W = W.sort_values('t')
    M = pd.merge_asof(W, Cc, left_on='t', right_on='ts_ms', by=['kidx', 'pr', 'sz'], direction='nearest', tolerance=10000); ok = M.side.notna(); conc = float((M.sd[ok] == M.side[ok]).mean()) if ok.any() else float('nan')
    return dict(n_ws=int(len(W)), n_match=int(ok.sum()), tasa_match=float(ok.mean()) if len(W) else float('nan'), concordancia=conc, valido=bool(ok.sum() >= 1000 and conc == conc and conc >= 0.95),
                motivo='' if (ok.sum() >= 1000 and conc == conc and conc >= 0.95) else f'lado del print: concordancia {conc} con {int(ok.sum())} casados (< 0,95 o < 1000)')
def sv_delta(q, bid, bsz, gana):
    """pnl(vender al mejor bid) - pnl(mantener a resolucion): acciones vendibles = min(q, profundidad visible) con minimo 5 acciones; comision de tomador 0,07*p*(1-p) por accion (feeSchedule cripto); bid en rejilla de tick."""
    qs = np.floor(min(q, bsz) * 100 + 1e-9) / 100
    return 0.0 if qs < 5.0 - 1e-9 else float(qs * (bid - gana) - 0.07 * bid * (1 - bid) * qs)
def extras(ns, R, C):
    """columnas extra de R (variantes planas, BASE): pnl_nr/reb, burst (sec. 6), mk1/mk5/mk30 (mid de L a +1/+5/+30 s menos el precio de relleno), sv150/500/1000 (pnl(vender al mejor bid en tf+delta) - pnl(mantener))."""
    D = ns['D']; TPX = ns['_TPX']; R['pnl_nr'] = R.q * (R.gana - R.L); R['reb'] = R.pnl - R.pnl_nr
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
        cols['burst_known'].append(any(x is not None for x in bks)); cols['burst'].append(any((x, D.mid[k]) in rafagas for x in bks if x is not None))
        for nm, dt_ in (('mk1', 1000), ('mk5', 5000), ('mk30', 30000)):
            b = D.book(k, tf + dt_); cols[nm].append(((b[0] + b[1]) / 2 - r.L) if (b is not None and np.isfinite(b[0]) and np.isfinite(b[1])) else np.nan)
        for nm, dt_ in (('sv150', 150), ('sv500', 500), ('sv1000', 1000)):
            b = D.book(k, tf + dt_)
            if b is None or not np.isfinite(b[0]) or b[0] <= 0.0: cols[nm].append(0.0); continue
            cols[nm].append(sv_delta(float(r.q), float(b[0]), float(b[2]), float(r.gana)))
    for c, v in cols.items(): R[c] = v
    return R
# ------------------------------------------------------------------ ejecucion
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
        sal = None; excl = json.load(open(HERE + f'out/excl_{d}.json'))
    ctx = Ctx(d, seed); vn = MAIN_VN if main else PLA_VN
    src = parchear(vn); sys.argv = ['passT.py', d]
    ns = {'__file__': od + 'passdb_run.py', '__name__': '__main__', '_VN': vn, '_EXTRA_BAD': {(d, int(h)) for h in excl['horas_excluidas']}, '_db_prepare': ctx.prepare, '_DB_SPECS': ctx.db_specs,
          '_SETFV': ctx.setfv, '_ACC': ctx.acc, '_FVX': ctx.fvx}
    exec(extraer_rt(), ns)    # qall, mid_at, cross_events, fill_v (rt_sim.py, sin editar) en el mismo espacio que passT
    exec(compile(src, 'passT_parcheado', 'exec'), ns)
    R = ns['R']; D = ns['D']; E = ns['E']; ks = ns['ks']
    R = R.copy(); R['pnl_nr'] = R.q * (R.gana - R.L); R['reb'] = R.pnl - R.pnl_nr
    if main:
        C = cargar_chain(d, D); Rp = R[~R['var'].str.contains('@')].copy(); Rp = extras(ns, Rp, C); Rc = R[R['var'].str.contains('@')]
        R = pd.concat([Rp, Rc], ignore_index=True)
        tot = [k for k in E.ks if E.sane(k) == 'ok']; vl = validar_lado(C, D, ks)
        cov = dict(dia=d, tokens_ok=len(tot), tokens_con_desenlace=len(ks), cobertura_desenlace=(len(ks) / len(tot) if tot else float('nan')), binance=sal, lado_print=vl,
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
