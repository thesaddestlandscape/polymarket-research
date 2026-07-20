# Estado del bot — 2026-07-20 03:28 UTC

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
| P&L fiel (stake fijo 1$) | +3312.14 $ |
| P&L sim compuesto | 🟢 +6069.87 $ (ficción Kelly: +23860% s/ operativo) |
| P&L sim hoy (2026-07-20) | 🟢 +71.55 $ |
| Operaciones resueltas | 23732 (14433 WIN / 9299 LOSS) — 60.8% |
| Señales abiertas | 129 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6022 | 60.8% | +0.108 | ➡️ estable | +2131.68$ | 1.08$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3241 | 65.6% | +0.156 | ➡️ estable | +2026.03$ | 1.56$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3203 | 60.4% | +0.104 | 📈 madura (+0.05) | +1196.60$ | 1.04$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 731 | 67.3% | +0.173 | ➡️ estable | +324.16$ | 1.73$ | ✅ activa |
| UPDOWN_GBM | 1896 | 52.1% | +0.021 | 📈 madura (+0.12) | +135.37$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 180 | 65.6% | +0.154 | 📈 madura (+0.07) | +96.33$ | 1.54$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4062 | 68.7% | +0.187 | ➡️ estable | +61.80$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| STREAK_FADE_15M | 229 | 59.8% | +0.097 | ➡️ estable | +35.37$ | 0.97$ | ✅ activa |
| LATE_WINDOW_5MIN | 54 | 70.4% | +0.196 | ➡️ estable | +22.40$ | 1.96$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 388 | 64.4% | +0.144 | ➡️ estable | +17.92$ | 1.44$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 81 | 79.0% | +0.283 | 📉 agota (-0.11) | +14.93$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1635 | 51.2% | +0.012 | ➡️ estable | +12.62$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 212 | 52.4% | +0.023 | 📉 agota (-0.12) | +11.76$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 169 | 82.2% | +0.319 | ➡️ estable | +9.80$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 137 | 55.5% | +0.054 | ➡️ estable | +7.94$ | 0.54$ | ✅ activa |
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
| 2026-07-20T03:24 | GBM_LATE_5M#BTC#5min | Bitcoin Up or Down - July 19, 11:15PM-11:20PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-20T03:21 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 19, 11:00PM-11:15PM ET… | ✅ WIN | +1.38$ |
| 2026-07-20T03:21 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 19, 11:00PM-11:15PM ET… | ✅ WIN | +0.82$ |
| 2026-07-20T03:21 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 19, 11:00PM-11:15PM ET… | ✅ WIN | +1.38$ |
| 2026-07-20T03:21 | UPDOWN_GBM_15M_TARDIO#SOL#15min | Solana Up or Down - July 19, 11:00PM-11:15PM ET… | ❌ LOSS | -1.48$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-20T03:26 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,694.96 | 0.1min |  |
| ✅ ETH | $1,874.98 | 0.1min |  |
| ✅ SOL | $76.67 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,696.80 | consenso |  |
| ETH | $1,874.98 | consenso |  |
| SOL | $76.72 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*