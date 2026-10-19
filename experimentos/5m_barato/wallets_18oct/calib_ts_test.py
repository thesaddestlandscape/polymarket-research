# Prueba ligera: relacion hora de bloque (ts_est) vs fila t del registro (hora exchange c[1], recepcion c[6]) en los primeros minutos del 18-Oct.
import gzip,sys,numpy as np,pandas as pd
EXCH="0xe111180000d2663c0091e4f400237545b87b996b"
oc=[]
with gzip.open('/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_2026-10-18.csv.gz','rt') as fh:
    hdr=fh.readline().strip().split(',')
    for i,ln in enumerate(fh):
        if i>300000: break
        c=ln.rstrip('\n').split(',')
        if c[0]=='F' and c[7]!=EXCH: oc.append((float(c[2]),c[9],float(c[10]),float(c[11]),int(c[8]),c[7]))
oc=pd.DataFrame(oc,columns=['ts','tok','a','b','side','taker'])
tt=[]
with gzip.open('/mnt/HC_Volume_106538179/m5_registro/m5_registro_2026-10-18.csv.gz','rt',errors='replace') as fh:
    for i,ln in enumerate(fh):
        if i>3000000: break
        if ln[:2]=='t,':
            c=ln.split(',');tt.append((int(c[1])/1000,c[2],float(c[3]),c[4],float(c[5]),int(c[6])/1000))
tt=pd.DataFrame(tt,columns=['tex','tok','p','side','sz','trx'])
print(len(oc),oc.ts.min(),oc.ts.max(),len(tt),tt.tex.min(),tt.tex.max())
# acciones y precio del lado token
oc['sh']=np.where(oc.side==1,oc.a,oc.b);oc['usd']=np.where(oc.side==1,oc.b,oc.a);oc['p']=(oc.usd/oc.sh).round(2)
oc['sh']=oc.sh.round(4);tt['sz']=tt.sz.round(4);tt['p']=tt.p.round(2)
tmax=min(oc.ts.max(),tt.tex.max())-5
o=oc[oc.ts<tmax];t=tt[tt.tex<tmax]
m=o.merge(t,on=['tok','p'],how='inner')
m['dt']=m.ts-m.tex
print('merge rows',len(m))
mm=m[(m.dt>-1)&(m.dt<10)&((m.sh-m.sz).abs()<1e-3)]
print('con tamano',len(mm),'de',len(o))
print(mm.dt.describe(percentiles=[.05,.25,.5,.75,.95,.99]))
print('recepcion - exchange',(tt.trx-tt.tex).describe(percentiles=[.5,.9,.99]))
