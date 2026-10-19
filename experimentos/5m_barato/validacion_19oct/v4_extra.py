import csv,glob,json,statistics as st,random,itertools
from datetime import datetime
D='/root/polymarket-research-datalogs/'
des=json.load(open(D+'maker_ms_desenlaces_cache.json'))
cong=int(datetime.fromisoformat('2026-10-06T12:00:00+00:00').timestamp()*1000)
E=[]
for f in sorted(glob.glob(D+'vigia_5m_barato/eventos_*.csv')): E+=list(csv.DictReader(open(f)))
prim=[e for e in E if e['regla']=='B1_5m' and e['es_primero']=='1' and int(e['t_deteccion'])>=cong]
ex=[e for e in prim if float(e.get('L215_acciones') or 0)>0]
pr=[float(e['L215_precio']) for e in ex]
low=[p for p in pr if p<0.2];print('ops <0.20:',len(low),[round(p,3) for p in low])
# P(>=2 wins) bajo Poisson-binomial con p=precio
import numpy as np
rng=np.random.default_rng(1);ps=np.array(low);s=(rng.random((200000,len(ps)))<ps).sum(1);print('P(>=2 aciertos|H0 precio)',(s>=2).mean())
# bajo bid15
bd=[float(e['bid_otro_t0']) for e in ex if float(e['L215_precio'])<0.2];print('bid15 de esas',bd)
s=(rng.random((200000,len(bd)))<np.array(bd)).sum(1);print('P(>=2|H1 bid15)',(s>=2).mean())
# señales totales por bandas de precio ask_t0 <0.2
for lo,hi in ((0,.2),(.2,.4),(.4,.6),(.6,1)):
    s_=[e for e in prim if lo<=float(e['ask_compra_t0'])<hi]
    g=sum((des[e['market_compra']]=='YES')==(e['lado']=='Up') for e in s_)
    print(f'señales ask_t0 [{lo},{hi}): n={len(s_)} ganan={g} ask medio={st.mean(float(e["ask_compra_t0"]) for e in s_):.3f} bid15 medio={st.mean(float(e["bid_otro_t0"]) for e in s_):.3f}')
# necesidad de n para G1: 2/día
print('ejecutables/día medias',25/13)
