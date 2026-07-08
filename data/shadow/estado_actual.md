# Estado del bot — 2026-07-08 16:13 UTC

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
| P&L fiel (stake fijo 1$) | +360.50 $ |
| P&L sim compuesto | 🟢 +629.73 $ (ficción Kelly: +2475% s/ operativo) |
| P&L sim hoy (2026-07-08) | 🟢 +124.05 $ |
| Operaciones resueltas | 5565 (2975 WIN / 2590 LOSS) — 53.5% |
| Señales abiertas | 166 |

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
| STREAK_MOM_5M | 87 | 49.4% | -0.006 | -2.16$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | -4.68$ | 0.00$ | 🚫 desactivada |
| GBM_LATE_60M | 121 | 34.7% | -0.150 | -11.52$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | -18.89$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 144 | 52.1% | +0.021 | -20.78$ | 0.50$ | ✅ activa |
| UPDOWN_GBM | 1111 | 47.3% | -0.027 | -32.51$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-08T16:11 | STREAK_MOM_5M#ETH#5min | Ethereum Up or Down - July 8, 12:05PM-12:10PM ET… | ✅ WIN | +0.48$ |
| 2026-07-08T16:09 | STREAK_MOM_5M#ETH#5min | Ethereum Up or Down - July 8, 12:00PM-12:05PM ET… | ✅ WIN | +0.48$ |
| 2026-07-08T16:09 | STREAK_MOM_5M#SOL#5min | Solana Up or Down - July 8, 12:00PM-12:05PM ET… | ✅ WIN | +0.48$ |
| 2026-07-08T16:09 | WEEKLY_PRICE#SOL | Will the price of Solana be between $80 and $90 on… | ❌ LOSS | -0.51$ |
| 2026-07-08T16:07 | RESOLUTION_SNIPER#SOL#sniper | Will the price of Solana be between $70 and $80 on… | ✅ WIN | +0.43$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-08T16:13 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $61,797.65 | 0.0min |  |
| ✅ ETH | $1,726.23 | 0.0min |  |
| ✅ SOL | $76.97 | 0.0min |  |
| ✅ XRP | $1.08 | 0.0min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $61,797.65 | consenso |  |
| ETH | $1,726.23 | consenso |  |
| SOL | $76.91 | consenso |  |
| XRP | $1.08 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*