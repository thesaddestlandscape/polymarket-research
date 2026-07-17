# Estado del bot — 2026-07-17 14:14 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **1.85 $** |
| P&L real total | 🔴 **-23.59 $** |
| P&L real hoy | -1.09 $ |
| P&L real 7 días | -29.61 $ |
| Fees pagados (real) | 8.65 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +2347.08 $ |
| P&L sim compuesto | 🟢 +4155.30 $ (ficción Kelly: +16334% s/ operativo) |
| P&L sim hoy (2026-07-17) | 🟢 +434.23 $ |
| Operaciones resueltas | 18850 (11209 WIN / 7641 LOSS) — 59.5% |
| Señales abiertas | 90 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 5232 | 60.2% | +0.102 | ➡️ estable | +1650.62$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 2433 | 64.9% | +0.149 | ➡️ estable | +1416.90$ | 1.49$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 2412 | 59.7% | +0.097 | ➡️ estable | +779.95$ | 0.97$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 286 | 67.8% | +0.177 | 📈 madura (+0.04) | +100.83$ | 1.77$ | ✅ activa |
| UPDOWN_GBM | 1677 | 51.4% | +0.014 | 📈 madura (+0.11) | +97.54$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 148 | 66.2% | +0.160 | 📈 madura (+0.13) | +83.92$ | 1.60$ | ✅ activa |
| STREAK_FADE_15M | 212 | 60.8% | +0.107 | 📈 madura (+0.05) | +37.50$ | 1.07$ | ✅ activa |
| WEEKLY_PRICE | 273 | 63.7% | +0.136 | 📈 madura (+0.26) | +29.85$ | 1.36$ | ✅ activa |
| LATE_WINDOW_5MIN | 49 | 73.5% | +0.225 | ➡️ estable | +24.54$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 158 | 56.3% | +0.062 | 📉 agota (-0.16) | +19.24$ | 0.62$ | ✅ activa |
| ORDER_FLOW_5M | 1624 | 51.2% | +0.012 | ➡️ estable | +13.36$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 31 | 80.6% | +0.288 | 📈 madura (+0.13) | +6.59$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 29 | 69.0% | +0.177 | — | +4.58$ | 1.77$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 80 | 82.5% | +0.317 | 📈 madura (+0.05) | +3.90$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 326 | 38.3% | -0.116 | ➡️ estable | +3.81$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM_ETH_15M_HORA7 | 3 | 66.7% | +0.015 | — | +0.37$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_5M | 11 | 45.5% | -0.021 | — | -0.62$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 148 | 33.1% | -0.167 | 📉 agota (-0.12) | -3.76$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 3004 | 67.8% | +0.178 | ➡️ estable | -27.28$ | 1.77$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-17T14:11 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 17, 10:00AM-10:05AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-17T14:01 | UPDOWN_GBM_15M_TARDIO#DOGE#15min | Dogecoin Up or Down - July 17, 9:45AM-10:00AM ET… | ✅ WIN | +0.44$ |
| 2026-07-17T14:01 | GBM_LATE_15M_PYCONFIRMADO#XRP#15min | XRP Up or Down - July 17, 9:45AM-10:00AM ET… | ✅ WIN | +1.77$ |
| 2026-07-17T14:01 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 17, 9:45AM-10:00AM ET… | ✅ WIN | +0.22$ |
| 2026-07-17T14:01 | FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | Solana Up or Down - July 17, 9:45AM-10:00AM ET… | ✅ WIN | +0.10$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-17T14:13 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,365.92 | 0.1min |  |
| ✅ ETH | $1,829.70 | 0.1min |  |
| ✅ SOL | $74.65 | 0.1min |  |
| ✅ XRP | $1.08 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,380.00 | consenso |  |
| ETH | $1,829.94 | consenso |  |
| SOL | $74.63 | consenso |  |
| XRP | $1.08 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*