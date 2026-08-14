# Estado del bot — 2026-08-14 20:33 UTC

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
| P&L fiel (stake fijo 1$) | +5638.56 $ |
| P&L sim compuesto | 🟢 +16179.93 $ (ficción Kelly: +63600% s/ operativo) |
| P&L sim hoy (2026-08-14) | 🔴 -99.57 $ |
| Operaciones resueltas | 137107 (83580 WIN / 53527 LOSS) — 61.0% |
| Señales abiertas | 430 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 13071 | 61.0% | +0.110 | ➡️ estable | +5985.52$ | 0.57$ | ✅ activa |
| GBM_LATE_15M | 15099 | 60.1% | +0.100 | ➡️ estable | +5133.99$ | 0.96$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 11697 | 60.2% | +0.102 | 📈 madura (+0.08) | +4758.45$ | 1.77$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 4289 | 62.8% | +0.128 | 📉 agota (-0.04) | +1878.65$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 2132 | 69.7% | +0.197 | 📉 agota (-0.09) | +1573.07$ | 1.92$ | ✅ activa |
| UPDOWN_GBM | 4907 | 55.4% | +0.054 | 📈 madura (+0.04) | +613.04$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 824 | 77.9% | +0.278 | 📈 madura (+0.12) | +352.20$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1982 | 50.7% | +0.007 | 📈 madura (+0.07) | +110.79$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 805 | 54.7% | +0.046 | ➡️ estable | +105.32$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 211 | 75.4% | +0.251 | 📉 agota (-0.07) | +100.40$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 454 | 44.9% | -0.050 | 📈 madura (+0.13) | +52.55$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 363 | 79.1% | +0.289 | 📉 agota (-0.03) | +49.32$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 3444 | 62.3% | +0.122 | ➡️ estable | +29.90$ | 1.35$ | ✅ activa |
| ORDER_FLOW_5M | 1761 | 51.6% | +0.016 | ➡️ estable | +22.67$ | 0.62$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 331 | 55.3% | +0.053 | 📉 agota (-0.14) | +11.71$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 44 | 81.8% | +0.304 | 📉 agota (-0.08) | +7.91$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 256 | 54.7% | +0.047 | 📈 madura (+0.05) | +7.55$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 237 | 52.7% | +0.027 | 📉 agota (-0.05) | +1.42$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 35 | 48.6% | -0.014 | 📉 agota (-0.08) | -0.09$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_60M | 13 | 30.8% | -0.108 | — | -2.67$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 1345 | 51.6% | +0.016 | ➡️ estable | -2.92$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 204 | 36.3% | -0.136 | 📉 agota (-0.04) | -4.98$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 397 | 44.1% | -0.059 | 📉 agota (-0.13) | -5.96$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 201 | 92.0% | +0.416 | ➡️ estable | -9.23$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 180 | 90.0% | +0.396 | 📈 madura (+0.11) | -12.80$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 449 | 78.4% | +0.283 | ➡️ estable | -13.39$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| BALLENAS_CONFIRMADAS_15M | 2090 | 54.4% | +0.044 | 📉 agota (-0.18) | -17.46$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM_FADE | 85 | 22.4% | -0.270 | ➡️ estable | -19.72$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 519 | 48.9% | -0.011 | 📈 madura (+0.07) | -20.90$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 155 | 36.8% | -0.131 | 📈 madura (+0.08) | -21.81$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 753 | 79.2% | +0.291 | ➡️ estable | -24.43$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 170 | 20.0% | -0.297 | 📈 madura (+0.11) | -31.44$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 523 | 45.3% | -0.047 | 📉 agota (-0.04) | -32.77$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 256 | 38.7% | -0.112 | 📈 madura (+0.04) | -36.72$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 472 | 32.6% | -0.173 | ➡️ estable | -79.94$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 4107 | 69.1% | +0.191 | ➡️ estable | -289.24$ | 1.83$ | ✅ activa |
| BALLENAS_TARDIAS | 6085 | 45.3% | -0.047 | ➡️ estable | -1014.54$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 38135 | 61.2% | +0.112 | ➡️ estable | -1442.92$ | 1.36$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 18670 | 69.5% | +0.195 | ➡️ estable | -1529.86$ | 1.68$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-14T20:32 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | … | ✅ WIN | +0.35$ |
| 2026-08-14T20:32 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | … | ✅ WIN | +0.37$ |
| 2026-08-14T20:32 | UPDOWN_GBM#XRP#5min | XRP Up or Down - August 14, 4:15PM-4:20PM ET… | ❌ LOSS | -0.56$ |
| 2026-08-14T20:32 | UPDOWN_OU_5M#BNB#5min | BNB Up or Down - August 14, 4:15PM-4:20PM ET… | ✅ WIN | +0.51$ |
| 2026-08-14T20:32 | GBM_LATE_5M#BTC#5min | Bitcoin Up or Down - August 14, 4:15PM-4:20PM ET… | ✅ WIN | +0.50$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-14T20:29 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,877.50 | 0.2min |  |
| ✅ ETH | $1,878.07 | 0.2min |  |
| ✅ SOL | $75.12 | 0.2min |  |
| ✅ XRP | $1.00 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,881.60 | consenso |  |
| ETH | $1,878.13 | consenso |  |
| SOL | $75.12 | consenso |  |
| XRP | $1.00 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*