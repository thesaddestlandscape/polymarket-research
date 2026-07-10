# Estado del bot — 2026-07-10 04:14 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **31.45 $** |
| P&L real total | 🟢 **+6.01 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | +8.26 $ |
| Fees pagados (real) | 6.95 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +638.00 $ |
| P&L sim compuesto | 🟢 +974.83 $ (ficción Kelly: +3832% s/ operativo) |
| P&L sim hoy (2026-07-10) | 🟢 +62.89 $ |
| Operaciones resueltas | 7128 (3861 WIN / 3267 LOSS) — 54.2% |
| Señales abiertas | 165 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2738 | 61.4% | +0.114 | ➡️ estable | +906.20$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 227 | 65.2% | +0.151 | ➡️ estable | +69.54$ | 1.51$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 286 | 54.2% | +0.042 | 📈 madura (+0.09) | +27.34$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1567 | 51.3% | +0.013 | ➡️ estable | +17.22$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 111 | 58.6% | +0.084 | 📈 madura (+0.04) | +10.35$ | 0.84$ | ✅ activa |
| LATE_WINDOW_5MIN | 34 | 70.6% | +0.194 | 📉 agota (-0.11) | +9.39$ | 1.94$ | ✅ activa |
| GBM_LATE_60M | 208 | 37.5% | -0.124 | 📈 madura (+0.08) | +8.10$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| LEADLAG_BTC_XRP_15M | 14 | 50.0% | +0.000 | — | -0.16$ | 0.50$ | ✅ activa |
| UPDOWN_GBM | 1204 | 48.5% | -0.015 | ➡️ estable | -0.60$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 132 | 34.1% | -0.157 | 📉 agota (-0.10) | -0.77$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 159 | 55.3% | +0.053 | 📈 madura (+0.14) | -15.64$ | 0.53$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-10T04:08 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 9, 11:45PM-12:00AM ET… | ✅ WIN | +0.28$ |
| 2026-07-10T04:08 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 9, 11:45PM-12:00AM ET… | ✅ WIN | +1.27$ |
| 2026-07-10T04:08 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 9, 11:45PM-12:00AM ET… | ✅ WIN | +0.72$ |
| 2026-07-10T04:06 | ORDER_FLOW_5M#BTC#5min | Bitcoin Up or Down - July 9, 11:55PM-12:00AM ET… | ❌ LOSS | -1.41$ |
| 2026-07-10T04:06 | GBM_LATE_60M#BTC#60min | Bitcoin Up or Down - July 9, 11PM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-10T04:14 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,929.75 | 0.0min |  |
| ✅ ETH | $1,777.96 | 0.0min |  |
| ✅ SOL | $79.06 | 0.0min |  |
| ✅ XRP | $1.11 | 0.0min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,930.10 | consenso |  |
| ETH | $1,777.96 | consenso |  |
| SOL | $79.00 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*