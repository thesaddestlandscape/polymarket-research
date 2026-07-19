# Estado del bot — 2026-07-19 11:55 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **0.78 $** |
| P&L real total | 🔴 **-24.66 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -17.21 $ |
| Fees pagados (real) | 8.68 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3009.83 $ |
| P&L sim compuesto | 🟢 +5458.37 $ (ficción Kelly: +21456% s/ operativo) |
| P&L sim hoy (2026-07-19) | 🟢 +296.60 $ |
| Operaciones resueltas | 22438 (13568 WIN / 8870 LOSS) — 60.5% |
| Señales abiertas | 126 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 5812 | 60.6% | +0.106 | ➡️ estable | +1962.85$ | 1.06$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3042 | 65.2% | +0.151 | ➡️ estable | +1818.02$ | 1.51$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 2989 | 60.0% | +0.099 | 📈 madura (+0.03) | +1046.21$ | 1.00$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 611 | 68.2% | +0.182 | ➡️ estable | +280.62$ | 1.82$ | ✅ activa |
| UPDOWN_GBM | 1822 | 52.0% | +0.020 | 📈 madura (+0.12) | +131.50$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 169 | 65.7% | +0.155 | 📈 madura (+0.07) | +92.12$ | 1.55$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| FAVORITO_CONFIRMADO | 3793 | 68.4% | +0.184 | ➡️ estable | +37.81$ | 1.84$ | ✅ activa |
| STREAK_FADE_15M | 225 | 59.6% | +0.095 | ➡️ estable | +33.25$ | 0.95$ | ✅ activa |
| LATE_WINDOW_5MIN | 49 | 73.5% | +0.225 | ➡️ estable | +24.54$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 298 | 64.4% | +0.143 | 📉 agota (-0.04) | +16.69$ | 1.43$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 192 | 53.6% | +0.036 | 📉 agota (-0.11) | +14.03$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1631 | 51.3% | +0.013 | ➡️ estable | +13.70$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 62 | 77.4% | +0.266 | 📉 agota (-0.06) | +9.34$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 149 | 81.9% | +0.315 | 📉 agota (-0.04) | +7.70$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 328 | 38.7% | -0.112 | ➡️ estable | +6.48$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_5M | 103 | 57.3% | +0.071 | ➡️ estable | +4.33$ | 0.71$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 5 | 60.0% | +0.018 | — | +0.32$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 149 | 32.9% | -0.169 | 📉 agota (-0.12) | -4.27$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-19T11:51 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 19, 7:30AM-7:45AM ET… | ✅ WIN | +2.08$ |
| 2026-07-19T11:51 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 19, 7:30AM-7:45AM ET… | ✅ WIN | +2.08$ |
| 2026-07-19T11:51 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 19, 7:30AM-7:45AM ET… | ✅ WIN | +2.08$ |
| 2026-07-19T11:51 | UPDOWN_GBM_15M_TARDIO#XRP#15min | XRP Up or Down - July 19, 7:30AM-7:45AM ET… | ✅ WIN | +2.08$ |
| 2026-07-19T11:51 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 19, 7:30AM-7:45AM ET… | ✅ WIN | +1.56$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-19T11:53 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,484.64 | 0.1min |  |
| ✅ ETH | $1,873.81 | 0.1min |  |
| ✅ SOL | $76.11 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,486.57 | consenso |  |
| ETH | $1,873.61 | consenso |  |
| SOL | $76.13 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*