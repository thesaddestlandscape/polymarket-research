# Estado del bot — 2026-08-11 17:05 UTC

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
| P&L fiel (stake fijo 1$) | +6145.79 $ |
| P&L sim compuesto | 🟢 +15299.24 $ (ficción Kelly: +60139% s/ operativo) |
| P&L sim hoy (2026-08-11) | 🟢 +131.12 $ |
| Operaciones resueltas | 112411 (69053 WIN / 43358 LOSS) — 61.4% |
| Señales abiertas | 598 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11436 | 61.7% | +0.117 | ➡️ estable | +5605.12$ | 0.59$ | ✅ activa |
| GBM_LATE_15M | 13727 | 60.3% | +0.103 | ➡️ estable | +4701.62$ | 1.11$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10475 | 59.5% | +0.095 | 📈 madura (+0.05) | +3996.52$ | 1.90$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3611 | 65.8% | +0.158 | ➡️ estable | +1812.16$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1094 | 74.3% | +0.243 | 📈 madura (+0.06) | +993.45$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4121 | 55.8% | +0.058 | 📈 madura (+0.06) | +558.57$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 756 | 77.9% | +0.278 | 📈 madura (+0.14) | +334.57$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 464 | 54.7% | +0.047 | 📉 agota (-0.14) | +100.09$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 162 | 76.5% | +0.262 | 📉 agota (-0.05) | +82.81$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 329 | 80.5% | +0.304 | ➡️ estable | +63.37$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1694 | 49.8% | -0.002 | 📈 madura (+0.07) | +61.64$ | 0.94$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1984 | 63.2% | +0.131 | ➡️ estable | +39.07$ | 1.31$ | ✅ activa |
| GBM_LATE_60M | 422 | 42.7% | -0.073 | 📈 madura (+0.10) | +31.37$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1731 | 51.4% | +0.014 | ➡️ estable | +15.29$ | 0.53$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 895 | 52.4% | +0.024 | ➡️ estable | +7.00$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 34 | 76.5% | +0.250 | 📉 agota (-0.21) | +5.63$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1925 | 55.1% | +0.051 | 📉 agota (-0.16) | +3.44$ | 0.72$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 198 | 53.0% | +0.030 | ➡️ estable | +0.36$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 149 | 94.0% | +0.434 | 📈 madura (+0.04) | -0.58$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 8 | 25.0% | -0.080 | — | -2.11$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_60M | 165 | 50.9% | +0.009 | ➡️ estable | -3.18$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 196 | 33.7% | -0.162 | 📉 agota (-0.08) | -6.64$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 669 | 79.5% | +0.294 | ➡️ estable | -15.08$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 142 | 88.0% | +0.375 | 📈 madura (+0.12) | -15.21$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM_FADE | 61 | 21.3% | -0.278 | 📉 agota (-0.10) | -15.54$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_5M | 111 | 35.1% | -0.146 | 📈 madura (+0.08) | -18.02$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 371 | 77.6% | +0.275 | 📉 agota (-0.08) | -20.29$ | 2.00$ | ✅ activa |
| STREAK_FADE_5M | 286 | 47.2% | -0.028 | 📈 madura (+0.08) | -21.58$ | 1.10$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 162 | 38.9% | -0.110 | ➡️ estable | -23.20$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 140 | 18.6% | -0.310 | 📈 madura (+0.08) | -28.09$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 360 | 42.8% | -0.072 | 📉 agota (-0.11) | -33.69$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 353 | 31.7% | -0.182 | 📉 agota (-0.04) | -62.59$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3186 | 70.2% | +0.202 | ➡️ estable | -189.81$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 3727 | 45.7% | -0.043 | 📈 madura (+0.09) | -680.19$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 31473 | 61.7% | +0.117 | ➡️ estable | -865.93$ | 1.15$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 14682 | 69.8% | +0.198 | ➡️ estable | -1114.77$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-11T17:04 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ✅ WIN | +0.31$ |
| 2026-08-11T17:04 | UPDOWN_GBM#ETH#5min | Ethereum Up or Down - August 11, 12:45PM-12:50PM E… | ❌ LOSS | -0.56$ |
| 2026-08-11T17:04 | FAVORITO_CONFIRMADO#ETH#5min | … | ✅ WIN | +0.80$ |
| 2026-08-11T17:04 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-11T17:04 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | … | ❌ LOSS | -1.07$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-11T17:01 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,467.28 | 0.2min |  |
| ✅ ETH | $1,864.61 | 0.2min |  |
| ✅ SOL | $74.94 | 0.2min |  |
| ✅ XRP | $1.01 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,467.28 | consenso |  |
| ETH | $1,864.61 | consenso |  |
| SOL | $74.94 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*