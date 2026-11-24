#!/usr/bin/env python3
"""rf5_rapido.py -- ACELERACION del simulador RF5 sin tocar b_policy_sim.py (sellado) ni el motor: memoiza EngineBloqueo.run_segment. run_segment es una funcion PURA de (k, L, t_arr, t_end, rem, variant) dentro de un dia (la cinta y el libro no cambian entre replicas;
solo cambian las decisiones del hook, y por tanto QUE llamadas se hacen). Cada llamada se cachea con el efecto lateral que tiene en W (entradas de `fills` y contadores `cont`), y en un acierto se reproduce ese efecto: el resultado es IDENTICO bit a bit a la version lenta (test en 17-Nov en rf5_rapido_prueba.py).
Instancia por dia y por activo (bloq 0/1). Tope de entradas (RAM). 0 ordenes, 0 red."""
import os, sys
from collections import Counter
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HV)
import rf5_core as K5      # fija sys.path de sec7_core
import sec7_core as C

class EngineBloqueoCache(C.EngineBloqueo):
    MAX = 1_500_000
    def __init__(self, *a, **k):
        super().__init__(*a, **k); self._memo = {}; self.hits = 0; self.miss = 0
    def run_segment(self, k, L, t_arr, t_end, rem, variant):
        key = (int(k), float(L), int(t_arr), int(t_end), float(rem), variant); h = self._memo.get(key)
        if h is not None:
            self.hits += 1; res, nf, nc = h
            if nf: self.fills.update(nf)
            if nc: self.cont.update(nc)
            return res
        self.miss += 1; f0, c0 = self.fills, self.cont; self.fills = {}; self.cont = Counter()
        try: res = super().run_segment(k, L, t_arr, t_end, rem, variant); nf, nc = self.fills, self.cont
        finally: self.fills, self.cont = f0, c0
        f0.update(nf); c0.update(nc)
        if len(self._memo) < self.MAX: self._memo[key] = (res, (dict(nf) if nf else None), (Counter(nc) if nc else None))      # vacios => None (memoria)
        return res

# ------------------------------------------------------------------ simulador rapido: el MISMO b_policy_sim parcheado con hooks (replay_variantes.parchea) + 3 sustituciones por codigo equivalente (perfil 17-Nov: ocupados 18 %, top 28 % del tiempo)
#  (1) Mkt.top: bisect sobre array.array compactos (8 B/fila) precalculados por (mercado, token) = np.searchsorted(qt,t,'right')-1 con el mismo filtro (finito y >0 => float, si no None); si qt no esta ordenado cae al original.
#  (2) ocupados(t): lista ACT2 podada de ordenes con rel <= t (los instantes t del bucle son no decrecientes y rel solo baja de 1e18 una vez); si t retrocede cae al original sobre ACT.
#  El resultado se comprueba BIT A BIT contra la version lenta en 17-Nov (rf5_rapido_prueba.py) y se registra el sha del fuente rapido. Para validar o depurar: RF5_LENTO=1 usa replay_variantes.run_day.
import types, hashlib, bisect
import array as _ar_mod
A_TOP = ("    def top(s, k, t):\n        qt, v0, v1 = s.A[k]; j = int(np.searchsorted(qt, t, side='right')) - 1\n        if j < 0: return None, None\n        b, a = v0[j], v1[j]\n"
         "        return (float(b) if np.isfinite(b) and b > 0 else None), (float(a) if np.isfinite(a) and a > 0 else None)\n")
