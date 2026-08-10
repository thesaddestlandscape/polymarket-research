# Estado del bot — 2026-08-10 13:58 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **8.54 $** |
| P&L real total | 🔴 **-42.68 $** |
| P&L real hoy | -1.52 $ |
| P&L real 7 días | -10.97 $ |
| Fees pagados (real) | 15.12 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6179.13 $ |
| P&L sim compuesto | 🟢 +14827.64 $ (ficción Kelly: +58285% s/ operativo) |
| P&L sim hoy (2026-08-10) | 🟢 +452.16 $ |
| Operaciones resueltas | 105134 (64596 WIN / 40538 LOSS) — 61.4% |
| Señales abiertas | 503 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11069 | 62.1% | +0.121 | ➡️ estable | +5359.68$ | 1.21$ | ✅ activa |
| GBM_LATE_15M | 13434 | 60.2% | +0.102 | ➡️ estable | +4558.46$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10253 | 59.3% | +0.093 | 📈 madura (+0.04) | +3820.56$ | 0.93$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3567 | 66.0% | +0.160 | ➡️ estable | +1811.07$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 894 | 74.4% | +0.243 | 📈 madura (+0.07) | +811.73$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4041 | 55.9% | +0.059 | 📈 madura (+0.07) | +555.37$ | 0.59$ | ✅ activa |
| WEEKLY_PRICE | 710 | 77.6% | +0.275 | 📈 madura (+0.17) | +311.00$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 442 | 54.8% | +0.047 | 📉 agota (-0.13) | +96.24$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 152 | 76.3% | +0.260 | 📉 agota (-0.05) | +78.15$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 321 | 80.7% | +0.305 | ➡️ estable | +63.42$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1594 | 48.9% | -0.011 | 📈 madura (+0.04) | +39.19$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1448 | 63.1% | +0.130 | ➡️ estable | +20.90$ | 1.30$ | ✅ activa |
| GBM_LATE_60M | 406 | 42.4% | -0.076 | 📈 madura (+0.11) | +18.04$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1725 | 51.4% | +0.014 | ➡️ estable | +15.43$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 753 | 53.0% | +0.030 | ➡️ estable | +11.80$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.52$ | ✅ activa |
| RESOLUTION_SNIPER | 29 | 79.3% | +0.274 | — | +6.30$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_60M | 134 | 53.7% | +0.037 | 📈 madura (+0.06) | +1.76$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 147 | 51.7% | +0.017 | ➡️ estable | -0.91$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 143 | 93.7% | +0.431 | 📈 madura (+0.04) | -1.36$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 44 | 22.7% | -0.261 | 📉 agota (-0.08) | -10.29$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 651 | 79.7% | +0.296 | ➡️ estable | -12.92$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_5M | 80 | 31.2% | -0.183 | ➡️ estable | -16.05$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 117 | 38.5% | -0.113 | ➡️ estable | -16.34$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 132 | 87.1% | +0.366 | 📈 madura (+0.10) | -16.65$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1869 | 54.9% | +0.049 | 📉 agota (-0.17) | -17.36$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 346 | 77.5% | +0.273 | 📉 agota (-0.09) | -19.69$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 130 | 18.5% | -0.311 | 📈 madura (+0.09) | -26.50$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 251 | 44.6% | -0.053 | 📉 agota (-0.08) | -26.50$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 325 | 43.7% | -0.063 | 📉 agota (-0.10) | -27.91$ | 0.50$ | 🚫 desactivada |
| UPDOWN_OU_5M | 344 | 32.3% | -0.176 | ➡️ estable | -59.69$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2855 | 70.1% | +0.200 | 📉 agota (-0.04) | -181.70$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 3015 | 44.1% | -0.059 | 📈 madura (+0.05) | -617.19$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 29096 | 61.9% | +0.119 | ➡️ estable | -719.70$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 13305 | 70.0% | +0.200 | ➡️ estable | -976.04$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-10T13:56 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | … | ✅ WIN | +0.33$ |
| 2026-08-10T13:56 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-10T13:56 | FAVORITO_CONFIRMADO#BTC#5min | … | ✅ WIN | +0.71$ |
| 2026-08-10T13:56 | FAVORITO_CONFIRMADO#SOL#5min | … | ✅ WIN | +0.84$ |
| 2026-08-10T13:56 | FAVORITO_CONFIRMADO#XRP#5min | … | ✅ WIN | +0.68$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-10T13:53 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,547.94 | 0.1min |  |
| ✅ ETH | $1,897.49 | 0.1min |  |
| ✅ SOL | $76.17 | 0.1min |  |
| ✅ XRP | $1.02 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,547.94 | consenso |  |
| ETH | $1,898.18 | consenso |  |
| SOL | $76.22 | consenso |  |
| XRP | $1.02 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*