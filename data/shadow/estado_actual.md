# Estado del bot — 2026-07-22 07:37 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **26.19 $** |
| P&L real total | 🔴 **-25.03 $** |
| P&L real hoy | +2.22 $ |
| P&L real 7 días | -7.37 $ |
| Fees pagados (real) | 9.14 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3374.77 $ |
| P&L sim compuesto | 🟢 +6398.56 $ (ficción Kelly: +25152% s/ operativo) |
| P&L sim hoy (2026-07-22) | 🟢 +35.05 $ |
| Operaciones resueltas | 28504 (17092 WIN / 11412 LOSS) — 60.0% |
| Señales abiertas | 140 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6770 | 59.7% | +0.097 | ➡️ estable | +2134.07$ | 0.97$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3970 | 62.8% | +0.128 | 📉 agota (-0.04) | +2065.16$ | 1.28$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3943 | 58.3% | +0.083 | ➡️ estable | +1223.58$ | 0.83$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1138 | 66.3% | +0.162 | 📉 agota (-0.05) | +512.43$ | 1.62$ | ✅ activa |
| UPDOWN_GBM | 2158 | 52.8% | +0.028 | 📈 madura (+0.10) | +180.33$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 224 | 61.2% | +0.111 | 📉 agota (-0.06) | +107.55$ | 1.11$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4932 | 68.6% | +0.186 | ➡️ estable | +82.41$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| STREAK_FADE_15M | 262 | 58.0% | +0.080 | 📉 agota (-0.08) | +28.71$ | 0.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 702 | 62.4% | +0.124 | 📉 agota (-0.03) | +25.38$ | 1.24$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 117 | 78.6% | +0.282 | ➡️ estable | +19.54$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 248 | 81.9% | +0.316 | ➡️ estable | +12.69$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1653 | 51.1% | +0.011 | ➡️ estable | +11.85$ | 0.50$ | ✅ activa |
| GBM_LATE_5M | 275 | 49.5% | -0.005 | 📉 agota (-0.12) | +10.22$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 257 | 51.0% | +0.010 | 📉 agota (-0.15) | +9.66$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 330 | 38.8% | -0.111 | ➡️ estable | +6.19$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 9 | 44.4% | -0.020 | — | -0.77$ | 0.50$ | ⚠️ IC negativo |
| BALLENAS_TARDIAS | 13 | 76.9% | +0.152 | — | -1.30$ | 1.52$ | ✅ activa |
| LATE_WINDOW_5MIN | 316 | 45.3% | -0.047 | 📉 agota (-0.18) | -1.65$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 316 | 44.3% | -0.057 | 📉 agota (-0.09) | -24.82$ | 0.50$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-22T07:36 | BALLENAS_CONFIRMADAS_15M#ETH#15min | Ethereum Up or Down - July 22, 3:15AM-3:30AM ET… | ❌ LOSS | -0.66$ |
| 2026-07-22T07:36 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 22, 3:15AM-3:30AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-22T07:36 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 22, 3:15AM-3:30AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-22T07:36 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 22, 3:15AM-3:30AM ET… | ✅ WIN | +1.52$ |
| 2026-07-22T07:36 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 22, 3:15AM-3:30AM ET… | ✅ WIN | +0.64$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-22T07:35 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,792.55 | 0.1min |  |
| ✅ ETH | $1,913.91 | 0.1min |  |
| ✅ SOL | $77.11 | 0.1min |  |
| ✅ XRP | $1.13 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,792.55 | consenso |  |
| ETH | $1,914.14 | consenso |  |
| SOL | $77.12 | consenso |  |
| XRP | $1.13 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*