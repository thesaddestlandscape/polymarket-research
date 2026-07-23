# Estado del bot — 2026-07-23 09:15 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **29.73 $** |
| P&L real total | 🔴 **-21.49 $** |
| P&L real hoy | -1.35 $ |
| P&L real 7 días | -2.26 $ |
| Fees pagados (real) | 9.77 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3646.10 $ |
| P&L sim compuesto | 🟢 +6896.11 $ (ficción Kelly: +27107% s/ operativo) |
| P&L sim hoy (2026-07-23) | 🟢 +184.25 $ |
| Operaciones resueltas | 30623 (18429 WIN / 12194 LOSS) — 60.2% |
| Señales abiertas | 142 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 7088 | 59.7% | +0.097 | 📉 agota (-0.03) | +2229.95$ | 0.97$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4285 | 62.8% | +0.127 | 📉 agota (-0.04) | +2196.59$ | 1.27$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4295 | 58.2% | +0.082 | ➡️ estable | +1308.10$ | 0.82$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1350 | 66.6% | +0.166 | ➡️ estable | +628.40$ | 1.66$ | ✅ activa |
| UPDOWN_GBM | 2316 | 53.2% | +0.031 | 📈 madura (+0.11) | +205.83$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 241 | 61.0% | +0.109 | 📉 agota (-0.06) | +110.91$ | 1.09$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5348 | 68.8% | +0.187 | ➡️ estable | +94.26$ | 1.87$ | ✅ activa |
| WEEKLY_PRICE | 336 | 68.2% | +0.180 | 📈 madura (+0.21) | +67.16$ | 1.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 839 | 62.9% | +0.129 | ➡️ estable | +38.19$ | 1.29$ | ✅ activa |
| STREAK_FADE_15M | 270 | 58.5% | +0.085 | 📉 agota (-0.06) | +34.12$ | 0.85$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 131 | 79.4% | +0.289 | ➡️ estable | +24.29$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 284 | 82.0% | +0.318 | ➡️ estable | +16.24$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1659 | 51.2% | +0.012 | ➡️ estable | +11.80$ | 0.50$ | ✅ activa |
| GBM_LATE_5M | 340 | 48.8% | -0.012 | 📉 agota (-0.19) | +10.60$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 263 | 51.0% | +0.009 | 📉 agota (-0.17) | +9.67$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 336 | 38.7% | -0.112 | ➡️ estable | +4.40$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 24 | 87.5% | +0.346 | — | +1.67$ | 2.00$ | ✅ activa |
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
| 2026-07-23T09:10 | BALLENAS_TARDIAS#BTC#15min | … | ✅ WIN | +0.35$ |
| 2026-07-23T09:10 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 23, 4:45AM-5:00AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-23T09:10 | STREAK_FADE_15M#SOL#15min | Solana Up or Down - July 23, 4:45AM-5:00AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-23T09:10 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 23, 4:45AM-5:00AM ET… | ❌ LOSS | -1.48$ |
| 2026-07-23T09:10 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 23, 4:45AM-5:00AM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-23T09:14 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,674.90 | 0.1min |  |
| ✅ ETH | $1,928.98 | 0.1min |  |
| ✅ SOL | $77.53 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,674.90 | consenso |  |
| ETH | $1,928.98 | consenso |  |
| SOL | $77.49 | consenso |  |
| XRP | $1.14 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*