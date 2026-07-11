# Estado del bot — 2026-07-11 16:41 UTC

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
| P&L fiel (stake fijo 1$) | +969.14 $ |
| P&L sim compuesto | 🟢 +1502.62 $ (ficción Kelly: +5907% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +223.21 $ |
| Operaciones resueltas | 9466 (5299 WIN / 4167 LOSS) — 56.0% |
| Señales abiertas | 187 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3287 | 61.2% | +0.112 | ➡️ estable | +1053.51$ | 1.12$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 681 | 64.6% | +0.146 | ➡️ estable | +303.33$ | 1.46$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 830 | 57.7% | +0.077 | 📈 madura (+0.05) | +177.06$ | 0.77$ | ✅ activa |
| STREAK_FADE_15M | 131 | 61.8% | +0.117 | 📈 madura (+0.12) | +19.89$ | 1.17$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 50 | 64.0% | +0.135 | 📈 madura (+0.15) | +14.72$ | 1.35$ | ✅ activa |
| GBM_LATE_60M | 285 | 39.3% | -0.106 | 📈 madura (+0.09) | +10.70$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 1273 | 48.7% | -0.013 | 📈 madura (+0.03) | +5.15$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 136 | 34.6% | -0.152 | 📉 agota (-0.13) | -0.14$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 11 | 45.5% | -0.021 | — | -0.60$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 192 | 57.8% | +0.077 | 📈 madura (+0.23) | -13.59$ | 0.77$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 531 | 65.3% | +0.153 | 📉 agota (-0.05) | -38.09$ | 1.53$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T16:41 | STREAK_FADE_5M#ETH#5min | Ethereum Up or Down - July 11, 12:35PM-12:40PM ET… | ✅ WIN | +0.50$ |
| 2026-07-11T16:36 | STREAK_FADE_5M#ETH#5min | Ethereum Up or Down - July 11, 12:30PM-12:35PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-11T16:36 | STREAK_FADE_5M#SOL#5min | Solana Up or Down - July 11, 12:30PM-12:35PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-11T16:36 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 11, 12:15PM-12:30PM ET… | ✅ WIN | +1.13$ |
| 2026-07-11T16:36 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 11, 12:15PM-12:30PM ET… | ✅ WIN | +2.60$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T16:40 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,111.75 | 0.1min |  |
| ✅ ETH | $1,818.55 | 0.1min |  |
| ✅ SOL | $77.83 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,111.75 | consenso |  |
| ETH | $1,818.55 | consenso |  |
| SOL | $77.84 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*