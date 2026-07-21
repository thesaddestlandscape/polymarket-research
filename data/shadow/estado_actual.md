# Estado del bot — 2026-07-21 20:23 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **24.65 $** |
| P&L real total | 🔴 **-26.57 $** |
| P&L real hoy | -1.12 $ |
| P&L real 7 días | -10.37 $ |
| Fees pagados (real) | 9.02 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3321.03 $ |
| P&L sim compuesto | 🟢 +6283.59 $ (ficción Kelly: +24700% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -131.89 $ |
| Operaciones resueltas | 27462 (16503 WIN / 10959 LOSS) — 60.1% |
| Señales abiertas | 124 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6619 | 59.9% | +0.099 | ➡️ estable | +2122.14$ | 0.99$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3815 | 63.4% | +0.134 | 📉 agota (-0.04) | +2053.90$ | 1.34$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3786 | 58.7% | +0.087 | ➡️ estable | +1219.90$ | 0.87$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1038 | 66.7% | +0.166 | ➡️ estable | +468.29$ | 1.66$ | ✅ activa |
| UPDOWN_GBM | 2082 | 52.5% | +0.025 | 📈 madura (+0.11) | +165.81$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 217 | 61.8% | +0.116 | 📉 agota (-0.04) | +104.09$ | 1.16$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4742 | 68.4% | +0.184 | ➡️ estable | +61.30$ | 1.84$ | ✅ activa |
| STREAK_FADE_15M | 256 | 58.2% | +0.081 | 📉 agota (-0.08) | +29.43$ | 0.81$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 105 | 79.0% | +0.285 | ➡️ estable | +18.78$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 638 | 62.5% | +0.125 | 📉 agota (-0.05) | +15.02$ | 1.25$ | ✅ activa |
| GBM_LATE_5M | 260 | 49.2% | -0.008 | 📉 agota (-0.12) | +14.24$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 254 | 51.2% | +0.012 | 📉 agota (-0.16) | +10.81$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 233 | 81.5% | +0.313 | ➡️ estable | +10.63$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| LATE_WINDOW_5MIN | 240 | 47.9% | -0.021 | 📉 agota (-0.22) | +2.29$ | 0.50$ | ⚠️ IC negativo |
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
| 2026-07-21T20:22 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 4:10PM-4:15PM ET… | ✅ WIN | +0.67$ |
| 2026-07-21T20:22 | BALLENAS_CONFIRMADAS_15M#SOL#15min | Solana Up or Down - July 21, 4:00PM-4:15PM ET… | ✅ WIN | +0.51$ |
| 2026-07-21T20:22 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 21, 4:05PM-4:10PM ET… | ❌ LOSS | -1.83$ |
| 2026-07-21T20:22 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 21, 4:00PM-4:15PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-21T20:22 | FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | Solana Up or Down - July 21, 4:00PM-4:15PM ET… | ✅ WIN | +0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T20:21 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,353.00 | 0.0min |  |
| ✅ ETH | $1,921.26 | 0.0min |  |
| ✅ SOL | $77.85 | 0.0min |  |
| ✅ XRP | $1.15 | 0.0min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,355.10 | consenso |  |
| ETH | $1,920.90 | consenso |  |
| SOL | $77.85 | consenso |  |
| XRP | $1.15 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*