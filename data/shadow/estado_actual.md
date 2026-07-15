# Estado del bot — 2026-07-15 01:35 UTC

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
| P&L fiel (stake fijo 1$) | +1617.10 $ |
| P&L sim compuesto | 🟢 +2832.27 $ (ficción Kelly: +11133% s/ operativo) |
| P&L sim hoy (2026-07-15) | 🟢 +23.63 $ |
| Operaciones resueltas | 14616 (8480 WIN / 6136 LOSS) — 58.0% |
| Señales abiertas | 61 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4425 | 60.2% | +0.102 | 📉 agota (-0.03) | +1351.47$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1705 | 65.3% | +0.153 | ➡️ estable | +997.71$ | 1.53$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1646 | 58.0% | +0.080 | ➡️ estable | +424.88$ | 0.80$ | ✅ activa |
| UPDOWN_GBM | 1520 | 50.8% | +0.008 | 📈 madura (+0.08) | +66.00$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 111 | 60.4% | +0.102 | 📉 agota (-0.06) | +32.78$ | 1.02$ | ✅ activa |
| STREAK_FADE_15M | 183 | 60.1% | +0.100 | 📈 madura (+0.10) | +20.99$ | 1.00$ | ✅ activa |
| LATE_WINDOW_5MIN | 41 | 73.2% | +0.221 | 📈 madura (+0.06) | +17.23$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1600 | 51.2% | +0.012 | ➡️ estable | +13.76$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 239 | 61.1% | +0.110 | 📈 madura (+0.27) | +7.74$ | 1.10$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 326 | 38.3% | -0.116 | ➡️ estable | +3.81$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_PYCONFIRMADO | 12 | 41.7% | -0.043 | — | +0.05$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_5M | 5 | 40.0% | -0.018 | — | -0.57$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_60M_PYCONFIRMADO | 4 | 0.0% | -0.067 | — | -2.04$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 146 | 33.6% | -0.162 | 📉 agota (-0.12) | -2.74$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 1954 | 67.9% | +0.178 | ➡️ estable | -16.73$ | 1.78$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-15T01:33 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 14, 9:15PM-9:30PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-15T01:31 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 14, 9:15PM-9:30PM ET… | ✅ WIN | +1.92$ |
| 2026-07-15T01:31 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 14, 9:15PM-9:30PM ET… | ✅ WIN | +1.92$ |
| 2026-07-15T01:31 | GBM_LATE_15M_PYCONFIRMADO#SOL#15min | Solana Up or Down - July 14, 9:15PM-9:30PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-15T01:31 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 14, 9:15PM-9:30PM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-15T01:34 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,718.00 | 0.1min |  |
| ✅ ETH | $1,875.39 | 0.1min |  |
| ✅ SOL | $77.65 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,723.80 | consenso |  |
| ETH | $1,875.41 | consenso |  |
| SOL | $77.65 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*