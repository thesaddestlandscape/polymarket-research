# Estado del bot — 2026-07-21 14:52 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **26.07 $** |
| P&L real total | 🔴 **-25.14 $** |
| P&L real hoy | -4.30 $ |
| P&L real 7 días | -13.55 $ |
| Fees pagados (real) | 8.68 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3295.49 $ |
| P&L sim compuesto | 🟢 +6241.97 $ (ficción Kelly: +24536% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -173.51 $ |
| Operaciones resueltas | 26954 (16212 WIN / 10742 LOSS) — 60.1% |
| Señales abiertas | 138 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6540 | 59.9% | +0.099 | ➡️ estable | +2108.55$ | 0.99$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3736 | 63.5% | +0.135 | 📉 agota (-0.04) | +2034.79$ | 1.35$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3707 | 58.7% | +0.087 | ➡️ estable | +1207.70$ | 0.87$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 993 | 67.1% | +0.170 | 📉 agota (-0.03) | +459.55$ | 1.70$ | ✅ activa |
| UPDOWN_GBM | 2062 | 52.7% | +0.027 | 📈 madura (+0.11) | +172.00$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 212 | 62.3% | +0.121 | 📉 agota (-0.04) | +100.61$ | 1.21$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4648 | 68.6% | +0.186 | ➡️ estable | +73.45$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 256 | 58.2% | +0.081 | 📉 agota (-0.08) | +29.43$ | 0.81$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 104 | 79.8% | +0.292 | ➡️ estable | +20.82$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 254 | 50.4% | +0.004 | 📉 agota (-0.12) | +17.30$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 599 | 62.3% | +0.122 | 📉 agota (-0.05) | +14.16$ | 1.22$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 250 | 51.6% | +0.016 | 📉 agota (-0.15) | +11.79$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 222 | 81.5% | +0.312 | ➡️ estable | +10.71$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 213 | 49.3% | -0.007 | 📉 agota (-0.22) | +3.73$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 7 | 100.0% | +0.136 | — | +1.20$ | 1.36$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 8 | 50.0% | +0.000 | — | -0.26$ | 0.50$ | ✅ activa |
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
| 2026-07-21T14:50 | UPDOWN_GBM_15M_TARDIO#DOGE#15min | Dogecoin Up or Down - July 21, 10:30AM-10:45AM ET… | ✅ WIN | +1.77$ |
| 2026-07-21T14:50 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 21, 10:30AM-10:45AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-21T14:50 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 21, 10:30AM-10:45AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-21T14:50 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 21, 10:30AM-10:45AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-21T14:50 | UPDOWN_GBM#DOGE#15min | Dogecoin Up or Down - July 21, 10:30AM-10:45AM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

⚠️ **DEGRADED** — última verificación 2026-07-21T14:50 UTC | rechazos 1h: 6 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,870.85 | 0.1min |  |
| ✅ ETH | $1,936.81 | 0.1min |  |
| ✅ SOL | $78.11 | 0.1min |  |
| ✅ XRP | $1.15 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,875.50 | consenso |  |
| ETH | $1,936.91 | consenso |  |
| SOL | $78.17 | consenso |  |
| XRP | $1.15 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:6 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*