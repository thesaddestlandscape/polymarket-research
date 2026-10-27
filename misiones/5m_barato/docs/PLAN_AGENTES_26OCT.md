# Plan ordenado de agentes B — 26-Oct (Javi: organizados, sin gastar toda la cuota de la sesión)

## Estado de partida (verificado 26-Oct 07:40Z)
- Datos crudos 24-25 Oct NO en riesgo: maker_ms y onchain_fills rotan a /mnt/HC_Volume_106538179/datalogs_auto/ (symlink, 03:20Z). Falta nada que extraer a mano.
- Carga VPS: load5 ~6,4 con 2 núcleos (racimo de crons 06-09Z + shadow_predict). Regla: ningún agente pesado (CPU) antes de 09:30Z ni con load5>4.
- API: límite semanal resetea hoy 13:00Z. Hasta entonces, ningún agente con tokens. Los IDs viejos no son resumibles: relanzar desde la carpeta de cada informe.
- Validado en € para B: 0. Hueco al objetivo ≈193,7 k€/año.

## Reglas de gasto
1. Máx. 2 agentes con tokens a la vez; el 2º solo si es CPU/runner. Tope ~120 k tokens y 45 min por agente; Sonnet por defecto, Opus solo red-team/diseño con riesgo de falso positivo (~80 k).
2. Respuesta final ≤5 líneas; detalle a INFORME.md. El chief NO lee informes largos.
3. El siguiente arranca solo al entregar el anterior. Todo veredicto lo reverifica otro agente con datos crudos.
4. Nada a dinero real sin diseño + /code-review + OK Javi; sin recarga de B.

## Cola (en orden; cada línea = 1 agente)
| # | Tarea | Agente | Cuándo | Por qué suma a los 200 k |
|---|---|---|---|---|
| 1 | Calibrar etiqueta virtual vs rellenos reales de B (P(fill) 51 % virtual vs 5,1 % real) | execution-engineer (sonnet) | 13:00Z | Prerrequisito de TODA política de B: sin esto F8, huérfana, mitigar_as miden pérdida evitada irreal |
| 2 | Red-team de mitigar_as (rasgo «tamaño en ask 100 ms») y de F8 | red-team-auditor (opus) | tras #1 | Evita construir sobre un confusor (ETH/hora) |
| 3 | R0/R2 forward 10 días: leer L1/L1b/P-REAL ya en cron | sin agente (script) | ~02-03 Nov | R0 es el único con placebo p=0,000 y 16/17 días (Δ −0,234 al saltar el lado CON) |
| 4 | Forward pasivo A1 + réplica BTC/DOGE/BNB (cron solo lectura) | execution-engineer | tras OK Javi del cron | Gate ~04-Nov; vale ~0,7 k€/año solo con cancelación ≤100 ms |
| 5 | R8 con control emparejado por banda (libro ms) | statistical-validator | tras #1 | Única pista viva de flujo no informado |
| 6 | Libro de cuentas de la suma | objetivo-200k | semanal | Contabilidad honesta del hueco |
Pausadas: réplica pspspsps5 (sin mecanismo, relanzar solo con requisito cuantificable), re-sim 19-21 Oct (solo con load5<4 y >6 GB libres), limpiar F_2026-10-17/18/19.pkl.

