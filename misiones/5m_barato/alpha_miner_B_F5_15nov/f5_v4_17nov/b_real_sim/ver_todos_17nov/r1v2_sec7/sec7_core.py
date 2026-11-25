#!/usr/bin/env python3
"""sec7_core.py -- R1v2 sec.7 (a): CANAL BLOQUEO del replay de B + censo por canal + F5_t + cordura de octubre.
Solo calculo. 0 ordenes, 0 red, 0 escritura en data/. No lee tasas evento-placebo ni mide EV de R1v2.

Diseno (sin copiar codigo del motor):
 * El motor vigente (passT_v4: engine_v4.DayEngV4 + stamp_v3 'v3d', construido por eng_v5.build) y el simulador de la politica real de B (b_policy_sim.run_day) NO se tocan.
   `EngineBloqueo` ENVUELVE al motor (delegacion por __getattr__) y solo sobreescribe run_segment. b_policy_sim.run_day ya acepta un motor (E=...). Con `activo=False`
   (POR DEFECTO) run_segment devuelve EXACTAMENTE lo del motor: resultados previos intactos (test_flag_apagado_identico).
 * Canal bloqueo (R1v2_DISENO sec.7a): mientras la puja virtual (token propio, precio L) vive, el primer instante en que (i) bid del complementario >= 1-L, o (ii) ask propio <= L,
   pasa de FALSO a VERDADERO por una fila q con la puja ya llegada, SIN relleno por print previo -> relleno de B con tamano min(restante, tamano del nivel visible).
   Detalles de reloj (todo declarado):
     - estado = ultima fila q de cada token con RECEPCION (rx) <= t (nunca el futuro); candidatos = filas de cualquiera de los dos tokens cuya sello EXCHANGE esta en (t_arr, t_end]
       (la puja existe en el exchange), evaluadas en su rx. Fecha del relleno = rx de la fila (NUNCA bloque on-chain ni timestamp firmado). t_ex se guarda solo para ORDENAR frente a prints.
     - 'sin print previo': el print del motor (reloj exchange tf) gana si tf <= t_ex del evento. Si el bloqueo es anterior, manda el bloqueo (cantidad = min(restante, nivel); los prints
       posteriores NO completan el resto: cota conservadora en cantidad, el primer relleno cierra la puja en b_policy_sim).
     - condicion ya cierta en la llegada (estado exchange <= t_arr): no es evento (la orden seria taker/rechazada); se cuenta en info['ya_cumplido_llegada'].
     - libros cruzados (bid>ask en el MISMO token) -> condicion falsa, contado; dato ausente (NaN/<=0) -> falso, contado (NUNCA se imputa a 0 ni a 1). `excluir_igual` (bid==ask, 'bloqueado') opcional.
     - deltas/ordenes propias: la orden propia vive en el bid del token propio; (i) usa el bid del COMPLEMENTARIO y (ii) el ask propio, luego no entra en ninguna de las dos por construccion.
   LIMITES que NO se pueden resolver con L1 (declarados, no ocultos): el tamano de la orden en reposo es el del NIVEL top (cota superior: incluye otros makers); el L1 no distingue una orden en reposo
   de un nivel previo; rx-ex mezcla relojes (el bloqueo se fecha en rx, los prints en exchange: sesgo <= suelo rx-ex, 20-40 ms)."""
import sys, os, json, hashlib
from collections import Counter, OrderedDict
import numpy as np

HV = os.path.dirname(os.path.abspath(__file__)) + '/'
BR = os.path.dirname(HV.rstrip('/')) .rstrip('/') + '/'                       # ver_todos_17nov/
BSIM = os.path.dirname(BR.rstrip('/')).rstrip('/') + '/'                        # b_real_sim/
FLOOR = 1e-3            # = engine_v4.FLOOR (test_floor_igual_motor lo comprueba)
TOL = 1e-6              # tolerancia de precio (float32 del npz); = engine.EPS
TOLP = 0.0049           # = engine.TOLP (print en nivel vs por debajo)
C0, C1 = 3.526360511779785, 4.717426776885986          # cortes F5_t congelados (CONTRATO_R1v2_19nov_v2 sec.2)
MAX_AGE_MS = 30000      # antiguedad maxima del estado para F5_t (sec.2)
CANALES = ('print_nivel', 'TT', 'bloqueo')


