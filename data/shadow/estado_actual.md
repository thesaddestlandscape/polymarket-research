# Estado del bot — 2026-08-09 14:32 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **10.83 $** |
| P&L real total | 🔴 **-40.39 $** |
| P&L real hoy | -0.39 $ |
| P&L real 7 días | -10.76 $ |
| Fees pagados (real) | 14.97 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6029.65 $ |
| P&L sim compuesto | 🟢 +14229.89 $ (ficción Kelly: +55935% s/ operativo) |
| P&L sim hoy (2026-08-09) | 🟢 +169.97 $ |
| Operaciones resueltas | 98956 (60671 WIN / 38285 LOSS) — 61.3% |
| Señales abiertas | 844 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 10620 | 62.2% | +0.122 | ➡️ estable | +5224.24$ | 1.22$ | ✅ activa |
| GBM_LATE_15M | 13087 | 60.2% | +0.102 | ➡️ estable | +4396.34$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10034 | 59.0% | +0.090 | 📈 madura (+0.03) | +3607.21$ | 0.90$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3521 | 66.3% | +0.163 | ➡️ estable | +1808.04$ | 1.62$ | ✅ activa |
| UPDOWN_GBM | 4010 | 56.0% | +0.060 | 📈 madura (+0.07) | +566.02$ | 0.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 711 | 71.9% | +0.218 | ➡️ estable | +562.63$ | 2.00$ | ✅ activa |
| WEEKLY_PRICE | 682 | 77.1% | +0.270 | 📈 madura (+0.17) | +290.58$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 437 | 55.1% | +0.051 | 📉 agota (-0.13) | +98.04$ | 0.51$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 140 | 76.4% | +0.261 | 📉 agota (-0.04) | +76.28$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 309 | 80.6% | +0.304 | ➡️ estable | +60.56$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1550 | 48.8% | -0.012 | 📈 madura (+0.04) | +45.39$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 991 | 63.7% | +0.136 | ➡️ estable | +24.39$ | 1.37$ | ✅ activa |
| GBM_LATE_60M | 398 | 42.5% | -0.075 | 📈 madura (+0.12) | +16.84$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1723 | 51.4% | +0.014 | ➡️ estable | +15.45$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 326 | 55.5% | +0.055 | 📉 agota (-0.14) | +13.14$ | 0.55$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 28 | 78.6% | +0.267 | — | +4.53$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 32 | 50.0% | +0.000 | 📉 agota (-0.11) | +0.39$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 589 | 52.1% | +0.021 | 📉 agota (-0.03) | +0.02$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 130 | 93.8% | +0.432 | 📈 madura (+0.06) | -0.55$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_60M | 104 | 53.8% | +0.038 | 📈 madura (+0.07) | -0.80$ | 0.50$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_60M_PYCONFIRMADO | 117 | 52.1% | +0.021 | 📈 madura (+0.04) | -1.85$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 193 | 33.7% | -0.162 | 📉 agota (-0.09) | -5.71$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 394 | 43.9% | -0.061 | 📉 agota (-0.14) | -6.24$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 32 | 25.0% | -0.235 | ➡️ estable | -6.52$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 632 | 80.1% | +0.300 | 📉 agota (-0.03) | -7.03$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_15M | 87 | 40.2% | -0.096 | 📈 madura (+0.10) | -10.53$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_5M | 70 | 30.0% | -0.194 | ➡️ estable | -14.81$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 125 | 86.4% | +0.358 | 📈 madura (+0.08) | -17.48$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 323 | 77.1% | +0.269 | 📉 agota (-0.08) | -22.02$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 125 | 18.4% | -0.311 | 📈 madura (+0.07) | -25.36$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 247 | 44.9% | -0.050 | 📉 agota (-0.06) | -25.47$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 325 | 43.7% | -0.063 | 📉 agota (-0.10) | -27.91$ | 0.50$ | 🚫 desactivada |
| BALLENAS_CONFIRMADAS_15M | 1822 | 54.7% | +0.047 | 📉 agota (-0.16) | -28.17$ | 0.50$ | ✅ activa |
| UPDOWN_OU_5M | 340 | 32.6% | -0.173 | ➡️ estable | -57.65$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2592 | 70.0% | +0.200 | 📉 agota (-0.06) | -175.85$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 2567 | 42.9% | -0.071 | 📉 agota (-0.04) | -559.51$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 27036 | 61.9% | +0.119 | 📉 agota (-0.04) | -682.67$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 12146 | 69.9% | +0.199 | ➡️ estable | -901.74$ | 1.99$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-09T14:31 | BALLENAS_TARDIAS#XRP#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-09T14:31 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | … | ✅ WIN | +0.16$ |
| 2026-08-09T14:31 | GBM_LATE_5M#SOL#5min | Solana Up or Down - August 9, 10:15AM-10:20AM ET… | ❌ LOSS | -0.51$ |
| 2026-08-09T14:31 | BALLENAS_TARDIAS#SOL#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-09T14:31 | FAVORITO_CONFIRMADO#DOGE#5min | … | ❌ LOSS | -1.07$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-09T14:29 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,120.18 | 0.1min |  |
| ✅ ETH | $1,921.72 | 0.1min |  |
| ✅ SOL | $76.70 | 0.1min |  |
| ✅ XRP | $1.04 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,120.18 | consenso |  |
| ETH | $1,921.72 | consenso |  |
| SOL | $76.56 | consenso |  |
| XRP | $1.04 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*