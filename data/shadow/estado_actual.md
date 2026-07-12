# Estado del bot — 2026-07-12 23:00 UTC

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
| P&L fiel (stake fijo 1$) | +1354.18 $ |
| P&L sim compuesto | 🟢 +2218.46 $ (ficción Kelly: +8720% s/ operativo) |
| P&L sim hoy (2026-07-12) | 🟢 +613.74 $ |
| Operaciones resueltas | 11552 (6630 WIN / 4922 LOSS) — 57.4% |
| Señales abiertas | 149 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3720 | 61.3% | +0.113 | ➡️ estable | +1242.96$ | 1.13$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1068 | 66.5% | +0.164 | ➡️ estable | +628.01$ | 1.65$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1208 | 58.3% | +0.083 | 📈 madura (+0.03) | +308.84$ | 0.83$ | ✅ activa |
| UPDOWN_GBM | 1347 | 49.6% | -0.004 | 📈 madura (+0.07) | +29.18$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_15M | 158 | 62.0% | +0.119 | 📈 madura (+0.20) | +23.37$ | 1.19$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 72 | 62.5% | +0.122 | ➡️ estable | +19.96$ | 1.22$ | ✅ activa |
| ORDER_FLOW_5M | 1586 | 51.3% | +0.013 | ➡️ estable | +16.48$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO | 1070 | 68.4% | +0.184 | 📈 madura (+0.06) | +12.29$ | 1.83$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 317 | 38.8% | -0.111 | ➡️ estable | +7.10$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM | 138 | 34.8% | -0.150 | 📉 agota (-0.11) | +0.19$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 176 | 47.2% | -0.028 | ➡️ estable | -9.16$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 204 | 57.4% | +0.073 | 📈 madura (+0.24) | -13.93$ | 0.73$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-12T22:59 | STREAK_FADE_5M#XRP#5min | XRP Up or Down - July 12, 6:50PM-6:55PM ET… | ✅ WIN | +1.77$ |
| 2026-07-12T22:52 | STREAK_FADE_5M#XRP#5min | XRP Up or Down - July 12, 6:40PM-6:45PM ET… | ❌ LOSS | -1.92$ |
| 2026-07-12T22:50 | STREAK_FADE_5M#XRP#5min | XRP Up or Down - July 12, 6:45PM-6:50PM ET… | ❌ LOSS | -1.92$ |
| 2026-07-12T22:47 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 12, 6:30PM-6:45PM ET… | ✅ WIN | +1.96$ |
| 2026-07-12T22:47 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 12, 6:30PM-6:45PM ET… | ✅ WIN | +4.11$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-12T22:59 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,868.07 | 0.1min |  |
| ✅ ETH | $1,804.31 | 0.1min |  |
| ✅ SOL | $76.76 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,868.07 | consenso |  |
| ETH | $1,804.36 | consenso |  |
| SOL | $76.73 | consenso |  |
| XRP | $1.09 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*