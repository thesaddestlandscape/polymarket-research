# Estado del bot — 2026-08-14 16:19 UTC

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
| P&L fiel (stake fijo 1$) | +5664.10 $ |
| P&L sim compuesto | 🟢 +16149.40 $ (ficción Kelly: +63480% s/ operativo) |
| P&L sim hoy (2026-08-14) | 🔴 -130.10 $ |
| Operaciones resueltas | 135668 (82731 WIN / 52937 LOSS) — 61.0% |
| Señales abiertas | 456 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 12979 | 61.0% | +0.110 | ➡️ estable | +5970.44$ | 0.57$ | ✅ activa |
| GBM_LATE_15M | 15012 | 60.1% | +0.101 | ➡️ estable | +5115.37$ | 0.96$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 11616 | 60.2% | +0.102 | 📈 madura (+0.08) | +4718.10$ | 1.77$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 4255 | 62.9% | +0.129 | 📉 agota (-0.04) | +1874.86$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 2065 | 70.0% | +0.200 | 📉 agota (-0.10) | +1550.38$ | 1.95$ | ✅ activa |
| UPDOWN_GBM | 4868 | 55.3% | +0.053 | 📈 madura (+0.04) | +607.62$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 822 | 77.9% | +0.278 | 📈 madura (+0.12) | +349.07$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1975 | 50.6% | +0.006 | 📈 madura (+0.07) | +109.30$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 790 | 54.7% | +0.047 | ➡️ estable | +107.60$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 208 | 75.0% | +0.248 | 📉 agota (-0.08) | +96.40$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 451 | 44.6% | -0.054 | 📈 madura (+0.12) | +50.85$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 361 | 78.9% | +0.288 | 📉 agota (-0.03) | +48.98$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 3361 | 62.2% | +0.122 | ➡️ estable | +30.68$ | 1.38$ | ✅ activa |
| ORDER_FLOW_5M | 1758 | 51.6% | +0.016 | ➡️ estable | +22.17$ | 0.60$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 331 | 55.3% | +0.053 | 📉 agota (-0.14) | +11.71$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 44 | 81.8% | +0.304 | 📉 agota (-0.08) | +7.91$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 253 | 54.5% | +0.045 | ➡️ estable | +4.43$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 35 | 48.6% | -0.014 | 📉 agota (-0.08) | -0.09$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_60M | 232 | 52.2% | +0.021 | 📉 agota (-0.06) | -0.84$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 1323 | 51.6% | +0.016 | ➡️ estable | -2.53$ | 0.50$ | ✅ activa |
| STREAK_FADE_60M | 13 | 30.8% | -0.108 | — | -2.67$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 204 | 36.3% | -0.136 | 📉 agota (-0.04) | -4.98$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 397 | 44.1% | -0.059 | 📉 agota (-0.13) | -5.96$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 197 | 91.9% | +0.415 | ➡️ estable | -9.81$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 178 | 89.9% | +0.394 | 📈 madura (+0.11) | -13.04$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 445 | 78.4% | +0.283 | ➡️ estable | -13.37$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| BALLENAS_CONFIRMADAS_15M | 2086 | 54.5% | +0.045 | 📉 agota (-0.18) | -15.33$ | 0.50$ | ✅ activa |
| STREAK_FADE_5M | 498 | 49.2% | -0.008 | 📈 madura (+0.08) | -19.09$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 84 | 22.6% | -0.267 | ➡️ estable | -19.21$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_5M | 147 | 36.1% | -0.138 | 📈 madura (+0.06) | -21.68$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 750 | 79.1% | +0.290 | ➡️ estable | -25.27$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 170 | 20.0% | -0.297 | 📈 madura (+0.11) | -31.44$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 502 | 44.8% | -0.052 | ➡️ estable | -34.13$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 256 | 38.7% | -0.112 | 📈 madura (+0.04) | -36.72$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 450 | 32.2% | -0.177 | 📉 agota (-0.03) | -77.48$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 4060 | 69.2% | +0.192 | ➡️ estable | -280.47$ | 1.84$ | ✅ activa |
| BALLENAS_TARDIAS | 5924 | 45.5% | -0.045 | 📈 madura (+0.03) | -967.65$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 37754 | 61.2% | +0.112 | ➡️ estable | -1421.64$ | 1.38$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 18458 | 69.5% | +0.195 | ➡️ estable | -1522.32$ | 1.56$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-14T16:18 | BALLENAS_TARDIAS#SOL#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-14T16:18 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ✅ WIN | +0.37$ |
| 2026-08-14T16:18 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | … | ✅ WIN | +0.41$ |
| 2026-08-14T16:18 | BALLENAS_TARDIAS#DOGE#5min | … | ✅ WIN | +0.87$ |
| 2026-08-14T16:18 | LIQUIDACIONES_5M#DOGE#5min | Dogecoin Up or Down - August 14, 12:00PM-12:05PM E… | ✅ WIN | +0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-14T16:15 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,965.86 | 0.2min |  |
| ✅ ETH | $1,878.66 | 0.2min |  |
| ✅ SOL | $75.57 | 0.2min |  |
| ✅ XRP | $1.00 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,965.86 | consenso |  |
| ETH | $1,878.66 | consenso |  |
| SOL | $75.57 | consenso |  |
| XRP | $1.00 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*