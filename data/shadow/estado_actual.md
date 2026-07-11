# Estado del bot — 2026-07-11 05:12 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **25.30 $** |
| P&L real total | 🔴 **-0.14 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | +17.32 $ |
| Fees pagados (real) | 7.27 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +889.24 $ |
| P&L sim compuesto | 🟢 +1359.36 $ (ficción Kelly: +5343% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +79.96 $ |
| Operaciones resueltas | 8681 (4841 WIN / 3840 LOSS) — 55.8% |
| Señales abiertas | 167 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3118 | 61.4% | +0.114 | ➡️ estable | +1004.69$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 534 | 66.5% | +0.164 | ➡️ estable | +243.39$ | 1.64$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 661 | 57.0% | +0.070 | 📈 madura (+0.04) | +123.67$ | 0.70$ | ✅ activa |
| STREAK_FADE_15M | 124 | 61.3% | +0.111 | 📈 madura (+0.09) | +17.69$ | 1.11$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 40 | 67.5% | +0.167 | 📈 madura (+0.32) | +12.54$ | 1.67$ | ✅ activa |
| GBM_LATE_60M | 259 | 39.0% | -0.109 | 📈 madura (+0.10) | +10.94$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM | 1249 | 48.6% | -0.014 | ➡️ estable | -0.62$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 330 | 67.9% | +0.178 | ➡️ estable | -10.80$ | 1.78$ | ✅ activa |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T05:06 | GBM_LATE_60M#SOL#60min | Solana Up or Down - July 11, 12AM ET… | ✅ WIN | +0.54$ |
| 2026-07-11T05:06 | GBM_LATE_60M#BTC#60min | Bitcoin Up or Down - July 11, 12AM ET… | ✅ WIN | +0.19$ |
| 2026-07-11T05:06 | FAVORITO_CONFIRMADO#SOL#60min | Solana Up or Down - July 11, 12AM ET… | ✅ WIN | +1.25$ |
| 2026-07-11T05:06 | FAVORITO_CONFIRMADO#BTC#60min | Bitcoin Up or Down - July 11, 12AM ET… | ❌ LOSS | -1.04$ |
| 2026-07-11T05:04 | FAVORITO_CONFIRMADO#ETH#60min | Ethereum Up or Down - July 11, 12AM ET… | ❌ LOSS | -0.62$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T05:11 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,144.76 | 0.1min |  |
| ✅ ETH | $1,796.31 | 0.1min |  |
| ✅ SOL | $77.69 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,144.76 | consenso |  |
| ETH | $1,796.39 | consenso |  |
| SOL | $77.69 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*