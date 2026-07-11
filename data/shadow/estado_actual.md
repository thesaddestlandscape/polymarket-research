# Estado del bot — 2026-07-11 11:49 UTC

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
| P&L fiel (stake fijo 1$) | +940.64 $ |
| P&L sim compuesto | 🟢 +1447.38 $ (ficción Kelly: +5689% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +167.98 $ |
| Operaciones resueltas | 9109 (5090 WIN / 4019 LOSS) — 55.9% |
| Señales abiertas | 164 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3216 | 61.3% | +0.113 | ➡️ estable | +1044.05$ | 1.13$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 615 | 64.7% | +0.147 | 📉 agota (-0.04) | +269.47$ | 1.47$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 759 | 57.7% | +0.077 | ➡️ estable | +163.32$ | 0.77$ | ✅ activa |
| STREAK_FADE_15M | 130 | 62.3% | +0.121 | 📈 madura (+0.13) | +20.40$ | 1.21$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 47 | 61.7% | +0.112 | 📈 madura (+0.17) | +10.38$ | 1.12$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 274 | 39.4% | -0.105 | 📈 madura (+0.12) | +9.05$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM | 1257 | 48.5% | -0.015 | ➡️ estable | -0.24$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 443 | 66.4% | +0.163 | 📉 agota (-0.07) | -25.89$ | 1.63$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T11:47 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 11, 7:30AM-7:45AM ET… | ❌ LOSS | -1.12$ |
| 2026-07-11T11:47 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 11, 7:30AM-7:45AM ET… | ✅ WIN | +1.92$ |
| 2026-07-11T11:47 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 11, 7:30AM-7:45AM ET… | ✅ WIN | +0.22$ |
| 2026-07-11T11:47 | UPDOWN_GBM#ETH#15min | Ethereum Up or Down - July 11, 7:30AM-7:45AM ET… | ✅ WIN | +1.71$ |
| 2026-07-11T11:47 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 11, 7:30AM-7:45AM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T11:48 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,143.56 | 0.1min |  |
| ✅ ETH | $1,797.86 | 0.1min |  |
| ✅ SOL | $78.11 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,143.56 | consenso |  |
| ETH | $1,797.86 | consenso |  |
| SOL | $78.02 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*