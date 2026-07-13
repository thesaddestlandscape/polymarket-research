# Estado del bot — 2026-07-13 09:18 UTC

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
| P&L fiel (stake fijo 1$) | +1407.51 $ |
| P&L sim compuesto | 🟢 +2355.89 $ (ficción Kelly: +9261% s/ operativo) |
| P&L sim hoy (2026-07-13) | 🟢 +142.42 $ |
| Operaciones resueltas | 12230 (7026 WIN / 5204 LOSS) — 57.4% |
| Señales abiertas | 116 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3883 | 61.0% | +0.110 | ➡️ estable | +1275.89$ | 1.10$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1209 | 65.8% | +0.158 | ➡️ estable | +711.69$ | 1.58$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1303 | 57.9% | +0.079 | ➡️ estable | +329.36$ | 0.79$ | ✅ activa |
| UPDOWN_GBM | 1384 | 50.1% | +0.001 | 📈 madura (+0.08) | +50.45$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 165 | 62.4% | +0.123 | 📈 madura (+0.24) | +28.93$ | 1.23$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 80 | 63.7% | +0.134 | 📉 agota (-0.07) | +26.87$ | 1.34$ | ✅ activa |
| ORDER_FLOW_5M | 1591 | 51.2% | +0.012 | ➡️ estable | +13.79$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 38 | 71.1% | +0.200 | 📈 madura (+0.05) | +12.03$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 323 | 38.7% | -0.112 | ➡️ estable | +5.44$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 140 | 34.3% | -0.155 | 📉 agota (-0.14) | -0.83$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 201 | 46.8% | -0.032 | ➡️ estable | -13.32$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 1256 | 67.7% | +0.176 | ➡️ estable | -13.36$ | 1.76$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 204 | 57.4% | +0.073 | 📈 madura (+0.24) | -13.93$ | 0.73$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-13T09:18 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 13, 5:00AM-5:15AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-13T09:18 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 13, 5:00AM-5:15AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-13T09:18 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 13, 5:00AM-5:15AM ET… | ✅ WIN | +0.68$ |
| 2026-07-13T09:18 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 13, 5:00AM-5:15AM ET… | ✅ WIN | +0.76$ |
| 2026-07-13T09:18 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 13, 5:00AM-5:15AM ET… | ✅ WIN | +2.00$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-13T09:17 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,061.14 | 0.1min |  |
| ✅ ETH | $1,785.45 | 0.1min |  |
| ✅ SOL | $76.70 | 0.1min |  |
| ✅ XRP | $1.08 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,090.40 | consenso |  |
| ETH | $1,785.63 | consenso |  |
| SOL | $76.59 | consenso |  |
| XRP | $1.08 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*