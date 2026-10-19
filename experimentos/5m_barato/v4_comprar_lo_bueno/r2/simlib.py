"""Lector del extracto BTC (extrae_btc.sh) y estado del libro por RECEPCIÓN. Solo lectura. Sin look-ahead: el estado en t usa la
última fila con rx <= t. Libros cruzados (bid>ask) marcados como inválidos (regla v3+ del vigía)."""
import gzip, csv, json, glob, collections
from datetime import datetime
import numpy as np
O = '/mnt/HC_Volume_106538179/datalogs_analisis_caches/v4_comprar_lo_bueno/'
DL = '/root/polymarket-research-datalogs/'
DES = json.load(open(DL + 'maker_ms_desenlaces_cache.json'))
def fee(p): return 0.07 * p * (1 - p)
def p_limite(bid15, umbral=0.05):
    p = np.floor(bid15 * 100 + 1e-9) / 100
    while p > 0 and bid15 - p - fee(p) < umbral - 1e-12: p = round(p - 0.01, 2)
    return p if p > 0 else None

def kmap(D):
    km = {}
    for ln in open(O + f'k_{D}.csv'):
        c = ln.rstrip('\n').split(',')
        if len(c) >= 8 and c[3] == 'BTC' and c[4] in ('5min', '15min'):
            C = int(datetime.fromisoformat(c[6]).timestamp())
            km[(c[4], C, c[7])] = (c[2], c[5])
    return km

def lados(D):
    """Lado s y mercado 5m por cierre BTC (controles del vigía V4 = pares con referencias y gap>=1 bp)."""
    out = {}
    f = DL + f'vigia_5m_barato/controles_{D}.csv'
    for r in csv.DictReader(open(f)):
        if r['moneda'] == 'BTC': out[int(r['cierre'])] = (r['lado'], r['market_compra'])
    return out

class Q:
    __slots__ = ('rx', 'ex', 'bid', 'ask', 'bsz', 'asz')
    def __init__(self, rows):
        rows.sort(key=lambda r: (r[0], r[1]))
        a = np.array(rows, dtype=np.float64) if rows else np.zeros((0, 6))
        self.rx, self.ex = a[:, 0].astype(np.int64), a[:, 1].astype(np.int64)
        self.bid, self.ask, self.bsz, self.asz = a[:, 2], a[:, 3], a[:, 4], a[:, 5]
    def i(self, t):  # índice de la última fila con rx <= t (vectorizable)
        return np.searchsorted(self.rx, t, side='right') - 1

class T:
    __slots__ = ('rx', 'ex', 'p', 'buy', 'sz')
    def __init__(self, rows):
        rows.sort(key=lambda r: (r[0], r[1]))
        a = np.array(rows, dtype=np.float64) if rows else np.zeros((0, 5))
        self.rx, self.ex = a[:, 0].astype(np.int64), a[:, 1].astype(np.int64)
        self.p, self.buy, self.sz = a[:, 2], a[:, 3].astype(bool), a[:, 4]

def nan(x):
    return np.nan if x in ('', 'None') else float(x)

def grupos(D):
    """Itera (C15, {token: Q}, {token: T}) del extracto del día."""
    cur, q, t = None, collections.defaultdict(list), collections.defaultdict(list)
    with gzip.open(O + f'rows_{D}.csv.gz', 'rt') as fh:
        for ln in fh:
            c = ln.rstrip('\n').split(',')
            g = int(c[0])
            if g != cur:
                if cur is not None: yield cur, {k: Q(v) for k, v in q.items()}, {k: T(v) for k, v in t.items()}
                cur, q, t = g, collections.defaultdict(list), collections.defaultdict(list)
            try:
                if c[1] == 'q':
                    rx = int(c[8]) if c[8] else int(c[2])
                    q[c[3]].append((rx, int(c[2]), nan(c[4]), nan(c[5]), nan(c[6]) if c[6] else 0.0, nan(c[7]) if c[7] else 0.0))
                elif c[1] == 't':
                    rx = int(c[7]) if c[7] else int(c[2])
                    t[c[3]].append((rx, int(c[2]), float(c[4]), 1.0 if c[5] == 'BUY' else 0.0, float(c[6])))
            except (ValueError, IndexError):
                pass
    if cur is not None: yield cur, {k: Q(v) for k, v in q.items()}, {k: T(v) for k, v in t.items()}

def binance(D):
    """BTCUSDT aggTrades: (rx, E, precio), ordenado por rx y por E por separado."""
    rows = []
    with gzip.open(O + f'x_{D}.csv.gz', 'rt') as fh:
        for ln in fh:
            c = ln.split(',')
            try: rows.append((int(c[7]), int(c[6]), float(c[3])))
            except (ValueError, IndexError): pass
    a = np.array(rows, dtype=np.float64)
    o = np.argsort(a[:, 0], kind='stable'); r = a[o]
    o2 = np.argsort(a[:, 1], kind='stable'); e = a[o2]
    return dict(rx=r[:, 0].astype(np.int64), prx=r[:, 2], E=e[:, 1].astype(np.int64), pE=e[:, 2], lat=(a[:, 0] - a[:, 1]))

def bin_ret(B, t, w, clock='rx'):
    """Retorno (bps) de Binance entre t-w y t en el reloj dado (rx = visible para nosotros)."""
    ts, p = (B['rx'], B['prx']) if clock == 'rx' else (B['E'], B['pE'])
    i = np.searchsorted(ts, t, side='right') - 1; j = np.searchsorted(ts, t - w, side='right') - 1
    ok = (i >= 0) & (j >= 0)
    out = np.full(np.shape(t), np.nan)
    out[ok] = (p[i[ok]] / p[j[ok]] - 1) * 1e4
    return out
