# Misión 15M V3 — tabla de salida (07-Oct-2026)

Pregunta de la misión (Javi, 07-Oct): el maker de 15m pierde ~6 c por relleno. ¿Quién obtiene esa información antes, cómo, y podemos convertir el relleno, la cola o una fuente más rápida en ventaja?
Datos: registro ms 05-06 Oct (caché `m15_ms_cache`, reloj de RECEPCIÓN), on-chain 05-06 Oct (`m15_onchain`), captura de 7 venues 14:30Z 07-Oct, `trades.csv` real 28-Jul..07-Oct. Periodos DISC / VALID / FINAL (FINAL bloqueado salvo confirmación).

Estados: **NO EDGE ECONÓMICO** (se observa y se ejecuta, pero el EV es ≤0) · **NO OBSERVABLE** (la información existe pero no nos llega a tiempo) · **NO EJECUTABLE** (EV>0 a la latencia de otros, no a la nuestra) · **NO DATA** (falta muestra o fuente) · **ABIERTO**.

| # | Hipótesis | Datos | Información | Latencia | Ejecución | OOS | Estado |
|---|---|---|---|---|---|---|---|
| F0 | La cola de latencia del feed (P90 ~420-600 ms) es nuestra | 110 k msgs aislado vs producción; 1,36 M msgs con 4 lectores | El sello del WS es un sello de LOTE (hasta 470 ms antes del evento) | Pipeline propio P50 −3 ms; cola por conexión (corr 0,41); 4 conexiones P90 162→57 ms aislado | En producción, 2 réplicas: 5m P90 980→728, 15m sin mejora | — | Cerrado: la cola NO es nuestra. Réplicas APARCADAS (sin orden por token; 2 code-reviews) |
| F1 | El −6 c llega después del relleno (atacable cancelando) | 159 k órdenes virtuales | Salto DISCRETO simultáneo al relleno (mid ya −5/−6 c en el instante) | Post-relleno solo ~0,5 c más | Cancelar tras el relleno no sirve | DISC/VALID/FINAL | NO EDGE ECONÓMICO |
| 15-17 | Un actor concreto barre a los makers | 156.656 órdenes tomadoras on-chain, 97,9 % emparejadas | Ecosistema: 2.863 wallets, top10 = 33 % del volumen barrido; los mayores barredores ≈0 o negativos a resolución | — | No hay a quién "seguir"; las persistentes ganan por valor a resolución, no por velocidad | 2 días | NO EDGE ECONÓMICO (para copiar) |
| 24-26a | Binance precede a los barridos | Igual + x del registro (recepción) | Solo 11 % de los barridos con ≥1 bp en 500 ms previos | Tomadores con Binance previo +0,088 €/€ a SU latencia | A la nuestra (+250-400 ms) cerrado por la trampa del ask | — | NO EJECUTABLE |
| 24-26b | Otras monedas del mismo cierre (cross) preceden | Igual | Cross ≥2 c en 2 s: 33 % de barridos vs 12,6 % del resto | — | Tomador a +250 ms: negativo (salvo celda U≥0,05 n=69, 1 de 12) | — | NO EDGE ECONÓMICO (tomador); U≥0,05 y BTC ABIERTO rastreable |
| 24-26c | Chainlink RTDS precede | Igual | 6 % vs 4,8 %; solo pesa en T-180 s | — | Terreno de PRECIERRE (ya live) | — | NO EDGE ECONÓMICO (nuevo) |
| 24-26d | Otro venue (Coinbase, OKX…) precede | Captura 7 venues 30 min (2.182 órdenes) | Algún venue ≥1 bp en 500 ms: 25,5 % de barridos vs 12 %; sin Binance: Coinbase 8,5 %, OKX 9,7 % | Coinbase antes que Binance 7/10 eventos | — | — | NO DATA (captura de 3 h pendiente de analizar) |
| 24-26e | Pyth directo / Band | — | Hermes exige clave (401); Band agrega CEX en cadena (segundos) | — | — | — | NO DATA (Pyth) / descartado por diseño (Band) |
| 22 | Cancelar el bid cuando cross se mueve en contra (defensa) | 159 k órdenes virtuales | Señal en el 95 % de las vidas de orden | Cancelación 60-125 ms medida | "Cancelar para siempre" = veto degenerado; prueba justa (2 s previos): no discrimina | DISC/VALID/FINAL | NO EDGE ECONÓMICO |
| F2a | Algún estado (fase×spread×desequilibrio×banda) tiene EV de maker >0 | 51 celdas DISC con ≥40 rellenos | — | — | 0/51 con IC90>0 (azar 2,6) | DISC→VALID | NO EDGE ECONÓMICO |
| F2b | Cotizar 1-3 ticks bajo el mejor bid compensa | Órdenes virtuales k=0..3 | El salto que te rellena crece con k | — | EV por relleno ≈ −6 c para todo k | DISC y VALID | NO EDGE ECONÓMICO |
| F3a | Fase previa a la ventana mal cotizada (precio justo 0,50) | 589 mercados, 10 min antes | Libro centrado (P5-P95 0,48-0,515); desvíos en los últimos 10-30 s, informados | — | Comprar el lado barato: −3,5/−4,7 c por acción | 2 días | NO EDGE ECONÓMICO |
| F3b | Apertura / terminal / liquidación | Piezas existentes | Φ(z) sobreconfiado; terminal = PRECIERRE; post-cierre = "ya decidido" | — | — | — | Cubierto por otras piezas |
| F5 | La FOK que se llenó es un fallo del exchange | Ledger + on-chain + registro ms | Compra por importe + libro REST de ~1,5 s; el WS ya mostraba ask 0,06 | Envío→casado 210-235 ms | Semántica entendida | — | Cerrado (reconciliado) |
| F5b | Rellenarse por debajo del plan es un descuento (dinero real) | 346 trades reales | Re-quote con ask ≥1 c bajo el plan: −37,28 €, n=73, p=0,0002, 31 días | — | Guarda candidata esquivable re-disparando | Forward pendiente | ABIERTO: registro en sombra desplegado 07-Oct 22:15Z; decidir hacia 14-21 Oct |
| G | Un VPS más cerca del CLOB cambia la ecuación | — | — | Nuestro camino de orden ~215-250 ms; taker delay 150 ms estructural | — | — | NO DATA — decisión de Javi |

## Lectura económica
- En 15m, la información que barre a los makers llega al mercado **con el propio barrido**. Las fuentes que podemos ver (Binance, cross-moneda, Chainlink, venues) explican como mucho una parte, y a nuestra latencia no se convierten en EV positivo ni como tomador ni como maker defensivo.
- No es "el 15M es eficiente": con nuestra latencia y nuestras fuentes NO es explotable. Los dos huecos que siguen abiertos son de **ejecución propia**, no de alfa del mercado:
  1. **F5b**, la selección adversa en nuestros propios re-quotes: dinero real, −37 € en 73 trades, hoy en medición en sombra.
  2. **Latencia física (G)**, que solo resuelve un cambio de infraestructura.
- Rastreables con n bajo: cross U≥0,05 (n=69) y BTC-cross (n=308), a re-correr con días nuevos del registro ms antes de que rote (4 días); venues con la captura de 3 h.
