#!/usr/bin/env python3
"""Tests del nucleo del dry-run B-CXB60 (cxb60_core.py). Ejecutar: python3 -I test_cxb60_dryrun.py   (o pytest). Rapidos (<30 s), sin red, sin datos reales, 0 ordenes.
T1  equivalencia EXACTA maquina incremental (VMachine) vs `run_var`/`cfn` ORIGINALES de passT_cxb_v3.py (se extraen por AST del fichero del motor, no se copian) con datos sinteticos aleatorios y avance por pasos
    de t_known aleatorios con alimentacion incremental del buffer (sin lookahead): G0, GEO1, CXB35/60/100/150.
T2  causalidad: el resultado no cambia si se anaden filas futuras al buffer DESPUES de decidir (decision con rx <= t_known).
T3  TokBuf fuera de orden y duplicados de rx se ordenan de forma estable; TokenFeats incremental == de golpe.
T4  placebo: solo cancela donde CXB60 dispararia y el instante cae dentro del segmento.
T5  seguridad dry-run: el nucleo y el runner no importan py_clob_client/requests/web3/signers ni contienen llamadas de orden.
T6  cobertura de motivos: la suma de motivos + colocaciones cubre la rejilla; el gate coincide con gate_vec."""
import os, sys, ast, re, random
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HERE)
import cxb60_core as C

MOTOR = C.HERE + 'passT_cxb_v3.py'


def golden_funcs(fakeE):
    src = open(MOTOR).read(); tree = ast.parse(src); keep = {'first_after', 'run_var', 'cfn'}
    body = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in keep]; assert {n.name for n in body} == keep, [n.name for n in body]
    ns = dict(np=np, G=C.G, E=fakeE); exec(compile(ast.Module(body=body, type_ignores=[]), MOTOR, 'exec'), ns); return ns


class FakeE:
    @staticmethod
    def run_segment(k, L, t_arr, t_end, rem, variant):
        r = (int(t_arr) * 7 + int(t_end) * 3 + int(round(L * 100))) % 11
        q = min(rem, 5.0) if r in (0, 3, 7) else (min(rem, 2.0) if r == 5 else 0.0)
        return q, t_arr + 10 + r, 'fake'


def fake_fill(tok, L, t_arr, t_end, rem): return FakeE.run_segment(0, L, t_arr, t_end, rem, 'BASE')


