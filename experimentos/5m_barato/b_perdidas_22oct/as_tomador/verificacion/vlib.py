"""vlib.py -- carga y derivados INDEPENDIENTES (revisor adversarial) a partir de f_DIA.parquet (v1_extract.py, crudo m5_onchain + m5_registro)."""
import json, numpy as np, pandas as pd
V = '/mnt/HC_Volume_106538179/agentes_datos/as_tomador/verif/'
EX = '0xe111180000d2663c0091e4f400237545b87b996b'; US = '0x659a40ff9920febc5a66836213040924343d297f'
DES = json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))   # mid(str)->'YES'/'NO' (gamma)
FEE = 0.07
_codes = {}
def code(s):
    out = np.empty(len(s), np.int32)
    for i, w in enumerate(s):
        c = _codes.get(w)
        if c is None: c = _codes[w] = len(_codes)
        out[i] = c
    return out
def inv(): return {v: k for k, v in _codes.items()}
def load_day(d):
    F = pd.read_parquet(V + 'f_%s.parquet' % d)
    venta = F.side.values == 1
    sh = np.where(venta, F.maker_amt.values, F.taker_amt.values)
    usd = np.where(venta, F.taker_amt.values, F.maker_amt.values)
    ladoc_yes = np.where(venta, F.lado.values == 'NO', F.lado.values == 'YES')     # el MAKER adquiere este lado
    with np.errstate(divide='ignore', invalid='ignore'):
        pc = np.where(venta, 1 - usd / sh, usd / sh)
    des = F.mid.astype(str).map(DES)
    dv = np.where(des.isna(), -1, np.where(des == 'YES', 1, 0)).astype(np.int8)
    gana = np.where(dv < 0, -1, (dv == ladoc_yes.astype(np.int8))).astype(np.int8)
    X = pd.DataFrame({'dia': d, 'ts': F.ts_est.values, 'mid': F.mid.values, 'fin': F.fin.values, 'coin': F.coin.values,
                      'yes': ladoc_yes, 'sh': sh, 'pc': pc, 'mk': code(F.maker.values), 'tk': code(F.taker.values), 'gana': gana,
                      'side': F.side.values.astype(np.int8), 'tx': F.tx.values, 'li': F.log_index.values})
    X['coste_m'] = X.sh * X.pc
    ok = (X.sh > 0) & (X.pc > 0) & (X.pc < 1)
    return X, ok
def pnl_m(X): return np.where(X.gana.values == 1, X.sh.values, 0.0) - X.coste_m.values
