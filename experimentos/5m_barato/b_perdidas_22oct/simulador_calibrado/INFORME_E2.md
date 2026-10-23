# E2 — Simulador de B a nivel de ORDEN con el decidir() REAL (mock). 23-Oct-2026. EXPLORATORY, solo lectura (B, ejecutores, main intactos)
Prereg congelado ANTES de correr: `prereg/PREREG_E2_ORDEN_DECIDIR.md` (sha256 86ffe92c…, `sha256sum -c prereg/PREREG_E2_ORDEN_DECIDIR.sha256`). Visto antes y declarado: INFORME E1 y estadísticos descriptivos de `ordenes_b.json` y del ledger.

## Veredicto: **NO_REPRODUCE** (en EVAL, celda elegida en TUNE; falla O1-O4, B1-B5; solo B0 pasa)
Mejora real respecto a E1 en la dinámica de órdenes, pero ni el acuerdo puja a puja (κ 0,40), ni el hazard, ni las clases, ni el EV por moneda se reproducen. No sirve para medir palancas de ±0,05-0,10 €/€.

## Qué se hizo (los 3 pasos)
1. **Ancla a nivel de orden** (3.272 órdenes de `ordenes_b.json`): latencias fijadas desde los datos, no ajustadas (LAT_POST 0,085 s, LAT_CAN 0,055 s). Hallazgo nuevo e importante: **B real está limitado por el presupuesto de la wallet dedicada**: 718 eventos `bloqueo_suelo_saldo`, 158 de 305 pujas con ≥1 bloqueo dentro de su ventana (saldo−mínimo p50 1,36 $ en los bloqueos: cabe ~1 orden). E1 simulaba cada mercado con presupuesto infinito.
2. **decidir() real en mock** (`scripts/e2_engine.py`): `Exp47.decidir()` de `/root/polymarket-research-dev/experimento_maker_h47.py` (sha c82f5dc5f304b8a6 = `codigo_sha` de la última config de B), SIN editar; subclase que solo sustituye post/cancelar/presupuesto/log, reloj virtual, `X.leer_ledger`→[]; no crea cliente, no firma, no lee .env, no escribe ledgers (comprobado: sha del .py intacto). Simulación conjunta ETH+SOL+XRP por cierre con presupuesto compartido (`puede_enviar` = H(t) − comprometido − coste ≥ 0, H(t) = última observación real del ledger). Relleno = `e1q_sim.vida_orden` sin modificar.
3. **Clases X/C unificadas** (`scripts/e2_clases.py`): C1 = print más hondo a ≤25 ms del print de relleno, C2 = en (25 ms, 2 s], C3 = resto, aplicado a prints L2. Validado contra la clase on-chain `cl_h1_0.005` en 147 rellenos reales de B localizados en L2: **exactitud 0,82** (5 ms 0,82; 100 ms 0,78); cuotas on-chain C1/C2/C3 0,20/0,29/0,51 vs proxy 0,17/0,27/0,56. El proxy es válido; por tanto la diferencia de clases del sim es REAL, no de definición.

## TUNE (20-Oct, 33 pujas completas) — rejilla cerrada 3 cadencias × 2 δ_obs (`datos/e2_tune_eval.txt`)
| cadencia / δ_obs | órd/puja sim (real 8,7) | vida mediana (real 0,96 s) | hazard/orden (real 0,084) | L |
|---|---|---|---|---|
| 0,10 / 0 | 16,0 | 0,37 | 0,019 | 3,06 |
| 0,25 / 0 | 14,2 | 0,47 | 0,028 | 2,32 |
| 0,50 / 0 | 11,6 | 0,97 | 0,049 | 0,81 |
| **0,50 / 100 ms (elegida)** | 11,4 | 0,97 | 0,051 | **0,78** |
La elegida está en el BORDE de la rejilla (cadencia más lenta); el bucle real de B es más lento que los 0,1 s nominales (llamadas HTTP bloqueantes). No se amplió la rejilla (prereg cerrado); queda como siguiente paso.

