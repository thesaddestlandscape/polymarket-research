# Estado del bot — 2026-07-22 13:45 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **27.88 $** |
| P&L real total | 🔴 **-23.34 $** |
| P&L real hoy | +1.67 $ |
| P&L real 7 días | -7.92 $ |
| Fees pagados (real) | 9.24 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3403.50 $ |
| P&L sim compuesto | 🟢 +6457.79 $ (ficción Kelly: +25384% s/ operativo) |
| P&L sim hoy (2026-07-22) | 🟢 +94.28 $ |
| Operaciones resueltas | 28961 (17369 WIN / 11592 LOSS) — 60.0% |
| Señales abiertas | 141 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6838 | 59.6% | +0.096 | 📉 agota (-0.03) | +2135.59$ | 0.96$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4035 | 62.8% | +0.128 | 📉 agota (-0.04) | +2085.17$ | 1.28$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4025 | 58.2% | +0.082 | ➡️ estable | +1232.79$ | 0.82$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1181 | 66.2% | +0.162 | 📉 agota (-0.04) | +532.91$ | 1.62$ | ✅ activa |
| UPDOWN_GBM | 2183 | 52.9% | +0.029 | 📈 madura (+0.10) | +182.33$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 227 | 61.2% | +0.111 | 📉 agota (-0.05) | +108.23$ | 1.11$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5036 | 68.6% | +0.186 | ➡️ estable | +80.96$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 740 | 62.6% | +0.125 | ➡️ estable | +32.95$ | 1.25$ | ✅ activa |
| STREAK_FADE_15M | 262 | 58.0% | +0.080 | 📉 agota (-0.08) | +28.71$ | 0.80$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 119 | 79.0% | +0.285 | ➡️ estable | +20.13$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 259 | 82.2% | +0.320 | ➡️ estable | +16.76$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1653 | 51.1% | +0.011 | ➡️ estable | +11.85$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 257 | 51.0% | +0.010 | 📉 agota (-0.15) | +9.66$ | 0.50$ | ✅ activa |
| GBM_LATE_5M | 282 | 48.6% | -0.014 | 📉 agota (-0.13) | +6.27$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 332 | 38.9% | -0.111 | ➡️ estable | +5.44$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 11 | 45.5% | -0.021 | — | -0.76$ | 0.50$ | ⚠️ IC negativo |
| BALLENAS_TARDIAS | 14 | 78.6% | +0.175 | — | -1.02$ | 1.75$ | ✅ activa |
| LATE_WINDOW_5MIN | 320 | 45.0% | -0.050 | 📉 agota (-0.19) | -2.68$ | 0.50$ | ⚠️ IC negativo |
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
| 2026-07-22T13:38 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 22, 9:15AM-9:30AM ET… | ✅ WIN | +1.21$ |
| 2026-07-22T13:38 | BALLENAS_CONFIRMADAS_15M#SOL#15min | Solana Up or Down - July 22, 9:15AM-9:30AM ET… | ✅ WIN | +0.45$ |
| 2026-07-22T13:38 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 22, 9:15AM-9:30AM ET… | ✅ WIN | +0.68$ |
| 2026-07-22T13:38 | BALLENAS_CONFIRMADAS_15M#XRP#15min | XRP Up or Down - July 22, 9:15AM-9:30AM ET… | ✅ WIN | +0.68$ |
| 2026-07-22T13:38 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 22, 9:15AM-9:30AM ET… | ❌ LOSS | -1.33$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-22T13:43 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,844.48 | 0.1min |  |
| ✅ ETH | $1,935.94 | 0.1min |  |
| ✅ SOL | $77.79 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,848.40 | consenso |  |
| ETH | $1,935.94 | consenso |  |
| SOL | $77.73 | consenso |  |
| XRP | $1.14 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*