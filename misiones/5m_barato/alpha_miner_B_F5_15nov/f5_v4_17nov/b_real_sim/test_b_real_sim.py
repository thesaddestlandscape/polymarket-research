#!/usr/bin/env python3
"""test_b_real_sim.py -- pruebas del simulador (sin red, sin datos de produccion): motor SINTETICO con run_segment guionizado. Ejecutar: python3 test_b_real_sim.py"""
import sys, os, numpy as np, types, copy
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import b_policy_sim as S
FIN = 1_800_000_000          # s; mercado 5m: ventana (FIN-300 .. FIN)
P0 = dict(policy='R3', dec_rx=50, d_alta=53, ex_alta=35, d_canc=0, ex_canc=33, det_fill=250, d_r1=0.06, arm=0.0099, post_block=0, canc_block=0, settle_extra=0, tick=0)
class Stub:
    """E sintetico: mercados = lista de (coin, filas_up, filas_dn); fila = (rx_ms, bid, ask). prints guionizados: dict k -> [(t_ms, precio)] ; relleno completo si hay print <= L en (t_arr, t_end]."""
    def __init__(self, mk, prints=None, gana=1.0):
        n = 2 * len(mk); self.ks = list(range(n)); self.prints = prints or {}; self.g = gana
        qt, v0, v1, qb = [], [], [], [0]; mid, lado, fin, act = [], [], [], []
        for i, (coin, ru, rd) in enumerate(mk):
            for lad, rows in (('YES', ru), ('NO', rd)):
                for (t, b, a) in rows: qt.append(t); v0.append(np.nan if b is None else b); v1.append(np.nan if a is None else a)
                qb.append(len(qt)); mid.append(f'm{i}'); lado.append(lad); fin.append(FIN); act.append(coin.upper())
        self.K = types.SimpleNamespace(qb=np.array(qb), qt=np.array(qt, np.int64), v0=np.array(v0, np.float32), v1=np.array(v1, np.float32))
        self.D = types.SimpleNamespace(mid=np.array(mid), lado=np.array(lado), fin=np.array(fin), act=np.array(act, object))
        self.capt = types.SimpleNamespace(outcome=lambda D, k: self.g); self.calls = []
    def sane(self, k): return 'ok'
    def run_segment(self, k, L, t_arr, t_end, rem, var):
        self.calls.append((k, L, t_arr, t_end))
        for (t, p) in self.prints.get(k, []):
            if t_arr < t <= t_end and p <= L + 1e-9: return float(rem), t, 'ok'
        return 0.0, None, 'ok'
T0 = (FIN - 290) * 1000          # dentro de la ventana activa (T<=298)
def flat(b, a, t0=T0 - 400000, n=1): return [(t0, b, a)]
def run(st, P=P0):
    S.G.capt_outcome = lambda E, k: E.capt.outcome(E.D, k)
    return S.run_day('x', P, E=st)[0]
def test_topk_y_banda():
    st = Stub([('eth', flat(0.22, 0.24), flat(0.70, 0.72)), ('sol', flat(0.22, 0.24), flat(0.70, 0.72)), ('xrp', flat(0.31, 0.33), flat(0.60, 0.62)), ('eth', flat(0.225, 0.24), flat(0.6, 0.62))])
    R = run(st).drop_duplicates('mid').set_index('mid')
    assert abs(R.loc['m0', 'L'] - 0.20) < 1e-9 and R.loc['m0', 'size'] == 5          # ETH k=2: 0,22 -> 0,20
    assert abs(R.loc['m1', 'L'] - 0.21) < 1e-9                                       # SOL k=1
    assert 'm2' not in R.index and 'm3' not in R.index                              # fuera de banda (bid 0,31) y bid fuera de rejilla (0,225): sin orden
def test_tamano():
    st = Stub([('xrp', flat(0.20, 0.22), flat(0.7, 0.72))]); R = run(st); assert abs(R.L.iloc[0] - 0.19) < 1e-9 and R['size'].iloc[0] == 6.0     # 5*0,19<1 -> ceil(1/0,19)=6
def test_una_cara_y_repegado_con_asentar():
    up = [(T0 - 400000, 0.22, 0.24), (T0 + 5000, 0.23, 0.25)]; dn = [(T0 - 400000, 0.20, 0.22)]
    R = run(Stub([('eth', up, dn)])); assert set(R.k) == {0}                           # cara fijada: la 1a en banda (up)
    assert len(R) >= 2 and R.motivo_fin.iloc[0] == 'repega'
    assert R.t_dec.iloc[1] - R.t_cancel_dec.iloc[0] >= 1500                             # ASENTAR 1,5 s antes de reponer
    assert R.t_end.iloc[0] == R.t_cancel_dec.iloc[0] + 33 and R.t_arr.iloc[0] == R.t_dec.iloc[0] + 88   # latencias del contrato
