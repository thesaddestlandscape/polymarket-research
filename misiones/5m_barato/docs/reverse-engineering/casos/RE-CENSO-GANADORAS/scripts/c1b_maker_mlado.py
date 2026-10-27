#!/usr/bin/env python3
"""RE-CENSO c1b: rellenos MAKER y TOMADOR por (wallet, dia, moneda, mercado, lado, banda 0,05) en p<0,40 y p>=0,70 (unidad mercado-lado).
Solo lectura de VOL/m5_onchain; desenlace = union de caches. Idempotente por dia; guarda de carga (load5<8, Mem>2,5 GB, fuera de 06:00-09:30Z).
Salida: VOL/agentes_datos/re_censo/U_D.parquet + manifest_u.json"""
import sys, os, gzip, json, time
sys.path.insert(0, '/root/polymarket-research')
import numpy as np, pandas as pd
from analisis_5m_barato_quien_gana import mapas, EXCH
from archivo_volumen import VOL

OUT = VOL / 'agentes_datos' / 're_censo'
DL = '/root/polymarket-research-datalogs'
DES = {}
for f in (DL + '/maker_ms_desenlaces_cache.json', DL + '/mapa_escala/des.json', DL + '/desenlaces_por_market_id_cache.json',
          '/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/b_vs_poblacion/datos/des_gamma.json'):
    try:
        for k, v in json.load(open(f)).items():
            if v in ('YES', 'NO'): DES.setdefault(str(k), v)
    except Exception as e:
        print('aviso des', f, e, file=sys.stderr)
MAN = OUT / 'manifest_u.json'
man = json.load(open(MAN)) if MAN.exists() else {'dias': {}}


def carga_ok():
    mem = int([l for l in open('/proc/meminfo') if l.startswith('MemAvailable')][0].split()[1]) / 1e6
    h = time.gmtime(); hm = h.tm_hour * 60 + h.tm_min
    return os.getloadavg()[1] < 8.0 and mem > 2.5 and not (360 <= hm < 570)


for d in (sys.argv[1:] or ['2026-10-%02d' % x for x in range(5, 26)]):
    if man['dias'].get(d, {}).get('estado') == 'COMPLETE' and (OUT / f'U_{d}.parquet').exists():
        continue
    while not carga_ok():
        time.sleep(60)
    t0 = time.time(); tok = mapas(d)['5min']; parts = []
    with gzip.open(VOL / 'm5_onchain' / f'm5_onchain_{d}.csv.gz', 'rt') as fh:
        for x in pd.read_csv(fh, chunksize=300_000, dtype={'token_id': str, 'maker': str, 'taker': str},
                             usecols=['tipo', 'ts_est', 'maker', 'taker', 'side', 'token_id', 'maker_amt', 'taker_amt', 'fee']):
            x = x[x.tipo == 'F']; k = x.token_id.map(tok); x = x[k.notna()]; k = k[k.notna()]
            if not len(x): continue
            buy = x.side.values == 0
            acc = np.where(buy, x.taker_amt.values, x.maker_amt.values).astype(float)
            usd = np.where(buy, x.maker_amt.values, x.taker_amt.values).astype(float)
            p = np.divide(usd, acc, out=np.zeros_like(usd), where=acc > 0)
            # unidad = lado COMPRADO equivalente: una venta de s a p = compra del complementario a 1-p
            lado = k.map(lambda v: v[3]).values
            lado_c = np.where(buy, lado, np.where(lado == 'YES', 'NO', 'YES'))
            pc = np.where(buy, p, 1 - p)
            sel = (pc < 0.40) | (pc >= 0.70)
            if not sel.any(): continue
            mkt = k.map(lambda v: str(v[1])).values
            des = pd.Series(mkt).map(DES).values
            gana = (des == lado_c).astype(float); cob = pd.notna(des)
            rolT = x.taker.values == EXCH
            cost = acc * pc   # coste del lado comprado equivalente
            pnl = np.where(cob, acc * gana - cost, 0.0) - np.where(rolT, x.fee.astype(float).values, 0.0)
            reb = np.where(~rolT, 0.2 * 0.07 * acc * p * (1 - p), 0.0)
            T = k.map(lambda v: v[2]).values.astype(float) - x.ts_est.astype(float).values
            parts.append(pd.DataFrame({'w': x.maker.str.lower().values, 'rol': np.where(rolT, 'T', 'M'), 'act': k.map(lambda v: v[0]).values,
                                       'mkt': mkt, 'lado': lado_c, 'b05': np.floor(pc / 0.05).astype(int), 'pnl': pnl, 'reb': reb, 'c': cost,
                                       'acc': acc, 'T': T, 'cob': cob})[sel])
    X = pd.concat(parts, ignore_index=True)
    X['n'] = 1; X['Tc'] = X['T'] * X.c
    U = X.groupby(['w', 'rol', 'act', 'mkt', 'lado', 'b05'], observed=True).agg(pnl=('pnl', 'sum'), reb=('reb', 'sum'), c=('c', 'sum'), acc=('acc', 'sum'),
                                                                                  n=('n', 'sum'), Tc=('Tc', 'sum'), cob=('cob', 'min')).reset_index()
    U['dia'] = d
    U.to_parquet(OUT / f'U_{d}.parquet.tmp'); os.replace(OUT / f'U_{d}.parquet.tmp', OUT / f'U_{d}.parquet')
    man['dias'][d] = {'estado': 'COMPLETE', 'filas_sel': len(X), 'unidades': len(U), 'cobertura_c': round(float(X.c[X.cob].sum() / X.c.sum()), 5), 'seg': round(time.time() - t0, 1)}
    json.dump(man, open(str(MAN) + '.tmp', 'w'), indent=1); os.replace(str(MAN) + '.tmp', MAN)
    print(d, man['dias'][d], flush=True)
    del X, U, parts
