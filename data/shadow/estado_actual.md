# Estado del bot — 2026-07-17 13:08 UTC

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
| P&L fiel (stake fijo 1$) | +2303.93 $ |
| P&L sim compuesto | 🟢 +4080.10 $ (ficción Kelly: +16038% s/ operativo) |
| P&L sim hoy (2026-07-17) | 🟢 +359.04 $ |
| Operaciones resueltas | 18758 (11140 WIN / 7618 LOSS) — 59.4% |
| Señales abiertas | 91 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 5217 | 60.2% | +0.102 | ➡️ estable | +1635.38$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 2420 | 64.8% | +0.148 | ➡️ estable | +1397.48$ | 1.48$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 2397 | 59.6% | +0.096 | ➡️ estable | +760.84$ | 0.96$ | ✅ activa |
| UPDOWN_GBM | 1667 | 51.3% | +0.013 | 📈 madura (+0.11) | +93.77$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 276 | 67.0% | +0.169 | ➡️ estable | +88.80$ | 1.69$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 143 | 65.7% | +0.155 | 📈 madura (+0.15) | +76.20$ | 1.55$ | ✅ activa |
| STREAK_FADE_15M | 211 | 61.1% | +0.110 | 📈 madura (+0.04) | +39.54$ | 1.10$ | ✅ activa |
| WEEKLY_PRICE | 273 | 63.7% | +0.136 | 📈 madura (+0.26) | +29.85$ | 1.36$ | ✅ activa |
| LATE_WINDOW_5MIN | 47 | 74.5% | +0.235 | ➡️ estable | +24.66$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 158 | 56.3% | +0.062 | 📉 agota (-0.16) | +19.24$ | 0.62$ | ✅ activa |
| ORDER_FLOW_5M | 1624 | 51.2% | +0.012 | ➡️ estable | +13.36$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 31 | 80.6% | +0.288 | 📈 madura (+0.13) | +6.59$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 28 | 67.9% | +0.167 | — | +4.30$ | 1.67$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 326 | 38.3% | -0.116 | ➡️ estable | +3.81$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 78 | 82.1% | +0.312 | ➡️ estable | +3.50$ | 2.00$ | ✅ activa |
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
| FAVORITO_CONFIRMADO | 2986 | 67.8% | +0.178 | ➡️ estable | -26.66$ | 1.78$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-17T13:07 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 17, 8:45AM-9:00AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-17T13:02 | GBM_LATE_15M_PYCONFIRMADO#XRP#15min | XRP Up or Down - July 17, 8:45AM-9:00AM ET… | ✅ WIN | +2.17$ |
| 2026-07-17T13:02 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 17, 8:45AM-9:00AM ET… | ✅ WIN | +2.17$ |
| 2026-07-17T13:02 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 17, 8:45AM-9:00AM ET… | ✅ WIN | +3.59$ |
| 2026-07-17T13:02 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 17, 8:45AM-9:00AM ET… | ❌ LOSS | -0.97$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-17T13:06 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,941.01 | 0.1min |  |
| ✅ ETH | $1,824.95 | 0.1min |  |
| ✅ SOL | $73.87 | 0.1min |  |
| ✅ XRP | $1.07 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,941.01 | consenso |  |
| ETH | $1,825.10 | consenso |  |
| SOL | $74.22 | consenso |  |
| XRP | $1.08 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*