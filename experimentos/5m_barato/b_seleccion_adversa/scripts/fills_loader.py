"""Carga la cinta de rellenos MAKER de un dia (ETH/SOL/XRP, todas las bandas) -- extraido de build_units.all_fills (mismas reglas que pop.py).
S = carpeta con alt_DD.csv, gmap*.json, npbt.py (scratch de la sesion b_lecciones_wallets)."""
import json, numpy as np, pandas as pd
EX = '0xe111180000d2663c0091e4f400237545b87b996b'
CA = '/mnt/HC_Volume_106538179/datalogs_analisis_caches/wallets_18oct/'
DES = None
COINS = ('ETH', 'SOL', 'XRP')
def all_fills(d, S):
    global DES
    if DES is None: DES = json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
    if d <= '2026-10-18':
        F = pd.read_parquet(CA + f'fills_{d}.parquet', columns=['tx', 'is_tk', 'maker', 'taker', 'side', 'act', 'mkt', 'lado', 'fin', 'ts', 'maker_amt', 'taker_amt'])
        F = F[(F.is_tk == 0) & F.act.isin(COINS)].drop(columns=['is_tk'])
        F['mkt'] = F.mkt.astype(np.int64); F['des'] = F.mkt.astype(str).map(DES)
    else:
        import os, sys
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        gp = '/root/polymarket-research-datalogs/sa_r1/gmap_%s.json' % d
        if not os.path.exists(gp):
            import r1_fwd_extract as X; X.gmap(d)
        gm = json.load(open(gp))
        tok = {}
        for slug, v in gm.items():
            st = int(slug.rsplit('-', 1)[1]); coin = slug.split('-')[0].upper()
            for t, l in zip(v['toks'], ('YES', 'NO')): tok[t] = (coin, int(v['id']), st + 300, l, v['des'])
        cols = ['tipo', 'bloque', 'ts', 'tx', 'li', 'oh', 'maker', 'taker', 'side', 'tok', 'maker_amt', 'taker_amt', 'fee']
        parts = []
        for ch in pd.read_csv('/root/polymarket-research-datalogs/onchain_fills_%s.csv.gz' % d, header=0, names=cols, dtype={'tok': str, 'tx': str, 'maker': str, 'taker': str},
                              usecols=['tipo', 'ts', 'tx', 'maker', 'taker', 'side', 'tok', 'maker_amt', 'taker_amt'], chunksize=500000, on_bad_lines='skip'):
            ch = ch[(ch.tipo == 'F') & (ch.taker.str.lower() != EX) & ch.tok.isin(tok.keys())]
            if len(ch): parts.append(ch.copy())
        F = pd.concat(parts, ignore_index=True)
        F['maker'] = F.maker.str.lower(); F['taker'] = F.taker.str.lower()
        for i, c in enumerate(['act', 'mkt', 'fin', 'lado', 'des']): F[c] = F.tok.map(lambda t, i=i: tok[t][i])
        F = F.drop(columns=['tipo', 'tok'])
        F = F[F.act.isin(COINS)]
    v = F.side.values == 1
    F['sh'] = np.where(v, F.maker_amt, F.taker_amt)
    F = F[F.sh > 0].copy()
    usd = np.where(F.side.values == 1, F.taker_amt, F.maker_amt)
    ptok = usd / F.sh.values
    F['lado_c'] = np.where(F.side.values == 1, np.where(F.lado == 'YES', 'NO', 'YES'), F.lado)
    F['pyes'] = np.where(F.lado.values == 'YES', ptok, 1 - ptok)
    F['pc'] = np.where(F.lado_c.values == 'YES', F.pyes.values, 1 - F.pyes.values)
    F['flow_yes'] = np.where(F.lado_c.values == 'NO', F.sh.values, -F.sh.values)
    F['ts'] = F.ts.astype(float)
    return F[['tx', 'maker', 'taker', 'act', 'mkt', 'fin', 'ts', 'sh', 'pyes', 'pc', 'flow_yes', 'des', 'lado_c']].reset_index(drop=True)
