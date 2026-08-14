# Estado del bot — 2026-08-14 15:09 UTC

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
| P&L fiel (stake fijo 1$) | +5603.89 $ |
| P&L sim compuesto | 🟢 +16031.65 $ (ficción Kelly: +63018% s/ operativo) |
| P&L sim hoy (2026-08-14) | 🔴 -247.85 $ |
| Operaciones resueltas | 135213 (82425 WIN / 52788 LOSS) — 61.0% |
| Señales abiertas | 459 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 12953 | 61.0% | +0.110 | ➡️ estable | +5950.56$ | 0.56$ | ✅ activa |
| GBM_LATE_15M | 14989 | 60.0% | +0.100 | ➡️ estable | +5089.62$ | 0.94$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 11593 | 60.1% | +0.101 | 📈 madura (+0.08) | +4687.54$ | 1.76$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 4243 | 62.9% | +0.129 | 📉 agota (-0.04) | +1871.77$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 2040 | 70.0% | +0.200 | 📉 agota (-0.10) | +1529.46$ | 1.95$ | ✅ activa |
| UPDOWN_GBM | 4858 | 55.3% | +0.053 | 📈 madura (+0.04) | +599.75$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 800 | 77.9% | +0.278 | 📈 madura (+0.12) | +344.10$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1974 | 50.7% | +0.007 | 📈 madura (+0.07) | +109.81$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 786 | 54.6% | +0.046 | ➡️ estable | +106.38$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 206 | 74.8% | +0.245 | 📉 agota (-0.08) | +91.02$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 450 | 44.7% | -0.053 | 📈 madura (+0.12) | +52.38$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 361 | 78.9% | +0.288 | 📉 agota (-0.03) | +48.98$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 3342 | 62.2% | +0.122 | ➡️ estable | +29.68$ | 1.38$ | ✅ activa |
| ORDER_FLOW_5M | 1758 | 51.6% | +0.016 | ➡️ estable | +22.17$ | 0.60$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 331 | 55.3% | +0.053 | 📉 agota (-0.14) | +11.71$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 44 | 81.8% | +0.304 | 📉 agota (-0.08) | +7.91$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 251 | 54.6% | +0.045 | 📈 madura (+0.03) | +4.72$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 231 | 52.4% | +0.024 | 📉 agota (-0.05) | +0.22$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 35 | 48.6% | -0.014 | 📉 agota (-0.08) | -0.09$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 1313 | 51.7% | +0.017 | ➡️ estable | -1.39$ | 0.50$ | ✅ activa |
| STREAK_FADE_60M | 13 | 30.8% | -0.108 | — | -2.67$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 201 | 35.3% | -0.145 | 📉 agota (-0.05) | -5.67$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 397 | 44.1% | -0.059 | 📉 agota (-0.13) | -5.96$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 197 | 91.9% | +0.415 | ➡️ estable | -9.81$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 442 | 78.5% | +0.284 | ➡️ estable | -11.86$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 176 | 89.8% | +0.393 | 📈 madura (+0.11) | -13.33$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| BALLENAS_CONFIRMADAS_15M | 2086 | 54.5% | +0.045 | 📉 agota (-0.18) | -15.33$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM_FADE | 78 | 21.8% | -0.275 | 📉 agota (-0.07) | -19.02$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 492 | 49.0% | -0.010 | 📈 madura (+0.08) | -19.99$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 140 | 36.4% | -0.134 | 📈 madura (+0.12) | -20.11$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 750 | 79.1% | +0.290 | ➡️ estable | -25.27$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 170 | 20.0% | -0.297 | 📈 madura (+0.11) | -31.44$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 496 | 45.0% | -0.050 | 📉 agota (-0.04) | -33.13$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 256 | 38.7% | -0.112 | 📈 madura (+0.04) | -36.72$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 447 | 32.2% | -0.177 | ➡️ estable | -76.95$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 4042 | 69.2% | +0.192 | ➡️ estable | -279.93$ | 1.84$ | ✅ activa |
| BALLENAS_TARDIAS | 5878 | 45.5% | -0.045 | 📈 madura (+0.03) | -961.74$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 37649 | 61.2% | +0.112 | ➡️ estable | -1432.25$ | 1.38$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 18389 | 69.4% | +0.194 | ➡️ estable | -1522.69$ | 1.47$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-14T15:08 | BALLENAS_TARDIAS#SOL#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-14T15:08 | GBM_LATE_5M#BTC#5min | Bitcoin Up or Down - August 14, 10:50AM-10:55AM ET… | ✅ WIN | +0.50$ |
| 2026-08-14T15:08 | UPDOWN_GBM#BTC#5min | Bitcoin Up or Down - August 14, 10:50AM-10:55AM ET… | ✅ WIN | +0.50$ |
| 2026-08-14T15:08 | UPDOWN_OU_5M#ETH#5min | Ethereum Up or Down - August 14, 10:50AM-10:55AM E… | ❌ LOSS | -0.51$ |
| 2026-08-14T15:08 | UPDOWN_GBM#ETH#5min | Ethereum Up or Down - August 14, 10:50AM-10:55AM E… | ✅ WIN | +0.50$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-14T15:05 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,572.96 | 0.2min |  |
| ✅ ETH | $1,864.89 | 0.2min |  |
| ✅ SOL | $75.17 | 0.2min |  |
| ✅ XRP | $1.00 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,572.96 | consenso |  |
| ETH | $1,864.89 | consenso |  |
| SOL | $75.17 | consenso |  |
| XRP | $1.00 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*