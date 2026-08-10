# Estado del bot — 2026-08-10 09:11 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **8.86 $** |
| P&L real total | 🔴 **-42.36 $** |
| P&L real hoy | -1.19 $ |
| P&L real 7 días | -10.64 $ |
| Fees pagados (real) | 15.09 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6175.84 $ |
| P&L sim compuesto | 🟢 +14730.01 $ (ficción Kelly: +57901% s/ operativo) |
| P&L sim hoy (2026-08-10) | 🟢 +354.54 $ |
| Operaciones resueltas | 103885 (63816 WIN / 40069 LOSS) — 61.4% |
| Señales abiertas | 492 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 10974 | 62.1% | +0.121 | ➡️ estable | +5339.49$ | 1.21$ | ✅ activa |
| GBM_LATE_15M | 13361 | 60.2% | +0.102 | ➡️ estable | +4526.65$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10199 | 59.2% | +0.092 | 📈 madura (+0.04) | +3787.66$ | 0.92$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3561 | 66.1% | +0.161 | ➡️ estable | +1809.79$ | 1.61$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 847 | 73.8% | +0.237 | 📈 madura (+0.06) | +754.67$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4035 | 55.9% | +0.059 | 📈 madura (+0.07) | +555.97$ | 0.59$ | ✅ activa |
| WEEKLY_PRICE | 710 | 77.6% | +0.275 | 📈 madura (+0.17) | +311.00$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 438 | 55.3% | +0.052 | 📉 agota (-0.13) | +98.28$ | 0.52$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 151 | 76.2% | +0.258 | 📉 agota (-0.07) | +77.76$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 319 | 80.6% | +0.304 | ➡️ estable | +62.42$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1586 | 48.7% | -0.013 | 📈 madura (+0.04) | +36.54$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 406 | 42.4% | -0.076 | 📈 madura (+0.11) | +18.04$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1347 | 62.9% | +0.129 | ➡️ estable | +16.14$ | 1.29$ | ✅ activa |
| ORDER_FLOW_5M | 1725 | 51.4% | +0.014 | ➡️ estable | +15.43$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.52$ | ✅ activa |
| STRUCT_NO_15M | 729 | 52.4% | +0.024 | ➡️ estable | +6.97$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 29 | 79.3% | +0.274 | — | +6.30$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_60M | 127 | 53.5% | +0.035 | 📈 madura (+0.05) | +1.74$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 138 | 51.4% | +0.014 | 📈 madura (+0.04) | -0.26$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 142 | 93.7% | +0.431 | 📈 madura (+0.04) | -1.45$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 44 | 22.7% | -0.261 | 📉 agota (-0.08) | -10.29$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 646 | 79.7% | +0.296 | ➡️ estable | -12.92$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 75 | 33.3% | -0.162 | ➡️ estable | -13.50$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 110 | 40.0% | -0.098 | 📈 madura (+0.04) | -13.76$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 130 | 86.9% | +0.364 | 📈 madura (+0.10) | -16.88$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1858 | 54.8% | +0.048 | 📉 agota (-0.16) | -17.22$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 340 | 77.1% | +0.269 | 📉 agota (-0.09) | -23.10$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 127 | 18.9% | -0.306 | 📈 madura (+0.09) | -24.97$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 251 | 44.6% | -0.053 | 📉 agota (-0.08) | -26.50$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 325 | 43.7% | -0.063 | 📉 agota (-0.10) | -27.91$ | 0.50$ | 🚫 desactivada |
| UPDOWN_OU_5M | 344 | 32.3% | -0.176 | ➡️ estable | -59.69$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2808 | 70.2% | +0.202 | 📉 agota (-0.04) | -174.53$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 2926 | 44.0% | -0.060 | 📈 madura (+0.04) | -614.38$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 28677 | 61.9% | +0.119 | 📉 agota (-0.03) | -712.28$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 13088 | 70.1% | +0.201 | ➡️ estable | -940.56$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-10T09:10 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | … | ✅ WIN | +0.39$ |
| 2026-08-10T09:10 | FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | Solana Up or Down - August 10, 4:45AM-5:00AM ET… | ❌ LOSS | -0.51$ |
| 2026-08-10T09:10 | FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | Solana Up or Down - August 10, 4:45AM-5:00AM ET… | ✅ WIN | +0.30$ |
| 2026-08-10T09:10 | BALLENAS_CONFIRMADAS_15M#ETH#15min | Ethereum Up or Down - August 10, 4:45AM-5:00AM ET… | ❌ LOSS | -1.53$ |
| 2026-08-10T09:10 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ✅ WIN | +0.39$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-10T09:07 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,165.00 | 0.1min |  |
| ✅ ETH | $1,924.84 | 0.1min |  |
| ✅ SOL | $76.92 | 0.1min |  |
| ✅ XRP | $1.03 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,159.39 | consenso |  |
| ETH | $1,924.41 | consenso |  |
| SOL | $76.89 | consenso |  |
| XRP | $1.03 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*