# MISIÓN DEFINITIVA 15m — encontrar y explotar cualquier ineficiencia rentable (Javi, 07-Oct)

Orden de Javi: **seguirla ESTRICTAMENTE y EN ORDEN**. Métrica principal: € netos realmente capturables (tras fees,
spread, slippage, impacto, profundidad, P(fill), parciales, legging, latencia, selección adversa, inventario, unwind,
rebates reales). AUC/accuracy/Sharpe/nº de señales = secundarias. Objetivo: 200.000 € limpios en cripto.
Modos a explorar a la vez y demostrar (no asumir): MAKER, TAKER, HYBRID.
Reglas duras: §39 tolerancia cero a look-ahead/timestamps/token mapping/apertura/expiry/libro rancio/duplicados/
profundidad/fees; §40 precio histórico ≠ ejecutable (precio disponible en la decisión + latencia); §48 no dar por
imposible por latencia (pre-posición, resting, cola, maker, inventario, orden en vuelo, anticipación, ruta alternativa,
híbrido); §49 no fabricar soluciones (fills imposibles, datos futuros, latencia inexistente, profundidad falsa, fee
incorrecta, órdenes que la API no permite → descartar); §50 "rentable" = PnL neto realista; §52 elegir por dinero
defendible por unidad de riesgo y capital; §54 ante una anomalía, preguntar primero "¿se convierte en una orden que
capture dinero?"; §56 ni resuelto por una positiva ni imposible por 100 negativas: DESCUBRIR → MEDIR → EJECUTAR →
FALSAR → OPTIMIZAR → VALIDAR → MINAR.

