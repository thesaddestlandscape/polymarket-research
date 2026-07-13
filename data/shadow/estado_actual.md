# Estado del bot — 2026-07-13 18:35 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **10.03 $** |
| P&L real total | 🔴 **-15.41 $** |
| P&L real hoy | -4.41 $ |
| P&L real 7 días | +1.17 $ |
| Fees pagados (real) | 7.98 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1476.36 $ |
| P&L sim compuesto | 🟢 +2507.98 $ (ficción Kelly: +9858% s/ operativo) |
| P&L sim hoy (2026-07-13) | 🟢 +294.51 $ |
| Operaciones resueltas | 12826 (7394 WIN / 5432 LOSS) — 57.6% |
| Señales abiertas | 115 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4015 | 60.9% | +0.109 | ➡️ estable | +1304.14$ | 1.09$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1339 | 65.8% | +0.158 | ➡️ estable | +784.53$ | 1.58$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1373 | 58.6% | +0.086 | ➡️ estable | +385.43$ | 0.86$ | ✅ activa |
| UPDOWN_GBM | 1415 | 50.2% | +0.002 | 📈 madura (+0.08) | +51.22$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 88 | 61.4% | +0.111 | 📉 agota (-0.04) | +28.70$ | 1.11$ | ✅ activa |
| STREAK_FADE_15M | 173 | 60.7% | +0.106 | 📈 madura (+0.16) | +20.86$ | 1.06$ | ✅ activa |
| LATE_WINDOW_5MIN | 39 | 71.8% | +0.207 | 📈 madura (+0.06) | +13.83$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1591 | 51.2% | +0.012 | ➡️ estable | +13.79$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 323 | 38.7% | -0.112 | ➡️ estable | +5.44$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 142 | 34.5% | -0.153 | 📉 agota (-0.12) | -0.70$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 219 | 59.4% | +0.093 | 📈 madura (+0.26) | -1.22$ | 0.93$ | ✅ activa |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 1411 | 67.5% | +0.175 | ➡️ estable | -17.49$ | 1.75$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 245 | 45.3% | -0.047 | 📉 agota (-0.04) | -23.43$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-13T18:35 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 13, 2:15PM-2:30PM ET… | ✅ WIN | +1.38$ |
| 2026-07-13T18:35 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 13, 2:15PM-2:30PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-13T18:35 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 13, 2:15PM-2:30PM ET… | ❌ LOSS | -1.55$ |
| 2026-07-13T18:35 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 13, 2:15PM-2:30PM ET… | ❌ LOSS | -1.36$ |
| 2026-07-13T18:32 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 13, 2:15PM-2:30PM ET… | ✅ WIN | +1.77$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-13T18:34 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $61,858.33 | 0.1min |  |
| ✅ ETH | $1,756.85 | 0.1min |  |
| ✅ SOL | $74.80 | 0.1min |  |
| ✅ XRP | $1.06 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $61,866.70 | consenso |  |
| ETH | $1,756.85 | consenso |  |
| SOL | $74.86 | consenso |  |
| XRP | $1.06 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*