# PREREG E-RE-CB-03 — criterio de TRANSFERENCIA de la etiqueta M a órdenes contrafactuales (RE-CANCEL-B). Congelado ANTES de calcular nada sobre verdad nueva.
Hora: la del mtime de este fichero y su sha256 en PREREG_TRANSFERENCIA.sha256 (no una hora escrita a mano).

## Lo ya visto (honestidad)
- Todo E-RE-CB-01/02 y la validación (VALIDACION_RE_CANCEL_B.md): sobre TEST 22-23 Oct, sin auto-print, M − ingenua −0,007 (IC90 −0,078..+0,068); M − placebo +0,0675 (IC90 en el filo según semilla). Esos 4 días (20-23 Oct) de B NO cuentan como verdad nueva.
- Para la opción (b) solo se han mirado CABECERAS/tipos de fila (sin resultados): `onchain_fills_D.csv.gz` (tipo,bloque,ts_est,tx,log_index,order_hash,maker,taker,side,token_id,maker_amt,taker_amt,fee), `m5_registro_D` (k/q top-of-book/t/x), `libro5_ms_D_*` (G/d/B/T: L2 agregado por nivel con hora de recepción), `libro5_bajos_D` (B: snapshots de niveles bajos). Ninguno trae id de orden en el libro.

## Verdades admitidas (en este orden)
- V1: órdenes reales NUEVAS tipo B (B o micro-órdenes aleatorizadas, fecha ≥ 24-Oct y posterior a este prereg), verdad on-chain por order_hash. Unidad = PUJA (como E-RE-CB-01).
- V2 (opción b del validador): órdenes de OTROS makers en niveles tipo B (bid (0,11-0,30], ETH/SOL/XRP 5m), verdad = relleno on-chain por order_hash; SOLO si pasan la puerta de identificación I. Unidad = ORDEN inferida con vida [t_alta, t_fin].

## Puerta de identificación I (solo V2; se evalúa ANTES de calcular ninguna puntuación)
- I1: las fuentes dan hora de alta Y de fin (relleno o cancelación) por orden ajena, incluidas las órdenes NO rellenas (negativos). Si no (solo hay rellenos on-chain y L2 agregado sin id), pasar a I2.
- I2: inferencia de órdenes ajenas desde el L2 agregado (episodio de nivel 0→s en un solo evento, solo decrementos hasta volver a 0; fin por relleno si un decremento casa con un relleno on-chain al precio, por cancelación si no). Se acepta solo si (a) recupera el alta (±250 ms) y el fin (±500 ms) de las órdenes REALES de B (ordenes_b.parquet, 20-23 Oct) en ≥80 %, y (b) el subconjunto identificable NO es degenerado: ≥30 % de sus positivos tienen algún print consumidor a p que NO es del propio order_hash (si no, la puntuación «sin auto-print» queda vacía o forzada por la verdad).
- Si I falla: V2 = BLOCKED (bloqueo A, información). No se calcula ninguna puntuación. Se informa el n de rellenos ajenos en niveles tipo B como COTA de positivos (sin negativos no hay AUC).

## Puntuaciones (ambas SIN auto-print: se quitan del feed los prints de TODOS los rellenos on-chain de la(s) orden(es) etiquetada(s), regla de t4_sin_autoprint.py; si un relleno no casa por tamaño, se quita el print más cercano a ese precio en [ts_est−6 s, ts_est+1 s] sea cual sea su tamaño, y se informa cuántos)
- M: V1 → v3lib.simular_puja (sha 664f830a…), tune_latencias.json, 20 réplicas, semilla 7, inicio = t_dec de la 1ª orden. V2 → regla de consumo de la Capa 1 (e=250 ms, g=0,5, f=0) sobre la vida inferida [t_alta, t_fin].
- Ingenua: volumen de prints que consumen el PRIMER objetivo (V1) / el precio de la orden (V2) desde el inicio hasta T−60 s.
- Placebo: M con prints +90 s.

## Criterio (mínimos fijados; IC90 bootstrap por CIERRE, 2.000 reps)
- Mínimos para evaluar: n ≥ 750 unidades, ≥ 250 cierres, ≥ 5 días distintos, ≥ 100 positivos y ≥ 100 negativos. Sin miradas intermedias (con n=187 el IC90 del ΔAUC mide ±0,07; ±0,035 exige ~750).
- TRANSFIERE si: ΔAUC(M − ingenua) ≥ +0,03 con límite inferior del IC90 > 0 con las semillas de bootstrap 1, 2, 3, 4, 5 y 11 (todas); Y ΔAUC(M − placebo) ≥ +0,10 con IC90 > 0 (semilla 11); Y |media P_M − real| ≤ 0,05 con IC90 que contiene 0; Y el signo de ΔAUC(M − ingenua) es positivo en ≥ 4 de 5 días.
- NO_TRANSFIERE si el límite SUPERIOR del IC90 de ΔAUC(M − ingenua) < +0,03 (semilla 11).
- INCONCLUSO en otro caso.
- Consecuencia: TRANSFIERE → F8/A1/R3 pueden usar M como etiqueta (siguen necesitando sus propios gates; la etiqueta deja de ser motivo de EXPLORATORY). NO_TRANSFIERE → M solo para calibración de nivel; F8/A1/R3 usan la ingenua o el intervalo. INCONCLUSO o BLOCKED → F8/A1/R3 siguen EXPLORATORY con el intervalo P_puja [0,44; 0,52], AUC [0,70; 0,79], extremo sin auto-print (sesgo ≈ −5 pp), siempre frente a la ingenua.
- Nada de este criterio se cambia tras ver datos; un cambio = versión nueva con fecha y motivo.
