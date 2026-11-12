#!/usr/bin/env python3
"""cxb60_core.py -- NUCLEO del dry-run forward de B-CXB60 v1 (DRY_RUN puro: NO firma, NO envia, NO importa py-clob-client, NO toca el ejecutor, 0 ordenes).
Reglas de integridad (mandato Javi 11-Nov):
  * REUTILIZA (import, no copia) las funciones del motor v3: engine.gate_vec / vol30_vec / constantes (LAT_POST, GRID, TMIN, LEVELS, EPS, TOLP), engine_v3.fill_segment_v3 y DayEngV3.run_segment/qupd3 (relleno con dedupe),
    capt.Day.book/prints (cinta WS). Lo unico NUEVO aqui es la maquina de estados INCREMENTAL equivalente a `run_var` de passT_cxb_v3.py (que es batch) y los adaptadores de buffers vivos.
  * RELOJES (CONTRATO_RELOJES.md): las DECISIONES usan RECEPCION (`rx`): bid/ask/b15/vol30/b300 = ultimo mensaje con rx <= t_tick; la MECANICA DE RELLENO (libro en la llegada, cola, prints, cancelacion efectiva) usa EXCHANGE (`ex`).
    t_arr = t_dec + LAT_POST (LOC, supuesto del motor); cancelacion efectiva = rx_disparo + l (l parametro; varios en paralelo).
  * PROCESADO CON RETRASO (lagged): las decisiones solo usan datos con rx <= t_tick (causal), pero se PROCESAN cuando el reloj de flujo W (menor rx reciente de los ficheros leidos) supera el
    instante + SETTLE_MS (2 s por defecto) para que lleguen los mensajes tardios (rx-ex p50 16-18 ms, rafagas de cientos de ms). Es identico a procesar en tiempo real con 2 s de latencia de ESCRITURA; NO mide el
    tiempo real de reaccion de un ejecutor (d_proc), solo registra el coste de computo por evento (benchmark `t_cpu_us`).
  * La unidad de unicidad de resultados es (dia, token, L, variante, seg). Todo identificador de segmento es determinista (reproducible entre reinicios).
Variantes (spec): kind in {'G0' (puede=base, sin cancelar), 'GEO1' (puede=base&arm, sin cancelar = CONTROL de igual colocacion), 'CXB' (puede=base&arm, cancela al ver bid<L, efectiva rx+l), 'PLC' (placebo de igual cobertura:
mismo disparo que CXB60 pero cancelacion en instante uniforme del segmento, semilla s)}. Ver PREREG_CXB60_FORWARD_BORRADOR.md."""
import os, sys, math, json
import numpy as np

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'          # l2_carrera_10nov/ (solo para tests/replay que leen ficheros del motor ORIGINAL)
FROZEN = os.path.dirname(os.path.abspath(__file__)) + '/frozen/'                   # copia CONGELADA del motor v3 (hash en HASHES_CONGELADOS.json; el runner aborta si difiere)
P2 = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/'                 # origen de las copias (ya NO se importa de aqui)
sys.path.insert(0, HERE)                                                           # prioridad baja (los tests importan otros modulos de l2_carrera_10nov)
sys.path.insert(0, FROZEN)                                                         # prioridad maxima: engine/capt/relojes/engine_clock/engine_v3 salen de frozen/
import capt, relojes                                                               # orden importa: relojes y engine importan capt
import engine as G            # constantes y gate_vec/vol30_vec del motor (copia congelada)
import engine_v3 as E3        # fill_segment_v3 + DayEngV3.run_segment/qupd3
for _m in (capt, relojes, G, E3):
    assert os.path.dirname(os.path.abspath(_m.__file__)) + '/' == FROZEN, ('modulo del motor NO procede de frozen/', _m.__file__)

LAT_POST, GRID, TMIN, LEVELS, EPS, TOLP = G.LAT_POST, G.GRID, G.TMIN, G.LEVELS, G.EPS, G.TOLP
SIZE = 5.0; HARD_EXTRA_MS = 60; SETTLE_MS = 2000; C_PRINT = 19                      # C_PRINT: sello de la cinta WS = t_ev - C_PRINT - 1 (c_epoca de stamp_v3: p50 d_ex 18-21 ms; fallback)
REB = 0.2 * 0.07                                                                      # rebate maker (20 % de la comision 0,07*p*(1-p) del tomador), como el motor


