import csv, json
C='/mnt/HC_Volume_106538179/datalogs_analisis_caches/colas_20oct/'
tok={}
# kall (18-19 oct): token,act,marco,mkt,fin,lado
for l in open('/root/polymarket-research-datalogs/vigia_5m_barato_r5k/2026-10-19/kall.csv'):
    c=l.rstrip('\n').split(',')
    if len(c)>=6 and c[2]=='5min' and c[1] in('BTC','ETH','SOL','XRP'):
        tok[c[0]]=(c[1],c[3],c[5],c[4])
# k rows: k,t_ms,token,act,marco,mkt,fin,lado
for l in open(C+'k_17_20.csv'):
    c=l.rstrip('\n').split(',')
    if len(c)>=8 and c[4]=='5min' and c[3] in('BTC','ETH','SOL','XRP'):
        tok.setdefault(c[2],(c[3],c[5],c[7],c[6]))
from datetime import datetime
out={}
for t,(a,m,lado,fin) in tok.items():
    out[t]=(a,m,lado,datetime.fromisoformat(fin).timestamp())
json.dump(out,open(C+'tokens.json','w'))
open(C+'tokens.txt','w').write('\n'.join(out)+'\n,*,\n')
import collections
print(len(out), collections.Counter(v[0] for v in out.values()))
ds=collections.Counter((v[0],datetime.utcfromtimestamp(v[3]).strftime('%m-%d')) for v in out.values())
print(sorted(ds.items()))
# ensure two tokens/market
mk=collections.Counter(v[1] for v in out.values()); print(collections.Counter(mk.values()))
