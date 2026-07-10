# Estado del bot — 2026-07-10 23:52 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **25.30 $** |
| P&L real total | 🔴 **-0.14 $** |
| P&L real hoy | -6.15 $ |
| P&L real 7 días | +2.11 $ |
| Fees pagados (real) | 7.27 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +827.16 $ |
| P&L sim compuesto | 🟢 +1279.41 $ (ficción Kelly: +5029% s/ operativo) |
| P&L sim hoy (2026-07-10) | 🟢 +367.47 $ |
| Operaciones resueltas | 8326 (4622 WIN / 3704 LOSS) — 55.5% |
| Señales abiertas | 190 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3040 | 61.4% | +0.114 | ➡️ estable | +976.32$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 470 | 67.2% | +0.172 | ➡️ estable | +215.88$ | 1.72$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 584 | 56.8% | +0.068 | 📈 madura (+0.05) | +99.79$ | 0.68$ | ✅ activa |
| STREAK_FADE_15M | 121 | 62.0% | +0.118 | 📈 madura (+0.13) | +18.64$ | 1.18$ | ✅ activa |
| ORDER_FLOW_5M | 1570 | 51.3% | +0.013 | ➡️ estable | +17.57$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 245 | 38.4% | -0.115 | 📈 madura (+0.08) | +7.87$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 31 | 61.3% | +0.106 | 📈 madura (+0.25) | +4.24$ | 1.06$ | ✅ activa |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| FAVORITO_CONFIRMADO | 227 | 69.2% | +0.190 | 📉 agota (-0.05) | +2.34$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM | 1246 | 48.5% | -0.015 | ➡️ estable | -3.59$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-10T23:50 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 10, 7:30PM-7:45PM ET… | ✅ WIN | +1.63$ |
| 2026-07-10T23:50 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 10, 7:30PM-7:45PM ET… | ❌ LOSS | -1.70$ |
| 2026-07-10T23:50 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 10, 7:30PM-7:45PM ET… | ❌ LOSS | -1.17$ |
| 2026-07-10T23:50 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 10, 7:30PM-7:45PM ET… | ✅ WIN | +1.56$ |
| 2026-07-10T23:50 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 10, 7:30PM-7:45PM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-10T23:51 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,114.29 | 0.1min |  |
| ✅ ETH | $1,795.12 | 0.1min |  |
| ✅ SOL | $78.10 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,124.10 | consenso |  |
| ETH | $1,795.19 | consenso |  |
| SOL | $78.06 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*