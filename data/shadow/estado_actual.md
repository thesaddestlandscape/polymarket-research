# Estado del bot — 2026-07-12 15:30 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **14.13 $** |
| P&L real total | 🔴 **-11.31 $** |
| P&L real hoy | -3.85 $ |
| P&L real 7 días | +6.15 $ |
| Fees pagados (real) | 7.67 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1268.89 $ |
| P&L sim compuesto | 🟢 +2053.44 $ (ficción Kelly: +8072% s/ operativo) |
| P&L sim hoy (2026-07-12) | 🟢 +448.73 $ |
| Operaciones resueltas | 11079 (6331 WIN / 4748 LOSS) — 57.1% |
| Señales abiertas | 149 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3615 | 61.4% | +0.114 | ➡️ estable | +1203.41$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 974 | 66.6% | +0.166 | ➡️ estable | +543.08$ | 1.66$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1136 | 58.3% | +0.083 | ➡️ estable | +283.46$ | 0.83$ | ✅ activa |
| UPDOWN_GBM | 1328 | 49.4% | -0.006 | 📈 madura (+0.06) | +28.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_15M | 154 | 62.3% | +0.122 | 📈 madura (+0.18) | +24.62$ | 1.22$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 67 | 62.7% | +0.123 | 📈 madura (+0.04) | +20.42$ | 1.23$ | ✅ activa |
| ORDER_FLOW_5M | 1584 | 51.3% | +0.013 | ➡️ estable | +17.50$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 311 | 38.6% | -0.113 | ➡️ estable | +5.66$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 9 | 100.0% | +0.184 | — | +3.91$ | 1.84$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 136 | 34.6% | -0.152 | 📉 agota (-0.13) | -0.14$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 934 | 68.0% | +0.179 | ➡️ estable | -1.18$ | 1.79$ | ✅ activa |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 161 | 45.3% | -0.046 | 📉 agota (-0.07) | -11.84$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 192 | 57.8% | +0.077 | 📈 madura (+0.23) | -13.59$ | 0.77$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-12T15:18 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 12, 11:00AM-11:15AM ET… | ✅ WIN | +2.67$ |
| 2026-07-12T15:18 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 12, 11:00AM-11:15AM ET… | ✅ WIN | +1.85$ |
| 2026-07-12T15:18 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 12, 11:00AM-11:15AM ET… | ✅ WIN | +2.05$ |
| 2026-07-12T15:18 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 12, 11:00AM-11:15AM ET… | ✅ WIN | +1.92$ |
| 2026-07-12T15:18 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 12, 11:00AM-11:15AM ET… | ✅ WIN | +3.59$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-12T15:29 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,169.02 | 0.1min |  |
| ✅ ETH | $1,821.69 | 0.1min |  |
| ✅ SOL | $77.48 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,169.20 | consenso |  |
| ETH | $1,821.69 | consenso |  |
| SOL | $77.45 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*