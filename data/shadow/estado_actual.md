# Estado del bot — 2026-07-10 06:46 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **27.10 $** |
| P&L real total | 🟢 **+1.66 $** |
| P&L real hoy | -4.36 $ |
| P&L real 7 días | +3.91 $ |
| Fees pagados (real) | 7.11 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +679.34 $ |
| P&L sim compuesto | 🟢 +1034.77 $ (ficción Kelly: +4067% s/ operativo) |
| P&L sim hoy (2026-07-10) | 🟢 +122.83 $ |
| Operaciones resueltas | 7258 (3950 WIN / 3308 LOSS) — 54.4% |
| Señales abiertas | 160 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2779 | 61.5% | +0.115 | ➡️ estable | +923.35$ | 1.15$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 260 | 66.9% | +0.168 | 📈 madura (+0.05) | +98.25$ | 1.68$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 327 | 55.7% | +0.056 | 📈 madura (+0.14) | +41.26$ | 0.56$ | ✅ activa |
| ORDER_FLOW_5M | 1570 | 51.3% | +0.013 | ➡️ estable | +17.57$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 111 | 58.6% | +0.084 | 📈 madura (+0.04) | +10.35$ | 0.84$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 214 | 37.9% | -0.120 | 📈 madura (+0.10) | +7.63$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM | 1206 | 48.5% | -0.015 | ➡️ estable | -0.67$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 17 | 47.1% | -0.022 | — | -0.73$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 132 | 34.1% | -0.157 | 📉 agota (-0.10) | -0.77$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 159 | 55.3% | +0.053 | 📈 madura (+0.14) | -15.64$ | 0.53$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-10T06:45 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 10, 2:30AM-2:45AM ET… | ❌ LOSS | -1.88$ |
| 2026-07-10T06:45 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 10, 2:30AM-2:45AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-10T06:45 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 10, 2:30AM-2:45AM ET… | ❌ LOSS | -1.82$ |
| 2026-07-10T06:45 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 10, 2:30AM-2:45AM ET… | ❌ LOSS | -1.52$ |
| 2026-07-10T06:45 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 10, 2:30AM-2:45AM ET… | ❌ LOSS | -1.84$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-10T06:45 UTC | rechazos 1h: 5 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,858.86 | 0.0min |  |
| ✅ ETH | $1,771.69 | 0.0min |  |
| ✅ SOL | $79.02 | 0.0min |  |
| ✅ XRP | $1.11 | 0.0min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,863.60 | consenso |  |
| ETH | $1,771.69 | consenso |  |
| SOL | $78.93 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:5 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*