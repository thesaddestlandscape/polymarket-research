# Estado del bot — 2026-08-11 08:06 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **10.30 $** |
| P&L real total | 🔴 **-40.92 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -11.75 $ |
| Fees pagados (real) | 15.20 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6202.87 $ |
| P&L sim compuesto | 🟢 +15232.67 $ (ficción Kelly: +59877% s/ operativo) |
| P&L sim hoy (2026-08-11) | 🟢 +64.55 $ |
| Operaciones resueltas | 109789 (67483 WIN / 42306 LOSS) — 61.5% |
| Señales abiertas | 556 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11297 | 61.9% | +0.119 | ➡️ estable | +5575.58$ | 0.63$ | ✅ activa |
| GBM_LATE_15M | 13621 | 60.3% | +0.103 | ➡️ estable | +4664.06$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10408 | 59.4% | +0.094 | 📈 madura (+0.05) | +3947.09$ | 1.93$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3597 | 65.9% | +0.159 | ➡️ estable | +1815.81$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1029 | 74.8% | +0.248 | 📈 madura (+0.06) | +944.17$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4071 | 55.9% | +0.059 | 📈 madura (+0.07) | +561.22$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 732 | 77.9% | +0.278 | 📈 madura (+0.16) | +326.70$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 448 | 54.7% | +0.047 | 📉 agota (-0.13) | +98.56$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 160 | 76.9% | +0.265 | 📉 agota (-0.04) | +84.04$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 327 | 80.7% | +0.305 | ➡️ estable | +64.60$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1647 | 49.2% | -0.008 | 📈 madura (+0.05) | +43.85$ | 0.64$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1804 | 63.4% | +0.134 | ➡️ estable | +39.43$ | 1.34$ | ✅ activa |
| GBM_LATE_60M | 420 | 42.4% | -0.076 | 📈 madura (+0.09) | +19.21$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1728 | 51.4% | +0.014 | ➡️ estable | +16.96$ | 0.57$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 835 | 53.1% | +0.030 | ➡️ estable | +12.25$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.00$ | 🚫 desactivada |
| RESOLUTION_SNIPER | 32 | 81.2% | +0.294 | 📉 agota (-0.11) | +6.65$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 182 | 53.8% | +0.038 | ➡️ estable | +1.22$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 146 | 93.8% | +0.432 | 📈 madura (+0.04) | -0.91$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1907 | 55.1% | +0.051 | 📉 agota (-0.15) | -1.27$ | 0.73$ | ✅ activa |
| STREAK_FADE_60M | 7 | 28.6% | -0.058 | — | -1.60$ | 0.50$ | ⏳ acumulando |
| LIQUIDACIONES_60M | 157 | 51.6% | +0.016 | ➡️ estable | -1.94$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 52 | 21.2% | -0.278 | 📉 agota (-0.11) | -13.27$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 137 | 87.6% | +0.371 | 📈 madura (+0.10) | -15.87$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 660 | 79.5% | +0.295 | 📉 agota (-0.03) | -16.23$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 360 | 77.8% | +0.276 | 📉 agota (-0.08) | -17.28$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 87 | 31.0% | -0.185 | ➡️ estable | -17.69$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 142 | 38.7% | -0.111 | ➡️ estable | -20.04$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 254 | 45.3% | -0.047 | 📉 agota (-0.05) | -25.04$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 138 | 18.8% | -0.307 | 📈 madura (+0.08) | -27.07$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 328 | 43.3% | -0.067 | 📉 agota (-0.12) | -29.44$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 347 | 32.0% | -0.179 | 📉 agota (-0.03) | -61.22$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3073 | 70.0% | +0.200 | ➡️ estable | -193.29$ | 1.98$ | ✅ activa |
| BALLENAS_TARDIAS | 3445 | 45.3% | -0.047 | 📈 madura (+0.06) | -656.35$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 30700 | 61.7% | +0.117 | ➡️ estable | -829.97$ | 1.15$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 14204 | 69.9% | +0.199 | ➡️ estable | -1057.15$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-11T08:05 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | … | ✅ WIN | +0.06$ |
| 2026-08-11T08:05 | BALLENAS_TARDIAS#SOL#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-11T08:05 | BALLENAS_TARDIAS#ETH#5min | … | ✅ WIN | +0.35$ |
| 2026-08-11T08:05 | BALLENAS_TARDIAS#XRP#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-11T08:05 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | … | ❌ LOSS | -1.07$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-11T08:02 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,017.00 | 0.1min |  |
| ✅ ETH | $1,876.25 | 0.1min |  |
| ✅ SOL | $75.65 | 0.1min |  |
| ✅ XRP | $1.00 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,043.30 | consenso |  |
| ETH | $1,877.20 | consenso |  |
| SOL | $75.69 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*