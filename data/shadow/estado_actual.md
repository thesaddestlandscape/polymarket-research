# Estado del bot — 2026-07-23 14:02 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **28.11 $** |
| P&L real total | 🔴 **-23.11 $** |
| P&L real hoy | -1.24 $ |
| P&L real 7 días | -2.15 $ |
| Fees pagados (real) | 9.81 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3590.37 $ |
| P&L sim compuesto | 🟢 +6818.94 $ (ficción Kelly: +26804% s/ operativo) |
| P&L sim hoy (2026-07-23) | 🟢 +107.08 $ |
| Operaciones resueltas | 31018 (18616 WIN / 12402 LOSS) — 60.0% |
| Señales abiertas | 156 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 7147 | 59.5% | +0.095 | 📉 agota (-0.03) | +2208.90$ | 0.95$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4346 | 62.4% | +0.124 | 📉 agota (-0.04) | +2163.56$ | 1.24$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4356 | 57.8% | +0.078 | ➡️ estable | +1278.60$ | 0.78$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1372 | 66.5% | +0.164 | ➡️ estable | +636.41$ | 1.65$ | ✅ activa |
| UPDOWN_GBM | 2334 | 53.2% | +0.032 | 📈 madura (+0.11) | +208.43$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 242 | 60.7% | +0.107 | 📉 agota (-0.06) | +110.40$ | 1.07$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5422 | 68.8% | +0.188 | ➡️ estable | +98.31$ | 1.87$ | ✅ activa |
| WEEKLY_PRICE | 336 | 68.2% | +0.180 | 📈 madura (+0.21) | +67.16$ | 1.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 860 | 62.8% | +0.128 | ➡️ estable | +44.07$ | 1.28$ | ✅ activa |
| STREAK_FADE_15M | 270 | 58.5% | +0.085 | 📉 agota (-0.06) | +34.12$ | 0.85$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 131 | 79.4% | +0.289 | ➡️ estable | +24.29$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 289 | 82.4% | +0.321 | ➡️ estable | +18.81$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1659 | 51.2% | +0.012 | ➡️ estable | +11.80$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 264 | 51.1% | +0.011 | 📉 agota (-0.16) | +10.21$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 336 | 38.7% | -0.112 | ➡️ estable | +4.40$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 25 | 88.0% | +0.352 | — | +2.05$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 13 | 53.8% | +0.022 | — | +0.20$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 345 | 44.6% | -0.053 | 📉 agota (-0.15) | -4.85$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_5M | 401 | 46.9% | -0.031 | 📉 agota (-0.21) | -5.01$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 320 | 44.1% | -0.059 | 📉 agota (-0.08) | -26.41$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-23T13:54 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 23, 9:45AM-9:50AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-23T13:54 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 23, 9:40AM-9:45AM ET… | ✅ WIN | +0.49$ |
| 2026-07-23T13:51 | GBM_LATE_5M#BTC#5min | Bitcoin Up or Down - July 23, 9:40AM-9:45AM ET… | ✅ WIN | +1.52$ |
| 2026-07-23T13:51 | UPDOWN_GBM_15M_TARDIO#BNB#15min | BNB Up or Down - July 23, 9:30AM-9:45AM ET… | ✅ WIN | +1.12$ |
| 2026-07-23T13:51 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 23, 9:30AM-9:45AM ET… | ✅ WIN | +0.25$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-23T14:00 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,879.00 | 0.1min |  |
| ✅ ETH | $1,899.16 | 0.1min |  |
| ✅ SOL | $76.78 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,879.00 | consenso |  |
| ETH | $1,899.22 | consenso |  |
| SOL | $76.72 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*