## Orden de ejecución y estado (actualizar en cada sesión)
| # | Bloque | Estado |
|---|---|---|
| 3-4 | Auditoría de latencia: qué es de Polymarket / nuestro / red / firma / transmisión / ack / tipo de orden / endpoint / mercado / tamaño / congestión. LATENCY BUDGET por etapa (event→receive→parse→detect→decide→construct→sign→send→exchange→match→fill) con P50/P90/P95/P99/máx + CRITICAL PATH | EN CURSO 07-Oct: pasivo (`latencia_presupuesto_15m.py`); activo (órdenes reales mínimas) pendiente de OK de Javi + /code-review |
|  | **Resultado 07-Oct** (pasivo `latencia_presupuesto_15m.py`, activo `medir_latencia_ordenes_15m.py` a coste 0, OK Javi): Binance→nosotros 131 ms P50 (P90 145, P99 283; geografía Tokio); Polymarket evento→nosotros 20-24 ms P50 (P90 55-130) salvo **BTC 15m P90 423 / P99 2.126 ms y BTC 5m P90 881** (mixto servidor/nuestro, crece con mensajes/s y horario USA; muestreo de sockets 14:00Z y 19:00Z); parse 4-19 µs; firma 6 ms P50 (P99 135 con carga); red Cloudflare HEL 1,5 ms, borde→origen ~55 ms ida y vuelta; **GTC post-only 69 ms, cancel 60 ms, FOK no marketable 216 ms (n=30), FOK marketable que muere 244 ms (n=3: 216/244/887)** → las órdenes tomadoras pagan ~145 ms de retraso crucen o no; casado +0-30 ms. Cadena tomador tras Binance ≈370 ms P50; cancelación maker tras Binance ≈170 ms efectiva. PENDIENTE: T4 n≥20 (también horario USA), muestreo de sockets BTC, dependencia por tamaño. |
| 5 | Batir cada ms (arquitectura, infra, región, red, WS, endpoints, serialización, parsing, firma, CPU, memoria, concurrencia, precálculo, preparación, fast path, event-driven) — cada optimización medida en PnL y latencia | **EN CURSO 07-Oct.** Medido: cliente CLOB ya usa httpx HTTP/2 persistente y sin reintentos ocultos; conexión nueva +25 ms (TLS) vs keep-alive; test de inactividad en curso (5 s sin tráfico → 175 ms en 1 caso). Feeds BTC en Helsinki (60 s, P50 llegada): Kraken 24 ms, Bitstamp 28, Coinbase 64, Bybit 94, Binance 133, OKX 134; Binance futuros no responde desde el VPS (sin verificar causa); captura 20 min (08:24Z) y 30 min (14:30Z) para lead-lag. **VALOR EN DINERO (`analisis_15m_A3_politica_maker.py --curva [--neg]`, informes m15def_A3_curva_latencia*_07oct.txt): la curva del maker que cancela (CL+BN P90, con rebate 20 %) es PLANA de L=−130 a +300 ms (VALID −0,16/−0,26 $/merc, FINAL −0,62/−0,75; KEEP −4,19/−3,77) → valor de 1 ms ≈ 0 $ con las reglas actuales; ni VPS junto al origen ni feed más rápido desbloquean dinero hoy. La pérdida está en rellenos tóxicos no anticipados por Binance P90 1 s → palanca = §14 (EV maker por estado: A2 AUC 0,84, vol/spread).** BTC +0,72 $/merc con rebate (+0,81 a L=−130), VALID+FINAL. Mejoras gratuitas que sí proceden: prefirmar órdenes (firma P50 6 / P99 135 ms con carga) y repartir el WS de BTC (cola P90 423 ms). |
| 6 | Si 150 ms inamovibles: A pre-posición, B resting, C orden en vuelo, D ejecución condicional, E buffer de inventario, F maker-first, G híbrido, H tercera pata / hedge sintético | **HECHO 07-Oct (mapa; la medición de cada una vive en §10-16).** CONFIRMADO con órdenes reales: TODA orden tomadora (FOK/FAK, cruce o no) paga ~145 ms; una GTC post-only entra en ~34 ms y se cancela en ~30 (ida) → la latencia deja de ser cuello de botella solo si la exposición se toma como MAKER. Estado por arquitectura: **A/B/D/F (resting, maker-first, condicional)**: la vía con ventaja estructural (~200 ms sobre el tomador ante el mismo dato); hoy pierde por toxicidad, no por latencia (curva plana §5) → §10 cola, §13 GTC/GTD, §14 EV(estado). **C (orden en vuelo)**: una FOK no se puede cancelar en su ventana de retraso → disparar antes del evento exige un precursor; B1 dio AUC ≤0,5 → solo con precursor nuevo (§20-23). **E (inventario)**: con juegos YES+NO acuñados (split 1 USDC → 1 YES + 1 NO; sin comisión de trading, coste de gas/relayer SIN VERIFICAR) una "compra" se convierte en VENTA en reposo del lado contrario como maker → evita la segunda ejecución crítica de B1 y permite cotizar ambos lados con inventario (§16-18). **G (híbrido maker A + taker B)**: B1 paso 2 (maker en ambas patas cerca de la frontera) n=4 +2,00 $ en 15 h, sin BTC +0,30 → reabrir con cola real y rebate (§16). **H (tercera pata)**: Binance futuros NO responde desde el VPS; Hyperliquid perp accesible (on-chain) pero llega 344-989 ms tarde → solo válido como cobertura lenta de inventario del maker, no como pata rápida (§16). |
| 7 | MICROSTRUCTURE STATE VECTOR por timestamp (bid, ask, spread, depth, microprice, imbalance, pendiente, cola, agotamiento, reposición, cancelación, cambios de cotización, intensidad, flujo, liquidez rancia) | pendiente |
| 8 | Spread mining (NET EXECUTABLE EDGE) | pendiente |
| 9 | Depth mining | pendiente |
| 10 | Queue position alpha: P(fill | cola, estado), EV(fill | cola, estado); nunca fill por "tocar" | pendiente |
| 11 | FOK exhaustivo; FOK vs LIMIT/GTC/GTD | pendiente |
| 12 | FAK (parciales, residual, hedge, cancelación, pérdida esperada) | pendiente |
| 13 | GTC/GTD: resting, órdenes con expiración, pre-posición, expiración por evento, cancelación dinámica | pendiente |
| 14 | Maker alpha: MAKER EV(state) (informed MM, skew, inventario, selección adversa, cancelación, repricing, protección FV, liquidez por evento) | pendiente |
| 15 | Taker selectivo (edge enorme, sobrevive 215 ms, ventana larga, profundidad, segunda fase, shock) | pendiente |
| 16 | Hybrid (maker A + taker B, …, inventario + maker, maker + hedge, taker + salida pasiva) | pendiente |
| 17 | Arbitraje matemático: TODAS las restricciones (YES+NO, excluyentes, exhaustivos, expiries, anidados, mismo subyacente, cross-market, sintéticos) → GUARANTEED PAYOFF y MINIMUM EXECUTION EDGE | pendiente |
| 18 | Arbitraje de ejecución (dinero sin predecir el ganador) — PRIORIDAD | pendiente |
| 19 | 5m ↔ 15m distinto de B1 (5m lidera 15m, 15m lidera 5m, transmisión de vol/flujo, ejecución cross-horizonte, hedge condicional, una pata) | pendiente |
| 20 | Binance microestructura → Polymarket microestructura (cuándo retirar/poner/cruzar) | pendiente |
| 21 | Chainlink: llegada de ticks, frecuencia, desviación, vol, saltos, periodos rancios, discrepancia — INFORMATION/EVENT TIMING | pendiente |
| 22 | CROSS-VENUE STATE (Binance + Chainlink + 5m + 15m + libro + flujo) | pendiente |
| 23 | Event study exhaustivo (pre/evento/post: continuación, reversión, vacío, repricing, spread, cancelación maker, oportunidad taker) | pendiente |
| 24 | Leg 1 / 2 / 3: cuál tiene mejor PnL neto capturable | pendiente |
| 25 | Tail alpha clasificada ANTES del resultado | pendiente |
| 26 | Money-first mining (€ por operación/día/capital/hora/mercado) | pendiente |
| 27 | EXECUTION OPPORTUNITY MODEL: P(oportunidad ejecutable | estado), E[€ | estado] | pendiente |
| 28 | Failure-aware (no fill, parcial, precio rancio, cancelación, rechazo, latencia, selección adversa, legging) | pendiente |
| 29 | LATENCY → MONEY CURVE: EDGE(0,10,25,50,100,150,200,215,250,300 ms) | pendiente |
| 30 | VALUE OF 1 MS (€/ms) → priorizar inversión técnica | pendiente |
| 31 | Soluciones de latencia con ANTES/DESPUÉS/P50/P95/P99/PnL desbloqueado | pendiente |
| 32 | Pre-positioning para alfas con vida < latencia | pendiente |
| 33 | ML solo si gana en PnL neto a reglas/umbrales/lineales/ligeros | transversal |
| 34 | 200 hipótesis = 200 MECANISMOS económicamente distintos | pendiente |
| 35 | 200 → 50 → 20 → TOP 10 (PnL neto, robustez, capacidad, latencia, capital, complejidad, riesgo) | pendiente |
| 36 | Discovery / Validation / OOS / Holdout / Paper forward; multiple testing, data snooping, PBO, DSR, permutación, bootstrap, Reality Check/SPA | transversal |
| 37 | Leave-one-market-out (BTC, ETH, SOL, XRP, DOGE, principal fuera) | transversal |
| 38 | Leave-one-regime-out (baja/alta/normal/shock/terminal) | transversal |
| 39-40 | Forense de datos; precio ejecutable en la decisión + latencia | transversal |
| 41 | Capacidad: MAXIMUM EXECUTABLE CAPITAL, PnL neto vs tamaño | pendiente |
| 42 | Vigía forward por superviviente (señal, estado, acción, edge teórico/ejecutable, latencia, fill, parcial, fees, slippage, PnL, inventario, drawdown) | pendiente |
| 43 | Paper mode conservador: predicho vs realizado | pendiente |
| 44 | Micro-live solo con OOS+, paper+, latencia medida, PnL reconciliado, kill-switches, límites (+ checklist 6 cat. + /code-review + OK Javi) | pendiente |
| 45 | Kill-switches SYSTEM (datos malos, feeds rancios, pico de latencia, orden duplicada/huérfana, estado roto) y STRATEGY (colapso del edge, drawdown, P(fill), slippage) | pendiente |
| 46 | Monitorización en tiempo real | pendiente |
| 47 | Criterio de éxito (8 condiciones) | — |
| 51 | OUTPUT FINAL: TOP 10 con los 26 campos (mecanismo, ineficiencia, inputs, señal, tipo, latencia requerida/actual/solución, tipo de orden, entrada, salida, hedge, sizing, fees, slippage, P(fill), PnL neto, PnL/día, capacidad, drawdown, OOS, estrés, modos de fallo, kill switch) | pendiente |

## Lo que ya se sabe y entra como punto de partida (no se repite, se cita)
- Misión 15m 06-Oct (rondas 1-3, A1-A3, B, C): 0 alpha tomador a ≥215 ms ni a 45 s; maker pasivo −4,4/−5 $/mercado;
  maker que cancela −0,43 (BTC +0,36/+0,24, idea rastreable); repricing a 215 ms AUC 0,84; se anticipan vol y spread
  (misión `project_mision_15m_anticipar_vol_liquidez_07oct`). Informes `informes/m15_*`.
- B1 arbitraje anidado: edge real pero fugaz (patas mueren P50 38 ms, consumidas por arbitrajistas <50 ms), CERRADO en
  su forma reactiva; B2 pata 5m barata en vigía forward v3.
- Latencia medida 05-Oct: firma 5,1 ms caliente; POST /order (FOK a 0,02, no marketable) 226 ms P50 (p95 702) con
  taker delay 150 ms; lote 2 patas 254 ms; Binance→recepción p50 138 ms; Polymarket exchange→recepción p50 26 ms.
  Base 03-Sep (taker delay 50 ms): POST 180 ms P50. ⚠ +46 ms con +100 ms de taker delay → ¿el retraso se aplica a
  órdenes no marketables? Auditar (§3).
