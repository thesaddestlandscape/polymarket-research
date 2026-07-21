# Estado del bot — 2026-07-21 04:51 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **0.78 $** |
| P&L real total | 🔴 **-24.66 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -9.25 $ |
| Fees pagados (real) | 8.68 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3420.10 $ |
| P&L sim compuesto | 🟢 +6335.79 $ (ficción Kelly: +24905% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -79.69 $ |
| Operaciones resueltas | 25980 (15742 WIN / 10238 LOSS) — 60.6% |
| Señales abiertas | 124 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6380 | 60.3% | +0.103 | ➡️ estable | +2143.85$ | 1.03$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3576 | 64.5% | +0.145 | ➡️ estable | +2090.52$ | 1.45$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3558 | 59.5% | +0.095 | ➡️ estable | +1235.16$ | 0.95$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 921 | 67.2% | +0.172 | ➡️ estable | +425.30$ | 1.72$ | ✅ activa |
| UPDOWN_GBM | 2029 | 52.5% | +0.025 | 📈 madura (+0.12) | +155.96$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 203 | 64.0% | +0.139 | ➡️ estable | +104.87$ | 1.39$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4490 | 68.6% | +0.186 | ➡️ estable | +64.61$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 249 | 59.4% | +0.094 | 📉 agota (-0.04) | +37.12$ | 0.94$ | ✅ activa |
| GBM_LATE_5M | 228 | 54.8% | +0.048 | 📉 agota (-0.04) | +24.82$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 110 | 60.0% | +0.098 | 📉 agota (-0.21) | +19.72$ | 0.98$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 541 | 62.8% | +0.128 | 📉 agota (-0.03) | +17.65$ | 1.28$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 95 | 78.9% | +0.284 | 📉 agota (-0.08) | +15.82$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 242 | 52.1% | +0.020 | 📉 agota (-0.13) | +12.71$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1642 | 51.1% | +0.011 | ➡️ estable | +11.14$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 205 | 82.0% | +0.316 | ➡️ estable | +9.51$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 6 | 100.0% | +0.112 | — | +1.04$ | 1.12$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 6 | 66.7% | +0.037 | — | +0.87$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
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
| 2026-07-21T04:50 | UPDOWN_GBM_15M_TARDIO#SOL#15min | Solana Up or Down - July 21, 12:30AM-12:45AM ET… | ✅ WIN | +1.47$ |
| 2026-07-21T04:50 | UPDOWN_GBM_15M_TARDIO#DOGE#15min | Dogecoin Up or Down - July 21, 12:30AM-12:45AM ET… | ✅ WIN | +1.96$ |
| 2026-07-21T04:50 | STREAK_FADE_15M#SOL#15min | Solana Up or Down - July 21, 12:30AM-12:45AM ET… | ✅ WIN | +2.08$ |
| 2026-07-21T04:50 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 21, 12:30AM-12:45AM ET… | ❌ LOSS | -1.13$ |
| 2026-07-21T04:50 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 21, 12:30AM-12:45AM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T04:49 UTC | rechazos 1h: 4 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,474.69 | 0.1min |  |
| ✅ ETH | $1,922.40 | 0.1min |  |
| ✅ SOL | $78.14 | 0.1min |  |
| ✅ XRP | $1.12 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,476.40 | consenso |  |
| ETH | $1,922.40 | consenso |  |
| SOL | $78.06 | consenso |  |
| XRP | $1.12 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:4 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*