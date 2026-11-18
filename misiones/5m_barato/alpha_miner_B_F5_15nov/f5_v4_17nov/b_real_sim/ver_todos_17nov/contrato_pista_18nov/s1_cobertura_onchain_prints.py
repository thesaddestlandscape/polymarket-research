#!/usr/bin/env python3
"""s1 (18-Nov, MECANISMO, solo lectura): cobertura de on-chain (F) vs prints Sonda1 pasivo por dia, y unidad 'tx con un solo maker bid en nivel 0,10-0,29'.
Uso: s1_cobertura_onchain_prints.py YYYY-MM-DD. Etiqueta MECANISMO: no EV."""
import sys, gzip, pandas as pd, numpy as np, json
D = sys.argv[1]; DL = '/root/polymarket-research-datalogs/'
pr = pd.read_csv(DL + f'sonda1/pasivo/sonda1_prints_{D}.csv.gz', usecols=['slug','t_recv_ms','token','precio','size','side','tx_hash','ts_exchange'], dtype={'token':str})
_t = set(pr.token.unique()); _ch = []; _n = 0; _tipos = {}
for ch in pd.read_csv(DL + f'onchain_fills_{D}.csv.gz', usecols=['tipo','bloque','ts_est','tx','log_index','order_hash','maker','taker','side','token_id','maker_amt','taker_amt'], dtype={'token_id':str}, chunksize=400000):
    _n += len(ch)
    for k, v in ch.tipo.value_counts().items(): _tipos[k] = _tipos.get(k, 0) + int(v)
    ch = ch[ch.token_id.isin(_t) & (ch.tipo == 'F')].copy()
    for c in ('tx', 'order_hash', 'maker', 'taker'): ch[c] = ch[c].astype('category')
    ch['token_id'] = ch.token_id.astype('category'); _ch.append(ch.drop(columns=['bloque', 'ts_est', 'log_index', 'tipo']))
oc = pd.concat(_ch, ignore_index=True); del _ch
EX = '0xe111180000d2663c0091e4f400237545b87b996b'
out = {'dia': D, 'onchain_filas': _n, 'onchain_tipos': _tipos, 'F_tokens_sonda': len(oc), 'prints': len(pr)}
tok = pr.drop_duplicates('token').set_index('token').slug.to_dict()
oc['slug'] = oc.token_id.astype(str).map(tok); oc['asset'] = oc.slug.str.split('-').str[0]; oc['marco'] = oc.slug.str.split('-').str[2]
f = oc

# precio de la fila: BUY (side 0): maker_amt/taker_amt ; SELL (side 1): taker_amt/maker_amt
f = f.assign(precio=np.where(f.side == 0, f.maker_amt / f.taker_amt, f.taker_amt / f.maker_amt))
mk = f[(f.taker.astype(str) != EX) & f.slug.notna()]            # filas de ORDEN MAKER (la fila del tomador lleva taker=contrato exchange)
out['filas_maker'] = len(mk); out['filas_tomador_contrato'] = int((f.taker.astype(str) == EX).sum())
b5 = mk[(mk.marco == '5m')]
bid = b5[(b5.side == 0) & b5.precio.between(0.10, 0.2999)]
bid = bid.assign(tx=bid.tx.astype(str), token_id=bid.token_id.astype(str), order_hash=bid.order_hash.astype(str), maker=bid.maker.astype(str))
g = bid.groupby(['tx', 'token_id']).order_hash.nunique()
out['btc5m_bid_band_por_activo'] = bid.asset.value_counts().to_dict()
out['tx_tokenlado_bid_banda'] = int(len(g)); out['n_mk_dist'] = g.clip(upper=5).value_counts().sort_index().to_dict()
out['frac_solo_un_maker'] = float((g == 1).mean())
# join con prints por tx
pt = set(pr.tx_hash.unique()); txs = set(g.index.get_level_values(0))
out['tx_banda_con_print'] = float(np.mean([t in pt for t in txs])) if txs else None
# prints sin on-chain (cobertura inversa)
oct = set(oc.tx.astype(str).unique()); pb = pr[pr.slug.str.contains('-5m-') & pr.precio.between(0.10, 0.2999)]
out['prints_banda5m_tx_en_onchain'] = float(pb.tx_hash.isin(oct).mean())
# reloj: ts_exchange vs t_recv en prints (por hora UTC): p1 del suelo
pr['d'] = pr.t_recv_ms - pr.ts_exchange; pr['h'] = pd.to_datetime(pr.t_recv_ms, unit='ms').dt.hour
out['suelo_rx_menos_ex_p1_por_hora'] = pr.groupby('h').d.quantile(0.01).round(0).astype(int).to_dict()
# makers repetidos: misma direccion en >=2 tx de la banda
mc = bid.groupby('maker').tx.nunique(); out['makers_distintos_banda'] = int(len(mc)); out['makers_con_ge5_tx'] = int((mc >= 5).sum()); out['top10_makers_frac_filas'] = float(bid.maker.value_counts().head(10).sum() / len(bid))
print(json.dumps(out, indent=1, default=str))
json.dump(out, open(f'/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/f5_v4_17nov/b_real_sim/ver_todos_17nov/contrato_pista_18nov/s1_{D}.json', 'w'), indent=1, default=str)
