# Estado del bot — 2026-07-18 10:05 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **0.78 $** |
| P&L real total | 🔴 **-24.66 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -24.52 $ |
| Fees pagados (real) | 8.68 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +2652.61 $ |
| P&L sim compuesto | 🟢 +4746.53 $ (ficción Kelly: +18658% s/ operativo) |
| P&L sim hoy (2026-07-18) | 🟢 +241.77 $ |
| Operaciones resueltas | 20402 (12242 WIN / 8160 LOSS) — 60.0% |
| Señales abiertas | 95 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 5490 | 60.3% | +0.103 | ➡️ estable | +1771.91$ | 1.03$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 2702 | 65.0% | +0.150 | ➡️ estable | +1586.77$ | 1.50$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 2652 | 60.0% | +0.100 | 📈 madura (+0.04) | +905.51$ | 1.00$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 434 | 67.7% | +0.177 | ➡️ estable | +175.17$ | 1.77$ | ✅ activa |
| UPDOWN_GBM | 1753 | 51.7% | +0.017 | 📈 madura (+0.12) | +118.08$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 160 | 66.9% | +0.167 | 📈 madura (+0.11) | +93.77$ | 1.67$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| STREAK_FADE_15M | 218 | 60.6% | +0.105 | 📈 madura (+0.05) | +39.44$ | 1.04$ | ✅ activa |
| LATE_WINDOW_5MIN | 49 | 73.5% | +0.225 | ➡️ estable | +24.54$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 143 | 66.4% | +0.162 | 📈 madura (+0.03) | +21.72$ | 1.62$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 172 | 55.2% | +0.052 | 📉 agota (-0.15) | +17.23$ | 0.52$ | ✅ activa |
| ORDER_FLOW_5M | 1630 | 51.3% | +0.013 | ➡️ estable | +14.21$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 45 | 82.2% | +0.309 | 📈 madura (+0.09) | +12.27$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 108 | 81.5% | +0.309 | 📈 madura (+0.04) | +4.24$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 326 | 38.3% | -0.116 | ➡️ estable | +3.81$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM_ETH_15M_HORA7 | 3 | 66.7% | +0.015 | — | +0.37$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_5M | 11 | 45.5% | -0.021 | — | -0.62$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 3348 | 68.2% | +0.181 | ➡️ estable | -0.75$ | 1.81$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 149 | 32.9% | -0.169 | 📉 agota (-0.12) | -4.27$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-18T10:05 | FAVORITO_CONFIRMADO#BTC#60min | Bitcoin Up or Down - July 18, 5AM ET… | ✅ WIN | +0.90$ |
| 2026-07-18T10:02 | FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | Solana Up or Down - July 18, 5:45AM-6:00AM ET… | ✅ WIN | +0.97$ |
| 2026-07-18T10:02 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 18, 5:45AM-6:00AM ET… | ✅ WIN | +0.97$ |
| 2026-07-18T10:02 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 18, 5:45AM-6:00AM ET… | ✅ WIN | +1.84$ |
| 2026-07-18T10:02 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 18, 5:45AM-6:00AM ET… | ✅ WIN | +1.00$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-18T10:04 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,943.71 | 0.1min |  |
| ✅ ETH | $1,843.87 | 0.1min |  |
| ✅ SOL | $74.84 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,945.00 | consenso |  |
| ETH | $1,843.97 | consenso |  |
| SOL | $74.78 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*