## Hallazgos de B que ahorran o ganan dinero (todo sin validar en €)
AHORRAN (evitan pérdida; B real EV −0,03..−0,07 €/€, forward real ≈ −40 $/10 días):
- No recargar B hasta mitigar AS: evita el sangrado (AS −18..−33 pp en rellenos; es general del maker, B no es peor que la población).
- R0 (saltar el lado a favor de la tendencia, |rpre|≥7,7 bps): Δ −0,234 al ask real; candidata nº1, gate forward ~02-03 Nov.
- Cancelar al barrido: EV −0,010 vs −0,056 (Δ +0,040, IC cruza 0, 1/3 días).
- Saltar pujas ≥0,25 (skip025, cron 10:50): espejismo parcial, forward en curso.
- F8 (estructura): pierde menos, pero retenidas siguen −0,08..−0,10 → pérdida evitada, no ganancia.
GANAN (todas pequeñas):
- Recotización de makers rápidos (≤100 ms): ~0,7 k€/año.
- Rebate maker 20 %: umbral ≈1 €/día, +0,011 €/€ solo con ≥90 €/día de volumen.
- Nichos: 15m ETH [0,90-0,95) +0,031 (≈0 con cola) y 5m BNB [0,30-0,35) +0,118 (tamaño ínfimo).
- Flujo no informado: B recibe 9,9 % vs 26,2 % esperado; mantener la puja 3-12 s, cota optimista ~0,8 k€/año.
REFUTADAS (no reabrir): F7 precio del par, cosechar al abrir v3, fav 60m, F3 carry, PSA, huérfana ex-ante, E1 BN_W300, ganadoras persistentes (roster vacío), contrapunto informado.
SUMA honesta: 0-40 k€/año sin validar frente a 200 k€ → B sola no llega; el objetivo exige sumar subestrategias (tomador/otras 5m barato) tras masterizar B.

## Añadido 26-Oct
- Agente `cheap5m-reverse-engineer` (docs/reverse-engineering/): piloto RE-AS-B en curso. Forward A1 + R1 (E1D) en construcción (cron propuesto, sin instalar). Recarga de B condicionada a gate (PLAN_RECARGA_NOV_B.md).

## Objetivo fijado por Javi 26-Oct
200.000 €/año limpios de B (masterizar B → ponerla en marcha); después cada subestrategia de 5m barato igual. Caso RE-B-REFORMULACION en curso (modelo B→200 k€ por palancas). Sin recarga hasta el gate.
- RT cementerio 26-Oct: casos/RT_CEMENTERIO_26OCT.md (F3 agregado → INCONCLUSA, 15m ETH [0,90-0,95) REABRIBLE; cosechar v3 y fav60 confirmados).
- Programa BANDA-0-0,30 (Alpha Miner, 26-Oct): incluye la herramienta de RÉGIMEN alcista/bajista como conmutador de política (REGIMEN_PLAN.md en alpha_miner/banda_0_30/); antecedentes: detector_regimen (D-FUERTE nulo, R0 viva), detector_ex_ante, L1/L1b forward.
- V4 verificado con registro ms (alpha_miner/V4_ONCHAIN.md): 33/40 confirmables a Δ+100 ms, EV +0,113 IC90 por cierre −0,39..+0,71; sin mejor día −0,083; G1 no se cumple (39<40); 22-Oct sin procesar. V4 → EXPLORATORY.

## Gestión de consumo 26-Oct ~11:00Z (Javi: «escalonado y por prioridad»)
Máx. 3 agentes con tokens a la vez. P1 mecanismos de pspspsps5/mo-money (`a8e0159241e44bf1c`); P2 censo de ganadoras RE (`ad03925e4db29131a`); P3 programa banda 0-0,30 + régimen, Alpha Miner (`a440ebb78dd3c1b43`). PAUSADOS (estado en disco, reanudar con SendMessage al entregar uno de P1-P3, en este orden): calibración etiqueta virtual `a6c90bc93fd2a10eb` (bug acc_llena + verdad on-chain), wrapper forward A1+R1 `a1e2884936f3b1f6d` (cron propuesto sin instalar), R8 `af2395aecadc9424a`, contrato de datos hecho. Cola siguiente: M2/M1 (ingeniero + validador), arreglo lector zlib del crudo 22-Oct, red-team de lo que salga de P1/P2. Cada entrega ≤8 líneas; yo filtro.

