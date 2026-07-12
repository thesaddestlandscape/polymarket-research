# Estado del bot — 2026-07-12 13:38 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **15.24 $** |
| P&L real total | 🔴 **-10.20 $** |
| P&L real hoy | -2.75 $ |
| P&L real 7 días | +7.26 $ |
| Fees pagados (real) | 7.61 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1227.60 $ |
| P&L sim compuesto | 🟢 +1970.81 $ (ficción Kelly: +7747% s/ operativo) |
| P&L sim hoy (2026-07-12) | 🟢 +366.10 $ |
| Operaciones resueltas | 10972 (6252 WIN / 4720 LOSS) — 57.0% |
| Señales abiertas | 150 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3591 | 61.3% | +0.113 | ➡️ estable | +1178.37$ | 1.13$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 952 | 66.1% | +0.160 | ➡️ estable | +503.62$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1118 | 58.0% | +0.079 | ➡️ estable | +265.03$ | 0.80$ | ✅ activa |
| UPDOWN_GBM | 1322 | 49.3% | -0.007 | 📈 madura (+0.05) | +26.62$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_15M | 151 | 61.6% | +0.114 | 📈 madura (+0.19) | +18.94$ | 1.14$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 66 | 62.1% | +0.118 | ➡️ estable | +18.50$ | 1.18$ | ✅ activa |
| ORDER_FLOW_5M | 1584 | 51.3% | +0.013 | ➡️ estable | +17.50$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO | 904 | 68.4% | +0.183 | 📈 madura (+0.04) | +9.55$ | 1.83$ | ✅ activa |
| GBM_LATE_60M | 310 | 38.4% | -0.115 | ➡️ estable | +4.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 9 | 100.0% | +0.184 | — | +3.91$ | 1.84$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 136 | 34.6% | -0.152 | 📉 agota (-0.13) | -0.14$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 159 | 45.3% | -0.047 | 📉 agota (-0.08) | -11.64$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 192 | 57.8% | +0.077 | 📈 madura (+0.23) | -13.59$ | 0.77$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-12T13:38 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 12, 9:15AM-9:30AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-12T13:38 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 12, 9:15AM-9:30AM ET… | ❌ LOSS | -1.46$ |
| 2026-07-12T13:38 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 12, 9:15AM-9:30AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-12T13:38 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 12, 9:15AM-9:30AM ET… | ❌ LOSS | -1.47$ |
| 2026-07-12T13:34 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 12, 9:15AM-9:30AM ET… | ✅ WIN | +1.92$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-12T13:37 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,023.94 | 0.1min |  |
| ✅ ETH | $1,806.94 | 0.1min |  |
| ✅ SOL | $77.31 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,024.90 | consenso |  |
| ETH | $1,806.94 | consenso |  |
| SOL | $77.22 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*