# Estado del bot — 2026-07-18 12:20 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **0.78 $** |
| P&L real total | 🔴 **-24.66 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -24.52 $ |
| Fees pagados (real) | 8.68 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +2694.69 $ |
| P&L sim compuesto | 🟢 +4818.45 $ (ficción Kelly: +18940% s/ operativo) |
| P&L sim hoy (2026-07-18) | 🟢 +313.68 $ |
| Operaciones resueltas | 20568 (12368 WIN / 8200 LOSS) — 60.1% |
| Señales abiertas | 95 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 5512 | 60.4% | +0.104 | ➡️ estable | +1783.35$ | 1.04$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 2736 | 65.0% | +0.150 | ➡️ estable | +1596.34$ | 1.50$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 2675 | 60.1% | +0.101 | 📈 madura (+0.03) | +918.78$ | 1.01$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 444 | 68.0% | +0.179 | ➡️ estable | +180.79$ | 1.79$ | ✅ activa |
| UPDOWN_GBM | 1756 | 51.8% | +0.018 | 📈 madura (+0.12) | +120.14$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 161 | 67.1% | +0.169 | 📈 madura (+0.11) | +94.41$ | 1.69$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| STREAK_FADE_15M | 218 | 60.6% | +0.105 | 📈 madura (+0.05) | +39.44$ | 1.04$ | ✅ activa |
| FAVORITO_CONFIRMADO | 3393 | 68.4% | +0.184 | ➡️ estable | +27.54$ | 1.84$ | ✅ activa |
| LATE_WINDOW_5MIN | 49 | 73.5% | +0.225 | ➡️ estable | +24.54$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 160 | 66.9% | +0.167 | ➡️ estable | +21.54$ | 1.67$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 174 | 55.7% | +0.057 | 📉 agota (-0.12) | +18.23$ | 0.57$ | ✅ activa |
| ORDER_FLOW_5M | 1630 | 51.3% | +0.013 | ➡️ estable | +14.21$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 47 | 83.0% | +0.316 | 📈 madura (+0.09) | +12.81$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 326 | 38.3% | -0.116 | ➡️ estable | +3.81$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 113 | 81.4% | +0.309 | ➡️ estable | +3.57$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 3 | 66.7% | +0.015 | — | +0.37$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_5M | 13 | 53.8% | +0.022 | — | -0.28$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 149 | 32.9% | -0.169 | 📉 agota (-0.12) | -4.27$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-18T12:19 | BALLENAS_CONFIRMADAS_15M#XRP#15min | XRP Up or Down - July 18, 8:00AM-8:15AM ET… | ❌ LOSS | -0.97$ |
| 2026-07-18T12:19 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 18, 8:00AM-8:15AM ET… | ✅ WIN | +2.04$ |
| 2026-07-18T12:19 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 18, 8:00AM-8:15AM ET… | ✅ WIN | +2.04$ |
| 2026-07-18T12:19 | UPDOWN_GBM_15M_TARDIO#XRP#15min | XRP Up or Down - July 18, 8:00AM-8:15AM ET… | ✅ WIN | +2.00$ |
| 2026-07-18T12:19 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 18, 8:00AM-8:15AM ET… | ✅ WIN | +2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-18T12:19 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,088.04 | 0.1min |  |
| ✅ ETH | $1,845.29 | 0.1min |  |
| ✅ SOL | $74.87 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,090.00 | consenso |  |
| ETH | $1,845.35 | consenso |  |
| SOL | $74.95 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*