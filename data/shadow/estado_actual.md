# Estado del bot — 2026-07-21 17:24 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **24.30 $** |
| P&L real total | 🔴 **-26.92 $** |
| P&L real hoy | -3.28 $ |
| P&L real 7 días | -12.53 $ |
| Fees pagados (real) | 8.87 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3280.72 $ |
| P&L sim compuesto | 🟢 +6235.06 $ (ficción Kelly: +24509% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -180.42 $ |
| Operaciones resueltas | 27205 (16349 WIN / 10856 LOSS) — 60.1% |
| Señales abiertas | 128 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6576 | 59.8% | +0.098 | ➡️ estable | +2107.43$ | 0.98$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3773 | 63.4% | +0.134 | 📉 agota (-0.04) | +2032.43$ | 1.34$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3744 | 58.7% | +0.086 | ➡️ estable | +1206.08$ | 0.86$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1014 | 66.6% | +0.165 | 📉 agota (-0.04) | +454.82$ | 1.65$ | ✅ activa |
| UPDOWN_GBM | 2071 | 52.6% | +0.026 | 📈 madura (+0.11) | +168.62$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 214 | 62.1% | +0.120 | 📉 agota (-0.05) | +101.92$ | 1.20$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4692 | 68.6% | +0.186 | ➡️ estable | +76.20$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| STREAK_FADE_15M | 256 | 58.2% | +0.081 | 📉 agota (-0.08) | +29.43$ | 0.81$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 104 | 79.8% | +0.292 | ➡️ estable | +20.82$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 257 | 49.8% | -0.002 | 📉 agota (-0.13) | +15.77$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 253 | 51.4% | +0.014 | 📉 agota (-0.14) | +11.32$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 621 | 62.2% | +0.121 | 📉 agota (-0.06) | +11.20$ | 1.21$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 228 | 81.6% | +0.313 | ➡️ estable | +10.74$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| LATE_WINDOW_5MIN | 226 | 48.2% | -0.018 | 📉 agota (-0.23) | +0.24$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 8 | 50.0% | +0.000 | — | -0.26$ | 0.50$ | ✅ activa |
| BALLENAS_TARDIAS | 9 | 77.8% | +0.102 | — | -0.94$ | 1.02$ | ✅ activa |
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
| 2026-07-21T17:22 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 1:10PM-1:15PM ET… | ❌ LOSS | -0.85$ |
| 2026-07-21T17:20 | BALLENAS_CONFIRMADAS_15M#SOL#15min | Solana Up or Down - July 21, 1:00PM-1:15PM ET… | ✅ WIN | +0.37$ |
| 2026-07-21T17:20 | BALLENAS_CONFIRMADAS_15M#XRP#15min | XRP Up or Down - July 21, 1:00PM-1:15PM ET… | ✅ WIN | +0.76$ |
| 2026-07-21T17:20 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 21, 1:00PM-1:15PM ET… | ✅ WIN | +1.04$ |
| 2026-07-21T17:20 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 21, 1:00PM-1:15PM ET… | ✅ WIN | +0.26$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T17:22 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,391.24 | 0.1min |  |
| ✅ ETH | $1,922.33 | 0.1min |  |
| ✅ SOL | $77.96 | 0.1min |  |
| ✅ XRP | $1.15 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,413.30 | consenso |  |
| ETH | $1,922.33 | consenso |  |
| SOL | $77.91 | consenso |  |
| XRP | $1.15 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*