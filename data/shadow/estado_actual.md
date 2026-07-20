# Estado del bot — 2026-07-20 19:11 UTC

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
| P&L fiel (stake fijo 1$) | +3452.61 $ |
| P&L sim compuesto | 🟢 +6375.87 $ (ficción Kelly: +25062% s/ operativo) |
| P&L sim hoy (2026-07-20) | 🟢 +377.54 $ |
| Operaciones resueltas | 25057 (15246 WIN / 9811 LOSS) — 60.8% |
| Señales abiertas | 140 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6237 | 60.7% | +0.107 | ➡️ estable | +2169.67$ | 1.07$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3445 | 65.3% | +0.153 | ➡️ estable | +2131.74$ | 1.53$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3426 | 60.0% | +0.100 | 📈 madura (+0.03) | +1250.79$ | 1.00$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 830 | 66.9% | +0.168 | ➡️ estable | +367.51$ | 1.68$ | ✅ activa |
| UPDOWN_GBM | 1968 | 52.2% | +0.022 | 📈 madura (+0.12) | +141.53$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 185 | 65.9% | +0.158 | 📈 madura (+0.08) | +101.02$ | 1.58$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4335 | 68.7% | +0.187 | ➡️ estable | +80.85$ | 1.87$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 235 | 60.0% | +0.099 | ➡️ estable | +38.58$ | 0.99$ | ✅ activa |
| LATE_WINDOW_5MIN | 60 | 73.3% | +0.226 | 📈 madura (+0.12) | +32.92$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 212 | 56.6% | +0.065 | ➡️ estable | +21.42$ | 0.65$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 87 | 80.5% | +0.298 | 📉 agota (-0.06) | +18.13$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 475 | 63.8% | +0.137 | ➡️ estable | +17.71$ | 1.37$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 229 | 52.4% | +0.024 | 📉 agota (-0.14) | +13.31$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1638 | 51.2% | +0.012 | ➡️ estable | +13.23$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 190 | 82.6% | +0.323 | ➡️ estable | +11.46$ | 2.00$ | ✅ activa |
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
| 2026-07-20T19:06 | FAVORITO_CONFIRMADO#SOL#60min | Solana Up or Down - July 20, 2PM ET… | ❌ LOSS | -1.94$ |
| 2026-07-20T19:03 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 20, 2:45PM-3:00PM ET… | ✅ WIN | +1.32$ |
| 2026-07-20T19:03 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 20, 2:45PM-3:00PM ET… | ✅ WIN | +2.00$ |
| 2026-07-20T19:03 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 20, 2:45PM-3:00PM ET… | ✅ WIN | +1.33$ |
| 2026-07-20T19:03 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 20, 2:45PM-3:00PM ET… | ❌ LOSS | -0.99$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-20T19:08 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,129.06 | 0.1min |  |
| ✅ ETH | $1,893.55 | 0.1min |  |
| ✅ SOL | $77.72 | 0.1min |  |
| ✅ XRP | $1.12 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,134.40 | consenso |  |
| ETH | $1,893.55 | consenso |  |
| SOL | $77.57 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*