# «No pujar > 0,243» en B: ¿real o espejismo? (24-Oct-2026, ~10:50Z). EXPLORATORIO. Solo lectura; no toca B/live/crons.
Scripts: `load.py`, `vigia_skip025_forward.py` (sha256 2785855f...d45524). El resto del análisis se hizo con snippets ad hoc sobre `O_feat.pkl`/`U_orders.pkl`/`F_r3.pkl` (aquí guardados).
Datos: fills de B (215; 202 con desenlace ≥ 20-22 Oct → 186 unidades mercado+lado hasta 22-Oct), 3.796 pujas de B con desenlace (194 rellenas; `etiquetado_B_*` + `puja_post` del ledger = libro al pujar), población 28.871 rellenos de otros makers 17-22 Oct (415 wallets, ETH/SOL/XRP 5m, sin fee de maker), `r3_shadow` BASE (22-24 Oct, simulador de las pujas de B en vivo sobre el WS).
Todo EV = Σpnl/Σcoste (ponderado por €), fee de maker 0, unidad mercado+lado(+precio), IC90 por CIERRE.

## Veredicto: ESPEJISMO PARCIAL, no confirmado. Hay una señal interna en B, no replicada fuera de B, y el efecto se encoge ~4x en la réplica independiente.
| Test | Resultado | Lectura |
|---|---|---|
| B fills >0,243 vs ≤0,243 (186 unid.) | hit 0,15 vs 0,21; EV −0,445 (61 unid., 51 cierres) vs +0,222 | descubrimiento (ya visto) |
| B vs POBLACIÓN emparejada (misma moneda×día×bucket 0,04) | >0,243: EV B −0,445 vs pob +0,075 → exceso **−0,52** IC90 (−0,78,−0,22); ≤0,243: +0,12 (IC cruza 0) | la población NO pierde ahí (EV pob >0,243 = +0,085 en 20-22 Oct; +0,008 global) |
| Dosis-respuesta en B (3.796 pujas, rellena vs NO rellena a igual precio; unidad mercado+lado+precio) | AS (hit−p rellena menos no rellena): ≤0,243 −0,006 (n_rell 133); >0,243 **−0,158** IC90 (−0,25,−0,07) (n_rell 61, 51 cierres); DiD −0,152 (−0,25,−0,05). Barrido de 8 cortes (0,14…0,28): AS_hi −0,07→−0,16→−0,11, monótono; pendiente rellena×precio −1,07 IC90 (−2,0,−0,1) | la forma es suave, no un acantilado: favorece «real» |
| Max-estadístico sobre los 8 cortes (K=8) | p 0,008 (bootstrap por cierre centrado); p 0,063 (permutación de «rellena» dentro de día×moneda×precio, sin clúster) | **no pasa Bonferroni 0,10/ K total**: K_total honesto (56 celdas anatomía + 25 as_b_trades + 8 cortes + 10 cubos) ≈ 100 vistas sobre los MISMOS datos |
| Por día (AS_hi) | 20-Oct +0,001 / 21-Oct −0,077 / 22-Oct **−0,317** / 23-Oct −0,136 (n_rell 5) | el −24,3 € de 34,4 € del 22-Oct (1/23 acertó, día bajista); sin ese día el efecto es ~−0,05 |
| RÉPLICA INDEPENDIENTE: r3_shadow BASE (22-24 Oct, fills simulados, 300 unid. cons_x) | EXC de saltar >0,243: cons_x +0,075 IC90 (−0,08,+0,23) p placebo 0,22; cons_r +0,04 (−0,14,+0,22) p 0,39; opt_x +0,111 (−0,02,+0,25) p 0,058. Por día cons_x hi−lo: 22 +, 23 −, 24 −  | mismo signo, ¼ del tamaño, ningún IC>0 |
| Población (29 k) | EV >0,243 = +0,008 global, sin dosis-respuesta (ya conocido); emparejada por día +0,07/+0,09 | no replica |
**Cifras de decisión:** efecto a creer ≈ entre 0 (población) y +0,07..+0,11 por € retenido (réplica sim); el +0,297 (test)/+0,25 es el techo del descubrimiento.

## Mecanismo (descriptivo; NINGUNO es predictor previo al relleno)
- B pone el precio en best_bid − 1c (gap mediano 0,01; igual en ≥0,25 y <0,25; cola y profundidad por delante equivalentes: cola 63 vs 61, ahead 63 vs 69). Un bid >0,243 equivale a mid ≈0,29-0,30 (cerca del 50 % del token, ya fuera del régimen «lotería»).
- Su AS es UNIFORME por moneda (ETH −0,19, SOL −0,14, XRP −0,13), lado (NO −0,17, YES −0,13), spread, cola, T y mid: no hay subconjunto «culpable» dentro de >0,243. Eso apoya más «desplazamiento general por precio» (o ruido común) que un mecanismo de libro identificable.
- Tras el relleno (69 de B con anatomía, n pequeño): mid a 30 s −0,143 (hi) vs +0,102 (lo); a 120 s −0,287 vs +0,138; Binance a 30 s −1,13 vs +0,31 bps; Chainlink 30 s −1,43 vs −0,14 bps. Es decir: los rellenos >0,243 son barridos que SIGUEN (momentum) y los baratos revierten (rebote de lotería). Coherente con selección adversa informada solo en la zona del 25-30 %, pero es post-relleno (no accionable) y n=47 vs 105.
- No explica por qué la población (que también puja en esos precios) no sufre: queda abierto. Hipótesis no medida: B puja siempre best_bid−1c (nunca en el best bid ni dentro) y sus rellenos solo ocurren con barridos que atraviesan el best bid; la población incluye makers en el best bid con rellenos pequeños no adversos. Falta posición exacta en la cola de los rellenos de la población para contrastar (DATA_BLOCKED: la población no trae libro).
- Dónde NO está el efecto: spread, T, cola, lado, moneda (todos con AS ≈ igual dentro de >0,243).

