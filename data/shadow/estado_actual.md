# Estado del bot — 2026-07-23 19:37 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **26.91 $** |
| P&L real total | 🔴 **-24.31 $** |
| P&L real hoy | -2.32 $ |
| P&L real 7 días | -3.23 $ |
| Fees pagados (real) | 9.91 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3624.77 $ |
| P&L sim compuesto | 🟢 +6907.02 $ (ficción Kelly: +27150% s/ operativo) |
| P&L sim hoy (2026-07-23) | 🟢 +195.16 $ |
| Operaciones resueltas | 31532 (18929 WIN / 12603 LOSS) — 60.0% |
| Señales abiertas | 161 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 7215 | 59.6% | +0.096 | 📉 agota (-0.04) | +2237.73$ | 0.96$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4406 | 62.4% | +0.124 | 📉 agota (-0.05) | +2189.22$ | 1.24$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4428 | 57.7% | +0.077 | 📉 agota (-0.03) | +1283.25$ | 0.77$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1416 | 66.4% | +0.164 | ➡️ estable | +655.33$ | 1.64$ | ✅ activa |
| UPDOWN_GBM | 2377 | 53.1% | +0.031 | 📈 madura (+0.10) | +206.47$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 245 | 60.8% | +0.107 | 📉 agota (-0.06) | +111.22$ | 1.07$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5515 | 68.8% | +0.188 | ➡️ estable | +101.20$ | 1.88$ | ✅ activa |
| WEEKLY_PRICE | 352 | 69.0% | +0.189 | 📈 madura (+0.23) | +69.51$ | 1.89$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 880 | 62.8% | +0.128 | ➡️ estable | +41.65$ | 1.28$ | ✅ activa |
| STREAK_FADE_15M | 271 | 58.7% | +0.086 | 📉 agota (-0.06) | +35.54$ | 0.86$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 134 | 79.9% | +0.294 | ➡️ estable | +25.87$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 296 | 82.4% | +0.322 | ➡️ estable | +20.13$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1659 | 51.2% | +0.012 | ➡️ estable | +11.80$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 265 | 50.9% | +0.009 | 📉 agota (-0.16) | +9.65$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 336 | 38.7% | -0.112 | ➡️ estable | +4.40$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 12 | 83.3% | +0.171 | — | +2.98$ | 1.71$ | ✅ activa |
| BALLENAS_TARDIAS | 26 | 88.5% | +0.357 | — | +2.42$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 13 | 53.8% | +0.022 | — | +0.20$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_5M | 479 | 47.6% | -0.024 | 📉 agota (-0.09) | -0.77$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| LATE_WINDOW_5MIN | 348 | 44.8% | -0.051 | 📉 agota (-0.14) | -4.38$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 320 | 44.1% | -0.059 | 📉 agota (-0.08) | -26.41$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-23T19:36 | GBM_LATE_5M#ETH#5min | Ethereum Up or Down - July 23, 3:25PM-3:30PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-23T19:36 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 23, 3:15PM-3:30PM ET… | ✅ WIN | +1.84$ |
| 2026-07-23T19:36 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 23, 3:15PM-3:30PM ET… | ✅ WIN | +1.56$ |
| 2026-07-23T19:36 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 23, 3:15PM-3:30PM ET… | ✅ WIN | +1.03$ |
| 2026-07-23T19:36 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 23, 3:15PM-3:30PM ET… | ✅ WIN | +1.32$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-23T19:36 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,827.47 | 0.1min |  |
| ✅ ETH | $1,879.68 | 0.1min |  |
| ✅ SOL | $75.74 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,838.20 | consenso |  |
| ETH | $1,880.00 | consenso |  |
| SOL | $75.72 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*