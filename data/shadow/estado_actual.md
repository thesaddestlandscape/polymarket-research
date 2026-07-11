# Estado del bot — 2026-07-11 05:54 UTC

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
| P&L fiel (stake fijo 1$) | +909.73 $ |
| P&L sim compuesto | 🟢 +1386.50 $ (ficción Kelly: +5450% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +107.09 $ |
| Operaciones resueltas | 8727 (4872 WIN / 3855 LOSS) — 55.8% |
| Señales abiertas | 166 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3130 | 61.5% | +0.115 | ➡️ estable | +1020.65$ | 1.15$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 544 | 66.4% | +0.163 | ➡️ estable | +250.76$ | 1.63$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 673 | 57.4% | +0.073 | 📈 madura (+0.04) | +133.47$ | 0.73$ | ✅ activa |
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
| FAVORITO_CONFIRMADO | 340 | 67.4% | +0.173 | ➡️ estable | -16.34$ | 1.72$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T05:52 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 11, 1:45AM-1:50AM ET… | ✅ WIN | +0.48$ |
| 2026-07-11T05:52 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 11, 1:30AM-1:45AM ET… | ✅ WIN | +1.38$ |
| 2026-07-11T05:52 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 11, 1:30AM-1:45AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-11T05:52 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 11, 1:30AM-1:45AM ET… | ❌ LOSS | -0.99$ |
| 2026-07-11T05:52 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 11, 1:30AM-1:45AM ET… | ❌ LOSS | -0.94$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T05:54 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,100.47 | 0.1min |  |
| ✅ ETH | $1,796.55 | 0.1min |  |
| ✅ SOL | $77.85 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,106.60 | consenso |  |
| ETH | $1,796.55 | consenso |  |
| SOL | $77.76 | consenso |  |
| XRP | $1.10 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*