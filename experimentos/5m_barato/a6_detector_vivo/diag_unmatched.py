import sys, glob, collections
sys.path.insert(0,'.')
from r5k_io import *
from detector_r5k import normalizar
from r5k_eval import emparejar
S='/tmp/claude-0/-root-polymarket-research/cbc315b0-0ee3-4fbb-b193-997ca0900993/scratchpad/a6/d'
tok = tokens_btc5([f'{S}/k_2026-10-17.csv', f'{S}/k_2026-10-18.csv'])
d0,d1=1792305000,1792360000
tok={t:v for t,v in tok.items() if d0<=v[2]<=d1}
mk={v[0] for v in tok.values()}; cie={v[0]:v[2] for v in tok.values()}
ws=[]
for e in eventos_libro5([S+'/libro5_ms_2026-10-18_3349631.TG.gz'],[],tok):
    if e[0]=='T':
        m,l,c=tok[e[3]]; n=normalizar(l,e[5],e[4],e[6])
        if n and 0.10<n[1]<=0.30 and 40<c-e[1]/1000<=320: ws.append((m,n[0],round(n[1],2),e[6],e[1]/1000, e[5]))
ch=[r for r in banda_cadena(['/root/polymarket-research-datalogs/vigia_5m_barato_r5k/2026-10-18/out/band_2026-10-18.csv.gz']) if r['mkt'] in mk]
grp=collections.defaultdict(float); tsg={}; nrows=collections.Counter()
for r in ch:
    k=(r['tx'],r['mkt'],r['lado'],round(r['pc'],2)); grp[k]+=r['acc']; tsg[k]=min(tsg.get(k,9e18),r['ts']); nrows[k]+=1
cg=[(k[0],k[1],k[2],k[3],grp[k],tsg[k]) for k in grp]
par,chs,wss=emparejar(cg,[w[:5] for w in ws])
print('cadena sin pareja',len(chs),'ws sin pareja',len(wss))
big=sorted(chs,key=lambda g:-cg[g][4])[:8]
for g in big:
    tx,m,l,pc,acc,ts=cg[g]
    print('\nCH sin pareja',tx[:10],m,l,pc,'acc',round(acc,3),'filas',nrows[(tx,m,l,pc)],'T',round(cie[m]-ts,1))
    near=[w for w in ws if w[0]==m and w[1]==l and abs(w[2]-pc)<0.005 and -4<ts-w[4]<30]
    print('  WS mismo mercado/lado/pc cerca:',[(round(ts-w[4],2),w[3]) for w in near][:12])
    near2=[w for w in ws if w[0]==m and w[1]==l and -4<ts-w[4]<30]
    print('  WS mismo lado cualquier pc:',[(w[2],round(ts-w[4],1),w[3]) for w in near2][:10])
# distribucion de tamaños sin pareja ws
import statistics
print('ws sin pareja: tam mediano',statistics.median([ws[i][3] for i in wss]), 'total vol',sum(ws[i][3] for i in wss))
print('cadena sin pareja vol',sum(cg[g][4] for g in chs))
# por grupo de 'filas' (multi-fila)
mult=sum(1 for g in chs if nrows[(cg[g][0],cg[g][1],cg[g][2],cg[g][3])]>1)
print('cadena sin pareja con >1 fila:',mult,'de',len(chs))