## Forward A1+R1: wrapper construido (26-Oct ~11:30Z), cron NO instalado hasta validar
Código en experimentos/5m_barato/b_perdidas_22oct/mitigar_as_25oct/{forward,forward_r1}/. Pendiente (chief): cuando val23.out tenga línea 'fin', `python3 -I <scratchpad>/cmp23.py`; si coincide con r_2026-10-23.pkl / e1d_dia_2026-10-23.pkl → `sha256sum` de los PREREG_FWD*.md (bloquear) → instalar cron `10 11,15,19,23 * * * flock -n /tmp/fwd_a1_r1.lock bash .../forward/forward_cron.sh` (backup crontab antes) → procesar 24 y 25-Oct. Datos fuente archivados 60 d: no se pierde nada por esperar. Gates ≈03-Nov (R1) y ≈04-Nov (A1).

## ESCALONADO 26-Oct ~11:40Z (Javi: «trabajo optimizado y escalonado»)
Activos (máx. 3): P1 mecanismos pspspsps5/mo-money `a8e0159241e44bf1c`; P2 censo ganadoras `ad03925e4db29131a`; P3 calibración etiqueta virtual `a6c90bc93fd2a10eb`.
En espera (estado en disco; reanudar con SendMessage cuando entregue uno activo, en este orden): P4 Alpha Miner banda 0-0,30 + régimen `a440ebb78dd3c1b43` (se alimenta de P1/P2, no tiene sentido antes); P5 R8 `af2395aecadc9424a`. Entregados/sin tokens: wrapper A1+R1 `a1e2884936f3b1f6d` (falta validar val23 + instalar cron), contrato de datos, V4 on-chain, red-team cementerio, validación independiente.
Cola tras P1-P3: M1/M2 (ingeniero de código + validador, prereg en alpha_miner/), lector tolerante a zlib del crudo 22-Oct, red-team de lo que salga de P1/P2, libro de suma (objetivo-200k).

## Regla de carga actualizada 26-Oct 13:05Z (Javi AUTORIZA): VPS = 8 núcleos (tras Rescale) → análisis pesados con load5 < 8 (antes <4, valor de la época de 2 núcleos), nice -n 19, ionice -c3, ulimit -v 3000000, 1-2 procesos, MemAvailable>2,5 GB, fuera de 06-09:30Z, solo lectura. Regla raíz: sobresuscripción = load5/nproc > 3 sostenido. Nunca tocar procesos con dinero real.

## 26-Oct ~13:30Z — Javi: TODO el equipo parte de CARRY-FAV-5M (maker paciente en favoritos ≥0,70) para sacar una estrategia OPERABLE
Activos: P1 wallets `a8e0159241e44bf1c` (H2-H4 + especificación operable a nuestra escala), P2 censo `ad03925e4db29131a` (wallets maker persistentes ≥0,70 y capacidad), P3 calibración `a6c90bc93fd2a10eb` (+ transferibilidad B→favoritos), P4 Alpha Miner `a440ebb78dd3c1b43` (top-5 con CARRY-FAV-5M primero). Javi cree que la simulación de trades de B ya da la cola real: válido para banda 0,05-0,40; para ≥0,70 es supuesto hasta medir (F5 micro-órdenes: OK Javi + /code-review + wallet dedicada, solo tras simulación positiva).

