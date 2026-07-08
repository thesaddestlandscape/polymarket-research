# Estado del bot — 2026-07-08 08:19 UTC

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
| P&L fiel (stake fijo 1$) | +328.42 $ |
| P&L sim compuesto | 🟢 +583.62 $ (ficción Kelly: +2294% s/ operativo) |
| P&L sim hoy (2026-07-08) | 🟢 +77.94 $ |
| Operaciones resueltas | 5289 (2816 WIN / 2473 LOSS) — 53.2% |
| Señales abiertas | 147 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2056 | 61.5% | +0.115 | +659.19$ | 1.15$ | ✅ activa |
| ORDER_FLOW_5M | 1553 | 51.3% | +0.013 | +17.05$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 24 | 75.0% | +0.231 | +7.68$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 7 | 100.0% | +0.136 | +3.04$ | 1.36$ | ⏳ acumulando |
| STREAK_FADE_15M | 61 | 55.7% | +0.056 | +1.11$ | 0.56$ | ✅ activa |
| PRICE_TARGET_GBM | 124 | 34.7% | -0.151 | +0.90$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 16 | 37.5% | -0.089 | -2.19$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | -4.68$ | 0.00$ | 🚫 desactivada |
| GBM_LATE_60M | 103 | 33.0% | -0.167 | -12.61$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | -18.89$ | 0.00$ | 🚫 desactivada |
| UPDOWN_GBM | 1090 | 47.6% | -0.024 | -26.41$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 127 | 47.2% | -0.027 | -26.77$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-08T08:19 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 8, 4:00AM-4:15AM ET… | ✅ WIN | +1.71$ |
| 2026-07-08T08:19 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 8, 4:00AM-4:15AM ET… | ❌ LOSS | -1.71$ |
| 2026-07-08T08:19 | UPDOWN_GBM#ETH#15min | Ethereum Up or Down - July 8, 4:00AM-4:15AM ET… | ✅ WIN | +1.74$ |
| 2026-07-08T08:18 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 8, 4:00AM-4:15AM ET… | ✅ WIN | +1.83$ |
| 2026-07-08T08:16 | UPDOWN_GBM#BTC#15min | Bitcoin Up or Down - July 8, 4:00AM-4:15AM ET… | ✅ WIN | +3.39$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-08T08:19 UTC | rechazos 1h: 5 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,527.01 | 0.1min |  |
| ✅ ETH | $1,745.91 | 0.1min |  |
| ✅ SOL | $77.76 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,531.10 | consenso |  |
| ETH | $1,745.91 | consenso |  |
| SOL | $77.73 | consenso |  |
| XRP | $1.09 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:5 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*