# L real, «bid sin nosotros», curva EV(l), dry-run B-CXB60 y brecha de nivel — 11-Nov-2026
Autor: cheap5m-execution-engineer. Encargo de Javi (11-Nov) vía chief. **0 órdenes enviadas, 0 firmas, nada tocado de procesos/crons/watchdog/ejecutores/dev existente, sin commit.** HOLD ≥ 10-Nov no usado para ajustar nada (TRAIN = 26-Oct..09-Nov, 15 días). Ninguna estrategia se etiqueta como rentable: todo lo de abajo es medición/diagnóstico.
Todos los ficheros nuevos están bajo `/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/` (`l_real_11nov/`, `dryrun/`, `PREREG_CXB60_FORWARD.md`); cachés pesadas en `/root/polymarket-research-datalogs/l_real_11nov/` (fuera de git).

## 1. l real (latencia decisión→envío→aceptación y cancelación efectiva), solo con datos EXISTENTES
Script `l_real_11nov/anclas_l_real.py` → `l_real_11nov/out/anclas_l_real.json`. Épocas de reloj: lenta (17-Oct 08:35Z..27-Oct ~11:50Z; suelo rx−ex ≈38-43 ms) y rápida (desde 27-Oct ~11:50Z; ≈16-18 ms); Rescale 4→8 vCPU el 22-Oct 09:58:31Z.
| tipo | fuente (periodo) | n | p10 / p50 / p90 (ms) | nota |
|---|---|---|---|---|
| RTT POST (alta) | Sonda1 real (30-Oct..04-Nov, época rápida) | 77 | 67 / 84 / 342 (IC90 p50 78-100) | cola larga (máx 1054) |
| RTT POST | B real post-Rescale (22-23 Oct) | 1.418 | p50 78 | |
| RTT POST | B real pre-Rescale (20-22 Oct) | 2.378 | p50 99 / p90 281 | |
| RTT cancelación (envío DELETE→respuesta) | Sonda1 | 44 | 56 / 61 / 142 (IC90 p50 60-62) | |
| RTT cancelación | B real post-Rescale | 1.409 | 56 / 64 / 116 | |
| RTT cancelación | B pre-Rescale | 2.328 | p50 66 / p90 140 | |
| RTT cancelación | T1 7-Oct (FOK/GTC de prueba) | 70 | 59 / 70 / 96 | otra época |
| decisión→envío (alta) | Sonda1 | 77 | p50 22 | en B ≈ 0 (solo registro) |
| **cancelación efectiva en el exchange (directa, canal de usuario)** | Sonda1 04-Nov (`cancel_evid`) | **4** | ex−envío 33 / 35 / 43 (mín 32, máx 46); ack−ex 22,5 | **n<30: faltan 26** |
| alta efectiva (directa) | Sonda1 04-Nov | 9 | ex−envío p50 79 (p10 51, p90 160) | n<30 |
| cancelación visible en el WS público | Sonda1 (candidatos únicos) | 17 | rx−envío p50 53 (IC90 52-55) | = efectiva + ~17 ms de feed |
| **efectiva derivada = RTT − 22,5 (ack−ex)** | pool Sonda ∪ B post-Rescale | **1.453** | **34 / 41 / 96** (Sonda p50 38 p90 119; B post p50 41 p90 94; T1 p50 47 p90 73) | usa el único `ack−ex` medido (n=4) |
| **carrera cancelación-vs-print (ancla natural)** | B real 20-23 Oct, `dryrun/carrera_cancel_vs_print.py` | **39** (30 con relleno real) | umbral δ = **40 ms** (IC90 por bootstrap 32–136), acierto de clasificación 0,87 | ver §5; sello de la cinta ±18 ms |
- **Conclusión l**: l efectivo (rx del disparo → cancelación efectiva) ≈ d_proc + 41 ms p50 / ≈ d_proc + 96-119 ms p90. **d_proc (disparo → envío del DELETE) NO está medido en ningún bucle de disparo**: el dry-run no lo mide (procesa con 2 s de retraso). El rango realista de l es **~45 ms (p50) a ~100 ms (p90)**, no 35 ni 150.
- **Faltan para n≥30 de cancelación efectiva directa: 26.** Protocolo mínimo propuesto, SIN ejecutar (decide Javi): GTC post-only BUY de 5 acc a 0,01 en mercados 5m vivos con el canal de usuario del registro de Sonda activo, cancelación tras 1-2,5 s con `ts_ex_ms`; ≤ 40 órdenes; nocional 0,05 $ por orden (tope acumulado 2 $ aunque nunca se casara nada; las de Sonda a 0,01 casaron ~30/77 a coste 0,05 $) y parada dura a 2 $ gastados o 3 rechazos seguidos. Mide a la vez ack−ex y ex−envío de alta/cancelación y la variación por época.
- Limitaciones: las anclas directas son 4 y 9; la efectiva derivada resta un único `ack−ex` (22,5) a toda la cola; no se separa red/proceso más que con ese resto (RTT − ack_ex ≈ parte de ida; la vuelta ≈ 22 ms).

