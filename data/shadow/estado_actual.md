# Estado del bot — 2026-07-21 20:47 UTC

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
| P&L fiel (stake fijo 1$) | +3328.65 $ |
| P&L sim compuesto | 🟢 +6298.48 $ (ficción Kelly: +24758% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -117.00 $ |
| Operaciones resueltas | 27481 (16517 WIN / 10964 LOSS) — 60.1% |
| Señales abiertas | 134 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6623 | 59.9% | +0.099 | ➡️ estable | +2125.60$ | 0.99$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3819 | 63.4% | +0.134 | 📉 agota (-0.04) | +2057.62$ | 1.34$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3789 | 58.7% | +0.087 | ➡️ estable | +1221.74$ | 0.87$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1039 | 66.7% | +0.167 | ➡️ estable | +469.79$ | 1.67$ | ✅ activa |
| UPDOWN_GBM | 2084 | 52.6% | +0.026 | 📈 madura (+0.11) | +166.94$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 217 | 61.8% | +0.116 | 📉 agota (-0.04) | +104.09$ | 1.16$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4745 | 68.4% | +0.184 | ➡️ estable | +61.07$ | 1.84$ | ✅ activa |
| STREAK_FADE_15M | 256 | 58.2% | +0.081 | 📉 agota (-0.08) | +29.43$ | 0.81$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 639 | 62.6% | +0.126 | 📉 agota (-0.05) | +19.14$ | 1.26$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 105 | 79.0% | +0.285 | ➡️ estable | +18.78$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 260 | 49.2% | -0.008 | 📉 agota (-0.12) | +14.24$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 254 | 51.2% | +0.012 | 📉 agota (-0.16) | +10.81$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 233 | 81.5% | +0.313 | ➡️ estable | +10.63$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| LATE_WINDOW_5MIN | 241 | 47.7% | -0.023 | 📉 agota (-0.22) | +1.62$ | 0.50$ | ⚠️ IC negativo |
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
| 2026-07-21T20:40 | BALLENAS_CONFIRMADAS_15M#ETH#15min | Ethereum Up or Down - July 21, 4:15PM-4:30PM ET… | ✅ WIN | +4.11$ |
| 2026-07-21T20:40 | UPDOWN_GBM_15M_TARDIO#DOGE#15min | Dogecoin Up or Down - July 21, 4:15PM-4:30PM ET… | ✅ WIN | +1.51$ |
| 2026-07-21T20:40 | UPDOWN_GBM#DOGE#15min | Dogecoin Up or Down - July 21, 4:15PM-4:30PM ET… | ✅ WIN | +0.48$ |
| 2026-07-21T20:40 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 21, 4:15PM-4:30PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-21T20:40 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 21, 4:15PM-4:30PM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T20:46 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,418.01 | 0.1min |  |
| ✅ ETH | $1,924.12 | 0.1min |  |
| ✅ SOL | $78.00 | 0.1min |  |
| ✅ XRP | $1.15 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,422.60 | consenso |  |
| ETH | $1,924.12 | consenso |  |
| SOL | $77.97 | consenso |  |
| XRP | $1.15 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*