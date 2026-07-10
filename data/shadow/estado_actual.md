# Estado del bot — 2026-07-10 20:12 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **24.92 $** |
| P&L real total | 🔴 **-0.52 $** |
| P&L real hoy | -6.53 $ |
| P&L real 7 días | +1.73 $ |
| Fees pagados (real) | 7.19 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +788.72 $ |
| P&L sim compuesto | 🟢 +1213.08 $ (ficción Kelly: +4768% s/ operativo) |
| P&L sim hoy (2026-07-10) | 🟢 +301.14 $ |
| Operaciones resueltas | 8075 (4464 WIN / 3611 LOSS) — 55.3% |
| Señales abiertas | 191 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2981 | 61.5% | +0.114 | ➡️ estable | +966.20$ | 1.15$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 424 | 67.0% | +0.169 | 📈 madura (+0.06) | +181.69$ | 1.69$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 527 | 56.7% | +0.067 | 📈 madura (+0.09) | +87.30$ | 0.67$ | ✅ activa |
| ORDER_FLOW_5M | 1570 | 51.3% | +0.013 | ➡️ estable | +17.57$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 120 | 61.7% | +0.115 | 📈 madura (+0.13) | +17.48$ | 1.15$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 238 | 38.2% | -0.117 | 📈 madura (+0.07) | +8.57$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 28 | 60.7% | +0.100 | — | +3.21$ | 1.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 162 | 69.8% | +0.195 | 📉 agota (-0.08) | -1.72$ | 1.95$ | ✅ activa |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| UPDOWN_GBM | 1233 | 48.3% | -0.017 | ➡️ estable | -7.57$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-10T20:10 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 10, 4:05PM-4:10PM ET… | ✅ WIN | +0.17$ |
| 2026-07-10T20:10 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 10, 4:05PM-4:10PM ET… | ✅ WIN | +0.25$ |
| 2026-07-10T20:04 | FAVORITO_CONFIRMADO#ETH#240min | Ethereum Up or Down - July 10, 12:00PM-4:00PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-10T20:03 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 10, 3:45PM-4:00PM ET… | ❌ LOSS | -1.23$ |
| 2026-07-10T20:03 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 10, 3:45PM-4:00PM ET… | ❌ LOSS | -1.72$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-10T20:11 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,813.29 | 0.1min |  |
| ✅ ETH | $1,788.96 | 0.1min |  |
| ✅ SOL | $77.90 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,813.29 | consenso |  |
| ETH | $1,789.73 | consenso |  |
| SOL | $77.83 | consenso |  |
| XRP | $1.10 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*