## Dinero (SIN extrapolar de muestra pequeña)
- Ahorro bruto observado en B: saltar >0,243 evita −34,4 € de pnl sobre 77 € de coste en 3 días (−24,3 € en un solo día). NO es un ritmo anual.
- Ganancia de saltar = −EV(>0,243) × coste(>0,243). Flujo de B ≈ 68 €/día de coste, de los que ≈ 43 % (≈ 29 €/día) son >0,243. Con EV(>0,243): B real −0,445 → ≈ +13 €/día (4,7 k€/año, techo); réplica sim cons_x −0,212 → ≈ +6 €/día (2,2 k€/año; ojo, el sim es negativo en todo, ≈ +1 €/día si fuese «igual que lo barato»); si es neutro (población +0,07) → 0. Ponderando por la evidencia: **~1-2 k€/año a escala B, ~10-20 k€/año a 10x de flujo, solo si el efecto es real**.
- Ninguna cifra sostiene los 200 k€/año: esto es, como mucho, un recorte de pérdidas de B; no es «el click» de Javi.
- Coste de oportunidad: saltar quita el 35-43 % de las pujas (fill-rate no cambia); la variante lo>0,243 de B tiene EV +0,22 (n=125, IC cruza 0), también ruidoso.

## Qué NO es (por si se reabre)
No es V3 (spread>0,02), V9 (1.er relleno por cierre) ni R0: DiD AS de >0,243 es −0,152 con ambos spread bajo/alto. No se mezcla con R1/R2/R3 (mismo sim: BASE contra R2/R3 se comparan aparte). Cementerio: no se renombra nada; la «versión mejorada» no existe todavía porque el mecanismo no se aísla.

## FORWARD SHADOW propuesto (sin dinero; no instalado)
**Hipótesis congelada H-SKIP025:** en B (ETH/SOL/XRP 5m, pujas H35 best_bid−1c), saltarse las pujas con precio > 0,243 mejora el EV por € retenido. Unidad mercado+lado+precio; EXCESO = EV(retenidas) − EV(todas).
**Datos:** `r3_shadow` BASE (pujas de B simuladas en vivo; ya corre; cron de desenlaces */20) escenario cons_x PRIMARIO (cota prudente), opt_x/cons_r de contraste. B real parado (ledger sin pujas el 24-Oct): si se reanuda, añadir `etiquetado_B_*` como segunda fuente (fill real).
**Ventana forward:** desde 2026-10-25 00:00Z (el 24-Oct lo he visto: cons_x EXC +0,21 en 27 cierres, p placebo 0,11, NO cuenta).
**Gates (todos):** ≥10 días; ≥40 cierres saltados (≥ unos 4 días a ~27-36/día); IC90 por cierre del EXCESO >0; EXCESO>0 sin los 2 mejores días; placebo (misma fracción de € al azar dentro del día, 3000) p<0,05; signo igual en cons_x y opt_x; si cons_r da EXCESO ≤0 se reporta pero no veta. Corte fijo 0,243 (sin re-optimizar). K=1.
**Potencia:** SE del EXCESO ≈0,08-0,10 con 108 cierres hi (réplica); para detectar +0,10 con IC90 hacen falta ~150 cierres hi (≈5-6 días), +0,05 ≈ 600 (≈ 22 días). Con 10 días la prueba solo detecta ≥ +0,07: un efecto de +0,04 NO se podrá confirmar; se declarará «no resuelto».
**Script:** `vigia_skip025_forward.py --desde 2026-10-25 --salida .../skip025_forward.json` (probado hoy con 24-Oct; solo lectura, ~15 s, RAM <300 MB).
**Cron propuesto (NO instalado):** `50 10 * * * flock -n /tmp/skip025.lock bash -c 'ulimit -v 2500000; nice -n 19 ionice -c3 /usr/bin/python3 -I /root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/precio_025/vigia_skip025_forward.py --desde 2026-10-25 --salida /root/polymarket-research-datalogs/r3_shadow/skip025_forward.json >> /root/polymarket-research/logs/skip025.log 2>&1 || python3 -c "import sys;sys.path.insert(0,\"/root/polymarket-research\");from shadow_digest import enviar_telegram as e;e(\"skip025 vigia FALLO\")"'` (10:50Z, fuera de 06-09Z; tras el desenlace de las 10:20).
**Límites:** simulador con fidelidad media (acierto relleno 18,8 % sim vs 25 % real; EV sim −0,146 vs real +0,16): los fills simulados bajan el nivel, no necesariamente la diferencia hi−lo. Un resultado positivo SOLO justifica una micro-prueba real de B (con /code-review y OK de Javi), nunca el escalado.

## Siguiente paso (mínimo)
1. Dejar correr el forward shadow ≥10 días; leer a diario `skip025_forward.json`.
2. Mientras tanto, medir en el registro ms 17-22 Oct (rotando) la posición de cola de los rellenos de la POBLACIÓN a ≥0,25 vs <0,25 para ver si la población está en el best bid (hipótesis del mecanismo) — única vía a un mecanismo real.
3. No tocar B por esta regla antes de ese forward.
