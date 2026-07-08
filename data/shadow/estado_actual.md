# Estado del bot — 2026-07-08 12:32 UTC

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
| P&L fiel (stake fijo 1$) | +352.10 $ |
| P&L sim compuesto | 🟢 +609.80 $ (ficción Kelly: +2397% s/ operativo) |
| P&L sim hoy (2026-07-08) | 🟢 +104.13 $ |
| Operaciones resueltas | 5408 (2887 WIN / 2521 LOSS) — 53.4% |
| Señales abiertas | 146 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2118 | 61.7% | +0.117 | +683.75$ | 1.17$ | ✅ activa |
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
| UPDOWN_GBM | 1100 | 47.5% | -0.025 | -30.81$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-08T12:31 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 8, 8:15AM-8:30AM ET… | ✅ WIN | +1.49$ |
| 2026-07-08T12:31 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 8, 8:15AM-8:30AM ET… | ✅ WIN | +1.70$ |
| 2026-07-08T12:20 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 8, 8:00AM-8:15AM ET… | ✅ WIN | +1.68$ |
| 2026-07-08T12:20 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 8, 8:00AM-8:15AM ET… | ✅ WIN | +1.38$ |
| 2026-07-08T12:20 | UPDOWN_GBM#BTC#15min | Bitcoin Up or Down - July 8, 8:00AM-8:15AM ET… | ❌ LOSS | -1.59$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-08T12:32 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,200.69 | 0.0min |  |
| ✅ ETH | $1,744.92 | 0.0min |  |
| ✅ SOL | $77.46 | 0.0min |  |
| ✅ XRP | $1.09 | 0.0min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,200.69 | consenso |  |
| ETH | $1,744.92 | consenso |  |
| SOL | $77.42 | consenso |  |
| XRP | $1.09 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*