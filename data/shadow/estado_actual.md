# Estado del bot — 2026-07-16 06:31 UTC

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
| P&L fiel (stake fijo 1$) | +1924.47 $ |
| P&L sim compuesto | 🟢 +3366.08 $ (ficción Kelly: +13231% s/ operativo) |
| P&L sim hoy (2026-07-16) | 🟢 +97.65 $ |
| Operaciones resueltas | 16570 (9714 WIN / 6856 LOSS) — 58.6% |
| Señales abiertas | 61 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4805 | 60.2% | +0.102 | ➡️ estable | +1497.39$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 2040 | 65.0% | +0.149 | 📉 agota (-0.03) | +1186.24$ | 1.49$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 2007 | 59.1% | +0.091 | ➡️ estable | +607.18$ | 0.91$ | ✅ activa |
| UPDOWN_GBM | 1590 | 50.9% | +0.009 | 📈 madura (+0.09) | +75.20$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 114 | 69.3% | +0.190 | 📉 agota (-0.08) | +33.40$ | 1.90$ | ✅ activa |
| STREAK_FADE_15M | 202 | 59.9% | +0.098 | 📈 madura (+0.05) | +28.64$ | 0.98$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 135 | 59.3% | +0.091 | 📉 agota (-0.07) | +28.09$ | 0.91$ | ✅ activa |
| LATE_WINDOW_5MIN | 44 | 72.7% | +0.217 | ➡️ estable | +18.78$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 65 | 56.9% | +0.067 | 📈 madura (+0.24) | +15.65$ | 0.67$ | ✅ activa |
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
| FAVORITO_CONFIRMADO | 2455 | 67.2% | +0.172 | ➡️ estable | -68.19$ | 1.72$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-16T06:30 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 16, 2:15AM-2:30AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-16T06:30 | GBM_LATE_15M_PYCONFIRMADO#XRP#15min | XRP Up or Down - July 16, 2:15AM-2:30AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-16T06:30 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 16, 2:15AM-2:30AM ET… | ✅ WIN | +1.56$ |
| 2026-07-16T06:30 | UPDOWN_GBM_15M_TARDIO#XRP#15min | XRP Up or Down - July 16, 2:15AM-2:30AM ET… | ❌ LOSS | -1.14$ |
| 2026-07-16T06:30 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 16, 2:15AM-2:30AM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-16T06:30 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,767.04 | 0.1min |  |
| ✅ ETH | $1,921.04 | 0.1min |  |
| ✅ SOL | $77.32 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,780.70 | consenso |  |
| ETH | $1,921.04 | consenso |  |
| SOL | $77.32 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*