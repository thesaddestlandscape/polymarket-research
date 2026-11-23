#!/usr/bin/env python3
"""rf5_core.py -- piezas PURAS de RF5E-COMB-23NOV-v1 (prereg 16be06b6): reglas F5-entrada, hook de la politica combinada (UNA replay por politica), conjuntos de politicas, vetos de inversion.
Reutiliza replay_variantes.HookBinance/HookBase (V5=CXJ150, V6=E1b S1 SIN cambio) y sec7_core.f5t (regla de antiguedad 30 s). Los cortes se LEEN de rf5_cortes.json (nunca se recalculan). 0 ordenes, 0 red."""
import os, sys, json
import numpy as np
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; V = os.path.dirname(HV.rstrip('/')) + '/'; BSIM = os.path.dirname(V.rstrip('/')) + '/'
for p in (V + 'r1v2_eval/', V + 'r1v2_sec7/', BSIM): sys.path.insert(0, p)
CORTES = HV + 'rf5_cortes.json'

def lee_cortes(path=None):
    c = json.load(open(path or CORTES))
    assert c['measurement_id'] == 'RF5E-COMB-23NOV-v1'
    return c

def veta_f5(regla, coin, f5, c):
    """True = NO entrar. f5 None/NaN (invalido o antiguo >30 s) => True para TODA regla con F5 (prereg sec.1). Comparacion '>=' inclusiva en vetos; F2 entra solo con f5 < p20."""
    if regla is None: return False
    if f5 is None or not np.isfinite(f5): return True
    if regla == 'F1': return f5 >= c['C1']
    if regla == 'F2': return not (f5 < c['F2_p20'][coin])
    if regla == 'F3': return f5 >= c['F3_p80'][coin]
    if regla == 'U13': return f5 >= c['C1'] or f5 >= c['F3_p80'][coin]
    raise ValueError(regla)

# nombre -> (regla F5 | None | 'SET', V5, V6, L_cancel, inversion_binance). 'SET' = veto de lados explicito (inversion F5: los F5_0 MAS BAJOS, mismo n por dia x moneda)
POLITICAS_A = {'base': (None, False, False, 74, False), 'F1': ('F1', False, False, 74, False), 'F2': ('F2', False, False, 74, False), 'F3': ('F3', False, False, 74, False),
               'U13': ('U13', False, False, 74, False), 'INV_F3': ('SET', False, False, 74, False)}
POLITICAS_K = {'K1': ('F3', True, True, 74, False), 'K2': ('F1', True, True, 74, False), 'K3': ('F2', True, True, 74, False), 'K4': ('U13', True, True, 74, False), 'K5': (None, True, True, 74, False),
               'V5': (None, True, False, 74, False), 'V6': (None, False, True, 74, False), 'F3_V6': ('F3', False, True, 74, False), 'F3_V5': ('F3', True, False, 74, False), 'INV_K1': ('SET', True, True, 74, True)}
for _k, _r in (('K1', 'F3'), ('K2', 'F1'), ('K3', 'F2'), ('K4', 'U13')):
    for _lc in (111, 147): POLITICAS_K[f'{_k}@lc{_lc}'] = (_r, True, True, _lc, False)
BLOQ1_SOLO = ('base', 'F1', 'F2', 'F3', 'U13', 'K1', 'K2', 'K3', 'K4', 'K5')      # bloq1 = sensibilidad: solo las politicas de la familia (sin ablacion/lc/inversion)

def lados_a_vetar_inversion(f5tab, n_por_celda):
    """f5tab: DataFrame (dia, coin, mid, k, f5_0 [NaN=invalido]); n_por_celda {(dia, coin): n} = lados que vetaria la regla directa. Devuelve {(mid,k)} = los n F5_0 VALIDOS mas bajos por dia x moneda (prereg sec.3)."""
    out = set()
    for (dia, coin), g in f5tab.groupby(['dia', 'coin']):
        n = int(n_por_celda.get((dia, coin), 0))
        if n <= 0: continue
        g = g[np.isfinite(g.f5_0.astype(float))].sort_values(['f5_0', 'mid', 'k'], kind='stable').head(n)
        out |= {(m, int(k)) for m, k in zip(g.mid, g.k)}
    return out

