# Estado del bot — 2026-07-21 17:47 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **23.75 $** |
| P&L real total | 🔴 **-27.47 $** |
| P&L real hoy | -3.28 $ |
| P&L real 7 días | -12.53 $ |
| Fees pagados (real) | 8.90 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3286.82 $ |
| P&L sim compuesto | 🟢 +6231.94 $ (ficción Kelly: +24497% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -183.54 $ |
| Operaciones resueltas | 27232 (16364 WIN / 10868 LOSS) — 60.1% |
| Señales abiertas | 121 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6581 | 59.9% | +0.099 | ➡️ estable | +2108.66$ | 0.99$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3778 | 63.4% | +0.134 | 📉 agota (-0.04) | +2038.77$ | 1.34$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3749 | 58.7% | +0.087 | ➡️ estable | +1207.08$ | 0.87$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1016 | 66.5% | +0.165 | 📉 agota (-0.04) | +453.27$ | 1.65$ | ✅ activa |
| UPDOWN_GBM | 2072 | 52.6% | +0.026 | 📈 madura (+0.11) | +167.38$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 214 | 62.1% | +0.120 | 📉 agota (-0.05) | +101.92$ | 1.20$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4696 | 68.5% | +0.185 | ➡️ estable | +68.04$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| STREAK_FADE_15M | 256 | 58.2% | +0.081 | 📉 agota (-0.08) | +29.43$ | 0.81$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 104 | 79.8% | +0.292 | ➡️ estable | +20.82$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 257 | 49.8% | -0.002 | 📉 agota (-0.13) | +15.77$ | 0.50$ | ⚠️ IC negativo |
| BALLENAS_CONFIRMADAS_15M | 622 | 62.2% | +0.122 | 📉 agota (-0.06) | +11.74$ | 1.22$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 253 | 51.4% | +0.014 | 📉 agota (-0.14) | +11.32$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 228 | 81.6% | +0.313 | ➡️ estable | +10.74$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| LATE_WINDOW_5MIN | 229 | 48.0% | -0.019 | 📉 agota (-0.23) | +0.04$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 8 | 50.0% | +0.000 | — | -0.26$ | 0.50$ | ✅ activa |
| BALLENAS_TARDIAS | 10 | 70.0% | +0.083 | — | -2.01$ | 0.83$ | ✅ activa |
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
| 2026-07-21T17:46 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 1:35PM-1:40PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T17:40 | BALLENAS_TARDIAS#BTC#15min | … | ❌ LOSS | -1.07$ |
| 2026-07-21T17:40 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 21, 1:15PM-1:30PM ET… | ✅ WIN | +0.72$ |
| 2026-07-21T17:40 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 21, 1:15PM-1:30PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-21T17:40 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 21, 1:15PM-1:30PM ET… | ✅ WIN | +2.41$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T17:46 UTC | rechazos 1h: 3 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,460.13 | 0.1min |  |
| ✅ ETH | $1,926.15 | 0.1min |  |
| ✅ SOL | $77.91 | 0.1min |  |
| ✅ XRP | $1.16 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,460.13 | consenso |  |
| ETH | $1,926.15 | consenso |  |
| SOL | $77.89 | consenso |  |
| XRP | $1.16 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:3 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*