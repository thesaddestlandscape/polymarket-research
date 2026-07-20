# Estado del bot — 2026-07-20 15:32 UTC

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
| P&L fiel (stake fijo 1$) | +3409.48 $ |
| P&L sim compuesto | 🟢 +6277.89 $ (ficción Kelly: +24677% s/ operativo) |
| P&L sim hoy (2026-07-20) | 🟢 +279.57 $ |
| Operaciones resueltas | 24754 (15050 WIN / 9704 LOSS) — 60.8% |
| Señales abiertas | 135 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6185 | 60.7% | +0.107 | ➡️ estable | +2151.97$ | 1.07$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3398 | 65.4% | +0.154 | ➡️ estable | +2103.06$ | 1.53$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3372 | 60.1% | +0.100 | 📈 madura (+0.03) | +1228.71$ | 1.01$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 809 | 66.9% | +0.168 | 📉 agota (-0.03) | +359.25$ | 1.68$ | ✅ activa |
| UPDOWN_GBM | 1958 | 52.1% | +0.021 | 📈 madura (+0.11) | +134.23$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 182 | 65.9% | +0.158 | 📈 madura (+0.09) | +97.69$ | 1.58$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4271 | 68.6% | +0.186 | ➡️ estable | +78.57$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| STREAK_FADE_15M | 235 | 60.0% | +0.099 | ➡️ estable | +38.58$ | 0.99$ | ✅ activa |
| LATE_WINDOW_5MIN | 59 | 72.9% | +0.221 | 📈 madura (+0.07) | +31.00$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 211 | 56.9% | +0.068 | ➡️ estable | +21.93$ | 0.68$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 85 | 80.0% | +0.293 | 📉 agota (-0.11) | +16.42$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 446 | 63.9% | +0.138 | ➡️ estable | +16.00$ | 1.38$ | ✅ activa |
| ORDER_FLOW_5M | 1638 | 51.2% | +0.012 | ➡️ estable | +13.23$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 224 | 52.2% | +0.022 | 📉 agota (-0.15) | +12.64$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 186 | 82.3% | +0.319 | ➡️ estable | +9.93$ | 2.00$ | ✅ activa |
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
| 2026-07-20T15:30 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 20, 11:15AM-11:30AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-20T15:30 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 20, 11:15AM-11:30AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-20T15:30 | LEADLAG_BTC_XRP_15M#XRP#15min | XRP Up or Down - July 20, 11:15AM-11:30AM ET… | ❌ LOSS | -0.56$ |
| 2026-07-20T15:30 | FAVORITO_CONFIRMADO#XRP#15min | XRP Up or Down - July 20, 11:15AM-11:30AM ET… | ✅ WIN | +0.36$ |
| 2026-07-20T15:30 | BALLENAS_CONFIRMADAS_15M#XRP#15min | XRP Up or Down - July 20, 11:15AM-11:30AM ET… | ✅ WIN | +0.90$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-20T15:30 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,884.07 | 0.1min |  |
| ✅ ETH | $1,883.01 | 0.1min |  |
| ✅ SOL | $77.05 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,884.07 | consenso |  |
| ETH | $1,883.01 | consenso |  |
| SOL | $76.94 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*