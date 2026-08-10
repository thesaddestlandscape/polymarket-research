# Estado del bot — 2026-08-10 16:44 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **9.03 $** |
| P&L real total | 🔴 **-42.19 $** |
| P&L real hoy | -1.03 $ |
| P&L real 7 días | -10.48 $ |
| Fees pagados (real) | 15.12 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6173.68 $ |
| P&L sim compuesto | 🟢 +14887.29 $ (ficción Kelly: +58519% s/ operativo) |
| P&L sim hoy (2026-08-10) | 🟢 +511.81 $ |
| Operaciones resueltas | 105853 (65018 WIN / 40835 LOSS) — 61.4% |
| Señales abiertas | 553 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11099 | 62.1% | +0.121 | ➡️ estable | +5400.37$ | 1.21$ | ✅ activa |
| GBM_LATE_15M | 13458 | 60.2% | +0.102 | ➡️ estable | +4570.14$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10275 | 59.3% | +0.093 | 📈 madura (+0.04) | +3837.91$ | 0.93$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3573 | 66.0% | +0.160 | ➡️ estable | +1810.68$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 917 | 74.6% | +0.245 | 📈 madura (+0.06) | +842.59$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4050 | 55.9% | +0.059 | 📈 madura (+0.07) | +560.68$ | 0.59$ | ✅ activa |
| WEEKLY_PRICE | 732 | 77.9% | +0.278 | 📈 madura (+0.16) | +326.70$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 445 | 54.6% | +0.046 | 📉 agota (-0.13) | +96.50$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 152 | 76.3% | +0.260 | 📉 agota (-0.05) | +78.15$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 321 | 80.7% | +0.305 | ➡️ estable | +63.42$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1600 | 48.9% | -0.011 | 📈 madura (+0.04) | +37.40$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 406 | 42.4% | -0.076 | 📈 madura (+0.11) | +18.04$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1506 | 62.8% | +0.128 | ➡️ estable | +16.42$ | 1.28$ | ✅ activa |
| ORDER_FLOW_5M | 1725 | 51.4% | +0.014 | ➡️ estable | +15.43$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 757 | 53.2% | +0.032 | ➡️ estable | +14.61$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.52$ | ✅ activa |
| RESOLUTION_SNIPER | 32 | 81.2% | +0.294 | 📉 agota (-0.11) | +6.65$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 143 | 93.7% | +0.431 | 📈 madura (+0.04) | -1.36$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| LIQUIDACIONES_60M | 140 | 51.4% | +0.014 | ➡️ estable | -2.39$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 153 | 51.6% | +0.016 | ➡️ estable | -3.45$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| BALLENAS_CONFIRMADAS_15M | 1875 | 55.0% | +0.050 | 📉 agota (-0.16) | -9.96$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM_FADE | 52 | 21.2% | -0.278 | 📉 agota (-0.11) | -13.27$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 652 | 79.6% | +0.295 | ➡️ estable | -14.96$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 133 | 87.2% | +0.367 | 📈 madura (+0.10) | -16.48$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 86 | 31.4% | -0.182 | ➡️ estable | -17.18$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 124 | 37.1% | -0.127 | 📉 agota (-0.03) | -19.27$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 349 | 77.1% | +0.269 | 📉 agota (-0.10) | -23.60$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 130 | 18.5% | -0.311 | 📈 madura (+0.09) | -26.50$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 251 | 44.6% | -0.053 | 📉 agota (-0.08) | -26.50$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 325 | 43.7% | -0.063 | 📉 agota (-0.10) | -27.91$ | 0.50$ | 🚫 desactivada |
| UPDOWN_OU_5M | 344 | 32.3% | -0.176 | ➡️ estable | -59.69$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2885 | 70.1% | +0.200 | 📉 agota (-0.04) | -182.09$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 3065 | 44.3% | -0.057 | 📈 madura (+0.06) | -609.72$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 29344 | 61.8% | +0.118 | 📉 agota (-0.03) | -756.12$ | 1.18$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 13442 | 69.9% | +0.199 | ➡️ estable | -993.30$ | 1.99$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-10T16:43 | FAVORITO_CONFIRMADO#ETH#5min | … | ✅ WIN | +0.74$ |
| 2026-08-10T16:43 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | … | ✅ WIN | +0.80$ |
| 2026-08-10T16:43 | FAVORITO_CONFIRMADO#SOL#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-10T16:43 | FAVORITO_CONFIRMADO#XRP#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-10T16:43 | GBM_LATE_15M_ESPACIO_ATR#BNB#15min | … | ✅ WIN | +3.30$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-10T16:41 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,043.36 | 0.2min |  |
| ✅ ETH | $1,873.53 | 0.2min |  |
| ✅ SOL | $75.99 | 0.2min |  |
| ✅ XRP | $1.02 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,049.90 | consenso |  |
| ETH | $1,873.54 | consenso |  |
| SOL | $75.73 | consenso |  |
| XRP | $1.02 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*