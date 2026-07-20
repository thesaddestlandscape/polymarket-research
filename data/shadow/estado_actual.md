# Estado del bot — 2026-07-20 01:15 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **0.78 $** |
| P&L real total | 🔴 **-24.66 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -13.66 $ |
| Fees pagados (real) | 8.68 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3292.45 $ |
| P&L sim compuesto | 🟢 +6020.67 $ (ficción Kelly: +23666% s/ operativo) |
| P&L sim hoy (2026-07-20) | 🟢 +22.34 $ |
| Operaciones resueltas | 23538 (14309 WIN / 9229 LOSS) — 60.8% |
| Señales abiertas | 136 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 5992 | 60.8% | +0.108 | ➡️ estable | +2115.61$ | 1.08$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3212 | 65.5% | +0.155 | ➡️ estable | +1998.95$ | 1.55$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3172 | 60.4% | +0.104 | 📈 madura (+0.05) | +1185.57$ | 1.04$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 711 | 67.8% | +0.177 | ➡️ estable | +326.33$ | 1.77$ | ✅ activa |
| UPDOWN_GBM | 1889 | 52.2% | +0.022 | 📈 madura (+0.12) | +143.06$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 178 | 65.7% | +0.156 | 📈 madura (+0.05) | +96.16$ | 1.56$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4025 | 68.6% | +0.186 | ➡️ estable | +61.08$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| STREAK_FADE_15M | 229 | 59.8% | +0.097 | ➡️ estable | +35.37$ | 0.97$ | ✅ activa |
| LATE_WINDOW_5MIN | 53 | 69.8% | +0.191 | 📉 agota (-0.06) | +20.77$ | 1.91$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 77 | 79.2% | +0.285 | 📉 agota (-0.09) | +14.87$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 208 | 53.4% | +0.033 | 📉 agota (-0.12) | +13.80$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1631 | 51.3% | +0.013 | ➡️ estable | +13.70$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 376 | 63.6% | +0.135 | ➡️ estable | +11.82$ | 1.35$ | ✅ activa |
| GBM_LATE_5M | 127 | 56.7% | +0.066 | 📈 madura (+0.05) | +9.23$ | 0.66$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 166 | 81.9% | +0.315 | ➡️ estable | +9.20$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 5 | 60.0% | +0.018 | — | +0.32$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 149 | 32.9% | -0.169 | 📉 agota (-0.12) | -4.27$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-20T01:14 | GBM_LATE_5M#BTC#5min | Bitcoin Up or Down - July 19, 9:05PM-9:10PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-20T01:12 | GBM_LATE_5M#SOL#5min | Solana Up or Down - July 19, 9:05PM-9:10PM ET… | ✅ WIN | +0.32$ |
| 2026-07-20T01:06 | FAVORITO_CONFIRMADO#ETH#60min | Ethereum Up or Down - July 19, 8PM ET… | ✅ WIN | +0.84$ |
| 2026-07-20T01:04 | UPDOWN_GBM_15M_TARDIO#DOGE#15min | Dogecoin Up or Down - July 19, 8:45PM-9:00PM ET… | ✅ WIN | +2.05$ |
| 2026-07-20T01:04 | UPDOWN_GBM#DOGE#15min | Dogecoin Up or Down - July 19, 8:45PM-9:00PM ET… | ✅ WIN | +1.17$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-20T01:14 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,784.00 | 0.0min |  |
| ✅ ETH | $1,879.30 | 0.0min |  |
| ✅ SOL | $77.03 | 0.0min |  |
| ✅ XRP | $1.10 | 0.0min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,880.38 | consenso |  |
| ETH | $1,883.71 | consenso |  |
| SOL | $77.13 | consenso |  |
| XRP | $1.10 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*