# Estado del bot — 2026-07-12 22:33 UTC

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
| P&L fiel (stake fijo 1$) | +1356.97 $ |
| P&L sim compuesto | 🟢 +2221.34 $ (ficción Kelly: +8732% s/ operativo) |
| P&L sim hoy (2026-07-12) | 🟢 +616.63 $ |
| Operaciones resueltas | 11525 (6620 WIN / 4905 LOSS) — 57.4% |
| Señales abiertas | 151 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3716 | 61.3% | +0.113 | ➡️ estable | +1240.53$ | 1.13$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1064 | 66.4% | +0.164 | ➡️ estable | +617.32$ | 1.64$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1205 | 58.3% | +0.082 | 📈 madura (+0.03) | +305.32$ | 0.82$ | ✅ activa |
| UPDOWN_GBM | 1345 | 49.6% | -0.004 | 📈 madura (+0.07) | +29.17$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 1062 | 68.9% | +0.189 | 📈 madura (+0.07) | +28.61$ | 1.89$ | ✅ activa |
| STREAK_FADE_15M | 156 | 62.2% | +0.120 | 📈 madura (+0.19) | +23.27$ | 1.20$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 71 | 63.4% | +0.130 | ➡️ estable | +21.20$ | 1.30$ | ✅ activa |
| ORDER_FLOW_5M | 1586 | 51.3% | +0.013 | ➡️ estable | +16.48$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 317 | 38.8% | -0.111 | ➡️ estable | +7.10$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM | 138 | 34.8% | -0.150 | 📉 agota (-0.11) | +0.19$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 173 | 47.4% | -0.026 | ➡️ estable | -7.09$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 204 | 57.4% | +0.073 | 📈 madura (+0.24) | -13.93$ | 0.73$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-12T22:32 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 12, 6:15PM-6:30PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-12T22:32 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 12, 6:15PM-6:30PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-12T22:32 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 12, 6:15PM-6:30PM ET… | ❌ LOSS | -1.78$ |
| 2026-07-12T22:32 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 12, 6:15PM-6:30PM ET… | ❌ LOSS | -1.63$ |
| 2026-07-12T22:32 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 12, 6:15PM-6:30PM ET… | ✅ WIN | +2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-12T22:32 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,800.11 | 0.1min |  |
| ✅ ETH | $1,802.46 | 0.1min |  |
| ✅ SOL | $76.72 | 0.1min |  |
| ✅ XRP | $1.08 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,809.10 | consenso |  |
| ETH | $1,802.46 | consenso |  |
| SOL | $76.74 | consenso |  |
| XRP | $1.08 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*