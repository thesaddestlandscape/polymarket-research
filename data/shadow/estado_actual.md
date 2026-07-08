# Estado del bot — 2026-07-08 11:46 UTC

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
| P&L fiel (stake fijo 1$) | +345.45 $ |
| P&L sim compuesto | 🟢 +604.02 $ (ficción Kelly: +2374% s/ operativo) |
| P&L sim hoy (2026-07-08) | 🟢 +98.34 $ |
| Operaciones resueltas | 5390 (2877 WIN / 2513 LOSS) — 53.4% |
| Señales abiertas | 148 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2107 | 61.7% | +0.116 | +678.22$ | 1.16$ | ✅ activa |
| ORDER_FLOW_5M | 1553 | 51.3% | +0.013 | +17.05$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 25 | 76.0% | +0.241 | +8.74$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 7 | 100.0% | +0.136 | +3.04$ | 1.36$ | ⏳ acumulando |
| STREAK_MOM_5M | 52 | 53.8% | +0.037 | +1.16$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 61 | 55.7% | +0.056 | +1.11$ | 0.56$ | ✅ activa |
| PRICE_TARGET_GBM | 124 | 34.7% | -0.151 | +0.90$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | -4.68$ | 0.00$ | 🚫 desactivada |
| GBM_LATE_60M | 108 | 32.4% | -0.173 | -13.34$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | -18.89$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 127 | 47.2% | -0.027 | -26.77$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM | 1098 | 47.5% | -0.025 | -28.71$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-08T11:46 | UPDOWN_GBM#BTC#15min | Bitcoin Up or Down - July 8, 7:30AM-7:45AM ET… | ✅ WIN | +0.28$ |
| 2026-07-08T11:46 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 8, 7:30AM-7:45AM ET… | ✅ WIN | +0.71$ |
| 2026-07-08T11:46 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 8, 7:30AM-7:45AM ET… | ❌ LOSS | -1.82$ |
| 2026-07-08T11:46 | UPDOWN_GBM#ETH#15min | Ethereum Up or Down - July 8, 7:30AM-7:45AM ET… | ❌ LOSS | -1.21$ |
| 2026-07-08T11:34 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 8, 7:15AM-7:30AM ET… | ✅ WIN | +1.16$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-08T11:46 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,086.00 | 0.1min |  |
| ✅ ETH | $1,736.27 | 0.1min |  |
| ✅ SOL | $77.52 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,086.00 | consenso |  |
| ETH | $1,736.27 | consenso |  |
| SOL | $77.17 | consenso |  |
| XRP | $1.08 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*