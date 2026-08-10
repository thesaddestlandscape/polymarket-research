# Estado del bot — 2026-08-10 20:53 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **36.18 $** |
| P&L real total | 🔴 **-15.04 $** |
| P&L real hoy | +26.12 $ |
| P&L real 7 días | +16.67 $ |
| Fees pagados (real) | 15.18 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6182.44 $ |
| P&L sim compuesto | 🟢 +15045.63 $ (ficción Kelly: +59142% s/ operativo) |
| P&L sim hoy (2026-08-10) | 🟢 +670.16 $ |
| Operaciones resueltas | 106946 (65695 WIN / 41251 LOSS) — 61.4% |
| Señales abiertas | 701 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11156 | 62.0% | +0.120 | ➡️ estable | +5518.58$ | 1.20$ | ✅ activa |
| GBM_LATE_15M | 13508 | 60.2% | +0.102 | ➡️ estable | +4588.85$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10309 | 59.3% | +0.093 | 📈 madura (+0.05) | +3863.97$ | 0.93$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3583 | 66.0% | +0.160 | ➡️ estable | +1817.43$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 945 | 74.8% | +0.248 | 📈 madura (+0.08) | +871.31$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4057 | 55.9% | +0.059 | 📈 madura (+0.07) | +566.04$ | 0.59$ | ✅ activa |
| WEEKLY_PRICE | 732 | 77.9% | +0.278 | 📈 madura (+0.16) | +326.70$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 445 | 54.6% | +0.046 | 📉 agota (-0.13) | +96.50$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 156 | 76.9% | +0.266 | 📉 agota (-0.05) | +85.26$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 323 | 80.8% | +0.306 | ➡️ estable | +65.82$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1612 | 48.8% | -0.012 | 📈 madura (+0.04) | +33.62$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1588 | 62.8% | +0.128 | 📉 agota (-0.03) | +20.43$ | 1.28$ | ✅ activa |
| GBM_LATE_60M | 408 | 42.4% | -0.076 | 📈 madura (+0.10) | +16.82$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1725 | 51.4% | +0.014 | ➡️ estable | +15.43$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.52$ | ✅ activa |
| STRUCT_NO_15M | 772 | 53.0% | +0.030 | ➡️ estable | +9.69$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 32 | 81.2% | +0.294 | 📉 agota (-0.11) | +6.65$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1887 | 55.2% | +0.052 | 📉 agota (-0.15) | +1.09$ | 0.52$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 143 | 93.7% | +0.431 | 📈 madura (+0.04) | -1.36$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 6 | 16.7% | -0.075 | — | -2.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_60M_PYCONFIRMADO | 162 | 52.5% | +0.024 | ➡️ estable | -2.15$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 147 | 50.3% | +0.003 | 📉 agota (-0.03) | -4.36$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 52 | 21.2% | -0.278 | 📉 agota (-0.11) | -13.27$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 653 | 79.6% | +0.295 | ➡️ estable | -14.65$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 134 | 87.3% | +0.368 | 📈 madura (+0.10) | -16.34$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 86 | 31.4% | -0.182 | ➡️ estable | -17.18$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 136 | 36.8% | -0.130 | 📉 agota (-0.06) | -21.85$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 352 | 77.3% | +0.271 | 📉 agota (-0.10) | -22.01$ | 2.00$ | ✅ activa |
| STREAK_FADE_5M | 251 | 44.6% | -0.053 | 📉 agota (-0.08) | -26.50$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 131 | 18.3% | -0.312 | 📈 madura (+0.09) | -27.01$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 325 | 43.7% | -0.063 | 📉 agota (-0.10) | -27.91$ | 0.50$ | 🚫 desactivada |
| UPDOWN_OU_5M | 345 | 32.2% | -0.177 | 📉 agota (-0.03) | -60.20$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2939 | 70.0% | +0.199 | ➡️ estable | -189.74$ | 1.99$ | ✅ activa |
| BALLENAS_TARDIAS | 3157 | 44.8% | -0.052 | 📈 madura (+0.06) | -621.42$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 29711 | 61.8% | +0.118 | ➡️ estable | -779.69$ | 1.18$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 13671 | 69.9% | +0.199 | ➡️ estable | -1007.73$ | 1.99$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-10T20:52 | BALLENAS_TARDIAS#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-10T20:52 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-10T20:52 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-10T20:52 | FAVORITO_CONFIRMADO#XRP#5min | … | ✅ WIN | +0.65$ |
| 2026-08-10T20:52 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | … | ✅ WIN | +0.60$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-10T20:49 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,077.06 | 0.2min |  |
| ✅ ETH | $1,877.30 | 0.2min |  |
| ✅ SOL | $76.31 | 0.2min |  |
| ✅ XRP | $1.02 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,090.10 | consenso |  |
| ETH | $1,877.30 | consenso |  |
| SOL | $76.31 | consenso |  |
| XRP | $1.02 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*