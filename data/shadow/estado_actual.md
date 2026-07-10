# Estado del bot — 2026-07-10 08:35 UTC

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
| P&L fiel (stake fijo 1$) | +693.76 $ |
| P&L sim compuesto | 🟢 +1051.46 $ (ficción Kelly: +4133% s/ operativo) |
| P&L sim hoy (2026-07-10) | 🟢 +139.53 $ |
| Operaciones resueltas | 7344 (4002 WIN / 3342 LOSS) — 54.5% |
| Señales abiertas | 158 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2806 | 61.4% | +0.114 | ➡️ estable | +918.11$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 283 | 67.1% | +0.170 | ➡️ estable | +110.84$ | 1.70$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 352 | 56.2% | +0.062 | 📈 madura (+0.11) | +48.18$ | 0.62$ | ✅ activa |
| ORDER_FLOW_5M | 1570 | 51.3% | +0.013 | ➡️ estable | +17.57$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 112 | 58.9% | +0.088 | 📈 madura (+0.07) | +11.00$ | 0.88$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 218 | 38.1% | -0.118 | 📈 madura (+0.10) | +7.28$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| UPDOWN_GBM | 1211 | 48.6% | -0.014 | ➡️ estable | +0.93$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| LEADLAG_BTC_XRP_15M | 18 | 50.0% | +0.000 | — | -0.20$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 132 | 34.1% | -0.157 | 📉 agota (-0.10) | -0.77$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 159 | 55.3% | +0.053 | 📈 madura (+0.14) | -15.64$ | 0.53$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-10T08:30 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 10, 4:15AM-4:30AM ET… | ✅ WIN | +1.90$ |
| 2026-07-10T08:30 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 10, 4:15AM-4:30AM ET… | ✅ WIN | +0.36$ |
| 2026-07-10T08:30 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 10, 4:15AM-4:30AM ET… | ✅ WIN | +0.30$ |
| 2026-07-10T08:30 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 10, 4:15AM-4:30AM ET… | ✅ WIN | +0.41$ |
| 2026-07-10T08:30 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 10, 4:15AM-4:30AM ET… | ✅ WIN | +1.44$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-10T08:34 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,232.29 | 0.0min |  |
| ✅ ETH | $1,783.98 | 0.0min |  |
| ✅ SOL | $79.37 | 0.0min |  |
| ✅ XRP | $1.11 | 0.0min |  |

**Cross-source** (coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,238.30 | consenso |  |
| ETH | $1,784.00 | consenso |  |
| SOL | $79.30 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*