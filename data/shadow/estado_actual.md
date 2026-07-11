# Estado del bot — 2026-07-11 23:43 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **15.81 $** |
| P&L real total | 🔴 **-9.63 $** |
| P&L real hoy | -9.49 $ |
| P&L real 7 días | +7.83 $ |
| Fees pagados (real) | 7.56 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1022.48 $ |
| P&L sim compuesto | 🟢 +1584.67 $ (ficción Kelly: +6229% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +305.26 $ |
| Operaciones resueltas | 9955 (5603 WIN / 4352 LOSS) — 56.3% |
| Señales abiertas | 186 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3384 | 61.1% | +0.111 | ➡️ estable | +1065.48$ | 1.11$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 763 | 64.4% | +0.143 | 📉 agota (-0.05) | +320.50$ | 1.43$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 927 | 57.5% | +0.075 | ➡️ estable | +187.75$ | 0.75$ | ✅ activa |
| STREAK_FADE_15M | 134 | 61.9% | +0.118 | 📈 madura (+0.13) | +21.31$ | 1.18$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 55 | 63.6% | +0.132 | 📈 madura (+0.08) | +16.63$ | 1.32$ | ✅ activa |
| UPDOWN_GBM | 1293 | 49.1% | -0.009 | 📈 madura (+0.04) | +15.08$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 300 | 38.7% | -0.113 | 📈 madura (+0.04) | +9.21$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| STREAK_FADE_5M | 55 | 50.9% | +0.009 | 📉 agota (-0.09) | -0.09$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 136 | 34.6% | -0.152 | 📉 agota (-0.13) | -0.14$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 657 | 67.4% | +0.174 | ➡️ estable | -8.14$ | 1.74$ | ✅ activa |
| WEEKLY_PRICE | 192 | 57.8% | +0.077 | 📈 madura (+0.23) | -13.59$ | 0.77$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T23:37 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 11, 7:30PM-7:35PM ET… | ✅ WIN | +0.16$ |
| 2026-07-11T23:37 | STREAK_FADE_5M#SOL#5min | Solana Up or Down - July 11, 7:30PM-7:35PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-11T23:34 | STREAK_FADE_5M#SOL#5min | Solana Up or Down - July 11, 7:25PM-7:30PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-11T23:30 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 11, 7:15PM-7:30PM ET… | ✅ WIN | +2.87$ |
| 2026-07-11T23:30 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 11, 7:15PM-7:30PM ET… | ✅ WIN | +1.36$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T23:42 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,871.19 | 0.1min |  |
| ✅ ETH | $1,788.62 | 0.1min |  |
| ✅ SOL | $76.94 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,882.80 | consenso |  |
| ETH | $1,788.66 | consenso |  |
| SOL | $76.89 | consenso |  |
| XRP | $1.10 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*