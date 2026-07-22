# Estado del bot — 2026-07-22 21:14 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **28.89 $** |
| P&L real total | 🔴 **-22.33 $** |
| P&L real hoy | +4.60 $ |
| P&L real 7 días | -4.99 $ |
| Fees pagados (real) | 9.62 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3538.24 $ |
| P&L sim compuesto | 🟢 +6694.33 $ (ficción Kelly: +26314% s/ operativo) |
| P&L sim hoy (2026-07-22) | 🟢 +330.82 $ |
| Operaciones resueltas | 29586 (17796 WIN / 11790 LOSS) — 60.2% |
| Señales abiertas | 142 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6937 | 59.7% | +0.097 | ➡️ estable | +2188.34$ | 0.97$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4136 | 63.0% | +0.130 | 📉 agota (-0.04) | +2163.00$ | 1.30$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4128 | 58.3% | +0.083 | ➡️ estable | +1274.47$ | 0.83$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1245 | 66.3% | +0.163 | 📉 agota (-0.03) | +566.73$ | 1.63$ | ✅ activa |
| UPDOWN_GBM | 2230 | 53.0% | +0.030 | 📈 madura (+0.11) | +191.69$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 232 | 61.6% | +0.115 | 📉 agota (-0.06) | +110.74$ | 1.15$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5152 | 68.8% | +0.187 | ➡️ estable | +90.11$ | 1.87$ | ✅ activa |
| WEEKLY_PRICE | 336 | 68.2% | +0.180 | 📈 madura (+0.21) | +67.16$ | 1.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 780 | 62.9% | +0.129 | 📉 agota (-0.03) | +36.95$ | 1.29$ | ✅ activa |
| STREAK_FADE_15M | 264 | 58.3% | +0.083 | 📉 agota (-0.07) | +31.16$ | 0.83$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 121 | 78.5% | +0.280 | ➡️ estable | +18.36$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 268 | 82.5% | +0.322 | ➡️ estable | +18.12$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1653 | 51.1% | +0.011 | ➡️ estable | +11.85$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 262 | 50.8% | +0.008 | 📉 agota (-0.17) | +9.12$ | 0.50$ | ✅ activa |
| GBM_LATE_5M | 288 | 48.3% | -0.017 | 📉 agota (-0.13) | +6.52$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 336 | 38.7% | -0.112 | ➡️ estable | +4.40$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| BALLENAS_TARDIAS | 17 | 82.4% | +0.246 | — | -0.16$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 11 | 45.5% | -0.021 | — | -0.76$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 323 | 45.5% | -0.045 | 📉 agota (-0.17) | -1.65$ | 0.50$ | ⚠️ IC negativo |
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
| 2026-07-22T21:09 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 22, 4:45PM-5:00PM ET… | ✅ WIN | +0.72$ |
| 2026-07-22T21:09 | FAVORITO_CONFIRMADO#SOL#60min | Solana Up or Down - July 22, 4PM ET… | ✅ WIN | +1.11$ |
| 2026-07-22T21:05 | UPDOWN_GBM_15M_TARDIO#XRP#15min | XRP Up or Down - July 22, 4:45PM-5:00PM ET… | ✅ WIN | +2.00$ |
| 2026-07-22T21:05 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 22, 4:45PM-5:00PM ET… | ✅ WIN | +2.00$ |
| 2026-07-22T21:05 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 22, 4:45PM-5:00PM ET… | ✅ WIN | +0.22$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-22T21:12 UTC | rechazos 1h: 3 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,886.49 | 0.1min |  |
| ✅ ETH | $1,927.97 | 0.1min |  |
| ✅ SOL | $77.76 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,900.40 | consenso |  |
| ETH | $1,927.97 | consenso |  |
| SOL | $77.76 | consenso |  |
| XRP | $1.14 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:3 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*