import sys,glob,gzip,csv,numpy as np,pandas as pd
sys.path.insert(0,'/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/calma_v3/recalc_13nov')
dia=sys.argv[1]
# libro5_tx
def tx_times(dia):
    out=[];tks=set()
    for dd in (pd.Timestamp(dia)+pd.Timedelta(days=i) for i in (-1,0,1)):
        for f in glob.glob('/mnt/HC_Volume_106538179/libro5_tx/libro5_tx_%s_*.csv.gz'%dd.strftime('%Y-%m-%d')):
            x=pd.read_csv(f,header=None,usecols=[0,1],names=['t','tk'],dtype={'t':'int64','tk':str},on_bad_lines='skip');out.append(x)
    x=pd.concat(out);return x
d0=int(pd.Timestamp(dia,tz='UTC').timestamp()*1000);d1=d0+86400000
tx=tx_times(dia);tx=tx[(tx.t>=d0)&(tx.t<d1)].drop_duplicates()
t=np.sort(tx.t.values);e=np.concatenate([[d0],t,[d1]]);g=np.diff(e);idx=np.where(g>60000)[0]
holes=[(e[i],e[i+1]) for i in idx]
toks=set(tx.tk)
# libro5_ms stream counts
from collections import Counter
cnt={h:Counter() for h in holes}; ctl={h:Counter() for h in holes}; Gc={h:Counter() for h in holes}
for dd in (pd.Timestamp(dia)+pd.Timedelta(days=i) for i in (-1,0,1)):
  for f in glob.glob('/mnt/HC_Volume_106538179/libro5_ms/libro5_ms_%s_*.csv.gz'%dd.strftime('%Y-%m-%d')):
    try:
      with gzip.open(f,'rt',errors='ignore') as fh:
        for l in fh:
            p=l.split(',',7)
            if len(p)<7 or p[0] not in ('T','B','d','G') or not p[1].isdigit(): continue
            try: r=int(p[6]) if p[6] else int(p[1])
            except: continue
            for h in holes:
                a,b=h
                if a<=r<b:
                    cnt[h][p[0]]+=1
                    if p[0]=='G': Gc[h][(p[3][:30],p[2]=='*')]+=1
                elif a-300000<=r<a: ctl[h][p[0]]+=1
    except Exception as ex: print('err',f,ex)
# onchain
oc=pd.read_csv('/root/polymarket-research-datalogs/onchain_fills_%s.csv.gz'%dia,usecols=['tipo','bloque','ts_est','tx','token_id'],dtype={'token_id':str})
oc=oc[oc.tipo=='F'];oc['t']=(oc.ts_est*1000).astype('int64')
print(dia,'holes',len(holes),'tx rows',len(tx),'onchain F',len(oc))
for a,b in holes:
    sa=a;sb=b
    ocin=oc[(oc.t>=sa)&(oc.t<sb)];oc5=ocin[ocin.token_id.isin(toks)]
    ocx=ocin.tx.nunique();oc5x=oc5.tx.nunique()
    print(pd.Timestamp(sa,unit='ms').strftime('%H:%M:%S'),'dur %.0fs'%((sb-sa)/1000),'| onchain tx all %d, 5mtoks %d | ms IN-hole %s | 5min-before %s | G %s'%(ocx,oc5x,dict(cnt[(a,b)]),dict(ctl[(a,b)]),dict(Gc[(a,b)].most_common(4))))
# global onchain tx rate for context
oc5=oc[oc.token_id.isin(toks)];print('onchain tx per min day(5m toks):',oc5.tx.nunique()/1440,'libro5_tx tx per min:',tx.shape[0]/1440)
