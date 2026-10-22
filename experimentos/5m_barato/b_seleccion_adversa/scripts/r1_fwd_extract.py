#!/usr/bin/env python3
"""r1_fwd_extract.py [DIA ...] -- extraccion diaria on-chain para el forward de R1 (solo medicion, no toca B).
Lee datalogs/onchain_fills_DIA.csv.gz (retencion 4 d) -> unidades (primeras 5 acc por maker-mercado-lado, pc 0,10-0,30, T 60-300, ETH/SOL/XRP 5m,
sin la wallet dedicada) con vol30 (acc casadas en el mercado en los 30 s previos a ts-4 s) y hora UTC (ts-2,4 s). Salida:
/root/polymarket-research-datalogs/sa_r1/units_DIA.csv.gz (retencion 90 d) + gmap cache. Sin argumentos: ayer y anteayer (idempotente).
Solo escribe si la cobertura de desenlace >= 99 %; si no, sale con codigo 3 (se reintenta al dia siguiente mientras el on-chain no rote)."""
import sys, os, json, time, gzip, requests
import numpy as np, pandas as pd
from datetime import datetime, timedelta, timezone
DL = '/root/polymarket-research-datalogs/'; OUTD = DL + 'sa_r1/'; os.makedirs(OUTD, exist_ok=True)
EX = '0xe111180000d2663c0091e4f400237545b87b996b'; US = '0x659a40ff9920febc5a66836213040924343d297f'
COINS = ('eth', 'sol', 'xrp')
def gmap(d):
    f = OUTD + f'gmap_{d}.json'
    old = json.load(open(f)) if os.path.exists(f) else {}
    t0 = int(datetime.fromisoformat(d).replace(tzinfo=timezone.utc).timestamp())
    slugs = [f'{c}-updown-5m-{s}' for c in COINS for s in range(t0 - 300, t0 + 86400 + 300, 300)]
    ses = requests.Session(); out = dict(old)
    pend = [s for s in slugs if s not in out or (out[s].get('des') is None)]
    for k in range(0, len(pend), 40):
        for closed in ('true', 'false'):
            try:
                r = ses.get('https://gamma-api.polymarket.com/markets', timeout=25, params=[('slug', s) for s in pend[k:k + 40]] + [('closed', closed), ('limit', '40')]).json()
            except Exception as e:
                print('gamma err', e, file=sys.stderr); continue
            for m in r:
                toks = json.loads(m['clobTokenIds']) if isinstance(m.get('clobTokenIds'), str) else m.get('clobTokenIds')
                pr = m.get('outcomePrices'); pr = json.loads(pr) if isinstance(pr, str) else pr
                des = None
                if m.get('closed') and pr:
                    if float(pr[0]) >= 0.999: des = 'YES'
                    elif float(pr[1]) >= 0.999: des = 'NO'
                if m['slug'] not in out or des or not out[m['slug']].get('des'):
                    out[m['slug']] = dict(id=str(m['id']), toks=toks, des=des)
        time.sleep(0.15)
    json.dump(out, open(f, 'w'))
    return out
