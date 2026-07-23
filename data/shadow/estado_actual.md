# Estado del bot — 2026-07-23 08:30 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **29.40 $** |
| P&L real total | 🔴 **-21.82 $** |
| P&L real hoy | +0.17 $ |
| P&L real 7 días | -0.74 $ |
| Fees pagados (real) | 9.77 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3625.38 $ |
| P&L sim compuesto | 🟢 +6849.24 $ (ficción Kelly: +26923% s/ operativo) |
| P&L sim hoy (2026-07-23) | 🟢 +137.38 $ |
| Operaciones resueltas | 30556 (18378 WIN / 12178 LOSS) — 60.1% |
| Señales abiertas | 150 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 7078 | 59.6% | +0.096 | 📉 agota (-0.03) | +2219.56$ | 0.97$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4275 | 62.7% | +0.127 | 📉 agota (-0.04) | +2188.03$ | 1.27$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4283 | 58.2% | +0.082 | ➡️ estable | +1301.38$ | 0.82$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1345 | 66.5% | +0.164 | ➡️ estable | +620.67$ | 1.64$ | ✅ activa |
| UPDOWN_GBM | 2312 | 53.1% | +0.031 | 📈 madura (+0.11) | +203.10$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 240 | 60.8% | +0.107 | 📉 agota (-0.07) | +110.47$ | 1.07$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5336 | 68.7% | +0.187 | ➡️ estable | +86.39$ | 1.87$ | ✅ activa |
| WEEKLY_PRICE | 336 | 68.2% | +0.180 | 📈 madura (+0.21) | +67.16$ | 1.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 834 | 62.9% | +0.129 | ➡️ estable | +37.74$ | 1.29$ | ✅ activa |
| STREAK_FADE_15M | 268 | 58.6% | +0.085 | 📉 agota (-0.07) | +34.45$ | 0.85$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 130 | 79.2% | +0.288 | ➡️ estable | +23.71$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 283 | 82.0% | +0.318 | ➡️ estable | +15.52$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1659 | 51.2% | +0.012 | ➡️ estable | +11.80$ | 0.50$ | ✅ activa |
| GBM_LATE_5M | 337 | 48.7% | -0.013 | 📉 agota (-0.18) | +9.92$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 263 | 51.0% | +0.009 | 📉 agota (-0.17) | +9.67$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 336 | 38.7% | -0.112 | ➡️ estable | +4.40$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 23 | 87.0% | +0.340 | — | +1.32$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 13 | 53.8% | +0.022 | — | +0.20$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| LATE_WINDOW_5MIN | 336 | 44.9% | -0.050 | 📉 agota (-0.16) | -4.47$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 319 | 44.2% | -0.058 | 📉 agota (-0.08) | -25.29$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-23T08:26 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 23, 4:15AM-4:20AM ET… | ✅ WIN | +0.63$ |
| 2026-07-23T08:22 | UPDOWN_GBM#DOGE#15min | Dogecoin Up or Down - July 23, 4:00AM-4:15AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-23T08:19 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 23, 4:00AM-4:15AM ET… | ❌ LOSS | -1.89$ |
| 2026-07-23T08:19 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 23, 4:00AM-4:15AM ET… | ✅ WIN | +0.33$ |
| 2026-07-23T08:19 | BALLENAS_CONFIRMADAS_15M#ETH#15min | Ethereum Up or Down - July 23, 4:00AM-4:15AM ET… | ✅ WIN | +0.33$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-23T08:28 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,503.61 | 0.1min |  |
| ✅ ETH | $1,919.62 | 0.1min |  |
| ✅ SOL | $77.33 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,503.61 | consenso |  |
| ETH | $1,919.75 | consenso |  |
| SOL | $77.28 | consenso |  |
| XRP | $1.13 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*