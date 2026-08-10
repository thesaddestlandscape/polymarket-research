# Estado del bot — 2026-08-10 17:16 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **9.36 $** |
| P&L real total | 🔴 **-41.86 $** |
| P&L real hoy | -0.69 $ |
| P&L real 7 días | -10.14 $ |
| Fees pagados (real) | 15.15 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6226.01 $ |
| P&L sim compuesto | 🟢 +15037.71 $ (ficción Kelly: +59110% s/ operativo) |
| P&L sim hoy (2026-08-10) | 🟢 +662.24 $ |
| Operaciones resueltas | 106016 (65117 WIN / 40899 LOSS) — 61.4% |
| Señales abiertas | 539 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11111 | 62.1% | +0.121 | ➡️ estable | +5526.58$ | 1.21$ | ✅ activa |
| GBM_LATE_15M | 13470 | 60.3% | +0.103 | ➡️ estable | +4586.22$ | 1.03$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10285 | 59.3% | +0.093 | 📈 madura (+0.04) | +3846.99$ | 0.93$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3575 | 66.0% | +0.160 | ➡️ estable | +1815.26$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 927 | 74.8% | +0.247 | 📈 madura (+0.08) | +857.44$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4051 | 55.9% | +0.059 | 📈 madura (+0.07) | +562.25$ | 0.59$ | ✅ activa |
| WEEKLY_PRICE | 732 | 77.9% | +0.278 | 📈 madura (+0.16) | +326.70$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 445 | 54.6% | +0.046 | 📉 agota (-0.13) | +96.50$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 152 | 76.3% | +0.260 | 📉 agota (-0.05) | +78.15$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 321 | 80.7% | +0.305 | ➡️ estable | +63.42$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1602 | 48.9% | -0.011 | 📈 madura (+0.04) | +37.62$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1517 | 62.9% | +0.129 | ➡️ estable | +19.28$ | 1.29$ | ✅ activa |
| STRUCT_NO_15M | 761 | 53.5% | +0.035 | ➡️ estable | +18.26$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 406 | 42.4% | -0.076 | 📈 madura (+0.11) | +18.04$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1725 | 51.4% | +0.014 | ➡️ estable | +15.43$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.52$ | ✅ activa |
| RESOLUTION_SNIPER | 32 | 81.2% | +0.294 | 📉 agota (-0.11) | +6.65$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 143 | 93.7% | +0.431 | 📈 madura (+0.04) | -1.36$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_60M_PYCONFIRMADO | 154 | 51.9% | +0.019 | ➡️ estable | -2.85$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 141 | 51.1% | +0.010 | ➡️ estable | -2.90$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1879 | 55.1% | +0.051 | 📉 agota (-0.16) | -4.51$ | 0.51$ | ✅ activa |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 52 | 21.2% | -0.278 | 📉 agota (-0.11) | -13.27$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 652 | 79.6% | +0.295 | ➡️ estable | -14.96$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 133 | 87.2% | +0.367 | 📈 madura (+0.10) | -16.48$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 86 | 31.4% | -0.182 | ➡️ estable | -17.18$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 127 | 36.2% | -0.136 | 📉 agota (-0.04) | -20.95$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 349 | 77.1% | +0.269 | 📉 agota (-0.10) | -23.60$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 130 | 18.5% | -0.311 | 📈 madura (+0.09) | -26.50$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 251 | 44.6% | -0.053 | 📉 agota (-0.08) | -26.50$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 325 | 43.7% | -0.063 | 📉 agota (-0.10) | -27.91$ | 0.50$ | 🚫 desactivada |
| UPDOWN_OU_5M | 344 | 32.3% | -0.176 | ➡️ estable | -59.69$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2892 | 69.9% | +0.199 | 📉 agota (-0.04) | -189.11$ | 1.99$ | ✅ activa |
| BALLENAS_TARDIAS | 3074 | 44.3% | -0.057 | 📈 madura (+0.06) | -614.93$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 29391 | 61.8% | +0.118 | 📉 agota (-0.03) | -767.63$ | 1.18$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 13469 | 69.9% | +0.199 | ➡️ estable | -1002.08$ | 1.99$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-10T17:14 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-10T17:14 | BALLENAS_TARDIAS#SOL#5min | … | ✅ WIN | +0.16$ |
| 2026-08-10T17:14 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | … | ✅ WIN | +0.43$ |
| 2026-08-10T17:14 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ✅ WIN | +0.41$ |
| 2026-08-10T17:14 | GBM_LATE_5M#ETH#5min | Ethereum Up or Down - August 10, 12:55PM-1:00PM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-10T17:12 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,884.11 | 0.1min |  |
| ✅ ETH | $1,871.08 | 0.1min |  |
| ✅ SOL | $76.03 | 0.1min |  |
| ✅ XRP | $1.02 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,884.11 | consenso |  |
| ETH | $1,871.13 | consenso |  |
| SOL | $75.78 | consenso |  |
| XRP | $1.02 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*