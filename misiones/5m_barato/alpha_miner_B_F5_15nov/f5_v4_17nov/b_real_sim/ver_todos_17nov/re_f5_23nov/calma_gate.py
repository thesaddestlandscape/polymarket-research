#!/usr/bin/env python3
"""Gate de CALMA de H-CALMA-ESC-T1 (PREREG_CALMA_T1.md) como funcion UNICA para simulador, forward y ejecutor. Sin red, sin ordenes.

Definicion (identica a la de escalera_B/engine.py::jumps, que desde Q3 delega aqui):
  salto = |p / p_ref - 1| * 1e4 >= TH_BPS, con p_ref = ultimo trade RECIBIDO con t_recepcion <= t - LOOKBACK_MS (sin referencia -> no hay salto);
  refractario REFRACT_MS entre saltos ACEPTADOS; reloj = RECEPCION en ms (nunca el E de Binance).
Adverso para el lado: YES -> signo<0 (baja), NO -> signo>0 (sube). Armado permitido solo con >= REARM_MS desde el ultimo salto adverso.
Dos implementaciones de la MISMA regla, con igualdad exacta comprobada en test y sobre datos reales (verificar_equivalencia.py):
  jumps(t, p, th)   -> vectorizada (batch: simulador y forward);   JumpDetector.update(t, p) -> streaming (ejecutor).
Fail-closed del ejecutor: CalmaGate.puede_armar() es False si el STREAM de Binance de la moneda esta rancio (> stale_ms sin NINGUN mensaje: aggTrade o bookTicker via vivo()).
OJO: la edad del ultimo aggTrade NO sirve de liveness: medido en x_2026-11-02 (24 h), con > 2 s sin trade el 12,1 % (ETH), 21,0 % (SOL) y 30,8 % (XRP) del tiempo = calma normal; el simulador arma en esos tramos."""
import collections
import numpy as np

TH_BPS = 1.0
LOOKBACK_MS = 100
REFRACT_MS = 1000
REARM_MS = 1000
CANCEL_LAT_MS = 60          # lat. de cancelacion supuesta en el prereg (efectiva +60 ms); el ejecutor real debe MEDIRLA


def adverso(lado, signo):
    """Salto adverso para una puja de compra: YES pierde si el spot baja, NO si sube."""
    return signo < 0 if lado == 'YES' else signo > 0


def jumps(t, p, th=TH_BPS, lookback_ms=LOOKBACK_MS, refract_ms=REFRACT_MS):
    """Batch. t: ms de recepcion (ordenado), p: precio. Devuelve (t_salto int64, signo)."""
    t = np.asarray(t, np.int64); p = np.asarray(p, float)
    if len(t) == 0: return np.array([], np.int64), np.array([])
    j0 = np.searchsorted(t, t - lookback_ms, side='right') - 1; ok = j0 >= 0
    ret = np.where(ok, (p / p[np.maximum(j0, 0)] - 1) * 1e4, 0.0)
    cand = np.where(np.abs(ret) >= th)[0]; ts = []; sg = []; last = -10**15
    for i in cand:
        if t[i] - last < refract_ms: continue
        last = t[i]; ts.append(int(t[i])); sg.append(np.sign(ret[i]))
    return np.array(ts, np.int64), np.array(sg)


def adverse_times(jt, js, lado):
    """Tiempos de saltos adversos para el lado, a partir de (jt, js) de jumps()."""
    jt = np.asarray(jt); js = np.asarray(js)
    return jt[js < 0] if lado == 'YES' else jt[js > 0]


def armable_batch(jt_adv, t, rearm_ms=REARM_MS):
    """Misma regla que make_seg de esc_dec2.py: bloqueado si el ultimo salto adverso <= t esta a menos de rearm_ms (jt > t - rearm)."""
    if len(jt_adv) == 0 or rearm_ms <= 0: return True
    kk = np.searchsorted(jt_adv, t, side='right') - 1
    return not (kk >= 0 and jt_adv[kk] > t - rearm_ms)


class JumpDetector:
    """Streaming equivalente exacto de jumps() para UNA moneda. update(t_ms, px) -> signo (+1/-1) si hay salto aceptado, 0 si no.
    Ticks con t menor que el ultimo se IGNORAN y se cuentan (n_desorden): el batch exige orden, el vivo no debe romperse."""
    def __init__(self, th=TH_BPS, lookback_ms=LOOKBACK_MS, refract_ms=REFRACT_MS):
        self.th, self.lb, self.rf = th, lookback_ms, refract_ms
        self.dq = collections.deque(); self.ref = None; self.last_jump = -10**15; self.t_ult = None; self.n_desorden = 0; self.n_ticks = 0

    def update(self, t, p):
        if self.t_ult is not None and t < self.t_ult: self.n_desorden += 1; return 0
        self.t_ult = t; self.n_ticks += 1
        while self.dq and self.dq[0][0] <= t - self.lb: self.ref = self.dq.popleft()
        self.dq.append((t, p))
        if self.ref is None: return 0
        ret = (p / self.ref[1] - 1) * 1e4
        if abs(ret) < self.th or t - self.last_jump < self.rf: return 0
        self.last_jump = t
        return 1 if ret > 0 else -1


class CalmaGate:
    """Estado del gate para el ejecutor: un JumpDetector por moneda + ultimo salto adverso por (moneda, lado).
    on_tick(coin, t, px) -> signo del salto o 0. cancelar_si(coin, lado, signo) -> bool. puede_armar(coin, lado, t) -> bool (fail-closed)."""
    def __init__(self, coins, th=TH_BPS, rearm_ms=REARM_MS, stale_ms=2000):
        self.det = {c: JumpDetector(th) for c in coins}; self.rearm = rearm_ms; self.stale = stale_ms
        self.adv = {}; self.t_tick = {}

    def vivo(self, coin, t):
        """Cualquier mensaje del stream (bookTicker, aggTrade, pong) prueba que el feed esta vivo, sin alimentar el detector."""
        if t >= self.t_tick.get(coin, -10**18): self.t_tick[coin] = t

    def on_tick(self, coin, t, px):
        s = self.det[coin].update(t, px)
        if self.det[coin].t_ult == t: self.vivo(coin, t)
        if s:
            for lado in ('YES', 'NO'):
                if adverso(lado, s): self.adv[(coin, lado)] = t
        return s

    @staticmethod
    def cancelar_si(lado, signo):
        return signo != 0 and adverso(lado, signo)

    def puede_armar(self, coin, lado, t):
        if coin not in self.t_tick or t - self.t_tick[coin] > self.stale: return False      # sin feed fresco no hay calma demostrable
        u = self.adv.get((coin, lado))
        return u is None or u <= t - self.rearm
