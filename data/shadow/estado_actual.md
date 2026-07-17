# Estado del bot — 2026-07-17 03:56 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **2.94 $** |
| P&L real total | 🔴 **-22.50 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -28.51 $ |
| Fees pagados (real) | 8.61 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +2173.05 $ |
| P&L sim compuesto | 🟢 +3819.68 $ (ficción Kelly: +15014% s/ operativo) |
| P&L sim hoy (2026-07-17) | 🟢 +98.61 $ |
| Operaciones resueltas | 18057 (10680 WIN / 7377 LOSS) — 59.1% |
| Señales abiertas | 74 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 5100 | 60.2% | +0.102 | ➡️ estable | +1590.90$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 2307 | 65.0% | +0.150 | 📉 agota (-0.04) | +1328.86$ | 1.50$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 2285 | 59.5% | +0.095 | ➡️ estable | +717.87$ | 0.95$ | ✅ activa |
| UPDOWN_GBM | 1634 | 51.0% | +0.010 | 📈 madura (+0.09) | +72.80$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 202 | 66.8% | +0.167 | 📉 agota (-0.07) | +59.66$ | 1.67$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 119 | 64.7% | +0.145 | 📈 madura (+0.14) | +59.15$ | 1.45$ | ✅ activa |
| STREAK_FADE_15M | 207 | 60.4% | +0.103 | 📈 madura (+0.04) | +32.94$ | 1.03$ | ✅ activa |
| WEEKLY_PRICE | 273 | 63.7% | +0.136 | 📈 madura (+0.26) | +29.85$ | 1.36$ | ✅ activa |
| LATE_WINDOW_5MIN | 47 | 74.5% | +0.235 | ➡️ estable | +24.66$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 155 | 56.8% | +0.067 | 📉 agota (-0.13) | +20.66$ | 0.67$ | ✅ activa |
| ORDER_FLOW_5M | 1621 | 51.3% | +0.013 | ➡️ estable | +15.01$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 26 | 80.8% | +0.286 | — | +3.85$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 326 | 38.3% | -0.116 | ➡️ estable | +3.81$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 63 | 82.5% | +0.315 | 📈 madura (+0.04) | +2.77$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_5M | 11 | 45.5% | -0.021 | — | -0.62$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 148 | 33.1% | -0.167 | 📉 agota (-0.12) | -3.76$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 2819 | 67.5% | +0.175 | ➡️ estable | -52.19$ | 1.75$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-17T03:51 | ORDER_FLOW_5M#XRP#5min | XRP Up or Down - July 16, 11:45PM-11:50PM ET… | ✅ WIN | +0.47$ |
| 2026-07-17T03:47 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 16, 11:30PM-11:45PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-17T03:47 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 16, 11:30PM-11:45PM ET… | ❌ LOSS | -1.23$ |
| 2026-07-17T03:47 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 16, 11:30PM-11:45PM ET… | ❌ LOSS | -1.23$ |
| 2026-07-17T03:47 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 16, 11:30PM-11:45PM ET… | ✅ WIN | +1.92$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-17T03:55 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,503.06 | 0.1min |  |
| ✅ ETH | $1,850.91 | 0.1min |  |
| ✅ SOL | $75.23 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,504.50 | consenso |  |
| ETH | $1,851.12 | consenso |  |
| SOL | $75.15 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*