# Estado del bot — 2026-07-22 08:45 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **26.57 $** |
| P&L real total | 🔴 **-24.65 $** |
| P&L real hoy | +4.06 $ |
| P&L real 7 días | -5.53 $ |
| Fees pagados (real) | 9.17 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3376.83 $ |
| P&L sim compuesto | 🟢 +6409.11 $ (ficción Kelly: +25193% s/ operativo) |
| P&L sim hoy (2026-07-22) | 🟢 +45.60 $ |
| Operaciones resueltas | 28609 (17158 WIN / 11451 LOSS) — 60.0% |
| Señales abiertas | 132 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6784 | 59.7% | +0.097 | ➡️ estable | +2135.27$ | 0.97$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3984 | 62.9% | +0.129 | 📉 agota (-0.05) | +2069.86$ | 1.29$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3960 | 58.3% | +0.083 | ➡️ estable | +1226.43$ | 0.83$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1153 | 66.3% | +0.162 | 📉 agota (-0.05) | +516.23$ | 1.62$ | ✅ activa |
| UPDOWN_GBM | 2169 | 52.8% | +0.028 | 📈 madura (+0.11) | +179.05$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 224 | 61.2% | +0.111 | 📉 agota (-0.06) | +107.55$ | 1.11$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4952 | 68.6% | +0.186 | ➡️ estable | +82.80$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| STREAK_FADE_15M | 262 | 58.0% | +0.080 | 📉 agota (-0.08) | +28.71$ | 0.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 707 | 62.4% | +0.123 | 📉 agota (-0.04) | +25.33$ | 1.23$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 119 | 79.0% | +0.285 | ➡️ estable | +20.13$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 249 | 81.9% | +0.317 | ➡️ estable | +13.07$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1653 | 51.1% | +0.011 | ➡️ estable | +11.85$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 257 | 51.0% | +0.010 | 📉 agota (-0.15) | +9.66$ | 0.50$ | ✅ activa |
| GBM_LATE_5M | 279 | 48.7% | -0.012 | 📉 agota (-0.14) | +8.18$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 330 | 38.8% | -0.111 | ➡️ estable | +6.19$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 11 | 45.5% | -0.021 | — | -0.76$ | 0.50$ | ⚠️ IC negativo |
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
| 2026-07-22T08:43 | GBM_LATE_5M#BTC#5min | Bitcoin Up or Down - July 22, 4:30AM-4:35AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-22T08:40 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 22, 4:15AM-4:30AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-22T08:40 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 22, 4:15AM-4:30AM ET… | ❌ LOSS | -1.82$ |
| 2026-07-22T08:40 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 22, 4:15AM-4:30AM ET… | ❌ LOSS | -1.48$ |
| 2026-07-22T08:40 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 22, 4:15AM-4:30AM ET… | ❌ LOSS | -1.56$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-22T08:43 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,916.00 | 0.0min |  |
| ✅ ETH | $1,918.71 | 0.0min |  |
| ✅ SOL | $77.31 | 0.0min |  |
| ✅ XRP | $1.13 | 0.0min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,917.43 | consenso |  |
| ETH | $1,918.69 | consenso |  |
| SOL | $77.30 | consenso |  |
| XRP | $1.13 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*