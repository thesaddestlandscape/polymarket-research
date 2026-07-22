# Estado del bot — 2026-07-22 01:06 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **23.79 $** |
| P&L real total | 🔴 **-27.43 $** |
| P&L real hoy | +1.28 $ |
| P&L real 7 días | -8.31 $ |
| Fees pagados (real) | 9.06 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3346.32 $ |
| P&L sim compuesto | 🟢 +6375.60 $ (ficción Kelly: +25061% s/ operativo) |
| P&L sim hoy (2026-07-22) | 🟢 +12.10 $ |
| Operaciones resueltas | 27871 (16743 WIN / 11128 LOSS) — 60.1% |
| Señales abiertas | 153 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6683 | 59.8% | +0.098 | ➡️ estable | +2133.69$ | 0.98$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3878 | 63.2% | +0.132 | 📉 agota (-0.04) | +2061.79$ | 1.32$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3848 | 58.6% | +0.086 | ➡️ estable | +1242.61$ | 0.86$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1078 | 66.6% | +0.166 | ➡️ estable | +489.25$ | 1.66$ | ✅ activa |
| UPDOWN_GBM | 2111 | 52.7% | +0.027 | 📈 madura (+0.11) | +176.20$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 221 | 61.5% | +0.114 | 📉 agota (-0.06) | +106.22$ | 1.14$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4818 | 68.5% | +0.185 | ➡️ estable | +71.79$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| STREAK_FADE_15M | 260 | 58.1% | +0.080 | 📉 agota (-0.08) | +29.21$ | 0.80$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 112 | 80.4% | +0.298 | 📈 madura (+0.03) | +24.03$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 668 | 62.1% | +0.121 | 📉 agota (-0.06) | +18.45$ | 1.21$ | ✅ activa |
| GBM_LATE_5M | 264 | 48.9% | -0.011 | 📉 agota (-0.14) | +14.24$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 240 | 82.1% | +0.318 | ➡️ estable | +13.53$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 256 | 51.2% | +0.012 | 📉 agota (-0.15) | +10.84$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 8 | 50.0% | +0.000 | — | -0.26$ | 0.50$ | ✅ activa |
| BALLENAS_TARDIAS | 11 | 72.7% | +0.106 | — | -1.83$ | 1.06$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| LATE_WINDOW_5MIN | 256 | 45.7% | -0.043 | 📉 agota (-0.25) | -3.39$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-22T01:05 | FAVORITO_CONFIRMADO#SOL#60min | Solana Up or Down - July 21, 8PM ET… | ✅ WIN | +1.02$ |
| 2026-07-22T01:05 | FAVORITO_CONFIRMADO#BTC#60min | Bitcoin Up or Down - July 21, 8PM ET… | ✅ WIN | +1.27$ |
| 2026-07-22T01:05 | FAVORITO_CONFIRMADO#ETH#60min | Ethereum Up or Down - July 21, 8PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-22T00:53 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 21, 8:30PM-8:45PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-22T00:53 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 21, 8:30PM-8:45PM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-22T01:04 UTC | rechazos 1h: 5 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,543.40 | 0.1min |  |
| ✅ ETH | $1,937.10 | 0.1min |  |
| ✅ SOL | $78.45 | 0.1min |  |
| ✅ XRP | $1.15 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,556.20 | consenso |  |
| ETH | $1,937.10 | consenso |  |
| SOL | $78.40 | consenso |  |
| XRP | $1.14 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:5 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*