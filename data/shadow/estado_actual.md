# Estado del bot — 2026-07-20 11:27 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **0.78 $** |
| P&L real total | 🔴 **-24.66 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -13.66 $ |
| Fees pagados (real) | 8.68 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3376.07 $ |
| P&L sim compuesto | 🟢 +6218.88 $ (ficción Kelly: +24445% s/ operativo) |
| P&L sim hoy (2026-07-20) | 🟢 +220.55 $ |
| Operaciones resueltas | 24438 (14860 WIN / 9578 LOSS) — 60.8% |
| Señales abiertas | 130 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6132 | 60.7% | +0.107 | ➡️ estable | +2141.06$ | 1.07$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3351 | 65.4% | +0.153 | ➡️ estable | +2064.43$ | 1.53$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3319 | 60.3% | +0.103 | 📈 madura (+0.04) | +1235.99$ | 1.03$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 783 | 67.3% | +0.173 | ➡️ estable | +353.83$ | 1.73$ | ✅ activa |
| UPDOWN_GBM | 1937 | 51.9% | +0.019 | 📈 madura (+0.11) | +128.85$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 182 | 65.9% | +0.158 | 📈 madura (+0.09) | +97.69$ | 1.58$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4203 | 68.7% | +0.187 | ➡️ estable | +78.98$ | 1.87$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| STREAK_FADE_15M | 235 | 60.0% | +0.099 | ➡️ estable | +38.58$ | 0.99$ | ✅ activa |
| LATE_WINDOW_5MIN | 55 | 70.9% | +0.202 | ➡️ estable | +23.91$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 200 | 57.5% | +0.074 | ➡️ estable | +22.88$ | 0.74$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 83 | 79.5% | +0.288 | 📉 agota (-0.11) | +15.82$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 426 | 63.6% | +0.136 | ➡️ estable | +15.19$ | 1.35$ | ✅ activa |
| ORDER_FLOW_5M | 1638 | 51.2% | +0.012 | ➡️ estable | +13.23$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 179 | 82.7% | +0.323 | ➡️ estable | +11.90$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 220 | 52.3% | +0.023 | 📉 agota (-0.15) | +11.86$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 6 | 66.7% | +0.037 | — | +0.87$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-20T11:26 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 20, 7:20AM-7:25AM ET… | ✅ WIN | +1.52$ |
| 2026-07-20T11:26 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 20, 7:15AM-7:20AM ET… | ❌ LOSS | -1.63$ |
| 2026-07-20T11:18 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 20, 7:10AM-7:15AM ET… | ✅ WIN | +0.61$ |
| 2026-07-20T11:18 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 20, 7:10AM-7:15AM ET… | ❌ LOSS | -1.63$ |
| 2026-07-20T11:15 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 20, 7:00AM-7:15AM ET… | ✅ WIN | +0.15$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-20T11:26 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,271.08 | 0.1min |  |
| ✅ ETH | $1,871.23 | 0.1min |  |
| ✅ SOL | $76.41 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,271.08 | consenso |  |
| ETH | $1,871.23 | consenso |  |
| SOL | $76.42 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*