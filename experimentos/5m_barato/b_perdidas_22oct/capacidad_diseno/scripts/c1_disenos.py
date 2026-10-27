#!/usr/bin/env python3
"""CAPACIDAD-DISENO c1: nocional maker/tomador por marco x moneda x banda y EV de DISENOS (celdas disjuntas).
Fuente: mapa_escala/datos/{niche_dia.csv, niche_fin.csv.gz, niches.csv} (rellenos on-chain MAKER 06..21-Oct,
desenlace oficial 100 %, T en (60,L]). Solo lectura. EV = sum pnl / sum coste (ponderado por EUR), maker sin fee, sin rebate.
Taker pop = contraparte exacta: pnl_t = -pnl_m - fee_total (fee_total = 5*reb, porque reb = 0,2*fee), coste_t = acc - coste_m.
IC90: bootstrap de dias (2000, semilla 20261024) y de cierres (1000, cluster = fin, todas las monedas del mismo fin juntas).
"""
import csv, gzip, sys, collections
import numpy as np
D = '/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/mapa_escala/datos/'
OUT = '/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/capacidad_diseno/datos/'
BANDAS = ['0.01-0.05','0.05-0.10','0.10-0.20','0.20-0.30','0.30-0.50','0.50-0.70','0.70-0.90','0.90-0.99']
bi = {b: i for i, b in enumerate(BANDAS)}
ALT3 = ['ETH','SOL','XRP']; ALL = ['BTC','ETH','SOL','XRP','DOGE','BNB']
rng = np.random.default_rng(20261024)

# --- carga por dia
dia = collections.defaultdict(lambda: np.zeros(4))   # (marco,coin,banda,dia) -> coste,pnl,reb,acc
dias_marco = collections.defaultdict(set)
for x in csv.DictReader(open(D + 'niche_dia.csv')):
    k = (x['marco'], x['coin'], int(x['banda']), x['dia'])
    dia[k] += np.array([float(x['coste']), float(x['pnl']), float(x['reb']), float(x['acc'])])
    dias_marco[x['marco']].add(x['dia'])
# --- carga por cierre
fin = collections.defaultdict(lambda: np.zeros(2))   # (marco,coin,banda,fin) -> coste,pnl
fin_dia = {}
for x in csv.DictReader(gzip.open(D + 'niche_fin.csv.gz', 'rt')):
    k = (x['marco'], x['coin'], int(x['banda']), x['fin'])
    fin[k] += np.array([float(x['coste']), float(x['pnl'])])
    fin_dia[x['fin']] = x['dia']

def agg_dias(marco, coins, bandas):
    out = collections.defaultdict(lambda: np.zeros(4))
    for (m, c, b, d), v in dia.items():
        if m == marco and c in coins and b in [bi[z] for z in bandas]:
            out[d] += v
    return out

def agg_fin(marco, coins, bandas):
    out = collections.defaultdict(lambda: np.zeros(2))
    bs = [bi[z] for z in bandas]
    for (m, c, b, f), v in fin.items():
        if m == marco and c in coins and b in bs:
            out[f] += v
    return out

def ratio(a):  # a: array n x 2 (coste,pnl)
    return a[:, 1].sum() / a[:, 0].sum() if a[:, 0].sum() > 0 else np.nan

def boot(arr, B):
    n = len(arr); r = []
    for _ in range(B):
        idx = rng.integers(0, n, n); r.append(ratio(arr[idx]))
    return np.nanpercentile(r, [5, 95])

def evaluar(nombre, marco, coins, bandas, detalle=True):
    ad = agg_dias(marco, coins, bandas)
    ds = sorted(ad)
    A = np.array([ad[d] for d in ds])                    # coste,pnl,reb,acc
    nd = len(ds)
    cost, pnl, reb, acc = A.sum(0)
    ev = pnl / cost
    # IC dias
    ic_d = boot(A[:, [0, 1]], 2000)
    # DESC/OOS (mitad cronologica; igual que el mapa: 06..13 / 14..)
    desc = [i for i, d in enumerate(ds) if d <= '2026-10-13']; oos = [i for i, d in enumerate(ds) if d > '2026-10-13']
    ev_desc = ratio(A[desc][:, [0, 1]]) if desc else np.nan
    ev_oos = ratio(A[oos][:, [0, 1]]) if oos else np.nan
    # sin 2 mejores dias (por pnl)
    orden = np.argsort(-A[:, 1]); keep = np.setdiff1d(np.arange(nd), orden[:2])
    ev_s2 = ratio(A[keep][:, [0, 1]]) if len(keep) else np.nan
    dpos = int((A[:, 1] > 0).sum())
    # cierres
    af = agg_fin(marco, coins, bandas)
    F = np.array([af[f] for f in af]) if af else np.zeros((0, 2))
    ic_c = boot(F, 1000) if len(F) > 5 else (np.nan, np.nan)
    o5 = np.argsort(-F[:, 1])[:5]; k5 = np.setdiff1d(np.arange(len(F)), o5)
    ev_s5c = ratio(F[k5]) if len(F) > 10 else np.nan
    # tomador (contraparte exacta)
    cost_t = acc - cost; pnl_t = -pnl - 5 * reb
    ev_t = pnl_t / cost_t if cost_t > 0 else np.nan
    res = dict(nombre=nombre, marco=marco, coins='+'.join(coins) if len(coins) < 6 else 'ALL', bandas=bandas[0] + '..' + bandas[-1] if len(bandas) > 1 else bandas[0],
               dias=nd, vol_dia=cost / nd, ev=ev, ic_d_lo=ic_d[0], ic_d_hi=ic_d[1], ic_c_lo=ic_c[0], ic_c_hi=ic_c[1], dpos=dpos,
               ev_sin2d=ev_s2, ev_sin5c=ev_s5c, ev_desc=ev_desc, ev_oos=ev_oos, ev_reb=(pnl + reb) / cost, reb_dia=reb / nd,
               vol_tomador_dia=cost_t / nd, ev_tomador=ev_t, cierres=len(F))
    return res

