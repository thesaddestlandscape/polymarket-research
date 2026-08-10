# Estado del bot — 2026-08-10 08:19 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **9.62 $** |
| P&L real total | 🔴 **-41.60 $** |
| P&L real hoy | -0.44 $ |
| P&L real 7 días | -9.89 $ |
| Fees pagados (real) | 15.09 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6166.71 $ |
| P&L sim compuesto | 🟢 +14701.50 $ (ficción Kelly: +57789% s/ operativo) |
| P&L sim hoy (2026-08-10) | 🟢 +326.03 $ |
| Operaciones resueltas | 103670 (63688 WIN / 39982 LOSS) — 61.4% |
| Señales abiertas | 486 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 10956 | 62.1% | +0.121 | ➡️ estable | +5330.56$ | 1.21$ | ✅ activa |
| GBM_LATE_15M | 13349 | 60.2% | +0.102 | ➡️ estable | +4513.52$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10194 | 59.2% | +0.092 | 📈 madura (+0.04) | +3781.94$ | 0.92$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3559 | 66.1% | +0.161 | ➡️ estable | +1811.94$ | 1.61$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 841 | 73.7% | +0.237 | 📈 madura (+0.05) | +747.17$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4034 | 55.9% | +0.059 | 📈 madura (+0.07) | +557.58$ | 0.59$ | ✅ activa |
| WEEKLY_PRICE | 710 | 77.6% | +0.275 | 📈 madura (+0.17) | +311.00$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 438 | 55.3% | +0.052 | 📉 agota (-0.13) | +98.28$ | 0.52$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 151 | 76.2% | +0.258 | 📉 agota (-0.07) | +77.76$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 319 | 80.6% | +0.304 | ➡️ estable | +62.42$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1586 | 48.7% | -0.013 | 📈 madura (+0.04) | +36.54$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1330 | 63.1% | +0.131 | ➡️ estable | +19.97$ | 1.31$ | ✅ activa |
| GBM_LATE_60M | 406 | 42.4% | -0.076 | 📈 madura (+0.11) | +18.04$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1725 | 51.4% | +0.014 | ➡️ estable | +15.43$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.52$ | ✅ activa |
| STRUCT_NO_15M | 719 | 52.7% | +0.027 | ➡️ estable | +9.25$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 29 | 79.3% | +0.274 | — | +6.30$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_60M | 127 | 53.5% | +0.035 | 📈 madura (+0.05) | +1.74$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 138 | 51.4% | +0.014 | 📈 madura (+0.04) | -0.26$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 141 | 93.6% | +0.430 | 📈 madura (+0.04) | -1.52$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 44 | 22.7% | -0.261 | 📉 agota (-0.08) | -10.29$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_5M | 75 | 33.3% | -0.162 | ➡️ estable | -13.50$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 110 | 40.0% | -0.098 | 📈 madura (+0.04) | -13.76$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 644 | 79.7% | +0.296 | ➡️ estable | -13.97$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1857 | 54.9% | +0.049 | 📉 agota (-0.17) | -15.69$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 130 | 86.9% | +0.364 | 📈 madura (+0.10) | -16.88$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 340 | 77.1% | +0.269 | 📉 agota (-0.09) | -23.10$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 127 | 18.9% | -0.306 | 📈 madura (+0.09) | -24.97$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 251 | 44.6% | -0.053 | 📉 agota (-0.08) | -26.50$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 325 | 43.7% | -0.063 | 📉 agota (-0.10) | -27.91$ | 0.50$ | 🚫 desactivada |
| UPDOWN_OU_5M | 344 | 32.3% | -0.176 | ➡️ estable | -59.69$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2794 | 70.2% | +0.202 | 📉 agota (-0.04) | -173.03$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 2914 | 43.9% | -0.061 | 📈 madura (+0.04) | -628.04$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 28605 | 61.9% | +0.119 | 📉 agota (-0.03) | -699.92$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 13046 | 70.0% | +0.200 | ➡️ estable | -944.26$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-10T08:18 | FAVORITO_CONFIRMADO#BTC#5min | … | ✅ WIN | +0.84$ |
| 2026-08-10T08:18 | FAVORITO_CONFIRMADO#ETH#5min | … | ✅ WIN | +0.54$ |
| 2026-08-10T08:18 | FAVORITO_CONFIRMADO#XRP#5min | … | ✅ WIN | +0.80$ |
| 2026-08-10T08:18 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | … | ✅ WIN | +0.84$ |
| 2026-08-10T08:18 | GBM_LATE_5M#SOL#5min | Solana Up or Down - August 10, 4:00AM-4:05AM ET… | ✅ WIN | +0.39$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-10T08:17 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,207.42 | 0.1min |  |
| ✅ ETH | $1,925.59 | 0.1min |  |
| ✅ SOL | $76.96 | 0.1min |  |
| ✅ XRP | $1.04 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,215.10 | consenso |  |
| ETH | $1,925.59 | consenso |  |
| SOL | $76.93 | consenso |  |
| XRP | $1.04 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*