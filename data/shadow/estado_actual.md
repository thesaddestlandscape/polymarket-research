# Estado del bot — 2026-07-19 12:55 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **0.78 $** |
| P&L real total | 🔴 **-24.66 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -17.21 $ |
| Fees pagados (real) | 8.68 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3044.15 $ |
| P&L sim compuesto | 🟢 +5525.08 $ (ficción Kelly: +21718% s/ operativo) |
| P&L sim hoy (2026-07-19) | 🟢 +363.31 $ |
| Operaciones resueltas | 22509 (13625 WIN / 8884 LOSS) — 60.5% |
| Señales abiertas | 137 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 5825 | 60.7% | +0.107 | ➡️ estable | +1982.25$ | 1.07$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3053 | 65.2% | +0.152 | ➡️ estable | +1838.18$ | 1.52$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3002 | 60.1% | +0.101 | 📈 madura (+0.04) | +1065.35$ | 1.01$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 617 | 68.2% | +0.182 | ➡️ estable | +285.51$ | 1.82$ | ✅ activa |
| UPDOWN_GBM | 1824 | 52.0% | +0.020 | 📈 madura (+0.12) | +131.85$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 169 | 65.7% | +0.155 | 📈 madura (+0.07) | +92.12$ | 1.55$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| FAVORITO_CONFIRMADO | 3812 | 68.5% | +0.185 | ➡️ estable | +40.89$ | 1.84$ | ✅ activa |
| STREAK_FADE_15M | 225 | 59.6% | +0.095 | ➡️ estable | +33.25$ | 0.95$ | ✅ activa |
| LATE_WINDOW_5MIN | 49 | 73.5% | +0.225 | ➡️ estable | +24.54$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 302 | 64.6% | +0.145 | 📉 agota (-0.05) | +16.39$ | 1.45$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 192 | 53.6% | +0.036 | 📉 agota (-0.11) | +14.03$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1631 | 51.3% | +0.013 | ➡️ estable | +13.70$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 62 | 77.4% | +0.266 | 📉 agota (-0.06) | +9.34$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 151 | 82.1% | +0.317 | ➡️ estable | +8.21$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 328 | 38.7% | -0.112 | ➡️ estable | +6.48$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 104 | 56.7% | +0.066 | ➡️ estable | +3.82$ | 0.66$ | ✅ activa |
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
| 2026-07-19T12:48 | BALLENAS_CONFIRMADAS_15M#SOL#15min | Solana Up or Down - July 19, 8:30AM-8:45AM ET… | ✅ WIN | +0.31$ |
| 2026-07-19T12:48 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 19, 8:30AM-8:45AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-19T12:48 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 19, 8:30AM-8:45AM ET… | ✅ WIN | +0.38$ |
| 2026-07-19T12:48 | FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | Solana Up or Down - July 19, 8:30AM-8:45AM ET… | ✅ WIN | +0.31$ |
| 2026-07-19T12:48 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 19, 8:30AM-8:45AM ET… | ✅ WIN | +0.31$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-19T12:53 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,341.60 | 0.1min |  |
| ✅ ETH | $1,868.52 | 0.1min |  |
| ✅ SOL | $75.99 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,341.60 | consenso |  |
| ETH | $1,868.52 | consenso |  |
| SOL | $75.89 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*