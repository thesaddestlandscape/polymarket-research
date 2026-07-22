# Estado del bot — 2026-07-22 20:24 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **28.33 $** |
| P&L real total | 🔴 **-22.89 $** |
| P&L real hoy | +4.60 $ |
| P&L real 7 días | -4.99 $ |
| Fees pagados (real) | 9.59 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3551.52 $ |
| P&L sim compuesto | 🟢 +6710.04 $ (ficción Kelly: +26376% s/ operativo) |
| P&L sim hoy (2026-07-22) | 🟢 +346.53 $ |
| Operaciones resueltas | 29520 (17766 WIN / 11754 LOSS) — 60.2% |
| Señales abiertas | 150 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6926 | 59.7% | +0.097 | ➡️ estable | +2192.84$ | 0.97$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4126 | 63.0% | +0.130 | 📉 agota (-0.04) | +2168.32$ | 1.30$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4117 | 58.3% | +0.083 | ➡️ estable | +1278.26$ | 0.83$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1236 | 66.5% | +0.165 | 📉 agota (-0.04) | +567.34$ | 1.65$ | ✅ activa |
| UPDOWN_GBM | 2223 | 53.1% | +0.031 | 📈 madura (+0.11) | +190.20$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 232 | 61.6% | +0.115 | 📉 agota (-0.06) | +110.74$ | 1.15$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5138 | 68.8% | +0.188 | ➡️ estable | +91.40$ | 1.88$ | ✅ activa |
| WEEKLY_PRICE | 336 | 68.2% | +0.180 | 📈 madura (+0.21) | +67.16$ | 1.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 777 | 63.1% | +0.130 | ➡️ estable | +39.06$ | 1.30$ | ✅ activa |
| STREAK_FADE_15M | 264 | 58.3% | +0.083 | 📉 agota (-0.07) | +31.16$ | 0.83$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 121 | 78.5% | +0.280 | ➡️ estable | +18.36$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 268 | 82.5% | +0.322 | ➡️ estable | +18.12$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1653 | 51.1% | +0.011 | ➡️ estable | +11.85$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 262 | 50.8% | +0.008 | 📉 agota (-0.17) | +9.12$ | 0.50$ | ✅ activa |
| GBM_LATE_5M | 288 | 48.3% | -0.017 | 📉 agota (-0.13) | +6.52$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 336 | 38.7% | -0.112 | ➡️ estable | +4.40$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| BALLENAS_TARDIAS | 16 | 81.2% | +0.222 | — | -0.59$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 11 | 45.5% | -0.021 | — | -0.76$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 323 | 45.5% | -0.045 | 📉 agota (-0.17) | -1.65$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 317 | 44.2% | -0.058 | 📉 agota (-0.09) | -25.33$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-22T20:23 | UPDOWN_GBM#BNB#15min | BNB Up or Down - July 22, 4:00PM-4:15PM ET… | ❌ LOSS | -0.83$ |
| 2026-07-22T20:19 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 22, 4:00PM-4:15PM ET… | ❌ LOSS | -1.90$ |
| 2026-07-22T20:19 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 22, 4:00PM-4:15PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-22T20:19 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 22, 4:00PM-4:15PM ET… | ❌ LOSS | -1.59$ |
| 2026-07-22T20:19 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 22, 4:00PM-4:15PM ET… | ✅ WIN | +1.21$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-22T20:22 UTC | rechazos 1h: 5 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,878.15 | 0.1min |  |
| ✅ ETH | $1,927.22 | 0.1min |  |
| ✅ SOL | $77.85 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,878.15 | consenso |  |
| ETH | $1,927.22 | consenso |  |
| SOL | $77.81 | consenso |  |
| XRP | $1.14 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:5 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*