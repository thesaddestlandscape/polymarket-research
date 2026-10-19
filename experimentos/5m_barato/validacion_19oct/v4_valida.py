import csv,glob,json,random,statistics as st,collections,math
from datetime import datetime,timezone
D='/root/polymarket-research-datalogs/'
des=json.load(open(D+'maker_ms_desenlaces_cache.json'))
cong=int(datetime.fromisoformat('2026-10-06T12:00:00+00:00').timestamp()*1000)
def fee(p): return 0.07*p*(1-p)
E=[]
for f in sorted(glob.glob(D+'vigia_5m_barato/eventos_*.csv')):
    E+=list(csv.DictReader(open(f)))
prim=[e for e in E if e['regla']=='B1_5m' and e['es_primero']=='1' and int(e['t_deteccion'])>=cong]
print('señales OOS',len(prim),'sin desenlace',sum(1 for e in prim if e['market_compra'] not in des))
def pnl(e,pref='L215'):
    acc=float(e.get(pref+'_acciones') or 0); pr=e.get(pref+'_precio'); cl=e.get(pref+'_clase','')
    if cl=='UNKNOWN' or e['market_compra'] not in des: return None
    if acc<=0 or pr in (None,'','None'): return (0.0,0.0)
    pr=float(pr); g=(des[e['market_compra']]=='YES')==(e['lado']=='Up')
    return (acc*((1.0 if g else 0.0)-pr-fee(pr)),acc*(pr+fee(pr)))
rows=[]
for e in prim:
    p=pnl(e)
    if p and p[1]>0:
        rows.append(dict(day=datetime.fromtimestamp(int(e['cierre']),timezone.utc).date().isoformat(),mon=e['moneda'],lado=e['lado'],pnl=p[0],cost=p[1],pr=float(e['L215_precio']),cierre=int(e['cierre']),ev=e))
print('ejecutables',len(rows),'PnL',round(sum(r['pnl'] for r in rows),3),'coste',round(sum(r['cost'] for r in rows),3),'EV pond',round(sum(r['pnl'] for r in rows)/sum(r['cost'] for r in rows),4))
print('EV por unidad (media de cocientes)',round(st.mean(r['pnl']/r['cost'] for r in rows),4))
def ev(rs): 
    c=sum(r['cost'] for r in rs); return sum(r['pnl'] for r in rs)/c if c else None
bd=collections.defaultdict(list)
for r in rows: bd[r['day']].append(r)
print('\nPOR DÍA (cierre UTC): n, pnl, coste, ev')
for d in sorted(bd): print(d,len(bd[d]),round(sum(r['pnl'] for r in bd[d]),2),round(sum(r['cost'] for r in bd[d]),2),round(ev(bd[d]),3), [r['mon'] for r in bd[d]])
# señales (incl no ejecutables) por día
sd=collections.Counter(datetime.fromtimestamp(int(e['cierre']),timezone.utc).date().isoformat() for e in prim)
print('señales por día',dict(sorted(sd.items())))
print('\nTOP operaciones'); 
for r in sorted(rows,key=lambda r:-r['pnl'])[:6]: print(r['day'],r['mon'],r['lado'],round(r['pr'],3),round(r['pnl'],2),round(r['cost'],2))
best=max(rows,key=lambda r:r['pnl'])
print('EV sin mejor operación',round(ev([r for r in rows if r is not best]),4), 'PnL',round(sum(r['pnl'] for r in rows if r is not best),2))
top2=sorted(rows,key=lambda r:-r['pnl'])[:2]
print('EV sin 2 mejores ops',round(ev([r for r in rows if r not in top2]),4))
dp=sorted(bd,key=lambda d:-sum(r['pnl'] for r in bd[d]))
print('EV sin mejor día',dp[0],round(ev([r for r in rows if r['day']!=dp[0]]),4))
print('EV sin 2 mejores días',dp[:2],round(ev([r for r in rows if r['day'] not in dp[:2]]),4))
print('EV sin 3 mejores días',dp[:3],round(ev([r for r in rows if r['day'] not in dp[:3]]),4))
# bootstrap por días
def boot(days,fn,n=10000,seed=1):
    rng=random.Random(seed);m=[]
    for _ in range(n):
        s=[rng.choice(days) for _ in days]
        c=sum(fn(d)[1] for d in s)
        if c>0: m.append(sum(fn(d)[0] for d in s)/c)
    m.sort();return round(m[int(.05*len(m))],3),round(m[int(.95*len(m))],3)
