# Estado del bot — 2026-07-18 09:30 UTC

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
| P&L fiel (stake fijo 1$) | +2643.18 $ |
| P&L sim compuesto | 🟢 +4725.11 $ (ficción Kelly: +18574% s/ operativo) |
| P&L sim hoy (2026-07-18) | 🟢 +220.35 $ |
| Operaciones resueltas | 20368 (12216 WIN / 8152 LOSS) — 60.0% |
| Señales abiertas | 92 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 5483 | 60.3% | +0.103 | ➡️ estable | +1766.88$ | 1.03$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 2694 | 65.0% | +0.149 | ➡️ estable | +1580.64$ | 1.49$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 2647 | 60.0% | +0.100 | 📈 madura (+0.04) | +899.84$ | 1.00$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 434 | 67.7% | +0.177 | ➡️ estable | +175.17$ | 1.77$ | ✅ activa |
| UPDOWN_GBM | 1753 | 51.7% | +0.017 | 📈 madura (+0.12) | +118.08$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 160 | 66.9% | +0.167 | 📈 madura (+0.11) | +93.77$ | 1.67$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| STREAK_FADE_15M | 217 | 60.8% | +0.107 | 📈 madura (+0.07) | +40.97$ | 1.07$ | ✅ activa |
| LATE_WINDOW_5MIN | 49 | 73.5% | +0.225 | ➡️ estable | +24.54$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 141 | 66.7% | +0.164 | 📈 madura (+0.05) | +22.40$ | 1.64$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 172 | 55.2% | +0.052 | 📉 agota (-0.15) | +17.23$ | 0.52$ | ✅ activa |
| ORDER_FLOW_5M | 1630 | 51.3% | +0.013 | ➡️ estable | +14.21$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 45 | 82.2% | +0.309 | 📈 madura (+0.09) | +12.27$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 326 | 38.3% | -0.116 | ➡️ estable | +3.81$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 106 | 81.1% | +0.306 | ➡️ estable | +2.95$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 3 | 66.7% | +0.015 | — | +0.37$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_5M | 11 | 45.5% | -0.021 | — | -0.62$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 149 | 32.9% | -0.169 | 📉 agota (-0.12) | -4.27$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 3339 | 68.1% | +0.181 | ➡️ estable | -6.24$ | 1.81$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-18T09:30 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 18, 5:15AM-5:30AM ET… | ✅ WIN | +0.12$ |
| 2026-07-18T09:30 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 18, 5:15AM-5:30AM ET… | ✅ WIN | +1.10$ |
| 2026-07-18T09:30 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 18, 5:15AM-5:30AM ET… | ✅ WIN | +1.77$ |
| 2026-07-18T09:30 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 18, 5:15AM-5:30AM ET… | ✅ WIN | +1.71$ |
| 2026-07-18T09:23 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 18, 5:15AM-5:20AM ET… | ✅ WIN | +0.64$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-18T09:29 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,917.93 | 0.1min |  |
| ✅ ETH | $1,842.89 | 0.1min |  |
| ✅ SOL | $74.74 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,918.40 | consenso |  |
| ETH | $1,842.89 | consenso |  |
| SOL | $74.70 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*