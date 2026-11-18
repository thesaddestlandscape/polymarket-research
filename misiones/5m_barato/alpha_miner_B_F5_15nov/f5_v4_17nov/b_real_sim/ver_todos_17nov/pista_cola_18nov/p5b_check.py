#!/usr/bin/env python3
"""p5b_check.py (ADENDA_03). Lee out/p5_control_sin_relleno.pkl. modo 'bal': SOLO columnas no-desenlace (dt, vida, q150, coin, cola_pos, w) -> SMD fill vs no-fill (peso por ancla),
supervivencia (pujas descartadas por vida < todo dt, rellenos sin tm3). modo 'rates': LR global y POST-ESTRATIFICADO por (coin x tercil de vida) (se pondera el no-relleno al perfil de vida/coin de los rellenos)."""
import sys, json, numpy as np, pandas as pd
H = __file__.rsplit('/', 1)[0]; O = pd.read_pickle(H + '/out/p5_control_sin_relleno.pkl'); mode = sys.argv[1]
def wm(x, w): return float(np.average(x, weights=w))
def smd(c, a, b):
    x = O[c]
    xa, xb, wb = x[a].values, x[b].values, O.w[b].values; ma, mb = xa.mean(), wm(xb, wb); va, vb = xa.var(), float(np.average((xb - mb) ** 2, weights=wb)); return round((ma - mb) / np.sqrt((va + vb) / 2 + 1e-12), 3)
O['ldt'] = np.log1p(O.dt.clip(lower=0)); O['lvida'] = np.log1p(O.vida.clip(lower=0)); O['lq150'] = np.log1p(O.q150.fillna(0).clip(lower=0)); a, b = O.fillb, ~O.fillb
if mode == 'bal':
    R = dict(n_fill=int(a.sum()), n_nofill_pujas=int(O[b].oid.nunique()), SMD={c: smd(c, a, b) for c in ('ldt', 'lvida', 'lq150')}, frac_cola_pos=dict(fill=round(float(O[a].cola_pos.mean()), 3), nofill=round(wm(O[b].cola_pos.astype(float), O.w[b]), 3)),
             coin=dict(fill=O[a].coin.value_counts(normalize=True).round(3).to_dict(), nofill=(O[b].groupby('coin').w.sum() / O[b].w.sum()).round(3).to_dict()),
             vida_ms_mediana=dict(fill=float(O[a].vida.median()), nofill=float(O[b].vida.median())), dt_mediana=dict(fill=float(O[a].dt.median()), nofill=float(O[b].dt.median())),
             dt_gt_vida=int((O.dt > O.vida).sum()), dias=sorted(O.dia.unique().tolist()))
else:
    O['ter'] = pd.qcut(O[a].lvida.rank(method='first'), 3, labels=False).reindex(O.index) if False else np.nan
    cut = np.quantile(O[a].lvida, [1 / 3, 2 / 3]); O['ter'] = np.searchsorted(cut, O.lvida.values); O['st'] = O.coin + '|' + O.ter.astype(str)
    R = {}
    for m in ('F50', 'F90'):
        fa = O[a][m].mean(); sh = O[a].st.value_counts(normalize=True); acc = 0.0; used = 0.0; per = {}
        for s_, p_ in sh.items():
            bb = O[b & (O.st == s_)]
            if bb.w.sum() <= 0: continue
            v = wm(bb[m].astype(float), bb.w); acc += p_ * v; used += p_; per[s_] = (round(float(O[a & (O.st == s_)][m].mean()), 3), round(float(v), 3), int((O.st[a] == s_).sum()), int(bb.oid.nunique()))
        fb = acc / used; R[m] = dict(fill=round(float(fa), 4), nofill_poststrat=round(float(fb), 4), LR_poststrat=round(float(fa / fb), 2) if fb > 0 else None, cubierto_frac_rellenos=round(used, 3), por_estrato_fill_nofill_nfill_npujas=per)
print(json.dumps(R, indent=1, default=str))
