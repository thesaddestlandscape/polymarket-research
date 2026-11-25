#!/usr/bin/env python3
"""RE-Q11 toxicidad parte 3 (05-Nov, DESCRIPTIVO post hoc): primera colocacion vs re-armado, edad x geometria de armado, T de armado, lagj. Sin p (exploratorio)."""
import os, numpy as np, pandas as pd, warnings; warnings.filterwarnings('ignore')
H = os.path.dirname(os.path.abspath(__file__)) + '/'
A = pd.read_pickle(H + 'out/TOX.pkl'); A['rel_arm'] = A.arr_bid - A.L; A['T_arm'] = A.fin - (A.t_dec + 68) / 1000.0
def ev(x): c = x.cost.sum(); return x.pnl.sum() / c if c > 0 else np.nan
def dec(x):
    c = x.cost.sum(); return f"n {len(x)} pnl {x.pnl.sum():+.1f} ev {ev(x):+.3f} desc {(x.q*(x.m0-x.L)).sum()/c:+.3f} info {(x.q*(x.gana-x.m0)).sum()/c:+.3f} cierres {x.fin.nunique()} dias+ {int((x.groupby('dia').pnl.sum()>0).sum())}/{x.dia.nunique()}"
A['arm6'] = np.where(A.rel_arm >= 0.055, 'arm>=6c', 'arm<6c'); A['rearm'] = np.where(A.seg == 0, 'primera', 'rearme')
A['edt'] = pd.cut(A.edad, [0, 3000, 13000, 35000, 1e9], labels=['<=3s', '3-13s', '13-35s', '>35s']); A['Ta'] = pd.cut(A.T_arm, [0, 120, 200, 400], labels=['Tarm<120', '120-200', '>200'])
A['lj'] = np.where(A.lagj <= 3000, 'lagj<=3s', 'lagj>3s')
for cols in (['rearm'], ['arm6', 'rearm'], ['arm6', 'edt'], ['Ta'], ['arm6', 'Ta'], ['arm6', 'lj'], ['lj', 'edt'], ['lado', 'arm6']):
    print('==', cols)
    for v, x in A.groupby(cols, observed=True): print('  ', v, dec(x))
print('== mediana edad (s) por arm6:', (A.groupby('arm6').edad.median() / 1000).round(1).to_dict(), '| fraccion re-armes por arm6:', A.groupby('arm6').seg.apply(lambda s: round(float((s > 0).mean()), 3)).to_dict())
print('== mediana T_arm por arm6:', A.groupby('arm6').T_arm.median().round(0).to_dict())
