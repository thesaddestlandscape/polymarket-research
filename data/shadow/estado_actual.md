# Estado del bot — 2026-07-21 17:53 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **23.75 $** |
| P&L real total | 🔴 **-27.47 $** |
| P&L real hoy | -3.28 $ |
| P&L real 7 días | -12.53 $ |
| Fees pagados (real) | 8.90 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3277.93 $ |
| P&L sim compuesto | 🟢 +6221.12 $ (ficción Kelly: +24454% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -194.36 $ |
| Operaciones resueltas | 27243 (16365 WIN / 10878 LOSS) — 60.1% |
| Señales abiertas | 134 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6584 | 59.8% | +0.098 | ➡️ estable | +2105.50$ | 0.98$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3781 | 63.4% | +0.134 | 📉 agota (-0.04) | +2033.49$ | 1.34$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3752 | 58.6% | +0.086 | ➡️ estable | +1204.14$ | 0.86$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1017 | 66.6% | +0.165 | 📉 agota (-0.04) | +454.37$ | 1.65$ | ✅ activa |
| UPDOWN_GBM | 2072 | 52.6% | +0.026 | 📈 madura (+0.11) | +167.38$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 214 | 62.1% | +0.120 | 📉 agota (-0.05) | +101.92$ | 1.20$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4696 | 68.5% | +0.185 | ➡️ estable | +68.04$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| STREAK_FADE_15M | 256 | 58.2% | +0.081 | 📉 agota (-0.08) | +29.43$ | 0.81$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 104 | 79.8% | +0.292 | ➡️ estable | +20.82$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 257 | 49.8% | -0.002 | 📉 agota (-0.13) | +15.77$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 253 | 51.4% | +0.014 | 📉 agota (-0.14) | +11.32$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 623 | 62.1% | +0.121 | 📉 agota (-0.06) | +11.20$ | 1.21$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 228 | 81.6% | +0.313 | ➡️ estable | +10.74$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| LATE_WINDOW_5MIN | 229 | 48.0% | -0.019 | 📉 agota (-0.23) | +0.04$ | 0.50$ | ⚠️ IC negativo |
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
| 2026-07-21T17:52 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 21, 1:30PM-1:45PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T17:52 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 21, 1:30PM-1:45PM ET… | ❌ LOSS | -1.64$ |
| 2026-07-21T17:52 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 21, 1:30PM-1:45PM ET… | ❌ LOSS | -0.54$ |
| 2026-07-21T17:49 | BALLENAS_CONFIRMADAS_15M#ETH#15min | Ethereum Up or Down - July 21, 1:30PM-1:45PM ET… | ❌ LOSS | -0.54$ |
| 2026-07-21T17:49 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 21, 1:30PM-1:45PM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T17:52 UTC | rechazos 1h: 4 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,300.29 | 0.1min |  |
| ✅ ETH | $1,920.79 | 0.1min |  |
| ✅ SOL | $77.77 | 0.1min |  |
| ✅ XRP | $1.16 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,300.29 | consenso |  |
| ETH | $1,920.79 | consenso |  |
| SOL | $77.74 | consenso |  |
| XRP | $1.16 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:4 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*