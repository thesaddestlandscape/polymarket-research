# Catálogo de hipótesis — el 15m como activo autónomo (06-Oct)

Convención: cada hipótesis es una señal con signo (+ = comprar YES, − = comprar NO) evaluada como TOMADOR al ask real a
+215 ms, a resolución oficial y en ida y vuelta (30/60 s). **[R1]** = probada en la ronda 1 (`analisis_15m_mineria.py`
sobre `m15_maestro_06oct.csv`, ~20 h de registro ms, descubrimiento 60 % / prueba 40 % temporal). **[P:x]** = pendiente,
falta el dato x. Ninguna hipótesis "pendiente" cuenta como descartada.

## M1. Desequilibrio del libro (nivel 1)
1. [R1] desequilibrio de tamaños YES. 2. [R1] desequilibrio NO invertido. 3. [R1] desequilibrio neto YES−NO.
4. [R1] microprecio YES − mid. 5. [R1] microprecio NO invertido. 6. [P:L2 del 15m] pendiente del libro (niveles 2-5).
7. [P:L2 del 15m] desequilibrio de profundidad a 5c. 8. [R1] suma de asks < 1 con desequilibrio.
## M2. Agotamiento / reposición de cola
9. [R1] agotamiento del ask YES vs NO 1 s. 10. [R1] ídem 5 s. 11. [P:L2] reposición tras agotamiento.
12. [P:L2] ráfaga de cancelaciones en niveles 2-3. 13. [R1] secuencia flujo comprador + agotamiento.
## M3. Flujo agresor agregado
14-16. [R1] flujo comprador YES−NO 1/5/30 s (impulso). 17-19. [R1] el mismo invertido (reversión).
20. [R1] intensidad de operaciones × dirección del precio. 21. [P:firehose ms] tamaño medio agresor.
22. [P:firehose ms] concentración (nº de wallets distintas). 23. [P] burstiness (varianza de llegadas).
## M4. Impulso / reversión del propio precio
24-25. [R1] impulso del mid 1/5 s. 26-27. [R1] reversión 1/5 s. 28-29. [R1] aceleración / aceleración invertida.
30. [P] persistencia de rachas de ticks. 31. [P] distancia al máximo/mínimo de la ventana.
## M5. Edad del quote (hazard de repricing)
32. [R1] edad asimétrica ask YES vs NO. 33. [R1 dataset] hazard de cambio vs edad (estudio descriptivo).
34. [P] edad × spread. 35. [P] edad × tiempo al cierre. 36. [P] edad del bid vs ask como presión.
## M6. Fair value (Chainlink + referencia oficial + σ)
37. [R1] FV − mid. 38. [R1] FV − ask ejecutable (YES vs NO). 39. [R1] z directo. 40. [R1] z invertido.
41. [R1] distancia a la referencia en bps. 42. [P] FV con TWAP proyectado (no spot) en los últimos 60 s.
43. [P] FV con σ implícita del propio mercado. 44. [P] FV con colas gruesas (t de Student).
## M7. Chainlink como precursor
45-46. [R1] impulso Chainlink 5/30 s. 47-48. [R1] reversión Chainlink 5/30 s. 49. [R1] Chainlink se mueve y el
libro no (adelanto). 50. [R1] Chainlink se mueve con el mid quieto >3 s (secuencia). 51. [P] saltos discretos
de Chainlink (>2σ en 1 tick). 52. [P] edad del último tick Chainlink (oráculo parado).
## M8. 5m → 15m (sin arbitraje)
53-54. [R1] impulso del 5m 1/5 s. 55-56. [R1] adelanto del 5m sobre el 15m 1/5 s. 57. [R1] el 5m se mueve con el
15m quieto. 58. [P] spread del 5m como estrés. 59. [P] flujo del 5m.
## M9. Binance
60-62. [R1] impulso Binance 1/5/30 s. 63-65. [R1] reversión Binance. 66. [R1] Binance adelanta al libro.
67. [P] desequilibrio de aggTrade (comprador vs vendedor). 68. [P] CVD perp (fetcher ya en cron).
## M10. Calibración (precio = probabilidad)
69-78. [R1] comprar YES en cada tramo de 10c. 79-88. [R1] comprar NO en cada tramo de 10c.
89. [P:12 días precierre_multioffset] calibración tardía con asks reales. 90. [P:firehose mes] calibración con prints.
## M11. Tiempo hasta el cierre
91. [R1] FV en los últimos 120 s. 92. [R1] impulso en los últimos 120 s. 93. [R1] reversión en los 3 primeros min.
94. [P] deriva de resolución (último minuto). 95. [P] repricing terminal tras el último tick Chainlink.
## M12. Régimen de volatilidad
96. [R1] FV con σ alta. 97. [R1] FV con σ baja. 98. [P] shocks (|Binance 1 s| > p99).
## M13. Eventos
99. [P] respuesta del 15m a saltos de Binance >2 bps (estudio de evento, magnitud/persistencia/reversión).
100. [P] respuesta a liquidaciones (Bybit/Binance perp). 101. [P] respuesta a saltos de Chainlink.
## M14. Segundo orden
102. [P] X → cambio de volatilidad del 15m. 103. [P] X → cambio de liquidez (spread/tamaño).
## M15. Secuencias
104. [R1] flujo + agotamiento. 105. [P] operación → cancelación → cambio de quote. 106. [P] movimiento 5m →
cambio de libro 15m → continuación.
## M16. Regímenes del 15m
107. [P] señal × régimen (tendencia/reversión/ilíquido/terminal) con regímenes definidos en descubrimiento.
## M17. Ejecución como maker
108. [P] cada señal positiva monetizada como puja maker en vez de tomador. 109. [P] maker en el lado contrario.
## M18. Modelo combinado
110. [R1] gradient boosting con todos los rasgos (entrenado solo en descubrimiento), decil superior.
## M19. Colas de dinero
111. [R1 desglose] concentración del PnL (top 1/5/10 %) y si es predecible fuera de muestra.
## M20. Controles negativos
112. [R1] cada regla con la señal permutada dentro del minuto del contrato (20 permutaciones).
