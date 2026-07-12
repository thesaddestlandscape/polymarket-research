# Estado del bot — 2026-07-12 03:26 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **17.99 $** |
| P&L real total | 🔴 **-7.45 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | +10.01 $ |
| Fees pagados (real) | 7.61 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1080.75 $ |
| P&L sim compuesto | 🟢 +1677.58 $ (ficción Kelly: +6594% s/ operativo) |
| P&L sim hoy (2026-07-12) | 🟢 +72.87 $ |
| Operaciones resueltas | 10253 (5787 WIN / 4466 LOSS) — 56.4% |
| Señales abiertas | 152 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3443 | 61.2% | +0.112 | ➡️ estable | +1097.94$ | 1.12$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 814 | 64.9% | +0.148 | 📉 agota (-0.03) | +368.23$ | 1.48$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 985 | 57.7% | +0.076 | ➡️ estable | +211.78$ | 0.77$ | ✅ activa |
| STREAK_FADE_15M | 144 | 61.1% | +0.110 | 📈 madura (+0.16) | +19.13$ | 1.10$ | ✅ activa |
| ORDER_FLOW_5M | 1579 | 51.4% | +0.014 | ➡️ estable | +18.78$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 60 | 63.3% | +0.129 | ➡️ estable | +18.77$ | 1.29$ | ✅ activa |
| UPDOWN_GBM | 1299 | 49.1% | -0.009 | 📈 madura (+0.05) | +14.99$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 304 | 38.8% | -0.111 | ➡️ estable | +8.65$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 136 | 34.6% | -0.152 | 📉 agota (-0.13) | -0.14$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 89 | 48.3% | -0.016 | 📉 agota (-0.16) | -3.81$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 192 | 57.8% | +0.077 | 📈 madura (+0.23) | -13.59$ | 0.77$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 723 | 67.1% | +0.170 | ➡️ estable | -16.28$ | 1.70$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-12T03:16 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 11, 11:00PM-11:15PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-12T03:16 | UPDOWN_GBM#ETH#15min | Ethereum Up or Down - July 11, 11:00PM-11:15PM ET… | ❌ LOSS | -1.20$ |
| 2026-07-12T03:16 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 11, 11:00PM-11:15PM ET… | ❌ LOSS | -0.91$ |
| 2026-07-12T03:16 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 11, 11:00PM-11:15PM ET… | ✅ WIN | +1.50$ |
| 2026-07-12T03:16 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 11, 11:00PM-11:15PM ET… | ❌ LOSS | -1.56$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-12T03:25 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,091.21 | 0.1min |  |
| ✅ ETH | $1,805.88 | 0.1min |  |
| ✅ SOL | $76.95 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,091.21 | consenso |  |
| ETH | $1,805.88 | consenso |  |
| SOL | $76.88 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*