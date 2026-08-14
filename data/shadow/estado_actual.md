# Estado del bot — 2026-08-14 12:24 UTC

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
| P&L fiel (stake fijo 1$) | +5726.74 $ |
| P&L sim compuesto | 🟢 +16167.89 $ (ficción Kelly: +63553% s/ operativo) |
| P&L sim hoy (2026-08-14) | 🔴 -111.61 $ |
| Operaciones resueltas | 134243 (81918 WIN / 52325 LOSS) — 61.0% |
| Señales abiertas | 440 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 12890 | 61.1% | +0.111 | ➡️ estable | +5970.80$ | 0.59$ | ✅ activa |
| GBM_LATE_15M | 14938 | 60.0% | +0.100 | ➡️ estable | +5085.76$ | 0.95$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 11539 | 60.2% | +0.102 | 📈 madura (+0.08) | +4685.91$ | 1.80$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 4220 | 63.0% | +0.130 | 📉 agota (-0.04) | +1871.12$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1997 | 70.4% | +0.204 | 📉 agota (-0.09) | +1531.23$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4826 | 55.4% | +0.054 | 📈 madura (+0.04) | +612.30$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 800 | 77.9% | +0.278 | 📈 madura (+0.12) | +344.10$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1969 | 50.7% | +0.007 | 📈 madura (+0.07) | +110.34$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 767 | 54.5% | +0.045 | ➡️ estable | +109.42$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 203 | 74.9% | +0.246 | 📉 agota (-0.08) | +89.45$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 450 | 44.7% | -0.053 | 📈 madura (+0.12) | +52.38$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 360 | 79.2% | +0.290 | ➡️ estable | +51.02$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 3289 | 62.3% | +0.123 | ➡️ estable | +33.02$ | 1.54$ | ✅ activa |
| ORDER_FLOW_5M | 1756 | 51.6% | +0.016 | ➡️ estable | +21.93$ | 0.61$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 331 | 55.3% | +0.053 | 📉 agota (-0.14) | +11.71$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 44 | 81.8% | +0.304 | 📉 agota (-0.08) | +7.91$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 251 | 54.6% | +0.045 | 📈 madura (+0.03) | +4.72$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 227 | 53.3% | +0.033 | 📉 agota (-0.03) | +4.64$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 35 | 48.6% | -0.014 | 📉 agota (-0.08) | -0.09$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_60M | 13 | 30.8% | -0.108 | — | -2.67$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 1305 | 51.6% | +0.016 | ➡️ estable | -3.20$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 201 | 35.3% | -0.145 | 📉 agota (-0.05) | -5.67$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 397 | 44.1% | -0.059 | 📉 agota (-0.13) | -5.96$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 192 | 91.7% | +0.412 | ➡️ estable | -10.39$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 442 | 78.5% | +0.284 | ➡️ estable | -11.86$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 176 | 89.8% | +0.393 | 📈 madura (+0.11) | -13.33$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| BALLENAS_CONFIRMADAS_15M | 2080 | 54.5% | +0.045 | 📉 agota (-0.18) | -16.12$ | 0.50$ | ✅ activa |
| STREAK_FADE_5M | 470 | 49.1% | -0.008 | 📈 madura (+0.04) | -18.76$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 78 | 21.8% | -0.275 | 📉 agota (-0.07) | -19.02$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_5M | 139 | 36.7% | -0.131 | 📈 madura (+0.12) | -19.60$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 747 | 79.1% | +0.290 | ➡️ estable | -23.47$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 170 | 20.0% | -0.297 | 📈 madura (+0.11) | -31.44$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 475 | 44.6% | -0.053 | 📉 agota (-0.06) | -33.51$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 256 | 38.7% | -0.112 | 📈 madura (+0.04) | -36.72$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 435 | 32.2% | -0.177 | 📉 agota (-0.04) | -74.81$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 4011 | 69.3% | +0.192 | ➡️ estable | -272.73$ | 1.85$ | ✅ activa |
| BALLENAS_TARDIAS | 5759 | 45.6% | -0.044 | 📈 madura (+0.04) | -924.20$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 37408 | 61.2% | +0.112 | ➡️ estable | -1412.55$ | 1.40$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 18241 | 69.5% | +0.195 | ➡️ estable | -1493.00$ | 1.58$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-14T12:24 | BALLENAS_TARDIAS#XRP#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-14T12:24 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-14T12:24 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | … | ✅ WIN | +0.43$ |
| 2026-08-14T12:24 | FAVORITO_CONFIRMADO#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-14T12:24 | FAVORITO_CONFIRMADO#DOGE#5min | … | ✅ WIN | +0.74$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-14T12:21 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,753.00 | 0.1min |  |
| ✅ ETH | $1,873.51 | 0.1min |  |
| ✅ SOL | $75.33 | 0.1min |  |
| ✅ XRP | $1.00 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,776.89 | consenso |  |
| ETH | $1,874.29 | consenso |  |
| SOL | $75.37 | consenso |  |
| XRP | $1.00 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*