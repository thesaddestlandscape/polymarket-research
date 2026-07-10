# Estado del bot — 2026-07-10 07:40 UTC

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
| P&L fiel (stake fijo 1$) | +674.81 $ |
| P&L sim compuesto | 🟢 +1025.77 $ (ficción Kelly: +4032% s/ operativo) |
| P&L sim hoy (2026-07-10) | 🟢 +113.84 $ |
| Operaciones resueltas | 7296 (3965 WIN / 3331 LOSS) — 54.3% |
| Señales abiertas | 171 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2791 | 61.4% | +0.114 | ➡️ estable | +915.41$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 270 | 65.9% | +0.158 | ➡️ estable | +96.64$ | 1.58$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 338 | 55.3% | +0.053 | 📈 madura (+0.11) | +40.86$ | 0.53$ | ✅ activa |
| ORDER_FLOW_5M | 1570 | 51.3% | +0.013 | ➡️ estable | +17.57$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 112 | 58.9% | +0.088 | 📈 madura (+0.07) | +11.00$ | 0.88$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 215 | 37.7% | -0.122 | 📈 madura (+0.10) | +7.12$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| LEADLAG_BTC_XRP_15M | 18 | 50.0% | +0.000 | — | -0.20$ | 0.50$ | ✅ activa |
| UPDOWN_GBM | 1208 | 48.5% | -0.015 | ➡️ estable | -0.39$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 132 | 34.1% | -0.157 | 📉 agota (-0.10) | -0.77$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 159 | 55.3% | +0.053 | 📈 madura (+0.14) | -15.64$ | 0.53$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-10T07:31 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 10, 3:15AM-3:30AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-10T07:31 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 10, 3:15AM-3:30AM ET… | ✅ WIN | +1.44$ |
| 2026-07-10T07:31 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 10, 3:15AM-3:30AM ET… | ✅ WIN | +1.38$ |
| 2026-07-10T07:31 | UPDOWN_GBM#ETH#15min | Ethereum Up or Down - July 10, 3:15AM-3:30AM ET… | ✅ WIN | +1.57$ |
| 2026-07-10T07:31 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 10, 3:15AM-3:30AM ET… | ❌ LOSS | -0.56$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-10T07:40 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,877.00 | 0.1min |  |
| ✅ ETH | $1,771.84 | 0.1min |  |
| ✅ SOL | $78.83 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,897.60 | consenso |  |
| ETH | $1,772.67 | consenso |  |
| SOL | $78.86 | consenso |  |
| XRP | $1.10 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*