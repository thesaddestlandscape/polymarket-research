# Estado del bot — 2026-07-23 04:02 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **29.23 $** |
| P&L real total | 🔴 **-21.99 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -0.91 $ |
| Fees pagados (real) | 9.69 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3592.64 $ |
| P&L sim compuesto | 🟢 +6778.56 $ (ficción Kelly: +26645% s/ operativo) |
| P&L sim hoy (2026-07-23) | 🟢 +66.70 $ |
| Operaciones resueltas | 30162 (18144 WIN / 12018 LOSS) — 60.2% |
| Señales abiertas | 147 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 7020 | 59.7% | +0.097 | 📉 agota (-0.03) | +2201.77$ | 0.97$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4219 | 62.8% | +0.128 | 📉 agota (-0.04) | +2175.58$ | 1.28$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4222 | 58.2% | +0.082 | ➡️ estable | +1290.15$ | 0.82$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1305 | 66.5% | +0.165 | ➡️ estable | +597.55$ | 1.65$ | ✅ activa |
| UPDOWN_GBM | 2277 | 52.9% | +0.029 | 📈 madura (+0.11) | +185.52$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 239 | 61.1% | +0.110 | 📉 agota (-0.07) | +110.98$ | 1.10$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5261 | 68.8% | +0.188 | ➡️ estable | +99.97$ | 1.88$ | ✅ activa |
| WEEKLY_PRICE | 336 | 68.2% | +0.180 | 📈 madura (+0.21) | +67.16$ | 1.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 819 | 63.0% | +0.130 | ➡️ estable | +37.73$ | 1.30$ | ✅ activa |
| STREAK_FADE_15M | 267 | 58.4% | +0.084 | 📉 agota (-0.08) | +32.81$ | 0.84$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 126 | 79.4% | +0.289 | 📈 madura (+0.03) | +22.84$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 280 | 81.8% | +0.316 | ➡️ estable | +14.03$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1657 | 51.2% | +0.012 | ➡️ estable | +11.82$ | 0.50$ | ✅ activa |
| GBM_LATE_5M | 305 | 48.5% | -0.015 | 📉 agota (-0.17) | +11.02$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 263 | 51.0% | +0.009 | 📉 agota (-0.17) | +9.67$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 336 | 38.7% | -0.112 | ➡️ estable | +4.40$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 20 | 85.0% | +0.318 | — | +0.57$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 11 | 45.5% | -0.021 | — | -0.76$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 331 | 45.6% | -0.044 | 📉 agota (-0.15) | -1.92$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 318 | 44.0% | -0.059 | 📉 agota (-0.09) | -25.84$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-23T04:01 | ORDER_FLOW_5M#SOL#5min | Solana Up or Down - July 22, 11:50PM-11:55PM ET… | ❌ LOSS | -1.51$ |
| 2026-07-23T03:55 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 22, 11:45PM-11:50PM ET… | ❌ LOSS | -0.83$ |
| 2026-07-23T03:55 | BALLENAS_TARDIAS#BTC#15min | … | ✅ WIN | +0.16$ |
| 2026-07-23T03:55 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 22, 11:30PM-11:45PM ET… | ✅ WIN | +1.21$ |
| 2026-07-23T03:52 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 22, 11:30PM-11:45PM ET… | ✅ WIN | +1.84$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-23T04:01 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,624.51 | 0.1min |  |
| ✅ ETH | $1,919.53 | 0.1min |  |
| ✅ SOL | $77.59 | 0.1min |  |
| ✅ XRP | $1.13 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,624.51 | consenso |  |
| ETH | $1,919.53 | consenso |  |
| SOL | $77.58 | consenso |  |
| XRP | $1.13 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*