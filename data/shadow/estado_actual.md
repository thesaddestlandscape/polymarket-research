# Estado del bot — 2026-07-21 17:11 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **24.65 $** |
| P&L real total | 🔴 **-26.57 $** |
| P&L real hoy | -1.13 $ |
| P&L real 7 días | -10.38 $ |
| Fees pagados (real) | 8.87 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3268.94 $ |
| P&L sim compuesto | 🟢 +6216.93 $ (ficción Kelly: +24438% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -198.55 $ |
| Operaciones resueltas | 27188 (16333 WIN / 10855 LOSS) — 60.1% |
| Señales abiertas | 124 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6573 | 59.8% | +0.098 | ➡️ estable | +2104.05$ | 0.98$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3770 | 63.4% | +0.134 | 📉 agota (-0.04) | +2027.14$ | 1.34$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3741 | 58.6% | +0.086 | ➡️ estable | +1203.53$ | 0.86$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1011 | 66.5% | +0.164 | 📉 agota (-0.04) | +450.57$ | 1.64$ | ✅ activa |
| UPDOWN_GBM | 2071 | 52.6% | +0.026 | 📈 madura (+0.11) | +168.62$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 214 | 62.1% | +0.120 | 📉 agota (-0.05) | +101.92$ | 1.20$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4690 | 68.6% | +0.185 | ➡️ estable | +73.84$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| STREAK_FADE_15M | 256 | 58.2% | +0.081 | 📉 agota (-0.08) | +29.43$ | 0.81$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 104 | 79.8% | +0.292 | ➡️ estable | +20.82$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 257 | 49.8% | -0.002 | 📉 agota (-0.13) | +15.77$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 253 | 51.4% | +0.014 | 📉 agota (-0.14) | +11.32$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 228 | 81.6% | +0.313 | ➡️ estable | +10.74$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 619 | 62.0% | +0.120 | 📉 agota (-0.06) | +10.06$ | 1.20$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| LATE_WINDOW_5MIN | 225 | 48.4% | -0.015 | 📉 agota (-0.22) | +1.08$ | 0.50$ | ⚠️ IC negativo |
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
| 2026-07-21T17:10 | BALLENAS_TARDIAS#BTC#15min | … | ❌ LOSS | -1.07$ |
| 2026-07-21T17:10 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 21, 12:45PM-1:00PM ET… | ✅ WIN | +0.41$ |
| 2026-07-21T17:10 | FAVORITO_CONFIRMADO#SOL#60min | Solana Up or Down - July 21, 12PM ET… | ❌ LOSS | -0.91$ |
| 2026-07-21T17:07 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 21, 12:45PM-1:00PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-21T17:04 | GBM_LATE_5M#ETH#5min | Ethereum Up or Down - July 21, 12:50PM-12:55PM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T17:09 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,478.84 | 0.1min |  |
| ✅ ETH | $1,925.29 | 0.1min |  |
| ✅ SOL | $78.11 | 0.1min |  |
| ✅ XRP | $1.15 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,480.30 | consenso |  |
| ETH | $1,925.84 | consenso |  |
| SOL | $78.09 | consenso |  |
| XRP | $1.15 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*