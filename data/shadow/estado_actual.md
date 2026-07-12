# Estado del bot — 2026-07-12 00:01 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **17.99 $** |
| P&L real total | 🔴 **-7.45 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | +10.01 $ |
| Fees pagados (real) | 7.61 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1034.18 $ |
| P&L sim compuesto | 🟢 +1597.25 $ (ficción Kelly: +6279% s/ operativo) |
| P&L sim hoy (2026-07-12) | 🔴 -7.46 $ |
| Operaciones resueltas | 9995 (5626 WIN / 4369 LOSS) — 56.3% |
| Señales abiertas | 129 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3391 | 61.1% | +0.111 | ➡️ estable | +1075.99$ | 1.11$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 769 | 64.4% | +0.143 | 📉 agota (-0.05) | +327.93$ | 1.43$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 934 | 57.6% | +0.076 | ➡️ estable | +194.48$ | 0.76$ | ✅ activa |
| STREAK_FADE_15M | 135 | 61.5% | +0.113 | 📈 madura (+0.12) | +20.46$ | 1.13$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 56 | 64.3% | +0.138 | 📈 madura (+0.07) | +18.67$ | 1.38$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| UPDOWN_GBM | 1294 | 49.1% | -0.008 | 📈 madura (+0.05) | +15.60$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 300 | 38.7% | -0.113 | 📈 madura (+0.04) | +9.21$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| STREAK_FADE_5M | 59 | 52.5% | +0.025 | 📉 agota (-0.05) | +0.86$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 136 | 34.6% | -0.152 | 📉 agota (-0.13) | -0.14$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 192 | 57.8% | +0.077 | 📈 madura (+0.23) | -13.59$ | 0.77$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 670 | 66.6% | +0.165 | ➡️ estable | -22.89$ | 1.65$ | ✅ activa |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-12T00:00 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 11, 7:45PM-8:00PM ET… | ✅ WIN | +2.00$ |
| 2026-07-12T00:00 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 11, 7:45PM-8:00PM ET… | ✅ WIN | +0.58$ |
| 2026-07-12T00:00 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 11, 7:45PM-8:00PM ET… | ❌ LOSS | -1.55$ |
| 2026-07-12T00:00 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 11, 7:45PM-8:00PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-12T00:00 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 11, 7:45PM-8:00PM ET… | ✅ WIN | +2.00$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-12T00:00 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,785.01 | 0.1min |  |
| ✅ ETH | $1,787.71 | 0.1min |  |
| ✅ SOL | $76.68 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,792.10 | consenso |  |
| ETH | $1,787.71 | consenso |  |
| SOL | $76.73 | consenso |  |
| XRP | $1.10 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*