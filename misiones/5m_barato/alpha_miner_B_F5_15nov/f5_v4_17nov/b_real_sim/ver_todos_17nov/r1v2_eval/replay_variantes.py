#!/usr/bin/env python3
"""replay_variantes.py -- R1v2 FASE B (pendiente 2): cancelacion/no-armar DENTRO del replay de la politica REAL de B, sin editar b_policy_sim.py (sellado, sha 787fa37e...).
Metodo: en la importacion se LEE b_policy_sim.py, se comprueba su sha y se le INSERTAN lineas '# [HOOK]' en 4 anclas unicas (alta, repegado, vida de la orden, eventos extra) + el argumento HK de run_day; el resultado se ejecuta
en un modulo aparte. `verifica_parche` demuestra que quitando las lineas [HOOK] y el argumento HK queda EXACTAMENTE el original; con HK=None el replay es identico (test sobre stubs).
Hooks (interfaz): no_armar(m,k,t,L)->bool [alta y cada repegado: si True no se coloca / no se repega y la orden previa sigue viva]; cancela(m,o,trx)->bool [vida: trx = rx de la actualizacion que dispara];
t_end(m,o,trx)->ms [el relleno de la orden solo ocurre si tf1 <= t_end: efectividad rx+t_proc+L_cancel <= casado-20]; registra(m,o,trx). Tras cancelar por regla el mercado queda cerrado (kappa=T_STOP: sin re-armado).
Reloj: casado en EXCHANGE; para un relleno por bloqueo (tf1 = t_rx) t_end se corrige con (tf1 - t_ex) para comparar t_ex <= t_end_exchange (code-review 3 #9). 0 ordenes reales, 0 red."""
import os, sys, hashlib, types
from collections import Counter
import numpy as np
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; V = os.path.dirname(HV.rstrip('/')) + '/'; BSIM = os.path.dirname(V.rstrip('/')) + '/'
sys.path.insert(0, HV); sys.path.insert(0, V + 'r1v2_sec7/'); sys.path.insert(0, BSIM)
import variantes_b as VB
SRC = BSIM + 'b_policy_sim.py'; SHA_SRC = '787fa37eb286394e8b4d43de5723cc0aed9cf17d5239416a00b7ea75ee5c046c'
A_SIG = 'def run_day(d, P, E=None):'
A_ALTA = '        size = tamano_orden(objetivo, 5, 1.0)\n'
A_REPEG = "            if objetivo is None or abs(objetivo - o['L']) > 1e-9: cancela(m, t, 'repega' if objetivo is not None else 'cancela_banda')\n"
A_VIDA = '            if not valido:\n'
A_EVT = '    EVT = {id(m): evtimes(m) for m in mkts}; heap = []\n'
H_EVT = "    if HK is not None: EVT = {id(m): np.unique(np.concatenate([EVT[id(m)], HK.extra_events(m, DEC)])) for m in mkts}   # [HOOK]\n"
H_ALTA = '        if HK is not None and HK.no_armar(m, tok, t, objetivo): return   # [HOOK]\n'
H_REPEG = "            if HK is not None and objetivo is not None and abs(objetivo - o['L']) > 1e-9 and HK.no_armar(m, o['k'], t, objetivo): return   # [HOOK]\n"
H_VIDA = ("            if HK is not None and HK.cancela(m, o, t - DEC):   # [HOOK]\n"
          "                o_h = o; cancela(m, t, 'regla'); m.cerrado = False; settle(m, o_h, HK.t_end(m, o_h, t - DEC)); m.done = True; HK.registra(m, o_h, t - DEC); return   # [HOOK]\n")

def parchea(src):
    for a in (A_SIG, A_ALTA, A_REPEG, A_VIDA, A_EVT):
        if src.count(a) != 1: raise ValueError(f'ancla no unica/ausente ({src.count(a)}): {a.strip()[:60]}')
    s = src.replace(A_SIG, 'def run_day(d, P, E=None, HK=None):').replace(A_ALTA, H_ALTA + A_ALTA).replace(A_REPEG, H_REPEG + A_REPEG).replace(A_VIDA, H_VIDA + A_VIDA).replace(A_EVT, A_EVT + H_EVT)
    return s

def verifica_parche(orig, patched):
    """quitando las lineas [HOOK] y el argumento HK queda el original exacto."""
    ql = [l for l in patched.split('\n') if '# [HOOK]' not in l]; return '\n'.join(ql).replace('def run_day(d, P, E=None, HK=None):', A_SIG) == orig

