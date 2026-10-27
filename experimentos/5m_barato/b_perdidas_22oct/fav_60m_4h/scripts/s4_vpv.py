# s4_vpv.py: pujas virtuales (PREREG_FAV60 paso 2) sobre filas q/t del registro ms de tokens 60m. Orden por RECEPCION. Escribe datos/vpv_unidades.csv
import json, glob, gzip, sys, collections, csv
D='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/fav_60m_4h/datos/'
G=json.load(open(D+'tokmap_gamma.json')); TK=G['tokens']; MK=G['mercados']
BANDAS=[(0.10,0.30),(0.50,0.70),(0.70,0.90),(0.90,0.99)]
EPS=1e-9
import datetime as _dt
FILES=collections.defaultdict(list)
for f in sorted(glob.glob('/mnt/HC_Volume_106538179/agentes_datos/fav60_ms/*.60m.gz')): FILES[f.split('maker_ms_')[1][:10]].append(f)
def cargar(dia):
    """filas q/t de mercados 60m cuyo fin cae en (dia 00:00, dia+1 00:00], solo dentro de su ventana [fin-3600, fin]"""
    d0=int(_dt.datetime.fromisoformat(dia+'T00:00:00+00:00').timestamp()); ev=collections.defaultdict(list)
    for f in FILES[dia]:
        with gzip.open(f,'rt') as fh:
            for line in fh:
                c=line.rstrip('\n').split(',')
                v=TK.get(c[2]) if len(c)>=7 else None
                if not v or v[1]!='60min' or not (d0<v[3]<=d0+86400): continue
                try:
                    if c[0]=='q':
                        recv=int(c[7]); 
                        if not (v[3]-3600<=recv/1000.0<=v[3]): continue
                        ev[v[2]].append((recv,'q',v[4],float(c[3]) if c[3] else None,float(c[4]) if c[4] else None))
                    elif c[0]=='t':
                        recv=int(c[6])
                        if not (v[3]-3600<=recv/1000.0<=v[3]): continue
                        ev[v[2]].append((recv,'t',v[4],float(c[3]),None))
                except (ValueError,IndexError): continue
    return ev
out=[]
for dia in sorted(FILES):
  ev=cargar(dia); print(dia,'mercados',len(ev),sum(len(x) for x in ev.values()),flush=True)
  for mid,E in ev.items():
      m=MK.get(mid); 
      if not m: continue
      fin=m['fin']; E=sorted(set(E),key=lambda x:x[0])
      lados=['Up','Down']; book={'Up':[None,None],'Down':[None,None]}
      abiertas={}   # (lado,banda) -> dict
      hechos=set()
      for recv,tipo,lado,a,b in E:
          t=recv/1000.0; T=fin-t
          opp='Down' if lado=='Up' else 'Up'
          # 1) comprobar rellenos de pujas vivas con este evento
          for (s,bd),u in abiertas.items():
              if u['pes'] is not None and u['opt'] is not None: continue
              if t<u['t0']+0.1 or T<60: continue
              P=u['P']; pes=opt=False
              if tipo=='q':
                  if a is None or b is None or a>=b: continue   # libro cruzado/vacio: no cuenta (PREREG)
                  if lado==s and b is not None: pes=b<=P-0.01+EPS; opt=b<=P+EPS
                  if lado!=s and a is not None: pes=pes or a>=1-P+0.01-EPS; opt=opt or a>=1-P-EPS
              else:
                  if lado==s: pes=a<=P-0.01+EPS; opt=a<=P+EPS
                  else: pes=a>=1-P+0.01-EPS; opt=a>=1-P-EPS
              if opt and u['opt'] is None: u['opt']=t
              if pes and u['pes'] is None: u['pes']=t
          if tipo!='q': continue
          book[lado]=[a,b]
          bid,ask=a,b
          if bid is None or ask is None or bid>=ask: continue
          if not (120<T<=3600): continue
          for lo,hi in BANDAS:
              if lo-EPS<=bid<hi-EPS and (lado,lo) not in hechos:
                  hechos.add((lado,lo)); abiertas[(lado,lo)]=dict(t0=t,P=round(bid,3),T0=T,ask0=ask,pes=None,opt=None)
      for (s,lo),u in abiertas.items():
          out.append(dict(mid=mid,coin=m['coin'],fin=fin,lado=s,banda=lo,P=u['P'],T0=round(u['T0']),ask0=u['ask0'],
                          fill_pes=int(u['pes'] is not None),fill_opt=int(u['opt'] is not None),
                          t_fill_pes=round(u['pes']-u['t0'],1) if u['pes'] else '',win=('' if m['win'] is None else int(m['win']==s))))
with open(D+'vpv_unidades.csv','w',newline='') as fh:
    w=csv.DictWriter(fh,fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
print('unidades',len(out))