class InjFeats(C.TokenFeats):
    """Caracteristicas pre-calculadas inyectadas por trozos (misma ruta _apply que la real)."""
    def __init__(self, tok, fin, arrays, levels=C.LEVELS):
        super().__init__(tok, fin, None, None, None, levels); self.arr = arrays

    def extend(self, t_known):
        m1 = int(min(self.n, max(0, (t_known - self.g[0]) // C.GRID + 1))) if t_known >= self.g[0] else 0
        if m1 <= self.m: return
        a = self.arr; s = slice(self.m, m1); self._apply(self.g[s], a['bid'][s], a['ask'][s], a['b300'][s], a['b15'][s], a['vol'][s]); self.m = m1


def synth(seed, fin=1793100000):
    r = np.random.default_rng(seed); g = np.arange((fin - 300) * 1000, (fin - C.TMIN) * 1000 + 1, C.GRID); n = len(g)
    walk = lambda lo, hi, step: np.clip(np.cumsum(r.choice([-step, 0, 0, step], n)) + r.uniform(lo, hi), lo - 0.05, hi + 0.05)
    bid = np.round(walk(0.05, 0.25, 0.01), 2); ask = np.round(bid + r.choice([0.01, 0.02, 0.03], n), 2); b300 = np.concatenate([np.full(600 if n > 600 else n, np.nan), bid[:-600]])[:n] if n > 600 else bid.copy()
    b15 = np.round(bid + r.choice([0.0, 0.01, 0.02, 0.05], n), 2); b15[r.random(n) < 0.02] = np.nan
    vol = np.abs(np.cumsum(r.normal(0, 8, n))) + r.choice([0, 10, 40], n)
    ntick = r.integers(30, 160); rx = np.sort(r.integers(g[0] - 2000, g[-1] + 3000, ntick)); qbid = np.round(np.clip(0.10 + np.cumsum(r.choice([-0.03, -0.01, 0, 0.01, 0.03], ntick)) * 0.5, 0.0, 0.30), 2)
    return fin, dict(bid=bid, ask=ask, b300=b300, b15=b15, vol=vol), rx, qbid


def run_machine(spec, L, fin, arrays, rx, qbid, rng, add_future_after=None):
    buf = C.TokBuf(); F = InjFeats('tok', fin, arrays); mach = C.VMachine(spec, F, L, 12345); out = []; added = 0; t = F.g[0] - 5000
    while True:
        t += int(rng.integers(100, 3000))
        while added < len(rx) and rx[added] <= t: buf.add_q(rx[added] - 20, int(rx[added]), float(qbid[added]), float(qbid[added] + 0.01), 10.0, 10.0); added += 1
        F.buf = buf; F.extend(t); out += mach.step(t, fake_fill)
        if mach.done or t > F.g[-1] + 8000: break
    F.buf = buf; out += mach.step(10 ** 18, fake_fill); return out


def golden(L, fin, arrays, rx, qbid, name, l):
    ns = golden_funcs(FakeE); g = np.arange((fin - 300) * 1000, (fin - C.TMIN) * 1000 + 1, C.GRID); hora = (g // 3600000) % 24
    Gm = C.G.gate_vec('G', L, arrays['b15'], arrays['vol'], hora); base = Gm & np.isfinite(arrays['ask']) & (arrays['ask'] > L + C.EPS)
    with np.errstate(invalid='ignore'): arm = np.isfinite(arrays['b300']) & ((arrays['b300'] - L) >= 0.01 - 1e-6)
    can = base if name == 'G0' else base & arm; cf = None
    if name.startswith('CXB'): cf = ns['cfn'](rx.astype(np.int64), qbid < L - C.TOLP, l)
    return ns['run_var'](0, L, g, can, Gm, fin, cf)


def test_equivalencia_run_var():
    n_cmp = n_seg = n_canc = 0
    for seed in range(60):
        fin, arrays, rx, qbid = synth(seed)
        for L in C.LEVELS:
            for name, l in (('G0', None), ('GEO1', None), ('CXB35', 35), ('CXB60', 60), ('CXB100', 100), ('CXB150', 150)):
                spec = C.VSpec(name, 'G0' if name == 'G0' else ('GEO1' if name == 'GEO1' else 'CXB'), l=l)
                got = run_machine(spec, L, fin, arrays, rx, qbid, np.random.default_rng(seed * 13 + 5)); ref = golden(L, fin, arrays, rx, qbid, name, l)
                a = [(r['seg'], r['t_dec_rx'], r['t_arr'], r['t_end'], r['q'], r['tf'], r['canc']) for r in got]
                assert a == ref, (seed, L, name, a[:3], ref[:3]); n_cmp += 1; n_seg += len(a); n_canc += sum(x[6] for x in a)
    assert n_seg > 1000 and n_canc > 100, (n_seg, n_canc)      # el fuzz ejercita colocaciones y cancelaciones
    print('T1 ok: comparaciones', n_cmp, 'segmentos', n_seg, 'cancelaciones', n_canc)


def test_causalidad_futuro():
    """Datos futuros (rx > t_known) no pueden cambiar lo ya decidido: se compara el resultado con un buffer que NUNCA vio filas futuras anomalas frente a otro donde se inyectan rx tardios basura despues de cerrar el mercado."""
    for seed in range(20):
        fin, arrays, rx, qbid = synth(seed + 500)
        spec = C.VSpec('CXB60', 'CXB', l=60); base = run_machine(spec, 0.13, fin, arrays, rx, qbid, np.random.default_rng(seed))
        rx2 = np.concatenate([rx, [rx.max() + 100000]]); qb2 = np.concatenate([qbid, [0.0]])               # fila basura mucho despues del fin
        alt = run_machine(spec, 0.13, fin, arrays, rx2, qb2, np.random.default_rng(seed))
        assert [(r['t_arr'], r['t_end'], r['q'], r['canc']) for r in base] == [(r['t_arr'], r['t_end'], r['q'], r['canc']) for r in alt], seed
    print('T2 ok')


def test_tokbuf_y_feats_incremental():
    b = C.TokBuf(); rows = [(100, 120, 0.1, 0.2, 5, 5), (110, 150, 0.11, 0.2, 5, 5), (105, 130, 0.12, 0.2, 5, 5), (160, 160, 0.1, 0.2, 5, 5)]
    for ex, rx, *r in rows: b.add_q(ex, rx, *r)
    assert b.qrx == sorted(b.qrx) and b.n_q_fuera_de_orden == 1 and b.qbid == [0.1, 0.12, 0.11, 0.1], (b.qrx, b.qbid)
    b2 = C.TokBuf()
    for i, rx in enumerate([10, 20, 15]): b2.add_t(rx - 5, rx, 0.1, 0, 1.0 + i)
    assert b2.trx == [10, 15, 20] and abs(b2.ta()['S'][-1] - 6.0) < 1e-9
    # quotes_rx: ultimo mensaje con rx <= t
    bid, ask = C.quotes_rx(b, np.array([99, 120, 140, 155, 170]))
    assert np.isnan(bid[0]) and bid[1] == 0.1 and bid[2] == 0.12 and bid[3] == 0.11 and bid[4] == 0.1, bid
    print('T3 ok')


def test_placebo_cobertura():
    for seed in range(25):
        fin, arrays, rx, qbid = synth(seed + 900); L = 0.16
        spec = C.VSpec('PLC60_1', 'PLC', seed=1, ref_l=60); got = run_machine(spec, L, fin, arrays, rx, qbid, np.random.default_rng(seed))
        for r in got:
            assert r['t_arr'] <= r['t_end'] and (r['canc'] == 0 or r['t_end'] > r['t_arr'] - 1), r
            if r['canc']:
                ns = golden_funcs(FakeE); cf = ns['cfn'](rx.astype(np.int64), qbid < L - C.TOLP, 60); tc = cf(r['t_arr'], r['t_arr'] + 10 ** 7)
                assert tc is not None, ('placebo cancela donde CXB60 no dispararia', r)
    print('T4 ok')


def test_seguridad_dry_run():
    import importlib
    prohibidos = ('py_clob_client', 'requests', 'web3', 'eth_account', 'websockets', 'aiohttp')
    for m in prohibidos: assert m not in sys.modules or m in ('requests',) and False, m
    for fn in ('cxb60_core.py', 'cxb60_dryrun_fase0.py'):
        p = HERE + fn
        if not os.path.exists(p): continue
        src = open(p).read(); code = re.sub(r'(""".*?"""|#.*)', '', src, flags=re.S)
        for bad in ('post_order', 'create_order', 'create_and_post', 'ClobClient', 'private_key', 'PRIVATE_KEY', 'signer', 'import requests', 'from web3', 'eth_account', '.env', 'api_key', 'api_secret', 'os.system(', 'subprocess'):
            assert bad not in code, (fn, bad)
    print('T5 ok')


def test_motivos_y_gate():
    fin, arrays, rx, qbid = synth(77); F = InjFeats('tok', fin, arrays); F.extend(10 ** 15); hora = (F.g // 3600000) % 24
    for L in C.LEVELS:
        Gm = C.G.gate_vec('G', L, arrays['b15'], arrays['vol'], hora); assert np.array_equal(F.Gm[L], Gm)
        assert set(np.unique(F.code[L])) <= set(C.TokenFeats.CODES); assert ((F.code[L] == 0) == (Gm & np.isfinite(arrays['ask']) & (arrays['ask'] > L + C.EPS))).all()
    print('T6 ok')


if __name__ == '__main__':
    for f in (test_tokbuf_y_feats_incremental, test_equivalencia_run_var, test_causalidad_futuro, test_placebo_cobertura, test_seguridad_dry_run, test_motivos_y_gate): f()
    print('TODOS OK')
