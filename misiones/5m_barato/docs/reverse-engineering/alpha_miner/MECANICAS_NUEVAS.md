# MECÁNICAS NUEVAS 5m barato — ciclo de ingeniería inversa de quien SÍ gana (26-Oct-2026, polymarket-quantum-alpha-miner)
Estado: **EXPLORATORY (diseño; 0 cómputo nuevo)**. Todas las cifras son de artefactos existentes (ruta en cada línea), no recalculadas por mí. Ninguna mecánica tiene € validados. B se mantiene tal cual; esto son subestrategias NUEVAS (mecánica distinta a B y al cementerio).

## 1. Quién gana de forma PERSISTENTE (y quién paga)
Regla de lectura: «persistente» = signo en días distintos de los de selección. Selección ex post marcada como tal.

| Quién | Evidencia de persistencia | Mecanismo hipotético | Pagador | Por qué persiste | ¿Replicable por nosotros? |
|---|---|---|---|---|---|
| **pspspsps5** 0xb0f85baa… (100 % maker, solo compras, 466 mercados/día) | +0,031 €/€ 19 d (IC90 días +0,016..+0,046), 15/19 días +; placebo z=3,8; tickets <0,10: DESC +0,41 → HOLD +0,18 (IC cruza 0) (`wallet_pspspsps5/INFORME.md` §3-4) | **Bid profundo que solo se rellena cuando alguien vende POR DEBAJO de la paridad con el otro token** (f24/f25: estado gap=(1−último opuesto)−p ≥0,05 da a la POBLACIÓN +0,667 €/€, IC90 días +0,34..+0,99, placebo z=18,5; W no es especial dentro de ese estado) + parte por contraparte: con vendedores «raros» W +0,87/+0,35 vs población +0,13/−0,14 (`senales_externas/INFORME.md` §5-6) | vendedores ocasionales (minoristas, stop-loss, cierre de inventario) que lanzan órdenes a mercado sobre libros finos del lado barato | coste de atención (466 mercados/día, tickets de 1 $), capital inmovilizado en pujas que casi nunca se rellenan, cola vacía en niveles profundos | **Sí, en principio** → M2 |
| **Perdedoras persistentes** (z≤−2, 108-222 wallets/día, 2,5-5× el azar) | −0,196 €/€ OOS (IC90 días −0,26..−0,12), **0/9 días +**; 75 % del coste como TOMADOR de longshots a ~0,20, s≈126 (`ganadoras_persistentes/INFORME.md` §1, §3) | son el pagador, no el ganador: el maker del complementario (que les vende el barato) gana **+0,034 €/€** (IC90 +0,018..+0,049, 8/9 d) frente a +0,002 del resto (R7a) | ellas mismas (~4.600 $/día de pérdida en banda) | sesgo de comportamiento (lotería) estable día a día | **Sí, si su presencia se anticipa** (un maker no elige quién le casa; R7b por celdas REJECTED) → M1 |
| **Grandes makers BTC** 0x21f4 / 0xe290 / 0x86b1 | +32 k / +34 k / +22 k € en 16 d (rebate 31-43 % del neto); 44/48 de su clase positivos (selección ex post, listón bajo); top-35 DESC→OOS +0,0081 sin rebate (`rebate_ganadores/INFORME.md` §2, LIBRO nota 24-Oct) | 21f4/e290: cosechadores de pares que bloquean +5,5 %/€ y pierden −5,0 %/€ en la pata suelta; neto = diferencia de dos números de ±5 pp + rebate; ventaja en BTC 0,05-0,30 (56 % del neto con 10 % del volumen); residuo de selección DENTRO de la celda +0,008..+0,016 (no observable) | tomadores de BTC en general + rebate del exchange | escala (≥800 €/día de rebate), gestión de órdenes que no vemos | **No como réplica** (simulador no reproduce: 0/3 días ≤0,5 pp). Pero su NECESIDAD de completar pares es un flujo predecible → M4 |
| **0xf074 / 0x0ab0** (ETH, 100 % maker, asks, clips 5 acc) | +0,85..+1,5 %/vol, 5/6 d — elegidas VIENDO el TEST (exploratorio) (`pares_huecos/GANADORES_PARES_PARA_COSECHAR.md` §2-3) | MM continuo de dos lados con inventario ≤15-30 acc y sesgo hacia el lado que falta (reequilibra P=0,64/0,55) | tomadores de ETH; margen 2,5-3,5c por par | disciplina de inventario; 0xf074 va delante en la cola | Parcial; es la familia H39 (en pausa por Javi) → M5 |
| **Tomadoras persistentes** del proyecto (todas las cripto) | forward propio 20-25 Oct: 63-96 seleccionadas/día, neto +0,01..+1,84 % del volumen, 6/6 días + (`data/shadow/tomadores_persistentes_informe.json`, 26-Oct 07:18Z) | velocidad/información de tomador | makers lentos | latencia | **No**: copia con nuestra latencia (mediana 271 ms) −0,044 €/€ (IC90 −0,050..−0,037, n=620.724, 23 d) = cementerio (copiar tomadoras) |
| **mo-money** 0x32ed2e54… | +10,4 k$ en 10 d; 1ª pata maker ≤0,30 acierta 22,6 % vs 17,1 % de precio; lo direccional «se secó» en octubre (H30) | maker direccional | — | — | NUNCA_BIEN_PROBADA, prior bajo; no prioritario |
| Roster «ganadoras» 0,05-0,30 | **vacío** con BH; z≥2 = lo que da el azar (9-42 vs 43-48 esperadas) | — | — | — | No identificables con 7-8 días |