## 2. «Bid sin nosotros» (regla causal) — `l_real_11nov/bid_sin_nosotros.py`, `out/bid_sin_nosotros.json`
Datos: B real 20-23 Oct (3.594 órdenes sin relleno, 3.423 usables) × filas q (ex, rx, bid, ask, szb, sza) de `m5_registro`.
- Con nuestra orden dentro, el mejor bid visible NUNCA baja de L: de 85.464 filas en la ventana cierta, solo 23 (0,03 %) tienen bid<L; la regla ingenua `bid_rx<L` no dispara con la orden dentro (recall ≈ 0 por construcción). En 0 de 11.584 filas con bid==L el tamaño szb es menor que nuestra cantidad: **nuestra orden está incluida en el feed público** (verificable con szb==5,0 = tamaño propio y bid==L cuando los otros se van).
- **Regla** (función pura `bid_otros(bid, szb, ex_ms, L, r, t_ack_ms, t_cancel_ms)`): si bid>L → otros=bid; si bid==L y la orden está «incluida» (`ex_msg > t_ack_loc+5 ms` y `ex_msg < t_cancel_send+30 ms`) → **bid_otros = szb − r** (≤0,011 ⇒ «otros por debajo de L» ⇒ disparar); si bid==L y no incluida ⇒ ambigua (no disparar con szb); bid<L con la orden incluida ⇒ inválido (fail-closed, no dispara). r = size − size_matched.
- **Validación sobre órdenes reales de B** (estado al cancelar): P(bid<L tras la salida | regla dice «otros<L») = **454/522 = 0,870**; con otros presentes (szb−r>0), tras la salida szb baja exactamente r en 288/652 (0,44; la primera fila posterior no siempre refleja ya la salida). En 776 de 3.423 órdenes (22,7 %) la orden estuvo sola en L en algún momento (4.368 filas): ahí el bid de OTROS ya era <L y la regla ingenua no lo veía.
- **Falta en el feed**: (i) canal de usuario para `r` exacto con parciales y para `t_ack` en tiempo de exchange (hoy se estima con RTT + 5 ms); validado solo con órdenes sin relleno (r=size); (ii) ventana ambigua entre envío y alta visible (p50 74 ms en Sonda) donde no se sabe si szb incluye la orden; (iii) 68/522 «dispara» con otros que reaparecen en 8-319 ms. En el dry-run no hay orden propia (libro limpio): el problema solo aparece al ejecutar de verdad.

