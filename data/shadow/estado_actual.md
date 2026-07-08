# Estado del bot — 2026-07-08 16:07 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **25.13 $** |
| P&L real total | 🔴 **-0.31 $** |
| P&L real hoy | +0.39 $ |
| P&L real 7 días | -1.56 $ |
| Fees pagados (real) | 5.10 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +358.78 $ |
| P&L sim compuesto | 🟢 +628.80 $ (ficción Kelly: +2472% s/ operativo) |
| P&L sim hoy (2026-07-08) | 🟢 +123.12 $ |
| Operaciones resueltas | 5561 (2972 WIN / 2589 LOSS) — 53.4% |
| Señales abiertas | 164 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2175 | 61.7% | +0.117 | +706.39$ | 1.17$ | ✅ activa |
| ORDER_FLOW_5M | 1553 | 51.3% | +0.013 | +17.05$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 26 | 73.1% | +0.214 | +7.43$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | +3.47$ | 1.60$ | ✅ activa |
| STREAK_FADE_15M | 66 | 56.1% | +0.059 | +1.56$ | 0.59$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 129 | 34.1% | -0.156 | -0.43$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_TARDIO | 11 | 45.5% | -0.021 | -1.29$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 84 | 47.6% | -0.023 | -3.60$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | -4.68$ | 0.00$ | 🚫 desactivada |
| GBM_LATE_60M | 121 | 34.7% | -0.150 | -11.52$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | -18.89$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 143 | 52.4% | +0.024 | -20.27$ | 0.50$ | ✅ activa |
| UPDOWN_GBM | 1111 | 47.3% | -0.027 | -32.51$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-08T16:07 | RESOLUTION_SNIPER#SOL#sniper | Will the price of Solana be between $70 and $80 on… | ✅ WIN | +0.43$ |
| 2026-07-08T16:07 | WEEKLY_PRICE#SOL | Will the price of Solana be between $70 and $80 on… | ❌ LOSS | -0.51$ |
| 2026-07-08T16:05 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 8, 11:45AM-12:00PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-08T16:02 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 8, 11:45AM-12:00PM ET… | ❌ LOSS | -1.95$ |
| 2026-07-08T16:02 | PRICE_TARGET_GBM#SOL#atexpiry | Will the price of Solana be above $80 on July 8?… | ✅ WIN | +0.71$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-08T16:07 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $61,681.93 | 0.1min |  |
| ✅ ETH | $1,723.56 | 0.1min |  |
| ✅ SOL | $76.86 | 0.1min |  |
| ✅ XRP | $1.08 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $61,690.00 | consenso |  |
| ETH | $1,723.75 | consenso |  |
| SOL | $76.82 | consenso |  |
| XRP | $1.07 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*