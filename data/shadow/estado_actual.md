# Estado del bot — 2026-07-19 10:34 UTC

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
| P&L fiel (stake fijo 1$) | +3000.20 $ |
| P&L sim compuesto | 🟢 +5434.93 $ (ficción Kelly: +21364% s/ operativo) |
| P&L sim hoy (2026-07-19) | 🟢 +273.16 $ |
| Operaciones resueltas | 22337 (13512 WIN / 8825 LOSS) — 60.5% |
| Señales abiertas | 131 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 5794 | 60.6% | +0.106 | ➡️ estable | +1954.73$ | 1.06$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3023 | 65.2% | +0.152 | ➡️ estable | +1802.24$ | 1.52$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 2969 | 60.0% | +0.100 | 📈 madura (+0.04) | +1039.99$ | 1.00$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 606 | 68.5% | +0.184 | ➡️ estable | +281.36$ | 1.84$ | ✅ activa |
| UPDOWN_GBM | 1820 | 52.0% | +0.020 | 📈 madura (+0.12) | +131.28$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 169 | 65.7% | +0.155 | 📈 madura (+0.07) | +92.12$ | 1.55$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| FAVORITO_CONFIRMADO | 3772 | 68.4% | +0.184 | ➡️ estable | +38.00$ | 1.84$ | ✅ activa |
| STREAK_FADE_15M | 224 | 59.8% | +0.097 | ➡️ estable | +35.29$ | 0.97$ | ✅ activa |
| LATE_WINDOW_5MIN | 49 | 73.5% | +0.225 | ➡️ estable | +24.54$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 291 | 64.6% | +0.145 | 📉 agota (-0.05) | +16.96$ | 1.45$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 192 | 53.6% | +0.036 | 📉 agota (-0.11) | +14.03$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1631 | 51.3% | +0.013 | ➡️ estable | +13.70$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 61 | 78.7% | +0.278 | ➡️ estable | +10.92$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 145 | 82.1% | +0.316 | ➡️ estable | +8.27$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 328 | 38.7% | -0.112 | ➡️ estable | +6.48$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_5M | 100 | 58.0% | +0.078 | 📈 madura (+0.04) | +5.84$ | 0.78$ | ✅ activa |
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
| 2026-07-19T10:31 | BALLENAS_CONFIRMADAS_15M#ETH#15min | Ethereum Up or Down - July 19, 6:15AM-6:30AM ET… | ✅ WIN | +0.57$ |
| 2026-07-19T10:31 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 19, 6:15AM-6:30AM ET… | ✅ WIN | +0.57$ |
| 2026-07-19T10:21 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 19, 6:00AM-6:15AM ET… | ❌ LOSS | -1.35$ |
| 2026-07-19T10:21 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 19, 6:00AM-6:15AM ET… | ✅ WIN | +2.13$ |
| 2026-07-19T10:21 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 19, 6:00AM-6:15AM ET… | ✅ WIN | +3.92$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-19T10:33 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,580.19 | 0.1min |  |
| ✅ ETH | $1,867.11 | 0.1min |  |
| ✅ SOL | $76.05 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,580.19 | consenso |  |
| ETH | $1,867.11 | consenso |  |
| SOL | $76.02 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*