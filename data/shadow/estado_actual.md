# Estado del bot — 2026-08-07 15:50 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **10.64 $** |
| P&L real total | 🔴 **-40.58 $** |
| P&L real hoy | +1.35 $ |
| P&L real 7 días | -6.56 $ |
| Fees pagados (real) | 14.67 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +5936.19 $ |
| P&L sim compuesto | 🟢 +13655.52 $ (ficción Kelly: +53677% s/ operativo) |
| P&L sim hoy (2026-08-07) | 🟢 +182.97 $ |
| Operaciones resueltas | 87071 (53202 WIN / 33869 LOSS) — 61.1% |
| Señales abiertas | 395 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 9816 | 62.8% | +0.128 | ➡️ estable | +4971.45$ | 1.28$ | ✅ activa |
| GBM_LATE_15M | 12494 | 60.2% | +0.102 | ➡️ estable | +4168.82$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 9651 | 58.5% | +0.085 | ➡️ estable | +3280.07$ | 0.85$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3482 | 66.4% | +0.164 | ➡️ estable | +1802.85$ | 1.64$ | ✅ activa |
| UPDOWN_GBM | 3980 | 56.0% | +0.060 | 📈 madura (+0.07) | +566.46$ | 0.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 405 | 70.6% | +0.205 | 📉 agota (-0.05) | +291.62$ | 2.00$ | ✅ activa |
| WEEKLY_PRICE | 634 | 76.0% | +0.259 | 📈 madura (+0.18) | +240.56$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 433 | 55.0% | +0.049 | 📉 agota (-0.13) | +98.68$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 126 | 77.0% | +0.266 | 📉 agota (-0.05) | +72.54$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 299 | 80.9% | +0.307 | ➡️ estable | +60.86$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1500 | 48.5% | -0.015 | 📈 madura (+0.04) | +46.57$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 385 | 42.3% | -0.076 | 📈 madura (+0.11) | +19.93$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 114 | 69.3% | +0.190 | 📈 madura (+0.05) | +18.40$ | 1.90$ | ✅ activa |
| ORDER_FLOW_5M | 1722 | 51.4% | +0.014 | ➡️ estable | +15.96$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 318 | 55.7% | +0.056 | 📉 agota (-0.13) | +14.27$ | 0.56$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 27 | 77.8% | +0.259 | — | +4.05$ | 2.00$ | ✅ activa |
| STRUCT_NO_15M | 261 | 53.3% | +0.032 | ➡️ estable | +3.49$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 596 | 80.5% | +0.304 | 📉 agota (-0.03) | +2.51$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 32 | 50.0% | +0.000 | 📉 agota (-0.11) | +0.39$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 73 | 50.7% | +0.007 | 📈 madura (+0.12) | -0.02$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 60 | 50.0% | +0.000 | 📈 madura (+0.06) | -1.27$ | 0.50$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 97 | 92.8% | +0.419 | ➡️ estable | -2.40$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM_FADE | 15 | 26.7% | -0.154 | — | -2.81$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 193 | 33.7% | -0.162 | 📉 agota (-0.09) | -5.71$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 394 | 43.9% | -0.061 | 📉 agota (-0.14) | -6.24$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 62 | 38.7% | -0.109 | 📈 madura (+0.12) | -8.36$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 55 | 30.9% | -0.184 | 📉 agota (-0.04) | -11.10$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 102 | 86.3% | +0.356 | 📈 madura (+0.04) | -13.68$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 280 | 77.5% | +0.273 | 📉 agota (-0.08) | -16.56$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 85 | 14.1% | -0.351 | ➡️ estable | -23.32$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 247 | 44.9% | -0.050 | 📉 agota (-0.06) | -25.47$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 320 | 44.1% | -0.059 | 📉 agota (-0.08) | -26.41$ | 0.50$ | 🚫 desactivada |
| BALLENAS_CONFIRMADAS_15M | 1730 | 54.7% | +0.047 | 📉 agota (-0.16) | -40.64$ | 0.50$ | ✅ activa |
| UPDOWN_OU_5M | 299 | 33.8% | -0.161 | 📈 madura (+0.06) | -48.45$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 1978 | 69.8% | +0.197 | 📉 agota (-0.06) | -155.08$ | 1.98$ | ✅ activa |
| BALLENAS_TARDIAS | 1760 | 42.0% | -0.079 | 📉 agota (-0.19) | -286.67$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 22949 | 61.8% | +0.118 | 📉 agota (-0.06) | -588.36$ | 1.18$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 9736 | 69.3% | +0.193 | ➡️ estable | -759.05$ | 1.93$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-07T15:48 | UPDOWN_OU_5M#SOL#5min | Solana Up or Down - August 7, 11:35AM-11:40AM ET… | ✅ WIN | +1.45$ |
| 2026-08-07T15:48 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-07T15:48 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-07T15:48 | FAVORITO_CONFIRMADO#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-07T15:48 | FAVORITO_CONFIRMADO#SOL#5min | … | ❌ LOSS | -1.07$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-07T15:46 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,976.11 | 0.1min |  |
| ✅ ETH | $1,918.19 | 0.1min |  |
| ✅ SOL | $73.89 | 0.1min |  |
| ✅ XRP | $1.03 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,976.11 | consenso |  |
| ETH | $1,918.19 | consenso |  |
| SOL | $73.88 | consenso |  |
| XRP | $1.03 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*