def extract(d):
    gm = gmap(d); tok = {}
    for slug, v in gm.items():
        st = int(slug.rsplit('-', 1)[1]); coin = slug.split('-')[0].upper()
        for t, l in zip(v['toks'], ('YES', 'NO')): tok[t] = (coin, int(v['id']), st + 300, l, v['des'])
    nm = len(gm); cob = np.mean([v['des'] is not None for v in gm.values()]) if nm else 0
    path = DL + f'onchain_fills_{d}.csv.gz'
    if not os.path.exists(path): print(d, 'sin on-chain'); return 2
    cols = ['tipo', 'bloque', 'ts', 'tx', 'li', 'oh', 'maker', 'taker', 'side', 'tok', 'maker_amt', 'taker_amt', 'fee']
    parts = []
    for ch in pd.read_csv(path, header=0, names=cols, dtype={'tok': str, 'tx': str, 'maker': str, 'taker': str}, usecols=['tipo', 'ts', 'maker', 'taker', 'side', 'tok', 'maker_amt', 'taker_amt'], chunksize=500000, on_bad_lines='skip'):
        ch = ch[(ch.tipo == 'F') & (ch.taker.str.lower() != EX) & ch.tok.isin(tok.keys())]
        if len(ch): parts.append(ch.copy())
    F = pd.concat(parts, ignore_index=True)
    F['maker'] = F.maker.str.lower()
    for i, c in enumerate(['act', 'mkt', 'fin', 'lado', 'des']): F[c] = F.tok.map(lambda t, i=i: tok[t][i])
    F = F.drop(columns=['tipo', 'tok', 'taker'])
    v = F.side.values == 1
    F['sh'] = np.where(v, F.maker_amt, F.taker_amt); usd = np.where(v, F.taker_amt, F.maker_amt)
    F = F[F.sh > 0].copy(); v = F.side.values == 1; usd = np.where(v, F.taker_amt, F.maker_amt)
    ptok = usd / F.sh.values
    F['lado_c'] = np.where(v, np.where(F.lado == 'YES', 'NO', 'YES'), F.lado)
    pyes = np.where(F.lado.values == 'YES', ptok, 1 - ptok)
    F['pc'] = np.where(F.lado_c.values == 'YES', pyes, 1 - pyes)
    F['ts'] = F.ts.astype(float); F['T'] = F.fin - F.ts
    F = F.sort_values(['mkt', 'ts']).reset_index(drop=True)
    # actividad por mercado: acciones acumuladas (todas las filas maker del mercado)
    cum = np.concatenate([[0], np.cumsum(F.sh.values)]); mk = F.mkt.values
    Fd = F[(F.maker != US) & F.des.notna() & (F.pc > 0.10) & (F.pc <= 0.30) & (F['T'] > 60) & (F['T'] <= 300)].copy()
    Fd = Fd.sort_values(['maker', 'mkt', 'lado_c', 'ts'])
    Fd['cum'] = Fd.groupby(['maker', 'mkt', 'lado_c']).sh.cumsum(); Fd['prev'] = Fd.cum - Fd.sh
    Fd = Fd[Fd.prev < 5].copy(); take = np.minimum(Fd.sh, 5 - Fd.prev); f = take / Fd.sh
    Fd['coste'] = Fd.sh * Fd.pc * f; Fd['gana'] = (Fd.lado_c == Fd.des)
    Fd['pnl'] = np.where(Fd.gana, take, 0.0) - Fd.coste; Fd['sh'] = take
    U = Fd.groupby(['maker', 'mkt', 'lado_c', 'act']).agg(c=('coste', 'sum'), p=('pnl', 'sum'), sh=('sh', 'sum'), T=('T', 'first'), pc=('pc', 'first'), fin=('fin', 'first'), gana=('gana', 'first'), ts=('ts', 'first')).reset_index()
    # vol30 por unidad: acciones del mercado con ts en (t_obs-30, t_obs], t_obs = ts-4
    key = F.mkt.values.astype(np.int64) * 10**7 + (F.ts.values - F.ts.values.min())
    t0 = F.ts.values.min(); ku = U.mkt.values.astype(np.int64) * 10**7
    i1 = np.searchsorted(key, ku + (U.ts.values - 4 - t0), side='right'); i0 = np.searchsorted(key, ku + (U.ts.values - 34 - t0), side='right')
    lo = np.searchsorted(key, ku, side='left'); i0 = np.maximum(i0, lo); i1 = np.maximum(i1, i0)
    U['vol30'] = cum[i1] - cum[i0]
    U['hora'] = pd.to_datetime(U.ts - 2.4, unit='s').dt.hour; U.insert(0, 'dia', d)
    U['R1a'] = U.vol30 >= 26; U['R1b'] = U.hora >= 4
    n_mkts = F.mkt.nunique()
    print(d, 'mercados con fills', n_mkts, 'de', nm, 'cobertura desenlace gamma %.3f' % cob, 'unidades', len(U), 'EUR', round(U.c.sum()), 'EV %.4f' % (U.p.sum() / U.c.sum()))
    if cob < 0.99: print(d, 'cobertura <99 %: no se escribe'); return 3
    U.to_csv(OUTD + f'units_{d}.csv.gz', index=False); return 0
if __name__ == '__main__':
    days = sys.argv[1:] or [(datetime.now(timezone.utc) - timedelta(i)).date().isoformat() for i in (1, 2)]
    rc = 0
    for d in days:
        if os.path.exists(OUTD + f'units_{d}.csv.gz') and not sys.argv[1:]: print(d, 'ya'); continue
        rc = max(rc, extract(d))
    for f in os.listdir(OUTD):    # retencion 90 d
        if f.startswith(('units_', 'gmap_')) and time.time() - os.path.getmtime(OUTD + f) > 90 * 86400: os.remove(OUTD + f)
    sys.exit(rc)
