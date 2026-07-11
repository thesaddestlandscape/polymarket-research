# Estado del bot — 2026-07-11 21:44 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **21.16 $** |
| P&L real total | 🔴 **-4.28 $** |
| P&L real hoy | -6.75 $ |
| P&L real 7 días | +10.57 $ |
| Fees pagados (real) | 7.56 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +995.28 $ |
| P&L sim compuesto | 🟢 +1552.75 $ (ficción Kelly: +6104% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +273.35 $ |
| Operaciones resueltas | 9812 (5512 WIN / 4300 LOSS) — 56.2% |
| Señales abiertas | 186 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3356 | 61.1% | +0.110 | ➡️ estable | +1055.76$ | 1.10$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 737 | 64.2% | +0.141 | 📉 agota (-0.05) | +307.38$ | 1.41$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 899 | 57.5% | +0.075 | ➡️ estable | +179.77$ | 0.75$ | ✅ activa |
| STREAK_FADE_15M | 134 | 61.9% | +0.118 | 📈 madura (+0.13) | +21.31$ | 1.18$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 53 | 66.0% | +0.155 | 📈 madura (+0.15) | +19.18$ | 1.54$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| UPDOWN_GBM | 1286 | 49.0% | -0.010 | 📈 madura (+0.04) | +12.59$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 297 | 38.7% | -0.112 | 📈 madura (+0.04) | +10.33$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| STREAK_FADE_5M | 39 | 53.8% | +0.037 | 📈 madura (+0.11) | +1.10$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 136 | 34.6% | -0.152 | 📉 agota (-0.13) | -0.14$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 624 | 66.8% | +0.168 | 📉 agota (-0.04) | -11.61$ | 1.68$ | ✅ activa |
| WEEKLY_PRICE | 192 | 57.8% | +0.077 | 📈 madura (+0.23) | -13.59$ | 0.77$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T21:40 | STREAK_FADE_5M#XRP#5min | XRP Up or Down - July 11, 5:30PM-5:35PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-11T21:36 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 11, 5:25PM-5:30PM ET… | ✅ WIN | +0.25$ |
| 2026-07-11T21:34 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 11, 5:15PM-5:30PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-11T21:34 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 11, 5:15PM-5:30PM ET… | ❌ LOSS | -1.12$ |
| 2026-07-11T21:34 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 11, 5:15PM-5:30PM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T21:43 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,305.86 | 0.1min |  |
| ✅ ETH | $1,822.99 | 0.1min |  |
| ✅ SOL | $78.15 | 0.1min |  |
| ✅ XRP | $1.12 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,317.50 | consenso |  |
| ETH | $1,822.99 | consenso |  |
| SOL | $78.16 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*