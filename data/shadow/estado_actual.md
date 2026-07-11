# Estado del bot — 2026-07-11 07:25 UTC

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
| P&L fiel (stake fijo 1$) | +920.12 $ |
| P&L sim compuesto | 🟢 +1406.86 $ (ficción Kelly: +5530% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +127.46 $ |
| Operaciones resueltas | 8830 (4930 WIN / 3900 LOSS) — 55.8% |
| Señales abiertas | 165 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3154 | 61.4% | +0.114 | ➡️ estable | +1028.55$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 561 | 66.1% | +0.161 | ➡️ estable | +261.84$ | 1.61$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 697 | 57.4% | +0.074 | 📈 madura (+0.03) | +141.52$ | 0.74$ | ✅ activa |
| STREAK_FADE_15M | 127 | 62.2% | +0.120 | 📈 madura (+0.13) | +20.22$ | 1.20$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 43 | 65.1% | +0.144 | 📈 madura (+0.23) | +10.37$ | 1.44$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 263 | 39.2% | -0.108 | 📈 madura (+0.11) | +10.26$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| UPDOWN_GBM | 1252 | 48.6% | -0.014 | ➡️ estable | -0.08$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 365 | 66.8% | +0.168 | 📉 agota (-0.07) | -22.67$ | 1.68$ | ✅ activa |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T07:19 | UPDOWN_GBM#ETH#15min | Ethereum Up or Down - July 11, 3:00AM-3:15AM ET… | ✅ WIN | +2.26$ |
| 2026-07-11T07:19 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 11, 3:00AM-3:15AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-11T07:19 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 11, 3:00AM-3:15AM ET… | ❌ LOSS | -1.89$ |
| 2026-07-11T07:19 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 11, 3:00AM-3:15AM ET… | ✅ WIN | +2.45$ |
| 2026-07-11T07:19 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 11, 3:00AM-3:15AM ET… | ✅ WIN | +0.88$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T07:24 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,167.49 | 0.1min |  |
| ✅ ETH | $1,799.12 | 0.1min |  |
| ✅ SOL | $78.01 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,170.60 | consenso |  |
| ETH | $1,799.12 | consenso |  |
| SOL | $77.97 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*