#!/usr/bin/env python3
"""r6: volumen/dia que necesita una wallet para cruzar el suelo de 1.00 pUSD/dia (rebate = 0.2*0.07*p*(1-p) por accion = 0.014*(1-p) por EUR de coste), y lo que anade.
k = pagado/inferido de makers puros (p10 1.008, mediana 1.095 de r3): se usa k=1.0 (conservador) y k=1.1. Datos B de contabilidad_wallet_dedicada/posiciones.csv."""
import pandas as pd,numpy as np
R='/root/polymarket-research/experimentos/5m_barato/'
out=open(R+'b_perdidas_22oct/rebate_ganadores/datos/r6_necesidad_B.txt','w')
def P(*a):
    s=' '.join(str(x) for x in a); print(s); out.write(s+'\n')
P('precio  rebate/EUR  EUR/dia(k=1.0)  EUR/dia(k=1.1)  acciones/dia(k=1.0)')
for p in (0.05,0.10,0.15,0.20,0.25,0.30,0.50,0.70,0.90):
    r=0.014*(1-p); P(f'{p:5.2f}   {r:.4f}      {1/r:7.0f}        {1/(1.1*r):7.0f}          {1/(0.014*p*(1-p)):8.0f}')
p=pd.read_csv(R+'contabilidad_wallet_dedicada/posiciones.csv'); p['d']=p.fecha_primer_fill_utc.str[:10]
m=p[p.rol.str.contains('maker')&(p.estado.str.startswith('liquidada'))].copy()
m['reb']=0.014*(1-m.precio_medio)*m.coste
d=m.groupby('d').agg(n=('coste','size'),coste=('coste','sum'),pnl=('pnl_realizado','sum'),reb=('reb','sum'))
d['pc_medio']=m.groupby('d').apply(lambda g:(g.precio_medio*g.coste).sum()/g.coste.sum())
P('\nB dedicada (posiciones maker liquidadas):'); P(d.round(3).to_string())
tot=d.sum(); P(f"TOTAL coste {tot.coste:.1f} pnl {tot.pnl:.2f} EV {tot.pnl/tot.coste:+.4f} (n posiciones {int(tot.n)}) ; rebate inferido total {tot.reb:.2f} = {tot.reb/tot.coste:+.4f} por EUR ; mejor dia {d.reb.max():.3f} (suelo 1.000)")
P('dias de B que habrian cobrado:', int((d.reb>=1).sum()),'de',len(d),'| mejor dia / suelo = %.0f%%'%(100*d.reb.max()))
# escenarios anuales, EV propio de B: -0.072 (informe capacidad), rebate = 0.0112
for vol,ev in ((55,-0.072),(90,-0.072),(150,-0.072),(55,0.0),(90,0.0)):
    for conc in ('sin concentrar','concentrado en dias >=100'):
        reb=0.0112*vol*365 if (vol>=90 or conc!='sin concentrar') else 0.0
        P(f'vol {vol:4d} EUR/dia media, EV propio {ev:+.3f}, {conc:26s}: pnl propio {ev*vol*365:+8.0f} EUR/año, rebate {reb:6.0f}, total {ev*vol*365+reb:+8.0f}')
