# Estado del bot — 2026-07-18 16:14 UTC

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
| P&L fiel (stake fijo 1$) | +2777.94 $ |
| P&L sim compuesto | 🟢 +4966.97 $ (ficción Kelly: +19524% s/ operativo) |
| P&L sim hoy (2026-07-18) | 🟢 +462.21 $ |
| Operaciones resueltas | 20879 (12584 WIN / 8295 LOSS) — 60.3% |
| Señales abiertas | 109 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 5561 | 60.5% | +0.105 | ➡️ estable | +1828.85$ | 1.05$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 2784 | 65.2% | +0.151 | ➡️ estable | +1637.26$ | 1.51$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 2724 | 60.2% | +0.102 | 📈 madura (+0.03) | +953.37$ | 1.02$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 474 | 68.6% | +0.185 | ➡️ estable | +203.40$ | 1.85$ | ✅ activa |
| UPDOWN_GBM | 1772 | 52.1% | +0.021 | 📈 madura (+0.13) | +132.78$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 162 | 66.7% | +0.165 | 📈 madura (+0.12) | +93.90$ | 1.65$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| STREAK_FADE_15M | 222 | 59.5% | +0.094 | ➡️ estable | +32.14$ | 0.94$ | ✅ activa |
| FAVORITO_CONFIRMADO | 3457 | 68.4% | +0.184 | ➡️ estable | +31.24$ | 1.84$ | ✅ activa |
| LATE_WINDOW_5MIN | 49 | 73.5% | +0.225 | ➡️ estable | +24.54$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 178 | 55.6% | +0.056 | 📉 agota (-0.12) | +18.17$ | 0.56$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 183 | 65.6% | +0.154 | 📉 agota (-0.05) | +16.04$ | 1.54$ | ✅ activa |
| ORDER_FLOW_5M | 1630 | 51.3% | +0.013 | ➡️ estable | +14.21$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 49 | 81.6% | +0.304 | 📈 madura (+0.05) | +12.04$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 120 | 81.7% | +0.311 | ➡️ estable | +4.89$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 326 | 38.3% | -0.116 | ➡️ estable | +3.81$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_5M | 27 | 55.6% | +0.052 | — | +1.11$ | 0.52$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 3 | 66.7% | +0.015 | — | +0.37$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
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
| 2026-07-18T16:11 | GBM_LATE_5M#SOL#5min | Solana Up or Down - July 18, 12:05PM-12:10PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-18T16:08 | FAVORITO_CONFIRMADO#SOL#60min | Solana Up or Down - July 18, 11AM ET… | ✅ WIN | +0.53$ |
| 2026-07-18T16:08 | FAVORITO_CONFIRMADO#ETH#240min | Ethereum Up or Down - July 18, 8:00AM-12:00PM ET… | ❌ LOSS | -1.53$ |
| 2026-07-18T16:08 | FAVORITO_CONFIRMADO#BTC#240min | Bitcoin Up or Down - July 18, 8:00AM-12:00PM ET… | ✅ WIN | +1.26$ |
| 2026-07-18T16:06 | FAVORITO_CONFIRMADO#BTC#60min | Bitcoin Up or Down - July 18, 11AM ET… | ✅ WIN | +1.32$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-18T16:13 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,077.00 | 0.1min |  |
| ✅ ETH | $1,841.88 | 0.1min |  |
| ✅ SOL | $75.04 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,077.00 | consenso |  |
| ETH | $1,842.12 | consenso |  |
| SOL | $74.92 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*