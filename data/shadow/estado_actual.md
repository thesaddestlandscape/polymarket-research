# Estado del bot — 2026-07-10 14:24 UTC

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
| P&L fiel (stake fijo 1$) | +733.70 $ |
| P&L sim compuesto | 🟢 +1121.05 $ (ficción Kelly: +4407% s/ operativo) |
| P&L sim hoy (2026-07-10) | 🟢 +209.11 $ |
| Operaciones resueltas | 7676 (4211 WIN / 3465 LOSS) — 54.9% |
| Señales abiertas | 190 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2893 | 61.4% | +0.114 | ➡️ estable | +937.39$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 352 | 65.9% | +0.158 | ➡️ estable | +134.39$ | 1.58$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 439 | 56.5% | +0.065 | 📈 madura (+0.07) | +67.23$ | 0.65$ | ✅ activa |
| ORDER_FLOW_5M | 1570 | 51.3% | +0.013 | ➡️ estable | +17.57$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 116 | 60.3% | +0.102 | 📈 madura (+0.13) | +13.28$ | 1.02$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 230 | 38.3% | -0.116 | 📈 madura (+0.09) | +6.90$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 62 | 75.8% | +0.250 | 📈 madura (+0.09) | +3.80$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 25 | 56.0% | +0.056 | — | +1.38$ | 0.56$ | ✅ activa |
| UPDOWN_GBM | 1215 | 48.6% | -0.014 | ➡️ estable | +1.35$ | 0.50$ | ⚠️ IC negativo |
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
| 2026-07-10T14:16 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 10, 10:00AM-10:15AM ET… | ✅ WIN | +1.60$ |
| 2026-07-10T14:16 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 10, 10:00AM-10:15AM ET… | ✅ WIN | +0.61$ |
| 2026-07-10T14:16 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 10, 10:00AM-10:15AM ET… | ✅ WIN | +0.59$ |
| 2026-07-10T14:16 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 10, 10:00AM-10:15AM ET… | ✅ WIN | +0.31$ |
| 2026-07-10T14:16 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 10, 10:00AM-10:15AM ET… | ✅ WIN | +1.92$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-10T14:23 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,142.77 | 0.1min |  |
| ✅ ETH | $1,790.69 | 0.1min |  |
| ✅ SOL | $77.63 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,101.86 | consenso |  |
| ETH | $1,787.35 | consenso |  |
| SOL | $77.92 | consenso |  |
| XRP | $1.10 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*