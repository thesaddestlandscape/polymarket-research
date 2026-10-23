#!/usr/bin/env python3
"""s5_run_sim.py DIA... [--coins BTC,ETH,SOL,XRP] -- ejecuta cosechar_sim sobre ms5_<MONEDA>_<DIA>.npz. Idempotente: un (moneda, dia) con sim_*.csv.gz valido no se repite.
Salida DL/m5_cosechar_abrir/sim_<MONEDA>_<DIA>.csv.gz (clave unica dia,coin,mid,pol) + cobertura_<MONEDA>_<DIA>.json. Desenlace OFICIAL (gamma/ v2 tokens) o el mercado se excluye y se cuenta."""
import sys, os, json, gzip, hashlib, itertools, time, numpy as np, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, '/root/polymarket-research')
import cosechar_sim as S
from analisis_maker_cancelacion_binance import desenlaces
OUT = S.OUT
POLS = [(f'P{int(p*100)}_{d}_{r}', p, d, r, 0) for p in (0.96, 0.98) for d in ('A0', 'A_BN', 'B_15') for r in ('OPT', 'BASE', 'CONS')]
POLS += [('JOIN_A0_' + r, 'JOIN', 'A0', r, 0) for r in ('OPT', 'BASE', 'CONS')]
POLS += [('CTL60_P96_A0_BASE', 0.96, 'A0', 'BASE', 60000), ('CTL120_P96_A0_BASE', 0.96, 'A0', 'BASE', 120000)]
CODE_SHA = hashlib.sha256(open(S.__file__, 'rb').read() + open(__file__, 'rb').read()).hexdigest()[:16]
def run(coin, d):
    of = f'{OUT}/sim_{coin}_{d}.csv.gz'
    if os.path.exists(of):
        try:
            x = pd.read_csv(of, usecols=['code']); 
            if len(x) and x.code.iloc[0] == CODE_SHA: print(coin, d, 'ya (code igual)'); return
        except Exception: pass
    D = S.Dia5(coin, d)
    mk = {}
    for (marco, fin, lado), k in D.idx.items():
        if marco != '5min': continue
        mk.setdefault(fin, {})[lado] = k
    mids = {int(pd.Timestamp(str(D.tmap[k][3])).timestamp()): str(D.tmap[k][2]) for (marco, fin, lado), k in D.idx.items() if marco == '5min'}
    des = desenlaces(sorted(set(mids.values())))
    day0 = int(pd.Timestamp(d, tz='UTC').timestamp()); rows = []
    cov = dict(coin=coin, dia=d, esperados=0, sin_par=0, sin_datos=0, sin_desenlace=0, procesados=0)
    for fin, pr in sorted(mk.items()):
        if not (day0 <= fin - 300 < day0 + 86400): continue          # solo mercados que ABREN en el dia
        cov['esperados'] += 1
        if 'YES' not in pr or 'NO' not in pr: cov['sin_par'] += 1; continue
        kY, kN = pr['YES'], pr['NO']; fm = fin * 1000; t0 = fm - 300000
        ty, tn = D.top(kY, t0 + 50), D.top(kN, t0 + 50)
        ay = D.qs[kY + 1] - D.qs[kY]
        if ty is None or tn is None: cov['sin_datos'] += 1; continue
        # el dato debe ser de la ventana (ultimo q <= t0+50 no mas viejo de 20 s)
        a = D.qs[kY]; j = np.searchsorted(D.qr[a:D.qs[kY + 1]], t0 + 50, 'right') - 1
        if t0 + 50 - D.qr[a + j] > 20000: cov['sin_datos'] += 1; continue
        dd = des.get(mids[fin])
        if dd not in ('YES', 'NO'): cov['sin_desenlace'] += 1; continue
        k15Y = D.idx.get(('15min', fin, 'YES')) if fin % 900 == 0 else None; k15N = D.idx.get(('15min', fin, 'NO')) if fin % 900 == 0 else None
        cov['procesados'] += 1
        for nom, par, defensa, reg, off in POLS:
            r = S.simular_mercado(D, kY, kN, fm, mids[fin], par, defensa, reg, k15Y, k15N, off)
            if r is None: continue                                   # B_15 sin 15m: no aplica
            res, px = r
            u = S.unidad(res, px, dd, t0)
            rows.append(dict(dia=d, coin=coin, mid=mids[fin], fin=fin, con15=int(k15Y is not None), pol=nom, des=dd, **u))
    df = pd.DataFrame(rows); df['code'] = CODE_SHA
    tmp = of + '.tmp'; df.to_csv(tmp, index=False, compression='gzip'); os.replace(tmp, of)
    json.dump(cov, open(f'{OUT}/cobertura_{coin}_{d}.json', 'w'))
    print(coin, d, cov, 'filas', len(df), flush=True)
if __name__ == '__main__':
    args = sys.argv[1:]; coins = S.COINS
    if '--coins' in args:
        i = args.index('--coins'); coins = tuple(args[i + 1].split(',')); del args[i:i + 2]
    for d in args:
        for c in coins:
            if os.path.exists(f'{OUT}/ms5_{c}_{d}.npz'): run(c, d)
            else: print(c, d, 'FALTA npz')
