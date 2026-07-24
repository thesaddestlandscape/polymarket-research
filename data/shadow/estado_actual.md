# Estado del bot — 2026-07-24 08:32 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **27.92 $** |
| P&L real total | 🔴 **-23.30 $** |
| P&L real hoy | +1.01 $ |
| P&L real 7 días | -0.02 $ |
| Fees pagados (real) | 9.94 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3770.58 $ |
| P&L sim compuesto | 🟢 +7137.31 $ (ficción Kelly: +28055% s/ operativo) |
| P&L sim hoy (2026-07-24) | 🟢 +162.94 $ |
| Operaciones resueltas | 32566 (19569 WIN / 12997 LOSS) — 60.1% |
| Señales abiertas | 119 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 7362 | 59.6% | +0.096 | 📉 agota (-0.04) | +2284.83$ | 0.96$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4559 | 62.4% | +0.124 | 📉 agota (-0.05) | +2262.70$ | 1.24$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4595 | 57.5% | +0.075 | 📉 agota (-0.04) | +1305.51$ | 0.75$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1514 | 66.4% | +0.164 | ➡️ estable | +705.58$ | 1.64$ | ✅ activa |
| UPDOWN_GBM | 2431 | 53.4% | +0.034 | 📈 madura (+0.09) | +226.88$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5736 | 68.8% | +0.188 | ➡️ estable | +116.85$ | 1.88$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 249 | 60.6% | +0.106 | 📉 agota (-0.08) | +111.96$ | 1.06$ | ✅ activa |
| WEEKLY_PRICE | 352 | 69.0% | +0.189 | 📈 madura (+0.23) | +69.51$ | 1.89$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 955 | 62.6% | +0.126 | ➡️ estable | +43.11$ | 1.26$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 142 | 81.0% | +0.306 | 📈 madura (+0.04) | +30.61$ | 2.00$ | ✅ activa |
| STREAK_FADE_15M | 280 | 57.9% | +0.078 | 📉 agota (-0.06) | +29.14$ | 0.78$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 317 | 81.7% | +0.315 | ➡️ estable | +15.34$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1661 | 51.2% | +0.012 | ➡️ estable | +12.78$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 270 | 51.1% | +0.011 | 📉 agota (-0.16) | +10.17$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 337 | 38.9% | -0.111 | ➡️ estable | +4.86$ | 0.50$ | ⚠️ IC negativo |
| BALLENAS_TARDIAS | 29 | 89.7% | +0.371 | — | +3.37$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 13 | 84.6% | +0.195 | — | +3.10$ | 1.95$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 14 | 57.1% | +0.044 | — | +0.65$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_5M | 541 | 47.7% | -0.023 | 📉 agota (-0.04) | -1.17$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 350 | 45.1% | -0.048 | 📉 agota (-0.12) | -2.09$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 320 | 44.1% | -0.059 | 📉 agota (-0.08) | -26.41$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-24T08:24 | UPDOWN_GBM_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 24, 4:00AM-4:15AM ET… | ❌ LOSS | -0.98$ |
| 2026-07-24T08:24 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 24, 4:00AM-4:15AM ET… | ✅ WIN | +0.78$ |
| 2026-07-24T08:24 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 24, 4:00AM-4:15AM ET… | ❌ LOSS | -1.13$ |
| 2026-07-24T08:24 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 24, 4:00AM-4:15AM ET… | ✅ WIN | +0.42$ |
| 2026-07-24T08:24 | BALLENAS_CONFIRMADAS_15M#SOL#15min | Solana Up or Down - July 24, 4:00AM-4:15AM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-24T08:30 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,263.76 | 0.1min |  |
| ✅ ETH | $1,886.17 | 0.1min |  |
| ✅ SOL | $75.84 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,283.10 | consenso |  |
| ETH | $1,887.15 | consenso |  |
| SOL | $75.72 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*