class SerieL1:
    """Filas q (L1 con tamanos) de UN token, ordenadas por RECEPCION (estable). Arrays alineados: rx, ex (ms absolutos), bid, ask, bsz, asz (float64).
    Filas sin rx se excluyen y se cuentan (n_sin_rx): NO se imputan. Indice auxiliar por exchange para elegir candidatos sin suponer |rx-ex| acotado."""
    def __init__(s, rx, ex, bid, ask, bsz, asz, n_sin_rx=0):
        rx = np.asarray(rx, np.int64); o = np.argsort(rx, kind='stable')
        s.rx = rx[o]; s.ex = np.asarray(ex, np.int64)[o]
        s.bid = np.asarray(bid, np.float64)[o]; s.ask = np.asarray(ask, np.float64)[o]; s.bsz = np.asarray(bsz, np.float64)[o]; s.asz = np.asarray(asz, np.float64)[o]
        s.n_sin_rx = int(n_sin_rx); oe = np.argsort(s.ex, kind='stable'); s._exs = s.ex[oe]; s._exi = oe
    def __len__(s): return len(s.rx)
    def idx_rx(s, t):
        """posicion de la ultima fila con rx <= t (-1 si ninguna): el unico estado conocible en t."""
        return int(np.searchsorted(s.rx, t, side='right')) - 1
    def idx_ex(s, t):
        """posicion de la fila con el mayor sello exchange <= t (estado del exchange en t, solo para la condicion 'ya cumplida en la llegada')."""
        j = int(np.searchsorted(s._exs, t, side='right')) - 1
        return int(s._exi[j]) if j >= 0 else -1
    def cand(s, t0, t1):
        """posiciones (por rx) de las filas con ex en (t0, t1]."""
        a = int(np.searchsorted(s._exs, t0, side='right')); b = int(np.searchsorted(s._exs, t1, side='right'))
        return s._exi[a:b]


def serie_de_dia(D, k):
    """SerieL1 del token k desde la vista de RELLENO (exchange) del motor, con la recepcion de cada fila (D._otro, relativo a D.t0; -1 = sin rx)."""
    a, b = int(D.qb[k]), int(D.qb[k + 1])
    if b <= a: return SerieL1([], [], [], [], [], [])
    rel = np.asarray(D._otro[a:b], np.int64); ok = rel >= 0
    return SerieL1(rel[ok] + int(D.t0), np.asarray(D.qt[a:b], np.int64)[ok], D.v0[a:b][ok], D.v1[a:b][ok], D.v2[a:b][ok], D.v3[a:b][ok], n_sin_rx=int((~ok).sum()))


def _valido(bid, ask):
    """(libro utilizable, motivo). NaN/<=0 = sin dato (no se imputa); bid>ask = cruzado."""
    if not (np.isfinite(bid) and np.isfinite(ask)) or bid <= 0 or ask <= 0: return False, 'sin_dato'
    if bid > ask + TOL: return False, 'cruzado'
    return True, ''


def condicion(own, comp, io, ic, L, excluir_igual=False, cont=None):
    """Evalua (i)/(ii) con los estados io (token propio) e ic (complementario) YA elegidos (posiciones por rx o -1). -> (tipo, tamano_nivel) con tipo in {'', 'i', 'ii', 'i+ii'}."""
    cont = cont if cont is not None else Counter()
    if io < 0 or ic < 0: cont['sin_dato'] += 1; return '', 0.0
    vo, mo = _valido(own.bid[io], own.ask[io]); vc, mc = _valido(comp.bid[ic], comp.ask[ic])
    for v, m in ((vo, mo), (vc, mc)):
        if not v: cont[m] += 1
    if excluir_igual:
        if own.bid[io] >= own.ask[io] - TOL and vo: cont['bloqueado_igual'] += 1; vo = False
        if comp.bid[ic] >= comp.ask[ic] - TOL and vc: cont['bloqueado_igual'] += 1; vc = False
    ti = vc and comp.bid[ic] >= (1.0 - L) - TOL                       # (i) bid del complementario >= 1-L
    tii = vo and own.ask[io] <= L + TOL                               # (ii) ask propio <= L
    tipo = 'i+ii' if (ti and tii) else ('i' if ti else ('ii' if tii else ''))
    tam = 0.0
    if ti: tam = max(tam, float(comp.bsz[ic]))
    if tii: tam = max(tam, float(own.asz[io]))
    return tipo, tam


