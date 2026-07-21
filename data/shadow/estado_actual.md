# Estado del bot — 2026-07-21 23:38 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **23.93 $** |
| P&L real total | 🔴 **-27.29 $** |
| P&L real hoy | -2.20 $ |
| P&L real 7 días | -11.45 $ |
| Fees pagados (real) | 9.02 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3344.77 $ |
| P&L sim compuesto | 🟢 +6364.39 $ (ficción Kelly: +25017% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -51.09 $ |
| Operaciones resueltas | 27752 (16681 WIN / 11071 LOSS) — 60.1% |
| Señales abiertas | 128 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6664 | 59.9% | +0.099 | ➡️ estable | +2134.24$ | 0.99$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3860 | 63.3% | +0.133 | 📉 agota (-0.04) | +2063.18$ | 1.33$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3829 | 58.7% | +0.087 | ➡️ estable | +1238.99$ | 0.87$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1070 | 66.4% | +0.164 | ➡️ estable | +479.75$ | 1.64$ | ✅ activa |
| UPDOWN_GBM | 2106 | 52.8% | +0.028 | 📈 madura (+0.11) | +172.29$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 219 | 61.6% | +0.115 | 📉 agota (-0.05) | +105.11$ | 1.15$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4790 | 68.6% | +0.186 | ➡️ estable | +79.20$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| STREAK_FADE_15M | 259 | 57.9% | +0.079 | 📉 agota (-0.08) | +27.80$ | 0.79$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 110 | 80.0% | +0.295 | 📈 madura (+0.04) | +23.67$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 658 | 62.5% | +0.124 | 📉 agota (-0.06) | +20.27$ | 1.24$ | ✅ activa |
| GBM_LATE_5M | 263 | 48.7% | -0.013 | 📉 agota (-0.14) | +12.71$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 236 | 81.8% | +0.315 | ➡️ estable | +12.62$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 254 | 51.2% | +0.012 | 📉 agota (-0.16) | +10.81$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 8 | 50.0% | +0.000 | — | -0.26$ | 0.50$ | ✅ activa |
| BALLENAS_TARDIAS | 11 | 72.7% | +0.106 | — | -1.83$ | 1.06$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| LATE_WINDOW_5MIN | 256 | 45.7% | -0.043 | 📉 agota (-0.25) | -3.39$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-21T23:36 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 7:25PM-7:30PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T23:36 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 21, 7:15PM-7:30PM ET… | ❌ LOSS | -1.89$ |
| 2026-07-21T23:36 | UPDOWN_GBM_15M_TARDIO#XRP#15min | XRP Up or Down - July 21, 7:15PM-7:30PM ET… | ❌ LOSS | -1.73$ |
| 2026-07-21T23:36 | FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | Solana Up or Down - July 21, 7:15PM-7:30PM ET… | ✅ WIN | +0.80$ |
| 2026-07-21T23:36 | BALLENAS_CONFIRMADAS_15M#SOL#15min | Solana Up or Down - July 21, 7:15PM-7:30PM ET… | ✅ WIN | +0.80$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T23:36 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,385.24 | 0.1min |  |
| ✅ ETH | $1,921.76 | 0.1min |  |
| ✅ SOL | $78.03 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,385.50 | consenso |  |
| ETH | $1,921.78 | consenso |  |
| SOL | $77.94 | consenso |  |
| XRP | $1.14 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*