# Estado del bot — 2026-07-21 23:20 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **24.61 $** |
| P&L real total | 🔴 **-26.61 $** |
| P&L real hoy | -2.20 $ |
| P&L real 7 días | -11.45 $ |
| Fees pagados (real) | 9.02 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3356.78 $ |
| P&L sim compuesto | 🟢 +6371.81 $ (ficción Kelly: +25046% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -43.67 $ |
| Operaciones resueltas | 27715 (16665 WIN / 11050 LOSS) — 60.1% |
| Señales abiertas | 131 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6659 | 59.9% | +0.099 | ➡️ estable | +2138.11$ | 0.99$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3855 | 63.4% | +0.134 | 📉 agota (-0.04) | +2069.86$ | 1.34$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3824 | 58.7% | +0.087 | ➡️ estable | +1242.35$ | 0.87$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1066 | 66.5% | +0.165 | ➡️ estable | +478.94$ | 1.65$ | ✅ activa |
| UPDOWN_GBM | 2102 | 52.8% | +0.028 | 📈 madura (+0.11) | +171.77$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 218 | 61.9% | +0.118 | 📉 agota (-0.05) | +105.62$ | 1.18$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4785 | 68.5% | +0.185 | ➡️ estable | +73.23$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| STREAK_FADE_15M | 259 | 57.9% | +0.079 | 📉 agota (-0.08) | +27.80$ | 0.79$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 109 | 79.8% | +0.293 | 📈 madura (+0.04) | +22.23$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 655 | 62.4% | +0.124 | 📉 agota (-0.07) | +21.27$ | 1.24$ | ✅ activa |
| GBM_LATE_5M | 263 | 48.7% | -0.013 | 📉 agota (-0.14) | +12.71$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 235 | 81.7% | +0.314 | ➡️ estable | +11.82$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 254 | 51.2% | +0.012 | 📉 agota (-0.16) | +10.81$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 8 | 50.0% | +0.000 | — | -0.26$ | 0.50$ | ✅ activa |
| BALLENAS_TARDIAS | 11 | 72.7% | +0.106 | — | -1.83$ | 1.06$ | ✅ activa |
| LATE_WINDOW_5MIN | 253 | 46.2% | -0.037 | 📉 agota (-0.24) | -1.86$ | 0.50$ | ⚠️ IC negativo |
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
| 2026-07-21T23:18 | UPDOWN_GBM_15M_TARDIO#BNB#15min | BNB Up or Down - July 21, 7:00PM-7:15PM ET… | ✅ WIN | +2.17$ |
| 2026-07-21T23:18 | UPDOWN_GBM#BNB#15min | BNB Up or Down - July 21, 7:00PM-7:15PM ET… | ✅ WIN | +1.16$ |
| 2026-07-21T23:18 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 21, 7:00PM-7:15PM ET… | ✅ WIN | +2.17$ |
| 2026-07-21T23:18 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 21, 7:00PM-7:15PM ET… | ✅ WIN | +2.17$ |
| 2026-07-21T23:18 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 21, 7:00PM-7:15PM ET… | ✅ WIN | +2.17$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T23:18 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,288.01 | 0.1min |  |
| ✅ ETH | $1,918.31 | 0.1min |  |
| ✅ SOL | $77.87 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,288.01 | consenso |  |
| ETH | $1,918.33 | consenso |  |
| SOL | $77.83 | consenso |  |
| XRP | $1.14 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*