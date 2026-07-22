# Estado del bot — 2026-07-22 14:47 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **28.47 $** |
| P&L real total | 🔴 **-22.75 $** |
| P&L real hoy | +3.46 $ |
| P&L real 7 días | -6.12 $ |
| Fees pagados (real) | 9.31 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3406.65 $ |
| P&L sim compuesto | 🟢 +6474.96 $ (ficción Kelly: +25452% s/ operativo) |
| P&L sim hoy (2026-07-22) | 🟢 +111.45 $ |
| Operaciones resueltas | 29041 (17419 WIN / 11622 LOSS) — 60.0% |
| Señales abiertas | 151 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6850 | 59.5% | +0.095 | 📉 agota (-0.03) | +2132.74$ | 0.95$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4047 | 62.8% | +0.128 | 📉 agota (-0.04) | +2088.61$ | 1.28$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4040 | 58.1% | +0.081 | ➡️ estable | +1231.73$ | 0.81$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1188 | 66.3% | +0.163 | 📉 agota (-0.04) | +538.89$ | 1.63$ | ✅ activa |
| UPDOWN_GBM | 2187 | 52.9% | +0.029 | 📈 madura (+0.11) | +185.28$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 227 | 61.2% | +0.111 | 📉 agota (-0.05) | +108.23$ | 1.11$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5052 | 68.7% | +0.187 | ➡️ estable | +91.45$ | 1.87$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 746 | 62.3% | +0.123 | ➡️ estable | +31.20$ | 1.23$ | ✅ activa |
| STREAK_FADE_15M | 262 | 58.0% | +0.080 | 📉 agota (-0.08) | +28.71$ | 0.80$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 119 | 79.0% | +0.285 | ➡️ estable | +20.13$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 260 | 82.3% | +0.321 | ➡️ estable | +16.88$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1653 | 51.1% | +0.011 | ➡️ estable | +11.85$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 258 | 50.8% | +0.008 | 📉 agota (-0.16) | +9.15$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 333 | 39.0% | -0.109 | ➡️ estable | +5.93$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_5M | 284 | 48.2% | -0.017 | 📉 agota (-0.13) | +5.25$ | 0.50$ | ⚠️ IC negativo |
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
| 2026-07-22T14:33 | UPDOWN_GBM_15M_TARDIO#DOGE#15min | Dogecoin Up or Down - July 22, 10:15AM-10:30AM ET… | ✅ WIN | +1.77$ |
| 2026-07-22T14:33 | UPDOWN_GBM#DOGE#15min | Dogecoin Up or Down - July 22, 10:15AM-10:30AM ET… | ✅ WIN | +0.49$ |
| 2026-07-22T14:33 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 22, 10:15AM-10:30AM ET… | ✅ WIN | +1.77$ |
| 2026-07-22T14:33 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 22, 10:15AM-10:30AM ET… | ✅ WIN | +1.77$ |
| 2026-07-22T14:33 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 22, 10:15AM-10:30AM ET… | ✅ WIN | +1.77$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-22T14:45 UTC | rechazos 1h: 4 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,684.60 | 0.1min |  |
| ✅ ETH | $1,927.87 | 0.1min |  |
| ✅ SOL | $77.67 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,684.60 | consenso |  |
| ETH | $1,928.52 | consenso |  |
| SOL | $77.74 | consenso |  |
| XRP | $1.14 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:4 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*