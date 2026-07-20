# Estado del bot — 2026-07-20 12:58 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **0.78 $** |
| P&L real total | 🔴 **-24.66 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -13.66 $ |
| Fees pagados (real) | 8.68 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3391.42 $ |
| P&L sim compuesto | 🟢 +6247.68 $ (ficción Kelly: +24558% s/ operativo) |
| P&L sim hoy (2026-07-20) | 🟢 +249.35 $ |
| Operaciones resueltas | 24546 (14928 WIN / 9618 LOSS) — 60.8% |
| Señales abiertas | 127 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6151 | 60.7% | +0.107 | ➡️ estable | +2145.63$ | 1.07$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3365 | 65.3% | +0.153 | ➡️ estable | +2073.37$ | 1.53$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3336 | 60.2% | +0.102 | 📈 madura (+0.04) | +1231.98$ | 1.02$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 790 | 67.2% | +0.172 | ➡️ estable | +356.93$ | 1.72$ | ✅ activa |
| UPDOWN_GBM | 1939 | 52.0% | +0.020 | 📈 madura (+0.11) | +130.04$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 182 | 65.9% | +0.158 | 📈 madura (+0.09) | +97.69$ | 1.58$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4234 | 68.7% | +0.187 | ➡️ estable | +87.95$ | 1.87$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| STREAK_FADE_15M | 235 | 60.0% | +0.099 | ➡️ estable | +38.58$ | 0.99$ | ✅ activa |
| LATE_WINDOW_5MIN | 57 | 71.9% | +0.212 | 📈 madura (+0.08) | +28.08$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 204 | 56.9% | +0.068 | ➡️ estable | +21.25$ | 0.68$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 434 | 63.8% | +0.138 | ➡️ estable | +17.54$ | 1.38$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 83 | 79.5% | +0.288 | 📉 agota (-0.11) | +15.82$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1638 | 51.2% | +0.012 | ➡️ estable | +13.23$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 181 | 82.9% | +0.325 | ➡️ estable | +12.89$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 222 | 52.3% | +0.022 | 📉 agota (-0.16) | +12.02$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 6 | 66.7% | +0.037 | — | +0.87$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-20T12:46 | GBM_LATE_5M#ETH#5min | Ethereum Up or Down - July 20, 8:40AM-8:45AM ET… | ✅ WIN | +2.05$ |
| 2026-07-20T12:46 | UPDOWN_GBM_15M_TARDIO#XRP#15min | XRP Up or Down - July 20, 8:30AM-8:45AM ET… | ✅ WIN | +2.00$ |
| 2026-07-20T12:46 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 20, 8:30AM-8:45AM ET… | ✅ WIN | +2.00$ |
| 2026-07-20T12:46 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 20, 8:30AM-8:45AM ET… | ✅ WIN | +2.00$ |
| 2026-07-20T12:46 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 20, 8:30AM-8:45AM ET… | ✅ WIN | +3.76$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-20T12:56 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,637.82 | 0.1min |  |
| ✅ ETH | $1,872.54 | 0.1min |  |
| ✅ SOL | $76.76 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,638.80 | consenso |  |
| ETH | $1,872.54 | consenso |  |
| SOL | $76.74 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*