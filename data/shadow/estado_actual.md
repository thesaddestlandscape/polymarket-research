# Estado del bot — 2026-07-21 14:22 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **25.61 $** |
| P&L real total | 🔴 **-25.61 $** |
| P&L real hoy | -2.17 $ |
| P&L real 7 días | -11.42 $ |
| Fees pagados (real) | 8.68 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3289.78 $ |
| P&L sim compuesto | 🟢 +6229.53 $ (ficción Kelly: +24487% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -185.95 $ |
| Operaciones resueltas | 26915 (16187 WIN / 10728 LOSS) — 60.1% |
| Señales abiertas | 132 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6534 | 59.9% | +0.099 | ➡️ estable | +2107.39$ | 0.99$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3730 | 63.5% | +0.135 | 📉 agota (-0.04) | +2031.66$ | 1.35$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3704 | 58.7% | +0.087 | ➡️ estable | +1208.44$ | 0.87$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 987 | 67.0% | +0.169 | 📉 agota (-0.03) | +454.38$ | 1.69$ | ✅ activa |
| UPDOWN_GBM | 2057 | 52.7% | +0.027 | 📈 madura (+0.11) | +170.83$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 212 | 62.3% | +0.121 | 📉 agota (-0.04) | +100.61$ | 1.21$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4644 | 68.5% | +0.185 | ➡️ estable | +70.28$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 256 | 58.2% | +0.081 | 📉 agota (-0.08) | +29.43$ | 0.81$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 103 | 79.6% | +0.290 | ➡️ estable | +19.56$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 253 | 50.6% | +0.006 | 📉 agota (-0.13) | +17.81$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 595 | 62.2% | +0.121 | 📉 agota (-0.04) | +12.98$ | 1.21$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 250 | 51.6% | +0.016 | 📉 agota (-0.15) | +11.79$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 222 | 81.5% | +0.312 | ➡️ estable | +10.71$ | 2.00$ | ✅ activa |
| LATE_WINDOW_5MIN | 210 | 50.0% | +0.000 | 📉 agota (-0.21) | +6.28$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
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
| 2026-07-21T14:21 | GBM_LATE_5M#BTC#5min | Bitcoin Up or Down - July 21, 10:10AM-10:15AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T14:21 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 10:10AM-10:15AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T14:21 | GBM_LATE_5M#ETH#5min | Ethereum Up or Down - July 21, 10:10AM-10:15AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T14:18 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 21, 10:00AM-10:15AM ET… | ✅ WIN | +1.56$ |
| 2026-07-21T14:18 | BALLENAS_CONFIRMADAS_15M#SOL#15min | Solana Up or Down - July 21, 10:00AM-10:15AM ET… | ✅ WIN | +0.56$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T14:20 UTC | rechazos 1h: 4 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,822.79 | 0.1min |  |
| ✅ ETH | $1,936.07 | 0.1min |  |
| ✅ SOL | $78.31 | 0.1min |  |
| ✅ XRP | $1.15 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,827.40 | consenso |  |
| ETH | $1,936.07 | consenso |  |
| SOL | $78.28 | consenso |  |
| XRP | $1.14 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:4 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*