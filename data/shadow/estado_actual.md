# Estado del bot — 2026-07-21 18:12 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **23.89 $** |
| P&L real total | 🔴 **-27.33 $** |
| P&L real hoy | -4.36 $ |
| P&L real 7 días | -13.61 $ |
| Fees pagados (real) | 8.92 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3293.48 $ |
| P&L sim compuesto | 🟢 +6240.30 $ (ficción Kelly: +24529% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -175.18 $ |
| Operaciones resueltas | 27276 (16390 WIN / 10886 LOSS) — 60.1% |
| Señales abiertas | 123 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6588 | 59.8% | +0.098 | ➡️ estable | +2107.37$ | 0.98$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3786 | 63.4% | +0.134 | 📉 agota (-0.04) | +2037.97$ | 1.34$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3755 | 58.6% | +0.086 | ➡️ estable | +1203.70$ | 0.86$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1023 | 66.8% | +0.167 | ➡️ estable | +462.96$ | 1.67$ | ✅ activa |
| UPDOWN_GBM | 2074 | 52.7% | +0.026 | 📈 madura (+0.11) | +169.53$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 214 | 62.1% | +0.120 | 📉 agota (-0.05) | +101.92$ | 1.20$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4704 | 68.5% | +0.185 | ➡️ estable | +66.34$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| STREAK_FADE_15M | 256 | 58.2% | +0.081 | 📉 agota (-0.08) | +29.43$ | 0.81$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 104 | 79.8% | +0.292 | ➡️ estable | +20.82$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 257 | 49.8% | -0.002 | 📉 agota (-0.13) | +15.77$ | 0.50$ | ⚠️ IC negativo |
| BALLENAS_CONFIRMADAS_15M | 625 | 62.2% | +0.122 | 📉 agota (-0.06) | +12.36$ | 1.22$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 253 | 51.4% | +0.014 | 📉 agota (-0.14) | +11.32$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 228 | 81.6% | +0.313 | ➡️ estable | +10.74$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| LATE_WINDOW_5MIN | 232 | 48.3% | -0.017 | 📉 agota (-0.22) | +3.11$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 8 | 50.0% | +0.000 | — | -0.26$ | 0.50$ | ✅ activa |
| BALLENAS_TARDIAS | 10 | 70.0% | +0.083 | — | -2.01$ | 0.83$ | ✅ activa |
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
| 2026-07-21T18:11 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 2:00PM-2:05PM ET… | ✅ WIN | +2.82$ |
| 2026-07-21T18:07 | BALLENAS_CONFIRMADAS_15M#XRP#15min | XRP Up or Down - July 21, 1:45PM-2:00PM ET… | ✅ WIN | +0.76$ |
| 2026-07-21T18:07 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 21, 1:45PM-2:00PM ET… | ✅ WIN | +1.88$ |
| 2026-07-21T18:07 | UPDOWN_GBM_15M_TARDIO#DOGE#15min | Dogecoin Up or Down - July 21, 1:45PM-2:00PM ET… | ✅ WIN | +1.94$ |
| 2026-07-21T18:07 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 21, 1:45PM-2:00PM ET… | ✅ WIN | +1.88$ |

## Calidad de datos

⚠️ **DEGRADED** — última verificación 2026-07-21T18:10 UTC | rechazos 1h: 6 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,260.34 | 0.1min |  |
| ✅ ETH | $1,920.94 | 0.1min |  |
| ✅ SOL | $77.88 | 0.1min |  |
| ✅ XRP | $1.16 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,266.80 | consenso |  |
| ETH | $1,920.94 | consenso |  |
| SOL | $77.81 | consenso |  |
| XRP | $1.16 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:6 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*