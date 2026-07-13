# Estado del bot — 2026-07-13 00:54 UTC

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
| P&L fiel (stake fijo 1$) | +1386.90 $ |
| P&L sim compuesto | 🟢 +2278.38 $ (ficción Kelly: +8956% s/ operativo) |
| P&L sim hoy (2026-07-13) | 🟢 +64.91 $ |
| Operaciones resueltas | 11686 (6718 WIN / 4968 LOSS) — 57.5% |
| Señales abiertas | 122 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3751 | 61.3% | +0.113 | ➡️ estable | +1250.59$ | 1.13$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1094 | 66.7% | +0.167 | ➡️ estable | +666.19$ | 1.67$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1223 | 58.3% | +0.083 | 📈 madura (+0.03) | +313.10$ | 0.83$ | ✅ activa |
| UPDOWN_GBM | 1353 | 49.7% | -0.003 | 📈 madura (+0.08) | +33.39$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_15M | 160 | 62.5% | +0.123 | 📈 madura (+0.22) | +26.68$ | 1.23$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 76 | 63.2% | +0.128 | 📉 agota (-0.05) | +23.12$ | 1.28$ | ✅ activa |
| ORDER_FLOW_5M | 1587 | 51.2% | +0.012 | ➡️ estable | +15.15$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO | 1109 | 68.3% | +0.183 | 📈 madura (+0.05) | +12.52$ | 1.83$ | ✅ activa |
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
| 2026-07-13T00:51 | STREAK_FADE_5M#XRP#5min | XRP Up or Down - July 12, 8:40PM-8:45PM ET… | ✅ WIN | +0.83$ |
| 2026-07-13T00:48 | ORDER_FLOW_5M#BNB#5min | BNB Up or Down - July 12, 8:40PM-8:45PM ET… | ❌ LOSS | -1.34$ |
| 2026-07-13T00:46 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 12, 8:40PM-8:45PM ET… | ✅ WIN | +1.16$ |
| 2026-07-13T00:46 | STREAK_FADE_5M#SOL#5min | Solana Up or Down - July 12, 8:40PM-8:45PM ET… | ✅ WIN | +0.49$ |
| 2026-07-13T00:46 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 12, 8:30PM-8:45PM ET… | ✅ WIN | +0.92$ |

## Calidad de datos

⚠️ **DEGRADED** — última verificación 2026-07-13T00:53 UTC | rechazos 1h: 7 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,921.99 | 0.1min |  |
| ✅ ETH | $1,819.94 | 0.1min |  |
| ✅ SOL | $77.37 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,922.20 | consenso |  |
| ETH | $1,821.27 | consenso |  |
| SOL | $77.42 | consenso |  |
| XRP | $1.09 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:7 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*