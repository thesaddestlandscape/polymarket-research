# Estado del bot — 2026-07-22 01:48 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **23.79 $** |
| P&L real total | 🔴 **-27.43 $** |
| P&L real hoy | +1.28 $ |
| P&L real 7 días | -8.31 $ |
| Fees pagados (real) | 9.06 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3362.81 $ |
| P&L sim compuesto | 🟢 +6383.53 $ (ficción Kelly: +25092% s/ operativo) |
| P&L sim hoy (2026-07-22) | 🟢 +20.02 $ |
| Operaciones resueltas | 27936 (16787 WIN / 11149 LOSS) — 60.1% |
| Señales abiertas | 136 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6695 | 59.8% | +0.098 | ➡️ estable | +2134.99$ | 0.98$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3890 | 63.2% | +0.132 | 📉 agota (-0.04) | +2066.53$ | 1.32$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3860 | 58.6% | +0.086 | ➡️ estable | +1238.59$ | 0.86$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1085 | 66.5% | +0.164 | ➡️ estable | +486.92$ | 1.64$ | ✅ activa |
| UPDOWN_GBM | 2115 | 52.7% | +0.027 | 📈 madura (+0.11) | +175.73$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 221 | 61.5% | +0.114 | 📉 agota (-0.06) | +106.22$ | 1.14$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4825 | 68.5% | +0.185 | ➡️ estable | +76.24$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| STREAK_FADE_15M | 260 | 58.1% | +0.080 | 📉 agota (-0.08) | +29.21$ | 0.80$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 112 | 80.4% | +0.298 | 📈 madura (+0.03) | +24.03$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 675 | 62.5% | +0.125 | 📉 agota (-0.05) | +22.77$ | 1.25$ | ✅ activa |
| GBM_LATE_5M | 264 | 48.9% | -0.011 | 📉 agota (-0.14) | +14.24$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 240 | 82.1% | +0.318 | ➡️ estable | +13.53$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1647 | 51.1% | +0.011 | ➡️ estable | +11.75$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 256 | 51.2% | +0.012 | 📉 agota (-0.15) | +10.84$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 8 | 50.0% | +0.000 | — | -0.26$ | 0.50$ | ✅ activa |
| BALLENAS_TARDIAS | 11 | 72.7% | +0.106 | — | -1.83$ | 1.06$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| LATE_WINDOW_5MIN | 257 | 45.5% | -0.044 | 📉 agota (-0.26) | -3.90$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-22T01:38 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 9:25PM-9:30PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-22T01:38 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 21, 9:15PM-9:30PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-22T01:38 | UPDOWN_GBM_15M_TARDIO#BNB#15min | BNB Up or Down - July 21, 9:15PM-9:30PM ET… | ✅ WIN | +1.63$ |
| 2026-07-22T01:38 | UPDOWN_GBM#BNB#15min | BNB Up or Down - July 21, 9:15PM-9:30PM ET… | ✅ WIN | +0.82$ |
| 2026-07-22T01:38 | BALLENAS_CONFIRMADAS_15M#XRP#15min | XRP Up or Down - July 21, 9:15PM-9:30PM ET… | ✅ WIN | +0.80$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-22T01:46 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,331.99 | 0.1min |  |
| ✅ ETH | $1,931.99 | 0.1min |  |
| ✅ SOL | $78.37 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,331.99 | consenso |  |
| ETH | $1,933.01 | consenso |  |
| SOL | $78.26 | consenso |  |
| XRP | $1.14 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*