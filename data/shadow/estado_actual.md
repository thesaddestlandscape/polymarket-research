# Estado del bot — 2026-08-11 10:55 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **10.07 $** |
| P&L real total | 🔴 **-41.15 $** |
| P&L real hoy | -0.23 $ |
| P&L real 7 días | -11.98 $ |
| Fees pagados (real) | 15.23 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6188.49 $ |
| P&L sim compuesto | 🟢 +15250.85 $ (ficción Kelly: +59948% s/ operativo) |
| P&L sim hoy (2026-08-11) | 🟢 +82.73 $ |
| Operaciones resueltas | 110593 (67957 WIN / 42636 LOSS) — 61.4% |
| Señales abiertas | 573 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11341 | 61.8% | +0.118 | ➡️ estable | +5579.32$ | 0.58$ | ✅ activa |
| GBM_LATE_15M | 13652 | 60.3% | +0.103 | ➡️ estable | +4683.33$ | 1.13$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10426 | 59.4% | +0.094 | 📈 madura (+0.05) | +3965.52$ | 1.91$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3602 | 65.9% | +0.158 | ➡️ estable | +1816.75$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1045 | 74.5% | +0.245 | 📈 madura (+0.06) | +962.39$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4077 | 55.9% | +0.059 | 📈 madura (+0.06) | +562.22$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 732 | 77.9% | +0.278 | 📈 madura (+0.16) | +326.70$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 452 | 54.6% | +0.046 | 📉 agota (-0.13) | +98.56$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 161 | 76.4% | +0.261 | 📉 agota (-0.05) | +82.00$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 328 | 80.5% | +0.303 | ➡️ estable | +62.56$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1664 | 49.6% | -0.004 | 📈 madura (+0.06) | +55.67$ | 0.87$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1859 | 63.3% | +0.133 | ➡️ estable | +37.06$ | 1.33$ | ✅ activa |
| GBM_LATE_60M | 422 | 42.7% | -0.073 | 📈 madura (+0.10) | +31.37$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1729 | 51.5% | +0.015 | ➡️ estable | +18.29$ | 0.60$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.00$ | 🚫 desactivada |
| RESOLUTION_SNIPER | 32 | 81.2% | +0.294 | 📉 agota (-0.11) | +6.65$ | 2.00$ | ✅ activa |
| STRUCT_NO_15M | 860 | 52.3% | +0.023 | ➡️ estable | +6.06$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 187 | 54.0% | +0.040 | ➡️ estable | +2.85$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 149 | 94.0% | +0.434 | 📈 madura (+0.04) | -0.58$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 7 | 28.6% | -0.058 | — | -1.60$ | 0.50$ | ⏳ acumulando |
| LIQUIDACIONES_60M | 158 | 51.9% | +0.019 | ➡️ estable | -1.64$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1910 | 55.1% | +0.051 | 📉 agota (-0.15) | -1.95$ | 0.70$ | ✅ activa |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 52 | 21.2% | -0.278 | 📉 agota (-0.11) | -13.27$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 140 | 87.9% | +0.373 | 📈 madura (+0.10) | -15.48$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 364 | 78.0% | +0.279 | 📉 agota (-0.07) | -15.97$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 663 | 79.5% | +0.294 | ➡️ estable | -16.72$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 88 | 30.7% | -0.189 | ➡️ estable | -18.20$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 150 | 39.3% | -0.105 | ➡️ estable | -21.06$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 265 | 45.7% | -0.043 | ➡️ estable | -24.65$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 140 | 18.6% | -0.310 | 📈 madura (+0.08) | -28.09$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 339 | 43.4% | -0.066 | 📉 agota (-0.12) | -30.02$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 348 | 31.9% | -0.180 | ➡️ estable | -61.73$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3113 | 70.1% | +0.201 | ➡️ estable | -189.71$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 3524 | 45.4% | -0.046 | 📈 madura (+0.07) | -669.97$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 30946 | 61.7% | +0.117 | ➡️ estable | -859.28$ | 1.14$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 14361 | 69.9% | +0.199 | ➡️ estable | -1073.45$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-11T10:55 | BALLENAS_TARDIAS#DOGE#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-11T10:55 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | … | ✅ WIN | +0.31$ |
| 2026-08-11T10:55 | BALLENAS_TARDIAS#SOL#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-11T10:55 | GBM_LATE_5M#SOL#5min | Solana Up or Down - August 11, 6:35AM-6:40AM ET… | ✅ WIN | +0.49$ |
| 2026-08-11T10:55 | BALLENAS_TARDIAS#XRP#5min | … | ✅ WIN | +1.55$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-11T10:52 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,208.97 | 0.2min |  |
| ✅ ETH | $1,886.39 | 0.2min |  |
| ✅ SOL | $75.98 | 0.2min |  |
| ✅ XRP | $1.01 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,208.97 | consenso |  |
| ETH | $1,886.39 | consenso |  |
| SOL | $75.98 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*