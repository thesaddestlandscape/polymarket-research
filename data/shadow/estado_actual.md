# Estado del bot — 2026-08-13 11:28 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **5.97 $** |
| P&L real total | 🔴 **-45.25 $** |
| P&L real hoy | -2.18 $ |
| P&L real 7 días | -5.93 $ |
| Fees pagados (real) | 15.55 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +5991.61 $ |
| P&L sim compuesto | 🟢 +16008.07 $ (ficción Kelly: +62925% s/ operativo) |
| P&L sim hoy (2026-08-13) | 🟢 +268.28 $ |
| Operaciones resueltas | 125877 (77088 WIN / 48789 LOSS) — 61.2% |
| Señales abiertas | 451 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 12324 | 61.3% | +0.113 | ➡️ estable | +5859.47$ | 0.59$ | ✅ activa |
| GBM_LATE_15M | 14463 | 60.2% | +0.102 | ➡️ estable | +4974.74$ | 1.03$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 11084 | 60.0% | +0.100 | 📈 madura (+0.07) | +4476.56$ | 1.91$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3969 | 64.0% | +0.140 | 📉 agota (-0.03) | +1819.64$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1620 | 72.3% | +0.223 | ➡️ estable | +1377.26$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4562 | 55.5% | +0.055 | 📈 madura (+0.05) | +581.66$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 780 | 77.9% | +0.279 | 📈 madura (+0.14) | +342.55$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 667 | 54.1% | +0.041 | ➡️ estable | +95.05$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 189 | 76.2% | +0.259 | 📉 agota (-0.07) | +93.60$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1885 | 50.5% | +0.005 | 📈 madura (+0.07) | +90.41$ | 0.78$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 350 | 79.7% | +0.295 | ➡️ estable | +56.33$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 440 | 43.6% | -0.063 | 📈 madura (+0.12) | +45.10$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2801 | 62.3% | +0.123 | ➡️ estable | +20.41$ | 1.23$ | ✅ activa |
| ORDER_FLOW_5M | 1744 | 51.5% | +0.015 | ➡️ estable | +18.39$ | 0.58$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 330 | 55.5% | +0.054 | 📉 agota (-0.14) | +12.22$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 38 | 78.9% | +0.275 | 📉 agota (-0.10) | +6.65$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 237 | 54.4% | +0.044 | 📈 madura (+0.04) | +4.46$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 208 | 52.9% | +0.029 | ➡️ estable | +0.29$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 35 | 48.6% | -0.014 | 📉 agota (-0.08) | -0.09$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_60M | 10 | 30.0% | -0.083 | — | -2.19$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 170 | 93.5% | +0.430 | ➡️ estable | -2.25$ | 2.00$ | ✅ activa |
| STRUCT_NO_15M | 1161 | 51.3% | +0.013 | ➡️ estable | -5.77$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 198 | 34.3% | -0.155 | 📉 agota (-0.08) | -6.26$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 396 | 43.9% | -0.060 | 📉 agota (-0.13) | -6.46$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 164 | 89.6% | +0.392 | 📈 madura (+0.11) | -12.77$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| BALLENAS_CONFIRMADAS_15M | 2022 | 54.5% | +0.044 | 📉 agota (-0.18) | -14.00$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM_FADE | 70 | 21.4% | -0.278 | 📉 agota (-0.08) | -17.69$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 414 | 78.0% | +0.279 | 📉 agota (-0.04) | -18.15$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 129 | 36.4% | -0.134 | 📈 madura (+0.13) | -18.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 406 | 47.8% | -0.022 | ➡️ estable | -22.34$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 716 | 78.8% | +0.287 | 📉 agota (-0.03) | -26.93$ | 2.00$ | ✅ activa |
| STREAK_MOM_5M | 423 | 44.9% | -0.051 | 📉 agota (-0.05) | -27.17$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 159 | 20.1% | -0.295 | 📈 madura (+0.12) | -28.88$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_15M | 233 | 38.6% | -0.113 | ➡️ estable | -33.24$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 386 | 31.6% | -0.183 | 📉 agota (-0.05) | -68.35$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3693 | 70.0% | +0.200 | ➡️ estable | -219.38$ | 1.98$ | ✅ activa |
| BALLENAS_TARDIAS | 4920 | 46.8% | -0.032 | 📈 madura (+0.07) | -774.30$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 35190 | 61.3% | +0.113 | ➡️ estable | -1222.37$ | 1.06$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 16935 | 69.7% | +0.197 | ➡️ estable | -1338.41$ | 1.98$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-13T11:27 | BALLENAS_TARDIAS#SOL#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-13T11:27 | GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | Bitcoin Up or Down - August 13, 7:00AM-7:15AM ET… | ✅ WIN | +0.97$ |
| 2026-08-13T11:27 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - August 13, 7:00AM-7:15AM ET… | ✅ WIN | +0.97$ |
| 2026-08-13T11:27 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - August 13, 7:00AM-7:15AM ET… | ✅ WIN | +0.30$ |
| 2026-08-13T11:27 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - August 13, 7:00AM-7:15AM ET… | ❌ LOSS | -1.53$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-13T11:24 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,500.00 | 0.1min |  |
| ✅ ETH | $1,877.08 | 0.1min |  |
| ✅ SOL | $75.61 | 0.1min |  |
| ✅ XRP | $1.01 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,504.70 | consenso |  |
| ETH | $1,877.67 | consenso |  |
| SOL | $75.54 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*