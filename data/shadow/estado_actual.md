# Estado del bot — 2026-07-20 21:35 UTC

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
| P&L fiel (stake fijo 1$) | +3426.60 $ |
| P&L sim compuesto | 🟢 +6354.17 $ (ficción Kelly: +24977% s/ operativo) |
| P&L sim hoy (2026-07-20) | 🟢 +355.84 $ |
| Operaciones resueltas | 25274 (15357 WIN / 9917 LOSS) — 60.8% |
| Señales abiertas | 140 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6269 | 60.6% | +0.106 | ➡️ estable | +2165.13$ | 1.06$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3475 | 65.1% | +0.151 | ➡️ estable | +2122.84$ | 1.51$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3456 | 59.9% | +0.099 | 📈 madura (+0.03) | +1248.88$ | 0.99$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 850 | 66.6% | +0.165 | 📉 agota (-0.03) | +372.65$ | 1.66$ | ✅ activa |
| UPDOWN_GBM | 1981 | 52.2% | +0.022 | 📈 madura (+0.11) | +139.58$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 191 | 66.0% | +0.158 | 📈 madura (+0.10) | +107.65$ | 1.58$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4378 | 68.6% | +0.186 | ➡️ estable | +68.68$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 238 | 60.1% | +0.100 | ➡️ estable | +40.35$ | 1.00$ | ✅ activa |
| LATE_WINDOW_5MIN | 72 | 68.1% | +0.176 | 📉 agota (-0.08) | +27.43$ | 1.76$ | ✅ activa |
| GBM_LATE_5M | 215 | 56.3% | +0.062 | ➡️ estable | +20.66$ | 0.62$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 490 | 63.5% | +0.134 | ➡️ estable | +17.63$ | 1.34$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 89 | 79.8% | +0.291 | 📉 agota (-0.04) | +16.47$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 232 | 52.2% | +0.021 | 📉 agota (-0.14) | +13.49$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1638 | 51.2% | +0.012 | ➡️ estable | +13.23$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 193 | 82.9% | +0.326 | ➡️ estable | +13.12$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 6 | 66.7% | +0.037 | — | +0.87$ | 0.50$ | ⏳ acumulando |
| BALLENAS_TARDIAS | 2 | 100.0% | +0.025 | — | +0.38$ | 0.50$ | ⏳ acumulando |
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
| 2026-07-20T21:34 | UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | Ethereum Up or Down - July 20, 5:15PM-5:30PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-20T21:34 | UPDOWN_GBM_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 20, 5:15PM-5:30PM ET… | ❌ LOSS | -1.23$ |
| 2026-07-20T21:34 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 20, 5:15PM-5:30PM ET… | ✅ WIN | +2.04$ |
| 2026-07-20T21:34 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 20, 5:15PM-5:30PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-20T21:34 | GBM_LATE_15M_PYCONFIRMADO#XRP#15min | XRP Up or Down - July 20, 5:15PM-5:30PM ET… | ✅ WIN | +2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-20T21:33 UTC | rechazos 1h: 3 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,288.58 | 0.1min |  |
| ✅ ETH | $1,903.68 | 0.1min |  |
| ✅ SOL | $77.96 | 0.1min |  |
| ✅ XRP | $1.12 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,299.40 | consenso |  |
| ETH | $1,903.90 | consenso |  |
| SOL | $77.89 | consenso |  |
| XRP | $1.12 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:3 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*