def carga():
    txt = open(SRC, encoding='utf-8').read()
    if hashlib.sha256(txt.encode()).hexdigest() != SHA_SRC: raise ValueError('b_policy_sim.py cambio (sha) : el parche de hooks no se aplica (fail-closed)')
    p = parchea(txt); assert verifica_parche(txt, p)
    ns = {'__name__': 'b_policy_sim_hook', '__file__': SRC}; exec(compile(p, SRC + '#hooks', 'exec'), ns); return types.SimpleNamespace(run_day=ns['run_day'], ns=ns, sha_origen=SHA_SRC, sha_parcheado=hashlib.sha256(p.encode()).hexdigest())
MOD = carga(); run_day = MOD.run_day

# ------------------------------------------------------------------ hooks
class HookBase:
    """no hace nada (equivale a HK=None). Contadores en self.cont."""
    def __init__(self): self.cont = Counter(); self.tau = {}; self.fills = lambda: {}; self.dec = 0
    @staticmethod
    def key(m, o): return (m.mid, int(o['n_ord']))      # clave estable de la orden (no id(): Python reutiliza ids)
    def extra_events(self, m, DEC): self.dec = DEC; return np.zeros(0, np.int64)   # instantes de decision (reloj t = rx + DEC) adicionales donde el replay debe pasar por la politica
    def no_armar(self, m, k, t, L): return False
    def cancela(self, m, o, trx): return False
    def t_end(self, m, o, trx): raise NotImplementedError
    def registra(self, m, o, trx): self.cont['cancelaciones_regla'] += 1
    def _t_end(self, o, tau, trx, t_proc, l_cancel):
        """ANCLA = max(tau, trx): la cancelacion no puede empezar antes de que el replay (ejecutor de UN solo hilo: decide y envia en secuencia) procese la actualizacion que la dispara (trx = rx), aunque tau (instante de deteccion) sea anterior. el relleno solo se mantiene si tf1 <= anclaje + t_proc + L_cancel + 19 (es decir se anula si tau+t_proc+L <= tf-20); relleno por bloqueo: tf1 es rx -> se compara su t_ex."""
        te = int(max(int(tau), int(trx)) + t_proc + l_cancel + VB.MARGEN_CASADO_MS - 1); f = self.fills().get((int(o['k']), round(float(o['L']), 4), int(o['t_arr']), int(o['tf1'])) if o.get('tf1') is not None else None)
        if f is not None and f.get('canal') == 'bloqueo' and f.get('t_ex') is not None: te += int(o['tf1']) - int(f['t_ex'])
        return te

def lado_de(m, k): return 'YES' if k == m.ku else 'NO'

class HookBinance(HookBase):
    """V5 (CXJ150) / V6 (E1b S1): no armar en cada alta y repegado + cancelar la orden viva en el primer tick adverso desde su llegada. series = {coin: (t_rx_ordenado, precio)}; var = VB.V5 | VB.V6."""
    def __init__(self, series, var, t_proc, l_cancel=VB.L_CANCEL['primaria'], fills=None):
        super().__init__(); self.var = var; self.tp = t_proc; self.lc = l_cancel; self.series = series; self.J = {c: VB.saltos(t, p, var) for c, (t, p) in series.items()}
        if fills is not None: self.fills = fills
    def extra_events(self, m, DEC):
        self.dec = DEC
        """el replay solo visita eventos de libro + cadencia del bucle: se anaden los ticks adversos (cancelacion en el instante del tick, rx=tau) y el instante en que se levanta el no-armar (tau+300+ventana)."""
        if m.coin not in self.J: return np.zeros(0, np.int64)
        tk = np.concatenate([self.J[m.coin]['up'], self.J[m.coin]['dn']]).astype(np.int64); lo = (m.fin - 300) * 1000; hi = int((m.fin - 0) * 1000)
        ev = np.concatenate([tk + DEC, tk + VB.DELAY_ARMAR_MS + self.var['no_armar_ms'] + DEC + 1]); return np.unique(ev[(ev >= lo) & (ev <= hi)])
    def _adv(self, m, k): return VB.adverso(self.J[m.coin], lado_de(m, k)) if m.coin in self.J else np.array([], np.int64)
    def no_armar(self, m, k, t, L):
        self.cont['altas_o_repegados'] += 1; sd = m.coin not in self.series or bool(np.isnan(VB.ret_bps(*self.series[m.coin], [int(t) - VB.DELAY_ARMAR_MS], self.var['w_ms'])[0]))
        self.cont['sin_dato'] += int(sd); b = VB.no_armar(self._adv(m, k), t, self.var); self.cont['bloqueadas'] += int(b); return b
    def cancela(self, m, o, trx):
        if self.key(m, o) in self.tau: return False
        tb = VB.primer_disparo(self._adv(m, o['k']), int(o['t_arr']), int(trx))
        if tb is None: return False
        self.tau[self.key(m, o)] = tb; self.cont['vidas_con_disparo'] += 1; return True
    def t_end(self, m, o, trx): return self._t_end(o, self.tau[self.key(m, o)], trx, self.tp, self.lc)

