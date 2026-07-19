# Estado del bot — 2026-07-19 01:12 UTC

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
| P&L fiel (stake fijo 1$) | +2858.85 $ |
| P&L sim compuesto | 🟢 +5156.62 $ (ficción Kelly: +20270% s/ operativo) |
| P&L sim hoy (2026-07-19) | 🔴 -5.15 $ |
| Operaciones resueltas | 21632 (13044 WIN / 8588 LOSS) — 60.3% |
| Señales abiertas | 136 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 5679 | 60.5% | +0.105 | ➡️ estable | +1877.57$ | 1.05$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 2905 | 65.3% | +0.153 | ➡️ estable | +1731.46$ | 1.53$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 2850 | 60.0% | +0.100 | 📈 madura (+0.04) | +989.94$ | 1.00$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 546 | 67.6% | +0.175 | ➡️ estable | +226.16$ | 1.75$ | ✅ activa |
| UPDOWN_GBM | 1795 | 52.0% | +0.020 | 📈 madura (+0.13) | +127.54$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 166 | 66.3% | +0.161 | 📈 madura (+0.09) | +91.95$ | 1.61$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| FAVORITO_CONFIRMADO | 3618 | 68.4% | +0.183 | ➡️ estable | +36.45$ | 1.83$ | ✅ activa |
| STREAK_FADE_15M | 223 | 59.6% | +0.096 | ➡️ estable | +33.70$ | 0.96$ | ✅ activa |
| LATE_WINDOW_5MIN | 49 | 73.5% | +0.225 | ➡️ estable | +24.54$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 183 | 54.1% | +0.041 | 📉 agota (-0.12) | +14.50$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1631 | 51.3% | +0.013 | ➡️ estable | +13.70$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 251 | 64.1% | +0.140 | 📉 agota (-0.08) | +13.25$ | 1.40$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 56 | 78.6% | +0.276 | ➡️ estable | +10.15$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 132 | 81.8% | +0.313 | ➡️ estable | +4.88$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 326 | 38.3% | -0.116 | ➡️ estable | +3.81$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM_ETH_15M_HORA7 | 3 | 66.7% | +0.015 | — | +0.37$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_5M | 61 | 52.5% | +0.024 | ➡️ estable | -2.21$ | 0.50$ | ✅ activa |
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
| 2026-07-19T01:08 | FAVORITO_CONFIRMADO#SOL#60min | Solana Up or Down - July 18, 8PM ET… | ❌ LOSS | -1.95$ |
| 2026-07-19T01:05 | UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | Ethereum Up or Down - July 18, 8:45PM-9:00PM ET… | ✅ WIN | +0.27$ |
| 2026-07-19T01:05 | UPDOWN_GBM_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 18, 8:45PM-9:00PM ET… | ✅ WIN | +0.18$ |
| 2026-07-19T01:05 | BALLENAS_CONFIRMADAS_15M#SOL#15min | Solana Up or Down - July 18, 8:45PM-9:00PM ET… | ✅ WIN | +0.61$ |
| 2026-07-19T01:05 | BALLENAS_CONFIRMADAS_15M#ETH#15min | Ethereum Up or Down - July 18, 8:45PM-9:00PM ET… | ✅ WIN | +0.27$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-19T01:10 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,732.00 | 0.0min |  |
| ✅ ETH | $1,859.02 | 0.0min |  |
| ✅ SOL | $75.57 | 0.0min |  |
| ✅ XRP | $1.09 | 0.0min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,751.06 | consenso |  |
| ETH | $1,860.19 | consenso |  |
| SOL | $75.59 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*