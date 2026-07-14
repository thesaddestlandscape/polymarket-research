# Estado del bot — 2026-07-14 19:25 UTC

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
| P&L fiel (stake fijo 1$) | +1592.20 $ |
| P&L sim compuesto | 🟢 +2771.30 $ (ficción Kelly: +10893% s/ operativo) |
| P&L sim hoy (2026-07-14) | 🟢 +217.09 $ |
| Operaciones resueltas | 14215 (8233 WIN / 5982 LOSS) — 57.9% |
| Señales abiertas | 84 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4344 | 60.2% | +0.102 | 📉 agota (-0.03) | +1336.15$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1634 | 65.4% | +0.153 | ➡️ estable | +969.00$ | 1.53$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1578 | 58.0% | +0.080 | ➡️ estable | +425.34$ | 0.80$ | ✅ activa |
| UPDOWN_GBM | 1486 | 50.8% | +0.008 | 📈 madura (+0.07) | +68.07$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 106 | 58.5% | +0.083 | 📉 agota (-0.15) | +27.15$ | 0.83$ | ✅ activa |
| STREAK_FADE_15M | 178 | 60.1% | +0.100 | 📈 madura (+0.12) | +18.42$ | 1.00$ | ✅ activa |
| LATE_WINDOW_5MIN | 41 | 73.2% | +0.221 | 📈 madura (+0.06) | +17.23$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1593 | 51.2% | +0.012 | ➡️ estable | +13.78$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 239 | 61.1% | +0.110 | 📈 madura (+0.27) | +7.74$ | 1.10$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 326 | 38.3% | -0.116 | ➡️ estable | +3.81$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 146 | 33.6% | -0.162 | 📉 agota (-0.12) | -2.74$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 1845 | 67.6% | +0.176 | ➡️ estable | -30.57$ | 1.76$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-14T19:18 | UPDOWN_GBM#DOGE#15min | Dogecoin Up or Down - July 14, 3:00PM-3:15PM ET… | ❌ LOSS | -1.14$ |
| 2026-07-14T19:16 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 14, 3:10PM-3:15PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-14T19:16 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 14, 3:10PM-3:15PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-14T19:16 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 14, 3:00PM-3:15PM ET… | ✅ WIN | +1.54$ |
| 2026-07-14T19:16 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 14, 3:00PM-3:15PM ET… | ✅ WIN | +1.87$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-14T19:24 UTC | rechazos 1h: 5 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,626.47 | 0.1min |  |
| ✅ ETH | $1,878.69 | 0.1min |  |
| ✅ SOL | $77.44 | 0.1min |  |
| ✅ XRP | $1.12 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,626.47 | consenso |  |
| ETH | $1,878.69 | consenso |  |
| SOL | $77.42 | consenso |  |
| XRP | $1.12 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:5 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*