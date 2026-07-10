# Estado del bot — 2026-07-10 10:23 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **26.01 $** |
| P&L real total | 🟢 **+0.57 $** |
| P&L real hoy | -5.44 $ |
| P&L real 7 días | +2.82 $ |
| Fees pagados (real) | 7.14 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +706.82 $ |
| P&L sim compuesto | 🟢 +1075.28 $ (ficción Kelly: +4227% s/ operativo) |
| P&L sim hoy (2026-07-10) | 🟢 +163.35 $ |
| Operaciones resueltas | 7425 (4051 WIN / 3374 LOSS) — 54.6% |
| Señales abiertas | 163 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2834 | 61.4% | +0.114 | ➡️ estable | +929.09$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 302 | 66.9% | +0.168 | ➡️ estable | +118.53$ | 1.68$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 380 | 56.3% | +0.063 | 📈 madura (+0.07) | +53.25$ | 0.63$ | ✅ activa |
| ORDER_FLOW_5M | 1570 | 51.3% | +0.013 | ➡️ estable | +17.57$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 113 | 59.3% | +0.091 | 📈 madura (+0.08) | +11.63$ | 0.91$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 220 | 37.7% | -0.122 | 📈 madura (+0.08) | +6.26$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| UPDOWN_GBM | 1211 | 48.6% | -0.014 | ➡️ estable | +0.93$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 21 | 52.4% | +0.022 | — | +0.27$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 132 | 34.1% | -0.157 | 📉 agota (-0.10) | -0.77$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 159 | 55.3% | +0.053 | 📈 madura (+0.14) | -15.64$ | 0.53$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-10T10:18 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 10, 6:00AM-6:15AM ET… | ✅ WIN | +1.14$ |
| 2026-07-10T10:18 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 10, 6:00AM-6:15AM ET… | ✅ WIN | +0.44$ |
| 2026-07-10T10:18 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 10, 6:00AM-6:15AM ET… | ✅ WIN | +0.44$ |
| 2026-07-10T10:18 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 10, 6:00AM-6:15AM ET… | ✅ WIN | +1.92$ |
| 2026-07-10T10:18 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 10, 6:00AM-6:15AM ET… | ✅ WIN | +1.73$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-10T10:23 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,264.60 | 0.1min |  |
| ✅ ETH | $1,793.63 | 0.1min |  |
| ✅ SOL | $79.19 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,283.60 | consenso |  |
| ETH | $1,793.71 | consenso |  |
| SOL | $79.19 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*