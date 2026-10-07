# Misión 15M V3 — Fase 9: 20 mecanismos causales (07-Oct-2026)

Criterio de la lista, tras la tabla de salida (`m15v3_tabla_salida_07oct.md`): a nuestra latencia no hay ventaja informativa en microestructura. Por eso se priorizan mecanismos que NO dependen de llegar antes: estructura de la regla de resolución, información conocida antes de la ventana, ejecución propia y programas de Polymarket.
Estados: 🪦 falsado · ⏳ forward/rastreable · 🔬 por falsar (con el dato y el script indicados) · ❌ descartado por diseño.

| # | Mecanismo causal | Por qué podría pagar | Estado / evidencia |
|---|---|---|---|
| M1 | Sesgo base de Up en 15m (TWAP con empate a favor de Up) | El libro está centrado en 0,50 antes del inicio | 🪦 P(Up) 0,503-0,513 por moneda, IC90 incluye 0,5 (21 días, 11.802 ventanas) |
| M2 | **Reversión tras una ventana grande** (sobrerreacción a 15 min) | Libro centrado → si el desenlace previo predice, se compra antes del inicio | ⏳ **Hipótesis congelada H-REV15** (abajo): >30 bps → la reversión acierta 55,1 % IC90 (52,7-57,5 %), n=2.136; pero el ask de la reversión ya está a ~0,53 → EV ≈ +0,4c, IC incluye negativo. 05-06 Oct al ask real: 66,7 %, EV +0,12, n=48 (poco) |
| M3 | BTC previo → alts en la ventana siguiente | Arrastre cross-moneda | 🪦 apostar contra BTC 52,1 % (IC 50,7-53,5): por debajo del listón de 52,5 % |
| M4 | Hora del día | Flujos institucionales (apertura USA, Asia) | 🪦 ninguna hora pasa Bonferroni (22h 57,3 %, IC99,6 0,492-0,650) |
| M5 | Fase previa mal cotizada | Precio justo 0,50 sin referencia | 🪦 Fase 3: desvíos informados, −3,5/−4,7c |
| M6 | Cubrir el relleno del maker con el lado contrario | Fijar el par | 🪦 Fase 6: −6,7/−7,7c |
| M7 | Cotizar fuera del mejor bid | Comprar el salto más barato | 🪦 Fase 2: −6c por relleno para todo k |
| M8 | Estados con EV de maker >0 | Fase × spread × desequilibrio × banda | 🪦 0/51 celdas |
| M9 | Cross-moneda como precursor (tomador o defensa) | Factor común | 🪦 tomador negativo; defensa no discrimina. U≥0,05 y BTC rastreables |
| M10 | Nuestra selección adversa en el re-quote | Rellenarse bajo el plan = el mercado se movió en contra | ⏳ dinero real −37 € (n=73, p=0,0002); registro en sombra desde 07-Oct 22:15Z |
| M11 | Señales cuyo ask SUBIÓ algo tras el plan ganan más | Espejo de M10: confirmación del mercado | 🔬 BUY_YES ask +0,5/+2,5c: n=20, 70 % de acierto pero −0,112 €/€ (precio más caro). Falsar con el registro en sombra (mismo dataset) |
| M12 | Recompensas de liquidez (`rewards r: mi 50, ma 4,5`) + rebate 20 % a un maker LEJOS del mid | Cobrar sin rellenarse (o rellenándose poco) | 🔬 P21 reabierto; falta la fórmula de reparto real y el pool diario por mercado (dato de Polymarket) |
| M13 | Mint/merge: suma de bids YES+NO < 1 en libros finos | Arbitraje de construcción | ❌ la suma P + ask contrario ya es 1,04 (Fase 6); pares refutados en 2 patas |
| M14 | Regla TWAP: los últimos 3 s no cuentan (ventana [e−62, e−3]) | Desenlace conocido ~3 s antes de lo que cree el que mira el spot | ⏳ es la base de PRECIERRE/NAIVE (live). Nada nuevo |
| M15 | Desenlaces en racimo entre monedas en el mismo cierre | Correlación → tamaño y kill por cierre, no por mercado | ✅ ya regla (IC por cierre). Sin alfa nueva |
| M16 | Cambio de régimen de volatilidad → spread de 15m tarda en ajustarse | El maker se queda barato en volatilidad nueva | 🔬 misión "anticipar vol/liquidez" (|mov|→|mov 60 s| +0,125): solo defensa, sin alfa demostrada |
| M17 | Wallets persistentes que ganan por VALOR a resolución (0x32ed / 0xc2ad, ~33 $/orden, 3 monedas) | Modelo de valor, no velocidad → copiable con retraso | 🪦 OOS (selección 05-Oct, prueba 06-Oct, `analisis_15m_v3_fase9_copia_valor.py`): 13 wallets, 1.072 copias; ellas mismas −1,0c el 06; copia al ask real −2,2/−2,4c a +1/5/10 s (IC90<0), −1,8c a +30 s; wallet top 18 % |
| M18 | Mercados de 1 h que resuelven con la vela 1H de Binance (no TWAP) | Regla distinta, Binance conocido al ms | 🔬 tomador 60 min con regla congelada (Φ(z_Binance) − ask ≥ 0,05 a T-5..T-1 min), ya registrado en `project_maker_cancelacion_binance_05oct`; falta el análisis |
| M19 | Up/Down DIARIO (6 monedas, 12:00 ET) | Pocos participantes, cierre conocido 2 h antes | ⏳ `updown_diario_fase0.py` captura desde 30-Sep; falta el vigía (≥5 días ya disponibles) |
| M20 | Desequilibrio entre el 5m y el 15m que cierran juntos (valor relativo) | Garantía estructural de la pata | ⏳ vigía forward pata 5m barata v3 (OOS desde 06-Oct) |

## H-REV15 (congelada 07-Oct ~19:45Z; no se reajusta)
Regla: si la ventana 15m de una moneda que acaba de cerrar se movió > 30 bps (TWAP60 oficial reconstruido con [e−62, e−3] s), comprar el lado de la REVERSIÓN de la ventana siguiente de esa misma moneda al ask real a inicio−20 s, solo si el ask ≤ 0,55. Stake fijo; desenlace oficial.
Gate: n ≥ 40 eventos FORWARD (desde 08-Oct), ≥ 10 días, EV ≥ +0,05 €/acción con IC90 por días > 0, ningún día > 30 % del PnL, sin una sola moneda > 50 %.
Datos: el registro ms (libro, rota a 4 días) + `chainlink_*.csv`. Hace falta un vigía diario (pendiente del OK de Javi: proceso nuevo, cron diario, sin dinero).