def primer_bloqueo(own, comp, L, t_arr, t_end, rem, excluir_igual=False, info=None):
    """Primer instante (rx) en (t_arr, t_end] con la puja viva donde (i)/(ii) pasa de falso a verdadero. -> dict(t_rx, t_ex, tipo, q, nivel) o None.
    q = min(rem, tamano del nivel visible); si q < FLOOR no hay relleno (info['sin_tamano']). Solo datos con rx <= t_rx en el estado (sin futuro)."""
    info = info if info is not None else Counter()
    if t_end <= t_arr: return None
    prev = condicion(own, comp, own.idx_ex(t_arr), comp.idx_ex(t_arr), L, excluir_igual, Counter())[0] != ''
    if prev: info['ya_cumplido_llegada'] += 1
    rows = [(int(own.rx[i]), int(own.ex[i])) for i in own.cand(t_arr, t_end)] + [(int(comp.rx[i]), int(comp.ex[i])) for i in comp.cand(t_arr, t_end)]
    if not rows: return None
    rows.sort()
    seen = set()
    for (t, ex) in rows:
        if t in seen: continue
        seen.add(t)
        tipo, tam = condicion(own, comp, own.idx_rx(t), comp.idx_rx(t), L, excluir_igual, info)
        cond = tipo != ''
        if cond and not prev:
            q = min(float(rem), tam)
            if q >= FLOOR: return dict(t_rx=int(t), t_ex=int(ex), tipo=tipo, q=float(q), nivel=float(tam))
            info['sin_tamano'] += 1
        prev = cond
    return None


def clasifica_print(prints, L, tf, win=100, tolp=TOLP):
    """Canal de un relleno por print en (k, L, tf): 'TT' si el/los prints del relleno (t en [tf, tf+win], la ventana de emparejado de engine_v4) estan POR DEBAJO de L, 'print_nivel' si en L,
    'print_nd' si no se localiza (p. ej. tf de una fila L1 emparejada sin print en la ventana)."""
    if prints is None: return 'print_nd'
    pt, pp = np.asarray(prints[0], np.int64), np.asarray(prints[1], float)
    m = (pt >= tf) & (pt <= tf + win)
    if not m.any(): return 'print_nd'
    return 'TT' if (pp[m] < L - tolp).any() else 'print_nivel'


class EngineBloqueo:
    """Envuelve un motor (DayEngV4 o un stub con run_segment/D/K/ks/sane/capt). activo=False => identidad. Registra el canal de cada relleno en self.fills[(k, L4, t_arr, tf)]."""
    def __init__(self, E, activo=False, fuente=None, excluir_igual=False, cache_max=256):
        self._E = E; self.activo = bool(activo); self.excluir_igual = excluir_igual
        self.fuente = fuente or self._fuente_motor; self._cache = OrderedDict(); self._cmax = cache_max
        self.fills = {}; self.cont = Counter()
    def __getattr__(self, n):
        if n.startswith('__') or n in ('_E',): raise AttributeError(n)
        return getattr(self._E, n)
    def _serie(self, k):
        if k in self._cache: self._cache.move_to_end(k); return self._cache[k]
        s = serie_de_dia(self._E.D, k); self._cache[k] = s
        if len(self._cache) > self._cmax: self._cache.popitem(last=False)
        return s
    def _fuente_motor(self, k):
        kc = self._E.D.comp(k)
        return (self._serie(k), self._serie(kc)) if kc is not None else (None, None)
    def run_segment(self, k, L, t_arr, t_end, rem, variant):
        q, tf, why = self._E.run_segment(k, L, t_arr, t_end, rem, variant)
        if not self.activo: return q, tf, why
        self.cont['llamadas'] += 1
        from_print = (tf is not None and q > 0)
        own, comp = self.fuente(k)
        ev = None
        if own is not None and comp is not None and why not in ('sin_libro', 'seria_taker'):
            ev = primer_bloqueo(own, comp, L, t_arr, t_end, rem, self.excluir_igual, self.cont)
        elif own is not None and comp is not None: self.cont['sin_libro_o_taker_' + why] += 1
        if ev is not None and (not from_print or ev['t_ex'] < tf):
            self.fills[(int(k), round(float(L), 4), int(t_arr), int(ev['t_rx']))] = dict(canal='bloqueo', tipo=ev['tipo'], q=ev['q'], t_rx=ev['t_rx'], t_ex=ev['t_ex'], nivel=ev['nivel'])
            self.cont['bloqueo_fill'] += 1
            return float(ev['q']), int(ev['t_rx']), 'ok'
        if ev is not None: self.cont['bloqueo_ignorado_print_previo'] += 1
        if from_print:
            try: canal = clasifica_print(self._E.tape.get(k, L, t_arr, t_end), L, int(tf))
            except Exception: canal = 'print_nd'
            self.fills[(int(k), round(float(L), 4), int(t_arr), int(tf))] = dict(canal=canal, q=float(q), t_ex=int(tf))
            self.cont['fill_' + canal] += 1
        return q, tf, why


