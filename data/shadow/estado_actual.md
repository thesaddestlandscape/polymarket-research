# Estado del bot — 2026-07-11 20:54 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **22.40 $** |
| P&L real total | 🔴 **-3.04 $** |
| P&L real hoy | -2.90 $ |
| P&L real 7 días | +14.42 $ |
| Fees pagados (real) | 7.52 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +999.27 $ |
| P&L sim compuesto | 🟢 +1558.05 $ (ficción Kelly: +6124% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +278.64 $ |
| Operaciones resueltas | 9765 (5486 WIN / 4279 LOSS) — 56.2% |
| Señales abiertas | 182 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3347 | 61.1% | +0.111 | ➡️ estable | +1056.08$ | 1.11$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 729 | 64.5% | +0.144 | 📉 agota (-0.04) | +313.34$ | 1.44$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 890 | 57.6% | +0.076 | ➡️ estable | +181.49$ | 0.76$ | ✅ activa |
| STREAK_FADE_15M | 134 | 61.9% | +0.118 | 📈 madura (+0.13) | +21.31$ | 1.18$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 53 | 66.0% | +0.155 | 📈 madura (+0.15) | +19.18$ | 1.54$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| UPDOWN_GBM | 1285 | 48.9% | -0.010 | 📈 madura (+0.03) | +12.02$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 294 | 39.1% | -0.108 | 📈 madura (+0.05) | +11.86$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| STREAK_FADE_5M | 37 | 54.1% | +0.038 | 📈 madura (+0.17) | +1.13$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 136 | 34.6% | -0.152 | 📉 agota (-0.13) | -0.14$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 192 | 57.8% | +0.077 | 📈 madura (+0.23) | -13.59$ | 0.77$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 609 | 66.5% | +0.164 | 📉 agota (-0.05) | -15.31$ | 1.65$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T20:49 | STREAK_FADE_5M#XRP#5min | XRP Up or Down - July 11, 4:40PM-4:45PM ET… | ✅ WIN | +0.50$ |
| 2026-07-11T20:49 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 11, 4:30PM-4:45PM ET… | ✅ WIN | +0.28$ |
| 2026-07-11T20:49 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 11, 4:30PM-4:45PM ET… | ✅ WIN | +1.96$ |
| 2026-07-11T20:49 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 11, 4:30PM-4:45PM ET… | ✅ WIN | +1.71$ |
| 2026-07-11T20:49 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 11, 4:30PM-4:45PM ET… | ✅ WIN | +0.67$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T20:53 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,340.64 | 0.1min |  |
| ✅ ETH | $1,824.42 | 0.1min |  |
| ✅ SOL | $78.19 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,345.32 | consenso |  |
| ETH | $1,824.47 | consenso |  |
| SOL | $78.13 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*