# Estado del bot — 2026-08-14 09:00 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 61.22 $ |
| Balance on-chain | **14.89 $** |
| P&L real total | 🔴 **-46.33 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -4.41 $ |
| Fees pagados (real) | 15.58 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +5829.47 $ |
| P&L sim compuesto | 🟢 +16236.23 $ (ficción Kelly: +63822% s/ operativo) |
| P&L sim hoy (2026-08-14) | 🔴 -43.27 $ |
| Operaciones resueltas | 133140 (81326 WIN / 51814 LOSS) — 61.1% |
| Señales abiertas | 385 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 12816 | 61.1% | +0.111 | ➡️ estable | +5970.13$ | 0.60$ | ✅ activa |
| GBM_LATE_15M | 14876 | 60.1% | +0.101 | ➡️ estable | +5085.15$ | 0.97$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 11475 | 60.2% | +0.102 | 📈 madura (+0.08) | +4676.10$ | 1.83$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 4200 | 63.2% | +0.132 | 📉 agota (-0.04) | +1861.77$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1945 | 70.9% | +0.209 | 📉 agota (-0.08) | +1532.76$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4805 | 55.3% | +0.053 | 📈 madura (+0.04) | +602.22$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 800 | 77.9% | +0.278 | 📈 madura (+0.12) | +344.10$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1954 | 50.7% | +0.007 | 📈 madura (+0.07) | +110.10$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 756 | 54.8% | +0.047 | ➡️ estable | +109.04$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 200 | 75.0% | +0.248 | 📉 agota (-0.10) | +90.73$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 357 | 79.3% | +0.291 | 📉 agota (-0.03) | +52.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 449 | 44.5% | -0.054 | 📈 madura (+0.11) | +51.92$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 3222 | 62.2% | +0.122 | ➡️ estable | +22.32$ | 1.35$ | ✅ activa |
| ORDER_FLOW_5M | 1756 | 51.6% | +0.016 | ➡️ estable | +21.93$ | 0.61$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 331 | 55.3% | +0.053 | 📉 agota (-0.14) | +11.71$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 249 | 55.0% | +0.050 | 📈 madura (+0.04) | +7.99$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 44 | 81.8% | +0.304 | 📉 agota (-0.08) | +7.91$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_60M | 225 | 52.9% | +0.029 | 📉 agota (-0.03) | +3.73$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 35 | 48.6% | -0.014 | 📉 agota (-0.08) | -0.09$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_60M | 13 | 30.8% | -0.108 | — | -2.67$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 1289 | 51.5% | +0.015 | ➡️ estable | -3.95$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 201 | 35.3% | -0.145 | 📉 agota (-0.05) | -5.67$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 397 | 44.1% | -0.059 | 📉 agota (-0.13) | -5.96$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 191 | 91.6% | +0.412 | ➡️ estable | -10.53$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 174 | 89.7% | +0.392 | 📈 madura (+0.11) | -13.63$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 437 | 78.3% | +0.281 | 📉 agota (-0.03) | -14.93$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 2077 | 54.5% | +0.044 | 📉 agota (-0.18) | -17.15$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_5M | 137 | 37.2% | -0.126 | 📈 madura (+0.12) | -18.58$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 460 | 49.1% | -0.009 | 📈 madura (+0.03) | -18.64$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 78 | 21.8% | -0.275 | 📉 agota (-0.07) | -19.02$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 744 | 79.0% | +0.290 | ➡️ estable | -24.84$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 169 | 20.1% | -0.295 | 📈 madura (+0.14) | -30.93$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 465 | 44.5% | -0.055 | 📉 agota (-0.07) | -33.45$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_15M | 256 | 38.7% | -0.112 | 📈 madura (+0.04) | -36.72$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 417 | 31.9% | -0.180 | 📉 agota (-0.04) | -72.60$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3968 | 69.5% | +0.194 | ➡️ estable | -258.51$ | 1.89$ | ✅ activa |
| BALLENAS_TARDIAS | 5637 | 46.1% | -0.039 | 📈 madura (+0.06) | -892.85$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 37102 | 61.2% | +0.112 | ➡️ estable | -1371.77$ | 1.44$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 18077 | 69.5% | +0.195 | ➡️ estable | -1472.43$ | 1.56$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-14T08:59 | GBM_LATE_5M#BTC#5min | Bitcoin Up or Down - August 14, 4:45AM-4:50AM ET… | ❌ LOSS | -0.51$ |
| 2026-08-14T08:59 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | … | ✅ WIN | +0.43$ |
| 2026-08-14T08:59 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ✅ WIN | +0.28$ |
| 2026-08-14T08:59 | FAVORITO_CONFIRMADO#BTC#5min | … | ✅ WIN | +0.77$ |
| 2026-08-14T08:59 | FAVORITO_CONFIRMADO#ETH#5min | … | ✅ WIN | +0.84$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-14T08:57 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,842.71 | 0.2min |  |
| ✅ ETH | $1,873.96 | 0.2min |  |
| ✅ SOL | $75.83 | 0.2min |  |
| ✅ XRP | $1.01 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,861.70 | consenso |  |
| ETH | $1,874.01 | consenso |  |
| SOL | $75.75 | consenso |  |
| XRP | $1.00 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*