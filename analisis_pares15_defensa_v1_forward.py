#!/usr/bin/env python3
"""analisis_pares15_defensa_v1_forward.py -- PAIR15_DEFENSA_V1, CONGELADA 13-Oct ~10:30Z ANTES de ver datos forward.
Origen: punto 3 (salir si Binance va en contra antes del 1er relleno; analisis_pares15_defensa_cancelacion.py) + H-C del
híbrido (cubrir la pata suelta como tomador cerca del cierre aunque el par cueste >=1; analisis_15m_hibrido_mecanismo.py).
Descubrimiento (09-10 Oct) base −18,54 → −5,29 $; 12-13 Oct (también mirado al elegir T=240) −9,78 → +3,90 $ (IC cruza 0).
NADA de esto cuenta como validación. Regla sobre la política 'crear' del ensayo en seco (experimento_pares_cola_15m.py):
  (1) SALIR: si en la rejilla de 500 ms desde el inicio hasta (1er relleno − 200 ms) el retorno de Binance de 1 s va EN
      CONTRA de YES o de NO >= 1 bp -> cancelar todo y no operar ese mercado (PnL 0).
  (2) CUBRIR: si a T = 240 s queda pata suelta (y no hubo más rellenos después), comprar el exceso del lado contrario
      al ask real de nivel 1 (si cabe) pagando comisión; el par queda cerrado aunque cueste >= 1.
Forward: SOLO mercados con mercado_fin posterior a --desde (por defecto 2026-10-13T10:30). Gate: >= 80 mercados, IC90
bootstrap por mercados > 0, sin el mejor día > 0, BTC y SOL ambas >= 0. Uso: python3 analisis_pares15_defensa_v1_forward.py [--desde ISO]
"""
import sys, numpy as np
sys.path.insert(0,'/root/polymarket-research')
from analisis_pares15_patas_sueltas import cargar_mercados, cargar_libros, libro_en, pnl_original, fee
from analisis_pares15_defensa_cancelacion import cargar_binance, rasgos, LAT
from analisis_maker_cancelacion_binance import desenlaces
import argparse
ap=argparse.ArgumentParser(); ap.add_argument("--desde", default="2026-10-13T10:30"); A=ap.parse_args()
fwd=[m for m in cargar_mercados(A.desde,"2099") if m["pol"]=="crear"]
desc, val = [], fwd
gan=desenlaces({m["id"] for m in desc+val}); L=cargar_libros(desc+val)
B=cargar_binance(sorted({m["dia"] for m in desc+val}))
print(f"PAIR15_DEFENSA_V1 forward: {len(val)} mercados crear (BTC {sum(m['moneda']=='BTC' for m in val)}, SOL {sum(m['moneda']=='SOL' for m in val)})")
def cubrir(m,o,g,Tc=240):
    res=o["lado_res"]; otro="NO" if res=="YES" else "YES"; sobra=o["acc"][res]-o["par"]
    t_c=(m["cierre"]-Tc)*1000
    if max(t for t,*_ in m["fills"])*1000>t_c: return None
    b=libro_en(L,m["id"],otro,t_c)
    if not b or b[1] is None or b[3] is None or b[3]<sobra: return None
    return o["pnl_par"]+o["pnl_res"]+sobra*((1.0 if g==otro else 0.0)-b[1])-sobra*fee(b[1])
for nom,M in (("FORWARD desde "+A.desde,val),):
    r={"base":[], "cubrir240":[], "salir_bn1>=1":[], "salir+cubrir":[]}
    for m in M:
        g=gan.get(m["id"])
        if g is None or not m["fills"]:
            for k in r: r[k].append(0.0)
            continue
        o=pnl_original(m,g); tot=o["pnl_par"]+o["pnl_res"]
        c=cubrir(m,o,g) if o["lado_res"] is not None else None
        cub=tot if c is None else c
        t0=int(m["fills"][0][0]*1000)-LAT; inicio=(m["cierre"]-898)*1000
        sal=any(((rasgos(m,"YES",t,L,B)[0] or -9)>=1) or ((rasgos(m,"NO",t,L,B)[0] or -9)>=1) for t in range(inicio,t0+1,500))
        r["base"].append(tot); r["cubrir240"].append(cub); r["salir_bn1>=1"].append(0.0 if sal else tot); r["salir+cubrir"].append(0.0 if sal else cub)
    out=[]
    for k,v in r.items():
        v=np.array(v); bs=np.random.default_rng(1).integers(0,len(v),(2000,len(v))); s=v[bs].sum(1)
        out.append(f"{k} {v.sum():+.2f} $ (IC90 {np.quantile(s,.05):+.1f},{np.quantile(s,.95):+.1f})")
    print(f"{nom}: "+" | ".join(out))
