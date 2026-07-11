# Estado del bot — 2026-07-11 10:11 UTC

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
| P&L fiel (stake fijo 1$) | +934.29 $ |
| P&L sim compuesto | 🟢 +1436.22 $ (ficción Kelly: +5646% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +156.82 $ |
| Operaciones resueltas | 9012 (5040 WIN / 3972 LOSS) — 55.9% |
| Señales abiertas | 163 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3194 | 61.4% | +0.114 | ➡️ estable | +1042.27$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 596 | 65.3% | +0.152 | 📉 agota (-0.04) | +263.37$ | 1.52$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 737 | 57.9% | +0.079 | 📈 madura (+0.04) | +157.83$ | 0.79$ | ✅ activa |
| STREAK_FADE_15M | 127 | 62.2% | +0.120 | 📈 madura (+0.13) | +20.22$ | 1.20$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 46 | 63.0% | +0.125 | 📈 madura (+0.20) | +10.89$ | 1.25$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 272 | 39.3% | -0.106 | 📈 madura (+0.11) | +8.72$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM | 1255 | 48.4% | -0.016 | ➡️ estable | -2.42$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 417 | 66.9% | +0.168 | 📉 agota (-0.04) | -21.51$ | 1.68$ | ✅ activa |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T10:05 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 11, 5:55AM-6:00AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-11T10:01 | GBM_LATE_60M#ETH#60min | Ethereum Up or Down - July 11, 5AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-11T10:01 | FAVORITO_CONFIRMADO#ETH#60min | Ethereum Up or Down - July 11, 5AM ET… | ❌ LOSS | -1.46$ |
| 2026-07-11T10:00 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 11, 5:55AM-6:00AM ET… | ❌ LOSS | -1.60$ |
| 2026-07-11T10:00 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 11, 5:45AM-6:00AM ET… | ✅ WIN | +0.52$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T10:11 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,103.85 | 0.1min |  |
| ✅ ETH | $1,795.12 | 0.1min |  |
| ✅ SOL | $77.91 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,106.40 | consenso |  |
| ETH | $1,795.12 | consenso |  |
| SOL | $77.80 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*