# Estado del bot — 2026-08-14 17:02 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 61.22 $ |
| Balance on-chain | **16.11 $** |
| P&L real total | 🔴 **-45.11 $** |
| P&L real hoy | +1.22 $ |
| P&L real 7 días | -3.19 $ |
| Fees pagados (real) | 15.64 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +5671.46 $ |
| P&L sim compuesto | 🟢 +16163.44 $ (ficción Kelly: +63536% s/ operativo) |
| P&L sim hoy (2026-08-14) | 🔴 -116.06 $ |
| Operaciones resueltas | 135929 (82891 WIN / 53038 LOSS) — 61.0% |
| Señales abiertas | 462 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 12996 | 61.0% | +0.110 | ➡️ estable | +5962.32$ | 0.56$ | ✅ activa |
| GBM_LATE_15M | 15030 | 60.1% | +0.101 | ➡️ estable | +5123.81$ | 0.96$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 11630 | 60.2% | +0.102 | 📈 madura (+0.08) | +4720.36$ | 1.77$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 4265 | 62.9% | +0.129 | 📉 agota (-0.04) | +1881.78$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 2080 | 69.9% | +0.198 | 📉 agota (-0.10) | +1548.44$ | 1.94$ | ✅ activa |
| UPDOWN_GBM | 4877 | 55.3% | +0.053 | 📈 madura (+0.04) | +608.67$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 824 | 77.9% | +0.278 | 📈 madura (+0.12) | +352.20$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1976 | 50.6% | +0.006 | 📈 madura (+0.07) | +108.79$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 791 | 54.6% | +0.046 | ➡️ estable | +107.04$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 208 | 75.0% | +0.248 | 📉 agota (-0.08) | +96.40$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 451 | 44.6% | -0.054 | 📈 madura (+0.12) | +50.85$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 361 | 78.9% | +0.288 | 📉 agota (-0.03) | +48.98$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 3374 | 62.3% | +0.123 | ➡️ estable | +31.07$ | 1.40$ | ✅ activa |
| ORDER_FLOW_5M | 1758 | 51.6% | +0.016 | ➡️ estable | +22.17$ | 0.60$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 331 | 55.3% | +0.053 | 📉 agota (-0.14) | +11.71$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 44 | 81.8% | +0.304 | 📉 agota (-0.08) | +7.91$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 253 | 54.5% | +0.045 | ➡️ estable | +4.43$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 35 | 48.6% | -0.014 | 📉 agota (-0.08) | -0.09$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_60M | 232 | 52.2% | +0.021 | 📉 agota (-0.06) | -0.84$ | 0.50$ | ✅ activa |
| STREAK_FADE_60M | 13 | 30.8% | -0.108 | — | -2.67$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 1331 | 51.5% | +0.015 | ➡️ estable | -3.64$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 204 | 36.3% | -0.136 | 📉 agota (-0.04) | -4.98$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 397 | 44.1% | -0.059 | 📉 agota (-0.13) | -5.96$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 197 | 91.9% | +0.415 | ➡️ estable | -9.81$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 178 | 89.9% | +0.394 | 📈 madura (+0.11) | -13.04$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 445 | 78.4% | +0.283 | ➡️ estable | -13.37$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| BALLENAS_CONFIRMADAS_15M | 2087 | 54.5% | +0.045 | 📉 agota (-0.18) | -15.93$ | 0.50$ | ✅ activa |
| STREAK_FADE_5M | 503 | 49.1% | -0.009 | 📈 madura (+0.09) | -19.63$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 85 | 22.4% | -0.270 | ➡️ estable | -19.72$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_5M | 148 | 36.5% | -0.133 | 📈 madura (+0.05) | -21.20$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 750 | 79.1% | +0.290 | ➡️ estable | -25.27$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 170 | 20.0% | -0.297 | 📈 madura (+0.11) | -31.44$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 507 | 45.0% | -0.050 | 📉 agota (-0.03) | -33.62$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 256 | 38.7% | -0.112 | 📈 madura (+0.04) | -36.72$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 453 | 32.5% | -0.175 | ➡️ estable | -77.01$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 4070 | 69.2% | +0.192 | ➡️ estable | -282.50$ | 1.84$ | ✅ activa |
| BALLENAS_TARDIAS | 5949 | 45.6% | -0.044 | 📈 madura (+0.03) | -965.94$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 37820 | 61.2% | +0.112 | ➡️ estable | -1420.47$ | 1.39$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 18494 | 69.5% | +0.195 | ➡️ estable | -1518.88$ | 1.62$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-14T17:01 | FAVORITO_CONFIRMADO#XRP#5min | … | ✅ WIN | +0.74$ |
| 2026-08-14T17:01 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | … | ✅ WIN | +0.74$ |
| 2026-08-14T17:01 | FAVORITO_CONFIRMADO#BTC#5min | … | ✅ WIN | +0.80$ |
| 2026-08-14T17:01 | BALLENAS_TARDIAS#DOGE#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-14T17:01 | STREAK_FADE_5M#DOGE#5min | Dogecoin Up or Down - August 14, 12:40PM-12:45PM E… | ✅ WIN | +0.49$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-14T16:57 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,079.29 | 0.2min |  |
| ✅ ETH | $1,883.53 | 0.2min |  |
| ✅ SOL | $75.42 | 0.2min |  |
| ✅ XRP | $1.00 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,079.29 | consenso |  |
| ETH | $1,883.53 | consenso |  |
| SOL | $75.42 | consenso |  |
| XRP | $1.00 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*