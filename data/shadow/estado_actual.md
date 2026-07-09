# Estado del bot — 2026-07-09 16:33 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **28.85 $** |
| P&L real total | 🟢 **+3.41 $** |
| P&L real hoy | -3.82 $ |
| P&L real 7 días | +0.03 $ |
| Fees pagados (real) | 6.48 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +475.16 $ |
| P&L sim compuesto | 🟢 +784.23 $ (ficción Kelly: +3083% s/ operativo) |
| P&L sim hoy (2026-07-09) | 🟢 +138.73 $ |
| Operaciones resueltas | 6506 (3482 WIN / 3024 LOSS) — 53.5% |
| Señales abiertas | 163 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2559 | 61.2% | +0.112 | 📈 madura (+0.03) | +826.37$ | 1.12$ | ✅ activa |
| ORDER_FLOW_5M | 1560 | 51.3% | +0.013 | ➡️ estable | +18.55$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 78 | 62.8% | +0.125 | 📉 agota (-0.12) | +14.04$ | 1.25$ | ✅ activa |
| LATE_WINDOW_5MIN | 32 | 68.8% | +0.176 | 📉 agota (-0.11) | +6.54$ | 1.76$ | ✅ activa |
| STREAK_FADE_15M | 94 | 56.4% | +0.062 | 📈 madura (+0.06) | +4.28$ | 0.62$ | ✅ activa |
| GBM_LATE_60M | 177 | 36.2% | -0.137 | 📈 madura (+0.04) | +3.91$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 7 | 57.1% | +0.019 | — | +0.47$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 132 | 34.1% | -0.157 | 📉 agota (-0.10) | -0.77$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_TARDIO | 113 | 47.8% | -0.022 | 📉 agota (-0.25) | -3.35$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 159 | 55.3% | +0.053 | 📈 madura (+0.14) | -15.64$ | 0.53$ | ✅ activa |
| STREAK_MOM_5M | 276 | 46.4% | -0.036 | 📉 agota (-0.04) | -15.79$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| UPDOWN_GBM | 1177 | 47.8% | -0.022 | ➡️ estable | -20.38$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-09T16:31 | STREAK_MOM_5M#XRP#5min | XRP Up or Down - July 9, 12:20PM-12:25PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-09T16:30 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 9, 12:15PM-12:30PM ET… | ❌ LOSS | -0.71$ |
| 2026-07-09T16:30 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 9, 12:15PM-12:30PM ET… | ❌ LOSS | -0.56$ |
| 2026-07-09T16:30 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 9, 12:15PM-12:30PM ET… | ✅ WIN | +0.32$ |
| 2026-07-09T16:30 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 9, 12:15PM-12:30PM ET… | ❌ LOSS | -0.56$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-09T16:33 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,633.17 | 0.1min |  |
| ✅ ETH | $1,733.64 | 0.1min |  |
| ✅ SOL | $77.51 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,642.20 | consenso |  |
| ETH | $1,733.94 | consenso |  |
| SOL | $77.31 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*