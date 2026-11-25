#!/usr/bin/env python3
"""t4d_passT_lat.py LAT_MS STAMP ENG DIA -- ejecuta passT_v4.py SIN EDITARLO con la latencia de alta del motor sustituida: engine.LAT_POST = LAT_MS (en passT_v4 y engine el valor 68 era el RTT del POST del modelo; aqui = latencia REAL alta ex-envio de los ensayos reales vigentes paquete_l B2/B3/B5, 13-Nov, n=313: p50 38/34/35 ms, p90 147/47/42 ms).
Salida en $PASST_OUT. 0 ordenes. Misma politica G0, mismo motor de relleno; solo cambia cuando la orden esta viva (t_arr = t_dec + LAT)."""
import sys, os, runpy
lat = int(sys.argv[1]); stamp, eng, d = sys.argv[2:5]; L2 = '/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/'; P2 = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/'
sys.path.insert(0, L2); sys.path.insert(0, P2 + 'escalera_B'); import engine as G; assert G.LAT_POST == 68, G.LAT_POST; G.LAT_POST = lat
sys.argv = [L2 + 'passT_v4.py', stamp, eng, d]; os.chdir(L2); runpy.run_path(L2 + 'passT_v4.py', run_name='__main__')
