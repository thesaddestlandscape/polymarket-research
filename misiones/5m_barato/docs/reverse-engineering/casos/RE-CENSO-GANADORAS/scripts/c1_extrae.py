#!/usr/bin/env python3
"""RE-CENSO c1: censo on-chain 5m (6 monedas, todas las bandas, maker y tomador) por dia, agregado por wallet.
Solo lectura de VOL/m5_onchain y registros k; desenlace = union de caches existentes (sin red). Idempotente: salta dias hechos.
Uso: nice -n 19 ionice -c3 python3 c1_extrae.py [dias...]   Salida: VOL/agentes_datos/re_censo/{A,W}_D.parquet + manifest.json"""
import sys, os, gzip, json, time, hashlib
sys.path.insert(0, '/root/polymarket-research')
import numpy as np, pandas as pd
from analisis_5m_barato_quien_gana import mapas, EXCH
from archivo_volumen import VOL

OUT = VOL / 'agentes_datos' / 're_censo'
OUT.mkdir(parents=True, exist_ok=True)
DL = '/root/polymarket-research-datalogs'
DES = {}
for f in (DL + '/maker_ms_desenlaces_cache.json', DL + '/mapa_escala/des.json', DL + '/desenlaces_por_market_id_cache.json',
          '/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/b_vs_poblacion/datos/des_gamma.json'):
    try:
        d = json.load(open(f))
        for k, v in d.items():
            if v in ('YES', 'NO') and str(k) not in DES:
                DES[str(k)] = v
    except Exception as e:
        print('aviso des', f, e, file=sys.stderr)
PB = np.array([0, .01, .05, .10, .20, .30, .50, .70, .90, .99, 1.0001])
TB = np.array([-1e9, 0, 10, 60, 150, 300, 1e9])
SHA = hashlib.sha256(open(__file__, 'rb').read()).hexdigest()[:16]
MAN = OUT / 'manifest.json'
man = json.load(open(MAN)) if MAN.exists() else {'script_sha': SHA, 'dias': {}}
dias = sys.argv[1:] or ['2026-10-%02d' % d for d in range(5, 26)]


def carga_ok():
    # Javi 26-Oct: 8 nucleos -> load5 < 8 y MemAvailable > 2,5 GB; nunca 06:00-09:30Z
    mem = int([l for l in open('/proc/meminfo') if l.startswith('MemAvailable')][0].split()[1]) / 1e6
    h = time.gmtime(); hm = h.tm_hour * 60 + h.tm_min
    return os.getloadavg()[1] < 8.0 and mem > 2.5 and not (360 <= hm < 570)


for d in dias:
    if man['dias'].get(d, {}).get('estado') == 'COMPLETE' and (OUT / f'A_{d}.parquet').exists():
        continue
    while not carga_ok():
        time.sleep(60)
    t0 = time.time()
    tok = mapas(d)['5min']
    f = VOL / 'm5_onchain' / f'm5_onchain_{d}.csv.gz'
    if not f.exists():
        man['dias'][d] = {'estado': 'SIN_DATOS'}; continue
    parts = []; nrows = 0; nsin = 0
    with gzip.open(f, 'rt') as fh:
        for x in pd.read_csv(fh, chunksize=300_000, dtype={'token_id': str, 'maker': str, 'taker': str},
                             usecols=['tipo', 'ts_est', 'maker', 'taker', 'side', 'token_id', 'maker_amt', 'taker_amt', 'fee']):
            x = x[x.tipo == 'F']; nrows += len(x)
            k = x.token_id.map(tok)
            nsin += int(k.isna().sum()); x = x[k.notna()]; k = k[k.notna()]
            if not len(x):
                continue
            buy = x.side.values == 0
            acc = np.where(buy, x.taker_amt.values, x.maker_amt.values).astype(float)
            usd = np.where(buy, x.maker_amt.values, x.taker_amt.values).astype(float)
            p = np.divide(usd, acc, out=np.zeros_like(usd), where=acc > 0)
            mkt = k.map(lambda v: str(v[1])).values; lado = k.map(lambda v: v[3]).values
            cierre = k.map(lambda v: v[2]).values.astype(float)
            des = pd.Series(mkt).map(DES).values
            cob = pd.notna(des)
            gana = (des == lado).astype(float)
            rolT = x.taker.values == EXCH
            fee = x.fee.astype(float).values
            pnl = np.where(buy, acc * gana - usd, usd - acc * gana)
            reb = np.where(~rolT, 0.2 * 0.07 * acc * p * (1 - p), 0.0)
            parts.append(pd.DataFrame({'w': x.maker.str.lower().values, 'rol': np.where(rolT, 'T', 'M'),
                                       'act': k.map(lambda v: v[0]).values, 'mkt': mkt, 'lado': lado, 'buy': buy,
                                       'pb': np.digitize(p, PB) - 1, 'tb': np.digitize(cierre - x.ts_est.astype(float).values, TB) - 1,
                                       'pnl': np.where(cob, pnl, 0.0), 'fee': fee, 'reb': reb, 'usd': usd, 'acc': acc,
                                       'cob': cob, 'usd_sin': np.where(cob, 0.0, usd)}))
    X = pd.concat(parts, ignore_index=True)
    cobertura = 1 - X.usd_sin.sum() / X.usd.sum()
    X['n'] = 1
    A = X.groupby(['w', 'rol', 'act', 'pb', 'tb'], observed=True)[['pnl', 'fee', 'reb', 'usd', 'acc', 'n', 'usd_sin']].sum().reset_index()
    A['dia'] = d
    ml = X.groupby(['w', 'mkt']).lado.nunique()
    W = pd.DataFrame({'n_mkt': ml.groupby(level=0).size(), 'n_mkt_2lados': (ml > 1).groupby(level=0).sum()})
    W['dia'] = d
    A.to_parquet(OUT / f'A_{d}.parquet.tmp'); os.replace(OUT / f'A_{d}.parquet.tmp', OUT / f'A_{d}.parquet')
    W.reset_index().to_parquet(OUT / f'W_{d}.parquet.tmp'); os.replace(OUT / f'W_{d}.parquet.tmp', OUT / f'W_{d}.parquet')
    man['dias'][d] = {'estado': 'COMPLETE', 'filas_F': nrows, 'filas_sin_mapa': nsin, 'filas_5m': len(X),
                      'cobertura_desenlace_usd': round(float(cobertura), 5), 'wallets': int(A.w.nunique()), 'seg': round(time.time() - t0, 1)}
    man['script_sha'] = SHA
    json.dump(man, open(str(MAN) + '.tmp', 'w'), indent=1); os.replace(str(MAN) + '.tmp', MAN)
    print(d, man['dias'][d], flush=True)
    del X, A, W, parts
