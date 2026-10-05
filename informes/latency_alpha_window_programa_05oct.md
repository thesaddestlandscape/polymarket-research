# Programa: monetizar la ventana Binance → Polymarket (Latency Alpha Window) — 05-Oct-2026

Encargo de Javi (05-Oct): no "llegar antes", sino **cobrar la desalineación mientras existe**. Este documento fija
definiciones, instrumentación, mediciones, hipótesis y criterios de muerte ANTES de mirar los datos.

## 0. Reencuadre (hechos medidos, no supuestos)
- Los **150 ms** son el *taker delay* que Polymarket aplica a toda orden que cruza (desde 04-Sep). NO son el retraso de
  Polymarket frente a Binance. Ese retraso es **W = t2 − t0** y nunca se ha medido con reloj de exchange.
- Nuestra cadena tomadora: Binance → nosotros p50 **138 ms** (p90 165, p99 545; aggTrade T→recepción, 05-Oct) + decisión
  + POST al CLOB ~180-276 ms + 150 ms de retraso ⇒ ~**450-560 ms** tras t0.
- Lo que ya sabemos que NO funciona: comprar como tomador tras el salto/movimiento (5m/15m): H1-H4 forward −8,7/−20,5 %;
  1-3 bps (111 k eventos): EV ≤0 a +0,3/+0,6 s; ni a +0,15 s hay celda con IC90>0. El ask se mueve +2/+3,6c en 300 ms.
- Lo que eso implica: **alguien cobra esos 2-3,6c dentro de la ventana**. Por construcción del retraso de 150 ms solo
  pueden ser (a) makers que recotizan/cancelan antes de que les llegue el tomador retrasado, o (b) quien ya estaba
  posicionado antes de t0. Esos son los dos frentes principales.

## 1. Instrumentación (desplegada 05-Oct 15:54Z) y auditoría de tiempos
Registro `maker_ms_YYYY-MM-DD_<pid>.csv.gz` (datalogs, ~410 MB/día, 7 d), escrito por el hijo de `libro_estado_ws`:
| tipo | contenido | reloj |
|---|---|---|
| x | aggTrade Binance (6 monedas): precio, cantidad, comprador_es_maker | **T y E del exchange** + recepción |
| b | bookTicker Binance (mid y tamaños) | recepción |
| q | top Polymarket en cada cambio de PRECIO (bid, ask, tamaños) | exchange (ms) |
| h | top Polymarket muestreado 100 ms (con tamaños) | exchange |
| t | TODAS las operaciones del CLOB | exchange |
| k | token → moneda, marco, mercado, cierre, lado | — |
Auditoría de reloj: chrony sincronizado, desfase 2 µs, RMS 90 µs, dispersión ~1 ms; **cota de error ~21 ms**.
⇒ Buckets ≥10-25 ms sostenibles; **1-5 ms NO** (además desconocemos la precisión de los relojes de los exchanges).
Pendiente: (i) deriva Binance E vs recepción por hora (jitter); (ii) hora del exchange de Polymarket vs recepción
(¿lotes?, ¿desorden?); (iii) mensajes fuera de orden por conexión (ahora 18 conexiones).

## 2. Mediciones (M) — lo que pidió Javi, en orden
- **M1 Ventana W**: para cada evento Binance (t0 = T del primer aggTrade que completa un movimiento ≥k bps en ≤1 s),
  t1 = primer cambio de precio del top Polymarket en la dirección del movimiento (mercado vivo de esa moneda, 5m y 15m);
  t2 = cuando el mid de Polymarket alcanza el 90 % de su ajuste final a +5 s. Distribución P10…P99 + cola, por moneda,
  marco, tamaño del movimiento y hora.
