# Estado del bot — 2026-07-13 01:20 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **14.44 $** |
| P&L real total | 🔴 **-11.00 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | +5.58 $ |
| Fees pagados (real) | 7.77 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1382.19 $ |
| P&L sim compuesto | 🟢 +2272.35 $ (ficción Kelly: +8932% s/ operativo) |
| P&L sim hoy (2026-07-13) | 🟢 +58.88 $ |
| Operaciones resueltas | 11717 (6735 WIN / 4982 LOSS) — 57.5% |
| Señales abiertas | 118 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3759 | 61.2% | +0.112 | ➡️ estable | +1239.99$ | 1.11$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1102 | 66.6% | +0.166 | ➡️ estable | +664.18$ | 1.66$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1227 | 58.3% | +0.083 | ➡️ estable | +313.69$ | 0.83$ | ✅ activa |
| UPDOWN_GBM | 1354 | 49.7% | -0.003 | 📈 madura (+0.08) | +32.88$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_15M | 160 | 62.5% | +0.123 | 📈 madura (+0.22) | +26.68$ | 1.23$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 76 | 63.2% | +0.128 | 📉 agota (-0.05) | +23.12$ | 1.28$ | ✅ activa |
| FAVORITO_CONFIRMADO | 1118 | 68.6% | +0.186 | 📈 madura (+0.06) | +18.53$ | 1.85$ | ✅ activa |
| ORDER_FLOW_5M | 1588 | 51.3% | +0.013 | ➡️ estable | +15.64$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 36 | 72.2% | +0.211 | ➡️ estable | +12.22$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 318 | 39.0% | -0.109 | ➡️ estable | +8.24$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM | 138 | 34.8% | -0.150 | 📉 agota (-0.11) | +0.19$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 184 | 47.3% | -0.027 | ➡️ estable | -11.96$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 204 | 57.4% | +0.073 | 📈 madura (+0.24) | -13.93$ | 0.73$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-13T01:18 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 12, 9:00PM-9:15PM ET… | ✅ WIN | +1.21$ |
| 2026-07-13T01:18 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 12, 9:00PM-9:15PM ET… | ❌ LOSS | -1.75$ |
| 2026-07-13T01:18 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 12, 9:00PM-9:15PM ET… | ✅ WIN | +1.21$ |
| 2026-07-13T01:16 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 12, 9:00PM-9:15PM ET… | ✅ WIN | +1.21$ |
| 2026-07-13T01:16 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 12, 9:00PM-9:15PM ET… | ✅ WIN | +1.92$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-13T01:19 UTC | rechazos 1h: 3 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,711.51 | 0.1min |  |
| ✅ ETH | $1,817.82 | 0.1min |  |
| ✅ SOL | $77.17 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,711.51 | consenso |  |
| ETH | $1,817.95 | consenso |  |
| SOL | $77.10 | consenso |  |
| XRP | $1.09 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:3 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*