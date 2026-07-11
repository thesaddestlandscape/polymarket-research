# Estado del bot — 2026-07-11 13:28 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **26.36 $** |
| P&L real total | 🟢 **+0.92 $** |
| P&L real hoy | +1.06 $ |
| P&L real 7 días | +18.37 $ |
| Fees pagados (real) | 7.30 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +951.84 $ |
| P&L sim compuesto | 🟢 +1465.86 $ (ficción Kelly: +5762% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +186.45 $ |
| Operaciones resueltas | 9214 (5156 WIN / 4058 LOSS) — 56.0% |
| Señales abiertas | 169 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3238 | 61.3% | +0.113 | ➡️ estable | +1050.95$ | 1.13$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 636 | 64.8% | +0.147 | 📉 agota (-0.03) | +276.61$ | 1.47$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 781 | 57.9% | +0.079 | 📈 madura (+0.03) | +168.78$ | 0.79$ | ✅ activa |
| STREAK_FADE_15M | 131 | 61.8% | +0.117 | 📈 madura (+0.12) | +19.89$ | 1.17$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 47 | 61.7% | +0.112 | 📈 madura (+0.17) | +10.38$ | 1.12$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 278 | 39.2% | -0.107 | 📈 madura (+0.11) | +7.78$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| UPDOWN_GBM | 1261 | 48.6% | -0.014 | ➡️ estable | +1.37$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 474 | 66.2% | +0.162 | ➡️ estable | -26.75$ | 1.62$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T13:18 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 11, 9:10AM-9:15AM ET… | ❌ LOSS | -0.66$ |
| 2026-07-11T13:18 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 11, 9:00AM-9:15AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-11T13:18 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 11, 9:00AM-9:15AM ET… | ✅ WIN | +0.32$ |
| 2026-07-11T13:18 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 11, 9:00AM-9:15AM ET… | ✅ WIN | +0.24$ |
| 2026-07-11T13:18 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 11, 9:00AM-9:15AM ET… | ✅ WIN | +2.37$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T13:27 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,150.29 | 0.1min |  |
| ✅ ETH | $1,800.38 | 0.1min |  |
| ✅ SOL | $78.24 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,165.10 | consenso |  |
| ETH | $1,800.38 | consenso |  |
| SOL | $78.16 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*