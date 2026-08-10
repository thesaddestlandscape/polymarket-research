# Estado del bot — 2026-08-10 21:16 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **41.27 $** |
| P&L real total | 🔴 **-9.95 $** |
| P&L real hoy | +31.21 $ |
| P&L real 7 días | +21.76 $ |
| Fees pagados (real) | 15.20 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6172.59 $ |
| P&L sim compuesto | 🟢 +15037.46 $ (ficción Kelly: +59110% s/ operativo) |
| P&L sim hoy (2026-08-10) | 🟢 +661.99 $ |
| Operaciones resueltas | 107037 (65752 WIN / 41285 LOSS) — 61.4% |
| Señales abiertas | 697 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11161 | 61.9% | +0.119 | ➡️ estable | +5515.64$ | 1.19$ | ✅ activa |
| GBM_LATE_15M | 13511 | 60.2% | +0.102 | ➡️ estable | +4587.39$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10311 | 59.3% | +0.093 | 📈 madura (+0.05) | +3864.54$ | 0.93$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3584 | 66.0% | +0.160 | ➡️ estable | +1816.36$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 946 | 74.7% | +0.247 | 📈 madura (+0.08) | +869.27$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4057 | 55.9% | +0.059 | 📈 madura (+0.07) | +566.04$ | 0.59$ | ✅ activa |
| WEEKLY_PRICE | 732 | 77.9% | +0.278 | 📈 madura (+0.16) | +326.70$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 445 | 54.6% | +0.046 | 📉 agota (-0.13) | +96.50$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 156 | 76.9% | +0.266 | 📉 agota (-0.05) | +85.26$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 323 | 80.8% | +0.306 | ➡️ estable | +65.82$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1612 | 48.8% | -0.012 | 📈 madura (+0.04) | +33.62$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1593 | 62.9% | +0.129 | ➡️ estable | +22.01$ | 1.29$ | ✅ activa |
| GBM_LATE_60M | 408 | 42.4% | -0.076 | 📈 madura (+0.10) | +16.82$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1725 | 51.4% | +0.014 | ➡️ estable | +15.43$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.52$ | ✅ activa |
| STRUCT_NO_15M | 775 | 52.8% | +0.028 | ➡️ estable | +7.19$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 32 | 81.2% | +0.294 | 📉 agota (-0.11) | +6.65$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| BALLENAS_CONFIRMADAS_15M | 1888 | 55.1% | +0.051 | 📉 agota (-0.15) | -0.44$ | 0.51$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 144 | 93.8% | +0.432 | 📈 madura (+0.04) | -1.25$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 163 | 52.8% | +0.027 | ➡️ estable | -1.91$ | 0.50$ | ✅ activa |
| STREAK_FADE_60M | 6 | 16.7% | -0.075 | — | -2.08$ | 0.50$ | ⏳ acumulando |
| LIQUIDACIONES_60M | 147 | 50.3% | +0.003 | 📉 agota (-0.03) | -4.36$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 52 | 21.2% | -0.278 | 📉 agota (-0.11) | -13.27$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 654 | 79.7% | +0.296 | ➡️ estable | -14.54$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 135 | 87.4% | +0.369 | 📈 madura (+0.10) | -16.19$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 86 | 31.4% | -0.182 | ➡️ estable | -17.18$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 353 | 77.3% | +0.272 | 📉 agota (-0.10) | -21.33$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_15M | 136 | 36.8% | -0.130 | 📉 agota (-0.06) | -21.85$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 251 | 44.6% | -0.053 | 📉 agota (-0.08) | -26.50$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 131 | 18.3% | -0.312 | 📈 madura (+0.09) | -27.01$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 325 | 43.7% | -0.063 | 📉 agota (-0.10) | -27.91$ | 0.50$ | 🚫 desactivada |
| UPDOWN_OU_5M | 345 | 32.2% | -0.177 | 📉 agota (-0.03) | -60.20$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2944 | 70.0% | +0.200 | ➡️ estable | -189.15$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 3168 | 44.9% | -0.051 | 📈 madura (+0.06) | -620.24$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 29743 | 61.8% | +0.118 | ➡️ estable | -782.96$ | 1.18$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 13688 | 69.9% | +0.199 | ➡️ estable | -1006.29$ | 1.99$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-10T21:14 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | … | ✅ WIN | +0.43$ |
| 2026-08-10T21:14 | FAVORITO_CONFIRMADO#SOL#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-10T21:14 | BALLENAS_TARDIAS#ETH#5min | … | ✅ WIN | +0.18$ |
| 2026-08-10T21:14 | BALLENAS_TARDIAS#SOL#5min | … | ✅ WIN | +0.35$ |
| 2026-08-10T21:14 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | … | ✅ WIN | +0.18$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-10T21:12 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,059.00 | 0.2min |  |
| ✅ ETH | $1,875.21 | 0.2min |  |
| ✅ SOL | $76.33 | 0.2min |  |
| ✅ XRP | $1.02 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,062.00 | consenso |  |
| ETH | $1,875.31 | consenso |  |
| SOL | $76.33 | consenso |  |
| XRP | $1.02 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*