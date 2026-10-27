"""cf_lib.py -- utilidades del CONTRAFACTUAL SHADOW 'tomadores informados' sobre B (solo lectura de produccion).
Semantica de lado/precio copiada de verificacion/vlib.py (side==1: el maker VENDE el token => compra el lado opuesto a 1-pc)."""
import gzip, json, subprocess, datetime as dt
import numpy as np, pandas as pd

EX = '0xe111180000d2663c0091e4f400237545b87b996b'     # contrato exchange (taker de las filas del lado 'orden maker')
US = '0x659a40ff9920febc5a66836213040924343d297f'     # wallet dedicada (B)
RG = '/mnt/HC_Volume_106538179/m5_registro/m5_registro_%s.csv.gz'
OC = '/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_%s.csv.gz'
DES_PATH = '/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'
CACHE = '/mnt/HC_Volume_106538179/agentes_datos/as_tomador/contrafactual/'   # fuera de git
COINS = ('ETH', 'SOL', 'XRP')


def dday(d, k):
    return (dt.date.fromisoformat(d) + dt.timedelta(days=k)).isoformat()


def token_map(d):
    """token_id -> (coin, mid, fin_epoch, lado) de las filas 'k' de m5_registro D-1, D, D+1 (5min ETH/SOL/XRP)."""
    tok = {}
    for k in (-1, 0, 1):
        try:
            p = subprocess.Popen("gzip -dc '%s' 2>/dev/null | grep -a '^k,'" % (RG % dday(d, k)), shell=True, stdout=subprocess.PIPE)
        except Exception:
            continue
        for ln in p.stdout:
            c = ln.decode().rstrip('\n').split(',')
            if len(c) >= 8 and c[4] == '5min' and c[3] in COINS:
                tok[c[2]] = (c[3], int(c[5]), int(dt.datetime.fromisoformat(c[6]).timestamp()), c[7])
        p.wait()
    return tok


PRE_PATH = '/root/polymarket-research-datalogs/precierre_desenlaces_cache.json'   # slug -> 'Up'/'Down' (oficial; cobertura completa, 0 discrepancias vs DES en 1.772 mercados del 22-Oct)


def load_des():
    """Devuelve (DES mid->'YES'/'NO', PRE slug->'Up'/'Down'). DES manda; PRE rellena los mercados que DES aun no tiene (Up==YES)."""
    return json.load(open(DES_PATH)), json.load(open(PRE_PATH))


def fills_dia(d, des, chunk=60000):
    """Filas F (relleno de una orden maker; taker != contrato) 5m ETH/SOL/XRP del archivo on-chain del dia d, con derivados.
    Devuelve DataFrame compacto: ts,coin,mid,fin,yes,sh,pc,maker,taker,gana(-1 sin desenlace),tx,li. Solo resueltos NO se filtran aqui."""
    tok = token_map(d)
    parts = []
    with gzip.open(OC % d, 'rt') as fh:
        for x in pd.read_csv(fh, chunksize=chunk, dtype={'token_id': str, 'tx': str, 'maker': str, 'taker': str},
                             usecols=['tipo', 'ts_est', 'tx', 'log_index', 'maker', 'taker', 'side', 'token_id', 'maker_amt', 'taker_amt']):
            x = x[(x.tipo == 'F') & x.token_id.isin(tok)]
            x = x[x.taker.str.lower() != EX]
            if not len(x):
                continue
            t = x.token_id.map(tok)
            venta = x.side.values == 1
            sh = np.where(venta, x.maker_amt.values, x.taker_amt.values)
            usd = np.where(venta, x.taker_amt.values, x.maker_amt.values)
            lado = t.str[3].values
            yes = np.where(venta, lado == 'NO', lado == 'YES')
            with np.errstate(divide='ignore', invalid='ignore'):
                pc = np.where(venta, 1 - usd / sh, usd / sh)
            mid = t.str[1].astype('int64').values
            D, PRE = des
            dd = pd.Series(mid).astype(str).map(D)
            if dd.isna().any():
                fin_ = t.str[2].astype('int64').values; co_ = t.str[0].str.lower().values
                pre = pd.Series([PRE.get('%s-updown-5m-%d' % (c_, f_ - 300)) for c_, f_ in zip(co_, fin_)]).map({'Up': 'YES', 'Down': 'NO'})
                dd = dd.fillna(pre)
            dv = np.where(dd.isna(), -1, np.where(dd == 'YES', 1, 0)).astype(np.int8)
            gana = np.where(dv < 0, -1, (dv == yes.astype(np.int8))).astype(np.int8)
            parts.append(pd.DataFrame({'ts': x.ts_est.values, 'coin': t.str[0].values, 'mid': mid, 'fin': t.str[2].astype('int64').values,
                                       'yes': yes, 'sh': sh.astype('float64'), 'pc': pc.astype('float64'),
                                       'maker': x.maker.str.lower().values, 'taker': x.taker.str.lower().values,
                                       'gana': gana, 'tx': x.tx.values, 'li': x.log_index.values}))
    if not parts:
        return pd.DataFrame()
    F = pd.concat(parts, ignore_index=True)
    ok = (F.sh > 0) & (F.pc > 0) & (F.pc < 1)
    return F[ok].reset_index(drop=True)


def taker_stats_dia(F):
    """Por tomador (perspectiva del TOMADOR, solo mercados resueltos, excluye la wallet propia como tomador):
    n fills, coste = sh*(1-pc), pnl_bruto = -(pnl del maker) = -(sh*gana - sh*pc). Fee del tomador 0,07*sh*pc*(1-pc) aparte."""
    if not len(F):
        return pd.DataFrame(columns=['taker', 'n', 'coste', 'pnl_bruto', 'fee'])
    G = F[(F.gana >= 0) & (F.taker != US)]
    pm = np.where(G.gana.values == 1, G.sh.values, 0.0) - G.sh.values * G.pc.values
    D = pd.DataFrame({'taker': G.taker.values, 'c': G.sh.values * (1 - G.pc.values), 'p': -pm, 'f': 0.07 * G.sh.values * G.pc.values * (1 - G.pc.values)})
    A = D.groupby('taker').agg(n=('c', 'size'), coste=('c', 'sum'), pnl_bruto=('p', 'sum'), fee=('f', 'sum')).reset_index()
    return A


def cached_stats(d, des):
    """taker_stats del dia d, cacheado en CACHE (fuera de git). Idempotente: si existe se reutiliza."""
    import os
    os.makedirs(CACHE, exist_ok=True)
    p = CACHE + 'taker_stats_%s.csv' % d
    if os.path.exists(p):
        return pd.read_csv(p)
    F = fills_dia(d, des)
    A = taker_stats_dia(F)
    A.to_csv(p + '.tmp', index=False)
    os.replace(p + '.tmp', p)
    return A


def sha256_lines(items):
    import hashlib
    return hashlib.sha256(('\n'.join(sorted(items)) + '\n').encode()).hexdigest()
