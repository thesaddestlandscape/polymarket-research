# Estado del bot — 2026-07-13 07:57 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **13.33 $** |
| P&L real total | 🔴 **-12.11 $** |
| P&L real hoy | -1.10 $ |
| P&L real 7 días | +4.47 $ |
| Fees pagados (real) | 7.82 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1402.14 $ |
| P&L sim compuesto | 🟢 +2338.71 $ (ficción Kelly: +9193% s/ operativo) |
| P&L sim hoy (2026-07-13) | 🟢 +125.24 $ |
| Operaciones resueltas | 12137 (6973 WIN / 5164 LOSS) — 57.5% |
| Señales abiertas | 124 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3861 | 61.1% | +0.111 | ➡️ estable | +1275.01$ | 1.11$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1191 | 66.0% | +0.160 | ➡️ estable | +705.86$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1288 | 57.9% | +0.079 | ➡️ estable | +325.62$ | 0.79$ | ✅ activa |
| UPDOWN_GBM | 1376 | 49.9% | -0.001 | 📈 madura (+0.07) | +41.24$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_15M | 165 | 62.4% | +0.123 | 📈 madura (+0.24) | +28.93$ | 1.23$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 80 | 63.7% | +0.134 | 📉 agota (-0.07) | +26.87$ | 1.34$ | ✅ activa |
| ORDER_FLOW_5M | 1591 | 51.2% | +0.012 | ➡️ estable | +13.79$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 38 | 71.1% | +0.200 | 📈 madura (+0.05) | +12.03$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 323 | 38.7% | -0.112 | ➡️ estable | +5.44$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 140 | 34.3% | -0.155 | 📉 agota (-0.14) | -0.83$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 1229 | 67.9% | +0.179 | ➡️ estable | -9.76$ | 1.79$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 204 | 57.4% | +0.073 | 📈 madura (+0.24) | -13.93$ | 0.73$ | ✅ activa |
| STREAK_FADE_5M | 198 | 46.5% | -0.035 | 📉 agota (-0.04) | -14.45$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-13T07:51 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 13, 3:30AM-3:45AM ET… | ✅ WIN | +4.11$ |
| 2026-07-13T07:51 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 13, 3:30AM-3:45AM ET… | ✅ WIN | +3.99$ |
| 2026-07-13T07:51 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 13, 3:30AM-3:45AM ET… | ✅ WIN | +4.11$ |
| 2026-07-13T07:51 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 13, 3:30AM-3:45AM ET… | ✅ WIN | +2.45$ |
| 2026-07-13T07:51 | UPDOWN_GBM#BTC#15min | Bitcoin Up or Down - July 13, 3:30AM-3:45AM ET… | ✅ WIN | +3.60$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-13T07:56 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,923.00 | 0.1min |  |
| ✅ ETH | $1,784.34 | 0.1min |  |
| ✅ SOL | $76.40 | 0.1min |  |
| ✅ XRP | $1.08 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,928.00 | consenso |  |
| ETH | $1,784.39 | consenso |  |
| SOL | $76.33 | consenso |  |
| XRP | $1.08 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*