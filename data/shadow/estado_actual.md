# Estado del bot — 2026-08-11 14:25 UTC

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
| P&L fiel (stake fijo 1$) | +6154.75 $ |
| P&L sim compuesto | 🟢 +15251.71 $ (ficción Kelly: +59952% s/ operativo) |
| P&L sim hoy (2026-08-11) | 🟢 +83.59 $ |
| Operaciones resueltas | 111627 (68587 WIN / 43040 LOSS) — 61.4% |
| Señales abiertas | 610 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11405 | 61.7% | +0.117 | ➡️ estable | +5588.86$ | 0.58$ | ✅ activa |
| GBM_LATE_15M | 13700 | 60.2% | +0.102 | ➡️ estable | +4683.12$ | 1.09$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10455 | 59.4% | +0.094 | 📈 madura (+0.05) | +3970.20$ | 1.87$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3608 | 65.8% | +0.158 | ➡️ estable | +1814.56$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1072 | 74.2% | +0.241 | 📈 madura (+0.05) | +969.79$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4103 | 55.8% | +0.058 | 📈 madura (+0.06) | +559.51$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 732 | 77.9% | +0.278 | 📈 madura (+0.16) | +326.70$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 459 | 54.7% | +0.047 | 📉 agota (-0.14) | +99.20$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 162 | 76.5% | +0.262 | 📉 agota (-0.05) | +82.81$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 329 | 80.5% | +0.304 | ➡️ estable | +63.37$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1680 | 49.7% | -0.003 | 📈 madura (+0.07) | +61.01$ | 0.90$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1926 | 63.3% | +0.133 | ➡️ estable | +41.93$ | 1.33$ | ✅ activa |
| GBM_LATE_60M | 422 | 42.7% | -0.073 | 📈 madura (+0.10) | +31.37$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1729 | 51.5% | +0.015 | ➡️ estable | +18.29$ | 0.60$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 889 | 52.4% | +0.024 | ➡️ estable | +7.10$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 32 | 81.2% | +0.294 | 📉 agota (-0.11) | +6.65$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1919 | 55.1% | +0.051 | 📉 agota (-0.15) | +3.50$ | 0.74$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 195 | 53.3% | +0.033 | ➡️ estable | +1.04$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_60M | 160 | 52.5% | +0.025 | ➡️ estable | -0.49$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 149 | 94.0% | +0.434 | 📈 madura (+0.04) | -0.58$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 8 | 25.0% | -0.080 | — | -2.11$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 52 | 21.2% | -0.278 | 📉 agota (-0.11) | -13.27$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 666 | 79.6% | +0.295 | ➡️ estable | -14.47$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 142 | 88.0% | +0.375 | 📈 madura (+0.12) | -15.21$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 369 | 78.0% | +0.279 | 📉 agota (-0.07) | -16.21$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 98 | 31.6% | -0.180 | ➡️ estable | -19.34$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 276 | 46.7% | -0.032 | 📈 madura (+0.05) | -22.38$ | 1.13$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 160 | 38.8% | -0.111 | ➡️ estable | -23.19$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 140 | 18.6% | -0.310 | 📈 madura (+0.08) | -28.09$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 350 | 42.9% | -0.071 | 📉 agota (-0.12) | -32.61$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 353 | 31.7% | -0.182 | 📉 agota (-0.04) | -62.59$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3155 | 70.2% | +0.202 | ➡️ estable | -189.32$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 3641 | 45.6% | -0.044 | 📈 madura (+0.09) | -693.96$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 31242 | 61.8% | +0.118 | ➡️ estable | -850.87$ | 1.15$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 14542 | 69.9% | +0.199 | ➡️ estable | -1089.53$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-11T14:24 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-11T14:24 | FAVORITO_CONFIRMADO#XRP#5min | … | ✅ WIN | +0.80$ |
| 2026-08-11T14:24 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | … | ✅ WIN | +0.80$ |
| 2026-08-11T14:24 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | … | ✅ WIN | +0.37$ |
| 2026-08-11T14:24 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | … | ✅ WIN | +0.37$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-11T14:20 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,072.79 | 0.2min |  |
| ✅ ETH | $1,885.42 | 0.2min |  |
| ✅ SOL | $75.90 | 0.2min |  |
| ✅ XRP | $1.01 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,099.90 | consenso |  |
| ETH | $1,886.03 | consenso |  |
| SOL | $75.90 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*