- **M2 Mispricing(t)**: FV_Binance(t) = Φ(z) con z de (spot Binance − referencia de apertura TWAP) / σ√T; mispricing =
  FV − mid/ask de Polymarket, de t0−500 ms a t0+2 s en buckets 0-10/10-25/25-50/50-75/75-100/100-125/125-150/150-200/
  200-250/250-500 ms. ⚠ La referencia de apertura es Chainlink (TWAP [e−62, e−3]); usar la reconstruida desde RTDS por
  hora de RECEPCIÓN (trampa conocida: ws_timestamp = look-ahead de 1,36 s).
- **M3 PnL potencial(t)** al ask y al bid reales de cada bucket (tomador) y PnL de un bid/ask quieto (maker) que se rellena
  en ese bucket, con desenlace oficial.
- **M4 Pre-alpha** (t0−200…t0): ¿se mueve ya Polymarket? ¿hay precursores en Binance (aceleración, ráfaga de aggTrade,
  desequilibrio de tamaños del bookTicker, operaciones grandes del lado agresor, otras monedas)?
- **M5 P(fill) y E[PnL | fill]** del maker por distancia al top, cola delante, estado de Binance y latencia de cancelación.
- **M6 LAA(t)** = edge(t) − coste de llegar en t − fee − deslizamiento − selección adversa; instante en que cruza 0.
- **M7 Fuerza de la señal** → magnitud de la convergencia, duración de W y PnL neto (¿los movimientos grandes duran más que
  nuestra cadena?).
- **M8 Tramos**: tramo 1 (primer reajuste), 2 (continuación), 3 (estabilización); PnL de entrar en cada uno.

