# Estado del bot — 2026-07-11 14:00 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **23.86 $** |
| P&L real total | 🔴 **-1.58 $** |
| P&L real hoy | -1.46 $ |
| P&L real 7 días | +15.85 $ |
| Fees pagados (real) | 7.30 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +974.23 $ |
| P&L sim compuesto | 🟢 +1493.57 $ (ficción Kelly: +5871% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +214.16 $ |
| Operaciones resueltas | 9249 (5183 WIN / 4066 LOSS) — 56.0% |
| Señales abiertas | 181 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3246 | 61.4% | +0.114 | ➡️ estable | +1056.35$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 644 | 65.2% | +0.152 | ➡️ estable | +291.77$ | 1.52$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 789 | 58.2% | +0.082 | 📈 madura (+0.04) | +176.32$ | 0.82$ | ✅ activa |
| STREAK_FADE_15M | 131 | 61.8% | +0.117 | 📈 madura (+0.12) | +19.89$ | 1.17$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 48 | 62.5% | +0.120 | 📈 madura (+0.15) | +12.30$ | 1.20$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 278 | 39.2% | -0.107 | 📈 madura (+0.11) | +7.78$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM | 1264 | 48.7% | -0.013 | 📈 madura (+0.03) | +5.58$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 481 | 65.7% | +0.156 | 📉 agota (-0.04) | -33.26$ | 1.56$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T13:56 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 11, 9:50AM-9:55AM ET… | ❌ LOSS | -1.61$ |
| 2026-07-11T13:48 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 11, 9:30AM-9:45AM ET… | ✅ WIN | +0.40$ |
| 2026-07-11T13:48 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 11, 9:30AM-9:45AM ET… | ✅ WIN | +1.92$ |
| 2026-07-11T13:48 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 11, 9:30AM-9:45AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-11T13:48 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 11, 9:30AM-9:45AM ET… | ✅ WIN | +1.92$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T13:59 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,205.94 | 0.1min |  |
| ✅ ETH | $1,801.57 | 0.1min |  |
| ✅ SOL | $78.16 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,213.80 | consenso |  |
| ETH | $1,801.57 | consenso |  |
| SOL | $78.12 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*