# Estado del bot — 2026-07-10 21:50 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **24.92 $** |
| P&L real total | 🔴 **-0.52 $** |
| P&L real hoy | -6.53 $ |
| P&L real 7 días | +1.73 $ |
| Fees pagados (real) | 7.19 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +805.62 $ |
| P&L sim compuesto | 🟢 +1240.55 $ (ficción Kelly: +4876% s/ operativo) |
| P&L sim hoy (2026-07-10) | 🟢 +328.62 $ |
| Operaciones resueltas | 8191 (4536 WIN / 3655 LOSS) — 55.4% |
| Señales abiertas | 186 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3009 | 61.4% | +0.114 | ➡️ estable | +966.49$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 446 | 67.0% | +0.170 | 📈 madura (+0.04) | +196.52$ | 1.70$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 554 | 56.7% | +0.067 | 📈 madura (+0.06) | +93.43$ | 0.67$ | ✅ activa |
| ORDER_FLOW_5M | 1570 | 51.3% | +0.013 | ➡️ estable | +17.57$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 120 | 61.7% | +0.115 | 📈 madura (+0.13) | +17.48$ | 1.15$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 241 | 38.6% | -0.113 | 📈 madura (+0.09) | +9.37$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 29 | 62.1% | +0.113 | — | +3.69$ | 1.13$ | ✅ activa |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| FAVORITO_CONFIRMADO | 191 | 69.1% | +0.189 | 📉 agota (-0.15) | +0.06$ | 1.89$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM | 1239 | 48.5% | -0.015 | ➡️ estable | -4.39$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-10T21:49 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 10, 5:30PM-5:45PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-10T21:49 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 10, 5:30PM-5:45PM ET… | ❌ LOSS | -0.58$ |
| 2026-07-10T21:49 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 10, 5:30PM-5:45PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-10T21:49 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 10, 5:30PM-5:45PM ET… | ❌ LOSS | -1.67$ |
| 2026-07-10T21:49 | UPDOWN_GBM#BTC#15min | Bitcoin Up or Down - July 10, 5:30PM-5:45PM ET… | ✅ WIN | +0.85$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-10T21:49 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,960.57 | 0.1min |  |
| ✅ ETH | $1,793.47 | 0.1min |  |
| ✅ SOL | $77.93 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,967.70 | consenso |  |
| ETH | $1,793.47 | consenso |  |
| SOL | $77.91 | consenso |  |
| XRP | $1.10 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*