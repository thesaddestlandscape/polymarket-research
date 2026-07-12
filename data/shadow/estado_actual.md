# Estado del bot — 2026-07-12 23:55 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **14.44 $** |
| P&L real total | 🔴 **-11.00 $** |
| P&L real hoy | -3.55 $ |
| P&L real 7 días | +6.45 $ |
| Fees pagados (real) | 7.77 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1350.82 $ |
| P&L sim compuesto | 🟢 +2213.47 $ (ficción Kelly: +8701% s/ operativo) |
| P&L sim hoy (2026-07-12) | 🟢 +608.76 $ |
| Operaciones resueltas | 11619 (6664 WIN / 4955 LOSS) — 57.4% |
| Señales abiertas | 144 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3735 | 61.2% | +0.112 | ➡️ estable | +1233.38$ | 1.12$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1082 | 66.4% | +0.163 | ➡️ estable | +640.26$ | 1.63$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1217 | 58.1% | +0.081 | 📈 madura (+0.03) | +303.88$ | 0.81$ | ✅ activa |
| UPDOWN_GBM | 1350 | 49.6% | -0.004 | 📈 madura (+0.08) | +31.32$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_15M | 159 | 62.3% | +0.121 | 📈 madura (+0.20) | +24.84$ | 1.21$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 74 | 62.2% | +0.118 | 📉 agota (-0.05) | +19.84$ | 1.18$ | ✅ activa |
| ORDER_FLOW_5M | 1586 | 51.3% | +0.013 | ➡️ estable | +16.48$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 317 | 38.8% | -0.111 | ➡️ estable | +7.10$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 1091 | 68.2% | +0.182 | 📈 madura (+0.06) | +4.75$ | 1.81$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM | 138 | 34.8% | -0.150 | 📉 agota (-0.11) | +0.19$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 178 | 47.8% | -0.022 | ➡️ estable | -7.82$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 204 | 57.4% | +0.073 | 📈 madura (+0.24) | -13.93$ | 0.73$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-12T23:55 | STREAK_FADE_5M#XRP#5min | XRP Up or Down - July 12, 7:50PM-7:55PM ET… | ✅ WIN | +0.85$ |
| 2026-07-12T23:53 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 12, 7:45PM-7:50PM ET… | ✅ WIN | +0.72$ |
| 2026-07-12T23:51 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 12, 7:45PM-7:50PM ET… | ✅ WIN | +1.00$ |
| 2026-07-12T23:47 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 12, 7:30PM-7:45PM ET… | ✅ WIN | +1.11$ |
| 2026-07-12T23:47 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 12, 7:30PM-7:45PM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-12T23:54 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,744.49 | 0.1min |  |
| ✅ ETH | $1,806.12 | 0.1min |  |
| ✅ SOL | $76.93 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,747.90 | consenso |  |
| ETH | $1,806.12 | consenso |  |
| SOL | $76.80 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*