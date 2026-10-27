import numpy as np, pandas as pd
from wf import wf, W0
W0=W0.reset_index(drop=True)
def run(lbl,W,feat,**kw):
    W=W.reset_index(drop=True); r,R=wf(W,feat,nperm=1000,**kw)
    dp=R.dP.values; s=np.sort(dp)
    print(f"{lbl:28s} dP {r['dP']:+7d} dP_sin2mej {s[:-2].sum():+7.0f} dP_sin20oct {R[R.dia!='2026-10-20'].dP.sum():+7.0f} dPdias+ {(dp>0).sum()}/{len(dp)} | EXC {r['EXC']:+7d} p {r['p']:.4f} pcirc {r['p_circ']:.4f} sin2 {r['sin2']:+6d} dias+ {r['diaspos']} ret {r['ret']} k {r['k']}/{r['n']}",flush=True)
    return R
we=W0[W0.dow<5]
run('R1 base',W0,'R1')
run('R1 inversion(mejor)',W0,'R1',peor=False)
run('R1 tercil por moneda',W0,'R1',group='coin')
run('R1 tercil por bloque 4h',W0,'R1',group='hb')
run('R1 relativo 24h',W0,'R1rel')
for c in ['ETH','SOL','XRP']: run(f'R1 solo {c}',W0[W0.coin==c],'R1')
run('R1 sin ETH+SOL (=XRP)',W0[W0.coin=='XRP'],'R1')
run('R1 sin ETH',W0[W0.coin!='ETH'],'R1')
run('R1 q4 peor cuartil',W0,'R1',q=4)
run('R1 q5 peor quintil',W0,'R1',q=5)
run('R1 q2 mitad',W0,'R1',q=2)
run('R1 q3 fijo T0',W0,'R1',fixed=0)
run('V5 (5 min)',W0,'V5'); run('V30 (30 min)',W0,'V30'); run('R2 (60 min)',W0,'R2'); run('R1 ret 30 s',W0,'R1s30')
run('R1 solo L-V',we,'R1'); run('R1 solo fin de semana',W0[W0.dow>=5],'R1')
run('R1 sin 20-Oct',W0[W0.dia!='2026-10-20'],'R1')
run('R1 stale<=0,05',W0[W0.stale<=0.05],'R1')
