# Estado del bot — 2026-08-11 04:26 UTC

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
| P&L fiel (stake fijo 1$) | +6222.86 $ |
| P&L sim compuesto | 🟢 +15181.27 $ (ficción Kelly: +59675% s/ operativo) |
| P&L sim hoy (2026-08-11) | 🟢 +13.15 $ |
| Operaciones resueltas | 108867 (66926 WIN / 41941 LOSS) — 61.5% |
| Señales abiertas | 492 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11248 | 61.9% | +0.119 | ➡️ estable | +5553.43$ | 1.19$ | ✅ activa |
| GBM_LATE_15M | 13579 | 60.3% | +0.103 | ➡️ estable | +4630.12$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10369 | 59.4% | +0.094 | 📈 madura (+0.05) | +3915.98$ | 0.94$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3594 | 65.9% | +0.159 | ➡️ estable | +1817.18$ | 1.59$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 993 | 74.7% | +0.247 | 📈 madura (+0.06) | +910.49$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4066 | 55.9% | +0.059 | 📈 madura (+0.07) | +559.64$ | 0.59$ | ✅ activa |
| WEEKLY_PRICE | 732 | 77.9% | +0.278 | 📈 madura (+0.16) | +326.70$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 445 | 54.6% | +0.046 | 📉 agota (-0.13) | +96.50$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 159 | 76.7% | +0.264 | 📉 agota (-0.03) | +83.84$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 326 | 80.7% | +0.305 | ➡️ estable | +64.41$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1633 | 49.1% | -0.009 | 📈 madura (+0.05) | +43.44$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1733 | 62.7% | +0.127 | ➡️ estable | +17.95$ | 1.27$ | ✅ activa |
| ORDER_FLOW_5M | 1726 | 51.4% | +0.014 | ➡️ estable | +15.92$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 416 | 42.3% | -0.077 | 📈 madura (+0.10) | +13.94$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.52$ | ✅ activa |
| STRUCT_NO_15M | 817 | 52.8% | +0.027 | ➡️ estable | +9.24$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 32 | 81.2% | +0.294 | 📉 agota (-0.11) | +6.65$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 176 | 54.0% | +0.039 | ➡️ estable | -0.87$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 145 | 93.8% | +0.432 | 📈 madura (+0.04) | -1.08$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 7 | 28.6% | -0.058 | — | -1.60$ | 0.50$ | ⏳ acumulando |
| BALLENAS_CONFIRMADAS_15M | 1903 | 55.1% | +0.051 | 📉 agota (-0.15) | -1.71$ | 0.51$ | ✅ activa |
| LIQUIDACIONES_60M | 153 | 51.6% | +0.016 | ➡️ estable | -1.79$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 52 | 21.2% | -0.278 | 📉 agota (-0.11) | -13.27$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 137 | 87.6% | +0.371 | 📈 madura (+0.10) | -15.87$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 659 | 79.5% | +0.294 | 📉 agota (-0.03) | -16.84$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 86 | 31.4% | -0.182 | ➡️ estable | -17.18$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 360 | 77.8% | +0.276 | 📉 agota (-0.08) | -17.28$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_15M | 142 | 38.7% | -0.111 | ➡️ estable | -20.04$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 251 | 44.6% | -0.053 | 📉 agota (-0.08) | -26.50$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 325 | 43.7% | -0.063 | 📉 agota (-0.10) | -27.91$ | 0.50$ | 🚫 desactivada |
| GBM_LATE_60M_FADE | 135 | 18.5% | -0.310 | 📈 madura (+0.07) | -27.97$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 347 | 32.0% | -0.179 | 📉 agota (-0.03) | -61.22$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3034 | 70.1% | +0.201 | ➡️ estable | -188.90$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 3354 | 45.3% | -0.047 | 📈 madura (+0.06) | -633.53$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 30386 | 61.8% | +0.118 | ➡️ estable | -794.08$ | 1.18$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 14040 | 70.0% | +0.200 | ➡️ estable | -1013.44$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-11T04:25 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | … | ✅ WIN | +0.43$ |
| 2026-08-11T04:25 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | … | ✅ WIN | +0.43$ |
| 2026-08-11T04:25 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - August 11, 12:00AM-12:15AM E… | ✅ WIN | +3.45$ |
| 2026-08-11T04:25 | FAVORITO_CONFIRMADO#BNB#5min | … | ✅ WIN | +0.80$ |
| 2026-08-11T04:25 | FAVORITO_CONFIRMADO#DOGE#5min | … | ✅ WIN | +0.80$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-11T04:23 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,054.06 | 0.1min |  |
| ✅ ETH | $1,878.06 | 0.1min |  |
| ✅ SOL | $76.18 | 0.1min |  |
| ✅ XRP | $1.01 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,055.60 | consenso |  |
| ETH | $1,878.06 | consenso |  |
| SOL | $76.10 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*