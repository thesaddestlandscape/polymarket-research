# Estado del bot — 2026-07-21 16:53 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **24.53 $** |
| P&L real total | 🔴 **-26.69 $** |
| P&L real hoy | -1.29 $ |
| P&L real 7 días | -10.54 $ |
| Fees pagados (real) | 8.83 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3287.22 $ |
| P&L sim compuesto | 🟢 +6238.27 $ (ficción Kelly: +24522% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -177.21 $ |
| Operaciones resueltas | 27162 (16327 WIN / 10835 LOSS) — 60.1% |
| Señales abiertas | 124 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6569 | 59.9% | +0.099 | ➡️ estable | +2108.15$ | 0.99$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3766 | 63.4% | +0.134 | 📉 agota (-0.04) | +2034.55$ | 1.34$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3737 | 58.7% | +0.087 | ➡️ estable | +1207.10$ | 0.87$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1010 | 66.5% | +0.165 | 📉 agota (-0.04) | +452.61$ | 1.65$ | ✅ activa |
| UPDOWN_GBM | 2071 | 52.6% | +0.026 | 📈 madura (+0.11) | +168.62$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 214 | 62.1% | +0.120 | 📉 agota (-0.05) | +101.92$ | 1.20$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4682 | 68.6% | +0.186 | ➡️ estable | +75.51$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| STREAK_FADE_15M | 256 | 58.2% | +0.081 | 📉 agota (-0.08) | +29.43$ | 0.81$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 104 | 79.8% | +0.292 | ➡️ estable | +20.82$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 256 | 50.0% | +0.000 | 📉 agota (-0.12) | +16.28$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 253 | 51.4% | +0.014 | 📉 agota (-0.14) | +11.32$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 618 | 62.1% | +0.121 | 📉 agota (-0.06) | +10.83$ | 1.21$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 227 | 81.5% | +0.312 | ➡️ estable | +10.44$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| LATE_WINDOW_5MIN | 224 | 48.7% | -0.013 | 📉 agota (-0.22) | +1.59$ | 0.50$ | ⚠️ IC negativo |
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
| 2026-07-21T16:52 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 12:40PM-12:45PM ET… | ❌ LOSS | -0.98$ |
| 2026-07-21T16:50 | BALLENAS_CONFIRMADAS_15M#XRP#15min | XRP Up or Down - July 21, 12:30PM-12:45PM ET… | ✅ WIN | +0.69$ |
| 2026-07-21T16:50 | UPDOWN_GBM_15M_TARDIO#XRP#15min | XRP Up or Down - July 21, 12:30PM-12:45PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-21T16:50 | FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | Solana Up or Down - July 21, 12:30PM-12:45PM ET… | ✅ WIN | +0.25$ |
| 2026-07-21T16:50 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 21, 12:30PM-12:45PM ET… | ✅ WIN | +0.25$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T16:52 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,475.51 | 0.1min |  |
| ✅ ETH | $1,921.37 | 0.1min |  |
| ✅ SOL | $78.17 | 0.1min |  |
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