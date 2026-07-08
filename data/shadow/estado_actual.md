# Estado del bot — 2026-07-08 09:46 UTC

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
| P&L fiel (stake fijo 1$) | +331.08 $ |
| P&L sim compuesto | 🟢 +590.24 $ (ficción Kelly: +2320% s/ operativo) |
| P&L sim hoy (2026-07-08) | 🟢 +84.56 $ |
| Operaciones resueltas | 5323 (2835 WIN / 2488 LOSS) — 53.3% |
| Señales abiertas | 150 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2074 | 61.5% | +0.115 | +664.81$ | 1.15$ | ✅ activa |
| ORDER_FLOW_5M | 1553 | 51.3% | +0.013 | +17.05$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 25 | 76.0% | +0.241 | +8.74$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 7 | 100.0% | +0.136 | +3.04$ | 1.36$ | ⏳ acumulando |
| STREAK_FADE_15M | 61 | 55.7% | +0.056 | +1.11$ | 0.56$ | ✅ activa |
| PRICE_TARGET_GBM | 124 | 34.7% | -0.151 | +0.90$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 27 | 40.7% | -0.086 | -2.77$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | -4.68$ | 0.00$ | 🚫 desactivada |
| GBM_LATE_60M | 103 | 33.0% | -0.167 | -12.61$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | -18.89$ | 0.00$ | 🚫 desactivada |
| UPDOWN_GBM | 1094 | 47.6% | -0.024 | -25.89$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 127 | 47.2% | -0.027 | -26.77$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-08T09:45 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 8, 5:30AM-5:45AM ET… | ✅ WIN | +1.03$ |
| 2026-07-08T09:41 | STREAK_MOM_5M#XRP#5min | XRP Up or Down - July 8, 5:35AM-5:40AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-08T09:37 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 8, 5:15AM-5:30AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-08T09:36 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 8, 5:15AM-5:30AM ET… | ✅ WIN | +2.04$ |
| 2026-07-08T09:36 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 8, 5:15AM-5:30AM ET… | ❌ LOSS | -0.69$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-08T09:45 UTC | rechazos 1h: 3 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,036.46 | 0.0min |  |
| ✅ ETH | $1,736.69 | 0.0min |  |
| ✅ SOL | $77.29 | 0.0min |  |
| ✅ XRP | $1.08 | 0.0min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,039.50 | consenso |  |
| ETH | $1,736.80 | consenso |  |
| SOL | $77.20 | consenso |  |
| XRP | $1.08 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:3 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*