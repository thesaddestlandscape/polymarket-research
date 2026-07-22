# Estado del bot — 2026-07-22 12:18 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **26.34 $** |
| P&L real total | 🔴 **-24.88 $** |
| P&L real hoy | +3.83 $ |
| P&L real 7 días | -5.76 $ |
| Fees pagados (real) | 9.24 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3398.92 $ |
| P&L sim compuesto | 🟢 +6446.48 $ (ficción Kelly: +25340% s/ operativo) |
| P&L sim hoy (2026-07-22) | 🟢 +82.97 $ |
| Operaciones resueltas | 28840 (17296 WIN / 11544 LOSS) — 60.0% |
| Señales abiertas | 130 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6820 | 59.6% | +0.096 | 📉 agota (-0.03) | +2138.16$ | 0.96$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4019 | 62.9% | +0.128 | 📉 agota (-0.05) | +2085.92$ | 1.29$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4005 | 58.3% | +0.082 | ➡️ estable | +1236.87$ | 0.83$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1164 | 66.2% | +0.161 | 📉 agota (-0.05) | +520.26$ | 1.61$ | ✅ activa |
| UPDOWN_GBM | 2174 | 52.8% | +0.028 | 📈 madura (+0.11) | +180.65$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 226 | 61.1% | +0.110 | 📉 agota (-0.05) | +107.72$ | 1.10$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5014 | 68.6% | +0.186 | ➡️ estable | +78.91$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 731 | 62.4% | +0.123 | ➡️ estable | +30.41$ | 1.23$ | ✅ activa |
| STREAK_FADE_15M | 262 | 58.0% | +0.080 | 📉 agota (-0.08) | +28.71$ | 0.80$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 119 | 79.0% | +0.285 | ➡️ estable | +20.13$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 257 | 82.1% | +0.319 | ➡️ estable | +15.31$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1653 | 51.1% | +0.011 | ➡️ estable | +11.85$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 257 | 51.0% | +0.010 | 📉 agota (-0.15) | +9.66$ | 0.50$ | ✅ activa |
| GBM_LATE_5M | 280 | 48.6% | -0.014 | 📉 agota (-0.14) | +7.67$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 332 | 38.9% | -0.111 | ➡️ estable | +5.44$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 11 | 45.5% | -0.021 | — | -0.76$ | 0.50$ | ⚠️ IC negativo |
| BALLENAS_TARDIAS | 13 | 76.9% | +0.152 | — | -1.30$ | 1.52$ | ✅ activa |
| LATE_WINDOW_5MIN | 316 | 45.3% | -0.047 | 📉 agota (-0.18) | -1.65$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 316 | 44.3% | -0.057 | 📉 agota (-0.09) | -24.82$ | 0.50$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-22T12:10 | FAVORITO_CONFIRMADO#BTC#60min | Bitcoin Up or Down - July 22, 7AM ET… | ✅ WIN | +0.83$ |
| 2026-07-22T12:07 | BALLENAS_CONFIRMADAS_15M#SOL#15min | Solana Up or Down - July 22, 7:45AM-8:00AM ET… | ✅ WIN | +0.61$ |
| 2026-07-22T12:07 | FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | Solana Up or Down - July 22, 7:45AM-8:00AM ET… | ✅ WIN | +0.61$ |
| 2026-07-22T12:07 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 22, 7:45AM-8:00AM ET… | ✅ WIN | +0.61$ |
| 2026-07-22T12:07 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 22, 7:45AM-8:00AM ET… | ✅ WIN | +1.34$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-22T12:16 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,875.20 | 0.1min |  |
| ✅ ETH | $1,925.30 | 0.1min |  |
| ✅ SOL | $77.41 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,875.20 | consenso |  |
| ETH | $1,925.30 | consenso |  |
| SOL | $77.39 | consenso |  |
| XRP | $1.14 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*