# Estado del bot — 2026-07-20 23:49 UTC

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
| P&L fiel (stake fijo 1$) | +3472.04 $ |
| P&L sim compuesto | 🟢 +6418.08 $ (ficción Kelly: +25228% s/ operativo) |
| P&L sim hoy (2026-07-20) | 🟢 +419.76 $ |
| Operaciones resueltas | 25507 (15509 WIN / 9998 LOSS) — 60.8% |
| Señales abiertas | 127 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6305 | 60.6% | +0.106 | ➡️ estable | +2170.28$ | 1.06$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3509 | 65.0% | +0.150 | ➡️ estable | +2125.87$ | 1.50$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3488 | 59.9% | +0.099 | 📈 madura (+0.03) | +1255.67$ | 0.99$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 880 | 67.3% | +0.172 | ➡️ estable | +406.61$ | 1.72$ | ✅ activa |
| UPDOWN_GBM | 2005 | 52.3% | +0.023 | 📈 madura (+0.12) | +144.53$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 198 | 65.2% | +0.150 | 📈 madura (+0.05) | +106.48$ | 1.50$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4411 | 68.7% | +0.187 | ➡️ estable | +74.61$ | 1.87$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 241 | 59.8% | +0.097 | 📉 agota (-0.04) | +37.56$ | 0.97$ | ✅ activa |
| LATE_WINDOW_5MIN | 78 | 69.2% | +0.188 | 📉 agota (-0.05) | +30.95$ | 1.88$ | ✅ activa |
| GBM_LATE_5M | 219 | 56.2% | +0.061 | ➡️ estable | +23.10$ | 0.61$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 506 | 63.6% | +0.136 | ➡️ estable | +20.56$ | 1.36$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 91 | 79.1% | +0.285 | 📉 agota (-0.06) | +15.45$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 233 | 52.4% | +0.023 | 📉 agota (-0.14) | +14.03$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1638 | 51.2% | +0.012 | ➡️ estable | +13.23$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 197 | 82.7% | +0.324 | ➡️ estable | +12.63$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 6 | 66.7% | +0.037 | — | +0.87$ | 0.50$ | ⏳ acumulando |
| BALLENAS_TARDIAS | 3 | 100.0% | +0.045 | — | +0.51$ | 0.50$ | ⏳ acumulando |
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
| 2026-07-20T23:48 | BALLENAS_CONFIRMADAS_15M#XRP#15min | XRP Up or Down - July 20, 7:30PM-7:45PM ET… | ❌ LOSS | -1.11$ |
| 2026-07-20T23:48 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 20, 7:30PM-7:45PM ET… | ✅ WIN | +1.83$ |
| 2026-07-20T23:48 | BALLENAS_CONFIRMADAS_15M#SOL#15min | Solana Up or Down - July 20, 7:30PM-7:45PM ET… | ✅ WIN | +0.57$ |
| 2026-07-20T23:48 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 20, 7:30PM-7:45PM ET… | ❌ LOSS | -1.17$ |
| 2026-07-20T23:48 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 20, 7:30PM-7:45PM ET… | ✅ WIN | +2.17$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-20T23:47 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,189.74 | 0.1min |  |
| ✅ ETH | $1,900.83 | 0.1min |  |
| ✅ SOL | $77.78 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,201.90 | consenso |  |
| ETH | $1,900.94 | consenso |  |
| SOL | $77.66 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*