**Síntesis del pagador** (lo que de verdad aprendemos): en 5m barato el dinero no lo pierde «el mercado», lo pierden dos grupos identificables: (i) **compradores tomadores de longshots** (las perdedoras persistentes) y (ii) **vendedores ocasionales que liquidan bajo paridad**. B pierde porque se pone del MISMO lado que (i) (compra el barato) y en el nivel donde rellena el barrido informado (COND −0,227). Las dos mecánicas con pagador identificado se colocan en el lado contrario de esos flujos: M1 vende a (i), M2 compra a (ii) solo bajo paridad.

## 2. Mapa de mecánicas (distintas entre sí y del cementerio)
Cada una con predicción DIFERENCIAL frente a H0 (sin edge, el EV de cualquier relleno maker ≈ EV poblacional de su celda).

### M0 — Nula
El EV del maker barato es el del régimen (DESC +0,09 → HOLD +0,02, RE-CEMENTERIO E02) y ninguna condición ex ante lo desplaza fuera de muestra. Se cumple si M1-M4 dan Δ con IC90 por días que contiene 0.

### M1 — CONTRA-PERDEDORA-VISIBLE (vender el barato a quien ya sabemos que paga)
- **Decisión**: tras ver on-chain (bloque + ~3 s) la primera compra TOMADORA de una perdedora persistente (lista walk-forward d−7..d−1) del lado barato s∈[0,05-0,30] en el mercado m, colocar una puja maker en el complementario ŝ (= vender s) durante 5-60 s.
- **Predicción diferencial**: (a) las perdedoras REPITEN en (m,s) tras su primera compra visible (P(2ª compra en 60 s) alta); (b) los rellenos maker del complementario en [t+5, t+60] s rinden más que el resto del mismo día×moneda×precio; (c) un disparador placebo (tomadora NO perdedora con volumen y precio emparejados) no da el mismo Δ.
- **Distinta de**: R7b (celdas, REJECTED: aquí es identidad+momento), «contrapunto informado» (miraba la clase del tomador que rellena a B, no anticipar presencia), copiar tomadoras (aquí se va en CONTRA).
- **Confusores**: las perdedoras compran tras movimientos (el lado barato se abarata por momentum) → el complementario sube por dirección, no por ellas → control emparejado por movimiento previo de Binance/precio; racimos por cierre.
- **Test mínimo**: `PREREG_M1_CONTRA_PERDEDORA.md` (reutiliza scripts de `ganadoras_persistentes`; ~1-2 min por día de CPU).
- **€/año contrafactual**: el complementario frente a perdedoras rinde +0,034 sobre ~85 k$/día de capital (0,77 M$ / 9 d, R7a). Si 20-40 % de ese flujo llega tras un disparador visible y capturamos 5-10 % con Δ ≈ +0,03 → ≈ 85,6 k × 0,3 × 0,07 × 0,03 × 365 ≈ **5-25 k€/año**. Capital alto por € de PnL (compra a ~0,80): rotación en ≤5 min, no es límite.