class HookRF5:
    """Politica combinada como UNA sola simulacion. Precedencia (prereg sec.4): veto F5 de entrada -> en cada alta/repegado no armar si V5 O V6 -> la orden viva se cancela en el primer disparo de cualquiera
    (+ L_cancel; efectividad rx+t_proc+L_cancel <= casado-20 ms via HookBase._t_end). F5_0 se mide en la PRIMERA alta INTENTADA del (mercado, lado) aunque V5/V6 la bloqueen; veto => 0 altas y 0 repegados en ese lado.
    Registra f5_0/edad/veto por (mid,k) y quien dispara cada cancelacion. Contrato de hooks de replay_variantes.HookBase."""
    def __init__(self, serie_k, regla, cortes, v5=None, v6=None, veto_set=None, invierte=False):
        from collections import Counter
        self.cortes = cortes; self.regla = regla; self.serie = serie_k; self.v5 = v5; self.v6 = v6; self.veto_set = veto_set or set(); self.inv = invierte
        self.comps = [h for h in (v5, v6) if h is not None]; self.tau = {}; self.quien = {}; self.f5_0 = {}; self.vetado = {}; self.cont = Counter()
        self.fills = lambda: {}; self.dec = 0
    key = staticmethod(lambda m, o: (m.mid, int(o['n_ord'])))
    def extra_events(self, m, DEC):
        self.dec = DEC; ev = [h.extra_events(m, DEC) for h in self.comps]
        return np.unique(np.concatenate(ev)) if ev else np.zeros(0, np.int64)
    def _adv(self, h, m, k):
        """adverso del lado (o FAVORABLE si invierte: control de inversion de V5/V6)."""
        import variantes_b as VB
        if m.coin not in h.J: return np.array([], np.int64)
        lado = 'YES' if k == m.ku else 'NO'
        if self.inv: lado = 'NO' if lado == 'YES' else 'YES'
        return VB.adverso(h.J[m.coin], lado)
    def f5_primera(self, m, k, t):
        kk = (m.mid, int(k))
        if kk not in self.f5_0:
            import sec7_core as C
            own = self.serie(int(k)); i = own.idx_rx(int(t)) if own is not None else -1
            f5 = C.f5t(own, int(t)); edad = float(int(t) - int(own.rx[i])) if i >= 0 else float('nan')
            self.f5_0[kk] = dict(coin=m.coin, f5_0=(float('nan') if f5 is None else f5), edad_ms=edad, t0=int(t), lado=('YES' if k == m.ku else 'NO'))
            self.vetado[kk] = (kk in self.veto_set) if self.regla == 'SET' else veta_f5(self.regla, m.coin, f5, self.cortes)
            self.cont['lados_vetados_f5'] += int(self.vetado[kk]); self.cont['lados_intentados'] += 1
        return self.vetado[kk]
    def no_armar(self, m, k, t, L):
        import variantes_b as VB
        self.cont['altas_o_repegados'] += 1; veto = self.f5_primera(m, k, t); b = False
        for h in self.comps: b |= bool(VB.no_armar(self._adv(h, m, k), t, h.var))
        self.cont['no_armadas'] += int(veto or b); return bool(veto or b)
    def cancela(self, m, o, trx):
        import variantes_b as VB
        key = self.key(m, o)
        if key in self.tau: return False
        tbs = {}
        for nom, h in (('V5', self.v5), ('V6', self.v6)):
            if h is None: continue
            tb = VB.primer_disparo(self._adv(h, m, o['k']), int(o['t_arr']), int(trx))
            if tb is not None: tbs[nom] = tb
        if not tbs: return False
        tau = min(tbs.values()); self.tau[key] = tau; self.quien[key] = '+'.join(sorted(n for n, v in tbs.items() if v == tau)); self.cont['vidas_con_disparo'] += 1; return True
    def t_end(self, m, o, trx):
        h = self.comps[0]; return h._t_end(o, self.tau[self.key(m, o)], trx, h.tp, h.lc)
    def registra(self, m, o, trx): self.cont['cancelaciones_regla'] += 1

