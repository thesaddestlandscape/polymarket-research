# Estado del bot — 2026-07-10 11:45 UTC

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
| P&L fiel (stake fijo 1$) | +712.23 $ |
| P&L sim compuesto | 🟢 +1088.67 $ (ficción Kelly: +4279% s/ operativo) |
| P&L sim hoy (2026-07-10) | 🟢 +176.73 $ |
| Operaciones resueltas | 7479 (4085 WIN / 3394 LOSS) — 54.6% |
| Señales abiertas | 178 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2850 | 61.5% | +0.115 | ➡️ estable | +935.01$ | 1.15$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 314 | 66.2% | +0.161 | ➡️ estable | +119.61$ | 1.61$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 396 | 56.3% | +0.063 | 📈 madura (+0.06) | +58.54$ | 0.63$ | ✅ activa |
| ORDER_FLOW_5M | 1570 | 51.3% | +0.013 | ➡️ estable | +17.57$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 113 | 59.3% | +0.091 | 📈 madura (+0.08) | +11.63$ | 0.91$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 221 | 38.0% | -0.119 | 📈 madura (+0.09) | +6.90$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| UPDOWN_GBM | 1211 | 48.6% | -0.014 | ➡️ estable | +0.93$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 9 | 77.8% | +0.102 | — | +0.46$ | 1.02$ | ✅ activa |
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
| 2026-07-10T11:36 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 10, 7:30AM-7:35AM ET… | ✅ WIN | +0.12$ |
| 2026-07-10T11:36 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 10, 7:30AM-7:35AM ET… | ✅ WIN | +0.15$ |
| 2026-07-10T11:33 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 10, 7:15AM-7:30AM ET… | ❌ LOSS | -1.07$ |
| 2026-07-10T11:33 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 10, 7:15AM-7:30AM ET… | ✅ WIN | +0.83$ |
| 2026-07-10T11:33 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 10, 7:15AM-7:30AM ET… | ✅ WIN | +0.34$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-10T11:44 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,296.12 | 0.0min |  |
| ✅ ETH | $1,793.36 | 0.0min |  |
| ✅ SOL | $79.32 | 0.0min |  |
| ✅ XRP | $1.11 | 0.0min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,309.90 | consenso |  |
| ETH | $1,793.36 | consenso |  |
| SOL | $79.14 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*