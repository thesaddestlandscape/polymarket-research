# Estado del bot — 2026-07-11 20:22 UTC

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
| P&L fiel (stake fijo 1$) | +985.41 $ |
| P&L sim compuesto | 🟢 +1536.66 $ (ficción Kelly: +6040% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +257.25 $ |
| Operaciones resueltas | 9737 (5462 WIN / 4275 LOSS) — 56.1% |
| Señales abiertas | 172 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3341 | 61.0% | +0.110 | ➡️ estable | +1052.35$ | 1.10$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 724 | 64.2% | +0.142 | 📉 agota (-0.04) | +307.23$ | 1.42$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 884 | 57.5% | +0.074 | ➡️ estable | +178.13$ | 0.74$ | ✅ activa |
| STREAK_FADE_15M | 132 | 62.1% | +0.119 | 📈 madura (+0.12) | +20.55$ | 1.19$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 53 | 66.0% | +0.155 | 📈 madura (+0.15) | +19.18$ | 1.54$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 294 | 39.1% | -0.108 | 📈 madura (+0.05) | +11.86$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM | 1284 | 48.9% | -0.011 | 📈 madura (+0.03) | +11.59$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| STREAK_FADE_5M | 35 | 54.3% | +0.041 | 📈 madura (+0.23) | +1.14$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 136 | 34.6% | -0.152 | 📉 agota (-0.13) | -0.14$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 192 | 57.8% | +0.077 | 📈 madura (+0.23) | -13.59$ | 0.77$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 603 | 66.2% | +0.161 | 📉 agota (-0.05) | -22.32$ | 1.61$ | ✅ activa |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T20:18 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 11, 4:00PM-4:15PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-11T20:18 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 11, 4:00PM-4:15PM ET… | ❌ LOSS | -1.80$ |
| 2026-07-11T20:18 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 11, 4:00PM-4:15PM ET… | ❌ LOSS | -0.62$ |
| 2026-07-11T20:18 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 11, 4:00PM-4:15PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-11T20:18 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 11, 4:00PM-4:15PM ET… | ❌ LOSS | -1.55$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T20:21 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,283.53 | 0.1min |  |
| ✅ ETH | $1,823.68 | 0.1min |  |
| ✅ SOL | $78.18 | 0.1min |  |
| ✅ XRP | $1.12 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,283.53 | consenso |  |
| ETH | $1,823.68 | consenso |  |
| SOL | $78.11 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*