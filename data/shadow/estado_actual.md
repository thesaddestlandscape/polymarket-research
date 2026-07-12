# Estado del bot — 2026-07-12 23:33 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **13.03 $** |
| P&L real total | 🔴 **-12.41 $** |
| P&L real hoy | -4.96 $ |
| P&L real 7 días | +5.05 $ |
| Fees pagados (real) | 7.72 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1342.10 $ |
| P&L sim compuesto | 🟢 +2199.18 $ (ficción Kelly: +8645% s/ operativo) |
| P&L sim hoy (2026-07-12) | 🟢 +594.47 $ |
| Operaciones resueltas | 11601 (6649 WIN / 4952 LOSS) — 57.3% |
| Señales abiertas | 137 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3731 | 61.2% | +0.112 | ➡️ estable | +1230.29$ | 1.12$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1079 | 66.3% | +0.162 | ➡️ estable | +634.49$ | 1.62$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1216 | 58.1% | +0.080 | 📈 madura (+0.03) | +302.96$ | 0.81$ | ✅ activa |
| UPDOWN_GBM | 1349 | 49.6% | -0.004 | 📈 madura (+0.07) | +29.92$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_15M | 159 | 62.3% | +0.121 | 📈 madura (+0.20) | +24.84$ | 1.21$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 73 | 61.6% | +0.113 | 📉 agota (-0.04) | +18.00$ | 1.13$ | ✅ activa |
| ORDER_FLOW_5M | 1586 | 51.3% | +0.013 | ➡️ estable | +16.48$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 317 | 38.8% | -0.111 | ➡️ estable | +7.10$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 1085 | 68.2% | +0.182 | 📈 madura (+0.06) | +4.84$ | 1.81$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM | 138 | 34.8% | -0.150 | 📉 agota (-0.11) | +0.19$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 176 | 47.2% | -0.028 | ➡️ estable | -9.16$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 204 | 57.4% | +0.073 | 📈 madura (+0.24) | -13.93$ | 0.73$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-12T23:32 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 12, 7:15PM-7:30PM ET… | ✅ WIN | +1.92$ |
| 2026-07-12T23:32 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 12, 7:15PM-7:30PM ET… | ✅ WIN | +2.67$ |
| 2026-07-12T23:32 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 12, 7:15PM-7:30PM ET… | ✅ WIN | +2.28$ |
| 2026-07-12T23:32 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 12, 7:15PM-7:30PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-12T23:32 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 12, 7:15PM-7:30PM ET… | ❌ LOSS | -1.33$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-12T23:32 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,761.99 | 0.1min |  |
| ✅ ETH | $1,802.26 | 0.1min |  |
| ✅ SOL | $76.78 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,765.60 | consenso |  |
| ETH | $1,802.26 | consenso |  |
| SOL | $76.70 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*