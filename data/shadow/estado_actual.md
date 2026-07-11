# Estado del bot — 2026-07-11 09:34 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **25.30 $** |
| P&L real total | 🔴 **-0.14 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | +17.32 $ |
| Fees pagados (real) | 7.27 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +929.97 $ |
| P&L sim compuesto | 🟢 +1427.10 $ (ficción Kelly: +5610% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +147.69 $ |
| Operaciones resueltas | 8974 (5016 WIN / 3958 LOSS) — 55.9% |
| Señales abiertas | 160 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3186 | 61.4% | +0.114 | ➡️ estable | +1036.12$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 588 | 65.3% | +0.153 | 📉 agota (-0.04) | +262.36$ | 1.52$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 729 | 57.8% | +0.077 | 📈 madura (+0.04) | +153.03$ | 0.77$ | ✅ activa |
| STREAK_FADE_15M | 127 | 62.2% | +0.120 | 📈 madura (+0.13) | +20.22$ | 1.20$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 46 | 63.0% | +0.125 | 📈 madura (+0.20) | +10.89$ | 1.25$ | ✅ activa |
| GBM_LATE_60M | 269 | 39.8% | -0.101 | 📈 madura (+0.12) | +10.64$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM | 1255 | 48.4% | -0.016 | ➡️ estable | -2.42$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 406 | 67.0% | +0.169 | 📉 agota (-0.04) | -20.58$ | 1.69$ | ✅ activa |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T09:31 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 11, 5:15AM-5:30AM ET… | ❌ LOSS | -0.99$ |
| 2026-07-11T09:31 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 11, 5:15AM-5:30AM ET… | ✅ WIN | +2.00$ |
| 2026-07-11T09:31 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 11, 5:15AM-5:30AM ET… | ❌ LOSS | -1.80$ |
| 2026-07-11T09:31 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 11, 5:15AM-5:30AM ET… | ❌ LOSS | -0.66$ |
| 2026-07-11T09:31 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 11, 5:15AM-5:30AM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T09:33 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,248.00 | 0.1min |  |
| ✅ ETH | $1,798.29 | 0.1min |  |
| ✅ SOL | $77.97 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,248.00 | consenso |  |
| ETH | $1,798.29 | consenso |  |
| SOL | $78.03 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*