## 3. Hipótesis (54) agrupadas por mecanismo
**A. Pre-posicionamiento / ejecución anticipada (predecir t0 con ≥450 ms de antelación)**
A1 ráfaga de aggTrade agresor en BTC (n operaciones en 200 ms) precede movimientos ≥2 bps en 0,3-1 s · A2 aceleración del mid
(2ª derivada) · A3 desequilibrio de tamaños del bookTicker (bid/ask size) · A4 operaciones grandes (percentil 99) del mismo lado ·
A5 secuencias de 3+ aggTrade del mismo lado en <50 ms · A6 movimiento de BTC que aún no ha llegado a ETH/SOL (cadena cruzada) ·
A7 perpetuo/futuros de Binance como precursor del spot · A8 horas de publicación macro (eventos programados) · A9 apertura de vela
de 1 min/5 min (picos de volumen en el cambio de minuto) · A10 régimen de volatilidad: en ráfagas, P(movimiento) alta → pre-posición
barata en ambos lados.
**B. Maker que cobra la ventana (el retraso de 150 ms protege al maker)**
B1 bid en el mejor bid de ambos lados + cancelar el lado amenazado por Binance (simulador ya escrito) · B2 igual, pero recotizar
INMEDIATAMENTE al nuevo valor justo del lado favorecido (capturar el tomador lento que llega tarde) · B3 cotizar a FV_Binance ± margen
en vez de al mejor bid · B4 ensanchar en ráfaga, estrechar en calma · B5 inventario sesgado: menos tamaño en el lado que Binance
amenaza · B6 posición en la cola: entrar temprano en niveles que serán el nuevo top tras el movimiento · B7 solo en mercados con pocos
makers (spread ancho, poca profundidad) · B8 maker solo en 15m (más tiempo, menos competencia) · B9 maker con objetivo de PAR
(acumular YES+NO por debajo de 1) protegido por Binance · B10 devolución de comisión del 20 % al maker como colchón.
**C. Órdenes en reposo / condicionales (que solo se ejecuten durante la convergencia)**
C1 ask en reposo por ENCIMA del mercado en el lado que subirá: lo levanta el tomador que llega tarde (vendemos caro) · C2 bid en reposo
por DEBAJO en el lado que caerá: comprar barato el pánico del rezagado · C3 escalera de órdenes alrededor del FV · C4 "atrapar al
rezagado": tras el reajuste, órdenes al precio viejo que los tomadores retrasados todavía cruzan · C5 órdenes que se colocan en t0−x
(pre-posición pasiva) y se cancelan si no hay movimiento.
**D. Brecha de valor justo (FV gap) en lugar de "el movimiento"**
D1 comprar cuando FV_Binance − ask ≥ umbral adaptativo · D2 umbral en función de σ, tiempo restante, spread y profundidad · D3 solo
cuando la brecha PERSISTE ≥ nuestra cadena (450 ms) · D4 brecha con libro fino (poca profundidad = reajuste más lento) · D5 brecha en
el lado contrario (sobrerreacción de Polymarket → reversión) · D6 brecha medida contra el bid (vender lo que ya tenemos).
**E. Selección de eventos (solo las ventanas que sobreviven nuestra latencia)**
E1 movimientos ≥3/5/8 bps en ≤500 ms · E2 movimientos que siguen acelerando tras t0 · E3 cerca del umbral de la apertura (z≈0, máxima
sensibilidad de Φ) · E4 lejos del cierre (más tiempo para converger) vs cerca (más sensibilidad) · E5 horas de baja actividad de makers
(¿Asia?) · E6 monedas con makers lentos (DOGE/BNB muestran +3-3,6c de deriva: ¿más lentos o más volátiles?).
**F. Segundo y tercer tramo**
F1 entrar tras el primer reajuste cuando Binance sigue en la misma dirección (continuación) · F2 sobrerreacción del tramo 1 →
reversión · F3 el tramo 2 con confirmación de Binance a +500 ms · F4 salida pasiva en el tramo 3 (vender al bid que sube).
**G. Cadenas de adelanto (lead-lag)**
G1 BTC Binance → ETH/SOL Polymarket (dos saltos de retraso) · G2 5m → 15m del mismo activo (el 15m reajusta más lento) · G3 5m → 60m
(60m resuelve con la vela de Binance: sensibilidad directa) · G4 Polymarket de una moneda → otra moneda.
**H. Asimetría (riesgo acotado, ganancia de la convergencia)**
H1 entrar pasivo, salir tomador cuando converge · H2 entrar tomador en eventos extremos, salir pasivo · H3 tamaño parcial con salida
escalonada · H4 comprar el lado barato (≤0,20) como opción barata sobre el movimiento: riesgo = prima.
**I. Microestado de Polymarket como condición**
I1 mismo movimiento de Binance, distinto resultado según profundidad del top · I2 desequilibrio del libro de Polymarket a favor/en
contra · I3 operaciones recientes de tomadores grandes · I4 spread ancho = makers ausentes = ventana más larga · I5 libro "quieto"
(sin cambios en 2 s) = makers dormidos.

## 4. Reducción a mecanismos realmente distintos (los que se prueban)
| # | Mecanismo | Hipótesis | Por qué podría existir | Qué lo mata |
|---|---|---|---|---|
| 1 | **Maker protegido por Binance** | B1, B2, B5, B10 | el retraso de 150 ms deja al maker cancelar antes que el tomador | línea base −6/−10c y la cancelación a ≥200 ms no la lleva a >0 |
| 2 | **Maker que recotiza al FV** (cobra al rezagado) | B2, B3, C4 | tras t0 los tomadores lentos siguen cruzando precios viejos durante W | P(fill)×margen < selección adversa con lat ≥200 ms |
| 3 | **Ask/bid en reposo para el rezagado** | C1, C2, C3 | el tomador retrasado cruza nuestra orden ya colocada | rellenos que aciertan menos que el precio |
| 4 | **Pre-posición por precursores de Binance** | A1-A7, A10, C5 | si P(movimiento) a 0,45-1 s es predecible, la orden llega cuando ocurre | AUC del precursor ≤0,6 o EV al ask ≤0 |
| 5 | **Brecha FV persistente** | D1-D4, E1-E3 | algunas brechas duran más que nuestra cadena | ninguna celda con brecha a +450 ms y EV>0 |
| 6 | **Cadena cruzada** | A6, G1-G4 | el segundo eslabón reajusta más tarde | W del segundo eslabón ≤ nuestra cadena |
| 7 | **Selección por microestado** | I1-I5, B7 | makers ausentes = ventana larga | sin diferencia de W/PnL entre estados |
| 8 | **Tramos 2-3** | F1-F4 | menos competencia tras la confirmación | EV del tramo 2 ≤0 |
| 9 | **Asimetría (opción barata)** | H4, D5 | riesgo acotado a la prima | acierto < precio a igual brecha |
| 10 | **Híbrido maker/tomador** | H1-H3 | entrar barato pasivo, salir rápido | coste de ida y vuelta > convergencia |
Lo que NO se persigue como objetivo principal: bajar la latencia (complementario; ya medido Binance→nosotros 138 ms).

