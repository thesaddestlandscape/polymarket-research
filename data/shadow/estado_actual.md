# Estado del bot — 2026-08-11 02:58 UTC

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
| P&L fiel (stake fijo 1$) | +6220.25 $ |
| P&L sim compuesto | 🟢 +15144.61 $ (ficción Kelly: +59531% s/ operativo) |
| P&L sim hoy (2026-08-11) | 🔴 -23.51 $ |
| Operaciones resueltas | 108480 (66675 WIN / 41805 LOSS) — 61.5% |
| Señales abiertas | 471 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11228 | 61.9% | +0.119 | ➡️ estable | +5548.56$ | 1.19$ | ✅ activa |
| GBM_LATE_15M | 13565 | 60.2% | +0.102 | ➡️ estable | +4616.80$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10358 | 59.4% | +0.094 | 📈 madura (+0.05) | +3900.97$ | 0.94$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3593 | 65.9% | +0.159 | ➡️ estable | +1817.06$ | 1.59$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 986 | 74.6% | +0.246 | 📈 madura (+0.06) | +900.77$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4066 | 55.9% | +0.059 | 📈 madura (+0.07) | +559.64$ | 0.59$ | ✅ activa |
| WEEKLY_PRICE | 732 | 77.9% | +0.278 | 📈 madura (+0.16) | +326.70$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 445 | 54.6% | +0.046 | 📉 agota (-0.13) | +96.50$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 158 | 76.6% | +0.262 | 📉 agota (-0.04) | +83.54$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 325 | 80.6% | +0.304 | ➡️ estable | +64.11$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1631 | 49.1% | -0.009 | 📈 madura (+0.05) | +43.45$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1726 | 51.4% | +0.014 | ➡️ estable | +15.92$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 413 | 42.1% | -0.078 | 📈 madura (+0.09) | +14.15$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1702 | 62.6% | +0.126 | ➡️ estable | +12.89$ | 1.26$ | ✅ activa |
| STRUCT_NO_15M | 804 | 53.1% | +0.031 | ➡️ estable | +12.03$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.52$ | ✅ activa |
| RESOLUTION_SNIPER | 32 | 81.2% | +0.294 | 📉 agota (-0.11) | +6.65$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1898 | 55.1% | +0.051 | 📉 agota (-0.15) | +0.98$ | 0.51$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 144 | 93.8% | +0.432 | 📈 madura (+0.04) | -1.25$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 7 | 28.6% | -0.058 | — | -1.60$ | 0.50$ | ⏳ acumulando |
| LIQUIDACIONES_60M | 152 | 51.3% | +0.013 | ➡️ estable | -2.31$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 172 | 52.9% | +0.029 | ➡️ estable | -2.78$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 52 | 21.2% | -0.278 | 📉 agota (-0.11) | -13.27$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 135 | 87.4% | +0.369 | 📈 madura (+0.10) | -16.19$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 86 | 31.4% | -0.182 | ➡️ estable | -17.18$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 657 | 79.5% | +0.294 | 📉 agota (-0.03) | -17.69$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 358 | 77.7% | +0.275 | 📉 agota (-0.09) | -18.87$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_15M | 141 | 38.3% | -0.115 | ➡️ estable | -20.52$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 251 | 44.6% | -0.053 | 📉 agota (-0.08) | -26.50$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 134 | 18.7% | -0.309 | 📈 madura (+0.07) | -27.46$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 325 | 43.7% | -0.063 | 📉 agota (-0.10) | -27.91$ | 0.50$ | 🚫 desactivada |
| UPDOWN_OU_5M | 347 | 32.0% | -0.179 | 📉 agota (-0.03) | -61.22$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3010 | 70.1% | +0.201 | ➡️ estable | -186.37$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 3319 | 45.1% | -0.049 | 📈 madura (+0.06) | -633.01$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 30256 | 61.8% | +0.118 | ➡️ estable | -790.70$ | 1.18$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 13965 | 70.0% | +0.200 | ➡️ estable | -1008.17$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-11T02:57 | FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | … | ❌ LOSS | -1.07$ |
| 2026-08-11T02:57 | BALLENAS_TARDIAS#SOL#5min | … | ✅ WIN | +0.29$ |
| 2026-08-11T02:57 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | … | ✅ WIN | +0.35$ |
| 2026-08-11T02:57 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | … | ✅ WIN | +0.74$ |
| 2026-08-11T02:57 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ✅ WIN | +0.41$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-11T02:55 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,974.71 | 0.1min |  |
| ✅ ETH | $1,876.62 | 0.1min |  |
| ✅ SOL | $76.06 | 0.1min |  |
| ✅ XRP | $1.01 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,990.10 | consenso |  |
| ETH | $1,876.62 | consenso |  |
| SOL | $76.01 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*