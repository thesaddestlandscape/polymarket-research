# Estado del bot — 2026-07-10 19:01 UTC

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
| P&L fiel (stake fijo 1$) | +769.52 $ |
| P&L sim compuesto | 🟢 +1190.96 $ (ficción Kelly: +4681% s/ operativo) |
| P&L sim hoy (2026-07-10) | 🟢 +279.03 $ |
| Operaciones resueltas | 7996 (4410 WIN / 3586 LOSS) — 55.2% |
| Señales abiertas | 187 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2964 | 61.4% | +0.114 | ➡️ estable | +958.66$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 410 | 66.6% | +0.165 | 📈 madura (+0.06) | +172.22$ | 1.65$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 510 | 56.7% | +0.066 | 📈 madura (+0.08) | +85.50$ | 0.66$ | ✅ activa |
| ORDER_FLOW_5M | 1570 | 51.3% | +0.013 | ➡️ estable | +17.57$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 118 | 61.0% | +0.108 | 📈 madura (+0.13) | +16.00$ | 1.08$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 236 | 37.7% | -0.122 | 📈 madura (+0.06) | +5.29$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 28 | 60.7% | +0.100 | — | +3.21$ | 1.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 140 | 70.0% | +0.197 | 📉 agota (-0.06) | -1.79$ | 1.97$ | ✅ activa |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| UPDOWN_GBM | 1228 | 48.4% | -0.016 | ➡️ estable | -6.03$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-10T19:00 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 10, 2:45PM-3:00PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-10T19:00 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 10, 2:45PM-3:00PM ET… | ❌ LOSS | -0.88$ |
| 2026-07-10T19:00 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 10, 2:45PM-3:00PM ET… | ✅ WIN | +0.90$ |
| 2026-07-10T19:00 | GBM_LATE_60M#ETH#60min | Ethereum Up or Down - July 10, 2PM ET… | ✅ WIN | +0.94$ |
| 2026-07-10T19:00 | FAVORITO_CONFIRMADO#ETH#60min | Ethereum Up or Down - July 10, 2PM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-10T19:00 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,748.82 | 0.1min |  |
| ✅ ETH | $1,783.26 | 0.1min |  |
| ✅ SOL | $77.48 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,751.00 | consenso |  |
| ETH | $1,783.26 | consenso |  |
| SOL | $77.40 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*