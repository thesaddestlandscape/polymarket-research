# H23 v3 (H69, re-puja 150 ms) · INFORME 21-Oct · EXPLORATORY · solo replay/dry-run · paquete v1 (sha 602d5a2debb42cc0), H47-B, h23shadow, vigías, screens y git INTACTOS
Estado del job: PARTIAL (manifest `/mnt/HC_Volume_106538179/datalogs_analisis_caches/h23_v3/run_manifest.json`, log `run_v3.log`): hechos 19-20 Oct (OOS) y 13-Oct (validación); en cola 06-12 y 14-18 Oct (re-simulación EXACTA con tamaño real). 0 duplicados por clave. Reanudable: `bash v3/run_v3.sh` (salta lo hecho).
## (1) Conciliación (`v3/concilia_escalado.py`, sobre las filas de v2; escalado lineal al tamaño real, exacto si el relleno fue completo)
STATUS mezclaba dos celdas: «A n=16 +0,99» es **r0** (cota, 2 €); «+0,393 con 5 acc, ≈0 sin 2 mejores» es **r1500 (el arnés real)** con tamaño real. Todas son BTC cola base 79/60, 06-18 Oct (13 días, DESCUBRIMIENTO), EV ponderado por € (por unidad), IC90 por días, desenlace oficial:
| brazo A | tamaño | n | EV pond (unit) | IC90 días | sin 2 mejores (días rest.) | PnL |
|---|---|---|---|---|---|---|
| r0 (cota) | 2 € | 16 | +0,992 (+0,870) | (+0,33;+1,61) | +0,373 (6) | +43,74 |
| r0 | real+universo | 14 | +0,708 (+0,920) | (+0,28;+1,33) | +0,425 (5) | +16,67 |
| r150 | 2 € | 15 | +0,908 (+0,860) | (+0,33;+1,40) | +0,406 (6) | +37,97 |
| **r150** | **real** | **15** | **+0,671 (+0,860)** | (+0,29;+1,12) | **+0,439 (6)** | +18,16 |
| r1500 | 2 € | 10 | +0,595 (+0,591) | (−0,13;+0,98) | −0,035 (3) | +16,34 |
| **r1500** | **real** | **10** | **+0,393 (+0,591)** | (−0,05;+0,74) | **−0,001 (3)** | +7,10 |
B: r1500 real n=9 +0,440 (sin 2 mejores −0,168, 1 día); r150 real n=16 +0,673 (+0,495); r0 real+universo n=22 +0,663.
**Cifra de referencia: tamaño real + universo ejecutable (p 0,10-0,60, T>12 s), r150 vs r1500 → A +0,671 (n=15) vs +0,393 (n=10).** Los +0,99/+0,373 de v2 son 2 € y cota r0; ambas cuadran. El «≈0 sin 2 mejores» es r1500 con 3 días restantes (no robusto en ningún sentido); pesa por € menos porque los rellenos baratos (los más grandes a 2 €) dejan de dominar. Validación del código nuevo: v3 (2 €, acum) = v2 fila a fila el 13-Oct (60/60, 0 diferencias); 22 tests nuevos de sim/harness en verde.
## (2) OOS 19-20 Oct (BTC, `v3/h23_analisis_v3.py`; extracto nuevo en `v4_comprar_lo_bueno`, desenlace oficial 100 %: 1.701/1.669 controles con desenlace)
- Celda primaria (real, un relleno cierra la puja): **A r150 = r1500: n=1 (19-Oct, p 0,21, perdedor, −1,45 €)**; B r150 = r1500: n=1 (−1,66 €). 20-Oct: 0 rellenos A. Rellenos «recuperados» por r150 sobre r1500: **0**. Solo r0 (no ejecutable) añade 1 A perdedor y 2 B (1 ganador a 0,43).
- n, EV por € e IC90 por días: no estimables (2 días, 1 relleno). EV de esos 2 rellenos −0,99 (acierto 0/1): ruido, no refuta ni apoya. Etiqueta preregistrada: **INSUFICIENTE** (<5 días OOS o <5 recuperados; esperado ≈0,4-0,5 recuperados/día entre A y B).
- Hoy NO hay evidencia OOS de que re-pujar a 150 ms aporte algo; la evidencia sigue siendo 5-7 rellenos recuperados de 13 días ya vistos. Forward en `h23shadow` 20-21 Oct: 0 rellenos `join`/`join_r` (1 `nc`), 37 de 73 pares completos (cortes del WS).
## (3) Paquete v3 (nuevo, copia; todo en `experimentos/5m_barato/h23_maker/v3/`)
`h23_regla_v3.py` (hash 3eeff503cf0a75c9; regla v1 idéntica + `repuja_ms=150` + `acciones_real`) · `h23_sim_v3.py` (tamaño real, universo, «un relleno cierra», r0-r1500) · `paquete_real_v3/experimento_maker_h23_v3.py` (+104/−16 vs v1, `diff_harness_v1_v3.patch`; ledgers H23V3/H23V3B, OK propio; sha=498e612bf86d9fdc con h47=08e08d7a65ce10f7) · 97 tests (75 heredados + 22) · `PREREGISTRO.md` (hipótesis, celda primaria, gate n≥40/≥10 d/EV pond ≥+0,05/IC90 días>0/sin 2 mejores>0 + latencia real p50≤300 ms + cero doble exposición, kill, dinero real).
Seguridad de la re-puja: solo se libera a ≥150 ms de la decisión de cancelar si hubo lectura `get_order` terminal posterior, el WS del token emitió tras la decisión, sin relleno/kill; si no, espera 1,5 s como v1. Relleno tardío tras re-pujar = doble exposición → kill de brazo persistente. No ejecutado nunca (ni seco ni real): solo tests con cliente falso.
## Límites / riesgos
Descubrimiento y diferencial r150−r1500 ≈ 5-7 rellenos; multiplicidad 48 celdas; R1 (relleno visible ~1 s tarde), R2 (latencia real de re-puja, r300/r500 pierden casi todo), R3 (bid «fantasma» propio en el WS) NO medibles en replay. Ritmo A r150 ≈1,15 rellenos/día (n=40 ≈35 días si el real iguala el replay: improbable).
## Dinero real
NADA. Solo wallet dedicada 0x659a40…, tanda 5 $, suelo duro 12 pUSD, tras: ensayo en seco ≥1 día, /code-review del diff, H47-B terminado y OK de Javi ligado a sha/regla/kill en `H23V3_OK_JAVI.txt`. Lo decide la sesión principal con Javi.
## Reproducir
`bash v3/run_v3.sh` (guardas: fuera de 06:00-09:15Z, MemAvailable>1,8 GB, load5<20, ulimit 2,2 GB, nice 19/ionice 3) · `python3 -I v3/h23_analisis_v3.py` · `python3 -I v3/concilia_escalado.py` · tests: `pytest v3/test_h23_sim_v3.py` y `.venv/bin/python -m pytest v3/paquete_real_v3/test_experimento_maker_h23_v3.py`.
Pendiente para el validador estadístico/red team: re-simulación exacta de los 13 días DISC (en curso), OOS rodante al llegar más días de `m5/m15_registro`, y revisión del diff del harness.
