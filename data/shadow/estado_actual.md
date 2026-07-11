# Estado del bot — 2026-07-11 17:05 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **21.08 $** |
| P&L real total | 🔴 **-4.36 $** |
| P&L real hoy | -4.22 $ |
| P&L real 7 días | +13.10 $ |
| Fees pagados (real) | 7.36 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +959.01 $ |
| P&L sim compuesto | 🟢 +1493.55 $ (ficción Kelly: +5871% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +214.15 $ |
| Operaciones resueltas | 9507 (5316 WIN / 4191 LOSS) — 55.9% |
| Señales abiertas | 171 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3295 | 61.1% | +0.111 | ➡️ estable | +1048.84$ | 1.11$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 686 | 64.4% | +0.144 | ➡️ estable | +301.01$ | 1.44$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 838 | 57.6% | +0.076 | 📈 madura (+0.04) | +176.95$ | 0.76$ | ✅ activa |
| STREAK_FADE_15M | 131 | 61.8% | +0.117 | 📈 madura (+0.12) | +19.89$ | 1.17$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 51 | 64.7% | +0.142 | 📈 madura (+0.16) | +16.72$ | 1.41$ | ✅ activa |
| GBM_LATE_60M | 288 | 39.2% | -0.107 | 📈 madura (+0.08) | +11.37$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 1273 | 48.7% | -0.013 | 📈 madura (+0.03) | +5.15$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 136 | 34.6% | -0.152 | 📉 agota (-0.13) | -0.14$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 17 | 41.2% | -0.067 | — | -1.68$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 192 | 57.8% | +0.077 | 📈 madura (+0.23) | -13.59$ | 0.77$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 541 | 65.1% | +0.150 | 📉 agota (-0.05) | -41.64$ | 1.50$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T17:05 | GBM_LATE_60M#BTC#60min | Bitcoin Up or Down - July 11, 12PM ET… | ✅ WIN | +1.69$ |
| 2026-07-11T17:05 | FAVORITO_CONFIRMADO#BTC#60min | Bitcoin Up or Down - July 11, 12PM ET… | ❌ LOSS | -0.91$ |
| 2026-07-11T17:01 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 11, 12:45PM-1:00PM ET… | ❌ LOSS | -1.62$ |
| 2026-07-11T17:01 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 11, 12:45PM-1:00PM ET… | ❌ LOSS | -0.74$ |
| 2026-07-11T17:01 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 11, 12:45PM-1:00PM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T17:04 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,143.04 | 0.1min |  |
| ✅ ETH | $1,822.10 | 0.1min |  |
| ✅ SOL | $77.84 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,143.04 | consenso |  |
| ETH | $1,822.10 | consenso |  |
| SOL | $77.88 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*