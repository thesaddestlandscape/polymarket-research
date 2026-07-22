# Estado del bot — 2026-07-22 22:03 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **28.89 $** |
| P&L real total | 🔴 **-22.33 $** |
| P&L real hoy | +6.38 $ |
| P&L real 7 días | -3.21 $ |
| Fees pagados (real) | 9.62 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3535.89 $ |
| P&L sim compuesto | 🟢 +6693.68 $ (ficción Kelly: +26312% s/ operativo) |
| P&L sim hoy (2026-07-22) | 🟢 +330.17 $ |
| Operaciones resueltas | 29653 (17829 WIN / 11824 LOSS) — 60.1% |
| Señales abiertas | 145 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6948 | 59.7% | +0.097 | ➡️ estable | +2186.70$ | 0.97$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4148 | 62.9% | +0.129 | 📉 agota (-0.04) | +2158.30$ | 1.29$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4139 | 58.2% | +0.082 | ➡️ estable | +1274.37$ | 0.82$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1254 | 66.4% | +0.164 | 📉 agota (-0.03) | +572.50$ | 1.64$ | ✅ activa |
| UPDOWN_GBM | 2234 | 53.0% | +0.030 | 📈 madura (+0.11) | +191.00$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 233 | 61.4% | +0.113 | 📉 agota (-0.06) | +110.23$ | 1.13$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5160 | 68.7% | +0.187 | ➡️ estable | +88.58$ | 1.87$ | ✅ activa |
| WEEKLY_PRICE | 336 | 68.2% | +0.180 | 📈 madura (+0.21) | +67.16$ | 1.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 781 | 63.0% | +0.130 | 📉 agota (-0.03) | +37.75$ | 1.30$ | ✅ activa |
| STREAK_FADE_15M | 264 | 58.3% | +0.083 | 📉 agota (-0.07) | +31.16$ | 0.83$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 123 | 78.9% | +0.284 | ➡️ estable | +20.70$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 270 | 82.2% | +0.320 | ➡️ estable | +16.27$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1653 | 51.1% | +0.011 | ➡️ estable | +11.85$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 262 | 50.8% | +0.008 | 📉 agota (-0.17) | +9.12$ | 0.50$ | ✅ activa |
| GBM_LATE_5M | 293 | 48.1% | -0.019 | 📉 agota (-0.14) | +7.48$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 336 | 38.7% | -0.112 | ➡️ estable | +4.40$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| BALLENAS_TARDIAS | 17 | 82.4% | +0.246 | — | -0.16$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 11 | 45.5% | -0.021 | — | -0.76$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 324 | 45.7% | -0.043 | 📉 agota (-0.16) | -1.15$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 317 | 44.2% | -0.058 | 📉 agota (-0.09) | -25.33$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-22T21:59 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 22, 5:50PM-5:55PM ET… | ✅ WIN | +1.27$ |
| 2026-07-22T21:56 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 22, 5:45PM-5:50PM ET… | ✅ WIN | +0.50$ |
| 2026-07-22T21:49 | UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | Bitcoin Up or Down - July 22, 5:30PM-5:45PM ET… | ✅ WIN | +1.01$ |
| 2026-07-22T21:49 | UPDOWN_GBM_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 22, 5:30PM-5:45PM ET… | ✅ WIN | +0.74$ |
| 2026-07-22T21:49 | UPDOWN_GBM#BTC#15min | Bitcoin Up or Down - July 22, 5:30PM-5:45PM ET… | ✅ WIN | +1.00$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-22T22:01 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,019.46 | 0.1min |  |
| ✅ ETH | $1,937.88 | 0.1min |  |
| ✅ SOL | $77.93 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,019.46 | consenso |  |
| ETH | $1,937.88 | consenso |  |
| SOL | $77.97 | consenso |  |
| XRP | $1.14 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*