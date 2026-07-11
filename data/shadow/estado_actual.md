# Estado del bot — 2026-07-11 02:30 UTC

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
| P&L fiel (stake fijo 1$) | +864.08 $ |
| P&L sim compuesto | 🟢 +1319.26 $ (ficción Kelly: +5186% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +39.86 $ |
| Operaciones resueltas | 8494 (4727 WIN / 3767 LOSS) — 55.7% |
| Señales abiertas | 168 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3076 | 61.4% | +0.114 | ➡️ estable | +988.18$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 498 | 67.1% | +0.170 | ➡️ estable | +230.60$ | 1.70$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 619 | 57.0% | +0.070 | 📈 madura (+0.05) | +111.12$ | 0.70$ | ✅ activa |
| ORDER_FLOW_5M | 1573 | 51.4% | +0.014 | ➡️ estable | +18.85$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 121 | 62.0% | +0.118 | 📈 madura (+0.13) | +18.64$ | 1.18$ | ✅ activa |
| GBM_LATE_60M | 252 | 38.9% | -0.110 | 📈 madura (+0.08) | +12.17$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 35 | 62.9% | +0.122 | 📈 madura (+0.28) | +6.95$ | 1.22$ | ✅ activa |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM | 1248 | 48.6% | -0.014 | ➡️ estable | -1.68$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 280 | 67.9% | +0.177 | 📉 agota (-0.04) | -5.90$ | 1.77$ | ✅ activa |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T02:28 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 10, 10:20PM-10:25PM ET… | ✅ WIN | +0.12$ |
| 2026-07-11T02:26 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 10, 10:20PM-10:25PM ET… | ✅ WIN | +0.20$ |
| 2026-07-11T02:21 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 10, 10:15PM-10:20PM ET… | ✅ WIN | +0.11$ |
| 2026-07-11T02:21 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 10, 10:00PM-10:15PM ET… | ✅ WIN | +5.34$ |
| 2026-07-11T02:21 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 10, 10:00PM-10:15PM ET… | ✅ WIN | +0.60$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T02:30 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,975.36 | 0.1min |  |
| ✅ ETH | $1,789.23 | 0.1min |  |
| ✅ SOL | $77.66 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,986.90 | consenso |  |
| ETH | $1,789.34 | consenso |  |
| SOL | $77.57 | consenso |  |
| XRP | $1.10 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*