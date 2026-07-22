# Estado del bot — 2026-07-22 02:52 UTC

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
| P&L fiel (stake fijo 1$) | +3371.60 $ |
| P&L sim compuesto | 🟢 +6406.72 $ (ficción Kelly: +25184% s/ operativo) |
| P&L sim hoy (2026-07-22) | 🟢 +43.21 $ |
| Operaciones resueltas | 28032 (16843 WIN / 11189 LOSS) — 60.1% |
| Señales abiertas | 130 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6708 | 59.8% | +0.098 | ➡️ estable | +2139.92$ | 0.98$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3900 | 63.2% | +0.132 | 📉 agota (-0.04) | +2075.64$ | 1.32$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3875 | 58.6% | +0.086 | ➡️ estable | +1246.36$ | 0.86$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1095 | 66.5% | +0.165 | ➡️ estable | +494.70$ | 1.65$ | ✅ activa |
| UPDOWN_GBM | 2122 | 52.6% | +0.026 | 📈 madura (+0.11) | +172.05$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 222 | 61.3% | +0.112 | 📉 agota (-0.05) | +105.71$ | 1.12$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4847 | 68.5% | +0.185 | ➡️ estable | +73.70$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| STREAK_FADE_15M | 260 | 58.1% | +0.080 | 📉 agota (-0.08) | +29.21$ | 0.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 681 | 62.6% | +0.125 | 📉 agota (-0.04) | +24.30$ | 1.25$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 114 | 78.9% | +0.284 | ➡️ estable | +19.95$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 266 | 49.2% | -0.007 | 📉 agota (-0.13) | +15.75$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 242 | 82.2% | +0.320 | ➡️ estable | +14.51$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1647 | 51.1% | +0.011 | ➡️ estable | +11.75$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 256 | 51.2% | +0.012 | 📉 agota (-0.15) | +10.84$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 8 | 50.0% | +0.000 | — | -0.26$ | 0.50$ | ✅ activa |
| BALLENAS_TARDIAS | 13 | 76.9% | +0.152 | — | -1.30$ | 1.52$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| LATE_WINDOW_5MIN | 261 | 45.6% | -0.044 | 📉 agota (-0.24) | -4.05$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-22T02:50 | GBM_LATE_5M#ETH#5min | Ethereum Up or Down - July 21, 10:40PM-10:45PM ET… | ✅ WIN | +0.71$ |
| 2026-07-22T02:50 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 21, 10:40PM-10:45PM ET… | ✅ WIN | +0.66$ |
| 2026-07-22T02:50 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 21, 10:40PM-10:45PM ET… | ✅ WIN | +1.06$ |
| 2026-07-22T02:50 | UPDOWN_GBM_15M_TARDIO#XRP#15min | XRP Up or Down - July 21, 10:30PM-10:45PM ET… | ✅ WIN | +1.84$ |
| 2026-07-22T02:50 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 21, 10:30PM-10:45PM ET… | ✅ WIN | +0.57$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-22T02:50 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,313.65 | 0.1min |  |
| ✅ ETH | $1,929.22 | 0.1min |  |
| ✅ SOL | $78.22 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,317.10 | consenso |  |
| ETH | $1,929.22 | consenso |  |
| SOL | $78.22 | consenso |  |
| XRP | $1.14 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*