# ------------------------------------------------------------------ F5_t y censo
def f5t(own, t, max_age=MAX_AGE_MS):
    """F5_t = log1p(tamano del ask de NUESTRO token, ultimo estado con rx <= t, antiguedad <= 30 s). None = invalido (= no operar); nunca se imputa."""
    i = own.idx_rx(t) if own is not None else -1
    if i < 0: return None
    if t - int(own.rx[i]) > max_age: return None
    a = own.asz[i]
    if not np.isfinite(a) or a < 0: return None
    return float(np.log1p(a))


def tercil(v):
    """bajo <= C0 < medio <= C1 < alto (convencion de solo_observable_19nov/so2_f5t.py); inval si v is None."""
    if v is None: return 'inval'
    return 'bajo' if v <= C0 else ('medio' if v <= C1 else 'alto')


def anota_ordenes(R, wrapper, series_por_k):
    """R: DataFrame de b_policy_sim (cols k, L, t_arr, tf, q, t_dec, coin, mid, dia?). Devuelve copia con canal (solo rellenos), F5_t y tercil. series_por_k(k)->SerieL1 propio."""
    import pandas as pd
    R = R.copy(); canal = []; f5 = []; terc = []
    for r in R.itertuples():
        if r.q > 0:
            c = wrapper.fills.get((int(r.k), round(float(r.L), 4), int(r.t_arr), int(r.tf)), {}).get('canal', 'sin_registro')
        else: c = ''
        canal.append(c); v = f5t(series_por_k(int(r.k)), int(r.t_dec)); f5.append(np.nan if v is None else v); terc.append(tercil(v))
    R['canal'] = canal; R['f5t'] = f5; R['tercil'] = terc
    return R


def censo(R, por=('dia', 'coin', 'tercil')):
    """Censo de ORDENES y rellenos simulados por canal (print_nivel / TT / bloqueo) y por tercil. Solo conteos, acciones y P(relleno): sin pnl, sin EV."""
    import pandas as pd
    R = R.copy(); R['_fill'] = (R.q > 0).astype(int)
    out = []
    por = [c for c in por if c in R.columns]
    for key, g in R.groupby(por, dropna=False):
        key = key if isinstance(key, tuple) else (key,)
        row = dict(zip(por, key)); row['n_ordenes'] = int(len(g)); row['n_rellenos'] = int(g._fill.sum()); row['p_relleno'] = float(g._fill.mean()) if len(g) else float('nan')
        for c in CANALES + ('print_nd', 'sin_registro'): row['n_' + c] = int((g.canal == c).sum())
        out.append(row)
    return out


