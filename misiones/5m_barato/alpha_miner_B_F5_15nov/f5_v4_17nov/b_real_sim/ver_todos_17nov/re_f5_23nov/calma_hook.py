#!/usr/bin/env python3
"""calma_hook.py -- ESPEC_HOOK_CALMA_V4_23nov (firmada, sha 1b8f1893...): Calma-T1 como TERCER componente (junto a V5/V6) del HookRF5 de la politica K6 = K1 + Calma. Se porta la REGLA (calma_gate, copiado byte a byte: sha c66ce9de...), no la politica del discovery.
Parametros CONGELADOS: TH 1 bps, lookback 100 ms, refractario 1 s, no armar >= 1000 ms tras un salto adverso, cancelar la orden viva en el primer salto adverso desde su llegada. Convencion del motor vigente passT_v4: tq = t - 300 ms (DELAY_ARMAR_MS), sensibilidad tq = t.
Reloj: RECEPCION de Binance (m5_registro, filas x), nunca E. Sin RNG, sin I/O, sin estado entre dias (instancia nueva por dia y por replica). Fail-closed: sin dato => NO bloquea ni cancela (como V5/V6) pero se cuenta y el dia puede quedar NO_EVALUABLE_CALMA. 0 ordenes, 0 red."""
import os, sys
import numpy as np
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HV)
import rf5_core as K5                       # fija sys.path de r1v2_eval (variantes_b, replay_variantes)
import variantes_b as VB, replay_variantes as RV
import calma_gate as CG
SHA_CALMA_GATE = 'c66ce9deeeab40f9d2c9d988f21867adabb30316fdb1a8c5ef8ec09fddd4f168'; VAR_CALMA = dict(no_armar_ms=CG.REARM_MS)
NO_EVALUABLE_FRAC = 0.05                    # ESPEC sec.4: sin_dato > 5 % de altas/repegados => moneda-dia NO_EVALUABLE_CALMA

def verifica_gate():
    import hashlib
    h = hashlib.sha256(open(HV + 'calma_gate.py', 'rb').read()).hexdigest()
    if h != SHA_CALMA_GATE: raise ValueError('calma_gate.py copiado cambio (sha): fail-closed')
    return h

def calma_jumps(t, p):
    """= calma_gate.jumps(th=1.0, lookback_ms=100, refract_ms=1000). t ORDENADO por rx (VB.ordena_rx), p>0."""
    return CG.jumps(t, p, th=CG.TH_BPS, lookback_ms=CG.LOOKBACK_MS, refract_ms=CG.REFRACT_MS)

def calma_adversos(jt, js, lado):
    """= calma_gate.adverse_times: 'YES' -> saltos con signo<0; 'NO' -> signo>0."""
    return CG.adverse_times(jt, js, lado)

class HookCalma(RV.HookBase):
    """series = {coin_minuscula: (t_rx, px)} de m5_registro (la misma carga que V5/V6). J[coin] = {'up': tiempos signo>0, 'dn': tiempos signo<0}: formato de VB.adverso => YES adverso = 'dn', NO adverso = 'up' (identico a calma_adversos)."""
    def __init__(self, series, t_proc, l_cancel=VB.L_CANCEL['primaria'], fills=None, delay_armar_ms=VB.DELAY_ARMAR_MS):
        super().__init__(); verifica_gate()
        self.tp = int(t_proc); self.lc = int(l_cancel); self.series = series; self.delay_armar_ms = int(delay_armar_ms); self.var = VAR_CALMA; self.J = {}
        for c, (t, p) in series.items():
            jt, js = calma_jumps(t, p); self.J[c] = dict(up=np.asarray(jt)[np.asarray(js) > 0].astype(np.int64), dn=np.asarray(jt)[np.asarray(js) < 0].astype(np.int64))
        if fills is not None: self.fills = fills
    def extra_events(self, m, DEC):
        self.dec = DEC
        if m.coin not in self.J: return np.zeros(0, np.int64)
        tk = np.concatenate([self.J[m.coin]['up'], self.J[m.coin]['dn']]).astype(np.int64); lo = (m.fin - 300) * 1000; hi = int(m.fin * 1000)
        ev = np.concatenate([tk + DEC, tk + self.delay_armar_ms + self.var['no_armar_ms'] + DEC + 1]); return np.unique(ev[(ev >= lo) & (ev <= hi)])
    def _adv(self, m, k): return VB.adverso(self.J[m.coin], RV.lado_de(m, k)) if m.coin in self.J else np.array([], np.int64)
    def sin_dato(self, coin, tq):
        """sin serie, serie vacia o ultimo tick con rx <= tq a mas de VB.STALE_MS (o ninguno)."""
        if coin not in self.series: return True
        t = self.series[coin][0]; i = int(np.searchsorted(t, tq, side='right')) - 1
        return i < 0 or (tq - int(t[i])) > VB.STALE_MS
    def no_armar(self, m, k, t, L):
        self.cont['altas_o_repegados'] += 1; self.cont['altas_' + m.coin] += 1; tq = int(t) - self.delay_armar_ms; sd = int(self.sin_dato(m.coin, tq)); self.cont['sin_dato'] += sd; self.cont['sin_dato_' + m.coin] += sd
        ja = self._adv(m, k); b = bool(np.searchsorted(ja, tq, 'right') - np.searchsorted(ja, tq - self.var['no_armar_ms'], 'right') > 0); self.cont['bloqueadas'] += int(b); return b
    def cancela(self, m, o, trx):
        if self.key(m, o) in self.tau: return False
        tb = VB.primer_disparo(self._adv(m, o['k']), int(o['t_arr']), int(trx))
        if tb is None: return False
        self.tau[self.key(m, o)] = tb; return True
    def t_end(self, m, o, trx): return self._t_end(o, self.tau[self.key(m, o)], trx, self.tp, self.lc)
    def registra(self, m, o, trx): self.cont['cancelaciones_regla'] += 1

def estado_evaluable(cont, series_coins, coins=('eth', 'sol', 'xrp'), frac_max=NO_EVALUABLE_FRAC):
    """ESPEC sec.4: moneda-dia NO_EVALUABLE_CALMA si falta la serie entera o sin_dato > 5 % de sus altas/repegados; el dia es NO_EVALUABLE_CALMA si lo es cualquier moneda (=> K6 NO_EVALUABLE ese dia; K1-K5 siguen). cont: Counter del HookCalma
    (altas_<coin>, sin_dato_<coin>). Devuelve dict(estado, por_moneda{coin: dict(estado, motivo, frac_sin_dato, altas)})."""
    por = {}
    for c in coins:
        if c not in series_coins: por[c] = dict(estado='NO_EVALUABLE_CALMA', motivo='falta serie Binance', frac_sin_dato=None, altas=0); continue
        n = int(cont.get('altas_' + c, 0)); f = (cont.get('sin_dato_' + c, 0) / n) if n else 0.0
        por[c] = dict(estado=('NO_EVALUABLE_CALMA' if f > frac_max else 'EVALUABLE'), motivo=(f'sin_dato {f:.3f} > {frac_max}' if f > frac_max else None), frac_sin_dato=f, altas=n)
    return dict(estado=('NO_EVALUABLE_CALMA' if any(v['estado'] != 'EVALUABLE' for v in por.values()) else 'EVALUABLE'), por_moneda=por)
