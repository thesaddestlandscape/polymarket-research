# Estado del bot — 2026-07-23 09:08 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **29.40 $** |
| P&L real total | 🔴 **-21.82 $** |
| P&L real hoy | +0.17 $ |
| P&L real 7 días | -0.74 $ |
| Fees pagados (real) | 9.77 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3652.19 $ |
| P&L sim compuesto | 🟢 +6903.20 $ (ficción Kelly: +27135% s/ operativo) |
| P&L sim hoy (2026-07-23) | 🟢 +191.34 $ |
| Operaciones resueltas | 30614 (18427 WIN / 12187 LOSS) — 60.2% |
| Señales abiertas | 149 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 7086 | 59.7% | +0.097 | 📉 agota (-0.03) | +2231.44$ | 0.97$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4284 | 62.8% | +0.128 | 📉 agota (-0.04) | +2198.07$ | 1.28$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4293 | 58.2% | +0.082 | ➡️ estable | +1309.75$ | 0.82$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1350 | 66.6% | +0.166 | ➡️ estable | +628.40$ | 1.66$ | ✅ activa |
| UPDOWN_GBM | 2316 | 53.2% | +0.031 | 📈 madura (+0.11) | +205.83$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 241 | 61.0% | +0.109 | 📉 agota (-0.06) | +110.91$ | 1.09$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5346 | 68.8% | +0.188 | ➡️ estable | +95.03$ | 1.88$ | ✅ activa |
| WEEKLY_PRICE | 336 | 68.2% | +0.180 | 📈 madura (+0.21) | +67.16$ | 1.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 839 | 62.9% | +0.129 | ➡️ estable | +38.19$ | 1.29$ | ✅ activa |
| STREAK_FADE_15M | 269 | 58.7% | +0.087 | 📉 agota (-0.06) | +36.16$ | 0.87$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 131 | 79.4% | +0.289 | ➡️ estable | +24.29$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 284 | 82.0% | +0.318 | ➡️ estable | +16.24$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1659 | 51.2% | +0.012 | ➡️ estable | +11.80$ | 0.50$ | ✅ activa |
| GBM_LATE_5M | 340 | 48.8% | -0.012 | 📉 agota (-0.19) | +10.60$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 263 | 51.0% | +0.009 | 📉 agota (-0.17) | +9.67$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 336 | 38.7% | -0.112 | ➡️ estable | +4.40$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 23 | 87.0% | +0.340 | — | +1.32$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 13 | 53.8% | +0.022 | — | +0.20$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| LATE_WINDOW_5MIN | 336 | 44.9% | -0.050 | 📉 agota (-0.16) | -4.47$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 319 | 44.2% | -0.058 | 📉 agota (-0.08) | -25.29$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-23T09:07 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 23, 4:45AM-5:00AM ET… | ✅ WIN | +2.08$ |
| 2026-07-23T09:07 | STREAK_FADE_15M#XRP#15min | XRP Up or Down - July 23, 4:45AM-5:00AM ET… | ✅ WIN | +1.71$ |
| 2026-07-23T09:07 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 23, 4:45AM-5:00AM ET… | ✅ WIN | +1.84$ |
| 2026-07-23T09:07 | BALLENAS_CONFIRMADAS_15M#XRP#15min | XRP Up or Down - July 23, 4:45AM-5:00AM ET… | ✅ WIN | +0.70$ |
| 2026-07-23T09:07 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 23, 4:45AM-5:00AM ET… | ✅ WIN | +1.84$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-23T09:06 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,688.49 | 0.1min |  |
| ✅ ETH | $1,929.54 | 0.1min |  |
| ✅ SOL | $77.57 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,688.49 | consenso |  |
| ETH | $1,929.38 | consenso |  |
| SOL | $77.53 | consenso |  |
| XRP | $1.14 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*