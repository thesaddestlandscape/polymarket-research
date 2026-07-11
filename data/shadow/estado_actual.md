# Estado del bot — 2026-07-11 00:50 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **25.30 $** |
| P&L real total | 🔴 **-0.14 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | +17.32 $ |
| Fees pagados (real) | 7.27 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +819.11 $ |
| P&L sim compuesto | 🟢 +1277.13 $ (ficción Kelly: +5020% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🔴 -2.27 $ |
| Operaciones resueltas | 8393 (4655 WIN / 3738 LOSS) — 55.5% |
| Señales abiertas | 171 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3054 | 61.4% | +0.114 | ➡️ estable | +982.01$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 481 | 66.7% | +0.167 | ➡️ estable | +212.76$ | 1.67$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 598 | 56.9% | +0.068 | 📈 madura (+0.05) | +102.42$ | 0.68$ | ✅ activa |
| STREAK_FADE_15M | 121 | 62.0% | +0.118 | 📈 madura (+0.13) | +18.64$ | 1.18$ | ✅ activa |
| ORDER_FLOW_5M | 1572 | 51.3% | +0.013 | ➡️ estable | +17.51$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 248 | 37.9% | -0.120 | 📈 madura (+0.06) | +6.34$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 33 | 60.6% | +0.100 | 📈 madura (+0.18) | +4.99$ | 1.00$ | ✅ activa |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM | 1246 | 48.5% | -0.015 | ➡️ estable | -3.59$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 248 | 66.9% | +0.168 | 📉 agota (-0.08) | -4.29$ | 1.68$ | ✅ activa |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T00:46 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 10, 8:30PM-8:45PM ET… | ✅ WIN | +2.00$ |
| 2026-07-11T00:46 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 10, 8:30PM-8:45PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-11T00:46 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 10, 8:30PM-8:45PM ET… | ❌ LOSS | -1.07$ |
| 2026-07-11T00:46 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 10, 8:30PM-8:45PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-11T00:46 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 10, 8:30PM-8:45PM ET… | ✅ WIN | +1.75$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T00:50 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,058.08 | 0.1min |  |
| ✅ ETH | $1,791.16 | 0.1min |  |
| ✅ SOL | $77.81 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,058.08 | consenso |  |
| ETH | $1,791.16 | consenso |  |
| SOL | $77.78 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*