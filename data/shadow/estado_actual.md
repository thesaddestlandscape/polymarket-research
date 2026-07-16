# Estado del bot — 2026-07-16 06:25 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **4.03 $** |
| P&L real total | 🔴 **-21.41 $** |
| P&L real hoy | -1.11 $ |
| P&L real 7 días | -28.65 $ |
| Fees pagados (real) | 8.57 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1929.73 $ |
| P&L sim compuesto | 🟢 +3375.80 $ (ficción Kelly: +13270% s/ operativo) |
| P&L sim hoy (2026-07-16) | 🟢 +107.36 $ |
| Operaciones resueltas | 16563 (9713 WIN / 6850 LOSS) — 58.6% |
| Señales abiertas | 65 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4803 | 60.3% | +0.103 | ➡️ estable | +1501.41$ | 1.03$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 2039 | 65.0% | +0.150 | 📉 agota (-0.03) | +1188.28$ | 1.50$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 2006 | 59.1% | +0.091 | ➡️ estable | +609.22$ | 0.91$ | ✅ activa |
| UPDOWN_GBM | 1590 | 50.9% | +0.009 | 📈 madura (+0.09) | +75.20$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 113 | 69.9% | +0.196 | 📉 agota (-0.06) | +34.54$ | 1.96$ | ✅ activa |
| STREAK_FADE_15M | 202 | 59.9% | +0.098 | 📈 madura (+0.05) | +28.64$ | 0.98$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 135 | 59.3% | +0.091 | 📉 agota (-0.07) | +28.09$ | 0.91$ | ✅ activa |
| LATE_WINDOW_5MIN | 44 | 72.7% | +0.217 | ➡️ estable | +18.78$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 64 | 57.8% | +0.076 | 📈 madura (+0.26) | +17.69$ | 0.76$ | ✅ activa |
| WEEKLY_PRICE | 256 | 62.1% | +0.120 | 📈 madura (+0.28) | +13.84$ | 1.20$ | ✅ activa |
| ORDER_FLOW_5M | 1617 | 51.2% | +0.012 | ➡️ estable | +13.02$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 326 | 38.3% | -0.116 | ➡️ estable | +3.81$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 31 | 80.6% | +0.288 | 📉 agota (-0.10) | +0.59$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 16 | 75.0% | +0.178 | — | -0.19$ | 1.78$ | ✅ activa |
| GBM_LATE_5M | 11 | 45.5% | -0.021 | — | -0.62$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 147 | 33.3% | -0.164 | 📉 agota (-0.12) | -3.25$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 310 | 44.5% | -0.054 | 📉 agota (-0.06) | -22.30$ | 0.50$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 2454 | 67.2% | +0.172 | ➡️ estable | -69.75$ | 1.72$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-16T06:20 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 16, 2:00AM-2:15AM ET… | ✅ WIN | +0.33$ |
| 2026-07-16T06:20 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 16, 2:00AM-2:15AM ET… | ✅ WIN | +0.43$ |
| 2026-07-16T06:20 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 16, 2:00AM-2:15AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-16T06:20 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 16, 2:00AM-2:15AM ET… | ❌ LOSS | -1.68$ |
| 2026-07-16T06:20 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 16, 2:00AM-2:15AM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-16T06:24 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,812.07 | 0.1min |  |
| ✅ ETH | $1,923.23 | 0.1min |  |
| ✅ SOL | $77.36 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,812.07 | consenso |  |
| ETH | $1,923.26 | consenso |  |
| SOL | $77.36 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*