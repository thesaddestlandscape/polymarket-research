# Estado del bot — 2026-07-21 14:10 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 25.44 $ |
| Balance on-chain | **25.78 $** |
| P&L real total | 🟢 **+0.34 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -9.25 $ |
| Fees pagados (real) | 8.68 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3294.60 $ |
| P&L sim compuesto | 🟢 +6234.54 $ (ficción Kelly: +24507% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -180.94 $ |
| Operaciones resueltas | 26895 (16179 WIN / 10716 LOSS) — 60.2% |
| Señales abiertas | 124 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6531 | 59.9% | +0.099 | ➡️ estable | +2109.08$ | 0.99$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3727 | 63.5% | +0.135 | 📉 agota (-0.04) | +2033.55$ | 1.35$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3701 | 58.8% | +0.088 | ➡️ estable | +1210.51$ | 0.88$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 984 | 67.0% | +0.169 | 📉 agota (-0.03) | +452.09$ | 1.69$ | ✅ activa |
| UPDOWN_GBM | 2057 | 52.7% | +0.027 | 📈 madura (+0.11) | +170.83$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 212 | 62.3% | +0.121 | 📉 agota (-0.04) | +100.61$ | 1.21$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4642 | 68.5% | +0.185 | ➡️ estable | +70.76$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 256 | 58.2% | +0.081 | 📉 agota (-0.08) | +29.43$ | 0.81$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 103 | 79.6% | +0.290 | ➡️ estable | +19.56$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 251 | 51.0% | +0.010 | 📉 agota (-0.11) | +18.83$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 593 | 62.2% | +0.122 | 📉 agota (-0.04) | +13.24$ | 1.22$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 250 | 51.6% | +0.016 | 📉 agota (-0.15) | +11.79$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 222 | 81.5% | +0.312 | ➡️ estable | +10.71$ | 2.00$ | ✅ activa |
| LATE_WINDOW_5MIN | 208 | 50.0% | +0.000 | 📉 agota (-0.21) | +6.17$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 7 | 100.0% | +0.136 | — | +1.20$ | 1.36$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 8 | 50.0% | +0.000 | — | -0.26$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-21T14:09 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 21, 9:45AM-10:00AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-21T14:09 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 21, 9:45AM-10:00AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-21T14:09 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 21, 9:45AM-10:00AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-21T14:09 | FAVORITO_CONFIRMADO#SOL#60min | Solana Up or Down - July 21, 9AM ET… | ✅ WIN | +1.31$ |
| 2026-07-21T14:06 | UPDOWN_GBM_15M_TARDIO#BNB#15min | BNB Up or Down - July 21, 9:45AM-10:00AM ET… | ✅ WIN | +0.99$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T14:08 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,854.12 | 0.1min |  |
| ✅ ETH | $1,941.07 | 0.1min |  |
| ✅ SOL | $78.46 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,854.12 | consenso |  |
| ETH | $1,940.08 | consenso |  |
| SOL | $78.51 | consenso |  |
| XRP | $1.14 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*