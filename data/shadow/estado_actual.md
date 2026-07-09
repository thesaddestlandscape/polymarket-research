# Estado del bot — 2026-07-09 16:09 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **31.02 $** |
| P&L real total | 🟢 **+5.58 $** |
| P&L real hoy | -1.66 $ |
| P&L real 7 días | +2.19 $ |
| Fees pagados (real) | 6.42 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +482.98 $ |
| P&L sim compuesto | 🟢 +791.28 $ (ficción Kelly: +3110% s/ operativo) |
| P&L sim hoy (2026-07-09) | 🟢 +145.79 $ |
| Operaciones resueltas | 6481 (3473 WIN / 3008 LOSS) — 53.6% |
| Señales abiertas | 168 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2552 | 61.3% | +0.113 | 📈 madura (+0.03) | +828.83$ | 1.13$ | ✅ activa |
| ORDER_FLOW_5M | 1560 | 51.3% | +0.013 | ➡️ estable | +18.55$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 71 | 66.2% | +0.158 | 📉 agota (-0.20) | +16.45$ | 1.57$ | ✅ activa |
| LATE_WINDOW_5MIN | 32 | 68.8% | +0.176 | 📉 agota (-0.11) | +6.54$ | 1.76$ | ✅ activa |
| STREAK_FADE_15M | 94 | 56.4% | +0.062 | 📈 madura (+0.06) | +4.28$ | 0.62$ | ✅ activa |
| GBM_LATE_60M | 177 | 36.2% | -0.137 | 📈 madura (+0.04) | +3.91$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 7 | 57.1% | +0.019 | — | +0.47$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_TARDIO | 106 | 50.0% | +0.000 | 📉 agota (-0.24) | -0.15$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 132 | 34.1% | -0.157 | 📉 agota (-0.10) | -0.77$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 159 | 55.3% | +0.053 | 📈 madura (+0.14) | -15.64$ | 0.53$ | ✅ activa |
| STREAK_MOM_5M | 274 | 46.4% | -0.036 | 📉 agota (-0.05) | -15.80$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| UPDOWN_GBM | 1175 | 47.7% | -0.023 | ➡️ estable | -21.38$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-09T16:07 | STREAK_MOM_5M#XRP#5min | XRP Up or Down - July 9, 12:00PM-12:05PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-09T16:07 | PRICE_TARGET_GBM#SOL#atexpiry | Will the price of Solana be above $80 on July 9?… | ✅ WIN | +0.68$ |
| 2026-07-09T16:07 | WEEKLY_PRICE#SOL | Will the price of Solana be between $80 and $90 on… | ❌ LOSS | -0.51$ |
| 2026-07-09T16:07 | WEEKLY_PRICE#SOL | Will the price of Solana be between $70 and $80 on… | ❌ LOSS | -0.51$ |
| 2026-07-09T16:04 | WEEKLY_PRICE#SOL | Will the price of Solana be between $60 and $70 on… | ✅ WIN | +0.43$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-09T16:08 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,912.04 | 0.1min |  |
| ✅ ETH | $1,741.40 | 0.1min |  |
| ✅ SOL | $77.64 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,912.04 | consenso |  |
| ETH | $1,741.40 | consenso |  |
| SOL | $77.70 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*