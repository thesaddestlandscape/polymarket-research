# Estado del bot — 2026-07-12 23:16 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **13.21 $** |
| P&L real total | 🔴 **-12.23 $** |
| P&L real hoy | -4.96 $ |
| P&L real 7 días | +5.05 $ |
| Fees pagados (real) | 7.67 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1342.64 $ |
| P&L sim compuesto | 🟢 +2197.66 $ (ficción Kelly: +8639% s/ operativo) |
| P&L sim hoy (2026-07-12) | 🟢 +592.95 $ |
| Operaciones resueltas | 11578 (6639 WIN / 4939 LOSS) — 57.3% |
| Señales abiertas | 145 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3725 | 61.2% | +0.112 | ➡️ estable | +1234.06$ | 1.12$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1073 | 66.3% | +0.162 | ➡️ estable | +623.29$ | 1.62$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1211 | 58.1% | +0.081 | 📈 madura (+0.03) | +303.39$ | 0.81$ | ✅ activa |
| UPDOWN_GBM | 1348 | 49.6% | -0.004 | 📈 madura (+0.07) | +28.00$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_15M | 159 | 62.3% | +0.121 | 📈 madura (+0.20) | +24.84$ | 1.21$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 72 | 62.5% | +0.122 | ➡️ estable | +19.96$ | 1.22$ | ✅ activa |
| ORDER_FLOW_5M | 1586 | 51.3% | +0.013 | ➡️ estable | +16.48$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO | 1081 | 68.4% | +0.183 | 📈 madura (+0.06) | +10.28$ | 1.83$ | ✅ activa |
| GBM_LATE_60M | 317 | 38.8% | -0.111 | ➡️ estable | +7.10$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM | 138 | 34.8% | -0.150 | 📉 agota (-0.11) | +0.19$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 176 | 47.2% | -0.028 | ➡️ estable | -9.16$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 204 | 57.4% | +0.073 | 📈 madura (+0.24) | -13.93$ | 0.73$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-12T23:15 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 12, 7:10PM-7:15PM ET… | ✅ WIN | +1.32$ |
| 2026-07-12T23:15 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 12, 7:10PM-7:15PM ET… | ✅ WIN | +1.27$ |
| 2026-07-12T23:15 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 12, 7:05PM-7:10PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-12T23:15 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 12, 7:05PM-7:10PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-12T23:15 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 12, 7:00PM-7:15PM ET… | ✅ WIN | +0.57$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-12T23:15 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,794.64 | 0.1min |  |
| ✅ ETH | $1,802.08 | 0.1min |  |
| ✅ SOL | $76.80 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,801.60 | consenso |  |
| ETH | $1,802.08 | consenso |  |
| SOL | $76.68 | consenso |  |
| XRP | $1.08 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*