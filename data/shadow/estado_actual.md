# Estado del bot — 2026-08-10 07:10 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **8.98 $** |
| P&L real total | 🔴 **-42.24 $** |
| P&L real hoy | -1.08 $ |
| P&L real 7 días | -10.53 $ |
| Fees pagados (real) | 15.06 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6172.83 $ |
| P&L sim compuesto | 🟢 +14696.18 $ (ficción Kelly: +57768% s/ operativo) |
| P&L sim hoy (2026-08-10) | 🟢 +320.70 $ |
| Operaciones resueltas | 103359 (63489 WIN / 39870 LOSS) — 61.4% |
| Señales abiertas | 507 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 10935 | 62.1% | +0.121 | ➡️ estable | +5334.80$ | 1.21$ | ✅ activa |
| GBM_LATE_15M | 13334 | 60.2% | +0.102 | ➡️ estable | +4515.65$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10188 | 59.2% | +0.092 | 📈 madura (+0.04) | +3782.85$ | 0.92$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3556 | 66.1% | +0.161 | ➡️ estable | +1813.37$ | 1.61$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 837 | 73.7% | +0.237 | 📈 madura (+0.05) | +745.93$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4030 | 55.9% | +0.059 | 📈 madura (+0.07) | +557.79$ | 0.59$ | ✅ activa |
| WEEKLY_PRICE | 710 | 77.6% | +0.275 | 📈 madura (+0.17) | +311.00$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 438 | 55.3% | +0.052 | 📉 agota (-0.13) | +98.28$ | 0.52$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 148 | 76.4% | +0.260 | 📉 agota (-0.07) | +76.32$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 316 | 80.7% | +0.305 | ➡️ estable | +62.64$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1585 | 48.7% | -0.013 | 📈 madura (+0.03) | +36.15$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1305 | 63.3% | +0.133 | ➡️ estable | +24.48$ | 1.33$ | ✅ activa |
| GBM_LATE_60M | 406 | 42.4% | -0.076 | 📈 madura (+0.11) | +18.04$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1725 | 51.4% | +0.014 | ➡️ estable | +15.43$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.52$ | ✅ activa |
| STRUCT_NO_15M | 706 | 52.7% | +0.027 | ➡️ estable | +9.08$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 29 | 79.3% | +0.274 | — | +6.30$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_60M | 127 | 53.5% | +0.035 | 📈 madura (+0.05) | +1.74$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 136 | 52.2% | +0.022 | 📈 madura (+0.07) | +1.49$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 32 | 50.0% | +0.000 | 📉 agota (-0.11) | +0.39$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 141 | 93.6% | +0.430 | 📈 madura (+0.04) | -1.52$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 44 | 22.7% | -0.261 | 📉 agota (-0.08) | -10.29$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_5M | 75 | 33.3% | -0.162 | ➡️ estable | -13.50$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 110 | 40.0% | -0.098 | 📈 madura (+0.04) | -13.76$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 644 | 79.7% | +0.296 | ➡️ estable | -13.97$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1854 | 54.9% | +0.049 | 📉 agota (-0.16) | -14.12$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 129 | 86.8% | +0.363 | 📈 madura (+0.11) | -17.07$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 337 | 77.2% | +0.270 | 📉 agota (-0.09) | -21.96$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 125 | 18.4% | -0.311 | 📈 madura (+0.07) | -25.36$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 251 | 44.6% | -0.053 | 📉 agota (-0.08) | -26.50$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 325 | 43.7% | -0.063 | 📉 agota (-0.10) | -27.91$ | 0.50$ | 🚫 desactivada |
| UPDOWN_OU_5M | 344 | 32.3% | -0.176 | ➡️ estable | -59.69$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2782 | 70.1% | +0.201 | 📉 agota (-0.04) | -176.29$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 2896 | 43.7% | -0.063 | 📈 madura (+0.03) | -634.27$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 28495 | 61.9% | +0.119 | 📉 agota (-0.03) | -710.22$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 12985 | 70.0% | +0.200 | ➡️ estable | -944.59$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-10T07:08 | BALLENAS_TARDIAS#XRP#5min | … | ✅ WIN | +0.33$ |
| 2026-08-10T07:08 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-10T07:08 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-10T07:08 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | … | ✅ WIN | +0.35$ |
| 2026-08-10T07:08 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ✅ WIN | +0.39$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-10T07:06 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,233.26 | 0.1min |  |
| ✅ ETH | $1,925.69 | 0.1min |  |
| ✅ SOL | $76.95 | 0.1min |  |
| ✅ XRP | $1.04 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,233.80 | consenso |  |
| ETH | $1,926.01 | consenso |  |
| SOL | $76.90 | consenso |  |
| XRP | $1.04 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*