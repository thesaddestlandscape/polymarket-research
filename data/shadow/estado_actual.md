# Estado del bot — 2026-07-11 08:32 UTC

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
| P&L fiel (stake fijo 1$) | +933.66 $ |
| P&L sim compuesto | 🟢 +1430.26 $ (ficción Kelly: +5622% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +150.86 $ |
| Operaciones resueltas | 8906 (4980 WIN / 3926 LOSS) — 55.9% |
| Señales abiertas | 161 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3171 | 61.4% | +0.114 | ➡️ estable | +1028.88$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 574 | 66.0% | +0.160 | ➡️ estable | +267.27$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 714 | 57.8% | +0.078 | 📈 madura (+0.04) | +151.25$ | 0.78$ | ✅ activa |
| STREAK_FADE_15M | 127 | 62.2% | +0.120 | 📈 madura (+0.13) | +20.22$ | 1.20$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 266 | 39.5% | -0.104 | 📈 madura (+0.13) | +10.96$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 45 | 62.2% | +0.117 | 📈 madura (+0.14) | +8.93$ | 1.17$ | ✅ activa |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM | 1254 | 48.5% | -0.015 | ➡️ estable | -1.91$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 387 | 67.4% | +0.174 | 📉 agota (-0.04) | -12.18$ | 1.73$ | ✅ activa |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T08:32 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 11, 4:15AM-4:30AM ET… | ❌ LOSS | -0.72$ |
| 2026-07-11T08:32 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 11, 4:15AM-4:30AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-11T08:32 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 11, 4:15AM-4:30AM ET… | ✅ WIN | +0.75$ |
| 2026-07-11T08:26 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 11, 4:20AM-4:25AM ET… | ✅ WIN | +0.73$ |
| 2026-07-11T08:26 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 11, 4:20AM-4:25AM ET… | ✅ WIN | +0.32$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T08:32 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,202.43 | 0.1min |  |
| ✅ ETH | $1,800.09 | 0.1min |  |
| ✅ SOL | $78.02 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,214.70 | consenso |  |
| ETH | $1,800.09 | consenso |  |
| SOL | $77.98 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*