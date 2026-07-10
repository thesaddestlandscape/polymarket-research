# Estado del bot — 2026-07-10 20:43 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **24.92 $** |
| P&L real total | 🔴 **-0.52 $** |
| P&L real hoy | -6.53 $ |
| P&L real 7 días | +1.73 $ |
| Fees pagados (real) | 7.19 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +785.81 $ |
| P&L sim compuesto | 🟢 +1210.18 $ (ficción Kelly: +4757% s/ operativo) |
| P&L sim hoy (2026-07-10) | 🟢 +298.25 $ |
| Operaciones resueltas | 8104 (4476 WIN / 3628 LOSS) — 55.2% |
| Señales abiertas | 195 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2989 | 61.4% | +0.114 | ➡️ estable | +964.54$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 429 | 66.7% | +0.166 | 📈 madura (+0.05) | +179.74$ | 1.66$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 535 | 56.6% | +0.066 | 📈 madura (+0.08) | +89.75$ | 0.66$ | ✅ activa |
| ORDER_FLOW_5M | 1570 | 51.3% | +0.013 | ➡️ estable | +17.57$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 120 | 61.7% | +0.115 | 📈 madura (+0.13) | +17.48$ | 1.15$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 238 | 38.2% | -0.117 | 📈 madura (+0.07) | +8.57$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 28 | 60.7% | +0.100 | — | +3.21$ | 1.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 169 | 68.0% | +0.178 | 📉 agota (-0.13) | -5.17$ | 1.78$ | ✅ activa |
| UPDOWN_GBM | 1234 | 48.4% | -0.016 | ➡️ estable | -5.85$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-10T20:33 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 10, 4:15PM-4:30PM ET… | ✅ WIN | +1.04$ |
| 2026-07-10T20:33 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 10, 4:15PM-4:30PM ET… | ✅ WIN | +2.00$ |
| 2026-07-10T20:33 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 10, 4:15PM-4:30PM ET… | ✅ WIN | +1.79$ |
| 2026-07-10T20:33 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 10, 4:15PM-4:30PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-10T20:33 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 10, 4:15PM-4:30PM ET… | ✅ WIN | +2.84$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-10T20:42 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,828.00 | 0.1min |  |
| ✅ ETH | $1,791.85 | 0.1min |  |
| ✅ SOL | $77.88 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,829.60 | consenso |  |
| ETH | $1,791.90 | consenso |  |
| SOL | $77.87 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*