#!/usr/bin/env python3
"""r10: compara simulador (r9_sim_fills) con fills reales maker de 0x21f4/0xe290/0x86b1 en los MISMOS mercados de la muestra y ventana T(60,300]. Criterio de Javi: |EV_sim-EV_real|<=0.005 por dia y signo igual, >=6/8 dias (aqui solo hay 3 dias medibles)."""
import pandas as pd,numpy as np
R='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/rebate_ganadores/datos/'
out=open(R+'r10_compara.txt','w')
def P(*a):
    s=' '.join(str(x) for x in a); print(s); out.write(s+'\n')
import glob
S=pd.concat([pd.read_csv(f,dtype={'mid':str}) for f in sorted(glob.glob(R+'r9_sim_fills_2026*.csv.gz'))]); Rl=pd.concat([pd.read_csv(f,dtype={'mid':str}) for f in sorted(glob.glob(R+'r9_real_fills_muestra_2026*.csv.gz'))])
Rl['w']=Rl.maker.str[:10]; ev=lambda g:(g.pnl.sum()+g.reb.sum())/g.coste.sum() if g.coste.sum()>0 else np.nan
ev0=lambda g:g.pnl.sum()/g.coste.sum() if g.coste.sum()>0 else np.nan
dias=sorted(Rl.dia.unique()); nm=S.groupby('dia').mid.nunique()
P('mercados de la muestra con fill simulado por dia:',nm.to_dict())
P('\n== REAL (maker, ventana T 60-300, muestra 1/3 de mercados) ==')
for w,g in Rl.groupby('w'):
    P(w,'fills',len(g),'mercados',g.mid.nunique(),'coste',round(g.coste.sum()),'EV(+reb) por dia:',{d:round(ev(x),4) for d,x in g.groupby('dia')},'| total',round(ev(g),4),'sin reb',round(ev0(g),4))
P('\n== SIMULADO: EV(+reb) por dia y variante ==')
res={}
for (v,t),g in S.groupby(['var','tdq']):
    r={d:ev(x) for d,x in g.groupby('dia')}; res[(v,t)]=r
    P(f"{v:11s} tdq={t} fills {len(g):6d} mercados {g.mid.nunique():4d} coste {g.coste.sum():8,.0f} EV(+reb) por dia: "+' '.join(f"{d[-2:]}:{r.get(d,np.nan):+.4f}" for d in dias)+f" | total {ev(g):+.4f} sin reb {ev0(g):+.4f}")
P('\n== CRITERIO: dias con |dEV|<=0.005 y mismo signo (variante x wallet) ==')
for w,g in Rl.groupby('w'):
    rr={d:ev(x) for d,x in g.groupby('dia')}
    for k,r in res.items():
        ok=[abs(r.get(d,np.nan)-rr[d])<=0.005 and np.sign(r.get(d,np.nan))==np.sign(rr[d]) for d in rr]; sg=[np.sign(r.get(d,np.nan))==np.sign(rr[d]) for d in rr]
        P(f"{w} {k[0]:11s} tdq={k[1]}: error<=0.5pp+signo {sum(ok)}/{len(ok)} ; solo signo {sum(sg)}/{len(sg)} ; error medio {np.nanmean([r.get(d,np.nan)-rr[d] for d in rr]):+.4f}")
P('\n== COMPONENTES (BARATO vs ALL, real vs sim), EV(+reb) por banda de precio ==')
B=[0.05,0.10,0.20,0.30,0.50,0.70,0.90,0.99]
def porb(g): 
    b=pd.cut(g.pc,B,right=False); return {str(k):(round(ev(x),3),round(x.coste.sum())) for k,x in g.groupby(b,observed=True)}
for w,g in Rl.groupby('w'): P('real',w,porb(g))
for k in (('SIT_ALL',1),('TOP_ALL',1)): P('sim',k,porb(S[(S['var']==k[0])&(S.tdq==k[1])]))
P('\n== DIAGNOSTICO de colocacion real (libro 3 s antes del bloque) ==')
for w,g in Rl.groupby('w'):
    d=g.dropna(subset=['dist'])
    P(w,f"fills con libro {len(d)}/{len(g)}: en el touch (dist=0) {np.average(d.dist.abs()<0.005,weights=d.coste):.2f} (por coste); a 1 tick {np.average((d.dist>0.005)&(d.dist<0.015),weights=d.coste):.2f}; >=2 ticks {np.average(d.dist>=0.015,weights=d.coste):.2f}; nivel mediano {d.nivel.median():.0f} acc; acc/fill med {g.acc.median():.1f} p90 {g.acc.quantile(.9):.0f}; EV(+reb) touch {ev(d[d.dist.abs()<0.005]):+.4f} vs no-touch {ev(d[d.dist>=0.005]):+.4f}")
P('\n== COBERTURA de mercados y tamano (real vs sim) ==')
nmk=S.mid.nunique()
for w,g in Rl.groupby('w'): P(w,f"mercados con fill {g.mid.nunique()} de {nmk}; acc por mercado-lado med {g.groupby(['mid','lc']).acc.sum().median():.0f}")
for k in (('SIT_ALL',1),('TOP_ALL',1)):
    s=S[(S['var']==k[0])&(S.tdq==k[1])]; P('sim',k,f"mercados con fill {s.mid.nunique()}; acc por mercado-lado med {s.groupby(['mid','lc']).acc.sum().median():.1f}; fills por mercado-lado {len(s)/s.groupby(['mid','lc']).ngroups:.1f}")
