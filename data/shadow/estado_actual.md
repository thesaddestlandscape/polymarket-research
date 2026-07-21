# Estado del bot — 2026-07-21 16:03 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **25.41 $** |
| P&L real total | 🔴 **-25.81 $** |
| P&L real hoy | -0.37 $ |
| P&L real 7 días | -9.62 $ |
| Fees pagados (real) | 8.82 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3285.15 $ |
| P&L sim compuesto | 🟢 +6228.35 $ (ficción Kelly: +24483% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -187.13 $ |
| Operaciones resueltas | 27057 (16265 WIN / 10792 LOSS) — 60.1% |
| Señales abiertas | 131 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6556 | 59.9% | +0.099 | ➡️ estable | +2107.29$ | 0.99$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3752 | 63.5% | +0.135 | 📉 agota (-0.04) | +2033.65$ | 1.35$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3723 | 58.7% | +0.087 | ➡️ estable | +1207.07$ | 0.87$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1000 | 66.7% | +0.167 | ➡️ estable | +451.73$ | 1.67$ | ✅ activa |
| UPDOWN_GBM | 2069 | 52.7% | +0.027 | 📈 madura (+0.11) | +170.34$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 213 | 62.0% | +0.119 | 📉 agota (-0.04) | +100.10$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4665 | 68.6% | +0.186 | ➡️ estable | +73.04$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 256 | 58.2% | +0.081 | 📉 agota (-0.08) | +29.43$ | 0.81$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 104 | 79.8% | +0.292 | ➡️ estable | +20.82$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 254 | 50.4% | +0.004 | 📉 agota (-0.12) | +17.30$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 611 | 62.2% | +0.122 | 📉 agota (-0.05) | +13.38$ | 1.21$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 224 | 81.7% | +0.314 | ➡️ estable | +12.12$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 253 | 51.4% | +0.014 | 📉 agota (-0.14) | +11.32$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 218 | 49.5% | -0.005 | 📉 agota (-0.22) | +4.48$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 8 | 87.5% | +0.120 | — | +0.13$ | 1.20$ | ✅ activa |
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
| 2026-07-21T15:56 | BALLENAS_CONFIRMADAS_15M#SOL#15min | Solana Up or Down - July 21, 11:30AM-11:45AM ET… | ❌ LOSS | -0.78$ |
| 2026-07-21T15:56 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 21, 11:30AM-11:45AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T15:56 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 21, 11:30AM-11:45AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-21T15:56 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 21, 11:30AM-11:45AM ET… | ❌ LOSS | -1.83$ |
| 2026-07-21T15:56 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 21, 11:30AM-11:45AM ET… | ❌ LOSS | -0.95$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T16:02 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,624.07 | 0.1min |  |
| ✅ ETH | $1,930.20 | 0.1min |  |
| ✅ SOL | $78.17 | 0.1min |  |
| ✅ XRP | $1.16 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,624.07 | consenso |  |
| ETH | $1,930.53 | consenso |  |
| SOL | $78.06 | consenso |  |
| XRP | $1.15 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*