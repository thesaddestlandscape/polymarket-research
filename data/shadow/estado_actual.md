# Estado del bot — 2026-07-22 03:15 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **23.79 $** |
| P&L real total | 🔴 **-27.43 $** |
| P&L real hoy | +1.28 $ |
| P&L real 7 días | -8.31 $ |
| Fees pagados (real) | 9.06 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3376.44 $ |
| P&L sim compuesto | 🟢 +6410.43 $ (ficción Kelly: +25198% s/ operativo) |
| P&L sim hoy (2026-07-22) | 🟢 +46.93 $ |
| Operaciones resueltas | 28056 (16858 WIN / 11198 LOSS) — 60.1% |
| Señales abiertas | 142 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6710 | 59.8% | +0.098 | ➡️ estable | +2137.29$ | 0.98$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3902 | 63.2% | +0.132 | 📉 agota (-0.04) | +2072.62$ | 1.32$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3877 | 58.6% | +0.085 | ➡️ estable | +1243.59$ | 0.86$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1096 | 66.5% | +0.165 | ➡️ estable | +496.41$ | 1.65$ | ✅ activa |
| UPDOWN_GBM | 2123 | 52.7% | +0.027 | 📈 madura (+0.11) | +172.55$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 222 | 61.3% | +0.112 | 📉 agota (-0.05) | +105.71$ | 1.12$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4854 | 68.6% | +0.186 | ➡️ estable | +81.52$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| STREAK_FADE_15M | 260 | 58.1% | +0.080 | 📉 agota (-0.08) | +29.21$ | 0.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 682 | 62.6% | +0.126 | 📉 agota (-0.04) | +24.98$ | 1.26$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 114 | 78.9% | +0.284 | ➡️ estable | +19.95$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 242 | 82.2% | +0.320 | ➡️ estable | +14.51$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 269 | 49.4% | -0.006 | 📉 agota (-0.13) | +14.32$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1647 | 51.1% | +0.011 | ➡️ estable | +11.75$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 256 | 51.2% | +0.012 | 📉 agota (-0.15) | +10.84$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 8 | 50.0% | +0.000 | — | -0.26$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 266 | 45.9% | -0.041 | 📉 agota (-0.22) | -1.19$ | 0.50$ | ⚠️ IC negativo |
| BALLENAS_TARDIAS | 13 | 76.9% | +0.152 | — | -1.30$ | 1.52$ | ✅ activa |
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
| 2026-07-22T03:11 | GBM_LATE_5M#SOL#5min | Solana Up or Down - July 21, 11:00PM-11:05PM ET… | ✅ WIN | +0.25$ |
| 2026-07-22T03:11 | GBM_LATE_5M#BTC#5min | Bitcoin Up or Down - July 21, 11:00PM-11:05PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-22T03:11 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 11:00PM-11:05PM ET… | ✅ WIN | +2.94$ |
| 2026-07-22T03:11 | GBM_LATE_5M#ETH#5min | Ethereum Up or Down - July 21, 11:00PM-11:05PM ET… | ✅ WIN | +0.36$ |
| 2026-07-22T03:11 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 21, 10:45PM-11:00PM ET… | ✅ WIN | +1.32$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-22T03:13 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,192.24 | 0.1min |  |
| ✅ ETH | $1,927.58 | 0.1min |  |
| ✅ SOL | $78.01 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,192.24 | consenso |  |
| ETH | $1,927.58 | consenso |  |
| SOL | $77.97 | consenso |  |
| XRP | $1.14 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*