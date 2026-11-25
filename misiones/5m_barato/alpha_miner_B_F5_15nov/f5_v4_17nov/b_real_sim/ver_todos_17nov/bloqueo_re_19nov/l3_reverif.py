"""l3_reverif.py -- re-verifica L3 (CIERRE_LIMITES_SEC7) con ADENDA_A1 de V7: resto en ACCIONES = acciones originales - acciones recibidas en la tx.
Solo lectura. 202 rellenos de B (tomador_202.pkl) + calldata_b.jsonl / calldata_extra.jsonl. Salida out/l3_reverif.csv."""
import json, numpy as np, pandas as pd
def parse(inp):
    b = bytes.fromhex(inp[10:]); w = lambda i: int.from_bytes(b[i:i + 32], 'big')
    off_t, off_m, tfill, off_f = w(32), w(64), w(96), w(128)
    def order(s):
        f = [w(s + 32 * k) for k in range(12)]
        return dict(tokenId=str(f[3]), mA=f[4], tA=f[5], side=f[6])
    to = order(off_t); n = w(off_m); mk = [order(off_m + 32 + w(off_m + 32 * (1 + i))) for i in range(n)]
    nf = w(off_f); fl = [w(off_f + 32 * (1 + i)) for i in range(nf)]
    return to, mk, tfill, fl
CD = {}
for f in ('/root/polymarket-research-datalogs/cola_posicion/calldata_b.jsonl', '../calldata_extra.jsonl'):
    for l in open(f):
        d = json.loads(l); CD[d['tx']] = d['input']
d = pd.read_pickle('../tomador_202.pkl'); rows = []
for r in d.itertuples():
    inp = CD.get(r.tx); old = (r.tk_rem if r.tk_rem == r.tk_rem else np.nan) * r.tk_sz if r.tk_sz == r.tk_sz else np.nan
    if inp is None or not inp.startswith('0x3c2b4399'): rows.append(dict(oid=r.oid, tk_tipo=r.tk_tipo, estado='sin_calldata', rem_old=old)); continue
    to, mk, tfill, fl = parse(inp)
    if to['side'] == 0:
        got = sum(q * o['tA'] / o['mA'] if o['side'] == 0 else q for o, q in zip(mk, fl) if o['mA']) / 1e6
        new = to['tA'] / 1e6 - got
    else:
        new = (to['mA'] - tfill) / 1e6
    rows.append(dict(oid=r.oid, tk_tipo=r.tk_tipo, side=to['side'], estado='ok', tsz=r.tk_sz, rem_old=old, rem_new=new, tk_rem_old=r.tk_rem,
                     rem_frac_new=new / r.tk_sz if r.tk_sz else np.nan))
X = pd.DataFrame(rows); X.to_csv('out/l3_reverif.csv', index=False)
ok = X[X.estado == 'ok']; print('n', len(X), '| ok', len(ok), '| sin calldata', int((X.estado != 'ok').sum()), '| por tipo', X.tk_tipo.value_counts(dropna=False).to_dict())
po = ok.tk_rem_old > 0.01; pn = ok.rem_frac_new > 0.01
for t, G in ok.groupby('tk_tipo'):
    a = G.tk_rem_old > 0.01; b = G.rem_frac_new > 0.01
    print(f"{t}: n {len(G)} | resto>0 old {int(a.sum())} new {int(b.sum())} | old>0->new=0 {int((a & ~b).sum())} | old=0->new>0 {int((~a & b).sum())} | |rem_new-rem_old| acc p50/p90/max {np.nanpercentile((G.rem_new-G.rem_old).abs(),[50,90,100]).round(3).tolist()}")
print(f"TOTAL ok {len(ok)}: resto>0 old {int(po.sum())} new {int(pn.sum())} | old>0->new=0 {int((po & ~pn).sum())} | old=0->new>0 {int((~po & pn).sum())}")
G = ok[(ok.tk_tipo == 'compra_comp') & po & pn]; print('compra_comp con resto en ambas: rem_new/rem_old p10/50/90', np.nanpercentile(G.rem_new / G.rem_old, [10, 50, 90]).round(3).tolist(), 'n', len(G), '| new>=1 acc:', int((ok[ok.tk_tipo=='compra_comp'].rem_new >= 1).sum()))
