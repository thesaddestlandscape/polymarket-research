# Estado del bot — 2026-07-22 02:05 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **23.79 $** |
| P&L real total | 🔴 **-27.43 $** |
| P&L real hoy | +1.28 $ |
| P&L real 7 días | -8.31 $ |
| Fees pagados (real) | 9.06 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3364.27 $ |
| P&L sim compuesto | 🟢 +6391.88 $ (ficción Kelly: +25125% s/ operativo) |
| P&L sim hoy (2026-07-22) | 🟢 +28.37 $ |
| Operaciones resueltas | 27965 (16806 WIN / 11159 LOSS) — 60.1% |
| Señales abiertas | 139 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6699 | 59.8% | +0.098 | ➡️ estable | +2137.95$ | 0.98$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3893 | 63.2% | +0.132 | 📉 agota (-0.04) | +2067.85$ | 1.32$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3864 | 58.6% | +0.086 | ➡️ estable | +1241.35$ | 0.86$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1086 | 66.4% | +0.164 | ➡️ estable | +485.24$ | 1.64$ | ✅ activa |
| UPDOWN_GBM | 2117 | 52.7% | +0.027 | 📈 madura (+0.11) | +174.71$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 221 | 61.5% | +0.114 | 📉 agota (-0.06) | +106.22$ | 1.14$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4833 | 68.6% | +0.186 | ➡️ estable | +80.41$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| STREAK_FADE_15M | 260 | 58.1% | +0.080 | 📉 agota (-0.08) | +29.21$ | 0.80$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 112 | 80.4% | +0.298 | 📈 madura (+0.03) | +24.03$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 677 | 62.3% | +0.123 | 📉 agota (-0.05) | +21.40$ | 1.23$ | ✅ activa |
| GBM_LATE_5M | 265 | 49.1% | -0.009 | 📉 agota (-0.14) | +15.04$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 240 | 82.1% | +0.318 | ➡️ estable | +13.53$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1647 | 51.1% | +0.011 | ➡️ estable | +11.75$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 256 | 51.2% | +0.012 | 📉 agota (-0.15) | +10.84$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 8 | 50.0% | +0.000 | — | -0.26$ | 0.50$ | ✅ activa |
| BALLENAS_TARDIAS | 13 | 76.9% | +0.152 | — | -1.30$ | 1.52$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| LATE_WINDOW_5MIN | 259 | 45.6% | -0.044 | 📉 agota (-0.25) | -4.02$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-22T02:04 | BALLENAS_TARDIAS#BTC#15min | … | ✅ WIN | +0.16$ |
| 2026-07-22T02:04 | GBM_LATE_5M#BTC#5min | Bitcoin Up or Down - July 21, 9:55PM-10:00PM ET… | ✅ WIN | +0.80$ |
| 2026-07-22T02:04 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 21, 9:55PM-10:00PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-22T02:04 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 21, 9:45PM-10:00PM ET… | ✅ WIN | +1.96$ |
| 2026-07-22T02:04 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 21, 9:45PM-10:00PM ET… | ✅ WIN | +1.96$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-22T02:03 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,331.52 | 0.1min |  |
| ✅ ETH | $1,929.54 | 0.1min |  |
| ✅ SOL | $78.31 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,340.00 | consenso |  |
| ETH | $1,929.82 | consenso |  |
| SOL | $78.19 | consenso |  |
| XRP | $1.14 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*