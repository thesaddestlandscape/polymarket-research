# Estado del bot — 2026-08-12 18:06 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **8.15 $** |
| P&L real total | 🔴 **-43.07 $** |
| P&L real hoy | -3.02 $ |
| P&L real 7 días | -8.32 $ |
| Fees pagados (real) | 15.47 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +5984.85 $ |
| P&L sim compuesto | 🟢 +15598.59 $ (ficción Kelly: +61315% s/ operativo) |
| P&L sim hoy (2026-08-12) | 🟢 +342.94 $ |
| Operaciones resueltas | 120291 (73729 WIN / 46562 LOSS) — 61.3% |
| Señales abiertas | 547 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11932 | 61.4% | +0.114 | ➡️ estable | +5720.98$ | 0.54$ | ✅ activa |
| GBM_LATE_15M | 14149 | 60.2% | +0.102 | ➡️ estable | +4844.56$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10786 | 59.8% | +0.098 | 📈 madura (+0.06) | +4276.20$ | 1.93$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3826 | 64.7% | +0.147 | ➡️ estable | +1812.01$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1354 | 72.7% | +0.227 | ➡️ estable | +1177.90$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4410 | 55.6% | +0.056 | 📈 madura (+0.05) | +579.32$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 780 | 77.9% | +0.279 | 📈 madura (+0.14) | +342.55$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 559 | 55.6% | +0.056 | 📉 agota (-0.03) | +111.34$ | 0.67$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 178 | 75.8% | +0.256 | 📉 agota (-0.05) | +84.23$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1793 | 50.0% | -0.000 | 📈 madura (+0.08) | +66.55$ | 0.72$ | ⚠️ IC negativo |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 342 | 80.1% | +0.299 | ➡️ estable | +59.53$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 432 | 43.5% | -0.065 | 📈 madura (+0.11) | +39.69$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2472 | 62.7% | +0.127 | ➡️ estable | +33.50$ | 1.27$ | ✅ activa |
| ORDER_FLOW_5M | 1736 | 51.4% | +0.014 | ➡️ estable | +17.62$ | 0.54$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.00$ | 🚫 desactivada |
| RESOLUTION_SNIPER | 37 | 78.4% | +0.269 | 📉 agota (-0.18) | +6.14$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 222 | 54.1% | +0.040 | 📈 madura (+0.04) | +5.59$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 34 | 50.0% | +0.000 | 📉 agota (-0.05) | +0.47$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 160 | 93.8% | +0.432 | ➡️ estable | -1.28$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 10 | 30.0% | -0.083 | — | -2.19$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_60M | 192 | 52.1% | +0.021 | ➡️ estable | -3.21$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 198 | 34.3% | -0.155 | 📉 agota (-0.08) | -6.26$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 396 | 43.9% | -0.060 | 📉 agota (-0.13) | -6.46$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 1063 | 51.2% | +0.012 | ➡️ estable | -6.94$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1984 | 54.7% | +0.047 | 📉 agota (-0.18) | -7.94$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 157 | 89.2% | +0.387 | 📈 madura (+0.11) | -13.42$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM_FADE | 70 | 21.4% | -0.278 | 📉 agota (-0.08) | -17.69$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 400 | 78.0% | +0.279 | 📉 agota (-0.07) | -17.86$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 125 | 35.2% | -0.146 | 📈 madura (+0.09) | -20.09$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 698 | 78.9% | +0.289 | ➡️ estable | -23.69$ | 2.00$ | ✅ activa |
| STREAK_FADE_5M | 362 | 46.7% | -0.033 | ➡️ estable | -26.08$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 152 | 20.4% | -0.292 | 📈 madura (+0.12) | -27.06$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_15M | 218 | 37.6% | -0.123 | 📉 agota (-0.05) | -33.05$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 406 | 44.1% | -0.059 | 📉 agota (-0.09) | -33.13$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 375 | 31.5% | -0.184 | 📉 agota (-0.05) | -67.63$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3487 | 70.0% | +0.200 | ➡️ estable | -206.92$ | 1.99$ | ✅ activa |
| BALLENAS_TARDIAS | 4385 | 46.6% | -0.034 | 📈 madura (+0.08) | -716.72$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 33685 | 61.5% | +0.115 | ➡️ estable | -1092.46$ | 1.09$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 16042 | 69.7% | +0.197 | ➡️ estable | -1260.03$ | 1.99$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-12T18:05 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ✅ WIN | +0.14$ |
| 2026-08-12T18:05 | BALLENAS_TARDIAS#SOL#5min | … | ✅ WIN | +0.18$ |
| 2026-08-12T18:05 | BALLENAS_TARDIAS#XRP#5min | … | ✅ WIN | +0.14$ |
| 2026-08-12T18:05 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | … | ✅ WIN | +0.43$ |
| 2026-08-12T18:05 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | … | ✅ WIN | +0.28$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-12T18:02 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,424.00 | 0.1min |  |
| ✅ ETH | $1,886.39 | 0.1min |  |
| ✅ SOL | $75.88 | 0.1min |  |
| ✅ XRP | $1.01 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,411.35 | consenso |  |
| ETH | $1,886.86 | consenso |  |
| SOL | $75.89 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*