## 3. Curva EV(l) de CXB-true con motor v3 (TRAIN 15 días, sin mirar HOLD)
Scripts `l_real_11nov/passT_cxb_l.py` (copia acotada de passT_cxb_v3; paridad EXACTA con el original verificada el 26-Oct para G0/GEO1/CXB60/100/150), `run_l_curva.sh`, `analiza_curva_l.py`; salida `out_l/curva_v3.txt/.json`, `out_l/curva_v3p.txt/.json`. EV = Σpnl/Σcoste (rebate 0,2 incluido). CXBEMP = l muestreado del pool empírico (n=1.453) + 3 ms (d_proc supuesto, no medido). v3p = mezcla pesimista de sellos (el 38 % de fallback −= p95 de d_ex de las firmas únicas, 38-67 ms según día).
| variante | v3: fills / EV / IC90 días / sin 2 mejores / días+ | v3p (sello pesimista): fills / EV / IC90 días / sin 2 mejores / días+ |
|---|---|---|
| G0 | 4.601 / −0,154 / (−0,261,−0,048) / −0,223 / 3/15 | 4.598 / −0,158 / (−0,266,−0,051) / −0,228 / 3/15 |
| GEO1 (control) | 4.346 / −0,146 / (−0,253,−0,036) / −0,213 / 3/15 | 4.343 / −0,150 / (−0,256,−0,041) / −0,218 / 3/15 |
| CXB35 | 785 / **+0,122** / (−0,040,+0,299) / −0,000 / 7/15 | 800 / +0,101 / (−0,074,+0,293) / −0,026 / 8/15 |
| CXB45 | 817 / +0,126 / (−0,020,+0,285) / +0,023 / 9/15 | 837 / +0,101 / (−0,063,+0,285) / −0,009 / 7/15 |
| **CXB60** | 882 / **+0,135** / (−0,003,+0,284) / +0,040 / 8/15 | 896 / +0,080 / (−0,066,+0,242) / −0,019 / 7/15 |
| CXB80 | 964 / +0,060 / (−0,067,+0,198) / −0,027 / 7/15 | 979 / +0,033 / (−0,115,+0,198) / −0,071 / 7/15 |
| CXB100 | 1.025 / +0,049 / (−0,106,+0,207) / −0,059 / 7/15 | 1.041 / +0,007 / (−0,155,+0,183) / −0,113 / 7/15 |
| CXB120 | 1.113 / +0,022 / (−0,120,+0,178) / −0,089 / 6/15 | 1.127 / −0,013 / (−0,170,+0,159) / −0,136 / 7/15 |
| CXB150 | 1.205 / −0,002 / (−0,156,+0,171) / −0,124 / 5/15 | 1.229 / −0,032 / (−0,186,+0,144) / −0,158 / 5/15 |
| **CXBEMP (l realista)** | 892 / **+0,117** / (−0,027,+0,279) / +0,016 / 11/15 | 906 / +0,096 / (−0,067,+0,274) / −0,011 / 8/15 |
- **Dosis-respuesta**: pendiente de EV por +40 ms de l = **−0,050** (IC90 por días −0,092,−0,007) con v3 y −0,052 (−0,088,−0,018) con v3p: cada 40 ms de retraso quita ~5 puntos de EV; el signo no se invierte con el sello pesimista, pero CXB100 ya está en ≈0 y CXB150 en ≈−0,02.
- **Incremental vs GEO1 (misma colocación, sin cancelar; Δpnl)**: CXB60 +552,9 € (13/15 días+, IC90 por día +17,9..+56,1); CXBEMP +543 €; CXB150 +471 € — la regla evita 460-550 € de pérdida del control en 12-13 de 15 días con cualquier l; **el EV positivo del agregado depende de pocos días** (IC90 por días e IC por cierre incluyen 0 en todas las variantes; sin 2 mejores días ≈0 con v3 y ≤0 con v3p).
- **Por moneda** (CXB60, EV): v3 ETH +0,051 (582 rellenos) / SOL +0,322 (191) / XRP +0,259 (109); v3p ETH **−0,002** / SOL +0,248 / XRP +0,215. CXBEMP v3: ETH +0,078, SOL +0,168, XRP +0,233. **ETH, el 66 % del coste, queda en ≈0 con el sello pesimista.** Por L (CXB60 v3): L=0,10 +0,22; 0,13 +0,05; 0,16 +0,29; 0,19 +0,01 (no monótono; descriptivo).
- Ramas del sello (TRAIN, 15 días): firma única 470.062, ambigua 194.360, sin firma 92.246, guardia 8.658 (≈38 % fallback, c_época ≈18-21 ms). Sin corrección de multiplicidad entre las K=8 variantes de l: EXPLORATORIO.
- No verificado aquí: sensibilidad a la cola (BASE fija), a SIZE/TMIN, y la correlación entre la señal de cancelación y la selección de días (11/15 días+ con CXBEMP).

