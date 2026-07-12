# Estado del bot — 2026-07-12 08:00 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **15.24 $** |
| P&L real total | 🔴 **-10.20 $** |
| P&L real hoy | -2.75 $ |
| P&L real 7 días | +7.26 $ |
| Fees pagados (real) | 7.61 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1151.61 $ |
| P&L sim compuesto | 🟢 +1808.12 $ (ficción Kelly: +7107% s/ operativo) |
| P&L sim hoy (2026-07-12) | 🟢 +203.41 $ |
| Operaciones resueltas | 10625 (6026 WIN / 4599 LOSS) — 56.7% |
| Señales abiertas | 138 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3512 | 61.3% | +0.113 | ➡️ estable | +1131.08$ | 1.13$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 879 | 65.6% | +0.156 | 📉 agota (-0.03) | +426.05$ | 1.56$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1054 | 58.0% | +0.080 | ➡️ estable | +237.24$ | 0.80$ | ✅ activa |
| UPDOWN_GBM | 1310 | 49.2% | -0.008 | 📈 madura (+0.05) | +20.42$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_15M | 149 | 61.7% | +0.116 | 📈 madura (+0.17) | +19.64$ | 1.16$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 63 | 61.9% | +0.115 | ➡️ estable | +18.14$ | 1.15$ | ✅ activa |
| ORDER_FLOW_5M | 1584 | 51.3% | +0.013 | ➡️ estable | +17.50$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 309 | 38.5% | -0.114 | ➡️ estable | +6.62$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 805 | 68.2% | +0.182 | ➡️ estable | +4.25$ | 1.81$ | ✅ activa |
| RESOLUTION_SNIPER | 9 | 100.0% | +0.184 | — | +3.91$ | 1.84$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 136 | 34.6% | -0.152 | 📉 agota (-0.13) | -0.14$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 146 | 43.8% | -0.061 | 📉 agota (-0.16) | -12.68$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 192 | 57.8% | +0.077 | 📈 madura (+0.23) | -13.59$ | 0.77$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-12T08:00 | UPDOWN_GBM#ETH#15min | Ethereum Up or Down - July 12, 3:45AM-4:00AM ET… | ✅ WIN | +0.47$ |
| 2026-07-12T08:00 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 12, 3:50AM-3:55AM ET… | ✅ WIN | +1.02$ |
| 2026-07-12T08:00 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 12, 3:45AM-4:00AM ET… | ✅ WIN | +0.57$ |
| 2026-07-12T08:00 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 12, 3:45AM-4:00AM ET… | ✅ WIN | +1.92$ |
| 2026-07-12T08:00 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 12, 3:45AM-4:00AM ET… | ✅ WIN | +1.46$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-12T07:59 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,839.91 | 0.1min |  |
| ✅ ETH | $1,797.47 | 0.1min |  |
| ✅ SOL | $76.52 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,840.90 | consenso |  |
| ETH | $1,797.47 | consenso |  |
| SOL | $76.47 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*