# Estado del bot — 2026-07-13 14:19 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **11.12 $** |
| P&L real total | 🔴 **-14.32 $** |
| P&L real hoy | -3.32 $ |
| P&L real 7 días | +2.26 $ |
| Fees pagados (real) | 7.93 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1444.14 $ |
| P&L sim compuesto | 🟢 +2435.28 $ (ficción Kelly: +9573% s/ operativo) |
| P&L sim hoy (2026-07-13) | 🟢 +221.81 $ |
| Operaciones resueltas | 12541 (7212 WIN / 5329 LOSS) — 57.5% |
| Señales abiertas | 109 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3957 | 60.9% | +0.109 | ➡️ estable | +1294.85$ | 1.09$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1279 | 65.7% | +0.157 | ➡️ estable | +751.10$ | 1.56$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1343 | 58.5% | +0.085 | ➡️ estable | +376.11$ | 0.85$ | ✅ activa |
| UPDOWN_GBM | 1398 | 50.0% | +0.000 | 📈 madura (+0.07) | +44.98$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 83 | 62.7% | +0.124 | 📉 agota (-0.11) | +26.32$ | 1.23$ | ✅ activa |
| STREAK_FADE_15M | 171 | 60.8% | +0.107 | 📈 madura (+0.18) | +21.49$ | 1.07$ | ✅ activa |
| LATE_WINDOW_5MIN | 39 | 71.8% | +0.207 | 📈 madura (+0.06) | +13.83$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1591 | 51.2% | +0.012 | ➡️ estable | +13.79$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 323 | 38.7% | -0.112 | ➡️ estable | +5.44$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 140 | 34.3% | -0.155 | 📉 agota (-0.14) | -0.83$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 204 | 57.4% | +0.073 | 📈 madura (+0.24) | -13.93$ | 0.73$ | ✅ activa |
| STREAK_FADE_5M | 223 | 47.1% | -0.029 | 📉 agota (-0.05) | -14.89$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 1337 | 67.3% | +0.173 | ➡️ estable | -25.85$ | 1.73$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-13T14:17 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 13, 10:00AM-10:15AM ET… | ✅ WIN | +2.00$ |
| 2026-07-13T14:15 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 13, 10:00AM-10:15AM ET… | ✅ WIN | +1.92$ |
| 2026-07-13T14:15 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 13, 10:00AM-10:15AM ET… | ✅ WIN | +0.80$ |
| 2026-07-13T14:15 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 13, 10:00AM-10:15AM ET… | ✅ WIN | +1.44$ |
| 2026-07-13T14:15 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 13, 10:00AM-10:15AM ET… | ✅ WIN | +1.88$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-13T14:18 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,324.25 | 0.1min |  |
| ✅ ETH | $1,769.80 | 0.1min |  |
| ✅ SOL | $75.65 | 0.1min |  |
| ✅ XRP | $1.07 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,335.70 | consenso |  |
| ETH | $1,771.11 | consenso |  |
| SOL | $75.67 | consenso |  |
| XRP | $1.07 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*