## 4. Dry-run forward de B-CXB60 v1 (DRY_RUN; NO desplegado, NO lanzado)
**Qué existe** (todo en `dryrun/`, 0 envíos; el nucleo y el runner no importan py-clob-client/requests/web3 y un test lo comprueba):
- `cxb60_core.py`: máquina de estados INCREMENTAL de colocación/cancelación/re-armado equivalente a `run_var` + adaptadores de buffers vivos; **IMPORTA** del motor (`engine.gate_vec/vol30_vec/Tape` y constantes, `engine_v3.DayEngV3.run_segment/qupd3` → `fill_segment_v3` con dedupe, `capt.Day.book/prints`); no copia lógica de relleno. Decisiones con RX, relleno/cancelación con EX, `t_arr = t_dec+68`, cancelación efectiva = rx del disparo + l; variantes G0, GEO1, CXB{35,60,100,150} y placebo PLC60_s (20 semillas, igual cobertura).
- `cxb60_dryrun_fase0.py`: lector SOLO LECTURA de `maker_ms_<D>_<pid>.csv.gz` (filas k/q/t; zlib.decompressobj incremental; no usa `libro_estado_ws`, no abre WS, no toca el escritor del registro); manifiesto, latido, cobertura por día, log con marca temporal, `dec_<D>.csv.gz` (gz, anexado por mercado cerrado en un bloque; filas `seg` con ms ex/rx, motivo de fin, cantidad y sello del relleno; filas `nof` con motivos de no-colocación), retención `--retencion-dias 30`, fuera de git (datalogs/cxb60_dryrun/). Reinicio idempotente (se reconcilia con lo escrito; cola gz truncada se recorta). `--once --files` = replay offline; `--c-print` para el escenario de cinta pesimista.
- `cxb60_resolve.py`: une el desenlace OFICIAL (gmap del cron sa_r1) y regenera `res_<D>.csv.gz` (idempotente; relleno sin desenlace queda vacío y se cuenta; unicidad (tok,L,var,seg)).
- `replay_train.py` + `run_replay_cuando_libre.sh`: prueba de reproducción sobre un día TRAIN contra `out_v3/CX_v3dd_<D>.pkl` (ver abajo).
**Tests** (`python3 -I` en `dryrun/`; todos pasan):
- `test_cxb60_dryrun.py` T1-T6: **equivalencia EXACTA** de la máquina con el `run_var`/`cfn` ORIGINALES de `passT_cxb_v3.py` (extraídos por AST del fichero del motor, no copiados), 1.440 comparaciones, 3.052 segmentos, 1.470 cancelaciones, avance incremental con t_known aleatorio y buffer alimentado sin lookahead (una mutación l+1 se detecta en 8/10 casos: el test discrimina); causalidad (filas futuras basura no cambian lo decidido); TokBuf fuera de orden; placebo solo donde CXB60 dispararía; seguridad de dry-run (ninguna cadena de envío/credenciales); motivos == gate_vec.
- `test_runner_dryrun.py` R1-R7: lector gz incremental (miembros anexados y flujo con sync-flush), extremo a extremo con ficheros sintéticos, **idempotencia del reinicio** (el segundo arranque deja el fichero byte a byte igual), corrupción de cola gz, basura/duplicados contados, resolver (sin desenlace no inventa PnL; duplicar el bloque no duplica el PnL), microbench (primitiva de disparo 6-7 µs sobre 20k filas).
- `test_brecha.py`: calibración/corrección de la brecha (puras).
**Smoke real de lectura** (fichero vivo de hoy, scratch, sin mirar resultados económicos por ser HOLD): 8,8 M líneas en 16,7 s, RSS máximo 557 MB, 238/246 mercados procesados (6 `incompleto_arranque`, 2 `sin_token_15m`), 1 línea inválida, 0 duplicados, claves (tok,L,var,seg) únicas, ~2,5 MB gz/día estimados.
**Prueba de reproducción TRAIN** (`replay_train.py`): modo A (features y relleno del motor inyectados: la máquina debe reproducir EXACTO n_seg/n_canc/n_fill/pnl y cada relleno de G0/GEO1/CXB60/100/150) y modo B (ruta viva: features TokenFeats + relleno MiniDay con cinta WS). **Estado: NO ejecutada con resultado** — el preámbulo del motor necesita ~3-3,5 GB y la memoria libre del VPS fluctúa entre 1,1 y 4,6 GB (shadow_postmortem ~2,9 GB); por seguridad del `guard_ram` (reinicia observadores <900 MB) el lanzador `run_replay_cuando_libre.sh 2026-10-27` solo arranca con ≥5.000 MB libres y se mata a sí mismo por pid si baja de 1.600 MB. Lo que sí está demostrado es la equivalencia de la máquina con el `run_var` original (T1); lo que falta demostrar es la integración features+relleno con datos reales (la tolerancia exacta del modo A es 0 diferencias; el modo B REPORTA diferencia respecto del motor, no la exige).
**Plan de despliegue (no ejecutado; lo decide el chief)**:
1. Revisión de `data-integrity-authority` (script, tests, hashes) y congelación del prereg por el validador ANTES de desplegar.
2. Screen `cxb60dry`: `screen -dmS cxb60dry bash -c 'cd /root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/dryrun && ulimit -v 2500000 && exec nice -n 15 ionice -c3 /root/polymarket-research/.venv/bin/python -I cxb60_dryrun_fase0.py >> /root/polymarket-research-datalogs/cxb60_dryrun/stdout.log 2>&1'` (sin `choom -500`: no hay dinero). Registrar en `pipeline_watchdog.py` (`SCREEN_RESTART` + `check_screens()`) y `verify_deploy.py::SCREENS` (lo hace la sesión principal); si cae, se reinicia solo y reconcilia.
3. Recursos: RAM medida 557 MB pico (releyendo 2,2 h de registro), estimada <300 MB en régimen; CPU: `cpu_advance_us` p50 3,3 ms / p99 60 ms por ciclo, el lector duerme 0,5 s; disco ~2,5 MB/día gz × 30 días ≈ 75 MB (retención 30 d, fuera de git). Un reinicio relee el fichero del día desde el principio (~1-2 min de CPU).
4. Resolución: cron diario (p. ej. 10:50Z, tras `sa_r1` 10:40Z) `cxb60_resolve.py D-1`. Informe del prereg (EV por variante, IC90 por días/cierre, placebo, sin 2 mejores días, incremental vs GEO1) = tarea del validador sobre `res_<D>.csv.gz`; NO está construido.
5. No importa módulos de la cadena de `observadores_fase0`, así que no provoca reinicios; sí lee `engine.py/capt.py` del worktree dev permanente (hashes en el manifiesto).
**Borrador `PREREG_CXB60_FORWARD.md` (NO congelado)**: hipótesis única H-CXB60-FWD, puertas G1-G8 (n≥40, ≥10 días independientes, IC90 por días y por cierre >0, incremental vs GEO1, sin 2 mejores días, placebo p≤0,05 con ≥20 semillas, concentración, sensibilidad a la cinta y a l), exclusiones sin rellenar con ceros, congelación antes de leer forward, HOLD ≥10-Nov, debilidades declaradas.
**Limitaciones del dry-run**: la cinta WS usa sello `ex−19−1` (supuesto; el TRAIN tiene 61 % de firma exacta); no mide d_proc real; relleno por toque y cola BASE sin validar con órdenes reales; no hay forma de validar el relleno virtual sin órdenes reales.

