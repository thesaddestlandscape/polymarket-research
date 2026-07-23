# Estado del bot — 2026-07-23 04:09 UTC

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
| P&L fiel (stake fijo 1$) | +3600.02 $ |
| P&L sim compuesto | 🟢 +6790.57 $ (ficción Kelly: +26692% s/ operativo) |
| P&L sim hoy (2026-07-23) | 🟢 +78.71 $ |
| Operaciones resueltas | 30184 (18161 WIN / 12023 LOSS) — 60.2% |
| Señales abiertas | 138 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 7024 | 59.7% | +0.097 | 📉 agota (-0.03) | +2206.43$ | 0.97$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4222 | 62.8% | +0.128 | 📉 agota (-0.04) | +2180.53$ | 1.28$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4225 | 58.2% | +0.082 | ➡️ estable | +1291.05$ | 0.82$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1306 | 66.5% | +0.165 | ➡️ estable | +599.72$ | 1.65$ | ✅ activa |
| UPDOWN_GBM | 2278 | 52.9% | +0.029 | 📈 madura (+0.11) | +186.07$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 239 | 61.1% | +0.110 | 📉 agota (-0.07) | +110.98$ | 1.10$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5270 | 68.8% | +0.188 | ➡️ estable | +99.28$ | 1.88$ | ✅ activa |
| WEEKLY_PRICE | 336 | 68.2% | +0.180 | 📈 madura (+0.21) | +67.16$ | 1.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 819 | 63.0% | +0.130 | ➡️ estable | +37.73$ | 1.30$ | ✅ activa |
| STREAK_FADE_15M | 267 | 58.4% | +0.084 | 📉 agota (-0.08) | +32.81$ | 0.84$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 126 | 79.4% | +0.289 | 📈 madura (+0.03) | +22.84$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 280 | 81.8% | +0.316 | ➡️ estable | +14.03$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1658 | 51.1% | +0.011 | ➡️ estable | +11.31$ | 0.50$ | ✅ activa |
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
| 2026-07-23T04:07 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 22, 11:45PM-12:00AM ET… | ❌ LOSS | -1.53$ |
| 2026-07-23T04:07 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 22, 11:45PM-12:00AM ET… | ✅ WIN | +0.54$ |
| 2026-07-23T04:07 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 22, 11:45PM-12:00AM ET… | ✅ WIN | +0.88$ |
| 2026-07-23T04:07 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 22, 11:45PM-12:00AM ET… | ✅ WIN | +0.88$ |
| 2026-07-23T04:07 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 22, 11:45PM-12:00AM ET… | ✅ WIN | +1.84$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-23T04:07 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,622.05 | 0.1min |  |
| ✅ ETH | $1,919.87 | 0.1min |  |
| ✅ SOL | $77.63 | 0.1min |  |
| ✅ XRP | $1.13 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,622.05 | consenso |  |
| ETH | $1,919.87 | consenso |  |
| SOL | $77.62 | consenso |  |
| XRP | $1.13 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*