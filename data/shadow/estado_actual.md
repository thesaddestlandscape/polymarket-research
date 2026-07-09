# Estado del bot — 2026-07-09 01:58 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **34.91 $** |
| P&L real total | 🟢 **+9.47 $** |
| P&L real hoy | +2.23 $ |
| P&L real 7 días | +6.08 $ |
| Fees pagados (real) | 5.72 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +364.93 $ |
| P&L sim compuesto | 🟢 +660.43 $ (ficción Kelly: +2596% s/ operativo) |
| P&L sim hoy (2026-07-09) | 🟢 +14.94 $ |
| Operaciones resueltas | 5881 (3135 WIN / 2746 LOSS) — 53.3% |
| Señales abiertas | 152 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2329 | 61.3% | +0.113 | +739.82$ | 1.13$ | ✅ activa |
| ORDER_FLOW_5M | 1557 | 51.4% | +0.014 | +19.83$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 28 | 67.9% | +0.167 | +4.54$ | 1.67$ | ✅ activa |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 129 | 34.1% | -0.156 | -0.43$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_15M | 85 | 51.8% | +0.017 | -0.88$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 11 | 45.5% | -0.021 | -1.29$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | -4.68$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 168 | 49.4% | -0.006 | -5.52$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 141 | 34.0% | -0.157 | -9.44$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | -18.89$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 144 | 52.1% | +0.021 | -20.78$ | 0.50$ | ✅ activa |
| UPDOWN_GBM | 1147 | 47.6% | -0.024 | -31.41$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-09T01:56 | STREAK_MOM_5M#ETH#5min | Ethereum Up or Down - July 8, 9:50PM-9:55PM ET… | ✅ WIN | +0.50$ |
| 2026-07-09T01:56 | STREAK_MOM_5M#ETH#5min | Ethereum Up or Down - July 8, 9:45PM-9:50PM ET… | ✅ WIN | +0.48$ |
| 2026-07-09T01:52 | STREAK_MOM_5M#XRP#5min | XRP Up or Down - July 8, 9:45PM-9:50PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-09T01:52 | STREAK_MOM_5M#SOL#5min | Solana Up or Down - July 8, 9:45PM-9:50PM ET… | ❌ LOSS | -0.65$ |
| 2026-07-09T01:47 | STREAK_MOM_5M#ETH#5min | Ethereum Up or Down - July 8, 9:40PM-9:45PM ET… | ✅ WIN | +0.48$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-09T01:57 UTC | rechazos 1h: 3 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $61,875.10 | 0.0min |  |
| ✅ ETH | $1,731.30 | 0.0min |  |
| ✅ SOL | $77.38 | 0.0min |  |
| ✅ XRP | $1.08 | 0.0min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $61,877.80 | consenso |  |
| ETH | $1,731.53 | consenso |  |
| SOL | $77.44 | consenso |  |
| XRP | $1.08 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:3 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*