# Estado del bot — 2026-07-15 01:01 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **7.10 $** |
| P&L real total | 🔴 **-18.34 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -16.38 $ |
| Fees pagados (real) | 8.21 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1617.97 $ |
| P&L sim compuesto | 🟢 +2827.77 $ (ficción Kelly: +11115% s/ operativo) |
| P&L sim hoy (2026-07-15) | 🟢 +19.13 $ |
| Operaciones resueltas | 14586 (8464 WIN / 6122 LOSS) — 58.0% |
| Señales abiertas | 52 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4420 | 60.2% | +0.102 | 📉 agota (-0.03) | +1348.99$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1702 | 65.4% | +0.154 | ➡️ estable | +997.97$ | 1.54$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1642 | 58.0% | +0.080 | ➡️ estable | +422.16$ | 0.80$ | ✅ activa |
| UPDOWN_GBM | 1513 | 50.8% | +0.008 | 📈 madura (+0.07) | +62.14$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 110 | 60.0% | +0.098 | 📉 agota (-0.07) | +30.61$ | 0.98$ | ✅ activa |
| STREAK_FADE_15M | 183 | 60.1% | +0.100 | 📈 madura (+0.10) | +20.99$ | 1.00$ | ✅ activa |
| LATE_WINDOW_5MIN | 41 | 73.2% | +0.221 | 📈 madura (+0.06) | +17.23$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1597 | 51.3% | +0.013 | ➡️ estable | +14.91$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 239 | 61.1% | +0.110 | 📈 madura (+0.27) | +7.74$ | 1.10$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 326 | 38.3% | -0.116 | ➡️ estable | +3.81$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_PYCONFIRMADO | 11 | 45.5% | -0.021 | — | +0.56$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_5M | 5 | 40.0% | -0.018 | — | -0.57$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_60M_PYCONFIRMADO | 4 | 0.0% | -0.067 | — | -2.04$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 146 | 33.6% | -0.162 | 📉 agota (-0.12) | -2.74$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 1948 | 67.9% | +0.179 | ➡️ estable | -11.90$ | 1.79$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-15T01:00 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 14, 8:45PM-9:00PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-15T01:00 | GBM_LATE_15M_PYCONFIRMADO#ETH#15min | Ethereum Up or Down - July 14, 8:45PM-9:00PM ET… | ✅ WIN | +0.16$ |
| 2026-07-15T01:00 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 14, 8:45PM-9:00PM ET… | ✅ WIN | +0.64$ |
| 2026-07-15T01:00 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 14, 8:45PM-9:00PM ET… | ✅ WIN | +0.16$ |
| 2026-07-15T01:00 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 14, 8:45PM-9:00PM ET… | ❌ LOSS | -1.29$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-15T01:00 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,785.54 | 0.1min |  |
| ✅ ETH | $1,880.24 | 0.1min |  |
| ✅ SOL | $77.58 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,790.50 | consenso |  |
| ETH | $1,880.77 | consenso |  |
| SOL | $77.64 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*