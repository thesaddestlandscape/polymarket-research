# Estado del bot — 2026-07-08 10:08 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **26.30 $** |
| P&L real total | 🟢 **+0.86 $** |
| P&L real hoy | -1.22 $ |
| P&L real 7 días | -3.18 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +334.82 $ |
| P&L sim compuesto | 🟢 +593.86 $ (ficción Kelly: +2334% s/ operativo) |
| P&L sim hoy (2026-07-08) | 🟢 +88.18 $ |
| Operaciones resueltas | 5334 (2842 WIN / 2492 LOSS) — 53.3% |
| Señales abiertas | 153 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2081 | 61.5% | +0.115 | +666.64$ | 1.15$ | ✅ activa |
| ORDER_FLOW_5M | 1553 | 51.3% | +0.013 | +17.05$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 25 | 76.0% | +0.241 | +8.74$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 7 | 100.0% | +0.136 | +3.04$ | 1.36$ | ⏳ acumulando |
| STREAK_FADE_15M | 61 | 55.7% | +0.056 | +1.11$ | 0.56$ | ✅ activa |
| PRICE_TARGET_GBM | 124 | 34.7% | -0.151 | +0.90$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 29 | 44.8% | -0.048 | -1.78$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | -4.68$ | 0.00$ | 🚫 desactivada |
| GBM_LATE_60M | 105 | 33.3% | -0.164 | -11.81$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | -18.89$ | 0.00$ | 🚫 desactivada |
| UPDOWN_GBM | 1094 | 47.6% | -0.024 | -25.89$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 127 | 47.2% | -0.027 | -26.77$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-08T10:07 | STREAK_MOM_5M#ETH#5min | Ethereum Up or Down - July 8, 6:00AM-6:05AM ET… | ✅ WIN | +0.50$ |
| 2026-07-08T10:07 | STREAK_MOM_5M#XRP#5min | XRP Up or Down - July 8, 6:00AM-6:05AM ET… | ✅ WIN | +0.49$ |
| 2026-07-08T10:07 | GBM_LATE_60M#BTC#60min | Bitcoin Up or Down - July 8, 5AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-08T10:05 | GBM_LATE_60M#SOL#60min | Solana Up or Down - July 8, 5AM ET… | ✅ WIN | +1.31$ |
| 2026-07-08T10:01 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 8, 5:45AM-6:00AM ET… | ❌ LOSS | -1.49$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-08T10:08 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $61,868.89 | 0.0min |  |
| ✅ ETH | $1,732.94 | 0.0min |  |
| ✅ SOL | $77.07 | 0.0min |  |
| ✅ XRP | $1.08 | 0.0min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $61,870.00 | consenso |  |
| ETH | $1,732.94 | consenso |  |
| SOL | $77.01 | consenso |  |
| XRP | $1.08 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*