### M2 — COLCHÓN-PARIDAD (puja profunda que solo se rellena bajo paridad)
- **Decisión**: mantener pujas maker profundas en el lado barato s (p<0,10, BTC primero) cuyo precio queda ≥0,05 por debajo de (1 − último precio operado del token opuesto); se recolocan cuando el opuesto se mueve. Se rellenan solo si un vendedor cruza muy por debajo de la paridad.
- **Predicción diferencial**: (a) fuera de muestra (días ≥24-Oct, nunca mirados) los rellenos en estado gap≥0,05 rinden ≥ +0,10 €/€ y más que el resto del mismo día; (b) el efecto es mayor con vendedores no repetidores (contraparte minorista) que con bots repetidores; (c) en niveles profundos la cola por delante es pequeña → la fracción de ese flujo que se lleva una puja de 5 acc es alta (a medir en fase 2).
- **Distinta de**: stink bids genéricos (refutados por supervivencia: aquí el desenlace es oficial y el disparador es la incoherencia entre tokens, no la distancia al precio), F7 precio del par (filtraba las pujas de B AL TOP; aquí la puja vive lejos del top y solo casa con vendedores bajo paridad), escalera de W (H-C refutada como fuente).
- **Riesgos conocidos**: umbral 0,05 elegido tras ver f24 (K≈15) → solo vale el OOS; HOLD hit/p ≈0,99 (el EV puede venir de la cola de pagos: varianza enorme, sd ~6,4 €/€ por unidad <0,10 → ~1.300 unidades para detectar +0,29); «último opuesto» con edad p50 1,5 s puede estar rancio (trampa del prior rancio) → el estado debe medirse con el libro WS en fase 2.
- **Test mínimo**: `PREREG_M2_COLCHON_PARIDAD.md` (fase 1 población on-chain OOS; fase 2 capturabilidad con [pes,opt] calibrados).
- **€/año contrafactual**: flujo de población en el estado ≈ 4.345 $/día (BTC/ETH/SOL, <0,10; f24). Cuota q 10-30 % (sin medir) × EV +0,10 (suelo del gate) → **16-48 k€/año**; con el EV HOLD +0,39 → 62-186 k€/año (NO citar sin fase 1+2). Capital mínimo (tickets <0,10).

### M3 — INERCIA-TWAP del lado barato en el último minuto
- **Decisión**: entre T−60 y T−10 s, cuando el spot cruza la referencia pero el TWAP60 oficial ([e−62, e−3]) ya está mayoritariamente fijado del otro lado, vender (pedir en el ask) el lado barato que el spot «reanima».
- **Predicción diferencial**: el mid del lado barato sobre-reacciona a la distancia SPOT−ref frente a la distancia TWAP_parcial−ref: en una regresión del desenlace sobre logit(mid) + divergencia (spot-implícita − TWAP-implícita), el coeficiente de la divergencia es ≠0 fuera de muestra y con signo «el mercado precia spot».
- **Distinta de**: FV v1-v4 (Φ(z) con spot y σ300, sobreconfiado; aquí no se pide batir al mid con un FV sino medir el error del mid condicionado a la mecánica de resolución), PRECIERRE (tomador del favorito, fuera de la familia).
- **Riesgo**: trampa del FV sobreconfiado → calibrar SIEMPRE contra el mid; ticks Chainlink por RECEPCIÓN (+1,36 s); racimos por cierre.
- **Test mínimo** (fase 0, barato): `precierre_multioffset_fase0.csv` (TWAP `_v2`, varios offsets, 5m) × mid del libro; DESC/HOLD por días; coste minutos. Prereg pendiente (prioridad 4).
- **€/año**: no cuantificable antes de la fase 0; techo por capacidad del lado barato en el último minuto ≲10-20 k€.

