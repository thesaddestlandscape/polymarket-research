"""cola_lib.py (RE-AS-B Tarea B) -- utilidades compartidas, SOLO LECTURA. python3 -I. 
EVw = sum(pnl)/sum(coste) ponderado por euros; IC90 = bootstrap por CIERRE (2000, semilla 2711). n minimo para decidir = 40."""
import json, numpy as np, pandas as pd
VPV = '/root/polymarket-research-datalogs/vida_puja_virtual/vpv_%s.csv.gz'
DESF = '/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'
ACC, R, SEED, NMIN = 5.0, 2000, 2711, 40
REJ_EDGES = [-1e-9, 1e-9, 10, 25, 100, 1e12]; REJ_LAB = ['0', '(0,10]', '(10,25]', '(25,100]', '>100']
TRI_EDGES = [-1e-9, 1e-9, 25, 1e12]; TRI_LAB = ['0', '(0,25]', '>25']
BK_EDGES = [0.0999, 0.15, 0.20, 0.25, 0.3001]; BK_LAB = ['10-15', '15-20', '20-25', '25-30']
def cargar_vpv(dias):
    DES = json.load(open(DESF)); X = []
    for d in dias:
        x = pd.read_csv(VPV % d); X.append(x)
    X = pd.concat(X, ignore_index=True); X['mercado'] = X.mercado.astype(str)
    g = X.mercado.map(DES); X['gana'] = np.where(g.isna(), np.nan, (g == X.lado).astype(float))
    X['cob_gana'] = X.groupby('dia').gana.transform(lambda s: s.notna().mean())
    X['bk'] = pd.cut(X.b, BK_EDGES, labels=BK_LAB); X['rej'] = pd.cut(X.Q0, REJ_EDGES, labels=REJ_LAB); X['tri'] = pd.cut(X.Q0, TRI_EDGES, labels=TRI_LAB)
    X['pnl'] = ACC * (X.gana - X.b); X['cost'] = ACC * X.b
    return X
def unidades(X, modo='primer_relleno', col='relleno_pes', tcol='t_relleno_pes_ms'):
    """Una observacion por (mercado,lado). primer_relleno: la vida con menor t de relleno (empate: menor t0). primera_colocada: la primera vida por t0, solo si rellena (ex-ante)."""
    X = X[(X.gana.notna()) & (X.ba > X.b) & (X.b >= 0.10 - 1e-9) & (X.b <= 0.30 + 1e-9)]
    if modo == 'primer_relleno':
        r = X[X[col] == 1].sort_values([tcol, 't0_recv_ms']); return r.groupby(['mercado', 'lado'], as_index=False).head(1)
    p = X.sort_values('t0_recv_ms').groupby(['mercado', 'lado'], as_index=False).head(1); return p[p[col] == 1]
def ic90(q, rng):
    g = q.groupby('cierre').agg(p=('pnl', 'sum'), c=('cost', 'sum')); P, C = g.p.values, g.c.values; n = len(g)
    if n < 2: return (np.nan, np.nan)
    v = []
    for _ in range(R):
        s = rng.integers(0, n, n); v.append(P[s].sum() / C[s].sum())
    return tuple(np.percentile(v, [5, 95]))
def linea(nm, q, rng, nmin=NMIN):
    if len(q) == 0: return '  %-30s n=0' % nm
    ev = q.pnl.sum() / q.cost.sum(); lo, hi = ic90(q, rng) if len(q) >= 3 else (np.nan, np.nan)
    return '  %-30s n=%4d cierres=%4d coste=%7.1f EVw=%+.4f IC90cierre(%+.3f,%+.3f) EVu=%+.4f %s' % (nm, len(q), q.cierre.nunique(), q.cost.sum(), ev, lo, hi, (q.pnl / q.cost).mean(), '' if len(q) >= nmin else '[n<%d NO CONCLUYE]' % nmin)
