# A7: descomposicion del PnL 23-Oct de B en nulo-poblacion / regimen de la ventana / AS (escenarios, no puntos). POST-HOC descriptivo.
import pandas as pd, numpy as np, glob
D='/root/polymarket-research-datalogs'; O='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/post_25_27/datos'
rng=np.random.default_rng(20261023)
P=pd.read_csv(f'{O}/pos_b.csv',keep_default_na=False,na_values=['']); Q=P[P.dia=='2026-10-23'].copy()
pob=pd.concat([pd.read_csv(f) for f in sorted(glob.glob(f'{D}/etiquetado_pasivo_B/poblacion/pob_*.csv.gz'))])
pob=pob[pob.gana_lado.notna()&pob.coin.isin(['ETH','SOL','XRP'])&(pob.precio>=0.10)&(pob.precio<0.30)]; pob['bp']=(pob.precio*20).astype(int)/20
phit=pob.groupby('bp').gana_lado.mean(); Q['bp']=(Q.precio*20).astype(int)/20; p0=Q.bp.map(phit).values; pr=Q.precio.values; acc=Q.acciones.values
def esc(nm,p):
    W=rng.random((200000,len(Q)))<p; sim=(W*acc*(1-pr)-(~W)*acc*pr).sum(1); nw=W.sum(1)
    print(f'{nm}: hit medio esperado {p.mean():.3f} ; PnL esperado {sim.mean():+.2f} (sd {sim.std():.2f}) ; P(PnL<=obs {Q.pnl.sum():+.2f}) {np.mean(sim<=Q.pnl.sum()+0.01):.3f} ; P(<=1 acierto) {np.mean(nw<=1):.3f}')
    return sim.mean()
a=esc('(a) nulo poblacion 17-22 (maker medio a su precio)',p0)
# regimen de la ventana: ratio hit/bid ventana (0.130/0.193) frente a ratio poblacion
r_win=0.130/0.193; r_pop=pob.gana_lado.mean()/pob.precio.mean(); b=esc('(b) + regimen ventana 06:30-08:56 (longshots genericos, fill-independiente)',np.clip(p0*r_win/r_pop,0,1))
r_tw=(1/14)/0.193; c=esc('(c) + AS tipo gemelo en ventana (1/14 fills; n=14, IC90 EV (-1,-0.05)) [cota, muy ruidosa]',np.clip(p0*r_tw/r_pop,0,1))
obs=Q.pnl.sum(); print(f'\nDescomposicion (PnL en $, aproximada): observado {obs:+.2f} = nulo {a:+.2f} + regimen {b-a:+.2f} + AS(gemelo, cota) {c-b:+.2f} + residuo/azar {obs-c:+.2f}')
# lectura "puesta al ask" para el regimen: bid como coste es optimista
