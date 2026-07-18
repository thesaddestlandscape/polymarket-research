# Estado del bot — 2026-07-18 08:25 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **0.78 $** |
| P&L real total | 🔴 **-24.66 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -24.52 $ |
| Fees pagados (real) | 8.68 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +2645.16 $ |
| P&L sim compuesto | 🟢 +4727.58 $ (ficción Kelly: +18583% s/ operativo) |
| P&L sim hoy (2026-07-18) | 🟢 +222.82 $ |
| Operaciones resueltas | 20279 (12165 WIN / 8114 LOSS) — 60.0% |
| Señales abiertas | 94 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 5471 | 60.3% | +0.103 | ➡️ estable | +1764.03$ | 1.03$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 2677 | 65.0% | +0.150 | ➡️ estable | +1578.68$ | 1.50$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 2634 | 60.0% | +0.100 | 📈 madura (+0.04) | +901.27$ | 1.00$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 424 | 68.2% | +0.181 | ➡️ estable | +175.96$ | 1.81$ | ✅ activa |
| UPDOWN_GBM | 1746 | 51.8% | +0.018 | 📈 madura (+0.12) | +119.88$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 160 | 66.9% | +0.167 | 📈 madura (+0.11) | +93.77$ | 1.67$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| STREAK_FADE_15M | 217 | 60.8% | +0.107 | 📈 madura (+0.07) | +40.97$ | 1.07$ | ✅ activa |
| LATE_WINDOW_5MIN | 49 | 73.5% | +0.225 | ➡️ estable | +24.54$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 136 | 66.9% | +0.167 | 📈 madura (+0.04) | +22.59$ | 1.67$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 171 | 55.6% | +0.055 | 📉 agota (-0.13) | +17.74$ | 0.55$ | ✅ activa |
| ORDER_FLOW_5M | 1630 | 51.3% | +0.013 | ➡️ estable | +14.21$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 43 | 83.7% | +0.322 | 📈 madura (+0.14) | +13.58$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 104 | 81.7% | +0.311 | ➡️ estable | +4.31$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 326 | 38.3% | -0.116 | ➡️ estable | +3.81$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM_ETH_15M_HORA7 | 3 | 66.7% | +0.015 | — | +0.37$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_5M | 11 | 45.5% | -0.021 | — | -0.62$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 149 | 32.9% | -0.169 | 📉 agota (-0.12) | -4.27$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 3319 | 68.1% | +0.181 | ➡️ estable | -6.35$ | 1.80$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-18T08:22 | BALLENAS_CONFIRMADAS_15M#ETH#15min | Ethereum Up or Down - July 18, 4:00AM-4:15AM ET… | ❌ LOSS | -1.20$ |
| 2026-07-18T08:22 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 18, 4:00AM-4:15AM ET… | ❌ LOSS | -1.68$ |
| 2026-07-18T08:22 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 18, 4:00AM-4:15AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-18T08:22 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 18, 4:00AM-4:15AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-18T08:22 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 18, 4:00AM-4:15AM ET… | ❌ LOSS | -1.90$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-18T08:24 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,934.47 | 0.1min |  |
| ✅ ETH | $1,843.11 | 0.1min |  |
| ✅ SOL | $74.92 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,935.90 | consenso |  |
| ETH | $1,843.11 | consenso |  |
| SOL | $74.85 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*