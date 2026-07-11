# Estado del bot — 2026-07-11 20:04 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **22.40 $** |
| P&L real total | 🔴 **-3.04 $** |
| P&L real hoy | -2.90 $ |
| P&L real 7 días | +14.42 $ |
| Fees pagados (real) | 7.52 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +983.57 $ |
| P&L sim compuesto | 🟢 +1532.87 $ (ficción Kelly: +6025% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +253.47 $ |
| Operaciones resueltas | 9712 (5447 WIN / 4265 LOSS) — 56.1% |
| Señales abiertas | 167 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3337 | 61.0% | +0.110 | ➡️ estable | +1054.00$ | 1.10$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 721 | 64.2% | +0.142 | 📉 agota (-0.04) | +304.64$ | 1.42$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 880 | 57.5% | +0.075 | ➡️ estable | +179.41$ | 0.75$ | ✅ activa |
| STREAK_FADE_15M | 132 | 62.1% | +0.119 | 📈 madura (+0.12) | +20.55$ | 1.19$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 53 | 66.0% | +0.155 | 📈 madura (+0.15) | +19.18$ | 1.54$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 293 | 39.2% | -0.107 | 📈 madura (+0.06) | +12.85$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 1282 | 48.8% | -0.012 | 📈 madura (+0.03) | +8.72$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| STREAK_FADE_5M | 31 | 54.8% | +0.045 | 📈 madura (+0.25) | +1.18$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 136 | 34.6% | -0.152 | 📉 agota (-0.13) | -0.14$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 192 | 57.8% | +0.077 | 📈 madura (+0.23) | -13.59$ | 0.77$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 596 | 66.1% | +0.161 | 📉 agota (-0.05) | -24.61$ | 1.60$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T20:03 | GBM_LATE_60M#SOL#60min | Solana Up or Down - July 11, 3PM ET… | ✅ WIN | +2.52$ |
| 2026-07-11T20:03 | FAVORITO_CONFIRMADO#SOL#60min | Solana Up or Down - July 11, 3PM ET… | ❌ LOSS | -1.15$ |
| 2026-07-11T20:03 | FAVORITO_CONFIRMADO#BTC#240min | Bitcoin Up or Down - July 11, 12:00PM-4:00PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-11T20:02 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 11, 3:45PM-4:00PM ET… | ✅ WIN | +1.96$ |
| 2026-07-11T20:02 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 11, 3:45PM-4:00PM ET… | ✅ WIN | +1.80$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T20:03 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,246.00 | 0.1min |  |
| ✅ ETH | $1,823.31 | 0.1min |  |
| ✅ SOL | $78.14 | 0.1min |  |
| ✅ XRP | $1.12 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,246.00 | consenso |  |
| ETH | $1,823.31 | consenso |  |
| SOL | $78.08 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*