class HookControl(HookBase):
    """CONTROL del DeltaPnL de V5/V6: mismo replay con los MISMOS instantes de decision extra (ticks/desbloqueos de la variante) pero SIN regla (no_armar/cancela = False). DeltaPnL de la variante = variante - control (aisla el efecto de la regla del de visitar mas instantes)."""
    def __init__(self, ref): super().__init__(); self.ref = ref
    def extra_events(self, m, DEC): self.dec = DEC; return self.ref.extra_events(m, DEC)

class HookE1(HookBase):
    """V1-V4 (familia confirmatoria): en cada alta/repegado NO se arma si F5_t es invalido o 'alto' (gatillo Puerta 0) o si la regla E1 dispara (ucb: mu_ucb < -c; mu: mu_hat < -c).
    cancel_vida=True (EXPLORATORIA, fuera de familia) evalua ademas la regla sobre la orden viva. NaN en algun rasgo -> la regla NO se aplica (no se cancela ni se bloquea por ella; contado), nunca y=0.
    puntua(m, k, t, L) -> (f5t, mu_hat, mu_ucb) o None si el rasgo no es evaluable; lo inyecta el runner (e1_modelo.PuntuaE1.__call__)."""
    def __init__(self, puntua, regla, c, t_proc, l_cancel=VB.L_CANCEL['primaria'], cancel_vida=False, gate_f5=True, fills=None):
        super().__init__(); assert regla in ('ucb', 'mu'); self.puntua = puntua; self.regla = regla; self.c = c; self.tp = t_proc; self.lc = l_cancel; self.cv = cancel_vida; self.gate = gate_f5
        if fills is not None: self.fills = fills
    def extra_events(self, m, DEC):
        """solo cancel_vida (exploratoria): rejilla de 250 ms durante toda la ventana del mercado (el replay no visita el libro estatico entre eventos). Coste alto: no se usa en la familia primaria."""
        self.dec = DEC
        if not self.cv: return np.zeros(0, np.int64)
        return np.arange((m.fin - 300) * 1000, int((m.fin - MOD.ns['T_STOP']) * 1000) + 1, 250, dtype=np.int64) + DEC
    def _dispara(self, s):
        if s is None or not np.isfinite(s[1]) or not np.isfinite(s[2]): self.cont['rasgo_no_evaluable'] += 1; return False
        v = s[2] if self.regla == 'ucb' else s[1]; return bool(v < -self.c)
    def no_armar(self, m, k, t, L):
        self.cont['altas_o_repegados'] += 1; s = self.puntua(m, k, t, L)
        if self.gate:
            from sec7_core import tercil
            f5 = None if s is None else s[0]; tc = tercil(None if f5 is None or not np.isfinite(f5) else f5)
            if tc in ('inval', 'alto'): self.cont['bloq_f5_' + tc] += 1; return True
        if self._dispara(s): self.cont['bloq_regla'] += 1; return True
        return False
    def cancela(self, m, o, trx):
        if not self.cv or self.key(m, o) in self.tau or trx + self.dec < int(o['t_dec']): return False      # mismo reloj: rx + DEC = instante de decision
        if self._dispara(self.puntua(m, o['k'], trx, o['L'])): self.tau[self.key(m, o)] = int(trx); self.cont['vidas_con_disparo'] += 1; return True
        return False
    def t_end(self, m, o, trx): return self._t_end(o, self.tau[self.key(m, o)], trx, self.tp, self.lc)

# ------------------------------------------------------------------ horquilla de bloqueo: Delta (ADENDA_07 FIRMADA por el chief 19-Nov, sha db4484e5...; Delta SOLO por argumento, nunca por defecto)
import sec7_core as _C
class EngineBloqueoDelta(_C.EngineBloqueo):
    """EngineBloqueo (canal bloqueo ACTIVO) con q recortado a Delta acciones SOLO en los rellenos de canal 'bloqueo': q = min(restante, nivel visible, Delta). Delta obligatorio (>= FLOOR). No toca sec7_core."""
    def __init__(self, E, delta, **kw):
        if delta is None or not np.isfinite(delta) or delta < _C.FLOOR: raise ValueError('delta obligatorio y >= FLOOR (ADENDA_07 firmada, sha db4484e5...)')
        super().__init__(E, activo=True, **kw); self.delta = float(delta)
    def run_segment(self, k, L, t_arr, t_end, rem, variant):
        q, tf, why = super().run_segment(k, L, t_arr, t_end, rem, variant)
        f = self.fills.get((int(k), round(float(L), 4), int(t_arr), int(tf))) if (tf is not None and q > 0) else None
        if f is not None and f.get('canal') == 'bloqueo' and q > self.delta: q = self.delta; f['q'] = q; self.cont['bloqueo_recortado_delta'] += 1
        return q, tf, why
