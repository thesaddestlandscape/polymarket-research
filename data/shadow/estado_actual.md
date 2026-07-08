# Estado del bot — 2026-07-08 08:54 UTC

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
| P&L fiel (stake fijo 1$) | +332.74 $ |
| P&L sim compuesto | 🟢 +590.67 $ (ficción Kelly: +2322% s/ operativo) |
| P&L sim hoy (2026-07-08) | 🟢 +84.99 $ |
| Operaciones resueltas | 5304 (2826 WIN / 2478 LOSS) — 53.3% |
| Señales abiertas | 149 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2061 | 61.6% | +0.116 | +664.19$ | 1.16$ | ✅ activa |
| ORDER_FLOW_5M | 1553 | 51.3% | +0.013 | +17.05$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 25 | 76.0% | +0.241 | +8.74$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 7 | 100.0% | +0.136 | +3.04$ | 1.36$ | ⏳ acumulando |
| STREAK_FADE_15M | 61 | 55.7% | +0.056 | +1.11$ | 0.56$ | ✅ activa |
| PRICE_TARGET_GBM | 124 | 34.7% | -0.151 | +0.90$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 22 | 40.9% | -0.083 | -2.24$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | -4.68$ | 0.00$ | 🚫 desactivada |
| GBM_LATE_60M | 103 | 33.0% | -0.167 | -12.61$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | -18.89$ | 0.00$ | 🚫 desactivada |
| UPDOWN_GBM | 1093 | 47.7% | -0.023 | -25.37$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 127 | 47.2% | -0.027 | -26.77$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-08T08:50 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 8, 4:30AM-4:45AM ET… | ❌ LOSS | -0.70$ |
| 2026-07-08T08:50 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 8, 4:30AM-4:45AM ET… | ✅ WIN | +1.87$ |
| 2026-07-08T08:50 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 8, 4:30AM-4:45AM ET… | ✅ WIN | +1.58$ |
| 2026-07-08T08:50 | UPDOWN_GBM#XRP#15min | XRP Up or Down - July 8, 4:30AM-4:45AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-08T08:47 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 8, 4:30AM-4:45AM ET… | ✅ WIN | +0.59$ |

## Calidad de datos

⚠️ **DEGRADED** — última verificación 2026-07-08T08:54 UTC | rechazos 1h: 8 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,098.40 | 0.0min |  |
| ✅ ETH | $1,737.57 | 0.0min |  |
| ✅ SOL | $77.49 | 0.0min |  |
| ✅ XRP | $1.08 | 0.0min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,113.40 | consenso |  |
| ETH | $1,737.57 | consenso |  |
| SOL | $77.39 | consenso |  |
| XRP | $1.08 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:8 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*