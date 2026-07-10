# Estado del bot — 2026-07-10 07:58 UTC

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
| P&L fiel (stake fijo 1$) | +678.23 $ |
| P&L sim compuesto | 🟢 +1032.38 $ (ficción Kelly: +4058% s/ operativo) |
| P&L sim hoy (2026-07-10) | 🟢 +120.45 $ |
| Operaciones resueltas | 7309 (3975 WIN / 3334 LOSS) — 54.4% |
| Señales abiertas | 165 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2795 | 61.4% | +0.114 | ➡️ estable | +916.20$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 274 | 66.4% | +0.163 | ➡️ estable | +101.00$ | 1.63$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 342 | 55.6% | +0.055 | 📈 madura (+0.13) | +42.89$ | 0.55$ | ✅ activa |
| ORDER_FLOW_5M | 1570 | 51.3% | +0.013 | ➡️ estable | +17.57$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 112 | 58.9% | +0.088 | 📈 madura (+0.07) | +11.00$ | 0.88$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 215 | 37.7% | -0.122 | 📈 madura (+0.10) | +7.12$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| LEADLAG_BTC_XRP_15M | 18 | 50.0% | +0.000 | — | -0.20$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 132 | 34.1% | -0.157 | 📉 agota (-0.10) | -0.77$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM | 1209 | 48.5% | -0.015 | ➡️ estable | -0.95$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 159 | 55.3% | +0.053 | 📈 madura (+0.14) | -15.64$ | 0.53$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-10T07:50 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 10, 3:30AM-3:45AM ET… | ✅ WIN | +0.68$ |
| 2026-07-10T07:50 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 10, 3:30AM-3:45AM ET… | ✅ WIN | +0.29$ |
| 2026-07-10T07:50 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 10, 3:30AM-3:45AM ET… | ✅ WIN | +0.29$ |
| 2026-07-10T07:46 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 10, 3:30AM-3:45AM ET… | ✅ WIN | +0.72$ |
| 2026-07-10T07:46 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 10, 3:30AM-3:45AM ET… | ✅ WIN | +1.96$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-10T07:58 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,945.18 | 0.1min |  |
| ✅ ETH | $1,772.15 | 0.1min |  |
| ✅ SOL | $78.79 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,950.00 | consenso |  |
| ETH | $1,772.15 | consenso |  |
| SOL | $78.79 | consenso |  |
| XRP | $1.10 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*