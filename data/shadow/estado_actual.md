# Estado del bot — 2026-07-11 00:56 UTC

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
| P&L fiel (stake fijo 1$) | +822.35 $ |
| P&L sim compuesto | 🟢 +1280.66 $ (ficción Kelly: +5034% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +1.25 $ |
| Operaciones resueltas | 8402 (4662 WIN / 3740 LOSS) — 55.5% |
| Señales abiertas | 165 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3056 | 61.4% | +0.114 | ➡️ estable | +981.21$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 483 | 66.9% | +0.168 | ➡️ estable | +214.67$ | 1.68$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 600 | 56.8% | +0.068 | 📈 madura (+0.04) | +102.29$ | 0.68$ | ✅ activa |
| STREAK_FADE_15M | 121 | 62.0% | +0.118 | 📈 madura (+0.13) | +18.64$ | 1.18$ | ✅ activa |
| ORDER_FLOW_5M | 1572 | 51.3% | +0.013 | ➡️ estable | +17.51$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 248 | 37.9% | -0.120 | 📈 madura (+0.06) | +6.34$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 33 | 60.6% | +0.100 | 📈 madura (+0.18) | +4.99$ | 1.00$ | ✅ activa |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 250 | 67.2% | +0.171 | 📉 agota (-0.08) | -2.61$ | 1.71$ | ✅ activa |
| UPDOWN_GBM | 1247 | 48.5% | -0.015 | ➡️ estable | -2.72$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T00:51 | UPDOWN_GBM#ETH#15min | Ethereum Up or Down - July 10, 8:30PM-8:45PM ET… | ✅ WIN | +0.87$ |
| 2026-07-11T00:51 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 10, 8:30PM-8:45PM ET… | ✅ WIN | +0.37$ |
| 2026-07-11T00:51 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 10, 8:30PM-8:45PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-11T00:51 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 10, 8:30PM-8:45PM ET… | ✅ WIN | +0.38$ |
| 2026-07-11T00:51 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 10, 8:30PM-8:45PM ET… | ✅ WIN | +0.59$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T00:55 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,080.21 | 0.1min |  |
| ✅ ETH | $1,791.28 | 0.1min |  |
| ✅ SOL | $77.85 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,082.00 | consenso |  |
| ETH | $1,791.36 | consenso |  |
| SOL | $77.77 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*