# l EMPIRICO (CXBEMP): l_efectivo = PROC_MS + valor del pool de anclas propias (copia congelada l_pool_emp.json, 1.453 valores, p50 40,9 ms, p90 96 ms), UN sorteo por segmento, determinista:
# rng = default_rng([clave_token, round(L*100), n_segmento, 7919]) (no consume estado entre llamadas ni entre reinicios; el original passT_cxb_l.py usaba un rng por (mercado, L) con un sorteo por llamada: misma distribucion, otra secuencia).
POOL_FILE = os.path.dirname(os.path.abspath(__file__)) + '/l_pool_emp.json'
_P = json.load(open(POOL_FILE)); POOL_EMP = np.asarray(_P['valores'], np.int64); PROC_MS = int(_P['proc_ms'])
assert len(POOL_EMP) == _P['n'] >= 1000 and PROC_MS == 3 and POOL_EMP.min() >= 20


def l_emp(token_key, L, seg):
    return PROC_MS + int(POOL_EMP[np.random.default_rng([int(token_key), int(round(L * 100)), int(seg), 7919]).integers(len(POOL_EMP))])


class VSpec:
    def __init__(self, name, kind, l=None, seed=None, ref_l=60):
        assert kind in ('G0', 'GEO1', 'CXB', 'CXBEMP', 'PLC'), kind
        self.name, self.kind, self.l, self.seed, self.ref_l = name, kind, l, seed, ref_l
        self.uses_arm = kind != 'G0'; self.cancels = kind in ('CXB', 'CXBEMP', 'PLC')


def default_specs(l_list=(35, 45, 60, 100, 150), placebo_seeds=20, emp=True):
    s = [VSpec('G0', 'G0'), VSpec('GEO1', 'GEO1')] + [VSpec(f'CXB{l}', 'CXB', l=l) for l in l_list] + ([VSpec('CXBEMP', 'CXBEMP')] if emp else [])
    s += [VSpec(f'PLC60_{i}', 'PLC', seed=i, ref_l=60) for i in range(1, placebo_seeds + 1)]
    return s


# ----------------------------------------------------------------------------------------------------------------------------- buffers vivos
class TokBuf:
    """Buffers por token. q: filas de top del libro en orden de RECEPCION (rx no decreciente; si llega una fila antigua se inserta ordenada, estable). t: trades (rx, ex, price, is_buy, size)."""
    def __init__(self):
        self.qrx, self.qex, self.qbid, self.qask, self.qszb, self.qsza = [], [], [], [], [], []
        self.trx, self.tex, self.tp, self.tbuy, self.tsz = [], [], [], [], []
        self._qa = None; self._ta = None; self.n_q_fuera_de_orden = 0; self.n_t_fuera_de_orden = 0

    def add_q(self, ex, rx, bid, ask, szb, sza):
        if len(self.qrx) and rx < self.qrx[-1]:
            import bisect; i = bisect.bisect_right(self.qrx, rx); self.n_q_fuera_de_orden += 1
            for L_, v in ((self.qrx, rx), (self.qex, ex), (self.qbid, bid), (self.qask, ask), (self.qszb, szb), (self.qsza, sza)): L_.insert(i, v)
        else:
            self.qrx.append(rx); self.qex.append(ex); self.qbid.append(bid); self.qask.append(ask); self.qszb.append(szb); self.qsza.append(sza)
        self._qa = None

    def add_t(self, ex, rx, price, is_buy, size):
        if len(self.trx) and rx < self.trx[-1]:
            import bisect; i = bisect.bisect_right(self.trx, rx); self.n_t_fuera_de_orden += 1
            for L_, v in ((self.trx, rx), (self.tex, ex), (self.tp, price), (self.tbuy, is_buy), (self.tsz, size)): L_.insert(i, v)
        else:
            self.trx.append(rx); self.tex.append(ex); self.tp.append(price); self.tbuy.append(is_buy); self.tsz.append(size)
        self._ta = None

    def qa(self):
        if self._qa is None:
            self._qa = dict(rx=np.asarray(self.qrx, np.int64), ex=np.asarray(self.qex, np.int64), bid=np.asarray(self.qbid, np.float64), ask=np.asarray(self.qask, np.float64),
                            szb=np.asarray(self.qszb, np.float64), sza=np.asarray(self.qsza, np.float64))
        return self._qa

    def ta(self):
        if self._ta is None:
            sz = np.asarray(self.tsz, np.float64)
            self._ta = dict(rx=np.asarray(self.trx, np.int64), ex=np.asarray(self.tex, np.int64), p=np.asarray(self.tp, np.float64), buy=np.asarray(self.tbuy, np.float64), sz=sz, S=np.concatenate([[0.0], np.cumsum(sz)]))
        return self._ta


