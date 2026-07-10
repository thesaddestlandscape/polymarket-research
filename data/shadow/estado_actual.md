# Estado del bot — 2026-07-10 19:12 UTC

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
| P&L fiel (stake fijo 1$) | +768.74 $ |
| P&L sim compuesto | 🟢 +1185.99 $ (ficción Kelly: +4662% s/ operativo) |
| P&L sim hoy (2026-07-10) | 🟢 +274.05 $ |
| Operaciones resueltas | 8011 (4416 WIN / 3595 LOSS) — 55.1% |
| Señales abiertas | 190 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2967 | 61.4% | +0.114 | ➡️ estable | +955.39$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 413 | 66.3% | +0.163 | 📈 madura (+0.05) | +170.51$ | 1.63$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 513 | 56.5% | +0.065 | 📈 madura (+0.08) | +83.55$ | 0.65$ | ✅ activa |
| ORDER_FLOW_5M | 1570 | 51.3% | +0.013 | ➡️ estable | +17.57$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 118 | 61.0% | +0.108 | 📈 madura (+0.13) | +16.00$ | 1.08$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 238 | 38.2% | -0.117 | 📈 madura (+0.07) | +8.57$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 28 | 60.7% | +0.100 | — | +3.21$ | 1.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 144 | 68.8% | +0.185 | 📉 agota (-0.09) | -3.12$ | 1.85$ | ✅ activa |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| UPDOWN_GBM | 1228 | 48.4% | -0.016 | ➡️ estable | -6.03$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-10T19:06 | GBM_LATE_60M#BTC#60min | Bitcoin Up or Down - July 10, 2PM ET… | ✅ WIN | +1.71$ |
| 2026-07-10T19:06 | FAVORITO_CONFIRMADO#BTC#60min | Bitcoin Up or Down - July 10, 2PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-10T19:04 | GBM_LATE_60M#SOL#60min | Solana Up or Down - July 10, 2PM ET… | ✅ WIN | +1.57$ |
| 2026-07-10T19:04 | FAVORITO_CONFIRMADO#SOL#60min | Solana Up or Down - July 10, 2PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-10T19:02 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 10, 2:45PM-3:00PM ET… | ❌ LOSS | -1.52$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-10T19:11 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,816.60 | 0.1min |  |
| ✅ ETH | $1,785.19 | 0.1min |  |
| ✅ SOL | $77.67 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,816.60 | consenso |  |
| ETH | $1,785.21 | consenso |  |
| SOL | $77.55 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*