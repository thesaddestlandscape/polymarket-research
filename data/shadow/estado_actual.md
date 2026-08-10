# Estado del bot — 2026-08-10 23:01 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **10.30 $** |
| P&L real total | 🔴 **-40.92 $** |
| P&L real hoy | -32.86 $ |
| P&L real 7 días | -11.75 $ |
| Fees pagados (real) | 15.20 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6211.92 $ |
| P&L sim compuesto | 🟢 +15105.06 $ (ficción Kelly: +59375% s/ operativo) |
| P&L sim hoy (2026-08-10) | 🟢 +729.59 $ |
| Operaciones resueltas | 107503 (66061 WIN / 41442 LOSS) — 61.5% |
| Señales abiertas | 665 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11187 | 61.9% | +0.119 | ➡️ estable | +5531.21$ | 1.19$ | ✅ activa |
| GBM_LATE_15M | 13532 | 60.2% | +0.102 | ➡️ estable | +4603.23$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10329 | 59.4% | +0.094 | 📈 madura (+0.05) | +3886.18$ | 0.94$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3587 | 66.0% | +0.160 | ➡️ estable | +1817.65$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 960 | 74.8% | +0.247 | 📈 madura (+0.08) | +883.21$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4058 | 55.9% | +0.059 | 📈 madura (+0.07) | +565.53$ | 0.59$ | ✅ activa |
| WEEKLY_PRICE | 732 | 77.9% | +0.278 | 📈 madura (+0.16) | +326.70$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 445 | 54.6% | +0.046 | 📉 agota (-0.13) | +96.50$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 156 | 76.9% | +0.266 | 📉 agota (-0.05) | +85.26$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 323 | 80.8% | +0.306 | ➡️ estable | +65.82$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1616 | 48.9% | -0.011 | 📈 madura (+0.04) | +35.96$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1630 | 62.8% | +0.128 | ➡️ estable | +19.46$ | 1.28$ | ✅ activa |
| GBM_LATE_60M | 409 | 42.5% | -0.074 | 📈 madura (+0.10) | +17.11$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1725 | 51.4% | +0.014 | ➡️ estable | +15.43$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 790 | 53.2% | +0.032 | ➡️ estable | +12.27$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.52$ | ✅ activa |
| RESOLUTION_SNIPER | 32 | 81.2% | +0.294 | 📉 agota (-0.11) | +6.65$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1893 | 55.2% | +0.051 | 📉 agota (-0.15) | +2.20$ | 0.52$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 166 | 53.0% | +0.030 | ➡️ estable | -0.82$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 144 | 93.8% | +0.432 | 📈 madura (+0.04) | -1.25$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 6 | 16.7% | -0.075 | — | -2.08$ | 0.50$ | ⏳ acumulando |
| LIQUIDACIONES_60M | 147 | 50.3% | +0.003 | 📉 agota (-0.03) | -4.36$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 52 | 21.2% | -0.278 | 📉 agota (-0.11) | -13.27$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 135 | 87.4% | +0.369 | 📈 madura (+0.10) | -16.19$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 86 | 31.4% | -0.182 | ➡️ estable | -17.18$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 656 | 79.4% | +0.293 | 📉 agota (-0.03) | -18.62$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_15M | 140 | 38.6% | -0.113 | ➡️ estable | -20.01$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 354 | 77.4% | +0.272 | 📉 agota (-0.10) | -20.94$ | 2.00$ | ✅ activa |
| STREAK_FADE_5M | 251 | 44.6% | -0.053 | 📉 agota (-0.08) | -26.50$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 132 | 18.2% | -0.313 | 📈 madura (+0.06) | -27.52$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 325 | 43.7% | -0.063 | 📉 agota (-0.10) | -27.91$ | 0.50$ | 🚫 desactivada |
| UPDOWN_OU_5M | 347 | 32.0% | -0.179 | 📉 agota (-0.03) | -61.22$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2963 | 70.0% | +0.199 | ➡️ estable | -188.15$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 3219 | 44.9% | -0.051 | 📈 madura (+0.06) | -634.55$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 29901 | 61.8% | +0.118 | ➡️ estable | -776.75$ | 1.18$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 13768 | 70.0% | +0.200 | ➡️ estable | -1004.89$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-10T22:59 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | … | ✅ WIN | +0.33$ |
| 2026-08-10T22:59 | BALLENAS_TARDIAS#SOL#5min | … | ✅ WIN | +0.57$ |
| 2026-08-10T22:59 | FAVORITO_CONFIRMADO#SOL#5min | … | ✅ WIN | +0.57$ |
| 2026-08-10T22:59 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-10T22:59 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | … | ✅ WIN | +0.29$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-10T22:57 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,947.00 | 0.0min |  |
| ✅ ETH | $1,873.94 | 0.0min |  |
| ✅ SOL | $76.15 | 0.0min |  |
| ✅ XRP | $1.01 | 0.0min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,942.30 | consenso |  |
| ETH | $1,874.03 | consenso |  |
| SOL | $76.16 | consenso |  |
| XRP | $1.01 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*