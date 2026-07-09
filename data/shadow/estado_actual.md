# Estado del bot — 2026-07-09 02:03 UTC

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
| P&L fiel (stake fijo 1$) | +384.85 $ |
| P&L sim compuesto | 🟢 +674.85 $ (ficción Kelly: +2653% s/ operativo) |
| P&L sim hoy (2026-07-09) | 🟢 +29.36 $ |
| Operaciones resueltas | 5892 (3145 WIN / 2747 LOSS) — 53.4% |
| Señales abiertas | 144 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2333 | 61.3% | +0.113 | +741.07$ | 1.13$ | ✅ activa |
| ORDER_FLOW_5M | 1558 | 51.4% | +0.014 | +21.27$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 28 | 67.9% | +0.167 | +4.54$ | 1.67$ | ✅ activa |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 129 | 34.1% | -0.156 | -0.43$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_15M | 85 | 51.8% | +0.017 | -0.88$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 144 | 35.4% | -0.144 | -1.24$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_TARDIO | 11 | 45.5% | -0.021 | -1.29$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | -4.68$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 169 | 49.7% | -0.003 | -5.02$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | -18.89$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 144 | 52.1% | +0.021 | -20.78$ | 0.50$ | ✅ activa |
| UPDOWN_GBM | 1149 | 47.7% | -0.023 | -28.39$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-09T02:03 | ORDER_FLOW_5M#BTC#5min | Bitcoin Up or Down - July 8, 9:55PM-10:00PM ET… | ✅ WIN | +1.44$ |
| 2026-07-09T02:03 | STREAK_MOM_5M#ETH#5min | Ethereum Up or Down - July 8, 9:55PM-10:00PM ET… | ✅ WIN | +0.50$ |
| 2026-07-09T02:02 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 8, 9:45PM-10:00PM ET… | ✅ WIN | +0.62$ |
| 2026-07-09T02:02 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 8, 9:45PM-10:00PM ET… | ❌ LOSS | -1.72$ |
| 2026-07-09T02:02 | UPDOWN_GBM#XRP#15min | XRP Up or Down - July 8, 9:45PM-10:00PM ET… | ✅ WIN | +1.86$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-09T02:03 UTC | rechazos 1h: 3 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $61,872.00 | 0.0min |  |
| ✅ ETH | $1,730.19 | 0.0min |  |
| ✅ SOL | $77.30 | 0.0min |  |
| ✅ XRP | $1.08 | 0.0min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $61,872.00 | consenso |  |
| ETH | $1,730.62 | consenso |  |
| SOL | $77.32 | consenso |  |
| XRP | $1.08 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:3 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*