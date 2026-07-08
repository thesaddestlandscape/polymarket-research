# Estado del bot — 2026-07-08 12:09 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **26.30 $** |
| P&L real total | 🟢 **+0.86 $** |
| P&L real hoy | -1.22 $ |
| P&L real 7 días | -3.18 $ |
| Fees pagados (real) | 4.77 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +349.41 $ |
| P&L sim compuesto | 🟢 +607.80 $ (ficción Kelly: +2389% s/ operativo) |
| P&L sim hoy (2026-07-08) | 🟢 +102.12 $ |
| Operaciones resueltas | 5401 (2883 WIN / 2518 LOSS) — 53.4% |
| Señales abiertas | 149 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2112 | 61.6% | +0.116 | +680.15$ | 1.16$ | ✅ activa |
| ORDER_FLOW_5M | 1553 | 51.3% | +0.013 | +17.05$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 25 | 76.0% | +0.241 | +8.74$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 7 | 100.0% | +0.136 | +3.04$ | 1.36$ | ⏳ acumulando |
| STREAK_FADE_15M | 61 | 55.7% | +0.056 | +1.11$ | 0.56$ | ✅ activa |
| PRICE_TARGET_GBM | 124 | 34.7% | -0.151 | +0.90$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 54 | 51.9% | +0.018 | +0.14$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | -4.68$ | 0.00$ | 🚫 desactivada |
| GBM_LATE_60M | 111 | 34.2% | -0.155 | -9.97$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | -18.89$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 127 | 47.2% | -0.027 | -26.77$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM | 1099 | 47.5% | -0.025 | -29.22$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-08T12:07 | UPDOWN_GBM#BTC#15min | Bitcoin Up or Down - July 8, 7:45AM-8:00AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-08T12:07 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 8, 7:45AM-8:00AM ET… | ❌ LOSS | -0.71$ |
| 2026-07-08T12:05 | STREAK_MOM_5M#SOL#5min | Solana Up or Down - July 8, 7:55AM-8:00AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-08T12:05 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 8, 7:45AM-8:00AM ET… | ✅ WIN | +1.92$ |
| 2026-07-08T12:03 | STREAK_MOM_5M#ETH#5min | Ethereum Up or Down - July 8, 7:55AM-8:00AM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-08T12:09 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,271.00 | 0.0min |  |
| ✅ ETH | $1,746.04 | 0.0min |  |
| ✅ SOL | $77.61 | 0.0min |  |
| ✅ XRP | $1.09 | 0.0min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,273.60 | consenso |  |
| ETH | $1,746.49 | consenso |  |
| SOL | $77.44 | consenso |  |
| XRP | $1.09 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*