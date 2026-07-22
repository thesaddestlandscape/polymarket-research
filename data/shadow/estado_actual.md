# Estado del bot — 2026-07-22 00:07 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **23.79 $** |
| P&L real total | 🔴 **-27.43 $** |
| P&L real hoy | +1.28 $ |
| P&L real 7 días | -8.31 $ |
| Fees pagados (real) | 9.05 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3331.28 $ |
| P&L sim compuesto | 🟢 +6352.00 $ (ficción Kelly: +24969% s/ operativo) |
| P&L sim hoy (2026-07-22) | 🔴 -11.51 $ |
| Operaciones resueltas | 27795 (16697 WIN / 11098 LOSS) — 60.1% |
| Señales abiertas | 143 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6669 | 59.8% | +0.098 | ➡️ estable | +2129.92$ | 0.98$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3865 | 63.3% | +0.133 | 📉 agota (-0.04) | +2054.22$ | 1.33$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3834 | 58.6% | +0.086 | ➡️ estable | +1238.37$ | 0.86$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1076 | 66.6% | +0.166 | ➡️ estable | +489.24$ | 1.66$ | ✅ activa |
| UPDOWN_GBM | 2110 | 52.7% | +0.027 | 📈 madura (+0.11) | +176.71$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 220 | 61.4% | +0.113 | 📉 agota (-0.06) | +104.60$ | 1.13$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4802 | 68.5% | +0.185 | ➡️ estable | +68.20$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| STREAK_FADE_15M | 259 | 57.9% | +0.079 | 📉 agota (-0.08) | +27.80$ | 0.79$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 112 | 80.4% | +0.298 | 📈 madura (+0.03) | +24.03$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 660 | 62.3% | +0.122 | 📉 agota (-0.06) | +18.88$ | 1.22$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 237 | 81.9% | +0.316 | ➡️ estable | +12.75$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 263 | 48.7% | -0.013 | 📉 agota (-0.14) | +12.71$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 254 | 51.2% | +0.012 | 📉 agota (-0.16) | +10.81$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 8 | 50.0% | +0.000 | — | -0.26$ | 0.50$ | ✅ activa |
| BALLENAS_TARDIAS | 11 | 72.7% | +0.106 | — | -1.83$ | 1.06$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| LATE_WINDOW_5MIN | 256 | 45.7% | -0.043 | 📉 agota (-0.25) | -3.39$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-22T00:06 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 21, 7:55PM-8:00PM ET… | ✅ WIN | +0.58$ |
| 2026-07-22T00:06 | UPDOWN_GBM_15M_TARDIO#DOGE#15min | Dogecoin Up or Down - July 21, 7:45PM-8:00PM ET… | ✅ WIN | +1.77$ |
| 2026-07-22T00:06 | FAVORITO_CONFIRMADO#SOL#60min | Solana Up or Down - July 21, 7PM ET… | ❌ LOSS | -1.76$ |
| 2026-07-22T00:06 | FAVORITO_CONFIRMADO#SOL#240min | Solana Up or Down - July 21, 4:00PM-8:00PM ET… | ✅ WIN | +1.11$ |
| 2026-07-22T00:06 | FAVORITO_CONFIRMADO#ETH#240min | Ethereum Up or Down - July 21, 4:00PM-8:00PM ET… | ❌ LOSS | -1.40$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-22T00:06 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,510.10 | 0.1min |  |
| ✅ ETH | $1,928.62 | 0.1min |  |
| ✅ SOL | $78.24 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,510.20 | consenso |  |
| ETH | $1,928.62 | consenso |  |
| SOL | $78.09 | consenso |  |
| XRP | $1.14 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*