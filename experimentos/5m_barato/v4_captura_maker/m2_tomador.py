import csv,glob,json,collections,math,random
import numpy as np
DES=json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
OOS=1791288000000  # 2026-10-06T12:00Z
def fee(p): return 0.07*p*(1-p)
EV=[]
for f in sorted(glob.glob('/root/polymarket-research-datalogs/vigia_5m_barato/eventos_2026-10-*.csv')):
    for r in csv.DictReader(open(f)):
        if r['regla']!='B1_5m' or int(r['t_deteccion'])<OOS: continue
        sl='YES' if r['lado']=='Up' else 'NO'; o=DES.get(r['market_compra'])
        if o is None: continue
        g=1.0 if o==sl else 0.0
        e=dict(dia=f[-14:-4],mon=r['moneda'],prim=r['es_primero']=='1',g=g,ask=float(r['ask_compra_t0']),cl=r['L215_clase'],
               b5=float(r['bin_ret_5s_bps'] or 'nan')*(1 if r['lado']=='Up' else -1),edad=float(r['c_edad_ask_ms'] or 'nan'),
               csz=float(r['c_ask_sz'] or 'nan'),ocamb=float(r['o_cambios_1s'] or 'nan'),ccamb=float(r['c_cambios_1s'] or 'nan'),
               marg=float(r['margen_neto']),resto=float(r['resto_s']))
        for L in ('L150','L215','L250'):
            a=float(r[L+'_acciones'] or 0); p=float(r[L+'_precio'] or 'nan')
            e[L]=(a,p, a*g - a*p - a*fee(p) if a>0 else 0.0, a*p if a>0 else 0.0)
        EV.append(e)
def st(rows,L='L215'):
    rr=[e for e in rows if e[L][0]>0]
    if not rr: return 'n_ejec=0'
    P=sum(e[L][2] for e in rr); Cc=sum(e[L][3] for e in rr)
    byd=collections.defaultdict(lambda:[0,0])
    for e in rr: byd[e['dia']][0]+=e[L][2]; byd[e['dia']][1]+=e[L][3]
    ds=list(byd); bs=[]
    random.seed(1)
    for _ in range(2000):
        s=[random.choice(ds) for _ in ds]; c=sum(byd[d][1] for d in s); bs.append(sum(byd[d][0] for d in s)/c if c else 0)
    top=sorted(ds,key=lambda d:-byd[d][0])[:2]
    c2=sum(byd[d][1] for d in ds if d not in top); s2=sum(byd[d][0] for d in ds if d not in top)/c2 if c2 else float('nan')
    return f'n_ejec={len(rr)} dias={len(ds)} PnL={P:+.2f} coste={Cc:.2f} EVpond={P/Cc:+.3f} IC90d=({np.percentile(bs,5):+.2f},{np.percentile(bs,95):+.2f}) sin2={s2:+.3f}'
def linea(nom,rows):
    n=len(rows); ne=sum(1 for e in rows if e['L215'][0]>0); w=sum(e['g'] for e in rows); wl=sum(e['g'] for e in rows if e['L215'][0]==0)
    pa=np.mean([e['ask'] for e in rows]) if rows else float('nan')
    print(f'{nom:38s} señales={n:3d} acierto={w/max(n,1):.2f} vs ask={pa:.2f} | no_ejec={n-ne} ganan={wl:.0f} | {st(rows)}')
P=[e for e in EV if e['prim']]
print('== V4 (B1_5m 1ª señal, OOS desde 06-Oct 12Z, todas monedas, desenlace oficial) ==')
linea('V4 todas',P); linea('V4 L150 (suelo fisico)',P); print('   L150:',st(P,'L150'),'| L250:',st(P,'L250'))
for m in ('BTC','ETH','SOL','XRP','DOGE','BNB'): linea('  '+m,[e for e in P if e['mon']==m])
print('-- clase a 215 ms (todas): ',collections.Counter(e['cl'] for e in P))
for c in ('A_sigue_barato','A_sigue_barato_parcial','D_otro_nivel_barato','B_cancelado_o_repreciado','C_consumido'):
    rr=[e for e in P if e['cl']==c]; print(f'   {c:28s} n={len(rr):3d} acierto={np.mean([e["g"] for e in rr]) if rr else float("nan"):.2f} ask_med={np.mean([e["ask"] for e in rr]) if rr else float("nan"):.2f}')
