# Estado del bot — 2026-07-11 01:31 UTC

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
| P&L fiel (stake fijo 1$) | +827.17 $ |
| P&L sim compuesto | 🟢 +1291.09 $ (ficción Kelly: +5075% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +11.69 $ |
| Operaciones resueltas | 8447 (4692 WIN / 3755 LOSS) — 55.5% |
| Señales abiertas | 153 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3066 | 61.4% | +0.114 | ➡️ estable | +985.71$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 491 | 66.8% | +0.167 | ➡️ estable | +213.42$ | 1.67$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 610 | 56.6% | +0.065 | ➡️ estable | +101.75$ | 0.65$ | ✅ activa |
| ORDER_FLOW_5M | 1573 | 51.4% | +0.014 | ➡️ estable | +18.85$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 121 | 62.0% | +0.118 | 📈 madura (+0.13) | +18.64$ | 1.18$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 249 | 38.2% | -0.118 | 📈 madura (+0.07) | +6.50$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 34 | 61.8% | +0.111 | 📈 madura (+0.26) | +6.47$ | 1.11$ | ✅ activa |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| FAVORITO_CONFIRMADO | 264 | 68.2% | +0.180 | 📉 agota (-0.04) | +2.14$ | 1.80$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM | 1247 | 48.5% | -0.015 | ➡️ estable | -2.72$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T01:31 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 10, 9:15PM-9:30PM ET… | ✅ WIN | +0.10$ |
| 2026-07-11T01:31 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 10, 9:15PM-9:30PM ET… | ✅ WIN | +0.92$ |
| 2026-07-11T01:31 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 10, 9:15PM-9:30PM ET… | ✅ WIN | +1.70$ |
| 2026-07-11T01:31 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 10, 9:15PM-9:30PM ET… | ✅ WIN | +0.66$ |
| 2026-07-11T01:31 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 10, 9:15PM-9:30PM ET… | ✅ WIN | +0.69$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T01:31 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,204.53 | 0.1min |  |
| ✅ ETH | $1,795.34 | 0.1min |  |
| ✅ SOL | $77.99 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,204.53 | consenso |  |
| ETH | $1,795.34 | consenso |  |
| SOL | $77.94 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*