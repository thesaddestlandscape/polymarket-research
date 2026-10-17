# Libro de cuentas del objetivo 5m barato — 200.000 €/año netos como SUMA de subestrategias

Lo mantiene `cheap5m-objetivo-200k` (o `cheap5m-risk-economics` / el chief). Solo cuenta como ingreso lo que está en el
peldaño ≥5 de `FLUJO_DE_TRABAJO.md` (micro-real, live, rampa) con su gate superado; todo lo demás va en "potencial" y
etiquetado. Toda cifra con fecha, n, IC90 por días y fuente. **EV siempre ponderado por € (Σpnl/Σcoste).**

## Resumen — 17-Oct 14:10Z (1ª pasada, hecha por el chief: los agentes se cortaron por cuota)

| | €/año |
|---|---|
| **Ingreso validado (peldaño ≥5)** | **0** |
| Potencial conservador (lo que ya está en forward y no ha fallado) | 0 |
| Potencial optimista NO validado (techos poblacionales, ver filas) | ~60-65 k (H43 R5K a K=50) + ~10-15 k (maker de banda) — solapados en parte |
| **Hueco hasta 200 k€** | **200.000** |

Qué falta, en orden: **(1) edge propio medido con dinero real** (nada ha llegado al peldaño 5); **(2) capacidad**: el techo
optimista de lo mejor conocido (R5K) es ~1/3 del objetivo a K=50; **(3) capital**: principal 39,66 $ libres + 3,68 $ en posiciones (balance_real.json 14:30Z), dedicada 19,6 $ (tope de
pruebas 5 €); toda rampa es decisión de Javi.

## Subestrategias

| Subestrategia | Peldaño / estado | EV/€ ponderado (IC90) | n / días | Capacidad | Anual (cons / base / opt) | Solape | Siguiente prueba |
|---|---|---|---|---|---|---|---|
| **H43 R5K** (maker tras 5.000 acc acumuladas, BTC) | 2 · EXPLORATORY (24 celdas miradas) | +0,212 (cierre +0,10/+0,33), sin 2 mejores días +0,141, sin top-20 +0,117 — POBLACIÓN, cola optimista | 1.010 unidades / 11 días (06-16 Oct) | ~92 unidades/día × ~9 $ (K=50) ≈ 830 $/día de coste | 0 / 0 / ~65 k€ (si capturásemos el +0,21 en todas a K=50); K=200 +0,222 → techo mayor, cola sin medir | con H35/maker de banda (mismos mercados) | vigía forward diario 09:30Z (desde 17-Oct; ≥40 unidades en ≥10 días); micro-órdenes P1 orientadas a R5K |
| **Maker de banda** (línea base: unirse al bid 0,10-0,30) | 2 · línea base | población +0,064; **nuestras primeras 5 acc ≈+0,007** (+0,042/+0,031/+0,009/−0,054, 10-13 Oct); rebate ≈+0,011 sin verificar en 5m | ~2.000 unidades/día | ~2.200 $/día a 5 acc en todos los mercados | 0 / 0 / ~10-15 k€ | todas las maker | se mide dentro de las micro-órdenes P1 (es la línea base a batir) |
| **H35 DEEP_PEG** (puja 1-2 ticks bajo el top) | 3 · PARTIAL (15-16 Oct pendientes por memoria) | ALL +0,022 (1 día OOS); ETH +0,186, XRP +0,102, BTC −0,011; sin top-5 mercados casi todas <0 | OOS 14-Oct, 515 rellenos | — | 0 / 0 / ? | maker de banda, R5K | completar 15-16 Oct (h35_15_16.sh); recalcular ponderado; micro-real ETH/XRP |
| **Modelo de colocación** (cuándo/dónde pujar) | 1 · PENDING (agente cortado) | — | — | — | — | todas las maker | dataset en curso (DESC 05-10 / OOS 14-16; 11-13 excluidos por ser días de hallazgo de H35) y batir la línea base en ≥+0,05 |
| **H39 MM-REPOSO** (pares rotando, como las ganadoras) | 1 · PENDING | ganadoras on-chain +1,1/+1,6 %/€ (2 wallets 7/7 días OOS); mediana de las PAIR ≈0 | — | — | — | maker | tras el modelo de colocación (mismo motor) |
| **V4** (pata 5m barata como tomador) | 4 · FORWARD congelado, 4/10 gates, DRIFT | +0,21 comunicado (por señal ejecutable) | 17 ejecutables / 9 días | ~2 señales/día | 0 / 0 / pequeño | — | seguir forward (G1 n≥40 ~27-28 Oct) |
| **V7** (disparo 15m BTC) | 4 · FORWARD; escalón de régimen 13-Oct; revive 16-Oct con vendedores sustitutos | 16-Oct: 6 mercados, +6,49 € (n minúsculo) | — | descubrimiento ~28-37 k€/año (no validado) | 0 / 0 / ~30 k€ | V4 | seguir forward; vigilar a 0x56f609c6 y 0x29efa7c2 |
| **V6** (FOK en vuelo BTC) | 4 · FORWARD, 0/7 gates | 1 ejecución −2,12 € | — | descubrimiento ~30 k€ | 0 / 0 / ? | V4/V7 | forward |
| V2 / V3 / V5 | 4 · FORWARD, sin muestra o negativos | — | — | — | 0 | V4 | forward |
| **PRECIERRE** (fuera de la familia 5m barato; referencia) | 6 · LIVE 2 € | +0,12 €/€ (32 órdenes, 16/32, +7,36 €) | 32 / 18 días | ~1-2 órdenes/día | — | — | rampa pre-registrada (vigía 09:40Z) |

## Cerrado (no reabrir sin mecanismo nuevo)
Cosechar al abrir (H10/H11/H32), pares maker estáticos, FV v1-v3 y FV v4 tomador, H26 "Binance en contra" (look-ahead),
H26-MS y la predicción de Binance con margen (anticipa volatilidad, no pérdida), precursores externos (Bybit, barrido en
otra moneda), salidas tras relleno (H37/H40/H41), LOWLOW/LONGSHOT tomador, caja de 2 patas, vender bid15 rancio.

## Las 3 pruebas de mayor valor de la información (17-Oct)
1. **Micro-órdenes maker reales (P1)** en la dedicada, primero en mercados que cumplan R5K y en la línea base: es la única
   forma de saber si capturamos el +0,21 de R5K, el +0,007 de la línea base, o nada. Coste: construir el modo maker
   (dev + /code-review + OK Javi) y ≤5 € de riesgo.
2. **Forward de R5K** (ya en cron): confirma o refuta el +0,21 en días nuevos sin tocar dinero. ~10 días.
3. **Modelo de colocación** (turno pesado): si encuentra cuándo/dónde colocar con +0,05 sobre la línea base, es la palanca
   que puede multiplicar la capacidad (más mercados y más acciones por mercado).