# ------------------------------------------------------------------ cordura de octubre
CORDURA_MAX_FRAC = 0.005    # PROPUESTA del ingeniero (el diseno dice solo '~0'): violaciones / ventanas <= 0,5 %. El chief la confirma o la cambia ANTES de ver resultados.
def cordura(ventanas, fuente, tol_dt_ms=250, excluir_igual=False):
    """Cordura (sec.7a): con la orden REAL viva, el canal bloqueo debe dar ~0 eventos salvo dt~0 junto al relleno real.
    ventanas: iterable de dict(dia, coin, k, L, t_arr, t_end, rem, real_tm3 (NaN/None si no hubo relleno real)). fuente(k)->(own, comp). Un evento con |t_ex - real_tm3| <= tol_dt_ms es 'dt0' (permitido);
    cualquier otro es VIOLACION. Para ventanas con relleno real la busqueda se corta en real_tm3 + tol_dt (la orden ya no esta viva despues). Devuelve (filas por dia x coin, resumen)."""
    import pandas as pd
    filas = []; info = Counter()
    for w in ventanas:
        own, comp = fuente(w['k']); r = dict(dia=w['dia'], coin=w['coin'], ventana=1, evento=0, dt0=0, violacion=0, sin_serie=0)
        if own is None or comp is None: r['sin_serie'] = 1; filas.append(r); continue
        tm3 = w.get('real_tm3'); tiene = tm3 is not None and np.isfinite(tm3)
        t_end = min(w['t_end'], int(tm3) + tol_dt_ms) if tiene else w['t_end']
        ev = primer_bloqueo(own, comp, w['L'], int(w['t_arr']), int(t_end), float(w.get('rem', 5.0)), excluir_igual, info)
        if ev is not None:
            r['evento'] = 1
            if tiene and abs(ev['t_ex'] - tm3) <= tol_dt_ms: r['dt0'] = 1
            else: r['violacion'] = 1
        filas.append(r)
    df = pd.DataFrame(filas)
    if not len(df): return [], dict(n_ventanas=0, status='BLOCKED', motivo='sin ventanas')
    g = df.groupby(['dia', 'coin']).sum(numeric_only=True).reset_index()
    n = int(df.ventana.sum()); viol = int(df.violacion.sum()); frac = viol / n if n else float('nan')
    res = dict(n_ventanas=n, n_eventos=int(df.evento.sum()), n_dt0=int(df.dt0.sum()), n_violaciones=viol, frac_violacion=frac, max_frac=CORDURA_MAX_FRAC,
               sin_serie=int(df.sin_serie.sum()), contadores=dict(info), pasa=bool(n and frac <= CORDURA_MAX_FRAC and df.sin_serie.sum() == 0))
    return g.to_dict('records'), res


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''): h.update(b)
    return h.hexdigest()


# ------------------------------------------------------------------ suelo rx-ex causal por ventana (para clasificar los TP por lo/hi/indet)
D_LO, D_HI = -50, 400       # = suelo_causal.D_LO/D_HI (bins de 1 ms); test_suelo_bins_igual lo comprueba
BIN_MS = 10_000; W_HALF_MS = 300_000


def suelo_por_coin(D, coin):
    """(rx, d) ordenados por rx de TODAS las filas q con rx valido de los tokens del coin en el dia; d = rx - ex (ms). Sin imputar las filas sin rx."""
    rel = np.asarray(D._otro, np.int64); qk = np.asarray(D.qk); acts = np.asarray([str(a).lower() for a in D.act], object)
    ok = (rel >= 0) & (acts[qk] == str(coin).lower())
    rx = rel[ok] + int(D.t0); d = rx - np.asarray(D.qt, np.int64)[ok]; o = np.argsort(rx, kind='stable')
    return rx[o], d[o]


def hist_d(rx, d, t0, t1):
    """histograma (451 bins) de d para filas con rx en [t0, t1)."""
    a, b = int(np.searchsorted(rx, t0, side='left')), int(np.searchsorted(rx, t1, side='left')); x = d[a:b]
    x = x[(x >= D_LO) & (x <= D_HI)]
    return np.bincount((x - D_LO).astype(np.int64), minlength=D_HI - D_LO + 1)


def clase_suelo_en(rx, d, t):
    """clase causal (lo/hi/indet) con SOLO bins de 10 s completos anteriores a t: h1 = [B-600 s, B-300 s), h2 = [B-300 s, B), B = floor(t/10 s)*10 s."""
    from sec7_calculos import clase_suelo_ventana
    B = (int(t) // BIN_MS) * BIN_MS
    return clase_suelo_ventana(hist_d(rx, d, B - 2 * W_HALF_MS, B - W_HALF_MS), hist_d(rx, d, B - W_HALF_MS, B))[0]