def test_primer_relleno_cierra():
    up = [(T0 - 400000, 0.22, 0.24)]; st = Stub([('eth', up, [(T0 - 400000, 0.7, 0.72)])], prints={0: [(T0 + 2000, 0.19)]})
    R = run(st); assert (R.q > 0).sum() == 1 and len(R) == 1 and R.motivo_fin.iloc[0] == 'relleno'     # un relleno y ninguna orden mas en el mercado
    assert R.tf.iloc[0] == T0 + 2000 and R.pnl.iloc[0] > 0 and R.t_cancel_dec.iloc[0] >= R.tf.iloc[0] + 250
def test_max_vivas():
    mk = [('eth', flat(0.22, 0.24), flat(0.7, 0.72)) for _ in range(8)]; R = run(Stub(mk))
    ev = sorted([(r.t_dec, 1) for r in R.itertuples()] + [(r.t_cancel_dec + 1500, -1) for r in R.itertuples() if r.t_cancel_dec == r.t_cancel_dec]); vivas = 0; mx = 0
    for t, d in ev: vivas += d; mx = max(mx, vivas)
    assert mx <= 5 and R.mid.nunique() >= 5
def test_sin_lookahead():
    rng = np.random.default_rng(1); rows = lambda: [(T0 - 400000, 0.22, 0.24)] + [(T0 + int(x), float(rng.choice([0.21, 0.22, 0.23, 0.24])), 0.30) for x in np.sort(rng.integers(0, 60000, 40))]
    up, dn = rows(), [(T0 - 400000, 0.7, 0.72)]; full = run(Stub([('eth', up, dn)])); cut = T0 + 20000
    part = run(Stub([('eth', [r for r in up if r[0] <= cut], dn)]))
    a = full[full.t_dec <= cut][['L', 't_dec', 't_arr']].reset_index(drop=True); b = part[part.t_dec <= cut][['L', 't_dec', 't_arr']].reset_index(drop=True)
    assert len(a) > 3 and a.equals(b), (len(a), len(b))                                 # quitar el futuro no cambia ninguna decision anterior
def test_latencias_sensibilidad():
    up = [(T0 - 400000, 0.22, 0.24), (T0 + 5000, 0.23, 0.25)]; P = dict(P0, d_alta=150, ex_canc=74, dec_rx=100); R = run(Stub([('eth', up, [(T0 - 400000, 0.7, 0.72)])]), P)
    assert R.t_arr.iloc[0] == R.t_dec.iloc[0] + 150 + 35 and R.t_end.iloc[0] == R.t_cancel_dec.iloc[0] + 74
def test_R2_cancela_si_bid_cerca():
    up = [(T0 - 400000, 0.22, 0.24), (T0 + 3000, 0.21, 0.24)]       # bid cae a 0,21 pero seguimos en banda: R3 repega (objetivo 0,19); R2 cancela por armado (bid-L = 0,01 >= 0,0099: NO cancela); 0,20 -> cancela
    up2 = [(T0 - 400000, 0.22, 0.24), (T0 + 3000, 0.20, 0.24)]
    R2 = run(Stub([('eth', up2, [(T0 - 400000, 0.7, 0.72)])]), dict(P0, policy='R2')); assert R2.motivo_fin.iloc[0] in ('armado', 'repega')
    R2b = run(Stub([('eth', up, [(T0 - 400000, 0.7, 0.72)])]), dict(P0, policy='R2')); assert R2b.motivo_fin.iloc[0] != 'armado'
def test_t_stop():
    R = run(Stub([('eth', flat(0.22, 0.24), flat(0.7, 0.72))])); assert R.motivo_fin.iloc[-1] in ('t_stop', 'repega', 'cancela_banda') and (R.t_end <= (FIN - 60) * 1000 + 50 + 33 + 1).all() and (R.T_dec > 62).all()
def test_tick_y_bloqueo_y_settle():
    up = [(T0 - 400000, 0.22, 0.24), (T0 + 5000, 0.97, 0.98)]; dn = [(T0 - 400000, 0.7, 0.72), (T0 + 5000, 0.02, 0.03)]
    R = run(Stub([('eth', up, dn)]), dict(P0, tick=1)); assert R.motivo_fin.iloc[-1] == 'tick_cambiado' and (R.t_dec < T0 + 5100).all()      # tick_size_change: cierre definitivo
    up = [(T0 - 400000, 0.22, 0.24), (T0 + 5000, 0.23, 0.25)]; R = run(Stub([('eth', up, [(T0 - 400000, 0.7, 0.72)])]), dict(P0, settle_extra=200))
    assert R.t_dec.iloc[1] - R.t_cancel_dec.iloc[0] >= 1700                                                                                 # ASENTAR 1,5 + poll 0,2
    st = Stub([('eth', flat(0.22, 0.24), flat(0.7, 0.72)), ('sol', flat(0.22, 0.24), flat(0.7, 0.72))]); R = run(st, dict(P0, post_block=300)).sort_values('t_dec')
    assert R.t_dec.iloc[1] - R.t_dec.iloc[0] >= 300                                                                                          # hilo unico: el post bloquea a los demas mercados
if __name__ == '__main__':
    ts = [(n, f) for n, f in sorted(globals().items()) if n.startswith('test_')]
    for n, f in ts: f(); print('OK', n)
    print(len(ts), 'tests OK')
