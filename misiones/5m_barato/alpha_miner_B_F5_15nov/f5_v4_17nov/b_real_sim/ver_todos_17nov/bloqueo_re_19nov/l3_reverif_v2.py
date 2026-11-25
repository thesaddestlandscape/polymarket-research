"""l3_reverif_v2.py (CORRECCION 2 de CIERRE_LIMITES_SEC7, 19-Nov): resto del tomador en los 202 con la definicion ORIGINAL (rem_sh_limite = rem_usdc / limite = tk_rem*tsz). El rem_new de l3_reverif.csv (acciones originales - recibidas) queda DESCARTADO (columna rem_new_descartado). Solo lectura; salida out/l3_reverif_v2.csv. Uso: cd bloqueo_re_19nov && python3 l3_reverif_v2.py"""
import json, sys, numpy as np, pandas as pd
sys.path.insert(0, '../solo_observable_19nov'); from so_rem_a1 import rem_limite
exec(open('l3_reverif.py').read().split("CD = {}")[0].split('"""', 2)[2])   # parse() del script original
CD = {}
for f in ('/root/polymarket-research-datalogs/cola_posicion/calldata_b.jsonl', '../calldata_extra.jsonl'):
    for l in open(f):
        d = json.loads(l); CD[d['tx']] = d['input']
d = pd.read_pickle('../tomador_202.pkl'); old = pd.read_csv('out/l3_reverif.csv').set_index('oid'); rows = []
for r in d.itertuples():
    inp = CD.get(r.tx)
    if inp is None or not inp.startswith('0x3c2b4399'): rows.append(dict(oid=r.oid, tk_tipo=r.tk_tipo, estado='sin_calldata', tsz=r.tk_sz, tk_rem_old=r.tk_rem)); continue
    to, mk, tfill, fl = parse(inp); lim, ru, rs = rem_limite(to['mA'], to['tA'], tfill, to['side'])
    rows.append(dict(oid=r.oid, tk_tipo=r.tk_tipo, side=to['side'], estado='ok', tsz=r.tk_sz, tk_rem_old=r.tk_rem, mA=to['mA'], tA=to['tA'], tfill=tfill, limite=lim, rem_usdc=ru, rem_sh_limite=rs, rem_new_descartado=old.rem_new.get(r.oid, np.nan)))
X = pd.DataFrame(rows); ok = X[X.estado == 'ok']
assert np.allclose(ok.rem_sh_limite.values, (ok.tk_rem_old * ok.tsz).values, atol=1e-6), 'rem_sh_limite != tk_rem*tsz'
X.to_csv('out/l3_reverif_v2.csv', index=False)
print('n', len(X), '| ok', len(ok), '| rem_sh_limite>0:', int((ok.rem_sh_limite > 1e-9).sum()), '| compra_comp con resto>0:', int(((ok.tk_tipo == 'compra_comp') & (ok.rem_sh_limite > 1e-9)).sum()), '| rem_new_descartado<0:', int((ok.rem_new_descartado < 0).sum()))
