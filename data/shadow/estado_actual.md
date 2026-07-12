# Estado del bot — 2026-07-12 19:27 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **14.13 $** |
| P&L real total | 🔴 **-11.31 $** |
| P&L real hoy | -3.85 $ |
| P&L real 7 días | +6.15 $ |
| Fees pagados (real) | 7.67 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1323.81 $ |
| P&L sim compuesto | 🟢 +2155.33 $ (ficción Kelly: +8472% s/ operativo) |
| P&L sim hoy (2026-07-12) | 🟢 +550.62 $ |
| Operaciones resueltas | 11330 (6487 WIN / 4843 LOSS) — 57.3% |
| Señales abiertas | 144 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3670 | 61.3% | +0.113 | ➡️ estable | +1224.46$ | 1.13$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1021 | 66.6% | +0.166 | ➡️ estable | +602.89$ | 1.66$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1173 | 58.1% | +0.080 | ➡️ estable | +287.93$ | 0.80$ | ✅ activa |
| STREAK_FADE_15M | 155 | 62.6% | +0.124 | 📈 madura (+0.18) | +25.15$ | 1.24$ | ✅ activa |
| UPDOWN_GBM | 1335 | 49.4% | -0.006 | 📈 madura (+0.06) | +23.91$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 71 | 63.4% | +0.130 | ➡️ estable | +21.20$ | 1.30$ | ✅ activa |
| FAVORITO_CONFIRMADO | 1009 | 68.5% | +0.184 | 📈 madura (+0.05) | +17.06$ | 1.84$ | ✅ activa |
| ORDER_FLOW_5M | 1586 | 51.3% | +0.013 | ➡️ estable | +16.48$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 315 | 38.7% | -0.112 | ➡️ estable | +7.27$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM | 138 | 34.8% | -0.150 | 📉 agota (-0.11) | +0.19$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 165 | 46.1% | -0.039 | ➡️ estable | -10.48$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 204 | 57.4% | +0.073 | 📈 madura (+0.24) | -13.93$ | 0.73$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-12T19:20 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 12, 3:00PM-3:15PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-12T19:20 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 12, 3:00PM-3:15PM ET… | ✅ WIN | +5.51$ |
| 2026-07-12T19:20 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 12, 3:00PM-3:15PM ET… | ✅ WIN | +5.23$ |
| 2026-07-12T19:20 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 12, 3:00PM-3:15PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-12T19:20 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 12, 3:00PM-3:15PM ET… | ✅ WIN | +1.90$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-12T19:26 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,162.00 | 0.1min |  |
| ✅ ETH | $1,819.82 | 0.1min |  |
| ✅ SOL | $77.57 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,162.30 | consenso |  |
| ETH | $1,819.82 | consenso |  |
| SOL | $77.51 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*