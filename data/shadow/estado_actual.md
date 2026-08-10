# Estado del bot — 2026-08-10 21:58 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **43.17 $** |
| P&L real total | 🔴 **-8.05 $** |
| P&L real hoy | +33.11 $ |
| P&L real 7 días | +23.66 $ |
| Fees pagados (real) | 15.20 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6189.66 $ |
| P&L sim compuesto | 🟢 +15066.26 $ (ficción Kelly: +59223% s/ operativo) |
| P&L sim hoy (2026-08-10) | 🟢 +690.78 $ |
| Operaciones resueltas | 107231 (65884 WIN / 41347 LOSS) — 61.4% |
| Señales abiertas | 672 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11171 | 62.0% | +0.120 | ➡️ estable | +5526.25$ | 1.20$ | ✅ activa |
| GBM_LATE_15M | 13521 | 60.2% | +0.102 | ➡️ estable | +4589.77$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10319 | 59.4% | +0.094 | 📈 madura (+0.05) | +3872.11$ | 0.94$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3587 | 66.0% | +0.160 | ➡️ estable | +1817.65$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 951 | 74.7% | +0.246 | 📈 madura (+0.07) | +871.00$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4057 | 55.9% | +0.059 | 📈 madura (+0.07) | +566.04$ | 0.59$ | ✅ activa |
| WEEKLY_PRICE | 732 | 77.9% | +0.278 | 📈 madura (+0.16) | +326.70$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 445 | 54.6% | +0.046 | 📉 agota (-0.13) | +96.50$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 156 | 76.9% | +0.266 | 📉 agota (-0.05) | +85.26$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 323 | 80.8% | +0.306 | ➡️ estable | +65.82$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1612 | 48.8% | -0.012 | 📈 madura (+0.04) | +33.62$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1610 | 62.8% | +0.128 | ➡️ estable | +18.28$ | 1.28$ | ✅ activa |
| GBM_LATE_60M | 409 | 42.5% | -0.074 | 📈 madura (+0.10) | +17.11$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1725 | 51.4% | +0.014 | ➡️ estable | +15.43$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.52$ | ✅ activa |
| STRUCT_NO_15M | 781 | 52.9% | +0.029 | ➡️ estable | +9.06$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 32 | 81.2% | +0.294 | 📉 agota (-0.11) | +6.65$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1891 | 55.2% | +0.052 | 📉 agota (-0.15) | +5.05$ | 0.52$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 144 | 93.8% | +0.432 | 📈 madura (+0.04) | -1.25$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 164 | 53.0% | +0.030 | ➡️ estable | -1.44$ | 0.50$ | ✅ activa |
| STREAK_FADE_60M | 6 | 16.7% | -0.075 | — | -2.08$ | 0.50$ | ⏳ acumulando |
| LIQUIDACIONES_60M | 147 | 50.3% | +0.003 | 📉 agota (-0.03) | -4.36$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 52 | 21.2% | -0.278 | 📉 agota (-0.11) | -13.27$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 654 | 79.7% | +0.296 | ➡️ estable | -14.54$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 135 | 87.4% | +0.369 | 📈 madura (+0.10) | -16.19$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 86 | 31.4% | -0.182 | ➡️ estable | -17.18$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 139 | 38.1% | -0.117 | ➡️ estable | -20.45$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 354 | 77.4% | +0.272 | 📉 agota (-0.10) | -20.94$ | 2.00$ | ✅ activa |
| STREAK_FADE_5M | 251 | 44.6% | -0.053 | 📉 agota (-0.08) | -26.50$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 132 | 18.2% | -0.313 | 📈 madura (+0.06) | -27.52$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 325 | 43.7% | -0.063 | 📉 agota (-0.10) | -27.91$ | 0.50$ | 🚫 desactivada |
| UPDOWN_OU_5M | 347 | 32.0% | -0.179 | 📉 agota (-0.03) | -61.22$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2951 | 69.9% | +0.199 | ➡️ estable | -191.01$ | 1.99$ | ✅ activa |
| BALLENAS_TARDIAS | 3186 | 45.0% | -0.050 | 📈 madura (+0.06) | -620.09$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 29811 | 61.8% | +0.118 | ➡️ estable | -782.63$ | 1.18$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 13718 | 70.0% | +0.200 | ➡️ estable | -1004.36$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-10T21:56 | FAVORITO_CONFIRMADO#BTC#5min | … | ✅ WIN | +0.52$ |
| 2026-08-10T21:56 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-10T21:56 | FAVORITO_CONFIRMADO#XRP#5min | … | ✅ WIN | +0.16$ |
| 2026-08-10T21:56 | FAVORITO_CONFIRMADO#BNB#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-10T21:56 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | … | ✅ WIN | +0.28$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-10T21:54 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,933.75 | 0.1min |  |
| ✅ ETH | $1,872.62 | 0.1min |  |
| ✅ SOL | $76.30 | 0.1min |  |
| ✅ XRP | $1.02 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,936.10 | consenso |  |
| ETH | $1,873.34 | consenso |  |
| SOL | $76.26 | consenso |  |
| XRP | $1.02 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*