# Estado del bot — 2026-07-11 05:18 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **25.30 $** |
| P&L real total | 🔴 **-0.14 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | +17.32 $ |
| Fees pagados (real) | 7.27 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +905.86 $ |
| P&L sim compuesto | 🟢 +1379.33 $ (ficción Kelly: +5422% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +99.93 $ |
| Operaciones resueltas | 8697 (4853 WIN / 3844 LOSS) — 55.8% |
| Señales abiertas | 153 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3122 | 61.4% | +0.114 | ➡️ estable | +1014.18$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 537 | 66.7% | +0.166 | ➡️ estable | +252.35$ | 1.66$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 665 | 57.3% | +0.073 | 📈 madura (+0.04) | +130.28$ | 0.73$ | ✅ activa |
| STREAK_FADE_15M | 125 | 61.6% | +0.114 | 📈 madura (+0.10) | +18.44$ | 1.14$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 40 | 67.5% | +0.167 | 📈 madura (+0.32) | +12.54$ | 1.67$ | ✅ activa |
| GBM_LATE_60M | 259 | 39.0% | -0.109 | 📈 madura (+0.10) | +10.94$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM | 1250 | 48.6% | -0.014 | ➡️ estable | -1.83$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 333 | 67.3% | +0.172 | ➡️ estable | -15.43$ | 1.72$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T05:18 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 11, 1:00AM-1:15AM ET… | ✅ WIN | +0.99$ |
| 2026-07-11T05:18 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 11, 1:00AM-1:15AM ET… | ✅ WIN | +4.98$ |
| 2026-07-11T05:18 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 11, 1:00AM-1:15AM ET… | ✅ WIN | +1.37$ |
| 2026-07-11T05:18 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 11, 1:00AM-1:15AM ET… | ✅ WIN | +2.24$ |
| 2026-07-11T05:18 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 11, 1:00AM-1:15AM ET… | ✅ WIN | +1.08$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T05:17 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,093.92 | 0.1min |  |
| ✅ ETH | $1,796.15 | 0.1min |  |
| ✅ SOL | $77.76 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,109.10 | consenso |  |
| ETH | $1,796.15 | consenso |  |
| SOL | $77.68 | consenso |  |
| XRP | $1.10 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*