# Estado del bot — 2026-07-10 14:48 UTC

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
| P&L fiel (stake fijo 1$) | +741.44 $ |
| P&L sim compuesto | 🟢 +1131.81 $ (ficción Kelly: +4449% s/ operativo) |
| P&L sim hoy (2026-07-10) | 🟢 +219.88 $ |
| Operaciones resueltas | 7701 (4229 WIN / 3472 LOSS) — 54.9% |
| Señales abiertas | 187 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2898 | 61.4% | +0.114 | ➡️ estable | +940.38$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 357 | 66.1% | +0.160 | 📈 madura (+0.04) | +139.46$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 444 | 56.8% | +0.067 | 📈 madura (+0.08) | +69.41$ | 0.67$ | ✅ activa |
| ORDER_FLOW_5M | 1570 | 51.3% | +0.013 | ➡️ estable | +17.57$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 116 | 60.3% | +0.102 | 📈 madura (+0.13) | +13.28$ | 1.02$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 230 | 38.3% | -0.116 | 📈 madura (+0.09) | +6.90$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| FAVORITO_CONFIRMADO | 70 | 72.9% | +0.222 | ➡️ estable | +2.66$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 1216 | 48.7% | -0.013 | ➡️ estable | +2.55$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 26 | 57.7% | +0.071 | — | +1.86$ | 0.71$ | ✅ activa |
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
| 2026-07-10T14:46 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 10, 10:30AM-10:45AM ET… | ✅ WIN | +1.92$ |
| 2026-07-10T14:46 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 10, 10:30AM-10:45AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-10T14:46 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 10, 10:30AM-10:45AM ET… | ❌ LOSS | -1.89$ |
| 2026-07-10T14:46 | LEADLAG_BTC_XRP_15M#XRP#15min | XRP Up or Down - July 10, 10:30AM-10:45AM ET… | ✅ WIN | +0.48$ |
| 2026-07-10T14:44 | FAVORITO_CONFIRMADO#BTC#5min | Bitcoin Up or Down - July 10, 10:35AM-10:40AM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-10T14:47 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,021.60 | 0.1min |  |
| ✅ ETH | $1,785.61 | 0.1min |  |
| ✅ SOL | $77.72 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,025.90 | consenso |  |
| ETH | $1,785.61 | consenso |  |
| SOL | $77.59 | consenso |  |
| XRP | $1.10 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*