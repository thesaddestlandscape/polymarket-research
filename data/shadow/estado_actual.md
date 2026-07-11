# Estado del bot — 2026-07-11 01:14 UTC

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
| P&L fiel (stake fijo 1$) | +823.82 $ |
| P&L sim compuesto | 🟢 +1282.14 $ (ficción Kelly: +5040% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +2.73 $ |
| Operaciones resueltas | 8418 (4673 WIN / 3745 LOSS) — 55.5% |
| Señales abiertas | 166 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3059 | 61.4% | +0.114 | ➡️ estable | +982.56$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 485 | 66.8% | +0.167 | ➡️ estable | +213.16$ | 1.67$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 603 | 56.6% | +0.065 | 📈 madura (+0.03) | +100.39$ | 0.65$ | ✅ activa |
| ORDER_FLOW_5M | 1573 | 51.4% | +0.014 | ➡️ estable | +18.85$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 121 | 62.0% | +0.118 | 📈 madura (+0.13) | +18.64$ | 1.18$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 249 | 38.2% | -0.118 | 📈 madura (+0.07) | +6.50$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 33 | 60.6% | +0.100 | 📈 madura (+0.18) | +4.99$ | 1.00$ | ✅ activa |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 256 | 68.0% | +0.178 | 📉 agota (-0.06) | -0.57$ | 1.78$ | ✅ activa |
| UPDOWN_GBM | 1247 | 48.5% | -0.015 | ➡️ estable | -2.72$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T01:07 | GBM_LATE_60M#BTC#60min | Bitcoin Up or Down - July 10, 8PM ET… | ✅ WIN | +0.15$ |
| 2026-07-11T01:07 | FAVORITO_CONFIRMADO#BTC#60min | Bitcoin Up or Down - July 10, 8PM ET… | ✅ WIN | +0.41$ |
| 2026-07-11T01:06 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 10, 8:45PM-9:00PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-11T01:06 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 10, 8:45PM-9:00PM ET… | ❌ LOSS | -0.88$ |
| 2026-07-11T01:06 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 10, 8:45PM-9:00PM ET… | ❌ LOSS | -0.84$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T01:13 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,094.32 | 0.1min |  |
| ✅ ETH | $1,792.21 | 0.1min |  |
| ✅ SOL | $77.81 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,096.40 | consenso |  |
| ETH | $1,792.21 | consenso |  |
| SOL | $77.73 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*