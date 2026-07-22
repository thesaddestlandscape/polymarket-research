# Estado del bot — 2026-07-22 15:05 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **28.40 $** |
| P&L real total | 🔴 **-22.82 $** |
| P&L real hoy | +4.92 $ |
| P&L real 7 días | -4.67 $ |
| Fees pagados (real) | 9.34 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3422.57 $ |
| P&L sim compuesto | 🟢 +6511.86 $ (ficción Kelly: +25597% s/ operativo) |
| P&L sim hoy (2026-07-22) | 🟢 +148.35 $ |
| Operaciones resueltas | 29082 (17452 WIN / 11630 LOSS) — 60.0% |
| Señales abiertas | 135 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6855 | 59.6% | +0.096 | 📉 agota (-0.03) | +2140.96$ | 0.96$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4054 | 62.9% | +0.128 | 📉 agota (-0.04) | +2101.49$ | 1.29$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4046 | 58.1% | +0.081 | ➡️ estable | +1236.95$ | 0.81$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1194 | 66.3% | +0.163 | 📉 agota (-0.05) | +543.90$ | 1.63$ | ✅ activa |
| UPDOWN_GBM | 2191 | 52.9% | +0.029 | 📈 madura (+0.11) | +186.97$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 228 | 61.4% | +0.113 | 📉 agota (-0.05) | +109.02$ | 1.13$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5058 | 68.7% | +0.187 | ➡️ estable | +92.52$ | 1.87$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 749 | 62.5% | +0.125 | ➡️ estable | +32.94$ | 1.25$ | ✅ activa |
| STREAK_FADE_15M | 262 | 58.0% | +0.080 | 📉 agota (-0.08) | +28.71$ | 0.80$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 119 | 79.0% | +0.285 | ➡️ estable | +20.13$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 261 | 82.4% | +0.321 | ➡️ estable | +17.18$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1653 | 51.1% | +0.011 | ➡️ estable | +11.85$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 259 | 51.0% | +0.010 | 📉 agota (-0.16) | +9.65$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 334 | 38.9% | -0.110 | ➡️ estable | +5.42$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_5M | 284 | 48.2% | -0.017 | 📉 agota (-0.13) | +5.25$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 11 | 45.5% | -0.021 | — | -0.76$ | 0.50$ | ⚠️ IC negativo |
| BALLENAS_TARDIAS | 15 | 80.0% | +0.199 | — | -0.90$ | 1.99$ | ✅ activa |
| LATE_WINDOW_5MIN | 322 | 45.3% | -0.046 | 📉 agota (-0.17) | -1.93$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 316 | 44.3% | -0.057 | 📉 agota (-0.09) | -24.82$ | 0.50$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-22T15:04 | GBM_LATE_15M_PYCONFIRMADO#ETH#15min | Ethereum Up or Down - July 22, 10:45AM-11:00AM ET… | ✅ WIN | +0.80$ |
| 2026-07-22T15:04 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 22, 10:45AM-11:00AM ET… | ✅ WIN | +0.80$ |
| 2026-07-22T15:04 | BALLENAS_CONFIRMADAS_15M#ETH#15min | Ethereum Up or Down - July 22, 10:45AM-11:00AM ET… | ✅ WIN | +0.80$ |
| 2026-07-22T15:04 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 22, 10:45AM-11:00AM ET… | ✅ WIN | +0.92$ |
| 2026-07-22T15:04 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 22, 10:45AM-11:00AM ET… | ✅ WIN | +1.11$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-22T15:03 UTC | rechazos 1h: 4 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,784.00 | 0.0min |  |
| ✅ ETH | $1,933.11 | 0.0min |  |
| ✅ SOL | $77.88 | 0.0min |  |
| ✅ XRP | $1.14 | 0.0min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,787.30 | consenso |  |
| ETH | $1,932.99 | consenso |  |
| SOL | $78.00 | consenso |  |
| XRP | $1.14 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:4 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*