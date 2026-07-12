# Estado del bot — 2026-07-12 19:38 UTC

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
| P&L fiel (stake fijo 1$) | +1316.49 $ |
| P&L sim compuesto | 🟢 +2142.25 $ (ficción Kelly: +8421% s/ operativo) |
| P&L sim hoy (2026-07-12) | 🟢 +537.54 $ |
| Operaciones resueltas | 11340 (6489 WIN / 4851 LOSS) — 57.2% |
| Señales abiertas | 147 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3673 | 61.3% | +0.113 | ➡️ estable | +1218.81$ | 1.12$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1024 | 66.4% | +0.164 | ➡️ estable | +596.77$ | 1.64$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1175 | 58.0% | +0.079 | ➡️ estable | +285.20$ | 0.79$ | ✅ activa |
| STREAK_FADE_15M | 155 | 62.6% | +0.124 | 📈 madura (+0.18) | +25.15$ | 1.24$ | ✅ activa |
| UPDOWN_GBM | 1335 | 49.4% | -0.006 | 📈 madura (+0.06) | +23.91$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 71 | 63.4% | +0.130 | ➡️ estable | +21.20$ | 1.30$ | ✅ activa |
| FAVORITO_CONFIRMADO | 1011 | 68.5% | +0.185 | 📈 madura (+0.05) | +18.49$ | 1.85$ | ✅ activa |
| ORDER_FLOW_5M | 1586 | 51.3% | +0.013 | ➡️ estable | +16.48$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 315 | 38.7% | -0.112 | ➡️ estable | +7.27$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM | 138 | 34.8% | -0.150 | 📉 agota (-0.11) | +0.19$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 165 | 46.1% | -0.039 | ➡️ estable | -10.48$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 204 | 57.4% | +0.073 | 📈 madura (+0.24) | -13.93$ | 0.73$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-12T19:36 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 12, 3:15PM-3:30PM ET… | ✅ WIN | +0.41$ |
| 2026-07-12T19:36 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 12, 3:15PM-3:30PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-12T19:36 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 12, 3:15PM-3:30PM ET… | ❌ LOSS | -1.20$ |
| 2026-07-12T19:36 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 12, 3:15PM-3:30PM ET… | ❌ LOSS | -1.57$ |
| 2026-07-12T19:36 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 12, 3:15PM-3:30PM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-12T19:37 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,133.17 | 0.1min |  |
| ✅ ETH | $1,818.70 | 0.1min |  |
| ✅ SOL | $77.47 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,137.80 | consenso |  |
| ETH | $1,819.08 | consenso |  |
| SOL | $77.43 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*