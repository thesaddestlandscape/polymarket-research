# Estado del bot — 2026-07-09 20:00 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **32.09 $** |
| P&L real total | 🟢 **+6.65 $** |
| P&L real hoy | -0.59 $ |
| P&L real 7 días | +3.26 $ |
| Fees pagados (real) | 6.82 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +515.64 $ |
| P&L sim compuesto | 🟢 +830.85 $ (ficción Kelly: +3266% s/ operativo) |
| P&L sim hoy (2026-07-09) | 🟢 +185.35 $ |
| Operaciones resueltas | 6693 (3591 WIN / 3102 LOSS) — 53.7% |
| Señales abiertas | 167 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2611 | 61.3% | +0.113 | 📈 madura (+0.03) | +846.83$ | 1.13$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 118 | 64.4% | +0.142 | 📉 agota (-0.03) | +24.75$ | 1.42$ | ✅ activa |
| ORDER_FLOW_5M | 1560 | 51.3% | +0.013 | ➡️ estable | +18.55$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 103 | 58.3% | +0.081 | ➡️ estable | +9.08$ | 0.81$ | ✅ activa |
| LATE_WINDOW_5MIN | 33 | 69.7% | +0.186 | 📉 agota (-0.09) | +7.82$ | 1.86$ | ✅ activa |
| GBM_LATE_60M | 185 | 36.8% | -0.131 | 📈 madura (+0.04) | +3.56$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| LEADLAG_BTC_XRP_15M | 8 | 50.0% | +0.000 | — | -0.09$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 132 | 34.1% | -0.157 | 📉 agota (-0.10) | -0.77$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_TARDIO | 162 | 48.1% | -0.018 | 📉 agota (-0.07) | -1.64$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| UPDOWN_GBM | 1185 | 48.1% | -0.019 | ➡️ estable | -8.07$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 159 | 55.3% | +0.053 | 📈 madura (+0.14) | -15.64$ | 0.53$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 295 | 45.4% | -0.045 | 📉 agota (-0.04) | -19.53$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-09T20:00 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 9, 3:45PM-4:00PM ET… | ❌ LOSS | -1.52$ |
| 2026-07-09T20:00 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 9, 3:45PM-4:00PM ET… | ❌ LOSS | -0.56$ |
| 2026-07-09T20:00 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 9, 3:45PM-4:00PM ET… | ❌ LOSS | -1.02$ |
| 2026-07-09T19:49 | UPDOWN_GBM#BTC#15min | Bitcoin Up or Down - July 9, 3:30PM-3:45PM ET… | ✅ WIN | +1.66$ |
| 2026-07-09T19:49 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 9, 3:30PM-3:45PM ET… | ✅ WIN | +0.55$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-09T20:00 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,207.68 | 0.2min |  |
| ✅ ETH | $1,747.38 | 0.2min |  |
| ✅ SOL | $78.17 | 0.2min |  |
| ✅ XRP | $1.10 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,215.10 | consenso |  |
| ETH | $1,747.48 | consenso |  |
| SOL | $78.09 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*