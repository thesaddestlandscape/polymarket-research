# Estado del bot — 2026-07-21 16:48 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **25.01 $** |
| P&L real total | 🔴 **-26.21 $** |
| P&L real hoy | -2.51 $ |
| P&L real 7 días | -11.76 $ |
| Fees pagados (real) | 8.82 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3286.49 $ |
| P&L sim compuesto | 🟢 +6235.28 $ (ficción Kelly: +24510% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -180.20 $ |
| Operaciones resueltas | 27150 (16319 WIN / 10831 LOSS) — 60.1% |
| Señales abiertas | 126 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6568 | 59.9% | +0.098 | ➡️ estable | +2106.30$ | 0.99$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3764 | 63.4% | +0.134 | 📉 agota (-0.04) | +2034.60$ | 1.34$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3735 | 58.7% | +0.087 | ➡️ estable | +1205.76$ | 0.87$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1008 | 66.6% | +0.165 | 📉 agota (-0.03) | +453.20$ | 1.65$ | ✅ activa |
| UPDOWN_GBM | 2071 | 52.6% | +0.026 | 📈 madura (+0.11) | +168.62$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 214 | 62.1% | +0.120 | 📉 agota (-0.05) | +101.92$ | 1.20$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4681 | 68.6% | +0.185 | ➡️ estable | +75.27$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| STREAK_FADE_15M | 256 | 58.2% | +0.081 | 📉 agota (-0.08) | +29.43$ | 0.81$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 104 | 79.8% | +0.292 | ➡️ estable | +20.82$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 256 | 50.0% | +0.000 | 📉 agota (-0.12) | +16.28$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 253 | 51.4% | +0.014 | 📉 agota (-0.14) | +11.32$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 226 | 81.4% | +0.311 | ➡️ estable | +10.20$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 616 | 62.0% | +0.120 | 📉 agota (-0.06) | +9.89$ | 1.20$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| LATE_WINDOW_5MIN | 223 | 48.9% | -0.011 | 📉 agota (-0.21) | +2.57$ | 0.50$ | ⚠️ IC negativo |
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
| 2026-07-21T16:47 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 12:35PM-12:40PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T16:34 | BALLENAS_CONFIRMADAS_15M#XRP#15min | XRP Up or Down - July 21, 12:15PM-12:30PM ET… | ✅ WIN | +0.69$ |
| 2026-07-21T16:34 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 21, 12:15PM-12:30PM ET… | ✅ WIN | +1.56$ |
| 2026-07-21T16:34 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 21, 12:15PM-12:30PM ET… | ✅ WIN | +1.92$ |
| 2026-07-21T16:34 | UPDOWN_GBM_15M_TARDIO#XRP#15min | XRP Up or Down - July 21, 12:15PM-12:30PM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T16:46 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,475.51 | 0.1min |  |
| ✅ ETH | $1,921.37 | 0.1min |  |
| ✅ SOL | $78.04 | 0.1min |  |
| ✅ XRP | $1.15 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,475.90 | consenso |  |
| ETH | $1,921.64 | consenso |  |
| SOL | $78.00 | consenso |  |
| XRP | $1.15 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*