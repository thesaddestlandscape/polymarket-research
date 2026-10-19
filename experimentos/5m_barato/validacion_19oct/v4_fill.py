import csv,glob,json,math,statistics as st
from datetime import datetime
from math import comb
D='/root/polymarket-research-datalogs/'
des=json.load(open(D+'maker_ms_desenlaces_cache.json'))
cong=int(datetime.fromisoformat('2026-10-06T12:00:00+00:00').timestamp()*1000)
E=[]
for f in sorted(glob.glob(D+'vigia_5m_barato/eventos_*.csv')): E+=list(csv.DictReader(open(f)))
prim=[e for e in E if e['regla']=='B1_5m' and e['es_primero']=='1' and int(e['t_deteccion'])>=cong]
gana=lambda e:(des[e['market_compra']]=='YES')==(e['lado']=='Up')
ex=[e for e in prim if float(e.get('L215_acciones') or 0)>0]
nx=[e for e in prim if float(e.get('L215_acciones') or 0)<=0]
import collections
print('clases L215 no ejecutadas',collections.Counter(e['L215_clase'] for e in nx))
print('ejec',len(ex),sum(map(gana,ex)),'no ejec',len(nx),sum(map(gana,nx)))
# Fisher exact two-sided
a,b,c,d=sum(map(gana,ex)),len(ex)-sum(map(gana,ex)),sum(map(gana,nx)),len(nx)-sum(map(gana,nx))
N=a+b+c+d
def hyp(a):
    return comb(a+b,a)*comb(c+d,c+d-(a+c-a)) if False else comb(a+b,a)*comb(c+d,(a+c)-a)/comb(N,a+c)
tot=a+c
p0=hyp(a); p=sum(hyp(x) for x in range(max(0,tot-(c+d)),min(a+b,tot)+1) if hyp(x)<=p0+1e-12)
print('Fisher dos colas',round(p,4))
print('ask_t0 medio ejec',st.mean(float(e['ask_compra_t0']) for e in ex),'no ejec',st.mean(float(e['ask_compra_t0']) for e in nx))
print('bid15 medio ejec',st.mean(float(e['bid_otro_t0']) for e in ex),'no ejec',st.mean(float(e['bid_otro_t0']) for e in nx))
# L215 precio vs ask_t0 slippage ejecutadas
print('slippage L215 medio',st.mean(float(e['L215_precio'])-float(e['ask_compra_t0']) for e in ex))
# monedas por cierre: nº de señales por cierre
cc=collections.Counter(e['cierre'] for e in prim); print('señales por cierre dist',collections.Counter(cc.values()))