## 5. Protocolo de validación (obligatorio para todo resultado)
- **Causalidad**: cada decisión usa solo filas con hora ≤ t_decisión según el reloj con el que la habríamos visto (recepción
  para Binance; exchange para Polymarket + su latencia de entrega medida). Sin libro posterior, sin fills futuros.
- **Unidad**: el MERCADO (y el cierre si hay racimos entre monedas); IC90 por días; EV sin los 2 mejores días; ninguna moneda >60 %.
- **Estrés**: +10/+25/+50/+100/+150/+200/+300 ms en cada eslabón; deslizamiento +1/+2c; rellenos −25/−50 %; peor cola; cortes del WS.
- **Fuera de muestra**: reglas y umbrales fijados con los días 1-N, medidos en N+1..; walk-forward por día; holdout final.
- **Gate a dinero real**: n≥40 mercados, ≥5 días, EV ≥+0,10 €/€ (tomador) o >0 con IC90 por días >0 (maker, sin comisión),
  estrés +100 ms superado, checklist de 6 categorías + /code-review + OK de Javi.

## 6. Resultado obligatorio por estrategia ganadora
Ventana (W), mispricing, momento de entrada, tipo de orden, P(fill), convergencia cerrada, PnL neto, sensibilidad a latencia
(+10…+300 ms), capacidad, robustez OOS, mecanismo. Y la curva central: **PnL neto capturado dentro de la ventana por bucket
de latencia (0, 10, 25, 50, 75, 100, 125, 150, 200, 250, 500 ms)**.

## 7. Calendario (Stage 0-4 cierran 31-Oct)
- 06-Oct: auditoría de tiempos (i-iii) + M1 (W) + M2 (mispricing por buckets) con ~14 h de registro; simulador maker (mecanismo 1).
- 07-08 Oct: M4 precursores (mecanismo 4), M5 P(fill) (mecanismos 2-3), M7/M8; primeras curvas con 2-3 días.
- 09-10 Oct: estrés + fuera de muestra con ≥4-5 días; decidir los 1-2 mecanismos que pasan a dry-run ejecutor.
- Si algo maker pasa con lat ≥200 ms: pedir OK para medir NUESTRA latencia de cancelación con órdenes mínimas (5 acciones).