### M4 — COMPLETADO DE COSECHADORES (vender la pata que les falta)
- **Decisión**: cuando el inventario on-chain de un gran cosechador (21f4/e290 y los que el test identifique por CONDUCTA en días previos) en el mercado m queda desequilibrado ≥X acc hacia un lado, ofrecer (ask maker) el lado que le falta a precio ≥ mid, porque tiende a completarlo como tomador antes del cierre.
- **Predicción diferencial**: (a) los rellenos maker cuya contraparte TOMADORA es un cosechador tienen EV/markout mejor que los de la población en la misma celda (su compra es de inventario, no de información); (b) la compra de completado es predecible desde su desequilibrio visible (bloque+3 s) con P alta en los 60 s siguientes.
- **Distinta de**: cosechar/pares (nosotros no cosechamos: vendemos el completado), copiar ganadoras (no copiamos su dirección; explotamos su restricción de inventario).
- **Hecho de partida**: 21f4/e290 hacen 23-33 % de su volumen como tomador (21f4 −14 k€ en 16 d, EV −0,016) (`rebate_ganadores` §2.6): pagan spread+fee por completar.
- **€/año contrafactual**: volumen tomador de ambos ≈ 0,28 × (4,0+3,0 M€)/16 d ≈ 120 k€/día; cuota 2-5 % × margen ~2 %/€ → **10-40 k€/año**. Solapa con M5 (tomar el máximo, no sumar).
- **Test mínimo** (prioridad 3, prereg a escribir tras M1/M2): ledger `r4` de rebate_ganadores (1,40 M fills BTC 06-21 Oct, ya extraído) → markout y EV de los makers que les rellenan vs población; luego P(completado | desequilibrio) en días 22-25 Oct (OOS).

### M5 — MM CON INVENTARIO ACOTADO VÍA ASKS (familia H39)
- **Decisión**: cotizar ambos lados con asks (acuñando pares), clips 5 acc, |inventario| ≤15-30 acc, sesgo de precio hacia el lado que falta.
- **Predicción diferencial**: el residuo de pata suelta cae con el tope de inventario (dosis-respuesta medida ex post: res_frac <0,1 +4,0 %/vol vs >0,6 −11,6 %) → con tope ex ante el EV/vol ≥ +0,5 % + rebate.
- **Bloqueo**: H39 en pausa por orden de Javi; además necesita cola real (0xf074 va delante: no medible sin órdenes). **No se prerregistra sin orden de Javi.**
- **€/año**: ≤5-15 k€ (capacidad a nuestra escala pequeña según `pares_huecos/INFORME.md` §4). Solapa con M4.

### Descartadas en este ciclo por ser rebautizos (no reabrir)
- «Tamaño 20-200 acc como W»: la población con ese tamaño ≈0 en HOLD; no es mecanismo.
- Copiar tomadoras persistentes / roster ganador: cementerio (−0,044 con nuestra latencia).
- Celdas donde operan perdedoras/ganadoras (R2/R7b): efecto BTC>alts del periodo.
- Defensa por identidad de tomador informado sobre B: «contrapunto informado» REJECTED.
- Régimen d−1: ya en forward (H50).

## 3. Cartera sin solapes (contrafactual, NO previsión)
| Mecánica | lado/flujo | €/año contrafactual | solapa con | se suma |
|---|---|---|---|---|
| M2 | compra barato bajo paridad (vendedores ocasionales) | 16-48 k (gate) | M1 mismos mercados, flujo opuesto | sí |
| M1 | vende barato a perdedoras | 5-25 k | M2 (mercados), B (B compra el barato: se cancelan si coinciden) | sí |
| M4 / M5 | vende completado a cosechadores / MM | 10-40 k (máx de ambos) | entre sí | uno |
| M3 | vende barato reanimado en último minuto | ≲10-20 k | M1 (mismo lado) | parcial |
| **Total optimista sin solapes** | | **≈ 40-130 k€/año** | | |
Hueco a 200 k€: **200 k validado; ≥70 k incluso contra el optimista**. Lo único que lo cerraría sola es M2 con EV OOS ≈ +0,3 y cuota ≥30 % — exactamente lo que la fase 1+2 de M2 decide. Eso es lo que hace a M2 la prueba nº1.

## 4. Priorización (valor de la información × €/año × coste)
1. **M2 COLCHÓN-PARIDAD** — mayor € potencial, pagador identificado, fase 1 barata y con OOS limpio ya en disco (`m5_onchain_2026-10-24/25.csv.gz` existen; f24/f25 solo vieron 05-23 Oct). Prereg: `PREREG_M2_COLCHON_PARIDAD.md`.
2. **M1 CONTRA-PERDEDORA-VISIBLE** — único pagador con persistencia OOS demostrada (0/9 días +); test de 1-2 min/día con scripts existentes. Prereg: `PREREG_M1_CONTRA_PERDEDORA.md`.
3. **M4 COMPLETADO DE COSECHADORES** — datos ya extraídos (r4); prereg tras ver si M1/M2 sobreviven (no antes, para no gastar K).
(4. M3 — fase 0 barata pero mayor riesgo de rebautizo FV; 5. M5 — solo con orden de Javi.)
Hashes: ver `PLAN_CICLO.md` §1.
