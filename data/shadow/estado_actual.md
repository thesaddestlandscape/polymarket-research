# Estado del bot — 2026-07-22 06:14 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **24.46 $** |
| P&L real total | 🔴 **-26.76 $** |
| P&L real hoy | +1.95 $ |
| P&L real 7 días | -7.64 $ |
| Fees pagados (real) | 9.10 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3376.68 $ |
| P&L sim compuesto | 🟢 +6393.50 $ (ficción Kelly: +25132% s/ operativo) |
| P&L sim hoy (2026-07-22) | 🟢 +29.99 $ |
| Operaciones resueltas | 28365 (17015 WIN / 11350 LOSS) — 60.0% |
| Señales abiertas | 143 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6751 | 59.7% | +0.097 | ➡️ estable | +2134.89$ | 0.97$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3947 | 62.9% | +0.129 | 📉 agota (-0.04) | +2069.32$ | 1.29$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3920 | 58.3% | +0.083 | ➡️ estable | +1230.63$ | 0.83$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1125 | 66.3% | +0.163 | 📉 agota (-0.04) | +503.44$ | 1.63$ | ✅ activa |
| UPDOWN_GBM | 2147 | 52.8% | +0.028 | 📈 madura (+0.11) | +179.42$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 224 | 61.2% | +0.111 | 📉 agota (-0.06) | +107.55$ | 1.11$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4908 | 68.6% | +0.186 | ➡️ estable | +74.99$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| STREAK_FADE_15M | 262 | 58.0% | +0.080 | 📉 agota (-0.08) | +28.71$ | 0.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 696 | 62.4% | +0.123 | 📉 agota (-0.04) | +24.98$ | 1.23$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 117 | 78.6% | +0.282 | ➡️ estable | +19.54$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 247 | 81.8% | +0.315 | ➡️ estable | +12.39$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1653 | 51.1% | +0.011 | ➡️ estable | +11.85$ | 0.50$ | ✅ activa |
| GBM_LATE_5M | 275 | 49.5% | -0.005 | 📉 agota (-0.12) | +10.22$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 257 | 51.0% | +0.010 | 📉 agota (-0.15) | +9.66$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 330 | 38.8% | -0.111 | ➡️ estable | +6.19$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 8 | 50.0% | +0.000 | — | -0.26$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 299 | 45.5% | -0.045 | 📉 agota (-0.16) | -0.68$ | 0.50$ | ⚠️ IC negativo |
| BALLENAS_TARDIAS | 13 | 76.9% | +0.152 | — | -1.30$ | 1.52$ | ✅ activa |
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
| 2026-07-22T06:09 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 22, 1:45AM-2:00AM ET… | ✅ WIN | +0.92$ |
| 2026-07-22T06:09 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 22, 1:45AM-2:00AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-22T06:09 | STREAK_FADE_15M#SOL#15min | Solana Up or Down - July 22, 1:45AM-2:00AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-22T06:09 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 22, 1:45AM-2:00AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-22T06:09 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 22, 1:45AM-2:00AM ET… | ❌ LOSS | -1.34$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-22T06:12 UTC | rechazos 1h: 3 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,865.57 | 0.1min |  |
| ✅ ETH | $1,917.69 | 0.1min |  |
| ✅ SOL | $77.30 | 0.1min |  |
| ✅ XRP | $1.13 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,865.57 | consenso |  |
| ETH | $1,917.69 | consenso |  |
| SOL | $77.26 | consenso |  |
| XRP | $1.13 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:3 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*