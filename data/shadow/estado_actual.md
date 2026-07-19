# Estado del bot — 2026-07-19 00:11 UTC

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
| P&L fiel (stake fijo 1$) | +2863.30 $ |
| P&L sim compuesto | 🟢 +5160.77 $ (ficción Kelly: +20286% s/ operativo) |
| P&L sim hoy (2026-07-19) | 🔴 -1.00 $ |
| Operaciones resueltas | 21557 (13001 WIN / 8556 LOSS) — 60.3% |
| Señales abiertas | 132 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 5669 | 60.5% | +0.105 | ➡️ estable | +1878.89$ | 1.05$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 2893 | 65.3% | +0.153 | ➡️ estable | +1727.09$ | 1.52$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 2841 | 60.2% | +0.101 | 📈 madura (+0.04) | +997.19$ | 1.02$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 538 | 67.7% | +0.176 | ➡️ estable | +225.02$ | 1.76$ | ✅ activa |
| UPDOWN_GBM | 1795 | 52.0% | +0.020 | 📈 madura (+0.13) | +127.54$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 165 | 66.7% | +0.165 | 📈 madura (+0.11) | +93.99$ | 1.65$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| FAVORITO_CONFIRMADO | 3600 | 68.4% | +0.184 | ➡️ estable | +37.05$ | 1.83$ | ✅ activa |
| STREAK_FADE_15M | 223 | 59.6% | +0.096 | ➡️ estable | +33.70$ | 0.96$ | ✅ activa |
| LATE_WINDOW_5MIN | 49 | 73.5% | +0.225 | ➡️ estable | +24.54$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 182 | 54.4% | +0.043 | 📉 agota (-0.12) | +15.01$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1630 | 51.3% | +0.013 | ➡️ estable | +14.21$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 243 | 63.4% | +0.133 | 📉 agota (-0.09) | +10.61$ | 1.33$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 55 | 78.2% | +0.272 | 📉 agota (-0.06) | +9.87$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 326 | 38.3% | -0.116 | ➡️ estable | +3.81$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 130 | 81.5% | +0.311 | ➡️ estable | +3.56$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 3 | 66.7% | +0.015 | — | +0.37$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_5M | 57 | 54.4% | +0.042 | ➡️ estable | -0.54$ | 0.50$ | ✅ activa |
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
| 2026-07-19T00:07 | FAVORITO_CONFIRMADO#XRP#5min | XRP Up or Down - July 18, 8:00PM-8:05PM ET… | ✅ WIN | +0.89$ |
| 2026-07-19T00:07 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 18, 8:00PM-8:05PM ET… | ✅ WIN | +0.40$ |
| 2026-07-19T00:07 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 18, 7:45PM-8:00PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-19T00:07 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 18, 7:45PM-8:00PM ET… | ✅ WIN | +2.13$ |
| 2026-07-19T00:07 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 18, 7:45PM-8:00PM ET… | ✅ WIN | +2.13$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-19T00:09 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,797.94 | 0.1min |  |
| ✅ ETH | $1,861.32 | 0.1min |  |
| ✅ SOL | $75.50 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,805.00 | consenso |  |
| ETH | $1,861.32 | consenso |  |
| SOL | $75.46 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*