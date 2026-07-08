# Estado del bot — 2026-07-08 09:29 UTC

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
| P&L fiel (stake fijo 1$) | +335.22 $ |
| P&L sim compuesto | 🟢 +591.70 $ (ficción Kelly: +2326% s/ operativo) |
| P&L sim hoy (2026-07-08) | 🟢 +86.02 $ |
| Operaciones resueltas | 5315 (2833 WIN / 2482 LOSS) — 53.3% |
| Señales abiertas | 150 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2069 | 61.6% | +0.116 | +664.74$ | 1.16$ | ✅ activa |
| ORDER_FLOW_5M | 1553 | 51.3% | +0.013 | +17.05$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 25 | 76.0% | +0.241 | +8.74$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 7 | 100.0% | +0.136 | +3.04$ | 1.36$ | ⏳ acumulando |
| STREAK_FADE_15M | 61 | 55.7% | +0.056 | +1.11$ | 0.56$ | ✅ activa |
| PRICE_TARGET_GBM | 124 | 34.7% | -0.151 | +0.90$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 24 | 45.8% | -0.038 | -1.24$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | -4.68$ | 0.00$ | 🚫 desactivada |
| GBM_LATE_60M | 103 | 33.0% | -0.167 | -12.61$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | -18.89$ | 0.00$ | 🚫 desactivada |
| UPDOWN_GBM | 1094 | 47.6% | -0.024 | -25.89$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 127 | 47.2% | -0.027 | -26.77$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-08T09:28 | STREAK_MOM_5M#ETH#5min | Ethereum Up or Down - July 8, 5:20AM-5:25AM ET… | ✅ WIN | +0.50$ |
| 2026-07-08T09:26 | STREAK_MOM_5M#SOL#5min | Solana Up or Down - July 8, 5:20AM-5:25AM ET… | ✅ WIN | +0.50$ |
| 2026-07-08T09:20 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 8, 5:00AM-5:15AM ET… | ❌ LOSS | -1.92$ |
| 2026-07-08T09:16 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 8, 5:00AM-5:15AM ET… | ✅ WIN | +1.74$ |
| 2026-07-08T09:16 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 8, 5:00AM-5:15AM ET… | ✅ WIN | +0.86$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-08T09:28 UTC | rechazos 1h: 3 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $61,768.39 | 0.0min |  |
| ✅ ETH | $1,730.40 | 0.0min |  |
| ✅ SOL | $77.18 | 0.0min |  |
| ✅ XRP | $1.08 | 0.0min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $61,778.50 | consenso |  |
| ETH | $1,731.07 | consenso |  |
| SOL | $77.04 | consenso |  |
| XRP | $1.08 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:3 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*