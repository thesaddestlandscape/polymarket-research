# Estado del bot — 2026-07-13 00:32 UTC

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
| P&L fiel (stake fijo 1$) | +1377.85 $ |
| P&L sim compuesto | 🟢 +2261.76 $ (ficción Kelly: +8891% s/ operativo) |
| P&L sim hoy (2026-07-13) | 🟢 +48.29 $ |
| Operaciones resueltas | 11658 (6697 WIN / 4961 LOSS) — 57.4% |
| Señales abiertas | 115 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3745 | 61.3% | +0.112 | ➡️ estable | +1247.97$ | 1.12$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1090 | 66.6% | +0.166 | ➡️ estable | +658.73$ | 1.66$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1220 | 58.2% | +0.082 | 📈 madura (+0.03) | +308.45$ | 0.82$ | ✅ activa |
| UPDOWN_GBM | 1351 | 49.7% | -0.003 | 📈 madura (+0.08) | +31.81$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_15M | 160 | 62.5% | +0.123 | 📈 madura (+0.22) | +26.68$ | 1.23$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 76 | 63.2% | +0.128 | 📉 agota (-0.05) | +23.12$ | 1.28$ | ✅ activa |
| ORDER_FLOW_5M | 1586 | 51.3% | +0.013 | ➡️ estable | +16.48$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 36 | 72.2% | +0.211 | ➡️ estable | +12.22$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 318 | 39.0% | -0.109 | ➡️ estable | +8.24$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 1103 | 68.2% | +0.181 | 📈 madura (+0.05) | +6.74$ | 1.81$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM | 138 | 34.8% | -0.150 | 📉 agota (-0.11) | +0.19$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 178 | 47.8% | -0.022 | ➡️ estable | -7.82$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 204 | 57.4% | +0.073 | 📈 madura (+0.24) | -13.93$ | 0.73$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-13T00:30 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 12, 8:15PM-8:30PM ET… | ✅ WIN | +0.72$ |
| 2026-07-13T00:30 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 12, 8:15PM-8:30PM ET… | ❌ LOSS | -1.94$ |
| 2026-07-13T00:30 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 12, 8:15PM-8:30PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-13T00:30 | STREAK_FADE_15M#SOL#15min | Solana Up or Down - July 12, 8:15PM-8:30PM ET… | ✅ WIN | +1.84$ |
| 2026-07-13T00:18 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 12, 8:10PM-8:15PM ET… | ✅ WIN | +1.92$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-13T00:31 UTC | rechazos 1h: 4 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,148.67 | 0.1min |  |
| ✅ ETH | $1,831.79 | 0.1min |  |
| ✅ SOL | $77.62 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,155.90 | consenso |  |
| ETH | $1,831.79 | consenso |  |
| SOL | $77.70 | consenso |  |
| XRP | $1.10 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:4 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*