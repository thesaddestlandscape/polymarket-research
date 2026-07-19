# Estado del bot — 2026-07-19 11:18 UTC

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
| P&L fiel (stake fijo 1$) | +3007.60 $ |
| P&L sim compuesto | 🟢 +5450.95 $ (ficción Kelly: +21427% s/ operativo) |
| P&L sim hoy (2026-07-19) | 🟢 +289.18 $ |
| Operaciones resueltas | 22388 (13548 WIN / 8840 LOSS) — 60.5% |
| Señales abiertas | 136 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 5804 | 60.6% | +0.106 | ➡️ estable | +1954.45$ | 1.06$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3033 | 65.2% | +0.152 | ➡️ estable | +1810.45$ | 1.52$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 2979 | 60.0% | +0.100 | 📈 madura (+0.04) | +1040.75$ | 1.00$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 607 | 68.5% | +0.185 | ➡️ estable | +282.53$ | 1.85$ | ✅ activa |
| UPDOWN_GBM | 1821 | 52.1% | +0.021 | 📈 madura (+0.12) | +132.74$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 169 | 65.7% | +0.155 | 📈 madura (+0.07) | +92.12$ | 1.55$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| FAVORITO_CONFIRMADO | 3784 | 68.4% | +0.184 | ➡️ estable | +43.66$ | 1.84$ | ✅ activa |
| STREAK_FADE_15M | 224 | 59.8% | +0.097 | ➡️ estable | +35.29$ | 0.97$ | ✅ activa |
| LATE_WINDOW_5MIN | 49 | 73.5% | +0.225 | ➡️ estable | +24.54$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 294 | 64.3% | +0.142 | 📉 agota (-0.03) | +15.48$ | 1.42$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 192 | 53.6% | +0.036 | 📉 agota (-0.11) | +14.03$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1631 | 51.3% | +0.013 | ➡️ estable | +13.70$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 61 | 78.7% | +0.278 | ➡️ estable | +10.92$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 147 | 82.3% | +0.319 | ➡️ estable | +9.16$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 328 | 38.7% | -0.112 | ➡️ estable | +6.48$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_5M | 102 | 57.8% | +0.077 | ➡️ estable | +5.47$ | 0.77$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 5 | 60.0% | +0.018 | — | +0.32$ | 0.50$ | ⏳ acumulando |
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
| 2026-07-19T11:15 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 19, 7:00AM-7:15AM ET… | ✅ WIN | +0.12$ |
| 2026-07-19T11:15 | UPDOWN_GBM_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 19, 7:00AM-7:15AM ET… | ✅ WIN | +1.17$ |
| 2026-07-19T11:15 | UPDOWN_GBM#ETH#15min | Ethereum Up or Down - July 19, 7:00AM-7:15AM ET… | ✅ WIN | +1.46$ |
| 2026-07-19T11:15 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 19, 7:00AM-7:15AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-19T11:15 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 19, 7:00AM-7:15AM ET… | ❌ LOSS | -1.16$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-19T11:17 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,564.01 | 0.1min |  |
| ✅ ETH | $1,874.90 | 0.1min |  |
| ✅ SOL | $76.33 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,567.40 | consenso |  |
| ETH | $1,875.13 | consenso |  |
| SOL | $76.28 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*