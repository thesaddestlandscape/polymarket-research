# Estado del bot — 2026-07-12 22:12 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **14.13 $** |
| P&L real total | 🔴 **-11.31 $** |
| P&L real hoy | -3.85 $ |
| P&L real 7 días | +6.15 $ |
| Fees pagados (real) | 7.67 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1360.22 $ |
| P&L sim compuesto | 🟢 +2226.04 $ (ficción Kelly: +8750% s/ operativo) |
| P&L sim hoy (2026-07-12) | 🟢 +621.33 $ |
| Operaciones resueltas | 11501 (6607 WIN / 4894 LOSS) — 57.4% |
| Señales abiertas | 147 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3710 | 61.3% | +0.113 | ➡️ estable | +1241.94$ | 1.13$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1058 | 66.5% | +0.165 | ➡️ estable | +619.24$ | 1.65$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1201 | 58.3% | +0.083 | ➡️ estable | +304.63$ | 0.83$ | ✅ activa |
| UPDOWN_GBM | 1345 | 49.6% | -0.004 | 📈 madura (+0.07) | +29.17$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 1057 | 68.9% | +0.188 | 📈 madura (+0.07) | +28.61$ | 1.88$ | ✅ activa |
| STREAK_FADE_15M | 155 | 62.6% | +0.124 | 📈 madura (+0.18) | +25.15$ | 1.24$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 71 | 63.4% | +0.130 | ➡️ estable | +21.20$ | 1.30$ | ✅ activa |
| ORDER_FLOW_5M | 1586 | 51.3% | +0.013 | ➡️ estable | +16.48$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 317 | 38.8% | -0.111 | ➡️ estable | +7.10$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM | 138 | 34.8% | -0.150 | 📉 agota (-0.11) | +0.19$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 171 | 47.4% | -0.026 | ➡️ estable | -6.93$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 204 | 57.4% | +0.073 | 📈 madura (+0.24) | -13.93$ | 0.73$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-12T22:06 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 12, 5:45PM-6:00PM ET… | ✅ WIN | +2.78$ |
| 2026-07-12T22:06 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 12, 5:45PM-6:00PM ET… | ✅ WIN | +1.83$ |
| 2026-07-12T22:06 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 12, 5:45PM-6:00PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-12T22:04 | STREAK_FADE_5M#XRP#5min | XRP Up or Down - July 12, 5:55PM-6:00PM ET… | ✅ WIN | +1.76$ |
| 2026-07-12T22:02 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 12, 5:45PM-6:00PM ET… | ✅ WIN | +0.61$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-12T22:11 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,730.01 | 0.1min |  |
| ✅ ETH | $1,800.38 | 0.1min |  |
| ✅ SOL | $76.76 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,733.90 | consenso |  |
| ETH | $1,800.74 | consenso |  |
| SOL | $76.66 | consenso |  |
| XRP | $1.09 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*