## EVAL (21-22-Oct, 246 pujas reales; sim abre 207; 198 completas con mismo lado) — `datos/e2_eval_resultados.txt`
| Criterio | Umbral | base (prop) | cota cola conservadora (lo) | optimista (hi) | sin presupuesto (inf, diagnóstico) |
|---|---|---|---|---|---|
| B0 lado (sobre las que el sim abre) | ≥0,90 | 0,971 PASA | 0,971 | 0,971 | 0,953 |
| O1 órd/puja y Spearman | [0,85-1,15] y ≥0,60 | 14,2 vs 10,7 (1,34×), ρ 0,48 FALLA | 16,1 vs 10,7, ρ 0,39 | 14,1, ρ 0,48 | 16,3, ρ 0,43 |
| O2 vida orden | razón ≤1,25 y KS ≤0,15 | mediana 0,47 vs 0,66 s, KS 0,38 FALLA | igual | igual | igual |
| O3 hazard/orden | [0,80-1,25] | 0,035 vs 0,056 (0,62×) FALLA | 0,025 | 0,036 | 0,036 vs 0,056 |
| O4 1.ª orden | precio ≥0,85 y t≤1 s ≥0,70 | 0,39 y 0,48 FALLA | 0,39 / 0,48 | 0,39 / 0,48 | 0,32 / 0,38 |
| B1 tasa de relleno | \|Δ\|≤0,05 | 0,502 vs 0,592 (Δ−0,090, IC90 −0,149,−0,030) FALLA | 0,395 (Δ−0,20) | 0,512 (Δ−0,08) | 0,589 vs 0,584 (Δ+0,005) PASA |
| B2 acuerdo | acc≥0,80, κ≥0,60 | acc 0,701, κ 0,402 (IC90 0,29-0,50), recall 0,67, prec 0,79 FALLA | κ 0,21 | κ 0,40 | acc 0,708, κ 0,398 |
| B3 edad al relleno | KS≤0,15, \|Δmed\|≤0,5, pares ≤1 s ≥0,70 | KS 0,085, Δmed 0,38 s PASAN; pares a ≤1 s **0,64** FALLA | 0,44 | 0,63 | 0,53 |
| B4 EV y cuotas | \|ΔEV\|≤0,10, cuotas ≤0,10 | EV sim −0,008 vs real −0,092 (Δ+0,084, IC90 −0,18,+0,35) pasa; cuotas C1/C2/C3 sim 0,40/0,22/0,39 vs on-chain 0,21/0,30/0,50 (\|d\| 0,19/0,08/0,11) FALLA | cuotas 0,56/0,14/0,30 | 0,35/0,23/0,42 | 0,50/0,18/0,32 |
| B5 EV por moneda | signo y \|Δ\|≤0,30 | ETH sim +0,13 vs real −0,17; SOL −0,23 vs −0,00; XRP +0,02 vs −0,10 → 0/3 | 2/3 (ETH sigue invertido, ΔEV +0,39) | 0/3 | 1/3 (ETH +0,05 vs −0,14; SOL −0,35 vs 0,00) |
**El signo de ETH sigue invertido en TODAS las variantes** (sim ≥0, real −0,14/−0,17); SOL y XRP cambian de signo según la cota de cola. Rellenos que el sim inventa (solo sim) tienen EV +0,27/+0,52 (optimistas) y los que pierde (solo real) −0,06/−0,04 (neutros): el sim da rellenos buenos que el real no tiene. IC90 de ΔEV por moneda contienen 0 (n≈67 por moneda): sin potencia para afirmar ni negar, pero B5 es criterio de punto estimado y falla.

