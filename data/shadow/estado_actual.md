# Estado del bot — 2026-08-11 15:22 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **10.07 $** |
| P&L real total | 🔴 **-41.15 $** |
| P&L real hoy | -0.23 $ |
| P&L real 7 días | -11.98 $ |
| Fees pagados (real) | 15.23 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6157.89 $ |
| P&L sim compuesto | 🟢 +15274.85 $ (ficción Kelly: +60043% s/ operativo) |
| P&L sim hoy (2026-08-11) | 🟢 +106.73 $ |
| Operaciones resueltas | 111920 (68757 WIN / 43163 LOSS) — 61.4% |
| Señales abiertas | 591 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11422 | 61.8% | +0.118 | ➡️ estable | +5605.48$ | 0.60$ | ✅ activa |
| GBM_LATE_15M | 13715 | 60.3% | +0.103 | ➡️ estable | +4695.94$ | 1.12$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10466 | 59.5% | +0.095 | 📈 madura (+0.05) | +3989.88$ | 1.90$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3610 | 65.8% | +0.158 | ➡️ estable | +1814.20$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1085 | 74.4% | +0.243 | 📈 madura (+0.05) | +987.66$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4111 | 55.9% | +0.059 | 📈 madura (+0.06) | +562.77$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 732 | 77.9% | +0.278 | 📈 madura (+0.16) | +326.70$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 461 | 54.9% | +0.049 | 📉 agota (-0.14) | +100.59$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 162 | 76.5% | +0.262 | 📉 agota (-0.05) | +82.81$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 329 | 80.5% | +0.304 | ➡️ estable | +63.37$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1688 | 49.8% | -0.002 | 📈 madura (+0.07) | +60.46$ | 0.92$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1946 | 63.6% | +0.136 | ➡️ estable | +52.55$ | 1.36$ | ✅ activa |
| GBM_LATE_60M | 422 | 42.7% | -0.073 | 📈 madura (+0.10) | +31.37$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1731 | 51.4% | +0.014 | ➡️ estable | +15.29$ | 0.53$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 893 | 52.5% | +0.025 | ➡️ estable | +8.03$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 32 | 81.2% | +0.294 | 📉 agota (-0.11) | +6.65$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1920 | 55.2% | +0.052 | 📉 agota (-0.15) | +3.98$ | 0.76$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 197 | 53.3% | +0.033 | ➡️ estable | +1.64$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 149 | 94.0% | +0.434 | 📈 madura (+0.04) | -0.58$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_60M | 162 | 51.9% | +0.018 | ➡️ estable | -1.51$ | 0.50$ | ✅ activa |
| STREAK_FADE_60M | 8 | 25.0% | -0.080 | — | -2.11$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 52 | 21.2% | -0.278 | 📉 agota (-0.11) | -13.27$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 142 | 88.0% | +0.375 | 📈 madura (+0.12) | -15.21$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 369 | 78.0% | +0.279 | 📉 agota (-0.07) | -16.21$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 667 | 79.5% | +0.294 | ➡️ estable | -16.51$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 109 | 34.9% | -0.149 | 📈 madura (+0.06) | -18.06$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 161 | 39.1% | -0.107 | ➡️ estable | -22.69$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 280 | 46.4% | -0.035 | 📈 madura (+0.06) | -23.43$ | 0.71$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 140 | 18.6% | -0.310 | 📈 madura (+0.08) | -28.09$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 354 | 43.2% | -0.067 | 📉 agota (-0.12) | -31.62$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 353 | 31.7% | -0.182 | 📉 agota (-0.04) | -62.59$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3162 | 70.1% | +0.201 | ➡️ estable | -192.42$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 3675 | 45.4% | -0.046 | 📈 madura (+0.08) | -714.23$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 31325 | 61.7% | +0.117 | ➡️ estable | -863.09$ | 1.15$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 14583 | 69.8% | +0.198 | ➡️ estable | -1109.82$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-11T15:20 | BALLENAS_TARDIAS#ETH#5min | … | ✅ WIN | +0.80$ |
| 2026-08-11T15:20 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ✅ WIN | +0.43$ |
| 2026-08-11T15:20 | FAVORITO_CONFIRMADO#ETH#5min | … | ✅ WIN | +0.62$ |
| 2026-08-11T15:20 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ✅ WIN | +0.35$ |
| 2026-08-11T15:20 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | … | ❌ LOSS | -1.07$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-11T15:16 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,749.00 | 0.2min |  |
| ✅ ETH | $1,872.60 | 0.2min |  |
| ✅ SOL | $75.10 | 0.2min |  |
| ✅ XRP | $1.00 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,714.80 | consenso |  |
| ETH | $1,870.99 | consenso |  |
| SOL | $75.08 | consenso |  |
| XRP | $1.00 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*