# Numeros del PLAN_MAESTRO (20-Oct-2026). Solo lectura. Uso: nice -n 19 python3 escalado_numeros.py
import csv, math, collections
T90=lambda n:{1:6.31,2:2.92,3:2.35,4:2.13,5:2.02,6:1.94,7:1.89,8:1.86,9:1.83,10:1.81,12:1.78,15:1.76,19:1.73,20:1.73}.get(n,1.70)
def ic_dias(d):  # EV diario ponderado: media de dias, t-Student 90 %
    v=[a/b for a,b in d if b>0]; n=len(v)
    if n<2: return None
    m=sum(v)/n; s=(sum((x-m)**2 for x in v)/(n-1))**.5
    return round(m,3),round(m-T90(n-1)*s/n**.5,3),round(m+T90(n-1)*s/n**.5,3),n
rows=[r for r in csv.DictReader(open('/root/polymarket-research/data/live/trades.csv'))
      if r['strategy']=='RESOLUTION_SNIPER_PRECIERRE' and r['status']=='CLOSED']
def rep(nom,L):
    if not L: print(nom,'n=0'); return
    pn=sum(float(r['pnl_neto_eur']) for r in L); co=sum(float(r['stake_eur']) for r in L)
    d=collections.defaultdict(lambda:[0,0])
    for r in L:
        k=r['timestamp_utc'][:10]; d[k][0]+=float(r['pnl_neto_eur']); d[k][1]+=float(r['stake_eur'])
    dd=sorted(d.items(), key=lambda kv: kv[1][0]/kv[1][1])
    sin2=[v for k,v in dd[:-2]]
    s2=sum(a for a,b in sin2)/sum(b for a,b in sin2) if sin2 else None
    print(nom,'n',len(L),'aciertos',sum(float(r['pnl_neto_eur'])>0 for r in L),'pnl',round(pn,2),'coste',round(co,2),
          'EVpond',round(pn/co,3),'IC90dias(media,lo,hi,ndias)',ic_dias(list(d.values())),'sin2mejoresdias',None if s2 is None else round(s2,3),'dias',len(d))
for m in ('5min','15min'):
    L=[r for r in rows if r['subtype'].split('#')[1]==m]
    rep('PRECIERRE '+m,L); rep('  desde 17-Oct 08:16Z '+m,[r for r in L if r['timestamp_utc']>='2026-10-17T08:16'])
rep('PRECIERRE total',rows)
# ruina 1 %: C = ln(100)*sigma1^2*s/(2*EV)  (Browniano; sigma1 = desv. por € apostado)
def C1(s,sig,ev): return math.log(100)*sig**2*s/(2*ev)
print('\nC_1%ruina (EV pesimista) = 2,30*sigma1^2*s/EV')
for nom,sig,ev,stakes in (('H55',0.575,0.04,[2,5,10,25,50,100,147]),('H35 (s=coste por relleno $)',2.05,0.05,[1.02,2.04,5.1,10.2]),('PRECIERRE5m',1.0,0.03,[2,3,5]),('H23',2.05,0.25,[2,3,5])):
    print(nom,[(s,round(C1(s,sig,ev))) for s in stakes])
print('\nEUR/anio = N/dia * stake * EV * 365')
for nom,N,stakes,evs in (('H55',2.8,[2,5,10,25,50,100,147],(0.005,0.04,0.08,0.179,0.34)),('PRECIERRE5m V0',2.85,[2,3,5],(0.0,0.03,0.06)),
                         ('PRECIERRE15m V6',1.5,[2,5,10,25],(0.0,0.10,0.19)),('H23',1.3,[2,3,5,25],(0.20,0.25,0.80)),('V4b',1.0,[2,5,13.6],(0.056,0.11,0.507))):
    print(nom,'N',N,'EV',evs)
    for s in stakes: print('  stake',s,[round(N*s*e*365) for e in evs])
print('\nmultiplicador N*s requerido para 200k: 548/EV vs medido')
for nom,ev,medido in (('H55 EV.08',0.08,2.8*2),('H35 EV.075',0.075,293),('PRECIERRE5m EV.06',0.06,2.85*3),('PRECIERRE15m V6 .19',0.19,1.5*2),('H23 .25',0.25,1.3*2),('V4b .11',0.11,1.0*2)):
    print(nom,'req $/dia',round(200000/365/ev),'medido $/dia',round(medido,1),'x',round(200000/365/ev/medido))
print('\nautofinanciacion H55 (EV .08): dias para acumular C1%(EV .04) del peldaño siguiente con el beneficio del actual')
st=[2,5,10,25,50,100,147]
for a,b in zip(st,st[1:]):
    print(a,'->',b,'beneficio/dia',round(2.8*a*0.08,2),'C1% sig',round(C1(b,0.575,0.04)),'dias',round(C1(b,0.575,0.04)/(2.8*a*0.08)))
