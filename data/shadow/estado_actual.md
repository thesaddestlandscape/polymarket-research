# Estado del bot — 2026-07-23 16:03 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **26.91 $** |
| P&L real total | 🔴 **-24.31 $** |
| P&L real hoy | -2.32 $ |
| P&L real 7 días | -3.23 $ |
| Fees pagados (real) | 9.91 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3587.39 $ |
| P&L sim compuesto | 🟢 +6834.50 $ (ficción Kelly: +26865% s/ operativo) |
| P&L sim hoy (2026-07-23) | 🟢 +122.64 $ |
| Operaciones resueltas | 31208 (18722 WIN / 12486 LOSS) — 60.0% |
| Señales abiertas | 153 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 7168 | 59.5% | +0.095 | 📉 agota (-0.04) | +2208.15$ | 0.95$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4362 | 62.4% | +0.124 | 📉 agota (-0.04) | +2167.43$ | 1.24$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4379 | 57.7% | +0.077 | ➡️ estable | +1268.70$ | 0.77$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1394 | 66.4% | +0.164 | 📉 agota (-0.03) | +647.72$ | 1.64$ | ✅ activa |
| UPDOWN_GBM | 2356 | 53.1% | +0.031 | 📈 madura (+0.10) | +205.95$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5455 | 68.8% | +0.188 | ➡️ estable | +111.47$ | 1.88$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 242 | 60.7% | +0.107 | 📉 agota (-0.06) | +110.40$ | 1.07$ | ✅ activa |
| WEEKLY_PRICE | 336 | 68.2% | +0.180 | 📈 madura (+0.21) | +67.16$ | 1.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 868 | 62.7% | +0.126 | ➡️ estable | +40.76$ | 1.26$ | ✅ activa |
| STREAK_FADE_15M | 270 | 58.5% | +0.085 | 📉 agota (-0.06) | +34.12$ | 0.85$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 132 | 79.5% | +0.291 | ➡️ estable | +24.61$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 292 | 82.2% | +0.320 | ➡️ estable | +18.02$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1659 | 51.2% | +0.012 | ➡️ estable | +11.80$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 264 | 51.1% | +0.011 | 📉 agota (-0.16) | +10.21$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 336 | 38.7% | -0.112 | ➡️ estable | +4.40$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 25 | 88.0% | +0.352 | — | +2.05$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 13 | 53.8% | +0.022 | — | +0.20$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_5M | 439 | 47.4% | -0.026 | 📉 agota (-0.17) | -1.35$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| LATE_WINDOW_5MIN | 348 | 44.8% | -0.051 | 📉 agota (-0.14) | -4.38$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 320 | 44.1% | -0.059 | 📉 agota (-0.08) | -26.41$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-23T16:01 | GBM_LATE_5M#BTC#5min | Bitcoin Up or Down - July 23, 11:50AM-11:55AM ET… | ❌ LOSS | -1.46$ |
| 2026-07-23T16:01 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 23, 11:45AM-11:50AM ET… | ✅ WIN | +0.49$ |
| 2026-07-23T16:01 | GBM_LATE_5M#BTC#5min | Bitcoin Up or Down - July 23, 11:45AM-11:50AM ET… | ✅ WIN | +1.37$ |
| 2026-07-23T16:01 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 23, 11:30AM-11:45AM ET… | ✅ WIN | +0.97$ |
| 2026-07-23T16:01 | BALLENAS_CONFIRMADAS_15M#SOL#15min | Solana Up or Down - July 23, 11:30AM-11:45AM ET… | ❌ LOSS | -0.72$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-23T16:01 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,913.00 | 0.0min |  |
| ✅ ETH | $1,893.26 | 0.0min |  |
| ✅ SOL | $76.33 | 0.0min |  |
| ✅ XRP | $1.11 | 0.0min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,868.93 | consenso |  |
| ETH | $1,892.47 | consenso |  |
| SOL | $76.25 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*