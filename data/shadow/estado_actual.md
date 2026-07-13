# Estado del bot — 2026-07-13 03:43 UTC

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
| P&L fiel (stake fijo 1$) | +1423.47 $ |
| P&L sim compuesto | 🟢 +2365.43 $ (ficción Kelly: +9298% s/ operativo) |
| P&L sim hoy (2026-07-13) | 🟢 +151.96 $ |
| Operaciones resueltas | 11869 (6843 WIN / 5026 LOSS) — 57.7% |
| Señales abiertas | 122 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3794 | 61.3% | +0.113 | ➡️ estable | +1275.77$ | 1.13$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1133 | 66.9% | +0.169 | ➡️ estable | +697.65$ | 1.69$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1245 | 58.6% | +0.085 | 📈 madura (+0.03) | +330.23$ | 0.85$ | ✅ activa |
| UPDOWN_GBM | 1363 | 49.7% | -0.003 | 📈 madura (+0.07) | +32.27$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_15M | 163 | 62.6% | +0.124 | 📈 madura (+0.23) | +29.22$ | 1.24$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 78 | 64.1% | +0.137 | 📉 agota (-0.05) | +27.01$ | 1.38$ | ✅ activa |
| FAVORITO_CONFIRMADO | 1156 | 68.8% | +0.187 | 📈 madura (+0.05) | +23.30$ | 1.87$ | ✅ activa |
| ORDER_FLOW_5M | 1590 | 51.3% | +0.013 | ➡️ estable | +14.99$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 38 | 71.1% | +0.200 | 📈 madura (+0.05) | +12.03$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 318 | 39.0% | -0.109 | ➡️ estable | +8.24$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM | 138 | 34.8% | -0.150 | 📉 agota (-0.11) | +0.19$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 204 | 57.4% | +0.073 | 📈 madura (+0.24) | -13.93$ | 0.73$ | ✅ activa |
| STREAK_FADE_5M | 196 | 46.4% | -0.035 | ➡️ estable | -14.42$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-13T03:43 | ORDER_FLOW_5M#XRP#5min | XRP Up or Down - July 12, 11:35PM-11:40PM ET… | ❌ LOSS | -1.13$ |
| 2026-07-13T03:37 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 12, 11:30PM-11:35PM ET… | ✅ WIN | +1.17$ |
| 2026-07-13T03:34 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 12, 11:15PM-11:30PM ET… | ❌ LOSS | -1.68$ |
| 2026-07-13T03:34 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 12, 11:15PM-11:30PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-13T03:34 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 12, 11:15PM-11:30PM ET… | ❌ LOSS | -1.31$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-13T03:42 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,819.12 | 0.1min |  |
| ✅ ETH | $1,779.51 | 0.1min |  |
| ✅ SOL | $75.77 | 0.1min |  |
| ✅ XRP | $1.07 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,830.10 | consenso |  |
| ETH | $1,780.47 | consenso |  |
| SOL | $75.75 | consenso |  |
| XRP | $1.07 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*