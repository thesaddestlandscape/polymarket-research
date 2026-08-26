# Estado del bot — 2026-08-26 05:46 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| ⚠️ | Sin snapshot on-chain fresco (live_balance.py, cron 15min) |
| Fees pagados (real) | 16.12 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3965.12 $ |
| P&L sim compuesto | 🟢 +22033.62 $ (ficción Kelly: +86610% s/ operativo) |
| P&L sim hoy (2026-08-26) | 🟢 +375.22 $ |
| Operaciones resueltas | 267183 (155393 WIN / 111790 LOSS) — 58.2% |
| Señales abiertas | 1493 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 17646 | 59.0% | +0.090 | 📉 agota (-0.08) | +7857.86$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 16110 | 61.8% | +0.118 | 📈 madura (+0.09) | +7505.12$ | 1.66$ | ✅ activa |
| GBM_LATE_15M | 19348 | 58.0% | +0.080 | 📉 agota (-0.03) | +6202.89$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 5958 | 67.3% | +0.173 | ➡️ estable | +4085.86$ | 1.70$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 6964 | 54.3% | +0.043 | 📉 agota (-0.24) | +2252.75$ | 0.50$ | ✅ activa |
| GBM_LATE_5M | 3299 | 55.7% | +0.057 | 📈 madura (+0.13) | +727.38$ | 1.27$ | ✅ activa |
| UPDOWN_GBM | 9636 | 52.9% | +0.029 | 📉 agota (-0.05) | +705.00$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 1057 | 78.6% | +0.286 | 📈 madura (+0.06) | +427.80$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 1396 | 56.9% | +0.069 | 📈 madura (+0.05) | +282.49$ | 0.77$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 395 | 77.5% | +0.273 | ➡️ estable | +271.20$ | 2.00$ | ✅ activa |
| MOMENTUM_IBS_5M_BALLENA | 16277 | 42.7% | -0.073 | ➡️ estable | +260.14$ | 0.50$ | ⚠️ IC negativo |
| MOMENTUM_IBS_15M_BALLENA | 5930 | 46.5% | -0.035 | ➡️ estable | +196.58$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 8488 | 62.8% | +0.128 | ➡️ estable | +184.87$ | 1.31$ | ✅ activa |
| ORDER_FLOW_5M | 2001 | 52.8% | +0.028 | ➡️ estable | +102.56$ | 0.95$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 608 | 56.2% | +0.062 | 📈 madura (+0.12) | +95.43$ | 1.16$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 462 | 81.0% | +0.308 | ➡️ estable | +87.96$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 510 | 45.7% | -0.043 | 📈 madura (+0.14) | +82.86$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 176 | 33.5% | -0.163 | 📈 madura (+0.21) | +30.67$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 742 | 80.3% | +0.302 | 📈 madura (+0.05) | +12.43$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 54 | 77.8% | +0.268 | ➡️ estable | +9.77$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 2288 | 55.8% | +0.058 | 📉 agota (-0.14) | +9.43$ | 0.86$ | ✅ activa |
| STREAK_FADE_15M | 445 | 53.9% | +0.039 | 📉 agota (-0.11) | +8.73$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 321 | 53.9% | +0.039 | 📈 madura (+0.04) | +4.32$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 199 | 60.3% | +0.102 | ➡️ estable | +1.56$ | 1.02$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 368 | 94.3% | +0.441 | 📈 madura (+0.04) | +0.32$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 58 | 50.0% | +0.000 | 📉 agota (-0.03) | -0.66$ | 0.50$ | ✅ activa |
| STREAK_MOM_5M | 2376 | 51.0% | +0.010 | ➡️ estable | -1.79$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 407 | 45.2% | -0.048 | 📉 agota (-0.10) | -1.87$ | 1.67$ | ⚠️ IC negativo |
| STREAK_FADE_60M | 29 | 41.4% | -0.081 | — | -3.00$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_60M | 417 | 48.7% | -0.013 | 📉 agota (-0.08) | -6.97$ | 0.50$ | ⚠️ IC negativo |
| MOMENTUM_IBS_5M | 3130 | 50.3% | +0.003 | ➡️ estable | -7.94$ | 0.50$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 314 | 91.4% | +0.411 | 📈 madura (+0.04) | -15.22$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM | 256 | 33.6% | -0.163 | ➡️ estable | -20.27$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 3090 | 50.8% | +0.008 | ➡️ estable | -27.67$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 996 | 79.5% | +0.295 | ➡️ estable | -28.76$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 193 | 19.2% | -0.305 | 📈 madura (+0.11) | -34.48$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_15M | 270 | 38.9% | -0.110 | 📈 madura (+0.04) | -36.66$ | 0.50$ | ⚠️ IC negativo |
| MOMENTUM_IBS_15M_FADE | 554 | 44.0% | -0.059 | 📈 madura (+0.06) | -41.50$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 1425 | 49.0% | -0.010 | ➡️ estable | -51.03$ | 0.50$ | ⚠️ IC negativo |
| MOMENTUM_IBS_15M | 4038 | 50.0% | +0.000 | ➡️ estable | -56.13$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_5M | 718 | 42.8% | -0.072 | 📈 madura (+0.16) | -60.26$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 802 | 37.2% | -0.128 | 📈 madura (+0.10) | -106.33$ | 0.50$ | ⚠️ IC negativo |
| MOMENTUM_IBS_5M_FADE | 6011 | 49.0% | -0.010 | 📉 agota (-0.05) | -119.48$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_DEPTH_FASE0 | 5412 | 59.7% | +0.097 | ➡️ estable | -192.87$ | 0.97$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 7373 | 68.2% | +0.182 | 📉 agota (-0.04) | -554.11$ | 1.74$ | ✅ activa |
| BALLENAS_TARDIAS | 13998 | 42.0% | -0.080 | 📉 agota (-0.03) | -2111.01$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 32640 | 69.5% | +0.195 | ➡️ estable | -2688.25$ | 1.93$ | ✅ activa |
| FAVORITO_CONFIRMADO | 61969 | 61.0% | +0.110 | ➡️ estable | -3192.30$ | 1.14$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-26T05:43 | UPDOWN_GBM_15M_TARDIO#BTC#15min | Bitcoin Up or Down - August 26, 1:15AM-1:30AM ET… | ✅ WIN | +1.35$ |
| 2026-08-26T05:42 | GBM_LATE_5M#BNB#5min | BNB Up or Down - August 26, 1:30AM-1:35AM ET… | ✅ WIN | +1.83$ |
| 2026-08-26T05:42 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | … | ❌ LOSS | -1.07$ |
| 2026-08-26T05:42 | UPDOWN_GBM#SOL#5min | Solana Up or Down - August 26, 1:25AM-1:30AM ET… | ✅ WIN | +0.50$ |
| 2026-08-26T05:42 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - August 26, 1:15AM-1:30AM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-26T05:46 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $79,074.29 | 0.1min |  |
| ✅ ETH | $2,464.66 | 0.1min |  |
| ✅ SOL | $97.10 | 0.1min |  |
| ✅ XRP | $1.44 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $79,074.29 | consenso |  |
| ETH | $2,464.11 | consenso |  |
| SOL | $97.12 | consenso |  |
| XRP | $1.44 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*