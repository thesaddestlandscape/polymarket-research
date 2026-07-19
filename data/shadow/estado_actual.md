# Estado del bot — 2026-07-19 07:55 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **0.78 $** |
| P&L real total | 🔴 **-24.66 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -17.21 $ |
| Fees pagados (real) | 8.68 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +2970.05 $ |
| P&L sim compuesto | 🟢 +5376.89 $ (ficción Kelly: +21136% s/ operativo) |
| P&L sim hoy (2026-07-19) | 🟢 +215.13 $ |
| Operaciones resueltas | 22150 (13403 WIN / 8747 LOSS) — 60.5% |
| Señales abiertas | 138 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 5759 | 60.7% | +0.107 | ➡️ estable | +1937.39$ | 1.07$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 2990 | 65.3% | +0.153 | ➡️ estable | +1775.02$ | 1.53$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 2934 | 60.1% | +0.100 | 📈 madura (+0.03) | +1020.29$ | 1.01$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 597 | 68.7% | +0.186 | ➡️ estable | +278.62$ | 1.86$ | ✅ activa |
| UPDOWN_GBM | 1817 | 52.0% | +0.020 | 📈 madura (+0.13) | +129.23$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 168 | 65.5% | +0.153 | 📈 madura (+0.07) | +89.40$ | 1.53$ | ✅ activa |
| FAVORITO_CONFIRMADO | 3725 | 68.6% | +0.186 | ➡️ estable | +55.61$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| STREAK_FADE_15M | 223 | 59.6% | +0.096 | ➡️ estable | +33.70$ | 0.96$ | ✅ activa |
| LATE_WINDOW_5MIN | 49 | 73.5% | +0.225 | ➡️ estable | +24.54$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 285 | 64.2% | +0.141 | 📉 agota (-0.05) | +15.88$ | 1.41$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 190 | 54.2% | +0.042 | 📉 agota (-0.09) | +15.05$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1631 | 51.3% | +0.013 | ➡️ estable | +13.70$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 60 | 78.3% | +0.274 | 📉 agota (-0.03) | +10.45$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 143 | 81.8% | +0.314 | ➡️ estable | +7.34$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 327 | 38.5% | -0.114 | ➡️ estable | +6.13$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_5M | 90 | 57.8% | +0.076 | ➡️ estable | +4.82$ | 0.76$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 4 | 75.0% | +0.033 | — | +0.88$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
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
| 2026-07-19T07:51 | BALLENAS_CONFIRMADAS_15M#XRP#15min | XRP Up or Down - July 19, 3:30AM-3:45AM ET… | ❌ LOSS | -0.92$ |
| 2026-07-19T07:51 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 19, 3:30AM-3:45AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-19T07:51 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 19, 3:30AM-3:45AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-19T07:51 | UPDOWN_GBM_15M_TARDIO#XRP#15min | XRP Up or Down - July 19, 3:30AM-3:45AM ET… | ✅ WIN | +2.17$ |
| 2026-07-19T07:51 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 19, 3:30AM-3:45AM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-19T07:53 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,668.64 | 0.1min |  |
| ✅ ETH | $1,868.11 | 0.1min |  |
| ✅ SOL | $76.15 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,678.90 | consenso |  |
| ETH | $1,868.58 | consenso |  |
| SOL | $76.14 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*