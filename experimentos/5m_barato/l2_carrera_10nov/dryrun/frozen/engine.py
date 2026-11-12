#!/usr/bin/env python3
"""H-AR-ESCALERA-TAPE: motor de simulacion (DEV, solo lectura de datalogs, 0 ordenes). Especificacion congelada en PREREG.md.
Funciones puras (fill_segment, segments, jumps) probadas en test_engine.py con fixtures; la capa Day usa capt.Day (sa_ms, recepcion)."""
import sys, numpy as np, pandas as pd
P2 = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/'
LAT_POST = 68; LAT_CANC = 60; GRID = 500; TMIN = 61; EPS = 1e-6; TOLP = 0.0049
LEVELS = (0.10, 0.13, 0.16, 0.19); SIZE = 5.0
GATE = dict(lvl=0.03, vol=26.0, hora=4)
JUMP_TH = 2.0; JUMP_REARM_MS = 1000; A3_COINS = ('SOL', 'XRP')
VARIANTS = ('CONS', 'BASE', 'OPT')
INF = float('inf')

# ---------------------------------------------------------------- relleno de un segmento (orden viva de t_arr a t_end)
def fill_segment(book_arr, xa, qupd, prints, L, t_arr, t_end, rem, variant):
    """book_arr: (bid,ask,bsz,asz) vigente en t_arr o None. xa: tamano del ask complementario a 1-L (0 si no coincide).
    qupd: (t, v0, v2) cotizaciones DENTRO de (t_arr, t_end]. prints: (t, price, size) ventas contra bids con price<=L+TOLP en (t_arr, t_end].
    Devuelve (qty, t_primer_relleno, motivo). Cola por delante (acciones):
      OPT  = 0.   CONS = tamano visible en L si es el mejor bid (+ ask complementario), 0 si L mejora el bid, INF si L esta por debajo (solo barridos).
      BASE = como CONS sin complemento, y cuando L pasa a ser el mejor bid (o lo es) la cola se acota a min(cola, tamano visible) (variante K: cancelaciones).
    Print por debajo de L = barrido: relleno completo. Print en L consume cola y luego rellena."""
    if book_arr is None: return 0.0, None, 'sin_libro'
    bid, ask, bsz, _ = book_arr
    if not (ask > L + EPS): return 0.0, None, 'seria_taker'
    top = abs(bid - L) < EPS
    if variant == 'OPT': ahead = 0.0
    elif bid > L + EPS: ahead = INF
    elif top: ahead = bsz + (xa if variant == 'CONS' else 0.0)
    else: ahead = xa if variant == 'CONS' else 0.0
    evs = []
    if variant == 'BASE':
        qt, v0, v2 = qupd
        for j in np.where(np.abs(np.asarray(v0, float) - L) < EPS)[0]: evs.append((int(qt[j]), 0, float(v2[j])))
    pt, pp, ps = prints
    for j in range(len(pt)): evs.append((int(pt[j]), 1, (float(pp[j]), float(ps[j]))))
    evs.sort(key=lambda e: (e[0], e[1]))
    if variant == 'BASE' and top: ahead = min(ahead, bsz)
    qty = 0.0; tf = None
    for (t, kind, v) in evs:
        if kind == 0:
            ahead = min(ahead, v); continue
        q, s = v
        if q < L - TOLP: g = rem - qty; qty += g; tf = t if tf is None else tf; break
        if abs(q - L) <= TOLP:
            if ahead >= s - 1e-9: ahead -= s
            else:
                g = min(rem - qty, s - ahead); ahead = 0.0; qty += g; tf = t if tf is None else tf
                if qty >= rem - 1e-9: break
    return qty, tf, 'ok'

# ---------------------------------------------------------------- segmentos (independientes de la variante de relleno)
def blocked(t, jt):
    """True si hay salto adverso en (t-1000, t]."""
    if jt is None or len(jt) == 0: return False
    i = np.searchsorted(jt, t, side='right') - 1
    return i >= 0 and jt[i] > t - JUMP_REARM_MS

