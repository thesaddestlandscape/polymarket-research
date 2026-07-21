# Estado del bot — 2026-07-21 18:43 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **23.76 $** |
| P&L real total | 🔴 **-27.46 $** |
| P&L real hoy | -2.75 $ |
| P&L real 7 días | -12.00 $ |
| Fees pagados (real) | 8.92 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3290.94 $ |
| P&L sim compuesto | 🟢 +6239.74 $ (ficción Kelly: +24527% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -175.74 $ |
| Operaciones resueltas | 27311 (16407 WIN / 10904 LOSS) — 60.1% |
| Señales abiertas | 118 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6595 | 59.8% | +0.098 | ➡️ estable | +2109.84$ | 0.98$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3791 | 63.4% | +0.134 | 📉 agota (-0.04) | +2039.63$ | 1.34$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3762 | 58.6% | +0.086 | ➡️ estable | +1206.16$ | 0.86$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1023 | 66.8% | +0.167 | ➡️ estable | +462.96$ | 1.67$ | ✅ activa |
| UPDOWN_GBM | 2077 | 52.6% | +0.026 | 📈 madura (+0.11) | +167.36$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 215 | 61.9% | +0.118 | 📉 agota (-0.05) | +101.41$ | 1.17$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4711 | 68.5% | +0.185 | ➡️ estable | +64.79$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| STREAK_FADE_15M | 256 | 58.2% | +0.081 | 📉 agota (-0.08) | +29.43$ | 0.81$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 104 | 79.8% | +0.292 | ➡️ estable | +20.82$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 257 | 49.8% | -0.002 | 📉 agota (-0.13) | +15.77$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 253 | 51.4% | +0.014 | 📉 agota (-0.14) | +11.32$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 229 | 81.7% | +0.314 | ➡️ estable | +10.89$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 627 | 62.0% | +0.120 | 📉 agota (-0.06) | +9.46$ | 1.20$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| LATE_WINDOW_5MIN | 234 | 48.3% | -0.017 | 📉 agota (-0.21) | +2.95$ | 0.50$ | ⚠️ IC negativo |
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
| 2026-07-21T18:42 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 21, 2:15PM-2:30PM ET… | ✅ WIN | +1.16$ |
| 2026-07-21T18:42 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 21, 2:15PM-2:30PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T18:42 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 21, 2:15PM-2:30PM ET… | ❌ LOSS | -0.93$ |
| 2026-07-21T18:39 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 2:25PM-2:30PM ET… | ❌ LOSS | -0.70$ |
| 2026-07-21T18:39 | BALLENAS_CONFIRMADAS_15M#ETH#15min | Ethereum Up or Down - July 21, 2:15PM-2:30PM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T18:41 UTC | rechazos 1h: 3 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,213.01 | 0.1min |  |
| ✅ ETH | $1,919.60 | 0.1min |  |
| ✅ SOL | $77.90 | 0.1min |  |
| ✅ XRP | $1.16 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,213.01 | consenso |  |
| ETH | $1,919.60 | consenso |  |
| SOL | $77.84 | consenso |  |
| XRP | $1.16 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:3 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*