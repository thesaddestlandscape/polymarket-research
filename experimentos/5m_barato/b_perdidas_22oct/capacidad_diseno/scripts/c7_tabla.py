#!/usr/bin/env python3
"""c7: €/año por diseno (celdas DISJUNTAS) y suma. Entrada datos/disenos.csv (c1) y c2/c6. Cuotas ancladas: 0,4 % = R3 5 acc medido (136 EUR/dia sobre 33,9 k); 0,9 % = R3 K20 medido (x2,3);
3 % = supuesto no medido. Brecha de ejecucion de B (-0,053, n=202, IC90 cierre -0,32..+0,20) como estres. Rebate: solo si el maker acumula >= 1 EUR/dia (umbral medido en c5)."""
import csv
R={r['nombre']:r for r in csv.DictReader(open('../datos/disenos.csv'))}
f=lambda r,k: float(r[k])
GAP=0.053
disj=[ # nombre, etiqueta clase
 ('B: 5m ALT3 0,10-0,30','nucleo B'),('5m BTC 0,10-0,20','alt BTC'),('5m BTC 0,20-0,30','alt BTC'),('5m BNB+DOGE 0,10-0,30','alt'),
 ('5m ALL 0,05-0,10','banda'),('5m ALL 0,30-0,50','banda'),('5m ALL 0,90-0,99','favoritos'),('15m ALT3 0,70-0,99','favoritos'),('15m ALL 0,30-0,50','15m'),('15m BTC 0,10-0,30','15m'),
 ('60m ALL 0,70-0,90','60m 4d')]
tot={'c':0,'b':0,'o':0,'bg':0,'og':0}
out=[]
for n,cl in disj:
    r=R[n]; V=f(r,'vol_dia'); ev=f(r,'ev'); lo=f(r,'ic_d_lo'); s2=f(r,'ev_sin2d'); oos=f(r,'ev_oos') if r['ev_oos']!='nan' else ev; evr=f(r,'ev_reb')-ev
    cons_ev=max(0,min(lo,s2,oos))                  # exige TODOS >0
    base_ev=max(0,oos+evr)                          # OOS + rebate pagado
    opt_ev=max(0,ev+evr)
    c=V*0.004*cons_ev*365; b=V*0.009*base_ev*365; o=V*0.03*opt_ev*365
    bg=V*0.009*max(0,oos+evr-GAP)*365; og=V*0.03*max(0,ev+evr-GAP)*365
    out.append((n,cl,V,ev,lo,s2,oos,evr,c,b,o,bg,og))
    for k,v in zip(('c','b','o','bg','og'),(c,b,o,bg,og)): tot[k]+=v
print('| diseno | clase | vol/dia | EV16d | IC90d lo | sin2d | OOS | +reb | cons | base | opt | base-brecha | opt-brecha |')
for o in out: print(f"| {o[0]} | {o[1]} | {o[2]:,.0f} | {o[3]:+.3f} | {o[4]:+.3f} | {o[5]:+.3f} | {o[6]:+.3f} | {o[7]:+.3f} | {o[8]:,.0f} | {o[9]:,.0f} | {o[10]:,.0f} | {o[11]:,.0f} | {o[12]:,.0f} |")
print('SUMA', {k:round(v) for k,v in tot.items()})