def quotes_rx(buf, times):
    """(bid, ask) con el ultimo mensaje de rx <= t (misma formula que engine_clock.quotes)."""
    if buf is None or len(buf.qrx) == 0: return np.full(len(times), np.nan), np.full(len(times), np.nan)
    a = buf.qa(); j = np.searchsorted(a['rx'], times, side='right') - 1; ok = j >= 0; jj = np.where(ok, j, 0)
    return np.where(ok, a['bid'][jj], np.nan), np.where(ok, a['ask'][jj], np.nan)


class MiniDay:
    """Objeto con la interfaz minima de capt.Day (EX view) para UN mercado 5m: tokens [k, comp]. Se usa para llamar a capt.Day.book / capt.Day.prints / DayEngV3.qupd3 del motor SIN copiarlos.
    Las filas q se ordenan por EXCHANGE (estable respecto al orden de recepcion); la cinta es la WS (trades) con sello tm = ex - C_PRINT - 1 (misma convencion de fallback que stamp_v3)."""
    def __init__(self, bufs, meta, c_print=C_PRINT):
        self.toks = [m['tok'] for m in meta]; n = len(self.toks)
        self.mid = np.array([m['mid'] for m in meta], object); self.lado = np.array([m['lado'] for m in meta], object); self.marco = np.array(['5min'] * n, object)
        self.act = np.array([m['coin'] for m in meta], object); self.fin = np.array([m['fin'] for m in meta], np.int64)
        self.tokidx = {t: i for i, t in enumerate(self.toks)}; self.t5 = {(self.mid[i], self.lado[i]): i for i in range(n)}; self.t15 = {}
        qs = []; ts = []; self.qb = [0]; self.tb = [0]
        for b in bufs:
            a = b.qa(); o = np.argsort(a['ex'], kind='stable'); qs.append({k: v[o] for k, v in a.items()}); self.qb.append(self.qb[-1] + len(o))
            t = b.ta(); o = np.argsort(t['ex'], kind='stable'); ts.append({k: v[o] for k, v in t.items() if k != 'S'}); self.tb.append(self.tb[-1] + len(o))
        cat = lambda L_, k, dt: np.concatenate([x[k] for x in L_]) if L_ else np.empty(0, dt)
        self.qt = cat(qs, 'ex', np.int64); self.v0 = cat(qs, 'bid', np.float64); self.v1 = cat(qs, 'ask', np.float64); self.v2 = cat(qs, 'szb', np.float64); self.v3 = cat(qs, 'sza', np.float64)
        self.tt = cat(ts, 'ex', np.int64) - c_print - 1; self.tp = cat(ts, 'p', np.float64); self.tsd = cat(ts, 'buy', np.float64); self.tsz = cat(ts, 'sz', np.float64)
        self.qb = np.asarray(self.qb); self.tb = np.asarray(self.tb)

    def comp(self, k): return capt.Day.comp(self, k)
    def book(self, k, t): return capt.Day.book(self, k, t)
    def prints(self, kY, p, t0, t1): return capt.Day.prints(self, kY, p, t0, t1)


class _Eng:
    """Sustituto minimo de DayEngV3 para run_segment/qupd3 (se llaman las funciones UNBOUND del motor con este objeto como self). Solo variante BASE (no se usa xa)."""
    def __init__(self, D):
        self.D = D; self.dedupe = True; self.diag = {}; self.tape = G.Tape('ws', D)
        self.qupd3 = lambda k, L, t0, t1: E3.DayEngV3.qupd3(self, k, L, t0, t1)
    def run_segment(self, k, L, t_arr, t_end, rem, variant='BASE'): return E3.DayEngV3.run_segment(self, k, L, t_arr, t_end, rem, variant)


