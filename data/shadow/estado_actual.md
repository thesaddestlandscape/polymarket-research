# Estado del bot — 2026-07-14 13:30 UTC

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
| P&L fiel (stake fijo 1$) | +1581.88 $ |
| P&L sim compuesto | 🟢 +2734.57 $ (ficción Kelly: +10749% s/ operativo) |
| P&L sim hoy (2026-07-14) | 🟢 +180.37 $ |
| Operaciones resueltas | 13843 (8019 WIN / 5824 LOSS) — 57.9% |
| Señales abiertas | 64 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4264 | 60.5% | +0.105 | ➡️ estable | +1343.89$ | 1.04$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1568 | 65.4% | +0.154 | ➡️ estable | +939.91$ | 1.54$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1501 | 58.3% | +0.083 | ➡️ estable | +410.12$ | 0.83$ | ✅ activa |
| UPDOWN_GBM | 1470 | 50.6% | +0.006 | 📈 madura (+0.08) | +59.51$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 102 | 59.8% | +0.096 | 📉 agota (-0.09) | +28.34$ | 0.96$ | ✅ activa |
| STREAK_FADE_15M | 178 | 60.1% | +0.100 | 📈 madura (+0.12) | +18.42$ | 1.00$ | ✅ activa |
| LATE_WINDOW_5MIN | 39 | 71.8% | +0.207 | 📈 madura (+0.06) | +13.83$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1593 | 51.2% | +0.012 | ➡️ estable | +13.78$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 323 | 38.7% | -0.112 | ➡️ estable | +5.44$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 143 | 34.3% | -0.155 | 📉 agota (-0.13) | -1.21$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 219 | 59.4% | +0.093 | 📈 madura (+0.26) | -1.22$ | 0.93$ | ✅ activa |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 1744 | 68.0% | +0.180 | ➡️ estable | -14.15$ | 1.80$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-14T13:30 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 14, 9:15AM-9:30AM ET… | ✅ WIN | +1.44$ |
| 2026-07-14T13:30 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 14, 9:15AM-9:30AM ET… | ✅ WIN | +0.66$ |
| 2026-07-14T13:30 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 14, 9:15AM-9:30AM ET… | ✅ WIN | +0.84$ |
| 2026-07-14T13:30 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 14, 9:15AM-9:30AM ET… | ❌ LOSS | -1.50$ |
| 2026-07-14T13:30 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 14, 9:15AM-9:30AM ET… | ✅ WIN | +2.17$ |

## Calidad de datos

⚠️ **DEGRADED** — última verificación 2026-07-14T13:29 UTC | rechazos 1h: 14 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,896.81 | 0.1min |  |
| ✅ ETH | $1,878.21 | 0.1min |  |
| ✅ SOL | $77.35 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,896.81 | consenso |  |
| ETH | $1,878.21 | consenso |  |
| SOL | $77.35 | consenso |  |
| XRP | $1.10 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:14 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*