# Estado del bot — 2026-07-14 09:26 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **9.30 $** |
| P&L real total | 🔴 **-16.14 $** |
| P&L real hoy | -0.72 $ |
| P&L real 7 días | -6.20 $ |
| Fees pagados (real) | 8.11 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1565.77 $ |
| P&L sim compuesto | 🟢 +2698.46 $ (ficción Kelly: +10607% s/ operativo) |
| P&L sim hoy (2026-07-14) | 🟢 +144.25 $ |
| Operaciones resueltas | 13625 (7886 WIN / 5739 LOSS) — 57.9% |
| Señales abiertas | 71 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4211 | 60.6% | +0.106 | ➡️ estable | +1340.75$ | 1.06$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1519 | 65.6% | +0.155 | ➡️ estable | +920.10$ | 1.55$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1465 | 58.4% | +0.084 | ➡️ estable | +403.78$ | 0.84$ | ✅ activa |
| UPDOWN_GBM | 1463 | 50.6% | +0.006 | 📈 madura (+0.08) | +58.57$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 97 | 59.8% | +0.096 | 📉 agota (-0.05) | +27.84$ | 0.96$ | ✅ activa |
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
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 1677 | 67.8% | +0.178 | ➡️ estable | -21.07$ | 1.78$ | ✅ activa |
| STREAK_FADE_5M | 245 | 45.3% | -0.047 | 📉 agota (-0.04) | -23.43$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-14T09:20 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 14, 5:00AM-5:15AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-14T09:20 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 14, 5:00AM-5:15AM ET… | ✅ WIN | +1.01$ |
| 2026-07-14T09:20 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 14, 5:00AM-5:15AM ET… | ❌ LOSS | -0.83$ |
| 2026-07-14T09:16 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 14, 5:00AM-5:15AM ET… | ✅ WIN | +0.88$ |
| 2026-07-14T09:16 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 14, 5:00AM-5:15AM ET… | ✅ WIN | +2.45$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-14T09:25 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,593.12 | 0.1min |  |
| ✅ ETH | $1,785.87 | 0.1min |  |
| ✅ SOL | $75.16 | 0.1min |  |
| ✅ XRP | $1.07 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,593.12 | consenso |  |
| ETH | $1,785.87 | consenso |  |
| SOL | $75.09 | consenso |  |
| XRP | $1.07 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*