fn=lambda d:(sum(r['pnl'] for r in bd[d]),sum(r['cost'] for r in bd[d]))
days=list(bd)
print('IC90 bootstrap por días (ponderado €):',boot(days,fn),'n días',len(days))
# bootstrap por cierre (clusters por cierre)
bc=collections.defaultdict(list)
for r in rows: bc[r['cierre']].append(r)
print('n cierres con ejecución',len(bc), 'ops',len(rows))
fc=lambda c:(sum(r['pnl'] for r in bc[c]),sum(r['cost'] for r in bc[c]))
print('IC90 bootstrap por cierre:',boot(list(bc),fc))
# sin la mejor operación: IC por cierre
bc2=collections.defaultdict(list)
for r in rows:
    if r is not best: bc2[r['cierre']].append(r)
fc2=lambda c:(sum(r['pnl'] for r in bc2[c]),sum(r['cost'] for r in bc2[c]))
print('IC90 por cierre sin mejor op:',boot(list(bc2),fc2))
# t-test diario simple
dr=[ev(bd[d]) for d in days]
print('ROI diario media',round(st.mean(dr),3),'sd',round(st.stdev(dr),3),'t',round(st.mean(dr)/(st.stdev(dr)/math.sqrt(len(dr))),2))
# permutation sign: P(EV>=obs) under null of zero-mean? exact binomial of wins
w=sum(1 for r in rows if r['pnl']>0); print('aciertos',w,'/',len(rows))
# por moneda
print('\nPOR MONEDA')
for m in sorted({r['mon'] for r in rows}):
    rs=[r for r in rows if r['mon']==m]; print(m,len(rs),round(sum(r['pnl'] for r in rs),2),round(ev(rs),3))
print('POR LADO')
for l in ('Up','Down'):
    rs=[r for r in rows if r['lado']==l]; print(l,len(rs),round(sum(r['pnl'] for r in rs),2),round(ev(rs),3))
print('POR PRECIO')
for lo,hi in ((0,.2),(.2,.4),(.4,.6),(.6,1)):
    rs=[r for r in rows if lo<=r['pr']<hi]; 
    if rs: print(lo,hi,len(rs),round(sum(r['pnl'] for r in rs),2),round(ev(rs),3),'win',sum(1 for r in rs if r['pnl']>0))
# BTC only days
print('BTC por día')
for d in sorted(bd):
    rs=[r for r in bd[d] if r['mon']=='BTC']; 
    if rs: print(d,len(rs),round(sum(r['pnl'] for r in rs),2))
# 18-Oct y 17 detalle
print('\nDetalle 17-18 oct')
for r in rows:
    if r['day']>='2026-10-17': print(r['day'],r['mon'],r['lado'],r['pr'],round(r['pnl'],2),r['ev']['L215_acciones'],r['ev']['L215_clase'])
# latencia
for L in (150,175,200,215,225,250,275,300):
    rs=[]
    for e in prim:
        p=pnl(e,f'L{L}')
        if p and p[1]>0: rs.append(dict(pnl=p[0],cost=p[1],day=datetime.fromtimestamp(int(e['cierre']),timezone.utc).date().isoformat()))
    print('L',L,len(rs),round(sum(r['pnl'] for r in rs),2),round(ev(rs),3))