## AGENDA B (Javi 26-Oct ~13:45Z: «mover la aguja de B hacia el máximo dinero posible»; del pool de wallets alguna juega y gana en el rango de B)
Estado B: EV −0,072 (n=202 on-chain, IC90 por cierre −0,31..+0,20); AS como brecha = identidad; descomposición SPREAD +0,106 / SEL +0,048 / COND −0,227 (residuo, depende del 22-Oct). Frentes vivos, en orden:
1. Censo B-RANGO (P2 `ad03925e…`): wallets ganadoras en 0,05-0,40 maker, qué hacen distinto de B → variante concreta. 
2. Calibración [pes,opt] (P3 `a6c90bc9…`): desbloquea F8, A1, R3, H23, F3 con la verdad on-chain.
3. Forward pasivo R0/R2 (L1/L1b, ~02-03 Nov), R1 reparado y A1 (wrapper hecho; cron tras validar val23; gates ~03-04 Nov), skip025 (cron 10:50).
4. M1 CONTRA-PERDEDORA (prereg da120f36…; el maker que vende el lado barato a tomadoras perdedoras +0,034/€) y M2 COLCHÓN-PARIDAD (prereg 86291260…): ingeniero de código + validador, lecturas ~01-03 Nov. H3 (BTC <0,10 con MM presente).
5. Régimen como conmutador (Alpha Miner, REGIMEN_PLAN.md) + E03 (cancelar más rápido vs anticipar; prereg 85db9250…) + nivel agotado (E02).
6. CARRY-FAV-5M (P1/P4): estrategia operable en favoritos ≥0,70; B queda como estrategia tal cual con su máximo.
Reglas: ≤3-4 agentes con tokens; nada a real sin gate (EV>0 validado, red-team independiente, /code-review, OK Javi); recarga solo tras gate.

## ESCALONADO FIRME 26-Oct ~14:00Z (Javi: no consumir todos los tokens de la sesión)
Activos (3): P1 wallets `a8e0159241e44bf1c`, P2 censo B-rango+favoritos `ad03925e4db29131a`, P3 calibración `a6c90bc93fd2a10eb`. EN ESPERA: Alpha Miner `a440ebb78dd3c1b43` (reanudar al entregar P1 o P2: necesita sus resultados para priorizar), R8 `af2395aecadc9424a`. Cola: M1/M2, régimen, E02/E03, lector zlib, cron A1+R1 (tras val23). Regla: un agente nuevo/reanudado solo cuando entrega uno activo; yo leo ≤10 líneas por entrega.

## UN SOLO AGENTE A LA VEZ (Javi 26-Oct ~14:30Z; sesión con límite hasta 18:00Z)
Orden de turnos, uno cada vez, el siguiente solo al entregar el anterior: 1 calibración `a6c90bc93fd2a10eb` → 2 censo B-rango+favoritos `ad03925e4db29131a` → 3 wallets CARRY-FAV `a8e0159241e44bf1c` → 4 Alpha Miner `a440ebb78dd3c1b43` → 5 R8 `af2395aecadc9424a`. Cola: cron A1+R1 (tras val23), M1/M2, régimen/E02/E03, lector zlib. Tope ~150k tokens y ≤8 líneas por entrega.

## CHECKPOINT 26-Oct ~16:00Z (Javi: parar el agente en curso; primero resolver 4 frentes con TODO el equipo)
Censo B-rango/favoritos (afe1e21324ba734d0) PARADO por Javi sin entregar. Calibración entregada: NO_CALIBRADA (ver calibracion_etiqueta/INFORME.md «RESULTADOS REALES»).
Frentes a resolver con el equipo cheap5m-* (aún sin lanzar; secuencia a decidir con Javi):
 1. Etiqueta virtual: 2,3 % vs 4,1 % real por orden, 27 % vs 50 % por puja; causa = vida de la orden (0,59 s vs 60 s) y unidad (puja ≈7 órdenes), no la cola.
 2. F8: retenido −0,026..+0,025 €/€ vs −0,12/−0,15 de «todas»; pierde menos, no gana.
 3. Regla F5 de A1: no pasa gate; marcados n=36 EV −0,207, no marcados n=63 −0,036.
 4. Transferencia a favoritos ≥0,70: solo el método (unidad = puja, contraste on-chain por order_hash); tasas/EV/cola no transfieren; 0 rellenos reales ≥0,70.
Siguen en cola: censo, wallets CARRY-FAV, Alpha Miner, R8, cron A1+R1 (tras val23), M1/M2, régimen.
