# Estado del bot — 2026-07-14 13:25 UTC

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
| P&L fiel (stake fijo 1$) | +1575.19 $ |
| P&L sim compuesto | 🟢 +2723.61 $ (ficción Kelly: +10706% s/ operativo) |
| P&L sim hoy (2026-07-14) | 🟢 +169.40 $ |
| Operaciones resueltas | 13830 (8008 WIN / 5822 LOSS) — 57.9% |
| Señales abiertas | 75 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4261 | 60.4% | +0.104 | ➡️ estable | +1338.84$ | 1.04$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1565 | 65.4% | +0.154 | ➡️ estable | +939.13$ | 1.54$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1497 | 58.2% | +0.082 | ➡️ estable | +407.16$ | 0.82$ | ✅ activa |
| UPDOWN_GBM | 1470 | 50.6% | +0.006 | 📈 madura (+0.08) | +59.51$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 101 | 59.4% | +0.092 | 📉 agota (-0.09) | +27.80$ | 0.92$ | ✅ activa |
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
| FAVORITO_CONFIRMADO | 1742 | 68.0% | +0.179 | ➡️ estable | -15.79$ | 1.79$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-14T13:20 | UPDOWN_GBM#BNB#15min | BNB Up or Down - July 14, 9:00AM-9:15AM ET… | ✅ WIN | +1.33$ |
| 2026-07-14T13:18 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 14, 9:00AM-9:15AM ET… | ❌ LOSS | -1.25$ |
| 2026-07-14T13:18 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 14, 9:00AM-9:15AM ET… | ✅ WIN | +0.19$ |
| 2026-07-14T13:18 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 14, 9:00AM-9:15AM ET… | ❌ LOSS | -1.31$ |
| 2026-07-14T13:18 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 14, 9:00AM-9:15AM ET… | ❌ LOSS | -1.90$ |

## Calidad de datos

⚠️ **DEGRADED** — última verificación 2026-07-14T13:24 UTC | rechazos 1h: 12 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,816.97 | 0.1min |  |
| ✅ ETH | $1,857.40 | 0.1min |  |
| ✅ SOL | $77.62 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,816.97 | consenso |  |
| ETH | $1,858.93 | consenso |  |
| SOL | $76.59 | consenso |  |
| XRP | $1.09 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:12 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*