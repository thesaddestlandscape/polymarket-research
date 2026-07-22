# Estado del bot — 2026-07-22 06:51 UTC

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
| P&L fiel (stake fijo 1$) | +3383.06 $ |
| P&L sim compuesto | 🟢 +6409.71 $ (ficción Kelly: +25195% s/ operativo) |
| P&L sim hoy (2026-07-22) | 🟢 +46.20 $ |
| Operaciones resueltas | 28438 (17061 WIN / 11377 LOSS) — 60.0% |
| Señales abiertas | 136 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6761 | 59.7% | +0.097 | ➡️ estable | +2134.22$ | 0.97$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3959 | 62.9% | +0.129 | 📉 agota (-0.04) | +2066.21$ | 1.29$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3932 | 58.3% | +0.083 | ➡️ estable | +1226.93$ | 0.83$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1131 | 66.4% | +0.164 | 📉 agota (-0.04) | +512.56$ | 1.64$ | ✅ activa |
| UPDOWN_GBM | 2154 | 52.8% | +0.028 | 📈 madura (+0.11) | +180.15$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 224 | 61.2% | +0.111 | 📉 agota (-0.06) | +107.55$ | 1.11$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4920 | 68.7% | +0.187 | ➡️ estable | +88.11$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| STREAK_FADE_15M | 262 | 58.0% | +0.080 | 📉 agota (-0.08) | +28.71$ | 0.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 699 | 62.5% | +0.125 | 📉 agota (-0.03) | +26.32$ | 1.25$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 117 | 78.6% | +0.282 | ➡️ estable | +19.54$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 248 | 81.9% | +0.316 | ➡️ estable | +12.69$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1653 | 51.1% | +0.011 | ➡️ estable | +11.85$ | 0.50$ | ✅ activa |
| GBM_LATE_5M | 275 | 49.5% | -0.005 | 📉 agota (-0.12) | +10.22$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 257 | 51.0% | +0.010 | 📉 agota (-0.15) | +9.66$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 330 | 38.8% | -0.111 | ➡️ estable | +6.19$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 8 | 50.0% | +0.000 | — | -0.26$ | 0.50$ | ✅ activa |
| BALLENAS_TARDIAS | 13 | 76.9% | +0.152 | — | -1.30$ | 1.52$ | ✅ activa |
| LATE_WINDOW_5MIN | 308 | 45.1% | -0.048 | 📉 agota (-0.16) | -2.14$ | 0.50$ | ⚠️ IC negativo |
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
| 2026-07-22T06:50 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 22, 2:40AM-2:45AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-22T06:50 | FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | Solana Up or Down - July 22, 2:30AM-2:45AM ET… | ✅ WIN | +0.30$ |
| 2026-07-22T06:50 | BALLENAS_CONFIRMADAS_15M#SOL#15min | Solana Up or Down - July 22, 2:30AM-2:45AM ET… | ✅ WIN | +0.30$ |
| 2026-07-22T06:50 | UPDOWN_GBM_15M_TARDIO#SOL#15min | Solana Up or Down - July 22, 2:30AM-2:45AM ET… | ❌ LOSS | -0.62$ |
| 2026-07-22T06:50 | BALLENAS_CONFIRMADAS_15M#ETH#15min | Ethereum Up or Down - July 22, 2:30AM-2:45AM ET… | ✅ WIN | +0.61$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-22T06:49 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,910.01 | 0.1min |  |
| ✅ ETH | $1,916.83 | 0.1min |  |
| ✅ SOL | $77.19 | 0.1min |  |
| ✅ XRP | $1.13 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,910.10 | consenso |  |
| ETH | $1,916.83 | consenso |  |
| SOL | $77.24 | consenso |  |
| XRP | $1.13 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*