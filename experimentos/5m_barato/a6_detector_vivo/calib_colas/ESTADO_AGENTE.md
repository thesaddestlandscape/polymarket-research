# Estado del agente de calibración de colas (20-Oct ~12:25Z)
(sys.path de los scripts apunta al scratchpad de la sesión; si no existe, copiar analiza.py/runner.py/agrega.py de este directorio y cambiar la ruta `sys.path.insert` en runner.py/agrega.py/final_tabla.py a este directorio.)

## Calibradas (parte A, kind='g', libro5, L=85 ms, ventana de explicación [-300,+150] ms)
- BTC COMPLETA: n=2248 pujas, 859 mercados, 4 días. c prop 0,90 (IC90 días 0,88-0,92), lo 0,84 (0,81-0,88), hi 0,92 (0,90-0,94). f* 0,3 (rango 0,1-0,7). Cola recomendada: base central, rango [opt,cons]. Tablas: calib_colas/tablas_BTC.txt.
- ETH PARCIAL (934 pujas, ~300 mercados alternos, 3 días): c prop 0,98 (0,97-0,99); f* 0,1-0,9. Tablas: tablas_ETH_parcial.txt.
## Pendientes
- ETH completo, SOL, XRP, DOGE, BNB (no medidos); sensibilidades L=79/254 ms y ventana de explicación (BTC día 19, mercados alternos); tabla moneda x bucket x tramo final; actualizar calibracion_colas.md.
- Parte B: DATA_BLOCKED (0 rellenos reales; esperar H47-B).
## Datos / ficheros
- Cache (volumen): /mnt/HC_Volume_106538179/datalogs_analisis_caches/colas_20oct/ : mk/<MONEDA>_<mkt>.gz (extractos libro5 BTC/ETH/SOL/XRP completos; DOGE/BNB extracción 14/16 ficheros hecha, SIN terminar), tokens.json, muestras_<MONEDA>.ndjson (BTC completo, ETH parcial), orden_ficheros.txt, extract2_progreso.txt, runner2.log.
- Scripts (copias): calib_colas/{extract.py,analiza.py,runner.py,agrega.py,tabla.py,final_tabla.py,valida_cola.py,run2.sh,run3_reanudar.sh}.
## Jobs en marcha
- `run2.sh` (bash, nohup, nice 19 ionice -c3, ulimit 3 GB), lanzado 11:39Z, hoy en la extracción DOGE/BNB. NO está en setsid: puede morir al cerrarse la sesión. Si muere: ejecutar run3_reanudar.sh (borra mk/DOGE_*,BNB_* y reextrae para no duplicar; el runner salta mercados ya hechos).
## Siguiente comando exacto
`setsid nohup nice -n 19 ionice -c3 bash /root/polymarket-research/experimentos/5m_barato/a6_detector_vivo/calib_colas/run3_reanudar.sh > /mnt/HC_Volume_106538179/datalogs_analisis_caches/colas_20oct/run3.out 2>&1 &`
(solo si run2.sh ya no corre: comprobar con `ps -eo pid,args | grep run2.s[h]`). Cuando aparezca ANAFIN en runner2.log: `python3 -I final_tabla.py ETH,SOL,XRP,DOGE,BNB` y `python3 -I final_tabla.py BTC`; sensibilidades: `final_tabla.py BTC _sL79` etc. (tras SENSFIN). Después actualizar calibracion_colas.md (tabla por moneda, cola por moneda para A6/H23).
