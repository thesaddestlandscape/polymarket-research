# Estado del bot — 2026-07-20 11:38 UTC

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
| P&L fiel (stake fijo 1$) | +3371.53 $ |
| P&L sim compuesto | 🟢 +6212.77 $ (ficción Kelly: +24421% s/ operativo) |
| P&L sim hoy (2026-07-20) | 🟢 +214.44 $ |
| Operaciones resueltas | 24458 (14869 WIN / 9589 LOSS) — 60.8% |
| Señales abiertas | 123 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6135 | 60.7% | +0.107 | ➡️ estable | +2138.59$ | 1.07$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3354 | 65.3% | +0.153 | ➡️ estable | +2062.04$ | 1.53$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3323 | 60.2% | +0.102 | 📈 madura (+0.04) | +1231.62$ | 1.02$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 785 | 67.1% | +0.171 | 📉 agota (-0.03) | +351.30$ | 1.71$ | ✅ activa |
| UPDOWN_GBM | 1937 | 51.9% | +0.019 | 📈 madura (+0.11) | +128.85$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 182 | 65.9% | +0.158 | 📈 madura (+0.09) | +97.69$ | 1.58$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4206 | 68.7% | +0.187 | ➡️ estable | +82.67$ | 1.87$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| STREAK_FADE_15M | 235 | 60.0% | +0.099 | ➡️ estable | +38.58$ | 0.99$ | ✅ activa |
| LATE_WINDOW_5MIN | 56 | 71.4% | +0.207 | 📈 madura (+0.07) | +25.91$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 201 | 57.2% | +0.071 | ➡️ estable | +22.02$ | 0.71$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 428 | 63.8% | +0.137 | ➡️ estable | +16.52$ | 1.37$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 83 | 79.5% | +0.288 | 📉 agota (-0.11) | +15.82$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1638 | 51.2% | +0.012 | ➡️ estable | +13.23$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 179 | 82.7% | +0.323 | ➡️ estable | +11.90$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 221 | 52.0% | +0.020 | 📉 agota (-0.16) | +11.35$ | 0.50$ | ✅ activa |
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
| 2026-07-20T11:37 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 20, 7:30AM-7:35AM ET… | ✅ WIN | +2.00$ |
| 2026-07-20T11:34 | UPDOWN_GBM_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 20, 7:15AM-7:30AM ET… | ❌ LOSS | -1.08$ |
| 2026-07-20T11:34 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 20, 7:15AM-7:30AM ET… | ✅ WIN | +0.63$ |
| 2026-07-20T11:34 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 20, 7:15AM-7:30AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-20T11:34 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 20, 7:15AM-7:30AM ET… | ✅ WIN | +0.97$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-20T11:36 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,688.01 | 0.1min |  |
| ✅ ETH | $1,885.02 | 0.1min |  |
| ✅ SOL | $77.03 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,688.01 | consenso |  |
| ETH | $1,884.83 | consenso |  |
| SOL | $76.70 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*