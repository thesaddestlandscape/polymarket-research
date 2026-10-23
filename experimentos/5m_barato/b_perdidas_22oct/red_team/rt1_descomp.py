#!/usr/bin/env python3
"""red team: descompone dPnL de S1 en volumen vs seleccion; nulo de retirada al azar emparejado en tamano."""
import numpy as np, pandas as pd, os
DD='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/seleccion_adversa_plan/datos'
DIAS=['2026-10-17','2026-10-18','2026-10-19','2026-10-20','2026-10-21','2026-10-22']
X=pd.concat([pd.read_csv(f'{DD}/e1_{d}.csv.gz') for d in DIAS],ignore_index=True)
X['coste']=np.where(X.fill==1,5*X.obj,0.0); X['pnl']=np.where(X.fill==1,5*(X.gana-X.obj),0.0)
B=X[X['var']=='BASE'].set_index('mid')
def an(var, dias, tag):
    V=X[(X['var']==var)&X.dia.isin(dias)].set_index('mid'); b=B.loc[V.index]
    f=b.fill==1
    rem=f&((V.fill==0)|(V.r!=b.r)); gone=f&(V.fill==0); sub=rem&(V.fill==1)
    kept=f&~rem
    cb=b.coste.sum(); evb=b.pnl.sum()/cb
    dp=(V.pnl-b.pnl).sum()
    vol=(cb-V.coste.sum())*(-evb); sel=dp-vol
    def ev(m,src=b): return src.pnl[m].sum()/src.coste[m].sum() if src.coste[m].sum()>0 else np.nan
    def hit(m,src=b): return src.gana[m].mean()
    # hit-rate de equilibrio: precio medio
    print(f"{tag:5s} {var:22s} dP/EUR {dp/cb:+.4f} = vol {vol/cb:+.4f} + sel {sel/cb:+.4f} | EVbase {evb:+.4f} | "
          f"elim(sin sust) n={int(gone.sum())} EV {ev(gone):+.3f} hit {hit(gone):.3f} p {b.obj[gone].mean():.3f} | "
          f"sust n={int(sub.sum())} EVbase-de-esos {ev(sub):+.3f} EVsust {ev(sub,V):+.3f} p {b.obj[sub].mean():.3f}->{V.obj[sub].mean():.3f} | "
          f"ret n={int(kept.sum())} EV {ev(kept):+.3f} hit {hit(kept):.3f} p {b.obj[kept].mean():.3f}")
    return dict(dp=dp,cb=cb,vol=vol,sel=sel,gone=gone,b=b,V=V)
for per,d in (('DESC',DIAS[:3]),('TEST',DIAS[3:]),('ALL',DIAS)):
    for v in ['S1_x2_w2000|D100','S1_x2_w2000|D0','S1_x2_w2000|D250','S1_x2_w500|D100','S3_w2000|D100','S1_x2_w2000|INV','S1_x2_w2000|SH-60','S1_x2_w2000|SH+60']:
        an(v,d,per)
# nulo emparejado: eliminar al azar (sin sustitucion) el MISMO numero de mercados rellenados que S1 elimina, por dia; sustitucion como observada
rng=np.random.default_rng(1)
for per,dias in (('DESC',DIAS[:3]),('TEST',DIAS[3:]),('ALL',DIAS)):
    r=an('S1_x2_w2000|D100',dias,per+'*'); b=r['b']; V=r['V']; gone=r['gone']
    obs=-(b.pnl[gone].sum())  # ahorro de eliminar
    f=b[b.fill==1]; sims=[]
    for _ in range(5000):
        s=0
        for d,h in f.groupby('dia'):
            k=int(gone[h.index].sum()); s+=-h.pnl.values[rng.choice(len(h),k,replace=False)].sum()
        sims.append(s)
    sims=np.array(sims)
    print(f"  {per}: ahorro por ELIMINAR (sin sust) obs {obs:+.1f} EUR; azar mismo n/dia media {sims.mean():+.1f} p(azar>=obs) {np.mean(sims>=obs):.3f}; exceso {(obs-sims.mean())/r['cb']:+.4f}/EUR")