## 8. Misión 2 (Javi 05-Oct 16:05Z): QUIÉN captura la transición y cómo replicarlo
Regla grabada: **L_taker (150 ms, mecanismo de Polymarket) ≠ W (ventana de mercado, a medir)**. Nunca "hay 150 ms, llegamos tarde".
**Relojes (auditados 05-Oct)**: Binance T/E → recepción p50 138 ms (p90 165, p99 545); Polymarket exchange → recepción p50 26 ms
(p1 17, p90 360, p99 1,5 s; nunca negativo ⇒ relojes coherentes, mínimo = red). chrony ±1 ms (cota 21 ms). ⇒ W se mide con
hora de EXCHANGE en ambos lados; toda simulación de decisión usa hora de RECEPCIÓN (+ la cola de 360 ms-1,5 s de entrega).
**Registro desde 16:06Z**: q = cada cambio de precio O tamaño del top (cancelación vs relleno cruzando con t) + recepción; t + recepción.
**Quién (wallets)**: firehose `polymarket_activity_*.csv` (wallet, lado, precio, tamaño, hash; hora en s, ~0,9 s tarde) unido a las
operaciones t del registro por token + precio + tamaño (±2 s) ⇒ cada operación con wallet y ms; por hash: maker vs tomador.
**Mediciones nuevas**:
- W_primer, W_25, W_50, W_75, W_90, W_95, W_FV (convergencia a Φ(z_Binance)), W_residual (residual estadísticamente nulo); distribución completa.
- t0 = INICIO del movimiento (primer aggTrade de la racha), no su final; pre-alpha medido contra ese t0.
- Microcronología por evento (t−500 … t+500 ms): bid, ask, spread, tamaños del top, mid, microprice, operaciones, cancelaciones
  (caída de tamaño sin operación a ese precio), reposiciones.
- Movimiento 2-3,6c: distribución P10…P99, dependencia del tamaño del movimiento de Binance, velocidad, sobrerreacción, reversión.
- Stale Quote Window: t0 → cancelación/recotización del nivel obsoleto vs t0 → llegada del tomador (operación al precio viejo).
  % de veces que el maker se salva, % expuesto, precio y PnL de cada lado.
- Descomposición por evento: capturado por makers (cancelan/recotizan y luego rellenan mejor), por pre-posicionados (wallets con
  entrada < t0 en el lado ganador), por tomadores rápidos (operaciones al precio viejo en [t0, t0+W] y su PnL), y no capturado.
- Mapa de alpha por bucket (0-10 … 200-300 ms): Binance, Polymarket, mispricing, acción maker, acción tomador, PnL potencial.
- P(quote tóxica en 100-200 ms | microestado Binance + Polymarket) → cancelar/mantener/mover.
- EV por mecanismo condicionado al estado: tomador (solo si W esperado > L_taker + costes), maker informado vs maker sin Binance
  (la diferencia = valor de la información de Binance), pre-posición, segundo tramo, no operar ⇒ argmax.
- Cadena A → Binance → Polymarket: candidatos A = futuros/perpetuo de Binance, otros venues spot, otras monedas (BTC → alts).
**Las 15 preguntas finales** (W, distribución, movimiento en W, parte atribuible a Binance, quién, ¿makers?, ¿pre-posicionados?,
¿señal previa?, ¿replicable el maker?, ¿pre-posición?, cuándo tomador, cuándo maker, cuándo ya posicionados, PnL por mecanismo,
robustez) se responden con estas mediciones y el protocolo del §5. Primera lectura exploratoria (30 min): t1 mediana 147 ms,
W_50 mediana 219 ms (p25 106, p75 376, p90 792), W_90 mediana 399 ms; 18 % de eventos con W_50 > 500 ms (candidatos a tomador selectivo).

## 9. Frente 7 — rescate del TOMADOR en 5m/15m (Javi 05-Oct 16:20Z: "tenemos que ir a por él")
Cerrado solo el tomador indiscriminado tras el salto. Pistas: 18 % de eventos con W_50 >500 ms; ~49 % de movimientos de 1 bps no
mueven Polymarket ≥1c a 5 s. Vías (EV al ask real a recepción + nuestra cadena + 150 ms, desenlace oficial, causal):
1) selectivo por clase de evento observable al decidir; 2) anticipado por precursores de Binance (orden antes de t0);
3) segundo tramo; 4) cadena cruzada BTC → alts; 5) desglose de nuestra cadena (138 + decisión + POST 180-276 + 150) y valor de
recortarla (órdenes prefirmadas, conexión abierta, VPS cerca del CLOB = decisión de Javi) leído sobre la curva de W.
