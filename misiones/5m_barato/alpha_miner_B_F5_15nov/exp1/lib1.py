"""lib1.py -- EXP-1 (ADDENDUM1_B_F5.md; sha en ADDENDUM1_B_F5.sha256). Constantes y funciones comunes. Solo lectura de insumos; 0 ordenes.
Cada script que importa esto ABORTA si el addendum cambia tras el sellado (C10: los assert abortan)."""
import os, sys, json, hashlib, numpy as np, pandas as pd
AQ = '/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/'
EXP = AQ + 'exp1/'; CACHE = EXP + 'cache/'; os.makedirs(CACHE, exist_ok=True)
sys.path.insert(0, AQ)
from lib_ev import ter, RET, ev, t_ic, boot_cluster, sin_mejores, placebo_multi, resumen, C0, C1       # cortes de tercil CONGELADOS (TRAIN 06-08 Oct)
DL = '/root/polymarket-research-datalogs/'; REG = '/mnt/HC_Volume_106538179/m5_registro/'; MIT = DL + 'mitigar_as_25oct/'
L2 = '/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/'
SH = np.int64(1) << np.int64(41)
ADD_SHA = open(AQ + 'ADDENDUM1_B_F5.sha256').read().split()[0]
assert ADD_SHA.startswith('6fc7dba5') and hashlib.sha256(open(AQ + 'ADDENDUM1_B_F5.md', 'rb').read()).hexdigest() == ADD_SHA, 'ADDENDUM1 modificado tras el sellado'
assert (C0, C1) == (3.526360511779785, 4.717426776885986)
def ms(s): return int(pd.Timestamp(s).value // 10**6)
T_R1, T_R2 = ms('2026-10-17T08:35:00Z'), ms('2026-10-27T11:47:00Z')
FLOOR = {'R0': 19.5, 'R1': 39.5, 'R2': 19.0}
def epoca(t): t = np.asarray(t); return np.where(t < T_R1, 'R0', np.where(t < T_R2, 'R1', 'R2'))
def floor_of(t): e = epoca(t); return np.where(e == 'R1', 39.5, np.where(e == 'R0', 19.5, 19.0))
LS = (35, 60, 100, 150)
def specs():
    """(nombre, c, l_ef, d_proc, modo_delta): primarios p<l> (c=19, d_proc=3, delta=0); sensibilidades c, d_proc y delta (solo l=35,60)."""
    S = [(f'p{l}', 19, l, 3, 0) for l in LS]
    for l in (35, 60):
        S += [(f'c16_{l}', 16, l, 3, 0), (f'c22_{l}', 22, l, 3, 0), (f'd10_{l}', 19, l, 10, 0), (f'd30_{l}', 19, l, 30, 0), (f'dm_{l}', 19, l, 3, 'm'), (f'dp_{l}', 19, l, 3, 'p')]
    return S
def t_dec(tf, l, dp, dm):
    """t_dec = tf_ex + delta - l_ef - d_proc (ADDENDUM1 §2). delta = 0 primario; 'm' = -suelo (conservadora); 'p' = +suelo (solo sensibilidad, NO decide)."""
    fl = floor_of(tf); d = 0.0 if dm == 0 else (-fl if dm == 'm' else fl)
    return np.round(np.asarray(tf, float) + d - l - dp).astype(np.int64)
def leeq(path, keep=None, nodrop=True):
    """Filas q (id,rx,bid,ask,tb,ta) de un q_D.gz id-mapeado. nodrop=True: NO descarta filas con ask/tamano vacio (C5); devuelve (Q, n_filas_con_NaN)."""
    out = []; nn = 0
    for ch in pd.read_csv(path, header=None, names=['id', 'r', 'b', 'a', 'tb', 'ta'], chunksize=2_000_000, compression='gzip',
                          dtype={'id': np.int64, 'r': np.int64, 'b': np.float32, 'a': np.float32, 'tb': np.float32, 'ta': np.float32}, on_bad_lines='skip'):
        if keep is not None: ch = ch[ch.id.isin(keep)]
        nn += int(ch[['a', 'tb', 'ta']].isna().any(axis=1).sum()); out.append(ch if nodrop else ch.dropna())
    return pd.concat(out, ignore_index=True), nn
class Q:
    """Filas q ordenadas por (id, rx) con el MISMO desempate que forward_a1.rasgos (lexsort K,b,a,tb,ta). estado: ultima fila con rx <= t y antiguedad <= 30 s."""
    def __init__(self, ids, rx, b, a, tb, ta):
        K = np.asarray(ids, np.int64) * SH + np.asarray(rx, np.int64); o = np.lexsort((ta, tb, a, b, K))
        self.K = K[o]; self.R = np.asarray(rx, np.int64)[o]; self.B = np.asarray(b)[o]; self.A = np.asarray(a)[o]; self.TB = np.asarray(tb)[o]; self.TA = np.asarray(ta)[o]
    def feat(self, ids, t, maxage=30000):
        """Devuelve F5 (log1p tamano ask), bid, cat (0 ok, 1 sin_fila, 2 sin_ask, 3 cruzado) y asserta rx_usado <= t por fila (C5)."""
        ids = np.asarray(ids, np.int64); t = np.asarray(t, np.int64)
        i = np.searchsorted(self.K, ids * SH + t, 'right') - 1; ok = i >= 0; i = np.maximum(i, 0)
        ok &= ((self.K[i] // SH) == ids) & ((t - self.R[i]) <= maxage)
        assert (self.R[i][ok] <= t[ok]).all(), 'C5: rx usado > t_dec'
        a, ta, b = self.A[i], self.TA[i], self.B[i]; ask_ok = np.isfinite(a) & np.isfinite(ta)
        cat = np.where(~ok, 1, np.where(~ask_ok, 2, np.where(b >= a, 3, 0))).astype(np.int8)
        f5 = np.where(cat == 0, np.log1p(np.where(np.isfinite(ta), ta, 0.0)), np.nan).astype(np.float32)
        return f5, np.where(ok, b, np.nan).astype(np.float32), cat, i
def lab(f5):    # etiqueta de tercil; NaN (cualquier categoria) -> 'nan'
    return ter(f5)
CATN = {0: 'ok', 1: 'sin_fila', 2: 'sin_ask', 3: 'cruzado'}
def dist_ic(x):
    """IC90 por dias (t unilateral 95 %) -> (media, limite inferior, p unilateral)."""
    lo, p, m = t_ic(x); return m, lo, p
def boot_grad(df, a='bajo', b='alto', B=1000, seed=20261115):
    """Gradiente EV(a)-EV(b) pond. por EUR con bootstrap por cluster (cl). Devuelve (grad, ic90_lo, ic90_hi, sd_boot)."""
    rng = np.random.default_rng(seed); ma = (df.ter == a).values; mb = (df.ter == b).values
    P = pd.DataFrame({'pa': df.pnl.values * ma, 'ca': df.coste.values * ma, 'pb': df.pnl.values * mb, 'cb': df.coste.values * mb}).groupby(df.cl.values).sum().values
    s = P.sum(0); g = (s[0] / s[1] if s[1] > 0 else np.nan) - (s[2] / s[3] if s[3] > 0 else np.nan); n = len(P); r = np.empty(B)
    for k in range(B):
        x = P[rng.integers(0, n, n)].sum(0); r[k] = (x[0] / x[1] if x[1] > 0 else np.nan) - (x[2] / x[3] if x[3] > 0 else np.nan)
    return g, float(np.nanpercentile(r, 5)), float(np.nanpercentile(r, 95)), float(np.nanstd(r))
def n_req(n, g, sd): return float(n * (1.645 * sd / abs(g)) ** 2) if g and np.isfinite(g) and g != 0 else float('nan')
def write(path, lines): open(path, 'w').write('\n'.join(lines) + '\n')
def estado_fase(fase, estado, **kw):
    p = EXP + 'STATUS.json'; S = json.load(open(p)) if os.path.exists(p) else {}
    S[fase] = dict(estado=estado, t=pd.Timestamp.utcnow().strftime('%FT%TZ'), **kw); json.dump(S, open(p + '.tmp', 'w'), indent=1, default=str); os.replace(p + '.tmp', p)