## 5. Brecha de nivel EV motor (−0,222) vs real (−0,061) en verif_v3 — `dryrun/brecha_nivel_v3.py`, `out_replay/brecha_nivel_v3.json`
3.796 órdenes reales de B (20-23 Oct), 70 TP / 12 FP / 132 FN (clases por orden). EV = Σpnl/Σcoste con el rebate.
| clase | n | coste real | EV real (IC90 por clúster) | EV sim |
|---|---|---|---|---|
| TP (sim y real) | 70 | 82,8 € | −0,108 (−0,47,+0,30) | −0,106 |
| FP (solo sim) | 12 | 0 (sim 12,0) | — | **−0,989** (los 12 pierden) |
| FN (solo real) | 132 | 138,5 € | −0,034 (−0,36,+0,31) | — |
Descomposición escalonada: sim todos −0,2217 → **quitar los 12 FP −0,1055 (+0,116; IC90 del paso +0,053,+0,195 por clúster)** → cantidad real en las TP −0,1078 (−0,002) → añadir FN **−0,0615 real** (+0,046). Brecha 0,160: **72 % = 12 rellenos fantasma, 29 % cierra FN** (los pasos suman 100 %; la cantidad real no aporta). Conclusión: **en los rellenos que el motor SÍ ve, reproduce el EV real (−0,106 vs −0,108, n=70)**; el nivel falla por (a) 12 falsos positivos (todos perdedores) y (b) FN que el motor no ve.
- **Causa de los FP**: 9 de 12 tienen su primer print sim a −100..+85 ms de `t_fin` (= envío del DELETE + 30 ms): son **la carrera de cancelación** — `verif_v3` simula hasta `t_fuera` (retorno del DELETE, ≈ envío + RTT 60-70 ms) pero la orden real ya no existía en el exchange desde ≈ envío + 40 ms (δ medido en §1). Esto es a la vez un ancla independiente de l: con 39 órdenes (30 rellenos reales), umbral δ = 40 ms.
- **Corrección propuesta (código NUEVO, sin tocar el motor)**: fin de segmento = envío DELETE + δ (anula el relleno simulado si tf > t_envío+δ). Resultado (en muestra, δ estimado con las MISMAS órdenes: circular): δ=30 → 63 rellenos, precisión 0,937, cierra 89 % de la brecha; **δ=40 → 67 rellenos, precisión 0,910, recall 0,302, EV sim −0,107 (cierra 72 %)**; δ=47 → cierra 72 %; δ=60 → 50 %. Coste: baja el recall de 0,347 a 0,302 (anula también 9 TP). No validada fuera de muestra.
- **FN**: 94 (71 %) son tx de un solo maker = nuestra propia orden (sin print ajeno en el feed; EV real −0,186, coste 103 €) y 38 con otros makers (EV real +0,415, coste 35 €, fallos genuinos de cola/tiempo del motor). En la cinta de validación se excluyen NUESTROS propios prints, así que el recall bajo es en parte artefacto de la validación contra órdenes reales; en el dry-run/TRAIN la cinta es limpia (no hay órdenes propias). Un modelo «composición» (calibra_composicion: EV̂ = (EV_sim + ρ·EV_FN)/(1+ρ)) en validación cruzada por día (LODO, 4 días) reduce el error absoluto medio de 0,230 a 0,157 (cierra el 32 %), en muestra 75 % (circular). **No se debe multiplicar el EV del dry-run por ningún factor: la brecha depende del diseño de la validación**, y con 4 días (4 observaciones) y 129 clústeres ninguna cifra de nivel es fiable (IC90 real (−0,315,+0,207)).
- No verificado: tamaño de orden y fee/rebate por orden real (el rebate se asume 0,2 en ambos lados); el efecto de `size`>5 en 12 órdenes; qué parte de los FN con otros makers es cola vs tiempo.