DIS = [
 # B y vecinos 5m
 ('B: 5m ALT3 0,10-0,30',            '5min', ALT3, ['0.10-0.20','0.20-0.30']),
 ('5m ALT3 0,05-0,10',                '5min', ALT3, ['0.05-0.10']),
 ('5m BNB+DOGE 0,10-0,30',            '5min', ['BNB','DOGE'], ['0.10-0.20','0.20-0.30']),
 ('5m BTC 0,10-0,20',                 '5min', ['BTC'], ['0.10-0.20']),
 ('5m BTC 0,20-0,30',                 '5min', ['BTC'], ['0.20-0.30']),
 ('5m ALL 0,10-0,30',                 '5min', ALL, ['0.10-0.20','0.20-0.30']),
 ('5m ALL 0,05-0,10',                 '5min', ALL, ['0.05-0.10']),
 ('5m ALL 0,01-0,05',                 '5min', ALL, ['0.01-0.05']),
 ('5m ALL 0,01-0,10 (N4)',            '5min', ALL, ['0.01-0.05','0.05-0.10']),
 ('5m ALL 0,30-0,50',                 '5min', ALL, ['0.30-0.50']),
 ('5m ALL 0,50-0,70',                 '5min', ALL, ['0.50-0.70']),
 ('5m ALL 0,70-0,90',                 '5min', ALL, ['0.70-0.90']),
 ('5m ALL 0,90-0,99',                 '5min', ALL, ['0.90-0.99']),
 ('5m BTC 0,90-0,99',                 '5min', ['BTC'], ['0.90-0.99']),
 ('5m ALT3 0,90-0,99',                '5min', ALT3, ['0.90-0.99']),
 # 15m
 ('15m ALL 0,01-0,10',                '15min', ALL, ['0.01-0.05','0.05-0.10']),
 ('15m ALL 0,10-0,30',                '15min', ALL, ['0.10-0.20','0.20-0.30']),
 ('15m ALT3 0,10-0,30',               '15min', ALT3, ['0.10-0.20','0.20-0.30']),
 ('15m BTC 0,10-0,30',                '15min', ['BTC'], ['0.10-0.20','0.20-0.30']),
 ('15m ALL 0,30-0,50',                '15min', ALL, ['0.30-0.50']),
 ('15m ALL 0,50-0,70',                '15min', ALL, ['0.50-0.70']),
 ('15m ETH 0,70-0,99',                '15min', ['ETH'], ['0.70-0.90','0.90-0.99']),
 ('15m ALT3 0,70-0,99',               '15min', ALT3, ['0.70-0.90','0.90-0.99']),
 ('15m ALL 0,70-0,99',                '15min', ALL, ['0.70-0.90','0.90-0.99']),
 ('15m BTC 0,70-0,99',                '15min', ['BTC'], ['0.70-0.90','0.90-0.99']),
 # 60m/4h/24h (4 dias: descriptivo)
 ('60m ALL 0,70-0,90',                '60min', ALL, ['0.70-0.90']),
 ('60m ALL 0,90-0,99',                '60min', ALL, ['0.90-0.99']),
 ('60m ALL 0,10-0,30',                '60min', ALL, ['0.10-0.20','0.20-0.30']),
 ('4h ALL 0,90-0,99',                 '240min', ALL, ['0.90-0.99']),
 ('4h ALL 0,30-0,50',                 '240min', ALL, ['0.30-0.50']),
 ('24h ALL 0,30-0,50',                '24h', ALL, ['0.30-0.50']),
]
if __name__ == '__main__':
    rows = []
    for n, m, c, b in DIS:
        try:
            rows.append(evaluar(n, m, c, b))
        except Exception as e:
            print('ERR', n, e, file=sys.stderr)
    keys = list(rows[0].keys())
    with open(OUT + 'disenos.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, keys); w.writeheader()
        for r in rows: w.writerow({k: (round(v, 5) if isinstance(v, float) else v) for k, v in r.items()})
    for r in rows:
        print(f"{r['nombre']:26s} d={r['dias']:2d} vol/d={r['vol_dia']:>10,.0f} EV={r['ev']:+.3f} ICd=({r['ic_d_lo']:+.3f},{r['ic_d_hi']:+.3f}) ICc=({r['ic_c_lo']:+.3f},{r['ic_c_hi']:+.3f}) d+={r['dpos']}/{r['dias']} s2d={r['ev_sin2d']:+.3f} s5c={r['ev_sin5c']:+.3f} DESC={r['ev_desc']:+.3f} OOS={r['ev_oos']:+.3f} +reb={r['ev_reb']:+.3f} rebdia={r['reb_dia']:.0f} | TOM vol={r['vol_tomador_dia']:,.0f} EV={r['ev_tomador']:+.3f}")
