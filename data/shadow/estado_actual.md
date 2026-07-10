# Estado del bot — 2026-07-10 12:49 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **26.01 $** |
| P&L real total | 🟢 **+0.57 $** |
| P&L real hoy | -5.44 $ |
| P&L real 7 días | +2.82 $ |
| Fees pagados (real) | 7.14 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +701.55 $ |
| P&L sim compuesto | 🟢 +1087.04 $ (ficción Kelly: +4273% s/ operativo) |
| P&L sim hoy (2026-07-10) | 🟢 +175.10 $ |
| Operaciones resueltas | 7570 (4131 WIN / 3439 LOSS) — 54.6% |
| Señales abiertas | 167 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2870 | 61.3% | +0.113 | ➡️ estable | +929.43$ | 1.13$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 333 | 65.2% | +0.151 | ➡️ estable | +120.88$ | 1.51$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 416 | 55.3% | +0.053 | 📈 madura (+0.06) | +58.57$ | 0.53$ | ✅ activa |
| ORDER_FLOW_5M | 1570 | 51.3% | +0.013 | ➡️ estable | +17.57$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 113 | 59.3% | +0.091 | 📈 madura (+0.08) | +11.63$ | 0.91$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 224 | 38.8% | -0.111 | 📈 madura (+0.08) | +9.17$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| UPDOWN_GBM | 1212 | 48.6% | -0.014 | ➡️ estable | +1.31$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 24 | 54.2% | +0.038 | — | +0.89$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| FAVORITO_CONFIRMADO | 34 | 70.6% | +0.194 | 📉 agota (-0.21) | -0.16$ | 1.94$ | ✅ activa |
| PRICE_TARGET_GBM | 132 | 34.1% | -0.157 | 📉 agota (-0.10) | -0.77$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 159 | 55.3% | +0.053 | 📈 madura (+0.14) | -15.64$ | 0.53$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-10T12:45 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 10, 8:30AM-8:45AM ET… | ✅ WIN | +2.00$ |
| 2026-07-10T12:45 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 10, 8:30AM-8:45AM ET… | ❌ LOSS | -0.80$ |
| 2026-07-10T12:45 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 10, 8:30AM-8:45AM ET… | ✅ WIN | +0.16$ |
| 2026-07-10T12:45 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 10, 8:30AM-8:45AM ET… | ✅ WIN | +1.24$ |
| 2026-07-10T12:45 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 10, 8:30AM-8:45AM ET… | ✅ WIN | +0.39$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-10T12:48 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,313.79 | 0.1min |  |
| ✅ ETH | $1,793.83 | 0.1min |  |
| ✅ SOL | $78.96 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,325.20 | consenso |  |
| ETH | $1,793.83 | consenso |  |
| SOL | $78.96 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*