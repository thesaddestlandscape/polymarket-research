# Estado del bot — 2026-07-11 23:49 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **16.74 $** |
| P&L real total | 🔴 **-8.70 $** |
| P&L real hoy | -10.59 $ |
| P&L real 7 días | +6.73 $ |
| Fees pagados (real) | 7.56 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1028.87 $ |
| P&L sim compuesto | 🟢 +1594.25 $ (ficción Kelly: +6267% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +314.85 $ |
| Operaciones resueltas | 9965 (5612 WIN / 4353 LOSS) — 56.3% |
| Señales abiertas | 185 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3385 | 61.1% | +0.111 | ➡️ estable | +1067.29$ | 1.11$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 764 | 64.4% | +0.144 | 📉 agota (-0.05) | +322.54$ | 1.44$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 928 | 57.5% | +0.075 | ➡️ estable | +189.79$ | 0.75$ | ✅ activa |
| STREAK_FADE_15M | 134 | 61.9% | +0.118 | 📈 madura (+0.13) | +21.31$ | 1.18$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 56 | 64.3% | +0.138 | 📈 madura (+0.07) | +18.67$ | 1.38$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| UPDOWN_GBM | 1294 | 49.1% | -0.008 | 📈 madura (+0.05) | +15.60$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 300 | 38.7% | -0.113 | 📈 madura (+0.04) | +9.21$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| STREAK_FADE_5M | 58 | 51.7% | +0.017 | 📉 agota (-0.06) | +0.36$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 136 | 34.6% | -0.152 | 📉 agota (-0.13) | -0.14$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 659 | 67.5% | +0.175 | ➡️ estable | -7.46$ | 1.75$ | ✅ activa |
| WEEKLY_PRICE | 192 | 57.8% | +0.077 | 📈 madura (+0.23) | -13.59$ | 0.77$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T23:49 | STREAK_FADE_5M#ETH#5min | Ethereum Up or Down - July 11, 7:40PM-7:45PM ET… | ✅ WIN | +0.48$ |
| 2026-07-11T23:46 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 11, 7:35PM-7:40PM ET… | ✅ WIN | +0.55$ |
| 2026-07-11T23:46 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 11, 7:30PM-7:45PM ET… | ✅ WIN | +2.04$ |
| 2026-07-11T23:46 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 11, 7:30PM-7:45PM ET… | ✅ WIN | +0.13$ |
| 2026-07-11T23:46 | STREAK_FADE_5M#ETH#5min | Ethereum Up or Down - July 11, 7:35PM-7:40PM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T23:49 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,928.75 | 0.1min |  |
| ✅ ETH | $1,790.48 | 0.1min |  |
| ✅ SOL | $77.06 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,928.75 | consenso |  |
| ETH | $1,790.49 | consenso |  |
| SOL | $76.99 | consenso |  |
| XRP | $1.10 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*