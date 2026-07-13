# Estado del bot — 2026-07-13 18:02 UTC

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
| P&L fiel (stake fijo 1$) | +1480.81 $ |
| P&L sim compuesto | 🟢 +2508.14 $ (ficción Kelly: +9859% s/ operativo) |
| P&L sim hoy (2026-07-13) | 🟢 +294.67 $ |
| Operaciones resueltas | 12792 (7377 WIN / 5415 LOSS) — 57.7% |
| Señales abiertas | 114 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4007 | 60.9% | +0.109 | ➡️ estable | +1305.25$ | 1.09$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1331 | 65.8% | +0.158 | ➡️ estable | +781.62$ | 1.58$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1368 | 58.7% | +0.087 | ➡️ estable | +386.80$ | 0.87$ | ✅ activa |
| UPDOWN_GBM | 1411 | 50.4% | +0.004 | 📈 madura (+0.08) | +57.19$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 87 | 62.1% | +0.118 | 📉 agota (-0.06) | +29.21$ | 1.18$ | ✅ activa |
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
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 243 | 45.7% | -0.043 | 📉 agota (-0.04) | -22.41$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 1405 | 67.4% | +0.174 | ➡️ estable | -24.40$ | 1.73$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-13T18:01 | STREAK_FADE_5M#ETH#5min | Ethereum Up or Down - July 13, 1:55PM-2:00PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-13T18:01 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 13, 1:45PM-2:00PM ET… | ✅ WIN | +0.88$ |
| 2026-07-13T18:01 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 13, 1:45PM-2:00PM ET… | ✅ WIN | +0.44$ |
| 2026-07-13T18:01 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 13, 1:45PM-2:00PM ET… | ✅ WIN | +2.00$ |
| 2026-07-13T18:01 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 13, 1:45PM-2:00PM ET… | ✅ WIN | +2.31$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-13T18:01 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $61,919.36 | 0.1min |  |
| ✅ ETH | $1,754.75 | 0.1min |  |
| ✅ SOL | $74.65 | 0.1min |  |
| ✅ XRP | $1.06 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $61,919.36 | consenso |  |
| ETH | $1,756.63 | consenso |  |
| SOL | $74.65 | consenso |  |
| XRP | $1.06 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*