def make_live_fill(bufs_of, meta_of, c_print=C_PRINT):
    """fill_fn(token, L, t_arr, t_end, rem) -> (q, tf, motivo) con buffers vivos. bufs_of(tok) -> (buf_tok, buf_comp) (comp puede ser TokBuf vacio); meta_of(tok) -> [meta_tok, meta_comp] (dicts tok/mid/lado/coin/fin).
    Reutiliza capt.Day.book/prints y DayEngV3.run_segment (fill_segment_v3, dedupe) del motor; la cinta es la WS (prints) con sello tm = ex - c_print - 1 (supuesto: en el feed vivo no hay libro5_tx ni firma exacta)."""
    cache = {}
    def fill(tok, L, t_arr, t_end, rem):
        bt, bc = bufs_of(tok); key = (tok, len(bt.qrx), len(bt.trx), len(bc.qrx), len(bc.trx))
        if cache.get('k') != key:
            cache['k'] = key; cache['e'] = _Eng(MiniDay([bt, bc], meta_of(tok), c_print))
        return cache['e'].run_segment(0, L, t_arr, t_end, rem, 'BASE')
    return fill


# ----------------------------------------------------------------------------------------------------------------------------- caracteristicas por tick
class TokenFeats:
    """Caracteristicas de decision por tick de la rejilla de 500 ms de un mercado 5m (RECEPCION). Se calculan por trozos conforme llega el reloj de flujo (T_known). Vectorizado con las mismas formulas del motor
    (quotes, vol30_vec, gate_vec). Por nivel L guarda: Gm (gate), code (motivo de no-colocacion base), arm."""
    CODES = {0: 'ok', 1: 'sin_b15', 2: 'vol30_baja', 3: 'hora<4', 4: 'b15-L>0.03', 5: 'ask_nan', 6: 'ask<=L', 7: 'no_arm'}

    def __init__(self, tok, fin, buf, buf_comp, buf15, levels=LEVELS):
        self.tok, self.fin, self.buf, self.buf_comp, self.buf15, self.levels = tok, fin, buf, buf_comp, buf15, tuple(levels)
        self.g = np.arange((fin - 300) * 1000, (fin - TMIN) * 1000 + 1, GRID); self.n = len(self.g); self.m = 0
        self.hard = (fin - TMIN) * 1000 + HARD_EXTRA_MS
        self.bid = np.empty(0); self.ask = np.empty(0); self.b300 = np.empty(0); self.b15 = np.empty(0); self.vol = np.empty(0)
        self.Gm = {L: np.empty(0, bool) for L in levels}; self.code = {L: np.empty(0, np.int8) for L in levels}; self.arm = {L: np.empty(0, bool) for L in levels}

    def extend(self, t_known):
        m1 = int(min(self.n, max(0, math.floor((t_known - self.g[0]) / GRID) + 1))) if t_known >= self.g[0] else 0
        if m1 <= self.m: return
        g = self.g[self.m:m1]; bid, ask = quotes_rx(self.buf, g); b300 = quotes_rx(self.buf, g - 300)[0]
        b15 = quotes_rx(self.buf15, g)[0] if self.buf15 is not None else np.full(len(g), np.nan)
        vol = np.zeros(len(g))
        for b in (self.buf, self.buf_comp):
            if b is None or len(b.trx) == 0: continue
            t = b.ta(); vol += G.vol30_vec(t['rx'], t['S'], g)
        self._apply(g, bid, ask, b300, b15, vol); self.m = m1

    def _apply(self, g, bid, ask, b300, b15, vol):
        """Aplica gate/arm/motivo a un trozo de la rejilla (formulas del motor; punto de inyeccion de los tests de reproduccion)."""
        hora = (g // 3600000) % 24
        self.bid = np.concatenate([self.bid, bid]); self.ask = np.concatenate([self.ask, ask]); self.b300 = np.concatenate([self.b300, b300]); self.b15 = np.concatenate([self.b15, b15]); self.vol = np.concatenate([self.vol, vol])
        for L in self.levels:
            Gm = G.gate_vec('G', L, b15, vol, hora)
            with np.errstate(invalid='ignore'):
                code = np.where(~np.isfinite(b15), 1, np.where(vol < G.GATE['vol'], 2, np.where(hora < G.GATE['hora'], 3, np.where((b15 - L) > G.GATE['lvl'] + EPS, 4, np.where(~np.isfinite(ask), 5, np.where(~(ask > L + EPS), 6, 0))))))
                base = Gm & np.isfinite(ask) & (ask > L + EPS); assert np.array_equal(base, code == 0), 'codigo de motivo inconsistente con gate_vec'
                arm = np.isfinite(b300) & ((b300 - L) >= 0.01 - 1e-6)
            self.Gm[L] = np.concatenate([self.Gm[L], Gm]); self.code[L] = np.concatenate([self.code[L], code.astype(np.int8)]); self.arm[L] = np.concatenate([self.arm[L], arm])


def first_after(arr, t0, t1):
    i = np.searchsorted(arr, t0, side='left'); return int(arr[i]) if i < len(arr) and arr[i] <= t1 else None


class VMachine:
    """Maquina de estados de UN (token, L, variante): equivalente incremental de `run_var` (passT_cxb_v3.py L61-75). step(t_known, fill_fn) avanza todo lo decidible con datos completos hasta t_known y devuelve
    los registros de segmentos cerrados. Sin lookahead: el fin natural (primer tick con gate falso) y el disparo solo se aceptan cuando el flujo ya cubre ese instante."""
    def __init__(self, spec, feats, L, token_key):
        self.spec, self.F, self.L, self.key = spec, feats, L, token_key
        self.i = 0; self.rem = SIZE; self.seg = 0; self.live = None; self.done = False; self.reasons = np.zeros(8, np.int64)
        self.rng = np.random.default_rng(spec.seed * 7919 + (token_key % 1000003) * 31 + int(round(L * 100))) if spec.kind == 'PLC' else None

    def _can_arr(self):
        F = self.F; code = F.code[self.L][:F.m]; c = code == 0
        return (c & F.arm[self.L][:F.m]) if self.spec.uses_arm else c

    def _reason_codes(self, lo, hi):
        F = self.F; code = F.code[self.L][lo:hi].copy()
        if self.spec.uses_arm: code = np.where((code == 0) & ~F.arm[self.L][lo:hi], 7, code)
        return code

    def _trigger(self, t_arr, t1, l, t_known):
        """cancel_fn del motor con datos hasta min(t1, t_known): devuelve instante efectivo de cancelacion o None. cfn(qt, below, l): si el ultimo mensaje rx<=t_arr ya esta por debajo -> t_arr + l; si no, primer mensaje por debajo con
        rx >= t_arr+1 y rx <= t1 -> rx + l."""
        a = self.F.buf.qa(); rx, bid = a['rx'], a['bid']; below = bid < self.L - TOLP
        ix = np.searchsorted(rx, t_arr, side='right') - 1
        if ix >= 0 and below[ix]: return int(t_arr + l), int(t_arr), None
        qb = rx[below]; tb = first_after(qb, t_arr + 1, min(t1, t_known))
        if tb is None: return None, None, None
        j = np.searchsorted(rx, tb, side='left'); ex_tb = int(a['ex'][j + int(np.argmax(below[j:]))]) if j < len(rx) else None
        return int(tb + l), int(tb), ex_tb

    def step(self, t_known, fill_fn):
        F, L, sp = self.F, self.L, self.spec; out = []
        while not self.done:
            if self.live is None:
                if self.i >= F.n or self.rem <= 1e-9: self.done = True; break
                m = F.m
                if self.i >= m: break
                can = self._can_arr()[self.i:]
                if len(can) == 0: break
                nz = np.flatnonzero(can)
                j = self.i + int(nz[0]) if len(nz) else m
                if j > self.i: self.reasons += np.bincount(self._reason_codes(self.i, j), minlength=8)[:8]
                if j >= m: self.i = m; break
                self.i = j; t_dec = int(F.g[j]); self.live = dict(i=j, t_dec=t_dec, t_arr=t_dec + LAT_POST)
            lv = self.live; i0 = lv['i']; t_arr = lv['t_arr']; m = F.m
            rel = np.flatnonzero(~F.Gm[L][i0 + 1:m]); nat = None; nat_reason = None
            if len(rel): nat = min(int(F.g[i0 + 1 + int(rel[0])]) + 60, F.hard); nat_reason = 'gate_falso' if nat < F.hard else 'duro'
            elif m >= F.n: nat = F.hard; nat_reason = 'duro'
            end = None; canc = 0; t_trig_rx = t_trig_ex = None
            if nat is not None and nat <= t_arr: end = nat                                               # sin segmento (motor: t_end <= t_arr no coloca ni llama a cancel_fn)
            elif sp.cancels:
                if sp.kind in ('CXB', 'CXBEMP'):
                    l_eff = sp.l if sp.kind == 'CXB' else l_emp(self.key, L, self.seg)
                    tc, t_trig_rx, t_trig_ex = self._trigger(t_arr, nat if nat is not None else float('inf'), l_eff, t_known)
                    if tc is not None and (nat is None or tc < nat): end, canc = max(tc, t_arr), 1; nat_reason = 'cancel_bid<L'
                    elif nat is not None: end = nat
                else:                                                                                      # PLC: necesita el fin natural y datos hasta el: instante uniforme si el disparo (ref_l) existiria
                    if nat is not None and t_known >= nat:
                        tc, t_trig_rx, t_trig_ex = self._trigger(t_arr, nat, sp.ref_l, t_known); u = self.rng.random()
                        if tc is not None and tc < nat: end, canc = int(t_arr + u * (nat - t_arr)), 1; nat_reason = 'placebo'
                        else: end = nat
            elif nat is not None: end = nat
            if end is None or t_known < end: break                                                         # aun no decidible con datos completos
            rec = None
            if end > t_arr:
                q, tf, why = fill_fn(F.tok, L, t_arr, end, self.rem)
                rec = dict(var=sp.name, tok=F.tok, L=L, seg=self.seg, t_dec_rx=lv['t_dec'], t_arr=t_arr, t_end=int(end), canc=canc, motivo_fin=nat_reason, t_trig_rx=t_trig_rx, t_trig_ex=t_trig_ex, l_eff=(l_eff if sp.kind in ('CXB', 'CXBEMP') and end > t_arr and canc else None),
                           q=float(q), tf=(int(tf) if q > 1e-9 else -1), rem_antes=float(self.rem), why=why)
                self.seg += 1
                if q > 1e-9: self.rem -= q
                out.append(rec)
            self.i = max(lv['i'] + 1, int(np.searchsorted(F.g, end, side='left'))); self.live = None
        return out

    def finalize_reasons(self):
        """Tras el ultimo tick conocido, cuenta los motivos restantes del tramo ocioso (para el resumen por mercado)."""
        return {TokenFeats.CODES[i]: int(c) for i, c in enumerate(self.reasons) if c}


def pnl_of(q, L, gana):
    """PnL de un relleno de q acciones a L (BUY, GTC post-only maker): mismo criterio que el motor (rebate 20 % de la comision)."""
    return q * (gana - L) + q * REB * L * (1 - L)


class Market:
    """Un mercado 5m (un token): sus TokenFeats y sus maquinas (L x variante)."""
    def __init__(self, tok, fin, coin, lado, mid, comp_tok, buf, buf_comp, buf15, specs, levels=LEVELS, F=None):
        self.tok, self.fin, self.coin, self.lado, self.mid, self.comp_tok = tok, fin, coin, lado, mid, comp_tok
        self.F = F if F is not None else TokenFeats(tok, fin, buf, buf_comp, buf15, levels); key = int(tok[-9:]) if tok.isdigit() else abs(hash(tok))
        self.M = [VMachine(sp, self.F, L, key) for L in levels for sp in specs]; self.closed = False

    def advance(self, t_known, fill_fn):
        self.F.extend(t_known); out = []
        for m in self.M: out += m.step(t_known, fill_fn)
        if all(m.done for m in self.M) or t_known >= self.fin * 1000 + 5000:
            for m in self.M:
                if not m.done: m.step(10 ** 18, fill_fn)
            self.closed = True
        return out
