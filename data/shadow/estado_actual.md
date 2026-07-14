# Estado del bot — 2026-07-14 15:01 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **7.10 $** |
| P&L real total | 🔴 **-18.34 $** |
| P&L real hoy | -2.93 $ |
| P&L real 7 días | -8.40 $ |
| Fees pagados (real) | 8.21 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1565.10 $ |
| P&L sim compuesto | 🟢 +2714.28 $ (ficción Kelly: +10669% s/ operativo) |
| P&L sim hoy (2026-07-14) | 🟢 +160.07 $ |
| Operaciones resueltas | 13933 (8061 WIN / 5872 LOSS) — 57.9% |
| Señales abiertas | 70 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4283 | 60.3% | +0.103 | ➡️ estable | +1328.73$ | 1.03$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1584 | 65.3% | +0.153 | ➡️ estable | +942.71$ | 1.53$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1521 | 58.1% | +0.080 | ➡️ estable | +406.07$ | 0.80$ | ✅ activa |
| UPDOWN_GBM | 1473 | 50.6% | +0.006 | 📈 madura (+0.08) | +61.76$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 104 | 59.6% | +0.094 | 📉 agota (-0.11) | +29.75$ | 0.94$ | ✅ activa |
| STREAK_FADE_15M | 178 | 60.1% | +0.100 | 📈 madura (+0.12) | +18.42$ | 1.00$ | ✅ activa |
| LATE_WINDOW_5MIN | 40 | 72.5% | +0.214 | 📈 madura (+0.05) | +15.23$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1593 | 51.2% | +0.012 | ➡️ estable | +13.78$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 324 | 38.6% | -0.113 | ➡️ estable | +4.84$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 143 | 34.3% | -0.155 | 📉 agota (-0.13) | -1.21$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 219 | 59.4% | +0.093 | 📈 madura (+0.26) | -1.22$ | 0.93$ | ✅ activa |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 1772 | 67.8% | +0.178 | ➡️ estable | -22.49$ | 1.78$ | ✅ activa |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-14T15:01 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 14, 10:45AM-11:00AM ET… | ✅ WIN | +2.00$ |
| 2026-07-14T15:01 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 14, 10:45AM-11:00AM ET… | ✅ WIN | +0.68$ |
| 2026-07-14T15:01 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 14, 10:45AM-11:00AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-14T15:01 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 14, 10:45AM-11:00AM ET… | ✅ WIN | +1.11$ |
| 2026-07-14T15:01 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 14, 10:45AM-11:00AM ET… | ❌ LOSS | -1.22$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-14T15:00 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,257.33 | 0.1min |  |
| ✅ ETH | $1,879.73 | 0.1min |  |
| ✅ SOL | $77.31 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,257.33 | consenso |  |
| ETH | $1,879.94 | consenso |  |
| SOL | $77.31 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*