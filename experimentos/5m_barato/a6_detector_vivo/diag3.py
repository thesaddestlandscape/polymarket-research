import sys, glob, collections, bisect
sys.path.insert(0,'.')
from r5k_io import *
S='/tmp/claude-0/-root-polymarket-research/cbc315b0-0ee3-4fbb-b193-997ca0900993/scratchpad/a6/d'
tok = tokens_btc5([f'{S}/k_2026-10-17.csv', f'{S}/k_2026-10-18.csv'])
d0,d1=1792305000,1792360000
tok={t:v for t,v in tok.items() if d0<=v[2]<=d1}
tk=tomadores_cadena('/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_2026-10-18.csv.gz', tok)
tk=[x for x in tk if d0-400<=x[0]<=d1]
print('taker-level chain events', len(tk))
ws=[e for e in eventos_libro5([S+'/libro5_ms_2026-10-18_3349631.TG.gz'],[],tok) if e[0]=='T']
print('ws events', len(ws))
# match by (token, side, size)
por=collections.defaultdict(list)
for i,e in enumerate(ws): por[(e[3],e[5])].append((e[1]/1000,e[6],e[4],i))
for v in por.values(): v.sort()
used=set(); lags=[]; dp=[]; un=0; pares=[]
for ts,tx,li,t,side,sh,usd in sorted(tk):
    lst=por.get((t,side),[]); tl=[x[0] for x in lst]
    j=bisect.bisect_left(tl,ts-25); m=None
    while j<len(lst) and lst[j][0]<=ts+3:
        if lst[j][3] not in used and abs(lst[j][1]-sh)<=2e-3+1e-4*sh: m=lst[j]; break
        j+=1
    if m is None: un+=1; continue
    used.add(m[3]); lags.append(ts-m[0]); pavg=usd/sh; dp.append((m[2],pavg)); pares.append((sh,m[2],pavg))
print('chain taker events matched',len(lags),'unmatched',un, 'ws unmatched', len(ws)-len(used))
import statistics
lags.sort(); print('lag med',lags[len(lags)//2], 'p5',lags[len(lags)//20],'p95',lags[-len(lags)//20])
# relación precio WS vs precio medio
exact=sum(1 for a,b in dp if abs(a-b)<0.0051); print('price within half cent of avg', exact, len(dp))
r=collections.Counter()
for a,b in dp:
    r[round(a-round(b,2),2)]+=1
print('ws price - round(avg,2):', r.most_common(6))
big=[(s,a,b) for s,a,b in pares if s>300][:10]; print(big)
