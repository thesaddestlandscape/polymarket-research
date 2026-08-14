# Estado del bot — 2026-08-14 15:23 UTC

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
| P&L fiel (stake fijo 1$) | +5585.50 $ |
| P&L sim compuesto | 🟢 +16007.42 $ (ficción Kelly: +62922% s/ operativo) |
| P&L sim hoy (2026-08-14) | 🔴 -272.08 $ |
| Operaciones resueltas | 135274 (82448 WIN / 52826 LOSS) — 60.9% |
| Señales abiertas | 466 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 12958 | 60.9% | +0.109 | ➡️ estable | +5944.23$ | 0.55$ | ✅ activa |
| GBM_LATE_15M | 14993 | 60.0% | +0.100 | ➡️ estable | +5087.56$ | 0.94$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 11597 | 60.1% | +0.101 | 📈 madura (+0.08) | +4691.35$ | 1.76$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 4245 | 62.9% | +0.129 | 📉 agota (-0.04) | +1872.09$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 2046 | 69.9% | +0.199 | 📉 agota (-0.10) | +1525.90$ | 1.94$ | ✅ activa |
| UPDOWN_GBM | 4860 | 55.3% | +0.053 | 📈 madura (+0.04) | +599.89$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 800 | 77.9% | +0.278 | 📈 madura (+0.12) | +344.10$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1974 | 50.7% | +0.007 | 📈 madura (+0.07) | +109.81$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 787 | 54.5% | +0.045 | ➡️ estable | +105.87$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 206 | 74.8% | +0.245 | 📉 agota (-0.08) | +91.02$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 451 | 44.6% | -0.054 | 📈 madura (+0.12) | +50.85$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 361 | 78.9% | +0.288 | 📉 agota (-0.03) | +48.98$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 3347 | 62.3% | +0.123 | ➡️ estable | +32.81$ | 1.44$ | ✅ activa |
| ORDER_FLOW_5M | 1758 | 51.6% | +0.016 | ➡️ estable | +22.17$ | 0.60$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 331 | 55.3% | +0.053 | 📉 agota (-0.14) | +11.71$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 44 | 81.8% | +0.304 | 📉 agota (-0.08) | +7.91$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 252 | 54.4% | +0.043 | ➡️ estable | +4.21$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 35 | 48.6% | -0.014 | 📉 agota (-0.08) | -0.09$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 1315 | 51.8% | +0.018 | ➡️ estable | -0.43$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 232 | 52.2% | +0.021 | 📉 agota (-0.06) | -0.84$ | 0.50$ | ✅ activa |
| STREAK_FADE_60M | 13 | 30.8% | -0.108 | — | -2.67$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 201 | 35.3% | -0.145 | 📉 agota (-0.05) | -5.67$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 397 | 44.1% | -0.059 | 📉 agota (-0.13) | -5.96$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 197 | 91.9% | +0.415 | ➡️ estable | -9.81$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 176 | 89.8% | +0.393 | 📈 madura (+0.11) | -13.33$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 443 | 78.3% | +0.282 | ➡️ estable | -13.90$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 2086 | 54.5% | +0.045 | 📉 agota (-0.18) | -15.33$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM_FADE | 78 | 21.8% | -0.275 | 📉 agota (-0.07) | -19.02$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 492 | 49.0% | -0.010 | 📈 madura (+0.08) | -19.99$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 140 | 36.4% | -0.134 | 📈 madura (+0.12) | -20.11$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 750 | 79.1% | +0.290 | ➡️ estable | -25.27$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 170 | 20.0% | -0.297 | 📈 madura (+0.11) | -31.44$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 496 | 45.0% | -0.050 | 📉 agota (-0.04) | -33.13$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 256 | 38.7% | -0.112 | 📈 madura (+0.04) | -36.72$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 447 | 32.2% | -0.177 | ➡️ estable | -76.95$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 4044 | 69.1% | +0.191 | ➡️ estable | -282.07$ | 1.83$ | ✅ activa |
| BALLENAS_TARDIAS | 5885 | 45.4% | -0.046 | 📈 madura (+0.03) | -969.24$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 37663 | 61.2% | +0.112 | ➡️ estable | -1434.41$ | 1.37$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 18392 | 69.4% | +0.194 | ➡️ estable | -1525.90$ | 1.44$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-14T15:22 | BALLENAS_TARDIAS#XRP#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-14T15:22 | BALLENAS_TARDIAS#SOL#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-14T15:22 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-14T15:22 | FAVORITO_CONFIRMADO#SOL#5min | … | ✅ WIN | +0.80$ |
| 2026-08-14T15:22 | FAVORITO_CONFIRMADO#XRP#5min | … | ✅ WIN | +0.60$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-14T15:17 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,629.64 | 0.2min |  |
| ✅ ETH | $1,866.20 | 0.2min |  |
| ✅ SOL | $75.29 | 0.2min |  |
| ✅ XRP | $1.00 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,629.64 | consenso |  |
| ETH | $1,866.77 | consenso |  |
| SOL | $75.20 | consenso |  |
| XRP | $1.00 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*