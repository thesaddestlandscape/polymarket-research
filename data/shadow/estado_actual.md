# Estado del bot — 2026-07-09 17:16 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **29.46 $** |
| P&L real total | 🟢 **+4.02 $** |
| P&L real hoy | -4.91 $ |
| P&L real 7 días | -1.06 $ |
| Fees pagados (real) | 6.48 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +486.92 $ |
| P&L sim compuesto | 🟢 +792.43 $ (ficción Kelly: +3115% s/ operativo) |
| P&L sim hoy (2026-07-09) | 🟢 +146.94 $ |
| Operaciones resueltas | 6543 (3507 WIN / 3036 LOSS) — 53.6% |
| Señales abiertas | 169 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2568 | 61.2% | +0.112 | 📈 madura (+0.04) | +825.81$ | 1.12$ | ✅ activa |
| ORDER_FLOW_5M | 1560 | 51.3% | +0.013 | ➡️ estable | +18.55$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 85 | 64.7% | +0.144 | ➡️ estable | +16.49$ | 1.44$ | ✅ activa |
| LATE_WINDOW_5MIN | 32 | 68.8% | +0.176 | 📉 agota (-0.11) | +6.54$ | 1.76$ | ✅ activa |
| STREAK_FADE_15M | 98 | 57.1% | +0.070 | 📈 madura (+0.04) | +5.98$ | 0.70$ | ✅ activa |
| GBM_LATE_60M | 179 | 36.3% | -0.135 | ➡️ estable | +4.45$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| LEADLAG_BTC_XRP_15M | 8 | 50.0% | +0.000 | — | -0.09$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 132 | 34.1% | -0.157 | 📉 agota (-0.10) | -0.77$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_TARDIO | 121 | 48.8% | -0.012 | 📉 agota (-0.15) | -2.13$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 281 | 47.0% | -0.030 | ➡️ estable | -14.30$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 159 | 55.3% | +0.053 | 📈 madura (+0.14) | -15.64$ | 0.53$ | ✅ activa |
| UPDOWN_GBM | 1178 | 47.9% | -0.021 | ➡️ estable | -18.46$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-09T17:14 | STREAK_MOM_5M#ETH#5min | Ethereum Up or Down - July 9, 1:05PM-1:10PM ET… | ✅ WIN | +0.48$ |
| 2026-07-09T17:06 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 9, 12:45PM-1:00PM ET… | ✅ WIN | +0.80$ |
| 2026-07-09T17:06 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 9, 12:45PM-1:00PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-09T17:06 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 9, 12:45PM-1:00PM ET… | ✅ WIN | +0.48$ |
| 2026-07-09T17:06 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 9, 12:45PM-1:00PM ET… | ❌ LOSS | -1.83$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-09T17:15 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,637.54 | 0.1min |  |
| ✅ ETH | $1,737.93 | 0.1min |  |
| ✅ SOL | $77.75 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,644.90 | consenso |  |
| ETH | $1,738.12 | consenso |  |
| SOL | $77.64 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*