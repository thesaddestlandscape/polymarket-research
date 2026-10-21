import json,sys,csv,collections,glob
import numpy as np, pandas as pd
S=sys.argv[1]; EX='0xe111180000d2663c0091e4f400237545b87b996b'
W=set(json.load(open(S+'/cp_wallets.json')))
DES=json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
recs=[]; NM=collections.Counter()
for f in sorted(glob.glob(S+'/cp_2026-10-*.json')):
    d=f[-15:-5]; J=json.load(open(f))
    for r in J['tk']:
        r['des']=DES.get(str(r['mkt'])); r['dia']=d; recs.append(r)
    for w,c in J['n_maker'].items(): NM[(w,'09-18')]+=c
cols=['tipo','bloque','ts','tx','li','oh','maker','taker','side','tok','maker_amt','taker_amt','fee']
for d,gmf in [('19','gmap19.json'),('20','gmap.json'),('21','gmap.json')]:
    gm=json.load(open(S+'/'+gmf)); tok={}
    for slug,v in gm.items():
        st=int(slug.rsplit('-',1)[1])
        for t,l in zip(v['toks'],('YES','NO')): tok[t]=(slug.split('-')[0].upper(),v['id'],st+300,l,v['des'])
    for r in csv.reader(open(S+f'/alt_{d}.csv')):
        if r[0]!='F': continue
        mk=r[6].lower(); tk=r[7].lower()
        if mk not in W: continue
        if tk!=EX: NM[(mk,'19-21')]+=1; continue
        a,mid,fin,l,des=tok[r[9]]
        recs.append(dict(is_tk=1,maker=mk,taker=tk,side=int(r[8]),act=a,mkt=mid,lado=l,fin=fin,ts=float(r[2]),maker_amt=float(r[10]),taker_amt=float(r[11]),fee=float(r[12]),des=des,dia='2026-10-'+d))
T=pd.DataFrame(recs); T=T[T.des.notna()]
buy=T.side==0
T['sh']=np.where(buy,T.taker_amt,T.maker_amt); T['usd']=np.where(buy,T.maker_amt,T.taker_amt); T['px']=T.usd/T.sh
win=T.lado==T.des
T['pnl']=np.where(buy,np.where(win,T.sh,0)-T.usd,T.usd-np.where(win,T.sh,0))-T.fee
T['coste']=np.where(buy,T.usd,T.sh-T.usd)+T.fee; T['T']=T.fin-T.ts
T['alt']=T.act.isin(['ETH','SOL','XRP'])
# celda "compra el favorito contra pujas baratas": compra a 0,70-0,90 con T 60-300 (o venta del barato a 0,10-0,30)
pfav=np.where(buy,T.px,1-T.px)
T['celda']=(pfav>=0.70)&(pfav<0.90)&(T['T']>60)&(T['T']<=300)
T.to_pickle(S+'/cp_T.pkl')
rk=pd.read_csv(S+'/contrapartes_rank.csv',index_col=0)
def ev(t):
    if len(t)==0: return 'n=0'
    g=t.groupby('dia')[['pnl','coste']].sum()
    return f"n={len(t)} €={t.coste.sum():.0f} EV={t.pnl.sum()/t.coste.sum():+.3f} días+={int((g.pnl>0).sum())}/{len(g)}"
print('wallet|vs_nos(n,su_gan)|TOMADOR alts 09-19 (antes de B)|TOMADOR alts 20-21|celda fav alts 09-19|px med|acc med|T med|monedas tomador 09-18 (todas)|rellenos maker 09-18/19-21')
for w in rk.index:
    t=T[T.maker==w]
    if len(t)==0: print(w[:10],'sin actividad tomadora'); continue
    pre=t[t.alt&(t.dia<='2026-10-19')]; post=t[t.alt&(t.dia>='2026-10-20')]
    mon=t[t.dia<='2026-10-18'].act.value_counts(normalize=True).round(2).to_dict()
    print(f"{w[:10]}|({int(rk.loc[w,'n'])},{rk.loc[w,'su_gan']:+.2f})|{ev(pre)}|{ev(post)}|{ev(pre[pre.celda])}|{t.px.median():.2f}|{t.sh.median():.1f}|{t['T'].median():.0f}|{mon}|{NM[(w,'09-18')]}/{NM[(w,'19-21')]}")
