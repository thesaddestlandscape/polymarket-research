# Estado del bot — 2026-07-20 00:40 UTC

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
| P&L fiel (stake fijo 1$) | +3287.14 $ |
| P&L sim compuesto | 🟢 +6007.52 $ (ficción Kelly: +23614% s/ operativo) |
| P&L sim hoy (2026-07-20) | 🟢 +9.20 $ |
| Operaciones resueltas | 23490 (14276 WIN / 9214 LOSS) — 60.8% |
| Señales abiertas | 125 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 5985 | 60.8% | +0.108 | ➡️ estable | +2119.60$ | 1.08$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3207 | 65.4% | +0.154 | ➡️ estable | +1992.64$ | 1.54$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3164 | 60.4% | +0.104 | 📈 madura (+0.05) | +1185.36$ | 1.04$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 705 | 67.7% | +0.176 | ➡️ estable | +320.21$ | 1.76$ | ✅ activa |
| UPDOWN_GBM | 1884 | 52.2% | +0.022 | 📈 madura (+0.12) | +139.51$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 178 | 65.7% | +0.156 | 📈 madura (+0.05) | +96.16$ | 1.56$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4016 | 68.6% | +0.186 | ➡️ estable | +59.46$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| STREAK_FADE_15M | 229 | 59.8% | +0.097 | ➡️ estable | +35.37$ | 0.97$ | ✅ activa |
| LATE_WINDOW_5MIN | 53 | 69.8% | +0.191 | 📉 agota (-0.06) | +20.77$ | 1.91$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 77 | 79.2% | +0.285 | 📉 agota (-0.09) | +14.87$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 207 | 53.6% | +0.036 | 📉 agota (-0.11) | +14.31$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1631 | 51.3% | +0.013 | ➡️ estable | +13.70$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 372 | 63.7% | +0.136 | ➡️ estable | +12.27$ | 1.36$ | ✅ activa |
| GBM_LATE_5M | 125 | 56.8% | +0.067 | 📈 madura (+0.07) | +9.42$ | 0.67$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 165 | 81.8% | +0.314 | ➡️ estable | +8.74$ | 2.00$ | ✅ activa |
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
| 2026-07-20T00:34 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 19, 8:25PM-8:30PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-20T00:34 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 19, 8:15PM-8:30PM ET… | ❌ LOSS | -1.14$ |
| 2026-07-20T00:34 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 19, 8:15PM-8:30PM ET… | ✅ WIN | +2.07$ |
| 2026-07-20T00:34 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 19, 8:15PM-8:30PM ET… | ✅ WIN | +3.38$ |
| 2026-07-20T00:34 | UPDOWN_GBM_15M_TARDIO#SOL#15min | Solana Up or Down - July 19, 8:15PM-8:30PM ET… | ✅ WIN | +1.83$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-20T00:38 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,806.89 | 0.1min |  |
| ✅ ETH | $1,878.29 | 0.1min |  |
| ✅ SOL | $76.82 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,854.40 | consenso |  |
| ETH | $1,880.34 | consenso |  |
| SOL | $76.82 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*