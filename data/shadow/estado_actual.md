# Estado del bot — 2026-07-12 20:20 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **14.13 $** |
| P&L real total | 🔴 **-11.31 $** |
| P&L real hoy | -3.85 $ |
| P&L real 7 días | +6.15 $ |
| Fees pagados (real) | 7.67 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1339.83 $ |
| P&L sim compuesto | 🟢 +2189.25 $ (ficción Kelly: +8606% s/ operativo) |
| P&L sim hoy (2026-07-12) | 🟢 +584.54 $ |
| Operaciones resueltas | 11392 (6533 WIN / 4859 LOSS) — 57.3% |
| Señales abiertas | 138 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3685 | 61.3% | +0.113 | ➡️ estable | +1231.17$ | 1.13$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1035 | 66.7% | +0.166 | ➡️ estable | +612.47$ | 1.66$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1183 | 58.2% | +0.081 | ➡️ estable | +295.39$ | 0.81$ | ✅ activa |
| UPDOWN_GBM | 1339 | 49.4% | -0.006 | 📈 madura (+0.06) | +25.25$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_15M | 155 | 62.6% | +0.124 | 📈 madura (+0.18) | +25.15$ | 1.24$ | ✅ activa |
| FAVORITO_CONFIRMADO | 1026 | 68.7% | +0.187 | 📈 madura (+0.04) | +23.07$ | 1.86$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 71 | 63.4% | +0.130 | ➡️ estable | +21.20$ | 1.30$ | ✅ activa |
| ORDER_FLOW_5M | 1586 | 51.3% | +0.013 | ➡️ estable | +16.48$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 316 | 38.9% | -0.110 | ➡️ estable | +8.43$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM | 138 | 34.8% | -0.150 | 📉 agota (-0.11) | +0.19$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 166 | 46.4% | -0.036 | 📉 agota (-0.04) | -8.81$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 204 | 57.4% | +0.073 | 📈 madura (+0.24) | -13.93$ | 0.73$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-12T20:17 | STREAK_FADE_5M#XRP#5min | XRP Up or Down - July 12, 4:10PM-4:15PM ET… | ✅ WIN | +1.67$ |
| 2026-07-12T20:16 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 12, 4:00PM-4:15PM ET… | ✅ WIN | +0.10$ |
| 2026-07-12T20:16 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 12, 4:00PM-4:15PM ET… | ✅ WIN | +1.32$ |
| 2026-07-12T20:16 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 12, 4:00PM-4:15PM ET… | ✅ WIN | +0.92$ |
| 2026-07-12T20:16 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 12, 4:00PM-4:15PM ET… | ✅ WIN | +1.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-12T20:19 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,160.97 | 0.1min |  |
| ✅ ETH | $1,819.12 | 0.1min |  |
| ✅ SOL | $77.57 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,160.97 | consenso |  |
| ETH | $1,819.12 | consenso |  |
| SOL | $77.52 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*