# Estado del bot — 2026-07-23 17:46 UTC

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
| P&L fiel (stake fijo 1$) | +3601.08 $ |
| P&L sim compuesto | 🟢 +6867.39 $ (ficción Kelly: +26994% s/ operativo) |
| P&L sim hoy (2026-07-23) | 🟢 +155.53 $ |
| Operaciones resueltas | 31383 (18835 WIN / 12548 LOSS) — 60.0% |
| Señales abiertas | 160 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 7189 | 59.5% | +0.095 | 📉 agota (-0.04) | +2219.90$ | 0.95$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4383 | 62.4% | +0.124 | 📉 agota (-0.05) | +2172.06$ | 1.24$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4402 | 57.6% | +0.076 | 📉 agota (-0.03) | +1269.31$ | 0.76$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1407 | 66.5% | +0.165 | ➡️ estable | +655.96$ | 1.65$ | ✅ activa |
| UPDOWN_GBM | 2371 | 53.2% | +0.032 | 📈 madura (+0.10) | +209.95$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 242 | 60.7% | +0.107 | 📉 agota (-0.06) | +110.40$ | 1.07$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5485 | 68.8% | +0.188 | ➡️ estable | +107.24$ | 1.88$ | ✅ activa |
| WEEKLY_PRICE | 352 | 69.0% | +0.189 | 📈 madura (+0.23) | +69.51$ | 1.89$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 872 | 62.8% | +0.128 | ➡️ estable | +43.29$ | 1.28$ | ✅ activa |
| STREAK_FADE_15M | 271 | 58.7% | +0.086 | 📉 agota (-0.06) | +35.54$ | 0.86$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 133 | 79.7% | +0.293 | ➡️ estable | +25.22$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 294 | 82.3% | +0.321 | ➡️ estable | +18.98$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1659 | 51.2% | +0.012 | ➡️ estable | +11.80$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 265 | 50.9% | +0.009 | 📉 agota (-0.16) | +9.65$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 336 | 38.7% | -0.112 | ➡️ estable | +4.40$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 12 | 83.3% | +0.171 | — | +2.98$ | 1.71$ | ✅ activa |
| BALLENAS_TARDIAS | 26 | 88.5% | +0.357 | — | +2.42$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 13 | 53.8% | +0.022 | — | +0.20$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_5M | 464 | 47.6% | -0.024 | 📉 agota (-0.12) | -0.63$ | 0.50$ | ⚠️ IC negativo |
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
| 2026-07-23T17:45 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 23, 1:35PM-1:40PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-23T17:45 | GBM_LATE_5M#BTC#5min | Bitcoin Up or Down - July 23, 1:30PM-1:35PM ET… | ✅ WIN | +1.20$ |
| 2026-07-23T17:42 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 23, 1:30PM-1:35PM ET… | ✅ WIN | +0.49$ |
| 2026-07-23T17:38 | UPDOWN_GBM_15M_TARDIO#DOGE#15min | Dogecoin Up or Down - July 23, 1:15PM-1:30PM ET… | ✅ WIN | +1.73$ |
| 2026-07-23T17:38 | UPDOWN_GBM#DOGE#15min | Dogecoin Up or Down - July 23, 1:15PM-1:30PM ET… | ✅ WIN | +1.73$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-23T17:44 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,760.68 | 0.1min |  |
| ✅ ETH | $1,887.67 | 0.1min |  |
| ✅ SOL | $76.00 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,772.40 | consenso |  |
| ETH | $1,887.67 | consenso |  |
| SOL | $75.94 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*