print('-- rasgos en t0 (EXPLORATORIO, cortes fijados a priori; no elegir): fill215 y EV de los ejecutados')
for nom,key,cuts in (('edad ask ms','edad',(250,2000)),('c_ask_sz','csz',(20,100)),('o_cambios_1s (15m)','ocamb',(0.5,2.5)),('c_cambios_1s (5m)','ccamb',(0.5,2.5)),('margen_neto','marg',(0.08,0.15)),('ask t0','ask',(0.15,0.30)),('resto_s','resto',(120,220))):
    bins=[('<'+str(cuts[0]),lambda x:x<cuts[0]),('['+str(cuts[0])+','+str(cuts[1])+')',lambda x:cuts[0]<=x<cuts[1]),('>='+str(cuts[1]),lambda x:x>=cuts[1])]
    for bn,fn in bins:
        rr=[e for e in P if not math.isnan(e[key]) and fn(e[key])]
        ne=sum(1 for e in rr if e['L215'][0]>0)
        print(f'   {nom:18s} {bn:12s} n={len(rr):3d} fill={ne/max(len(rr),1):.2f} acierto_señal={np.mean([e["g"] for e in rr]) if rr else float("nan"):.2f} | {st(rr)}')
print('== V3: filtro Binance 5 s orientado (b5>=umbral) sobre V4 1ª señal y sobre V2 (todas) ==')
A=EV
for thr in (None,-3,-1,0,1):
    for nom,base in (('V4',P),('V2',A)):
        rr=base if thr is None else [e for e in base if not math.isnan(e['b5']) and e['b5']>=thr]
        linea(f'{nom} b5>={thr}',rr)
print('== V2/V3b colapsado por MERCADO (hasta 3 compras, riesgo<=6 €; unidad = mercado) ==')
import itertools
EV2=[]
for f in sorted(glob.glob('/root/polymarket-research-datalogs/vigia_5m_barato/eventos_2026-10-*.csv')):
    for r in csv.DictReader(open(f)):
        if r['regla']!='B1_5m' or int(r['t_deteccion'])<OOS: continue
        EV2.append((r['market_compra'],int(r['t_deteccion']),r))
def v2(thr):
    U=collections.OrderedDict()
    for mk,t,r in sorted(EV2,key=lambda x:(x[0],x[1])):
        e=[x for x in EV if x is not None]
    for mk,t,r in sorted(EV2,key=lambda x:x[1]):
        b5=float(r['bin_ret_5s_bps'] or 'nan')*(1 if r['lado']=='Up' else -1)
        if thr is not None and not (b5>=thr): continue
        a=float(r['L215_acciones'] or 0); p=float(r['L215_precio'] or 'nan')
        if a<=0: continue
        u=U.setdefault(mk,dict(dia=None,k=0,c=0.0,p=0.0))
        if u['k']>=3 or u['c']+a*p>6.0+1e-9: continue
        sl='YES' if r['lado']=='Up' else 'NO'; g=1.0 if DES[r['market_compra']]==sl else 0.0
        u['k']+=1; u['c']+=a*p; u['p']+=a*g-a*p-a*fee(p); u['dia']=r['t_deteccion']
    rows=[]
    import datetime
    for mk,u in U.items():
        if u['k']==0: continue
        d=datetime.datetime.utcfromtimestamp(int(u['dia'])/1000).strftime('%Y-%m-%d')
        rows.append(dict(dia=d,L215=(1,0,u['p'],u['c'])))
    return rows
for thr in (None,-3,-1,0):
    print(f'   V2 por mercado b5>={thr}:', st(v2(thr)))
print('== TOMADOR con colchon: limite = p_limite + k (renuncia a margen); relleno al ask real a +215 ms si <= limite y hay nivel 1 ==')
for k in (0.0,0.01,0.02,0.03,0.05):
    for nom,base in (('todas',P),('BTC',[e for e in P if e['mon']=='BTC'])):
        rows=[]; gan=0
        for f in sorted(glob.glob('/root/polymarket-research-datalogs/vigia_5m_barato/eventos_2026-10-*.csv')):
            pass
        for r in (x[2] for x in EV2):
            if r['es_primero']!='1': continue
            if nom=='BTC' and r['moneda']!='BTC': continue
            sl='YES' if r['lado']=='Up' else 'NO'; g=1.0 if DES[r['market_compra']]==sl else 0.0
            a=float(r['L215_acciones'] or 0); p=float(r['L215_precio'] or 'nan')
            if a<=0:
                lim=float(r['p_limite'])+k; disp=float(r['L215_disp_nivel1'] or 0)
                if not math.isnan(p) and p<=lim+1e-9:
                    a=max(5.0,2.0/p)
                else: a=0
            if a>0:
                import datetime
                d=datetime.datetime.utcfromtimestamp(int(r['t_deteccion'])/1000).strftime('%Y-%m-%d')
                rows.append(dict(dia=d,L215=(a,p,a*g-a*p-a*fee(p),a*p))); gan+=g
        print(f'   k=+{k:.2f} {nom:5s} ganadoras_capturadas={gan:.0f} |', st(rows))
