# Estado del bot — 2026-07-13 00:11 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **14.44 $** |
| P&L real total | 🔴 **-11.00 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | +5.58 $ |
| Fees pagados (real) | 7.77 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1362.43 $ |
| P&L sim compuesto | 🟢 +2233.19 $ (ficción Kelly: +8778% s/ operativo) |
| P&L sim hoy (2026-07-13) | 🟢 +19.72 $ |
| Operaciones resueltas | 11640 (6682 WIN / 4958 LOSS) — 57.4% |
| Señales abiertas | 120 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3739 | 61.2% | +0.112 | ➡️ estable | +1240.51$ | 1.12$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1086 | 66.5% | +0.165 | ➡️ estable | +646.79$ | 1.65$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1218 | 58.1% | +0.081 | 📈 madura (+0.03) | +305.32$ | 0.81$ | ✅ activa |
| UPDOWN_GBM | 1351 | 49.7% | -0.003 | 📈 madura (+0.08) | +31.81$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_15M | 159 | 62.3% | +0.121 | 📈 madura (+0.20) | +24.84$ | 1.21$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 75 | 62.7% | +0.123 | 📉 agota (-0.04) | +21.59$ | 1.23$ | ✅ activa |
| ORDER_FLOW_5M | 1586 | 51.3% | +0.013 | ➡️ estable | +16.48$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 318 | 39.0% | -0.109 | ➡️ estable | +8.24$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 1100 | 68.2% | +0.181 | 📈 madura (+0.05) | +5.99$ | 1.81$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM | 138 | 34.8% | -0.150 | 📉 agota (-0.11) | +0.19$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 178 | 47.8% | -0.022 | ➡️ estable | -7.82$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 204 | 57.4% | +0.073 | 📈 madura (+0.24) | -13.93$ | 0.73$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-13T00:07 | GBM_LATE_60M#ETH#60min | Ethereum Up or Down - July 12, 7PM ET… | ✅ WIN | +1.14$ |
| 2026-07-13T00:07 | FAVORITO_CONFIRMADO#ETH#60min | Ethereum Up or Down - July 12, 7PM ET… | ❌ LOSS | -1.78$ |
| 2026-07-13T00:02 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 12, 7:45PM-8:00PM ET… | ✅ WIN | +1.77$ |
| 2026-07-13T00:02 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 12, 7:45PM-8:00PM ET… | ✅ WIN | +1.44$ |
| 2026-07-13T00:02 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 12, 7:45PM-8:00PM ET… | ✅ WIN | +1.18$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-13T00:10 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,013.00 | 0.0min |  |
| ✅ ETH | $1,820.41 | 0.0min |  |
| ✅ SOL | $77.33 | 0.0min |  |
| ✅ XRP | $1.09 | 0.0min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,982.40 | consenso |  |
| ETH | $1,820.33 | consenso |  |
| SOL | $77.40 | consenso |  |
| XRP | $1.09 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*