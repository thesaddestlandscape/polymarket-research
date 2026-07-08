# Estado del bot — 2026-07-08 08:37 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **27.39 $** |
| P&L real total | 🟢 **+1.95 $** |
| P&L real hoy | -0.13 $ |
| P&L real 7 días | -2.09 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +332.79 $ |
| P&L sim compuesto | 🟢 +589.88 $ (ficción Kelly: +2319% s/ operativo) |
| P&L sim hoy (2026-07-08) | 🟢 +84.20 $ |
| Operaciones resueltas | 5298 (2823 WIN / 2475 LOSS) — 53.3% |
| Señales abiertas | 149 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2057 | 61.5% | +0.115 | +660.85$ | 1.15$ | ✅ activa |
| ORDER_FLOW_5M | 1553 | 51.3% | +0.013 | +17.05$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 25 | 76.0% | +0.241 | +8.74$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 7 | 100.0% | +0.136 | +3.04$ | 1.36$ | ⏳ acumulando |
| STREAK_FADE_15M | 61 | 55.7% | +0.056 | +1.11$ | 0.56$ | ✅ activa |
| PRICE_TARGET_GBM | 124 | 34.7% | -0.151 | +0.90$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 21 | 42.9% | -0.065 | -1.73$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | -4.68$ | 0.00$ | 🚫 desactivada |
| GBM_LATE_60M | 103 | 33.0% | -0.167 | -12.61$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | -18.89$ | 0.00$ | 🚫 desactivada |
| UPDOWN_GBM | 1092 | 47.7% | -0.023 | -23.33$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 127 | 47.2% | -0.027 | -26.77$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-08T08:36 | STREAK_MOM_5M#SOL#5min | Solana Up or Down - July 8, 4:30AM-4:35AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-08T08:36 | STREAK_MOM_5M#XRP#5min | XRP Up or Down - July 8, 4:30AM-4:35AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-08T08:35 | STREAK_MOM_5M#SOL#5min | Solana Up or Down - July 8, 4:25AM-4:30AM ET… | ✅ WIN | +0.49$ |
| 2026-07-08T08:31 | STREAK_MOM_5M#XRP#5min | XRP Up or Down - July 8, 4:25AM-4:30AM ET… | ✅ WIN | +0.50$ |
| 2026-07-08T08:31 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 8, 4:20AM-4:25AM ET… | ✅ WIN | +1.06$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-08T08:36 UTC | rechazos 1h: 5 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,015.69 | 0.1min |  |
| ✅ ETH | $1,731.89 | 0.1min |  |
| ✅ SOL | $77.10 | 0.1min |  |
| ✅ XRP | $1.08 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,025.80 | consenso |  |
| ETH | $1,732.54 | consenso |  |
| SOL | $77.19 | consenso |  |
| XRP | $1.08 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:5 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*