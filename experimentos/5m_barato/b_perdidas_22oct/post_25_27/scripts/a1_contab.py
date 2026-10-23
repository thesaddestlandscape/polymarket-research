# A1 contabilidad independiente (PREREG_POST2527). Solo lectura.
import pandas as pd, numpy as np, json
C='/root/polymarket-research/experimentos/5m_barato/contabilidad_wallet_dedicada'
m=pd.read_csv(f'{C}/movimientos.csv'); p=pd.read_csv(f'{C}/posiciones.csv')
d=json.load(open(f'{C}/estado_dashboard.json'))
print('movimientos',len(m),'tipos',m.tipo.value_counts().to_dict())
print('suma importes %.6f  saldo_acum_ultimo %.6f  saldo_onchain %.6f'%(m.importe_pusd.sum(),m.saldo_acumulado.iloc[-1],d['saldo']['pusd_onchain']))
m['dia']=m.fecha_utc.str[:10]
print(m.groupby(['dia','tipo']).importe_pusd.agg(['sum','count']).tail(12))
# por posicion: coste (COMPRA) y payout (REDENCION) por mercado/outcome
b=p[p.rol.str.startswith('maker')].copy()
print('posiciones maker',len(b),'coste %.4f payout %.4f pnl %.4f (pnl_realizado col %.4f)'%(b.coste.sum(),b.payout.sum(),(b.payout-b.coste).sum(),b.pnl_realizado.sum()))
for lab,sel in [('B total',b),('20-oct',b[b.fecha_primer_fill_utc<'2026-10-21']),('21-oct',b[(b.fecha_primer_fill_utc>='2026-10-21')&(b.fecha_primer_fill_utc<'2026-10-22')]),('22-oct',b[(b.fecha_primer_fill_utc>='2026-10-22')&(b.fecha_primer_fill_utc<'2026-10-23')]),('23-oct',b[b.fecha_primer_fill_utc>='2026-10-23'])]:
    print(lab,'n',len(sel),'ganadoras',int((sel.payout>0).sum()),'coste %.3f payout %.3f pnl %.3f EV/EUR %.4f'%(sel.coste.sum(),sel.payout.sum(),sel.payout.sum()-sel.coste.sum(),(sel.payout.sum()-sel.coste.sum())/sel.coste.sum()))
# identidad saldo: depositos + F1 + B pnl - ganadoras por redimir
f1=p[~p.rol.str.startswith('maker')]
print('F1 pnl %.5f ; 19 + F1 + Bpnl = %.5f ; saldo %.5f ; por redimir %.6f'%((f1.payout-f1.coste).sum(),19+(f1.payout-f1.coste).sum()+(b.payout-b.coste).sum(),d['saldo']['pusd_onchain'],d['pnl']['ganadoras_por_redimir_pusd']))
# redenciones de las ganadoras 23-oct
w=b[(b.fecha_primer_fill_utc>='2026-10-23')&(b.payout>0)]; print(w[['mercado','acciones','payout']])
print('REDEEM 23-oct:'); print(m[(m.dia=='2026-10-23')&(m.tipo!='COMPRA')][['fecha_utc','tipo','importe_pusd','mercado','size']])
# saldo al inicio de cada run (ultimo saldo_acum antes de la hora)
for h in ['2026-10-23T06:30:54','2026-10-23T07:50:24','2026-10-23T08:50:17','2026-10-24']:
    q=m[m.fecha_utc<h+'Z']; print('saldo acum antes de',h,round(q.saldo_acumulado.iloc[-1],4))
# rebate estimado (cota, no cobrado): 20% de fee taker 0.07*p*(1-p) por accion, solo posiciones B
b['reb']=0.2*0.07*b.precio_medio*(1-b.precio_medio)*b.acciones
print('rebate estimado B total %.4f ; 23-oct %.4f ; r25-r27 sobre coste 23-oct %.3f'%(b.reb.sum(),b[b.fecha_primer_fill_utc>='2026-10-23'].reb.sum(),b[b.fecha_primer_fill_utc>='2026-10-23'].coste.sum()))