def segments(grid, can_arm, G, fin, jt=None):
    """grid ms; can_arm[i]: se puede armar en i (gate + ask>L); G[i]: gate vigente (si cae -> cancelar en grid+60). jt: tiempos ms de saltos adversos (ordenados) o None.
    Devuelve lista (t_dec, t_arr, t_end). Rearme permitido; sin reponer hasta 1 s sin salto. Fin duro (fin-TMIN)*1000+LAT_CANC."""
    n = len(grid); out = []; hard = (fin - TMIN) * 1000 + LAT_CANC
    falsos = np.where(~G)[0]
    i = 0
    while i < n:
        if not can_arm[i] or blocked(int(grid[i]), jt): i += 1; continue
        t_dec = int(grid[i]); t_arr = t_dec + LAT_POST
        j = falsos[np.searchsorted(falsos, i + 1)] if np.searchsorted(falsos, i + 1) < len(falsos) else n
        t_end = int(grid[j]) + LAT_CANC if j < n else hard
        t_end = min(t_end, hard)
        if jt is not None and len(jt):
            k = np.searchsorted(jt, t_dec, side='left')       # primer salto con t_j >= t_dec
            if k < len(jt) and jt[k] + LAT_CANC < t_end: t_end = int(jt[k]) + LAT_CANC
        if t_end > t_arr: out.append((t_dec, t_arr, t_end))
        i = max(i + 1, int(np.searchsorted(grid, t_end)))
    return out

# ---------------------------------------------------------------- saltos de Binance (RECEPCION), regla H-A3-CANCEL v1
def jumps(t, p, th=JUMP_TH):
    """t ms recepcion (ordenado), p precio. Salto = |p/p(ultimo recibido <= t-100 ms) - 1| >= th bps; refractario 1 s. Devuelve (t_salto, signo)."""
    t = np.asarray(t, np.int64); p = np.asarray(p, float)
    j0 = np.searchsorted(t, t - 100, side='right') - 1; ok = j0 >= 0
    ret = np.where(ok, (p / p[np.maximum(j0, 0)] - 1) * 1e4, 0.0)
    cand = np.where(np.abs(ret) >= th)[0]; ts = []; sg = []; last = -10**15
    for i in cand:
        if t[i] - last < 1000: continue
        last = t[i]; ts.append(int(t[i])); sg.append(np.sign(ret[i]))
    return np.array(ts, np.int64), np.array(sg)

def vol30_vec(tt, S, times):
    """tt: tiempos de trades del token (ordenados), S: suma acumulada propia con S[0]=0 (S[i]=suma de las i primeras). Acciones en (t-30 s, t]."""
    i1 = np.searchsorted(tt, times, side='right'); i0 = np.searchsorted(tt, times - 30000, side='right')
    return S[i1] - S[i0]

# ---------------------------------------------------------------- capa de datos (capt.Day + cinta)
def load_capt():
    sys.path.insert(0, P2 + 'capturabilidad_A_R1ws'); import capt
    return capt

class Tape:
    """Cinta de ventas contra bids por token: arrays (t ms recepcion, price, size). modo 'chain' (maker fills side=0 on-chain, t = recv de libro5_tx) o 'ws' (D.prints)."""
    def __init__(self, mode, D=None, chain=None):
        self.mode = mode; self.D = D; self.by = {}
        if mode == 'chain':
            c = chain[chain.side == 0].sort_values(['t_ws_ms', 'tx', 'log_index'])
            for tok, g in c.groupby('token_id'):
                k = D.tokidx.get(str(tok))
                if k is None: continue
                self.by[k] = (g.t_ws_ms.values.astype(np.int64), g.price.values.astype(float), g.sh.values.astype(float))
    def get(self, k, L, t0, t1):
        if self.mode == 'ws':
            pr = self.D.prints(k, L, t0, t1)
            return (np.array([r[0] for r in pr], np.int64), np.array([r[1] for r in pr], float), np.array([r[2] for r in pr], float))
        a = self.by.get(k)
        if a is None: return (np.empty(0, np.int64), np.empty(0), np.empty(0))
        tt, pp, ss = a; i0 = np.searchsorted(tt, t0, side='right'); i1 = np.searchsorted(tt, t1, side='right')
        m = pp[i0:i1] <= L + TOLP
        return tt[i0:i1][m], pp[i0:i1][m], ss[i0:i1][m]

