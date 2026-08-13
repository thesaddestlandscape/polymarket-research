# Estado del bot — 2026-08-13 13:05 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 61.22 $ |
| Balance on-chain | **15.97 $** |
| P&L real total | 🔴 **-45.25 $** |
| P&L real hoy | -2.18 $ |
| P&L real 7 días | -5.93 $ |
| Fees pagados (real) | 15.55 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6019.14 $ |
| P&L sim compuesto | 🟢 +16080.71 $ (ficción Kelly: +63210% s/ operativo) |
| P&L sim hoy (2026-08-13) | 🟢 +340.92 $ |
| Operaciones resueltas | 126403 (77412 WIN / 48991 LOSS) — 61.2% |
| Señales abiertas | 483 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 12359 | 61.3% | +0.113 | ➡️ estable | +5850.44$ | 0.57$ | ✅ activa |
| GBM_LATE_15M | 14489 | 60.2% | +0.102 | ➡️ estable | +4987.88$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 11114 | 60.1% | +0.101 | 📈 madura (+0.07) | +4504.38$ | 1.92$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3988 | 63.8% | +0.138 | 📉 agota (-0.03) | +1820.26$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1640 | 72.3% | +0.222 | ➡️ estable | +1394.20$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4586 | 55.5% | +0.055 | 📈 madura (+0.05) | +584.64$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 780 | 77.9% | +0.279 | 📈 madura (+0.14) | +342.55$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1893 | 50.6% | +0.006 | 📈 madura (+0.07) | +99.93$ | 0.84$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 677 | 54.1% | +0.041 | ➡️ estable | +95.17$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 189 | 76.2% | +0.259 | 📉 agota (-0.07) | +93.60$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 350 | 79.7% | +0.295 | ➡️ estable | +56.33$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 440 | 43.6% | -0.063 | 📈 madura (+0.12) | +45.10$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1744 | 51.5% | +0.015 | ➡️ estable | +18.39$ | 0.58$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2835 | 62.2% | +0.121 | ➡️ estable | +15.48$ | 1.21$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 331 | 55.3% | +0.053 | 📉 agota (-0.14) | +11.71$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 38 | 78.9% | +0.275 | 📉 agota (-0.10) | +6.65$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 237 | 54.4% | +0.044 | 📈 madura (+0.04) | +4.46$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 35 | 48.6% | -0.014 | 📉 agota (-0.08) | -0.09$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 171 | 93.6% | +0.431 | ➡️ estable | -2.17$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_60M | 210 | 52.4% | +0.024 | 📉 agota (-0.04) | -2.26$ | 0.50$ | ✅ activa |
| STREAK_FADE_60M | 12 | 25.0% | -0.129 | — | -3.21$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 198 | 34.3% | -0.155 | 📉 agota (-0.08) | -6.26$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 396 | 43.9% | -0.060 | 📉 agota (-0.13) | -6.46$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 1165 | 51.2% | +0.012 | ➡️ estable | -7.81$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 2027 | 54.5% | +0.045 | 📉 agota (-0.18) | -10.88$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 164 | 89.6% | +0.392 | 📈 madura (+0.11) | -12.77$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM_FADE | 70 | 21.4% | -0.278 | 📉 agota (-0.08) | -17.69$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 414 | 78.0% | +0.279 | 📉 agota (-0.04) | -18.15$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 129 | 36.4% | -0.134 | 📈 madura (+0.13) | -18.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 409 | 47.9% | -0.021 | 📈 madura (+0.04) | -21.08$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 718 | 78.8% | +0.287 | 📉 agota (-0.03) | -26.21$ | 2.00$ | ✅ activa |
| STREAK_MOM_5M | 426 | 45.1% | -0.049 | 📉 agota (-0.05) | -26.72$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 159 | 20.1% | -0.295 | 📈 madura (+0.12) | -28.88$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_15M | 237 | 38.8% | -0.111 | ➡️ estable | -33.36$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 387 | 31.5% | -0.184 | 📉 agota (-0.05) | -68.86$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3712 | 70.0% | +0.200 | ➡️ estable | -218.59$ | 1.99$ | ✅ activa |
| BALLENAS_TARDIAS | 4964 | 46.8% | -0.032 | 📈 madura (+0.07) | -772.30$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 35339 | 61.4% | +0.114 | ➡️ estable | -1213.90$ | 1.07$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 17015 | 69.8% | +0.198 | ➡️ estable | -1333.07$ | 1.99$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-13T13:05 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | … | ✅ WIN | +0.43$ |
| 2026-08-13T13:05 | BALLENAS_TARDIAS#SOL#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-13T13:05 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ✅ WIN | +0.19$ |
| 2026-08-13T13:05 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | … | ✅ WIN | +0.41$ |
| 2026-08-13T13:05 | BALLENAS_TARDIAS#ETH#5min | … | ✅ WIN | +3.70$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-13T13:02 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,686.14 | 0.2min |  |
| ✅ ETH | $1,888.47 | 0.2min |  |
| ✅ SOL | $76.08 | 0.2min |  |
| ✅ XRP | $1.01 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,689.10 | consenso |  |
| ETH | $1,888.47 | consenso |  |
| SOL | $76.08 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*