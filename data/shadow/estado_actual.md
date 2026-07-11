# Estado del bot — 2026-07-11 17:56 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **23.52 $** |
| P&L real total | 🔴 **-1.92 $** |
| P&L real hoy | -1.78 $ |
| P&L real 7 días | +15.54 $ |
| Fees pagados (real) | 7.36 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +967.09 $ |
| P&L sim compuesto | 🟢 +1509.55 $ (ficción Kelly: +5934% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +230.15 $ |
| Operaciones resueltas | 9561 (5352 WIN / 4209 LOSS) — 56.0% |
| Señales abiertas | 182 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3307 | 61.1% | +0.110 | ➡️ estable | +1047.44$ | 1.10$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 695 | 64.3% | +0.143 | ➡️ estable | +305.68$ | 1.43$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 850 | 57.4% | +0.074 | 📈 madura (+0.03) | +174.83$ | 0.74$ | ✅ activa |
| STREAK_FADE_15M | 131 | 61.8% | +0.117 | 📈 madura (+0.12) | +19.89$ | 1.17$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 52 | 65.4% | +0.148 | 📈 madura (+0.14) | +17.26$ | 1.48$ | ✅ activa |
| UPDOWN_GBM | 1278 | 48.9% | -0.011 | 📈 madura (+0.03) | +12.09$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 288 | 39.2% | -0.107 | 📈 madura (+0.08) | +11.37$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 136 | 34.6% | -0.152 | 📉 agota (-0.13) | -0.14$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 19 | 47.4% | -0.023 | — | -0.70$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 192 | 57.8% | +0.077 | 📈 madura (+0.23) | -13.59$ | 0.77$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 554 | 65.7% | +0.156 | 📉 agota (-0.04) | -35.25$ | 1.56$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T17:48 | STREAK_FADE_5M#SOL#5min | Solana Up or Down - July 11, 1:40PM-1:45PM ET… | ✅ WIN | +0.50$ |
| 2026-07-11T17:46 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 11, 1:30PM-1:45PM ET… | ✅ WIN | +0.48$ |
| 2026-07-11T17:46 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 11, 1:30PM-1:45PM ET… | ✅ WIN | +0.44$ |
| 2026-07-11T17:46 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 11, 1:30PM-1:45PM ET… | ✅ WIN | +0.94$ |
| 2026-07-11T17:46 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 11, 1:30PM-1:45PM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T17:55 UTC | rechazos 1h: 3 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,288.97 | 0.1min |  |
| ✅ ETH | $1,823.91 | 0.1min |  |
| ✅ SOL | $78.08 | 0.1min |  |
| ✅ XRP | $1.12 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,289.00 | consenso |  |
| ETH | $1,823.91 | consenso |  |
| SOL | $78.02 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:3 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*