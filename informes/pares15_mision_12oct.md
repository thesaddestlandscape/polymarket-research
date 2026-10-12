# Misión «pares 15m: eliminar las patas sueltas y escalar» (Javi, 12-Oct, prompt definitivo)
Optimizar el PnL neto de CARTERA (pares + patas sueltas + costes + exposición), no el % de pares. Reglas congeladas
(anclar/crear/mixta del experimento, dev 8857438f2b) = benchmarks inmutables. Nada a dinero sin gates + /code-review + OK.

## Paso 1 — Auditoría (12-Oct)
`experimento_pares_cola_15m.py` (dev): de T=898 s a T=90 s una puja maker post-only de 5 acciones en YES y otra en NO en
el libro WS; un relleno cierra ese lado; la otra puja SIGUE quieta (no hay lógica de completar ni de salir); a T=90 s se
cancela todo y lo suelto va a resolución. Cancela además por seguridad si la orden queda EXPUESTA (≥2 ticks sobre el
mejor bid ajeno o sola). anclar = unirse al mejor bid sin moverse · crear = 1 tick sobre el mejor bid ajeno si cabe bajo
el ask, recolocar si nos superan (≤3) · mixta = crear la 1ª orden de cada lado y luego anclar. Ensayo en seco: rellenos
simulados con cola CONSERVADORA (toda la cola delante al unirse; 0 si creamos el nivel), consumo por ventas tomadoras y
acuñación, ventana de vida con latencias medidas.

## Paso 2 — Reproducción (EXACTA) — `analisis_pares15_patas_sueltas.py`, 80 mercados 09-10 Oct, desenlace oficial 100 %
| | SOL anclar | SOL crear | SOL mixta | BTC anclar | BTC crear | BTC mixta | TOTAL |
|---|---|---|---|---|---|---|---|
| pares completos | 4 (+3,45) | 9 (+4,50) | 4 (+2,91) | 11 (+1,90) | 12 (+1,04) | 10 (+0,87) | 50 (+14,67 $) |
| patas sueltas | 9 (−18,54) | 4 (−3,20) | 7 (−2,65) | 2 (−4,90) | 2 (−1,54) | 3 (−2,38) | 27 (−33,21 $) |
| ganan | 0/9 | 1/4 | 2/7 | 0/2 | 1/2 | 1/3 | 5/27 (18,5 %) |
Margen por par +0,293 $ (5 acc, ~6c/acc); pérdida por pata suelta −1,23 $; **las sueltas consumen el 226 % del margen
de los pares** (1 suelta ≈ 4 pares). Total −18,54 $.

## Paso 3 — Autopsia del primer relleno
Sueltas (27) vs pares (50): precio 0,42 vs 0,49 · espera 15 s vs 3 s · cola 13 vs 50 · el mid cae a +5 s en el 67 % vs
42 %. Precio medio de las sueltas 0,41 → esperable ~40 % de acierto, real 18,5 % → selección adversa: nos llenan el lado
que está bajando. Espera del 2º relleno en los pares: P50 55 s, P75 169 s, P90 558 s.

## Pasos 4-6 — Políticas nuevas (DESCUBRIMIENTO: misma muestra, nada validado)
- **A PAIR15_TAKER_COMPLETE** (completar como tomador al primer relleno, margen m 0-0,02, L 300-1000 ms): solo hay margen
  en 1-2 de 77 → −18,5/−19,8 $. **Estructuralmente imposible**: el margen del par existe solo si AMBOS lados se compran
  en el bid (coste ≈ 1 − spread); bid de un lado + ask del otro + comisión ≥ 1.
- **B PAIR15_FAST_EXIT** (vender la pata al bid al instante, L 300-1000): −15,8/−17,0 $ (mejor que el original, pero mata
  también los pares que se habrían completado).
- **C PAIR15_HYBRID límite de exposición τ** (esperar al maker τ s; si no llega, cancelar y salir o mantener):
  τ 2-300 s: salir −16,3…−25,2 $; mantener −20,4…−23,8 $. **Ninguna positiva.**
Conclusión de la fase: con este mecanismo de entrada, la gestión posterior al primer relleno NO salva la estrategia: el
margen por par (~6c/acc) es menor que lo que cuesta la selección adversa más salir (spread + comisión + deriva).

## Estado y bloqueos
- Validación de "crear" (40 SOL + 40 BTC) en curso desde 12-Oct 14:59Z → `analisis_experimento_pares_sim.py --desde 2026-10-12T14:59`.
- **BLOCKED_BY_DATA**: la cola del ensayo es conservadora (toda la cola delante); los cosechadores ganadores están al frente
  (entran a T=898 creando nivel). La posición real en la cola solo se mide con órdenes reales: es el propósito original
  del experimento con la wallet dedicada (5 USDC, OK Javi pendiente).
- Siguiente investigación: filtro de ENTRADA (¿se puede predecir en T=898, antes de pujar, qué mercados acaban en pata
  suelta?: libro, desequilibrio, Binance) — el único sitio donde aún puede estar la mejora.

## Registro de versiones
| versión | estado | resultado (descubrimiento 09-10 Oct) |
|---|---|---|
| anclar / crear / mixta (originales) | benchmarks | −15,09·+1,30·+0,26 SOL; −3,00·−0,50·−1,51 BTC |
| A PAIR15_TAKER_COMPLETE_V1 | REFUTED (estructural) | completa 1-2/77; −18,5/−19,8 $ |
| B PAIR15_FAST_EXIT_V1 | TESTING (negativo) | −15,8 $ |
| C PAIR15_HYBRID_V1 (τ) | TESTING (negativo) | mejor −16,3 $ (τ=2 s) |
| **PAIR15_ENTRY_MID_V1a** (\|mid YES − 0,5\| ≤ 0,02 en la apertura, incluye el borde) | FORWARD_PENDING (hash 4f3406a18ebdf542) | descubrimiento 31/80 merc., 7 sueltas, +1,76 $, sin el mejor −1,14 (no cuenta) |
| **PAIR15_ENTRY_MID_V1b** (≤ 0,015) | FORWARD_PENDING (hash 4f3406a18ebdf542) | descubrimiento 26/80 merc., 4 sueltas, +6,76 $, sin el mejor +3,86 (no cuenta) |

## Filtro de ENTRADA (12-Oct 17:15Z, `analisis_pares15_filtro_entrada.py`)
En la apertura (T=898 s): spread YES 1 tick → 15 % sueltas, +0,06 $/merc; ≥4 ticks → 61 %, −0,47 (el "margen potencial"
ancho es una trampa: libro poco competido). Spread de 1 tick ≈ casi solo BTC (confunde moneda). |mid YES − 0,5| ≤ 0,015
→ 15 % sueltas, +0,26 $/merc. Binance (ret 60/300 s, operaciones) sin señal limpia. Congelada **PAIR15_ENTRY_MID_V1**
(|mid − 0,5| ≤ 0,02) ANTES de mirar el ensayo 'crear' (desde 14:59Z) → validación cuando exista m15_registro del 12-Oct
(cron 03:45 del 13-Oct): `python3 vigia_pares15_entrada_mid.py`.

**Corrección 17:25Z (Fail Loud)**: el +6,76 $ inicial correspondía en realidad a ≤0,015 (5 mercados en el borde exacto 0,02 quedaban fuera por coma flotante y pierden); con ≤0,02 inclusivo es +1,76 $ (sin el mejor −1,14). El resultado es SENSIBLE AL CORTE → se congelan y validan las dos variantes (V1a/V1b, multiplicidad 2) antes de mirar ningún mercado de validación.
