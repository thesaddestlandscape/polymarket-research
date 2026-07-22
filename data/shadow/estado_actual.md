# Estado del bot — 2026-07-22 16:10 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **28.95 $** |
| P&L real total | 🔴 **-22.27 $** |
| P&L real hoy | +6.44 $ |
| P&L real 7 días | -3.15 $ |
| Fees pagados (real) | 9.37 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3462.16 $ |
| P&L sim compuesto | 🟢 +6580.07 $ (ficción Kelly: +25865% s/ operativo) |
| P&L sim hoy (2026-07-22) | 🟢 +216.56 $ |
| Operaciones resueltas | 29179 (17532 WIN / 11647 LOSS) — 60.1% |
| Señales abiertas | 145 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6868 | 59.6% | +0.096 | 📉 agota (-0.03) | +2152.66$ | 0.96$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4066 | 62.9% | +0.129 | 📉 agota (-0.04) | +2120.43$ | 1.29$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4060 | 58.3% | +0.083 | ➡️ estable | +1256.23$ | 0.83$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1201 | 66.5% | +0.165 | 📉 agota (-0.04) | +552.87$ | 1.65$ | ✅ activa |
| UPDOWN_GBM | 2194 | 53.0% | +0.030 | 📈 madura (+0.11) | +187.05$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 229 | 61.6% | +0.115 | 📉 agota (-0.05) | +109.27$ | 1.15$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5077 | 68.7% | +0.187 | ➡️ estable | +93.39$ | 1.87$ | ✅ activa |
| WEEKLY_PRICE | 334 | 68.3% | +0.182 | 📈 madura (+0.21) | +68.72$ | 1.81$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 757 | 62.5% | +0.125 | ➡️ estable | +33.39$ | 1.25$ | ✅ activa |
| STREAK_FADE_15M | 263 | 58.2% | +0.081 | 📉 agota (-0.07) | +30.04$ | 0.81$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 119 | 79.0% | +0.285 | ➡️ estable | +20.13$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 263 | 82.5% | +0.323 | ➡️ estable | +18.78$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1653 | 51.1% | +0.011 | ➡️ estable | +11.85$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 261 | 51.0% | +0.010 | 📉 agota (-0.16) | +9.68$ | 0.50$ | ✅ activa |
| GBM_LATE_5M | 284 | 48.2% | -0.017 | 📉 agota (-0.13) | +5.25$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 335 | 38.8% | -0.111 | ➡️ estable | +4.91$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| BALLENAS_TARDIAS | 16 | 81.2% | +0.222 | — | -0.59$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 11 | 45.5% | -0.021 | — | -0.76$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 322 | 45.3% | -0.046 | 📉 agota (-0.17) | -1.93$ | 0.50$ | ⚠️ IC negativo |
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
| 2026-07-22T16:08 | BALLENAS_TARDIAS#BTC#15min | … | ✅ WIN | +0.31$ |
| 2026-07-22T16:08 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 22, 11:45AM-12:00PM ET… | ✅ WIN | +2.56$ |
| 2026-07-22T16:08 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 22, 11:45AM-12:00PM ET… | ✅ WIN | +2.00$ |
| 2026-07-22T16:08 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 22, 11:45AM-12:00PM ET… | ✅ WIN | +2.07$ |
| 2026-07-22T16:08 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 22, 11:45AM-12:00PM ET… | ✅ WIN | +1.84$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-22T16:07 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,045.26 | 0.1min |  |
| ✅ ETH | $1,942.57 | 0.1min |  |
| ✅ SOL | $78.53 | 0.1min |  |
| ✅ XRP | $1.15 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,050.00 | consenso |  |
| ETH | $1,942.79 | consenso |  |
| SOL | $78.46 | consenso |  |
| XRP | $1.15 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*