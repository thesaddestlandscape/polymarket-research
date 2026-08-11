# Estado del bot — 2026-08-11 00:11 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **10.30 $** |
| P&L real total | 🔴 **-40.92 $** |
| P&L real hoy | -32.86 $ |
| P&L real 7 días | -11.75 $ |
| Fees pagados (real) | 15.20 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6260.90 $ |
| P&L sim compuesto | 🟢 +15175.58 $ (ficción Kelly: +59652% s/ operativo) |
| P&L sim hoy (2026-08-11) | 🟢 +7.46 $ |
| Operaciones resueltas | 107784 (66264 WIN / 41520 LOSS) — 61.5% |
| Señales abiertas | 476 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11199 | 62.0% | +0.119 | ➡️ estable | +5545.33$ | 1.19$ | ✅ activa |
| GBM_LATE_15M | 13542 | 60.3% | +0.103 | ➡️ estable | +4615.47$ | 1.03$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10338 | 59.4% | +0.094 | 📈 madura (+0.05) | +3896.68$ | 0.94$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3587 | 66.0% | +0.160 | ➡️ estable | +1817.65$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 968 | 74.9% | +0.248 | 📈 madura (+0.08) | +898.19$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4061 | 55.9% | +0.059 | 📈 madura (+0.07) | +565.87$ | 0.59$ | ✅ activa |
| WEEKLY_PRICE | 732 | 77.9% | +0.278 | 📈 madura (+0.16) | +326.70$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 445 | 54.6% | +0.046 | 📉 agota (-0.13) | +96.50$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 157 | 77.1% | +0.267 | 📉 agota (-0.05) | +85.58$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 324 | 80.9% | +0.307 | ➡️ estable | +66.15$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1620 | 49.0% | -0.010 | 📈 madura (+0.04) | +38.80$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1648 | 62.9% | +0.128 | ➡️ estable | +19.63$ | 1.29$ | ✅ activa |
| GBM_LATE_60M | 410 | 42.4% | -0.075 | 📈 madura (+0.11) | +15.68$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1725 | 51.4% | +0.014 | ➡️ estable | +15.43$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 790 | 53.2% | +0.032 | ➡️ estable | +12.27$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.52$ | ✅ activa |
| RESOLUTION_SNIPER | 32 | 81.2% | +0.294 | 📉 agota (-0.11) | +6.65$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1894 | 55.1% | +0.051 | 📉 agota (-0.15) | +0.99$ | 0.51$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 168 | 53.6% | +0.035 | ➡️ estable | +0.20$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 144 | 93.8% | +0.432 | 📈 madura (+0.04) | -1.25$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 6 | 16.7% | -0.075 | — | -2.08$ | 0.50$ | ⏳ acumulando |
| LIQUIDACIONES_60M | 148 | 50.7% | +0.007 | ➡️ estable | -3.73$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 52 | 21.2% | -0.278 | 📉 agota (-0.11) | -13.27$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 135 | 87.4% | +0.369 | 📈 madura (+0.10) | -16.19$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 86 | 31.4% | -0.182 | ➡️ estable | -17.18$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 656 | 79.4% | +0.293 | 📉 agota (-0.03) | -18.62$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 356 | 77.5% | +0.274 | 📉 agota (-0.09) | -19.91$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_15M | 140 | 38.6% | -0.113 | ➡️ estable | -20.01$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 251 | 44.6% | -0.053 | 📉 agota (-0.08) | -26.50$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 132 | 18.2% | -0.313 | 📈 madura (+0.06) | -27.52$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 325 | 43.7% | -0.063 | 📉 agota (-0.10) | -27.91$ | 0.50$ | 🚫 desactivada |
| UPDOWN_OU_5M | 347 | 32.0% | -0.179 | 📉 agota (-0.03) | -61.22$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2975 | 70.0% | +0.200 | ➡️ estable | -189.42$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 3250 | 45.0% | -0.050 | 📈 madura (+0.06) | -635.39$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 30006 | 61.8% | +0.118 | ➡️ estable | -763.34$ | 1.18$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 13828 | 70.0% | +0.200 | ➡️ estable | -1001.55$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-11T00:10 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - August 10, 7:45PM-8:00PM ET… | ❌ LOSS | -2.04$ |
| 2026-08-11T00:10 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - August 10, 7:45PM-8:00PM ET… | ✅ WIN | +1.84$ |
| 2026-08-11T00:10 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - August 10, 7:45PM-8:00PM ET… | ✅ WIN | +1.84$ |
| 2026-08-11T00:10 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | … | ✅ WIN | +0.31$ |
| 2026-08-11T00:10 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | … | ❌ LOSS | -1.07$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-11T00:08 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,870.36 | 0.1min |  |
| ✅ ETH | $1,870.01 | 0.1min |  |
| ✅ SOL | $75.86 | 0.1min |  |
| ✅ XRP | $1.01 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,880.40 | consenso |  |
| ETH | $1,870.12 | consenso |  |
| SOL | $75.85 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*