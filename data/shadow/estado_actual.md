# Estado del bot — 2026-07-21 00:05 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **0.78 $** |
| P&L real total | 🔴 **-24.66 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -9.25 $ |
| Fees pagados (real) | 8.68 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3458.48 $ |
| P&L sim compuesto | 🟢 +6398.88 $ (ficción Kelly: +25153% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -16.60 $ |
| Operaciones resueltas | 25536 (15519 WIN / 10017 LOSS) — 60.8% |
| Señales abiertas | 104 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6309 | 60.5% | +0.105 | ➡️ estable | +2163.86$ | 1.05$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3513 | 64.9% | +0.149 | ➡️ estable | +2117.79$ | 1.49$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3492 | 59.8% | +0.098 | 📈 madura (+0.03) | +1249.99$ | 0.98$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 882 | 67.1% | +0.171 | ➡️ estable | +403.26$ | 1.71$ | ✅ activa |
| UPDOWN_GBM | 2006 | 52.3% | +0.023 | 📈 madura (+0.12) | +143.23$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 199 | 64.8% | +0.147 | 📈 madura (+0.04) | +105.97$ | 1.47$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4420 | 68.7% | +0.187 | ➡️ estable | +77.94$ | 1.87$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 242 | 59.9% | +0.098 | 📉 agota (-0.04) | +39.13$ | 0.98$ | ✅ activa |
| LATE_WINDOW_5MIN | 78 | 69.2% | +0.188 | 📉 agota (-0.05) | +30.95$ | 1.88$ | ✅ activa |
| GBM_LATE_5M | 219 | 56.2% | +0.061 | ➡️ estable | +23.10$ | 0.61$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 508 | 63.6% | +0.135 | ➡️ estable | +20.83$ | 1.35$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 91 | 79.1% | +0.285 | 📉 agota (-0.06) | +15.45$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 233 | 52.4% | +0.023 | 📉 agota (-0.14) | +14.03$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 198 | 82.8% | +0.325 | ➡️ estable | +13.60$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1638 | 51.2% | +0.012 | ➡️ estable | +13.23$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 6 | 66.7% | +0.037 | — | +0.87$ | 0.50$ | ⏳ acumulando |
| BALLENAS_TARDIAS | 3 | 100.0% | +0.045 | — | +0.51$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-21T00:04 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 20, 7:45PM-8:00PM ET… | ✅ WIN | +0.61$ |
| 2026-07-21T00:04 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 20, 7:45PM-8:00PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-21T00:04 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 20, 7:45PM-8:00PM ET… | ❌ LOSS | -1.30$ |
| 2026-07-21T00:04 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 20, 7:45PM-8:00PM ET… | ❌ LOSS | -1.38$ |
| 2026-07-21T00:04 | FAVORITO_CONFIRMADO#BTC#60min | Bitcoin Up or Down - July 20, 7PM ET… | ✅ WIN | +1.01$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T00:04 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,186.14 | 0.1min |  |
| ✅ ETH | $1,901.28 | 0.1min |  |
| ✅ SOL | $77.82 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,186.14 | consenso |  |
| ETH | $1,901.28 | consenso |  |
| SOL | $77.76 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*