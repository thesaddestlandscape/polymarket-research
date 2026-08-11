# Estado del bot — 2026-08-11 16:36 UTC

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
| P&L fiel (stake fijo 1$) | +6155.94 $ |
| P&L sim compuesto | 🟢 +15304.88 $ (ficción Kelly: +60161% s/ operativo) |
| P&L sim hoy (2026-08-11) | 🟢 +136.76 $ |
| Operaciones resueltas | 112275 (68973 WIN / 43302 LOSS) — 61.4% |
| Señales abiertas | 601 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11430 | 61.7% | +0.117 | ➡️ estable | +5607.67$ | 0.59$ | ✅ activa |
| GBM_LATE_15M | 13724 | 60.3% | +0.103 | ➡️ estable | +4701.98$ | 1.12$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10473 | 59.5% | +0.095 | 📈 madura (+0.05) | +3996.58$ | 1.90$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3611 | 65.8% | +0.158 | ➡️ estable | +1812.16$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1093 | 74.3% | +0.242 | 📈 madura (+0.06) | +992.91$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4119 | 55.8% | +0.058 | 📈 madura (+0.06) | +557.40$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 756 | 77.9% | +0.278 | 📈 madura (+0.14) | +334.57$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 463 | 54.9% | +0.048 | 📉 agota (-0.14) | +100.60$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 162 | 76.5% | +0.262 | 📉 agota (-0.05) | +82.81$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 329 | 80.5% | +0.304 | ➡️ estable | +63.37$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1691 | 49.8% | -0.002 | 📈 madura (+0.07) | +60.84$ | 0.93$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1973 | 63.2% | +0.132 | ➡️ estable | +39.95$ | 1.32$ | ✅ activa |
| GBM_LATE_60M | 422 | 42.7% | -0.073 | 📈 madura (+0.10) | +31.37$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1731 | 51.4% | +0.014 | ➡️ estable | +15.29$ | 0.53$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 895 | 52.4% | +0.024 | ➡️ estable | +7.00$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1922 | 55.2% | +0.051 | 📉 agota (-0.15) | +5.99$ | 0.75$ | ✅ activa |
| RESOLUTION_SNIPER | 34 | 76.5% | +0.250 | 📉 agota (-0.21) | +5.63$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 198 | 53.0% | +0.030 | ➡️ estable | +0.36$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 149 | 94.0% | +0.434 | 📈 madura (+0.04) | -0.58$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 8 | 25.0% | -0.080 | — | -2.11$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_60M | 165 | 50.9% | +0.009 | ➡️ estable | -3.18$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 196 | 33.7% | -0.162 | 📉 agota (-0.08) | -6.64$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 142 | 88.0% | +0.375 | 📈 madura (+0.12) | -15.21$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM_FADE | 61 | 21.3% | -0.278 | 📉 agota (-0.10) | -15.54$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 668 | 79.5% | +0.294 | ➡️ estable | -15.59$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 109 | 34.9% | -0.149 | 📈 madura (+0.06) | -18.06$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 371 | 77.6% | +0.275 | 📉 agota (-0.08) | -20.29$ | 2.00$ | ✅ activa |
| STREAK_FADE_5M | 284 | 47.2% | -0.028 | 📈 madura (+0.07) | -21.53$ | 1.15$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 162 | 38.9% | -0.110 | ➡️ estable | -23.20$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 140 | 18.6% | -0.310 | 📈 madura (+0.08) | -28.09$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 358 | 42.7% | -0.072 | 📉 agota (-0.12) | -33.66$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 353 | 31.7% | -0.182 | 📉 agota (-0.04) | -62.59$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3178 | 70.3% | +0.203 | ➡️ estable | -186.20$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 3712 | 45.6% | -0.044 | 📈 madura (+0.09) | -684.05$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 31430 | 61.7% | +0.117 | ➡️ estable | -869.92$ | 1.14$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 14651 | 69.8% | +0.198 | ➡️ estable | -1108.82$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-11T16:35 | BALLENAS_TARDIAS#BNB#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-11T16:35 | STREAK_FADE_5M#SOL#5min | Solana Up or Down - August 11, 12:10PM-12:15PM ET… | ✅ WIN | +0.50$ |
| 2026-08-11T16:35 | STREAK_MOM_5M#SOL#5min | Solana Up or Down - August 11, 12:10PM-12:15PM ET… | ❌ LOSS | -0.51$ |
| 2026-08-11T16:35 | GBM_LATE_5M#SOL#5min | Solana Up or Down - August 11, 12:10PM-12:15PM ET… | ❌ LOSS | -2.04$ |
| 2026-08-11T16:35 | BALLENAS_TARDIAS#XRP#5min | … | ✅ WIN | +0.31$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-11T16:31 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,557.12 | 0.2min |  |
| ✅ ETH | $1,863.98 | 0.2min |  |
| ✅ SOL | $74.95 | 0.2min |  |
| ✅ XRP | $1.01 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,557.12 | consenso |  |
| ETH | $1,863.98 | consenso |  |
| SOL | $74.95 | consenso |  |
| XRP | $1.01 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*