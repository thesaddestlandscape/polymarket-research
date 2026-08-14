# Estado del bot — 2026-08-14 13:19 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 61.22 $ |
| Balance on-chain | **15.57 $** |
| P&L real total | 🔴 **-45.65 $** |
| P&L real hoy | +0.67 $ |
| P&L real 7 días | -3.74 $ |
| Fees pagados (real) | 15.61 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +5651.18 $ |
| P&L sim compuesto | 🟢 +16080.07 $ (ficción Kelly: +63208% s/ operativo) |
| P&L sim hoy (2026-08-14) | 🔴 -199.43 $ |
| Operaciones resueltas | 134577 (82073 WIN / 52504 LOSS) — 61.0% |
| Señales abiertas | 412 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 12914 | 61.0% | +0.110 | ➡️ estable | +5956.66$ | 0.57$ | ✅ activa |
| GBM_LATE_15M | 14956 | 60.0% | +0.100 | ➡️ estable | +5082.53$ | 0.94$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 11560 | 60.1% | +0.101 | 📈 madura (+0.08) | +4682.11$ | 1.77$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 4229 | 62.9% | +0.129 | 📉 agota (-0.04) | +1870.85$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 2011 | 70.2% | +0.202 | 📉 agota (-0.09) | +1526.25$ | 1.97$ | ✅ activa |
| UPDOWN_GBM | 4836 | 55.3% | +0.053 | 📈 madura (+0.04) | +608.69$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 800 | 77.9% | +0.278 | 📈 madura (+0.12) | +344.10$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1970 | 50.7% | +0.007 | 📈 madura (+0.07) | +110.84$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 774 | 54.5% | +0.045 | ➡️ estable | +108.85$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 203 | 74.9% | +0.246 | 📉 agota (-0.08) | +89.45$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 450 | 44.7% | -0.053 | 📈 madura (+0.12) | +52.38$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 360 | 79.2% | +0.290 | ➡️ estable | +51.02$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 3306 | 62.4% | +0.124 | ➡️ estable | +37.21$ | 1.61$ | ✅ activa |
| ORDER_FLOW_5M | 1756 | 51.6% | +0.016 | ➡️ estable | +21.93$ | 0.61$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 331 | 55.3% | +0.053 | 📉 agota (-0.14) | +11.71$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 44 | 81.8% | +0.304 | 📉 agota (-0.08) | +7.91$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 251 | 54.6% | +0.045 | 📈 madura (+0.03) | +4.72$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 230 | 52.6% | +0.026 | 📉 agota (-0.04) | +0.73$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 35 | 48.6% | -0.014 | 📉 agota (-0.08) | -0.09$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 1312 | 51.7% | +0.017 | ➡️ estable | -1.87$ | 0.50$ | ✅ activa |
| STREAK_FADE_60M | 13 | 30.8% | -0.108 | — | -2.67$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 201 | 35.3% | -0.145 | 📉 agota (-0.05) | -5.67$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 397 | 44.1% | -0.059 | 📉 agota (-0.13) | -5.96$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 195 | 91.8% | +0.414 | ➡️ estable | -10.06$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 442 | 78.5% | +0.284 | ➡️ estable | -11.86$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 176 | 89.8% | +0.393 | 📈 madura (+0.11) | -13.33$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| BALLENAS_CONFIRMADAS_15M | 2082 | 54.5% | +0.045 | 📉 agota (-0.18) | -16.66$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM_FADE | 78 | 21.8% | -0.275 | 📉 agota (-0.07) | -19.02$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 481 | 49.1% | -0.009 | 📈 madura (+0.06) | -19.36$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 139 | 36.7% | -0.131 | 📈 madura (+0.12) | -19.60$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 748 | 79.1% | +0.291 | ➡️ estable | -23.37$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 170 | 20.0% | -0.297 | 📈 madura (+0.11) | -31.44$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 485 | 44.7% | -0.052 | 📉 agota (-0.06) | -33.55$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 256 | 38.7% | -0.112 | 📈 madura (+0.04) | -36.72$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 435 | 32.2% | -0.177 | 📉 agota (-0.04) | -74.81$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 4023 | 69.1% | +0.191 | ➡️ estable | -281.28$ | 1.83$ | ✅ activa |
| BALLENAS_TARDIAS | 5796 | 45.5% | -0.044 | 📈 madura (+0.04) | -943.38$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 37491 | 61.2% | +0.112 | ➡️ estable | -1431.44$ | 1.38$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 18285 | 69.5% | +0.195 | ➡️ estable | -1504.96$ | 1.50$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-14T13:18 | BALLENAS_TARDIAS#SOL#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-14T13:18 | BALLENAS_TARDIAS#XRP#5min | … | ✅ WIN | +0.43$ |
| 2026-08-14T13:18 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-14T13:18 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-14T13:18 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | … | ✅ WIN | +0.43$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-14T13:16 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,603.51 | 0.2min |  |
| ✅ ETH | $1,867.79 | 0.2min |  |
| ✅ SOL | $75.36 | 0.2min |  |
| ✅ XRP | $1.00 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,620.40 | consenso |  |
| ETH | $1,868.16 | consenso |  |
| SOL | $75.36 | consenso |  |
| XRP | $1.00 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*