## Qué explica (diagnóstico, descriptivo — `datos/e2_cola.txt`, `e2_clases_validacion.txt`)
- **El libro y la cola a la entrada SÍ se reproducen**: 952 pares de órdenes (mismo slug, mismo precio, |Δt_dec|≤1 s): cola delante mediana 38,0 real vs 38,0 sim, 79 % a ≤2 acciones. Los volúmenes L2 ya cuadraban en E1 (W2 0,995). El fallo NO está en el replay del libro al postear.
- **El fallo está en el proceso de relleno**: el sim rellena 0,62× por orden y, cuando rellena, es «barrido» (C1 40 % vs 17 % proxy en reales / 21 % on-chain) en vez de cola (C3 39 % vs 51-56 %). Los rellenos reales son más de cola y más frecuentes: sospecha (no probada) en cómo `vida_orden` consume la cola delante (eventos «explicados» por prints y asignación `alloc`; las cotas lo/hi mueven κ 0,21-0,40 pero no cierran la brecha) y en el sesgo conservador de D1 (un print a q<puja consume delante antes de rellenarnos).
- **La dinámica de órdenes mejora mucho con el código real + presupuesto + cadencia lenta** (órd/puja 14,2 vs 20,9 de E1; hazard 0,62× vs 0,52×; vida KS 0,25 en TUNE, 0,38 en EVAL), pero la primera orden de la puja aún no coincide (39 % mismo precio): sim y real discrepan en cuándo/qué ven en los primeros segundos (reloj libro5 ≠ WS del bot, asks sintéticos = 1 − bid opuesto).
- **El presupuesto importa**: quitarlo sube la tasa de relleno 0,50→0,59 y cambia el EV por moneda (cota de la sensibilidad); H(t) solo se observa en los bloqueos, así que es una cota gruesa.
- La tasa agregada (B1) pasa en `inf` y falló en E1/E2 base: acertar el agregado depende de qué parámetro se relaje (sigue siendo compensación de errores).

## Qué reglas de ±0,05-0,10 €/€ se pueden probar ya
**Ninguna con este simulador.** El criterio del prereg exige REPRODUCE o que el efecto supere el error medido de B5 (±0,30 por moneda, ETH invertido). Lo que SÍ se puede probar sin simulador, de forma real y barata: (a) levantar el cuello de botella de presupuesto (158/305 pujas con bloqueo) en un test A/B real de pocas decenas de pujas, porque limita órdenes simultáneas entre monedas; (b) NO usar el sim para decidir sobre ETH.

## Siguiente paso (por orden)
1. Anclar el relleno a nivel de ORDEN con las 186 órdenes reales rellenadas: para cada una, ¿qué print la rellenó y qué predecía el sim en ESA orden (misma cola, mismo t_dec)? Eso aísla `vida_orden`/D1/alloc del resto (el pareado de 952 órdenes ya demuestra que la cola coincide).
2. Ampliar la rejilla de cadencia (0,75-1,5 s; el óptimo está en el borde) y estimar la cadencia real con `cancel_lat`/`repega` del ledger. 3. Primera orden: medir el desfase entre el reloj de libro5 y el del bot con las propias órdenes de B como anclas.

## Límites
Sin más días de B (el ledger acaba el 22-Oct 15:48Z). EVAL ≈ 198 pujas completas (de 246 reales; el sim abre 207, 201 con el mismo lado): SE de EV ≈ 0,12; las 39 reales sin puja simulada mezclan huecos de datos/fuera de MEDIR (no separados en la salida) con no-apertura del sim. Rejilla de 6 celdas elegida con 33 pujas (ruido; la elegida está en el borde). Asks sintéticos. Libro5 incluye las órdenes reales de B (inflan la cola a su propio nivel). Presupuesto H(t) a trozos. Tiempo de relleno real = recepción WS. Se corrió con nice 19/ionice 3/ulimit 3 GB, un proceso, ≈10 s por tanda, durante 06:10-06:16Z (ventana 06-09Z, tandas mínimas).

## Reproducir
`cd experimentos/5m_barato/b_perdidas_22oct/simulador_calibrado/scripts && ulimit -v 3000000; nice -n 19 ionice -c3 python3 -B e2_run.py 2026-10-20 rej tune base && python3 -B e2_eval.py tune base && for v in base lo hi inf; do nice -n 19 ionice -c3 python3 -B e2_run.py 2026-10-21,2026-10-22 0.5:100 eval $v; done && python3 -B e2_eval.py eval base lo hi inf` · `e2_clases.py` · `e2_cola.py`. Salidas en `datos/e2_*` (3,3 MB, hashes en `datos/HASHES_E2.txt`, manifiestos `e2_*_manifest.json`). Handoff: statistical-validator (S1: usar O1-O4/B5 como línea base; el proxy de clases queda validado a 0,82) y red-team (el «EV agregado ≈» sigue siendo compensación; el signo de ETH invertido es el contraejemplo más claro).
