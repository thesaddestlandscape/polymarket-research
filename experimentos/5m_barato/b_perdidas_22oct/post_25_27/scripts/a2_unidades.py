# A2: unidades B (posiciones) con etiquetas L1, regimen R-TEND, flags R2/R3 (r3shadow), S1p (Binance), markouts. Salida datos/pos_b.csv. Solo lectura.
import pandas as pd, numpy as np, json, gzip, glob, os, bisect
D='/root/polymarket-research-datalogs'; C='/root/polymarket-research/experimentos/5m_barato/contabilidad_wallet_dedicada'
S='/tmp/claude-0/-root-polymarket-research/3253f6f0-a68e-48c4-97db-8bfe225d6aca/scratchpad'
OUT='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/post_25_27/datos'
p=pd.read_csv(f'{C}/posiciones.csv'); p=p[p.rol.str.startswith('maker')].copy()
p['dia']=p.fecha_primer_fill_utc.str[:10]; p['t_fill']=pd.to_datetime(p.fecha_primer_fill_utc,utc=True).astype('int64')//10**9
p['pnl']=p.pnl_realizado
L=pd.concat([pd.read_csv(f'{D}/etiquetado_pasivo_B/etiquetado_B_{d}.csv.gz') for d in ['2026-10-20','2026-10-21','2026-10-22','2026-10-23']])
L=L[L.unidad=='posicion'][['mercado','outcome','coin','lado','T_s','fin_s','t0','t0_fuente','rpre_bps','r900_bps','clase_rpre','h_w1','gana_lado']]
P=p.merge(L,on=['mercado','outcome'],how='left',validate='1:1'); assert P.coin.notna().all(), P[P.coin.isna()].mercado.tolist()
P['tmin']=(P.fin_s//60-5).astype(int)
E=pd.concat([pd.read_csv(f) for f in sorted(glob.glob(f'{D}/regimen_5m/etiquetas/regimen_*.csv.gz'))]+[pd.read_csv(f'{S}/reg/etiquetas/regimen_2026-10-23.csv.gz')])
E=E.drop_duplicates(['coin','tmin'],keep='last')[['coin','tmin','R','D','COH','ER60','VR240']]
P=P.merge(E,on=['coin','tmin'],how='left'); P['R']=P.R.fillna('NA')
# ledger
ord_={}; pf={}; tard={}
for l in open(f'{D}/experimento_h47_B_ledger.jsonl'):
    d=json.loads(l); t=d['tipo']
    if t=='puja_post': ord_[d['oid']]=d
    elif t=='puja_fin': pf[d['slug']]=d
    elif t=='relleno_tardio': tard.setdefault(d['slug'],[]).append(d)
bym={}
for o in ord_.values(): bym.setdefault((o['slug'],o['lado']),[]).append(o)
# orden que origina la posicion, markouts
tdec=[];prec=[];mk5=[];mk30=[];mk120=[];tdet=[];espera=[]
for r in P.itertuples():
    lado=r.lado; oid=None; f=pf.get(r.mercado); rl=[]
    if f:
        rl=[x for x in f['rellenos']]
        if rl: oid=rl[0]['oid']
    if oid is None and r.mercado in tard: oid=tard[r.mercado][0]['oid']
    o=ord_.get(oid) if oid else None
    if o is None:   # ultima orden anterior al fill en ese slug+lado
        c=[x for x in bym.get((r.mercado,lado),[]) if x['t_dec']<=r.t_fill]; o=max(c,key=lambda x:x['t_dec']) if c else None
    tdec.append(o['t_dec'] if o else np.nan); prec.append(o['precio'] if o else np.nan)
    if rl:
        w=np.array([x['acc'] for x in rl]); 
        def wm(k):
            v=np.array([x.get(k) if x.get(k) is not None else np.nan for x in rl],float); ok=np.isfinite(v); return float((v[ok]*w[ok]).sum()/w[ok].sum()) if ok.any() else np.nan
        mk5.append(wm('markout_5s'));mk30.append(wm('markout_30s'));mk120.append(wm('markout_120s')); tdet.append(rl[0]['t_deteccion']); espera.append(rl[0].get('espera_s',np.nan))
    else: mk5.append(np.nan);mk30.append(np.nan);mk120.append(np.nan);tdet.append(np.nan);espera.append(np.nan)
P['t_dec']=tdec;P['precio_orden']=prec;P['mk5']=mk5;P['mk30']=mk30;P['mk120']=mk120;P['t_det']=tdet;P['espera_s']=espera
# r3shadow: ultima muestra <= t_dec (<=6 s)
sh={}
for f in sorted(glob.glob(f'{D}/r3_shadow/r3_shadow_2026-10-2[23].jsonl.gz')):
    for l in gzip.open(f,'rt'):
        if '"tipo":"smp"' not in l and '"tipo":"dec"' not in l: continue
        d=json.loads(l)
        if d.get('b15') is None: continue
        sh.setdefault((d['slug'],d['lado']),[]).append((d['r'],d['b15'],d['vol30'],d['hora']))
for k in sh: sh[k].sort()
b15=[];v30=[];hr=[]
for r in P.itertuples():
    a=sh.get((r.mercado,r.lado)); res=(np.nan,np.nan,np.nan)
    if a and np.isfinite(r.t_dec):
        rs=[x[0] for x in a]; i=bisect.bisect_right(rs,int(r.t_dec*1000))-1
        if i>=0 and r.t_dec*1000-rs[i]<=6000: res=a[i][1:]
    b15.append(res[0]);v30.append(res[1]);hr.append(res[2])
P['b15']=b15;P['vol30']=v30;P['hora_sh']=hr
P['gap15_mil']=np.round((P.b15-P.precio_orden)*1000)
P['RB2_pasa']=np.where(P.b15.notna(),(P.gap15_mil<=30),np.nan)
P['RB3_pasa']=np.where(P.b15.notna(),((P.gap15_mil<=30)&(P.vol30>=26)&(P.hora_sh>=4)),np.nan)
# S1p: Binance mid (recepcion) 2 s antes de t_det
bt={}
for d in ['2026-10-20','2026-10-21','2026-10-22','2026-10-23']:
    x=pd.read_csv(f'{D}/binance_bookticker_{d}.csv',usecols=['ts_recepcion_ms','activo','mid'])
    for c,g in x.groupby('activo'): bt.setdefault(c,[]).append(g.sort_values('ts_recepcion_ms'))
bt={c:pd.concat(v).sort_values('ts_recepcion_ms') for c,v in bt.items()}
def mid_at(c,t_ms):
    g=bt.get(c); 
    if g is None: return np.nan
    i=np.searchsorted(g.ts_recepcion_ms.values,t_ms,side='right')-1
    return g.mid.values[i] if i>=0 and t_ms-g.ts_recepcion_ms.values[i]<60000 else np.nan
mv=[]
for r in P.itertuples():
    if not np.isfinite(r.t_det): mv.append(np.nan); continue
    a=mid_at(r.coin,(r.t_det-2)*1000); b=mid_at(r.coin,r.t_det*1000); sg=1 if r.lado=='YES' else -1
    mv.append((b/a-1)*1e4*sg if np.isfinite(a) and np.isfinite(b) else np.nan)
P['mov2s_bps_lado']=mv      # <0 = Binance en contra del lado comprado
P['S1p_salta']=np.where(P.mov2s_bps_lado.notna(),(P.mov2s_bps_lado<=-2.0),np.nan)
# tanda r25-r27 (por hora del primer fill)
def run(t):
    return np.select([t>='2026-10-23T08:50:17Z',t>='2026-10-23T07:50:24Z',t>='2026-10-23T06:30:54Z'],['r27','r26','r25'],default='previa')
P['run']=run(P.fecha_primer_fill_utc)
P['hora']=P.fecha_primer_fill_utc.str[11:13].astype(int)
P['precio']=P.precio_medio; P['cierre']=P.fin_s
P.to_csv(f'{OUT}/pos_b.csv',index=False)
print(len(P),P.dia.value_counts().sort_index().to_dict()); print('NaN: t_dec',P.t_dec.isna().sum(),'t_det',P.t_det.isna().sum(),'b15',P.b15.notna().sum(),'R NA',(P.R=='NA').sum(),'mov2s',P.mov2s_bps_lado.notna().sum())
print(P[P.dia=='2026-10-23'][['mercado','run','lado','precio','acc' if 'acc' in P else 'acciones','h_w1','R','gap15_mil','vol30','RB2_pasa','RB3_pasa','mov2s_bps_lado','mk5','mk30','pnl']].to_string())
