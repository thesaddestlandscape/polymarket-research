# Estado del bot — 2026-08-09 04:33 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **10.44 $** |
| P&L real total | 🔴 **-40.78 $** |
| P&L real hoy | -0.78 $ |
| P&L real 7 días | -11.15 $ |
| Fees pagados (real) | 14.97 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6001.13 $ |
| P&L sim compuesto | 🟢 +14094.61 $ (ficción Kelly: +55403% s/ operativo) |
| P&L sim hoy (2026-08-09) | 🟢 +34.70 $ |
| Operaciones resueltas | 96443 (59081 WIN / 37362 LOSS) — 61.3% |
| Señales abiertas | 722 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 10459 | 62.4% | +0.124 | ➡️ estable | +5189.21$ | 1.24$ | ✅ activa |
| GBM_LATE_15M | 12965 | 60.2% | +0.102 | ➡️ estable | +4367.80$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 9955 | 58.9% | +0.089 | ➡️ estable | +3525.00$ | 0.89$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3512 | 66.3% | +0.163 | ➡️ estable | +1803.21$ | 1.63$ | ✅ activa |
| UPDOWN_GBM | 4004 | 55.9% | +0.059 | 📈 madura (+0.07) | +563.54$ | 0.59$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 654 | 71.7% | +0.216 | ➡️ estable | +492.23$ | 2.00$ | ✅ activa |
| WEEKLY_PRICE | 682 | 77.1% | +0.270 | 📈 madura (+0.17) | +290.58$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 436 | 55.0% | +0.050 | 📉 agota (-0.14) | +97.89$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 136 | 75.7% | +0.254 | 📉 agota (-0.04) | +71.24$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 306 | 80.7% | +0.305 | ➡️ estable | +61.72$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1518 | 48.4% | -0.016 | ➡️ estable | +37.20$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 808 | 64.1% | +0.141 | 📈 madura (+0.07) | +26.94$ | 1.41$ | ✅ activa |
| GBM_LATE_60M | 398 | 42.5% | -0.075 | 📈 madura (+0.12) | +16.84$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1723 | 51.4% | +0.014 | ➡️ estable | +15.45$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 323 | 55.4% | +0.054 | 📉 agota (-0.14) | +12.10$ | 0.54$ | ✅ activa |
| RESOLUTION_SNIPER | 28 | 78.6% | +0.267 | — | +4.53$ | 2.00$ | ✅ activa |
| STRUCT_NO_15M | 509 | 52.5% | +0.024 | ➡️ estable | +1.80$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 32 | 50.0% | +0.000 | 📉 agota (-0.11) | +0.39$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 104 | 51.9% | +0.019 | 📈 madura (+0.07) | -0.15$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 123 | 93.5% | +0.428 | 📈 madura (+0.06) | -1.53$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| LIQUIDACIONES_60M | 100 | 52.0% | +0.020 | 📈 madura (+0.04) | -4.32$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 625 | 80.2% | +0.301 | 📉 agota (-0.04) | -5.03$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM | 193 | 33.7% | -0.162 | 📉 agota (-0.09) | -5.71$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 394 | 43.9% | -0.061 | 📉 agota (-0.14) | -6.24$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 32 | 25.0% | -0.235 | ➡️ estable | -6.52$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_15M | 86 | 40.7% | -0.091 | 📈 madura (+0.11) | -10.02$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 67 | 31.3% | -0.181 | 📈 madura (+0.08) | -13.28$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 310 | 78.1% | +0.279 | 📉 agota (-0.09) | -13.36$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 118 | 87.3% | +0.367 | 📈 madura (+0.11) | -14.05$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1804 | 54.7% | +0.047 | 📉 agota (-0.16) | -21.77$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_FADE | 125 | 18.4% | -0.311 | 📈 madura (+0.07) | -25.36$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 247 | 44.9% | -0.050 | 📉 agota (-0.06) | -25.47$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 324 | 43.8% | -0.061 | 📉 agota (-0.10) | -27.40$ | 0.50$ | 🚫 desactivada |
| UPDOWN_OU_5M | 337 | 32.3% | -0.176 | ➡️ estable | -58.65$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2464 | 69.9% | +0.199 | 📉 agota (-0.06) | -174.39$ | 1.99$ | ✅ activa |
| BALLENAS_TARDIAS | 2405 | 42.9% | -0.071 | 📉 agota (-0.05) | -530.15$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 26158 | 61.9% | +0.119 | 📉 agota (-0.05) | -652.92$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 11618 | 69.7% | +0.197 | ➡️ estable | -884.41$ | 1.97$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-09T04:31 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | … | ✅ WIN | +0.19$ |
| 2026-08-09T04:31 | FAVORITO_CONFIRMADO#XRP#5min | … | ✅ WIN | +0.50$ |
| 2026-08-09T04:31 | BALLENAS_TARDIAS#XRP#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-09T04:31 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | … | ✅ WIN | +0.60$ |
| 2026-08-09T04:31 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | … | ✅ WIN | +0.84$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-09T04:30 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,756.25 | 0.1min |  |
| ✅ ETH | $1,912.40 | 0.1min |  |
| ✅ SOL | $76.05 | 0.1min |  |
| ✅ XRP | $1.04 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,756.25 | consenso |  |
| ETH | $1,912.56 | consenso |  |
| SOL | $75.96 | consenso |  |
| XRP | $1.04 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*