def construye_hook(nombre, tabla, serie_k, bsrc, cortes, tp, fills, veto_set=None):
    """tabla = POLITICAS_A | POLITICAS_K. tp = t_proc ms OBLIGATORIO si hay V5/V6 (sin default). fills = callable -> fills del EngineBloqueo vigente."""
    import replay_variantes as RV, variantes_b as VB
    regla, a5, a6, lc, inv = tabla[nombre]; v5 = v6 = None
    if a5 or a6:
        if tp is None: raise ValueError('t_proc obligatorio para V5/V6 (sin default)')
        if a5: v5 = RV.HookBinance(bsrc, VB.V5, tp, l_cancel=lc, fills=fills)
        if a6: v6 = RV.HookBinance(bsrc, VB.V6, tp, l_cancel=lc, fills=fills)
    h = HookRF5(serie_k, regla, cortes, v5=v5, v6=v6, veto_set=veto_set, invierte=inv); h.fills = fills; return h

def conjuntos_exclusivos(R_base, flags):
    """Tabla de conjuntos exclusivos (solo F5 / solo V5 / solo V6 / V5 y V6 / F5 y (V5 o V6) / ninguno) sobre las unidades (mid,lado) de la base, con n, coste y PnL (DESCRIPTIVA, no suma EV).
    R_base: DataFrame con cols mid, lado, q, cost, pnl; flags: DataFrame (mid, lado, f5, v5, v6) booleanos."""
    X = R_base.groupby(['mid', 'lado'], as_index=False).agg(cost=('cost', 'sum'), pnl=('pnl', 'sum'), rell=('q', lambda s: int((s > 0).any()))).merge(flags, on=['mid', 'lado'], how='inner')
    def cj(r):
        if r.f5 and (r.v5 or r.v6): return 'F5_y_(V5oV6)'
        if r.f5: return 'solo_F5'
        if r.v5 and r.v6: return 'V5_y_V6'
        if r.v5: return 'solo_V5'
        if r.v6: return 'solo_V6'
        return 'ninguno'
    X['conjunto'] = [cj(r) for r in X.itertuples()]
    return X.groupby('conjunto').agg(n_lados=('mid', 'size'), n_rellenos=('rell', 'sum'), coste=('cost', 'sum'), pnl=('pnl', 'sum')).reset_index()

def verifica_veto_postfiltro(R_base, R_veto, f5tab, regla, cortes):
    """Prueba 'veto dentro del simulador == post-filtro de la base en un dia': las unidades con relleno de R_veto deben ser EXACTAMENTE las de R_base cuyo (mid,k) NO vetaria la regla (mismo pnl)."""
    vet = {(m, int(k)) for m, k, c, f in zip(f5tab.mid, f5tab.k, f5tab.coin, f5tab.f5_0) if veta_f5(regla, c, (None if not np.isfinite(f) else float(f)), cortes)}
    fb = R_base[R_base.q > 0]; fv = R_veto[R_veto.q > 0]
    kb = {(m, int(k)): p for m, k, p in zip(fb.mid, fb.k, fb.pnl) if (m, int(k)) not in vet}; kv = {(m, int(k)): p for m, k, p in zip(fv.mid, fv.k, fv.pnl)}
    so_v = sorted(set(kv) - set(kb)); so_b = sorted(set(kb) - set(kv)); dif = float(sum(kb[x] for x in kb if x in kv) - sum(kv[x] for x in kv if x in kb))
    return dict(ok=(not so_v and not so_b and abs(dif) < 1e-9), n_base=len(kb), n_veto=len(kv), solo_en_veto=len(so_v), solo_en_base=len(so_b), pnl_dif=dif)