## 6. No verificado / límites (resumen)
d_proc real; 26 anclas directas de cancelación; `ack−ex` único para toda la cola; regla «bid sin nosotros» con parciales y ventana ambigua (necesita canal de usuario); cinta WS sin firma exacta; replay TRAIN con datos reales no ejecutado por memoria; δ=40 estimado y evaluado con las mismas órdenes; curva EV(l) exploratoria (K=8, IC90 incluyen 0, depende de pocos días, ETH ≈0 con sello pesimista); placebo y control GEO1 solo en el dry-run (en la curva l no hay placebo); EV del dry-run = índice, no euros.

## 7. Reproducción (todo solo lectura, nice/ionice, ulimit ≤3,7 GB, nunca 06-09Z)
```
cd /root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov
python3 -I l_real_11nov/anclas_l_real.py ; python3 -I l_real_11nov/bid_sin_nosotros.py
cd l_real_11nov && ./run_l_curva.sh v3 && ./run_l_curva.sh v3p && python3 -I analiza_curva_l.py v3 v3p   # log out_l/run_l.log
cd ../dryrun && python3 -I test_cxb60_dryrun.py && python3 -I test_runner_dryrun.py && python3 -I test_brecha.py
python3 -I brecha_nivel_v3.py ; python3 -I carrera_cancel_vs_print.py
./run_replay_cuando_libre.sh 2026-10-27   # prueba de reproducción TRAIN (espera memoria; out_replay/replay_2026-10-27.log/.json)
python3 -I cxb60_dryrun_fase0.py --out /tmp/x/ --once --files <maker_ms_D_pid.csv.gz>   # replay offline del runner; cxb60_resolve.py D --out /tmp/x/
```
## 8. Siguientes especialistas
1. `data-integrity-authority`: auditar script + tests + hashes ANTES de desplegar (cobertura, claves únicas, cinta WS, reinicio, desenlace).
2. Validador estadístico: revisar y congelar `PREREG_CXB60_FORWARD.md` (puertas, placebo, multiplicidad, l de referencia), escribir el informe sobre `res_<D>.csv.gz`; valorar la corrección δ de la brecha y la curva de l.
3. `execution-engineer` en shadow (sin envío) + chief/Javi: despliegue de `cxb60dry` (watchdog/verify_deploy) y decisión sobre el protocolo mínimo de anclas de cancelación (≤40 órdenes a 0,01, tope 2 $).
4. Red team: sesgo de la validación contra órdenes propias (FN solo-nuestra), selección de días en la curva de l, ETH con sello pesimista.
