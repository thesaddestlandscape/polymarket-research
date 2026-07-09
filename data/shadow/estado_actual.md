# Estado del bot — 2026-07-09 13:01 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **39.22 $** |
| P&L real total | 🟢 **+13.78 $** |
| P&L real hoy | +2.74 $ |
| P&L real 7 días | +6.59 $ |
| Fees pagados (real) | 6.10 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +482.01 $ |
| P&L sim compuesto | 🟢 +781.85 $ (ficción Kelly: +3073% s/ operativo) |
| P&L sim hoy (2026-07-09) | 🟢 +136.36 $ |
| Operaciones resueltas | 6274 (3375 WIN / 2899 LOSS) — 53.8% |
| Señales abiertas | 156 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2500 | 61.6% | +0.116 | 📈 madura (+0.05) | +827.91$ | 1.16$ | ✅ activa |
| ORDER_FLOW_5M | 1560 | 51.3% | +0.013 | ➡️ estable | +18.55$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 167 | 38.3% | -0.115 | 📈 madura (+0.16) | +9.01$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_ESPACIO_ATR | 29 | 79.3% | +0.274 | — | +8.68$ | 2.00$ | ✅ activa |
| LATE_WINDOW_5MIN | 31 | 67.7% | +0.167 | 📉 agota (-0.09) | +5.44$ | 1.67$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 56 | 60.7% | +0.103 | ➡️ estable | +5.27$ | 1.03$ | ✅ activa |
| STREAK_FADE_15M | 93 | 55.9% | +0.058 | 📈 madura (+0.07) | +3.82$ | 0.58$ | ✅ activa |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 4 | 75.0% | +0.033 | — | +0.99$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 129 | 34.1% | -0.156 | 📉 agota (-0.10) | -0.43$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 257 | 46.7% | -0.033 | 📉 agota (-0.08) | -14.17$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 144 | 52.1% | +0.021 | 📈 madura (+0.09) | -20.78$ | 0.50$ | ✅ activa |
| UPDOWN_GBM | 1162 | 47.8% | -0.022 | ➡️ estable | -28.46$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-09T12:56 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 9, 8:45AM-8:50AM ET… | ✅ WIN | +0.81$ |
| 2026-07-09T12:50 | UPDOWN_GBM#BTC#15min | Bitcoin Up or Down - July 9, 8:30AM-8:45AM ET… | ❌ LOSS | -1.13$ |
| 2026-07-09T12:49 | STREAK_MOM_5M#XRP#5min | XRP Up or Down - July 9, 8:40AM-8:45AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-09T12:49 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 9, 8:30AM-8:45AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-09T12:49 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 9, 8:30AM-8:45AM ET… | ❌ LOSS | -0.99$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-09T13:00 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,553.15 | 0.1min |  |
| ✅ ETH | $1,740.17 | 0.1min |  |
| ✅ SOL | $77.79 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,567.50 | consenso |  |
| ETH | $1,740.20 | consenso |  |
| SOL | $77.57 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*