class DayEng:
    def __init__(self, d, tape_mode, chain=None, bad_hours=None, universe=('ETH', 'SOL', 'XRP')):
        self.capt = load_capt(); self.d = d; D = self.D = self.capt.Day(d)
        self.tape = Tape(tape_mode, D, chain); self.bad = bad_hours or set()
        self.day0 = int(pd.Timestamp(d, tz='UTC').timestamp()) * 1000; self.day1 = self.day0 + 86400000
        self.ks = [k for k in range(len(D.toks)) if D.marco[k] == '5min' and D.act[k] in universe]
        # suma acumulada propia por token (corrige la resta de cs global de capt.vol30 cuando no hay trade previo en la ventana)
        self.S = {}
    def _S(self, k):
        if k not in self.S:
            D = self.D; a, b = D.tb[k], D.tb[k + 1]
            self.S[k] = np.concatenate([[0.0], np.cumsum(D.tsz[a:b].astype(np.float64))])
        return self.S[k]
    def quotes(self, k, times):
        D = self.D; a, b = D.qb[k], D.qb[k + 1]
        if b <= a: return np.full(len(times), np.nan), np.full(len(times), np.nan)
        j = np.searchsorted(D.qt[a:b], times, side='right') - 1; ok = j >= 0; jj = np.where(ok, j, 0)
        return np.where(ok, D.v0[a + jj], np.nan).astype(float), np.where(ok, D.v1[a + jj], np.nan).astype(float)
    def grid(self, k): return np.arange((int(self.D.fin[k]) - 300) * 1000, (int(self.D.fin[k]) - TMIN) * 1000 + 1, GRID)
    def feats(self, k):
        """Vectores en la rejilla de 500 ms: bid, ask, b15 (bid 15m del mismo lado), vol30 (acciones de ambos tokens 5m), hora UTC."""
        D = self.D; g = self.grid(k); fin = int(D.fin[k])
        bid, ask = self.quotes(k, g)
        f15 = int(np.ceil(fin / 900.0) * 900); k15 = D.t15.get((D.act[k], f15, D.lado[k]))
        b15 = self.quotes(k15, g)[0] if k15 is not None else np.full(len(g), np.nan)
        vol = np.zeros(len(g))
        for kk in (k, D.comp(k)):
            if kk is None: continue
            a, b = D.tb[kk], D.tb[kk + 1]
            if b > a: vol += vol30_vec(D.tt[a:b], self._S(kk), g)
        hora = (g // 3600000) % 24
        return g, bid, ask, b15, vol, hora
    def sane(self, k):
        """Mercado utilizable: entero dentro del dia, comp existe, libro con >=2 cotizaciones, ninguna hora 'mala' en [fin-300, fin]."""
        D = self.D; fin = int(D.fin[k]); t0 = (fin - 300) * 1000
        if t0 < self.day0 or fin * 1000 > self.day1: return 'borde'
        if D.comp(k) is None: return 'sin_comp'
        if D.qb[k + 1] - D.qb[k] < 2: return 'sin_libro'
        for h in {pd.Timestamp(t0, unit='ms', tz='UTC'), pd.Timestamp(fin * 1000, unit='ms', tz='UTC')}:
            if self.bad and (h.strftime('%Y-%m-%d'), h.hour) in self.bad: return 'hora_mala'
        return 'ok'
    def xa(self, k, L, t):
        kX = self.D.comp(k)
        if kX is None: return 0.0
        bx = self.D.book(kX, t)
        return float(bx[3]) if bx is not None and abs(bx[1] - (1 - L)) < TOLP else 0.0
    def qupd(self, k, t0, t1):
        D = self.D; a, b = D.qb[k], D.qb[k + 1]; qt = D.qt[a:b]; i0 = np.searchsorted(qt, t0, side='right'); i1 = np.searchsorted(qt, t1, side='right')
        return qt[i0:i1], D.v0[a + i0:a + i1], D.v2[a + i0:a + i1]
    def run_segment(self, k, L, t_arr, t_end, rem, variant):
        return fill_segment(self.D.book(k, t_arr), self.xa(k, L, t_arr) if variant == 'CONS' else 0.0, self.qupd(k, t_arr, t_end) if variant == 'BASE' else None,
                            self.tape.get(k, L, t_arr, t_end), L, t_arr, t_end, rem, variant)

def gate_vec(mode, L, b15, vol, hora):
    base = np.isfinite(b15) & (vol >= GATE['vol']) & (hora >= GATE['hora'])
    with np.errstate(invalid='ignore'): lv = (b15 - L) <= GATE['lvl'] + EPS
    if mode == 'U': return np.ones(len(b15), bool)
    if mode == 'INV': return base & ~lv
    return base & lv          # G, G0, PLA

def adverse_jumps(J, coin, lado):
    """J: dict coin -> (t, signo). Salto adverso para YES = baja (signo<0); para NO = sube."""
    if coin not in J: return None
    t, s = J[coin]; return t[(s < 0)] if lado == 'YES' else t[(s > 0)]

def run_ladder(E, J, mode, d, a3_on=True, pla_seed=None, cov=None):
    """Una pasada del escalon completo para un modo ('G','G0','U','INV','PLA'). Devuelve DataFrame de rellenos (qty>0) y contadores."""
    D = E.D; rows = []; cnt = dict(tokens=0, posts=0, skip={}); feats = {}
    ks = []
    for k in E.ks:
        s = E.sane(k)
        if s != 'ok': cnt['skip'][s] = cnt['skip'].get(s, 0) + 1; continue
        if capt_outcome(E, k) is None: cnt['skip']['sin_desenlace'] = cnt['skip'].get('sin_desenlace', 0) + 1; continue
        ks.append(k)
    for k in ks: feats[k] = E.feats(k)
    src = {k: k for k in ks}
    if mode == 'PLA':       # gate aleatorizado dia x moneda x lado: b15 y vol30 de OTRO mercado de la misma moneda y lado (semilla fija)
        rng = np.random.default_rng(pla_seed)
        grp = {}
        for k in ks: grp.setdefault((D.act[k], D.lado[k]), []).append(k)
        for key, lst in grp.items():
            perm = rng.permutation(len(lst))
            for i, k in enumerate(lst):
                kk = lst[perm[i]]
                if kk == k and len(lst) > 1: kk = lst[(perm[i] + 1) % len(lst)]
                src[k] = kk
    for k in ks:
        g, bid, ask, b15, vol, hora = feats[k]; fin = int(D.fin[k]); gana = capt_outcome(E, k); coin = D.act[k]; lado = D.lado[k]
        if mode == 'PLA':
            _, _, _, b15, vol, _ = feats[src[k]]
        jt = adverse_jumps(J, coin, lado) if (a3_on and coin in A3_COINS and mode != 'G0') else None
        cnt['tokens'] += 1
        for L in LEVELS:
            G = gate_vec(mode, L, b15, vol, hora)
            can = G & np.isfinite(ask) & (ask > L + EPS)
            segs = segments(g, can, G, fin, jt)
            rem = {v: SIZE for v in VARIANTS}; ns = 0
            for si, (t_dec, t_arr, t_end) in enumerate(segs):
                if all(rem[v] <= 1e-9 for v in VARIANTS): break
                ns += 1
                for v in VARIANTS:
                    if rem[v] <= 1e-9: continue
                    q, tf, why = E.run_segment(k, L, t_arr, t_end, rem[v], v)
                    if q > 1e-9:
                        rem[v] -= q
                        rows.append((mode, d, coin, lado, int(D.mid[k]), fin, L, v, si, q, tf, (fin * 1000 - tf) / 1000.0, gana))
            cnt['posts'] += ns
    df = pd.DataFrame(rows, columns=['mode', 'dia', 'act', 'lado', 'mkt', 'fin', 'L', 'var', 'seg', 'q', 't_fill', 'T', 'gana'])
    return df, cnt

def capt_outcome(E, k):
    return E.capt.outcome(E.D, k)

def imitar(E, U, W_s):
    """Puerta registrada: cada unidad de poblacion (primer fill de maker) se imita con una orden de 5 acc a su precio pc, viva desde tf-W hasta tf+1 s (sin gate, sin A3).
    U: columnas token_id, pc, fin, t_ws (recepcion ms), gana, p, c, act, AR. Devuelve DataFrame con qty por variante (0 si no detectado) y motivo de descarte."""
    rows = []; D = E.D
    for r in U.itertuples():
        k = D.tokidx.get(str(r.token_id))
        if k is None or D.marco[k] != '5min': rows.append((r.Index, None, 'sin_token')); continue
        s = E.sane(k)
        if s != 'ok': rows.append((r.Index, None, s)); continue
        L = round(float(r.pc), 2); tf = int(r.t_ws); fin = int(r.fin)
        t_dec = max((fin - 300) * 1000, tf - int(W_s * 1000)); t_arr = t_dec + LAT_POST; t_end = tf + 1000
        if t_end <= t_arr: rows.append((r.Index, None, 'ventana_vacia')); continue
        qs = {v: E.run_segment(k, L, t_arr, t_end, SIZE, v)[0] for v in VARIANTS}
        rows.append((r.Index, qs, 'ok'))
    out = []
    for idx, qs, why in rows:
        out.append(dict(idx=idx, why=why, **({('q_' + v): (qs[v] if qs else np.nan) for v in VARIANTS})))
    return pd.DataFrame(out).set_index('idx')
