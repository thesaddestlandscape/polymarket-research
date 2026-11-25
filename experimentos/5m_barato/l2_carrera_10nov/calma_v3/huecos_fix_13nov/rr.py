#!/usr/bin/env python3
"""Reconstructor de relleno 'verdad' (solo lectura; DEV). Causa del 19,8 %: el WS emite UN last_trade_price por casado y por token del TOMADOR, con precio = VWAP del
tomador y tamano = total del tx. En un MINT (91 % de los casados) el print va en el token COMPLEMENTARIO (precio 1-p); el emparejado por (token,precio) no lo ve.
Fuente de verdad del relleno = fills on-chain de makers (precio y tamano EXACTOS por nivel) + instante WS en ms del casado = libro5_tx (token,tx,t_ev), unido por HASH DE TX.
Si el tx no esta en libro5_tx: instante estimado ts_bloque-2,25 s (+-1 s), marcado src='bloque'."""
import glob, numpy as np, pandas as pd
EX = '0xe111180000d2663c0091e4f400237545b87b996b'
OFFSET_BLOQUE_S = -2.25      # mediana medida (t_WS - ts_bloque) 27/29/31-Oct: -2,25/-2,23/-2,28 s; p5-p95 [-3,3, -1,3]

def fills_makers(df):
    """df: filas onchain (columnas tipo,tx,ts_est,maker,taker,side,token_id,maker_amt,taker_amt,log_index). Devuelve fills de MAKER con precio/acciones."""
    f = df[(df.tipo == 'F') & (df.taker != EX)].copy()
    f = f.drop_duplicates(['tx', 'log_index'])      # reparacion 02-Nov: ficheros principal+parcial solapan; unicidad on-chain = (tx, log_index)
    buy = f.side.values == 0
    f['sh'] = np.where(buy, f.taker_amt, f.maker_amt)
    f = f[f.sh > 0].copy()
    usd = np.where(f.side.values == 0, f.maker_amt, f.taker_amt)
    f['price'] = usd / f.sh.values
    return f

def tx_ws(tx_frames, con_tokens=True):
    """tx_frames: DataFrames [t_ev, token, tx, recv] de libro5_tx. -> Series tx -> RECEPCION minima (recv, ms; reparacion 02-Nov: antes t_ev = sello
    del exchange, que mezcla relojes; recv-t_ev p50 20 ms, p99 220) y dict tx -> set(tokens)."""
    T = pd.concat(tx_frames, ignore_index=True).drop_duplicates(['token', 'tx'])
    return T.groupby('tx').recv.min(), (T.groupby('tx').token.apply(set).to_dict() if con_tokens else {})

def cobertura_hora(f):
    """f: salida de reconstruir (con 'ts_est'). -> DataFrame (dia, hora) -> n fills, share con src=='tx_ws'. Hora de ts_est UTC."""
    t = pd.to_datetime(f.ts_est, unit='s', utc=True)
    g = pd.DataFrame({'dia': t.dt.strftime('%Y-%m-%d'), 'hora': t.dt.hour, 'ok': (f.src == 'tx_ws').values})
    return g.groupby(['dia', 'hora']).ok.agg(n='size', cob='mean').reset_index()

def horas_sanas(f, umbral=0.95, nmin=50):
    """Conjunto de (dia, hora) con cobertura tx_ws >= umbral. Horas con n<nmin fills se consideran NO sanas (sin evidencia). Reparacion 02-Nov: excluir por hora."""
    c = cobertura_hora(f)
    return {(r.dia, int(r.hora)) for r in c.itertuples() if r.n >= nmin and r.cob >= umbral}

def reconstruir(fills, t_ws):
    f = fills.copy()
    f['t_ws_ms'] = f.tx.map(t_ws)
    f['src'] = np.where(f.t_ws_ms.notna(), 'tx_ws', 'bloque')
    f['t_ws_ms'] = f.t_ws_ms.fillna(f.ts_est * 1000 + OFFSET_BLOQUE_S * 1000).astype('int64')
    n = f.groupby('tx').maker.transform('nunique'); f['n_makers_tx'] = n
    f['tipo_tx'] = np.where(n == 1, '1_maker', np.where(n == 2, '2_makers', '3+_makers'))
    return f.sort_values(['t_ws_ms', 'tx', 'log_index']).reset_index(drop=True)

def cinta_implicita(tok, t, pr, sd, sz, comp):
    """Tape WS consciente del complemento (sin on-chain): print BUY (sd=1) en el token c con precio P == venta implicita en comp[c] a 1-P (tamano total del tx).
    Devuelve arrays (token_X, t, precio_X, size) de ventas contra bids de X (nivel = VWAP: en barridos el nivel mas bajo solo lo da on-chain/libro)."""
    m = (sd == 1) & (comp[tok] >= 0)
    ts = (sd == 0)
    return (np.concatenate([comp[tok][m], tok[ts]]), np.concatenate([t[m], t[ts]]),
            np.concatenate([1 - pr[m], pr[ts]]), np.concatenate([sz[m], sz[ts]]))
