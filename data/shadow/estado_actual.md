# Estado del bot — 2026-08-13 06:21 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **7.08 $** |
| P&L real total | 🔴 **-44.14 $** |
| P&L real hoy | -1.07 $ |
| P&L real 7 días | -4.82 $ |
| Fees pagados (real) | 15.49 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6090.70 $ |
| P&L sim compuesto | 🟢 +16028.14 $ (ficción Kelly: +63004% s/ operativo) |
| P&L sim hoy (2026-08-13) | 🟢 +288.35 $ |
| Operaciones resueltas | 124324 (76206 WIN / 48118 LOSS) — 61.3% |
| Señales abiertas | 432 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 12210 | 61.4% | +0.114 | ➡️ estable | +5847.34$ | 0.61$ | ✅ activa |
| GBM_LATE_15M | 14383 | 60.2% | +0.102 | ➡️ estable | +4932.50$ | 1.01$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10998 | 60.0% | +0.100 | 📈 madura (+0.07) | +4435.12$ | 1.94$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3939 | 64.1% | +0.141 | ➡️ estable | +1813.56$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1553 | 72.4% | +0.224 | ➡️ estable | +1338.51$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4536 | 55.6% | +0.056 | 📈 madura (+0.05) | +585.72$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 780 | 77.9% | +0.279 | 📈 madura (+0.14) | +342.55$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 629 | 55.3% | +0.053 | ➡️ estable | +106.72$ | 0.54$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 189 | 76.2% | +0.259 | 📉 agota (-0.07) | +93.60$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1872 | 50.4% | +0.004 | 📈 madura (+0.07) | +86.37$ | 0.77$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 350 | 79.7% | +0.295 | ➡️ estable | +56.33$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 440 | 43.6% | -0.063 | 📈 madura (+0.12) | +45.10$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1740 | 51.5% | +0.015 | ➡️ estable | +18.47$ | 0.59$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 330 | 55.5% | +0.054 | 📉 agota (-0.14) | +12.22$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2705 | 62.0% | +0.120 | ➡️ estable | +8.32$ | 1.20$ | ✅ activa |
| RESOLUTION_SNIPER | 38 | 78.9% | +0.275 | 📉 agota (-0.10) | +6.65$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 234 | 54.7% | +0.047 | 📈 madura (+0.05) | +6.45$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 206 | 53.4% | +0.034 | ➡️ estable | +2.84$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 34 | 50.0% | +0.000 | 📉 agota (-0.05) | +0.47$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 166 | 94.0% | +0.435 | ➡️ estable | -0.55$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 10 | 30.0% | -0.083 | — | -2.19$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 198 | 34.3% | -0.155 | 📉 agota (-0.08) | -6.26$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 396 | 43.9% | -0.060 | 📉 agota (-0.13) | -6.46$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 1140 | 51.0% | +0.010 | ➡️ estable | -9.84$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 2015 | 54.5% | +0.045 | 📉 agota (-0.18) | -12.11$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 164 | 89.6% | +0.392 | 📈 madura (+0.11) | -12.77$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM_FADE | 70 | 21.4% | -0.278 | 📉 agota (-0.08) | -17.69$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 414 | 78.0% | +0.279 | 📉 agota (-0.04) | -18.15$ | 2.00$ | ✅ activa |
| STREAK_FADE_5M | 383 | 47.5% | -0.025 | ➡️ estable | -18.60$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 129 | 36.4% | -0.134 | 📈 madura (+0.13) | -18.96$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 711 | 78.9% | +0.288 | 📉 agota (-0.03) | -23.75$ | 2.00$ | ✅ activa |
| STREAK_MOM_5M | 422 | 44.8% | -0.052 | 📉 agota (-0.05) | -27.67$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 158 | 20.3% | -0.294 | 📈 madura (+0.12) | -28.37$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_15M | 223 | 37.2% | -0.127 | 📉 agota (-0.05) | -34.65$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 383 | 31.6% | -0.183 | 📉 agota (-0.06) | -67.83$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3641 | 70.1% | +0.201 | ➡️ estable | -210.58$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 4752 | 47.1% | -0.029 | 📈 madura (+0.08) | -717.81$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 34741 | 61.4% | +0.114 | ➡️ estable | -1177.94$ | 1.08$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 16686 | 69.8% | +0.198 | ➡️ estable | -1297.75$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-13T06:21 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | … | ✅ WIN | +0.74$ |
| 2026-08-13T06:21 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-13T06:21 | FAVORITO_CONFIRMADO#DOGE#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-13T06:21 | BALLENAS_TARDIAS#SOL#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-13T06:21 | STREAK_FADE_5M#ETH#5min | Ethereum Up or Down - August 13, 2:00AM-2:05AM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-13T06:18 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,758.25 | 0.2min |  |
| ✅ ETH | $1,892.38 | 0.2min |  |
| ✅ SOL | $76.34 | 0.2min |  |
| ✅ XRP | $1.01 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,758.25 | consenso |  |
| ETH | $1,892.38 | consenso |  |
| SOL | $76.34 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*