# Estado del bot — 2026-07-14 15:47 UTC

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
| P&L fiel (stake fijo 1$) | +1570.35 $ |
| P&L sim compuesto | 🟢 +2726.88 $ (ficción Kelly: +10719% s/ operativo) |
| P&L sim hoy (2026-07-14) | 🟢 +172.67 $ |
| Operaciones resueltas | 13974 (8087 WIN / 5887 LOSS) — 57.9% |
| Señales abiertas | 79 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4294 | 60.2% | +0.102 | ➡️ estable | +1319.39$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1590 | 65.5% | +0.155 | ➡️ estable | +951.33$ | 1.54$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1531 | 58.0% | +0.080 | ➡️ estable | +407.89$ | 0.80$ | ✅ activa |
| UPDOWN_GBM | 1476 | 50.7% | +0.007 | 📈 madura (+0.08) | +66.37$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 104 | 59.6% | +0.094 | 📉 agota (-0.11) | +29.75$ | 0.94$ | ✅ activa |
| STREAK_FADE_15M | 178 | 60.1% | +0.100 | 📈 madura (+0.12) | +18.42$ | 1.00$ | ✅ activa |
| LATE_WINDOW_5MIN | 41 | 73.2% | +0.221 | 📈 madura (+0.06) | +17.23$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1593 | 51.2% | +0.012 | ➡️ estable | +13.78$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 324 | 38.6% | -0.113 | ➡️ estable | +4.84$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 143 | 34.3% | -0.155 | 📉 agota (-0.13) | -1.21$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 219 | 59.4% | +0.093 | 📈 madura (+0.26) | -1.22$ | 0.93$ | ✅ activa |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 1782 | 67.9% | +0.179 | ➡️ estable | -17.60$ | 1.79$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-14T15:45 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 14, 11:30AM-11:45AM ET… | ✅ WIN | +0.19$ |
| 2026-07-14T15:45 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 14, 11:30AM-11:45AM ET… | ✅ WIN | +2.17$ |
| 2026-07-14T15:45 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 14, 11:30AM-11:45AM ET… | ✅ WIN | +1.44$ |
| 2026-07-14T15:45 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 14, 11:30AM-11:45AM ET… | ❌ LOSS | -1.62$ |
| 2026-07-14T15:39 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 14, 11:30AM-11:35AM ET… | ✅ WIN | +2.00$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-14T15:46 UTC | rechazos 1h: 4 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,748.00 | 0.1min |  |
| ✅ ETH | $1,879.31 | 0.1min |  |
| ✅ SOL | $77.54 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,748.00 | consenso |  |
| ETH | $1,879.72 | consenso |  |
| SOL | $77.45 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:4 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*