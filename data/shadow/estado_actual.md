# Estado del bot — 2026-07-22 15:50 UTC

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
| P&L fiel (stake fijo 1$) | +3444.19 $ |
| P&L sim compuesto | 🟢 +6553.61 $ (ficción Kelly: +25761% s/ operativo) |
| P&L sim hoy (2026-07-22) | 🟢 +190.10 $ |
| Operaciones resueltas | 29135 (17495 WIN / 11640 LOSS) — 60.0% |
| Señales abiertas | 138 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6862 | 59.6% | +0.096 | 📉 agota (-0.03) | +2147.66$ | 0.96$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4063 | 62.9% | +0.129 | 📉 agota (-0.04) | +2114.86$ | 1.29$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4054 | 58.2% | +0.082 | ➡️ estable | +1249.11$ | 0.82$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1198 | 66.4% | +0.164 | 📉 agota (-0.04) | +550.08$ | 1.64$ | ✅ activa |
| UPDOWN_GBM | 2193 | 52.9% | +0.029 | 📈 madura (+0.11) | +186.45$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 229 | 61.6% | +0.115 | 📉 agota (-0.05) | +109.27$ | 1.15$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5070 | 68.8% | +0.188 | ➡️ estable | +95.19$ | 1.87$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 755 | 62.4% | +0.124 | ➡️ estable | +32.20$ | 1.23$ | ✅ activa |
| STREAK_FADE_15M | 262 | 58.0% | +0.080 | 📉 agota (-0.08) | +28.71$ | 0.80$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 119 | 79.0% | +0.285 | ➡️ estable | +20.13$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 263 | 82.5% | +0.323 | ➡️ estable | +18.78$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1653 | 51.1% | +0.011 | ➡️ estable | +11.85$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 260 | 51.2% | +0.011 | 📉 agota (-0.16) | +10.25$ | 0.50$ | ✅ activa |
| GBM_LATE_5M | 284 | 48.2% | -0.017 | 📉 agota (-0.13) | +5.25$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 335 | 38.8% | -0.111 | ➡️ estable | +4.91$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 11 | 45.5% | -0.021 | — | -0.76$ | 0.50$ | ⚠️ IC negativo |
| BALLENAS_TARDIAS | 15 | 80.0% | +0.199 | — | -0.90$ | 1.99$ | ✅ activa |
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
| 2026-07-22T15:49 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 22, 11:30AM-11:45AM ET… | ✅ WIN | +0.38$ |
| 2026-07-22T15:49 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 22, 11:30AM-11:45AM ET… | ✅ WIN | +1.23$ |
| 2026-07-22T15:49 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 22, 11:30AM-11:45AM ET… | ✅ WIN | +0.41$ |
| 2026-07-22T15:49 | UPDOWN_GBM_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 22, 11:30AM-11:45AM ET… | ✅ WIN | +1.50$ |
| 2026-07-22T15:49 | UPDOWN_GBM#ETH#15min | Ethereum Up or Down - July 22, 11:30AM-11:45AM ET… | ✅ WIN | +0.38$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-22T15:48 UTC | rechazos 1h: 3 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,947.90 | 0.1min |  |
| ✅ ETH | $1,941.90 | 0.1min |  |
| ✅ SOL | $78.51 | 0.1min |  |
| ✅ XRP | $1.15 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,948.20 | consenso |  |
| ETH | $1,941.90 | consenso |  |
| SOL | $78.45 | consenso |  |
| XRP | $1.15 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:3 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*