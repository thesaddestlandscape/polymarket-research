# Estado exacto del agente (20-Oct ~12:45Z) — encargo §1b pasos (1)(2)(3)
## Hecho (todo sin commitear, bajo experimentos/5m_barato/)
- Paso 1 H55: `h55_forward/vigia_5m_barato_h55_forward.py` (+ `m5b_anidado_regla.py` decisión pura, `m5b_anidado_dia.py` extractor BTC por día, `m5b_anidado_stats.py`). Hash de manifiesto = config + 4 ficheros. Salida: DL/vigia_5m_barato_anidado/entradas_D.csv.gz (+meta.json) y DL/vigia_5m_barato_h55/informe.{json,txt}. Tests: `python3 -m pytest -q h55_forward/test_h55_forward.py` -> 7 passed (fixture sintética, idempotencia, parcial, congelación, solo lectura).
- Paso 2: `h55_forward/vigia_5m_barato_h53_forward.py` (H53 + H54 emparejado maker/tomador/combinado + V4 réplica), misma maquinaria; salida DL/vigia_5m_barato_h53/.
- Paso 3: `rampa_plantilla/{rampa_plantilla.py,spec_h55.json,tabla_rampa_h55.txt,.json,ESPECIFICACION_BRAZO_H55_F2.md}`.
## NO hecho / pendiente
- Extracción real 19-20 Oct NO ejecutada: el runner espera load5<20 y MemAvailable>2,5 GB (load5 era 23-28). Validación contra descubrimiento (18-Oct) tampoco. Ningún informe forward generado; el vigía no ha corrido sobre datos reales (solo fixture).
- Manifiestos aún no creados (no se ha corrido `procesar`): el código sigue editable hasta el primer `procesar`.
- F2 no modificado; sin cron ni procesos persistentes.
## Procesos que dejé corriendo
- PID 175720 `bash correr_extraccion.sh 2026-10-19 2026-10-20 2026-10-18` (espera condiciones; nice 19 ionice idle ulimit 3 GB; log /mnt/HC_Volume_106538179/datalogs_analisis_caches/h55_forward/extraccion.log; escribe solo DL/vigia_5m_barato_anidado/). Padre 175717 es el shell. Un `esperar_extraccion.sh` en background (id bvw0lmbx4, máx 100 min, solo lee el log). Parar: `kill 175720`.
## Retomar
cd /root/polymarket-research/experimentos/5m_barato/h55_forward && python3 vigia_5m_barato_h55_forward.py procesar --dia 2026-10-19 (idem h53) y luego `... informe`; 20-Oct se marca parcial hasta 00:10Z del 21.
## Números clave (descubrimiento 06-18, NO OOS)
H55: n=36 ejecutables/69 disparos, 2,77 entradas/día, EV pond +0,179 IC90 cierre (+0,012;+0,341), precio medio 0,645, acierto 0,78, sd 0,71/€. Coste medio por entrada a "2 €" = 3,3 € (5 acciones mínimo): 100 % > 2 €. Techo capacidad nivel 1 ≈ 23,6 k€/año (punto), 5,3 k (sin 2 mejores días +0,04), 0,7 k (cota inf). 200 k€ inalcanzable con H55 solo (haría falta ~8,5x volumen al EV puntual). €/año al stake 2/10/100/500: 596 [-76;1.316] / 1.710 / 11.024 / 31.227 (EV empírico, IC90 días). Kill K1 falso 23-29 % con EV +0,04; P(gate) 72 % a 28 d solo si EV real=+0,179, 7-19 % con EV prudente.
