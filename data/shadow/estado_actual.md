# Estado del bot — 2026-07-21 15:03 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **26.28 $** |
| P&L real total | 🔴 **-24.94 $** |
| P&L real hoy | -1.48 $ |
| P&L real 7 días | -10.73 $ |
| Fees pagados (real) | 8.71 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3286.93 $ |
| P&L sim compuesto | 🟢 +6237.90 $ (ficción Kelly: +24520% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -177.58 $ |
| Operaciones resueltas | 26973 (16219 WIN / 10754 LOSS) — 60.1% |
| Señales abiertas | 128 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6543 | 59.9% | +0.098 | 📉 agota (-0.03) | +2106.49$ | 0.99$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3739 | 63.5% | +0.135 | 📉 agota (-0.04) | +2029.66$ | 1.35$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3710 | 58.7% | +0.087 | ➡️ estable | +1206.17$ | 0.87$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 994 | 67.0% | +0.170 | 📉 agota (-0.03) | +459.01$ | 1.70$ | ✅ activa |
| UPDOWN_GBM | 2063 | 52.7% | +0.027 | 📈 madura (+0.11) | +171.49$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 213 | 62.0% | +0.119 | 📉 agota (-0.04) | +100.10$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4651 | 68.6% | +0.186 | ➡️ estable | +75.47$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 256 | 58.2% | +0.081 | 📉 agota (-0.08) | +29.43$ | 0.81$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 104 | 79.8% | +0.292 | ➡️ estable | +20.82$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 254 | 50.4% | +0.004 | 📉 agota (-0.12) | +17.30$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 601 | 62.4% | +0.124 | 📉 agota (-0.05) | +15.39$ | 1.23$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 250 | 51.6% | +0.016 | 📉 agota (-0.15) | +11.79$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 223 | 81.6% | +0.313 | ➡️ estable | +11.47$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 214 | 49.5% | -0.005 | 📉 agota (-0.22) | +5.93$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 7 | 100.0% | +0.136 | — | +1.20$ | 1.36$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 8 | 50.0% | +0.000 | — | -0.26$ | 0.50$ | ✅ activa |
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
| 2026-07-21T14:59 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 10:50AM-10:55AM ET… | ✅ WIN | +2.21$ |
| 2026-07-21T14:53 | GBM_LATE_15M_PYCONFIRMADO#ETH#15min | Ethereum Up or Down - July 21, 10:30AM-10:45AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T14:53 | BALLENAS_CONFIRMADAS_15M#ETH#15min | Ethereum Up or Down - July 21, 10:30AM-10:45AM ET… | ✅ WIN | +0.48$ |
| 2026-07-21T14:53 | BALLENAS_CONFIRMADAS_15M#SOL#15min | Solana Up or Down - July 21, 10:30AM-10:45AM ET… | ✅ WIN | +0.76$ |
| 2026-07-21T14:53 | FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | Solana Up or Down - July 21, 10:30AM-10:45AM ET… | ✅ WIN | +0.76$ |

## Calidad de datos

⚠️ **DEGRADED** — última verificación 2026-07-21T15:02 UTC | rechazos 1h: 6 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,733.99 | 0.1min |  |
| ✅ ETH | $1,928.71 | 0.1min |  |
| ✅ SOL | $77.91 | 0.1min |  |
| ✅ XRP | $1.15 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,733.99 | consenso |  |
| ETH | $1,928.75 | consenso |  |
| SOL | $77.89 | consenso |  |
| XRP | $1.15 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:6 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*