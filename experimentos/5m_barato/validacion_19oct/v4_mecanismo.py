import csv,glob,json,random,statistics as st,collections,math
from datetime import datetime,timezone
D='/root/polymarket-research-datalogs/'
des=json.load(open(D+'maker_ms_desenlaces_cache.json'))
cong=int(datetime.fromisoformat('2026-10-06T12:00:00+00:00').timestamp()*1000)
def fee(p): return 0.07*p*(1-p)
E=[]
for f in sorted(glob.glob(D+'vigia_5m_barato/eventos_*.csv')): E+=list(csv.DictReader(open(f)))
prim=[e for e in E if e['regla']=='B1_5m' and e['es_primero']=='1' and int(e['t_deteccion'])>=cong]
def gana(e): return (des[e['market_compra']]=='YES')==(e['lado']=='Up')
print('TODAS las señales (58): ask_t0 medio, bid15 (cota) medio, acierto real')
a=[float(e['ask_compra_t0']) for e in prim]; b=[float(e['bid_otro_t0']) for e in prim]; g=[gana(e) for e in prim]
print(len(prim),round(st.mean(a),3),round(st.mean(b),3),round(sum(g)/len(g),3), 'aciertos',sum(g))
# por moneda
for m in sorted({e['moneda'] for e in prim}):
    s=[e for e in prim if e['moneda']==m]
    print(' ',m,len(s),round(st.mean(float(e['ask_compra_t0']) for e in s),3),round(st.mean(float(e['bid_otro_t0']) for e in s),3),sum(gana(e) for e in s))
# Brier-type: log-likelihood ratio test; H0 p=ask ; simulate total "paper EV at ask_t0" sums
# EV paper al ask t0 con todas las señales (sin fill): acciones=2€/precio
def paper(e):
    p=float(e['ask_compra_t0']); n=2.0/(p+fee(p)); return n*((1.0 if gana(e) else 0)-p-fee(p)), 2.0
pp=[paper(e) for e in prim]; print('PnL papel al ask_t0 (2€ por señal, sin fill, 58 señales)',round(sum(x[0] for x in pp),2),'EV',round(sum(x[0] for x in pp)/sum(x[1] for x in pp),3))
# por día, papel
bd=collections.defaultdict(lambda:[0,0])
for e,x in zip(prim,pp):
    d=datetime.fromtimestamp(int(e['cierre']),timezone.utc).date().isoformat(); bd[d][0]+=x[0]; bd[d][1]+=x[1]
print({d:(round(v[0],2),round(v[0]/v[1],2)) for d,v in sorted(bd.items())})
# sin las 2 BTC longshot
print('papel sin top2:',)
srt=sorted(range(len(prim)),key=lambda i:-pp[i][0])[:2]
rest=[pp[i] for i in range(len(prim)) if i not in srt]
print(round(sum(x[0] for x in rest),2),round(sum(x[0] for x in rest)/sum(x[1] for x in rest),3))
# Monte Carlo bajo H0: gana ~ Bernoulli(ask_t0) en las 25 ejecutadas  (precio L215)
rows=[]
for e in prim:
    acc=float(e.get('L215_acciones') or 0)
    if acc>0 and e['L215_precio'] not in ('','None'):
        rows.append((acc,float(e['L215_precio']),gana(e)))
rng=random.Random(5)
def sim(pfun,n=40000):
    obs=sum(a*((1.0 if w else 0)-p-fee(p)) for a,p,w in rows)
    c=sum(a*(p+fee(p)) for a,p,w in rows); cnt=0;ev=[]
    for _ in range(n):
        t=sum(a*((1.0 if rng.random()<pfun(p) else 0)-p-fee(p)) for a,p,w in rows)
        ev.append(t)
        if t>=obs: cnt+=1
    ev.sort(); return obs,cnt/n,ev[int(.05*n)],ev[int(.5*n)],ev[int(.95*n)]
print('MC H0 (P(gana)=precio fill): obs, p-valor, P5,P50,P95 del PnL', [round(x,3) for x in sim(lambda p:p)])
print('MC H0 con p=precio+fee (ecuación nula -fee, EV=-fee)', [round(x,3) for x in sim(lambda p:p+fee(p))])
# bajo H1 P(gana)=bid15 (cota)
rowsb=[]
for e in prim:
    acc=float(e.get('L215_acciones') or 0)
    if acc>0 and e['L215_precio'] not in ('','None'): rowsb.append((acc,float(e['L215_precio']),float(e['bid_otro_t0']),gana(e)))
obs=sum(a*((1.0 if w else 0)-p-fee(p)) for a,p,b,w in rowsb)
exp=sum(a*(b-p-fee(p)) for a,p,b,w in rowsb)
c=sum(a*(p+fee(p)) for a,p,b,w in rowsb)
print('esperado bajo H1 (P=bid15): PnL',round(exp,2),'EV',round(exp/c,3),' observado',round(obs,2))
rng2=random.Random(9); n=40000; v=[]
for _ in range(n): v.append(sum(a*((1.0 if rng2.random()<b else 0)-p-fee(p)) for a,p,b,w in rowsb))
v.sort(); print('H1 P5/P50/P95 PnL',[round(v[int(q*n)],2) for q in (.05,.5,.95)],'P(PnL<=obs)',sum(1 for x in v if x<=obs)/n)
# acierto de las ejecutadas vs bid15
print('ejecutadas: n',len(rowsb),'win',sum(r[3] for r in rowsb),'precio medio',round(st.mean(r[1] for r in rowsb),3),'bid15 medio',round(st.mean(r[2] for r in rowsb),3))
