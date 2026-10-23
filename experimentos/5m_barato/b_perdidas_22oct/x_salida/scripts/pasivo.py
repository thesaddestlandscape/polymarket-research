# MODO PASIVO: recalcula cada regla sobre el flujo REAL de B (solo lectura de posiciones.csv). No toca B. Uso: python3 -I pasivo.py
import pandas as pd, sys, csv, os, datetime
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from xs_sim import sim,REGLAS
P='/root/polymarket-research/experimentos/5m_barato/contabilidad_wallet_dedicada/posiciones.csv'
O='/root/polymarket-research-datalogs/x_salida/pasivo.csv'
ts=lambda c:(pd.to_datetime(c,utc=True)-pd.Timestamp('1970-01-01',tz='UTC')).dt.total_seconds().astype('int64')
d=pd.read_csv(P); b=d[(d.experimento=='H47-B')&d.estado.str.startswith('liquidada')].copy()
b['t']=ts(b.fecha_primer_fill_utc); b['fin']=ts(b.fin_mercado_utc); b=b.sort_values(['fin','t'])
flow=[(int(f),int(f//86400),tuple(g.coste.values),tuple(g.pnl_realizado.values)) for f,g in b.groupby('fin')]
now=datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%MZ'); rows=[]
for env,(Ei,H) in {'S_real':(19.59,12.0),'S_H0':(19.59,0.0)}.items():
    for dia in sorted({x[1] for x in flow}):
        fl=[x for x in flow if x[1]<=dia]
        for k,r in REGLAS.items():
            m=sim(fl,r,Ei,H=H); rows.append([now,env,datetime.datetime.utcfromtimestamp(dia*86400).strftime('%Y-%m-%d'),k,round(m['pnl'],3),m['takes'],round(m['cost'],2),round(m['dd'],2),int(m['halted'])])
new=not os.path.exists(O)
with open(O,'a',newline='') as f:
    w=csv.writer(f)
    if new: w.writerow(['calculado','entorno','hasta_dia','regla','pnl_acum','posiciones_tomadas','coste','dd_max','parada'])
    w.writerows(rows)
print(len(rows),'filas ->',O)