N_TOP = ("    def top(s, k, t):                                          # [RAPIDO]\n        L = s.__dict__.setdefault('_L', {}).get(k)                  # [RAPIDO]\n        if L is None:                                              # [RAPIDO]\n"
         "            qt, v0, v1 = s.A[k]; ok = bool(len(qt) < 2 or np.all(np.diff(qt) >= 0)); f = lambda v: np.where(np.isfinite(v) & (v > 0), v, np.nan).astype(np.float64)   # [RAPIDO]\n"
         "            a_q = _ar.array('q'); a_q.frombytes(np.ascontiguousarray(qt, np.int64).tobytes()); a_b = _ar.array('d'); a_b.frombytes(f(v0).tobytes()); a_a = _ar.array('d'); a_a.frombytes(f(v1).tobytes())   # [RAPIDO] arrays compactos (8 B/fila)\n"
         "            L = s._L[k] = [a_q, a_b, a_a, ok, qt, v0, v1]          # [RAPIDO]\n        if not L[3]:                                               # [RAPIDO] qt desordenado: original\n"
         "            qt, v0, v1 = L[4], L[5], L[6]; j = int(np.searchsorted(qt, t, side='right')) - 1\n            if j < 0: return None, None\n            b, a = v0[j], v1[j]\n"
         "            return (float(b) if np.isfinite(b) and b > 0 else None), (float(a) if np.isfinite(a) and a > 0 else None)\n        j = _bs.bisect_right(L[0], t) - 1                          # [RAPIDO]\n"
         "        if j < 0: return None, None                                # [RAPIDO]\n        b = L[1][j]; a = L[2][j]                                   # [RAPIDO]\n        return (b if b == b else None), (a if a == a else None)    # [RAPIDO]\n")
A_OCUP = "    def ocupados(t): return sum(1 for x in ACT if x['rel'] > t)\n"
N_OCUP = ("    ACT2 = []; LT = [-10**18]                                      # [RAPIDO]\n    def ocupados(t):                                               # [RAPIDO]\n        if t >= LT[0]:                                             # [RAPIDO]\n"
          "            ACT2[:] = [x for x in ACT2 if x['rel'] > t]; LT[0] = t; return len(ACT2)   # [RAPIDO]\n        return sum(1 for x in ACT if x['rel'] > t)                 # [RAPIDO]\n")
A_APP = "ORD.append(o); ACT.append(o);"; N_APP = "ORD.append(o); ACT.append(o); ACT2.append(o);"

def parchea_rapido(p):
    for a in (A_TOP, A_OCUP, A_APP):
        if p.count(a) != 1: raise ValueError(f'ancla rapida no unica/ausente ({p.count(a)}): {a.strip()[:50]}')
    return p.replace(A_TOP, N_TOP).replace(A_OCUP, N_OCUP).replace(A_APP, N_APP)

def verifica_rapido(p, q):
    """deshaciendo las 3 sustituciones queda EXACTAMENTE el fuente parcheado con hooks (= original + hooks)."""
    r = q.replace(N_TOP, A_TOP).replace(N_OCUP, A_OCUP).replace(N_APP, A_APP); return r == p

def carga_rapido():
    import replay_variantes as RV
    txt = open(RV.SRC, encoding='utf-8').read()
    if hashlib.sha256(txt.encode()).hexdigest() != RV.SHA_SRC: raise ValueError('b_policy_sim.py cambio (sha): fail-closed')
    p = RV.parchea(txt); q = parchea_rapido(p)
    if not verifica_rapido(p, q): raise AssertionError('parche rapido no reversible')
    ns = {'__name__': 'b_policy_sim_rapido', '__file__': RV.SRC, '_bs': bisect, '_ar': _ar_mod}; exec(compile(q, RV.SRC + '#rapido', 'exec'), ns)
    return types.SimpleNamespace(run_day=ns['run_day'], ns=ns, sha_origen=RV.SHA_SRC, sha_hooks=hashlib.sha256(p.encode()).hexdigest(), sha_rapido=hashlib.sha256(q.encode()).hexdigest())

_MOD = []
def run_day(d, P, E=None, HK=None):
    """b_policy_sim parcheado (hooks + rapido). RF5_LENTO=1 => version lenta (replay_variantes)."""
    import replay_variantes as RV
    if os.environ.get('RF5_LENTO'): return RV.run_day(d, P, E=E, HK=HK)
    if not _MOD: _MOD.append(carga_rapido())
    return _MOD[0].run_day(d, P, E=E, HK=HK)
