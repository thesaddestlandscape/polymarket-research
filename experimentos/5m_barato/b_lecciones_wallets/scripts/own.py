import json,csv,sys,collections
sys.path.insert(0,sys.argv[1]); S=sys.argv[1]
from common import *
L=json.load(open(S+'/ledger_extract.json')); des=json.load(open(S+'/des_pujas.json'))
pos=[r for r in csv.DictReader(open('/root/polymarket-research/experimentos/5m_barato/contabilidad_wallet_dedicada/posiciones.csv')) if r['experimento']=='H47-B']
mov=[r for r in csv.DictReader(open('/root/polymarket-research/experimentos/5m_barato/contabilidad_wallet_dedicada/movimientos.csv')) if r['experimento']=='H47-B' and r['tipo']=='COMPRA']
us='0x659a40ff9920febc5a66836213040924343d297f'; EX='0xe111180000d2663c0091e4f400237545b87b996b'
oc=[]
for d in ('2026-10-20','2026-10-21'):
    oc+=list(csv.reader(open(S+f'/our_tx_{d}.csv')))
bytx=collections.defaultdict(list)
for r in oc: bytx[r[3]].append(r)
bt=load_bt(['2026-10-20','2026-10-21']); cl=load_cl(['2026-10-20','2026-10-21'])
fills=[]
for m in mov:
    rows=bytx[m['tx']]
    ours=[r for r in rows if r[0]=='F' and r[6].lower()==us]
    for o in ours:
        oid=o[5]; tk=o[7].lower()
        # orden tomadora: fila F con maker=tk y taker=EX, y M
        tko=[r for r in rows if r[0]=='F' and r[6].lower()==tk and r[7].lower()==EX]
        mm=[r for r in rows if r[0]=='M']
        mk_others=[r for r in rows if r[0]=='F' and r[7].lower()==tk and r[6].lower()!=us]
        info=L['orders'].get(oid)
        sh=float(o[11]) if o[8]=='0' else float(o[10])
        usd=float(o[10]) if o[8]=='0' else float(o[11])
        f=dict(tx=m['tx'],oid=oid,slug=m['mercado'],outcome=m['outcome'],tanda=m['tanda_B'],precio=usd/sh,sh=sh,coste=usd,
               ts_block=float(o[2]),taker=tk,
               tk_side=(tko[0][8] if tko else None),tk_tok_same=(tko[0][9]==o[9] if tko else None),
               tk_fee=(float(tko[0][12]) if tko else None),
               tk_sh=(float(tko[0][11]) if tko and tko[0][8]=='0' else (float(tko[0][10]) if tko else None)),
               tk_usd=(float(tko[0][10]) if tko and tko[0][8]=='0' else (float(tko[0][11]) if tko else None)),
               n_makers_tx=1+len(set(r[6] for r in mk_others)),
               niveles_tx=len(set(round((float(r[10])/float(r[11]) if r[8]=='0' else float(r[11])/float(r[10])),3) for r in mk_others+[o])))
        if info:
            f.update(T_post=info['T'],t_dec=info['t_dec'],n_orden=info['n_orden'],cola_post=info['cola'],p_post=info['precio'],coin=info['coin'],lado=info['lado'])
        lec=L['lect'].get(oid,[])
        f['t_det']=min((iso2e(x['ts']) for x in lec),default=None)
        f['tras_cancel']=any(x.get('tras_cancel') for x in lec)
        f['tardio']=any(x.get('tipo')=='relleno_tardio' for x in lec)
        fills.append(f)
print('fills',len(fills),'sin info ledger',sum(1 for f in fills if 'T_post' not in f))
# fin de mercado y desenlace
for f in fills:
    st=int(f['slug'].rsplit('-',1)[1]); f['inicio']=st; f['fin']=st+300
    f['coin']=f['slug'].split('-')[0].upper()
    f['des']=des.get(f['slug']); side='YES' if f['outcome']=='Up' else 'NO'; f['lado']=side
    f['gana']=(f['des']==side)
    f['pnl']=(f['sh'] if f['gana'] else 0)-f['coste']
    # tiempo de casado estimado: deteccion propia (poll) o bloque-2.4
    cands=[x for x in (f['t_det'],f['ts_block']-2.4) if x]
    f['t_fill']=min(cands); f['T_fill']=f['fin']-f['t_fill']
    sg=1 if side=='YES' else -1
    a=f['coin']; t=f['t_fill']
    for nm,(x0,x1) in dict(pre30=(-30,0),pre10=(-10,0),pre3=(-3,0),pre10x=(-10,-1.5),pre5x=(-5,-1.5),pre20x=(-20,-1.5),post3=(0,3),post10=(0,10),post30=(0,30),toend=(0,None)).items():
        x1v=(f['fin']-t) if x1 is None else x1
        r=ret_bps(bt[a],t+x0,t+x1v); f['bn_'+nm]=None if r is None else sg*r
        r2=ret_bps(cl[a],t+x0,t+x1v); f['cl_'+nm]=None if r2 is None else sg*r2
    ref=twap_ref(cl,a,f['inicio'])
    sp=px_at(cl[a],t); spd=px_at(cl[a],f.get('t_dec',t))
    f['marg_fill']=None if (ref is None or sp is None) else sg*(sp/ref-1)*1e4
    f['marg_dec']=None if (ref is None or spd is None) else sg*(spd/ref-1)*1e4
    f['hora']=datetime.fromtimestamp(t,timezone.utc).hour
    f['dia']=datetime.fromtimestamp(t,timezone.utc).strftime('%m-%d')
json.dump(fills,open(S+'/own_fills.json','w'))
# cuadre con posiciones
pp={(r['mercado'],r['outcome']):r for r in pos}
agg=collections.defaultdict(lambda:[0,0])
for f in fills: agg[(f['slug'],f['outcome'])][0]+=f['coste']; agg[(f['slug'],f['outcome'])][1]+=f['pnl']
bad=[(k,v,pp.get(k,{}).get('pnl_realizado')) for k,v in agg.items() if k not in pp or abs(float(pp[k]['pnl_realizado'])-v[1])>0.011]
print('posiciones',len(agg),'vs',len(pp),'descuadres',bad[:5])
print('pnl total',round(sum(f['pnl'] for f in fills),3),'coste',round(sum(f['coste'] for f in fills),3))
