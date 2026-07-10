# Estado del bot — 2026-07-10 04:02 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **31.45 $** |
| P&L real total | 🟢 **+6.01 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | +8.26 $ |
| Fees pagados (real) | 6.95 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +633.86 $ |
| P&L sim compuesto | 🟢 +974.17 $ (ficción Kelly: +3829% s/ operativo) |
| P&L sim hoy (2026-07-10) | 🟢 +62.23 $ |
| Operaciones resueltas | 7115 (3854 WIN / 3261 LOSS) — 54.2% |
| Señales abiertas | 168 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2734 | 61.4% | +0.114 | 📈 madura (+0.03) | +908.11$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 225 | 64.9% | +0.148 | ➡️ estable | +66.29$ | 1.48$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 282 | 54.3% | +0.042 | 📈 madura (+0.08) | +28.45$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1566 | 51.3% | +0.013 | ➡️ estable | +18.63$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 111 | 58.6% | +0.084 | 📈 madura (+0.04) | +10.35$ | 0.84$ | ✅ activa |
| LATE_WINDOW_5MIN | 34 | 70.6% | +0.194 | 📉 agota (-0.11) | +9.39$ | 1.94$ | ✅ activa |
| GBM_LATE_60M | 206 | 37.4% | -0.125 | 📈 madura (+0.09) | +6.26$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| LEADLAG_BTC_XRP_15M | 14 | 50.0% | +0.000 | — | -0.16$ | 0.50$ | ✅ activa |
| UPDOWN_GBM | 1204 | 48.5% | -0.015 | ➡️ estable | -0.60$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 132 | 34.1% | -0.157 | 📉 agota (-0.10) | -0.77$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 159 | 55.3% | +0.053 | 📈 madura (+0.14) | -15.64$ | 0.53$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-10T04:00 | GBM_LATE_60M#ETH#60min | Ethereum Up or Down - July 9, 11PM ET… | ✅ WIN | +1.53$ |
| 2026-07-10T03:48 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 9, 11:30PM-11:45PM ET… | ❌ LOSS | -1.23$ |
| 2026-07-10T03:48 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 9, 11:30PM-11:45PM ET… | ✅ WIN | +0.48$ |
| 2026-07-10T03:48 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 9, 11:30PM-11:45PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-10T03:48 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 9, 11:30PM-11:45PM ET… | ❌ LOSS | -1.85$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-10T04:02 UTC | rechazos 1h: 3 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,873.26 | 0.1min |  |
| ✅ ETH | $1,773.88 | 0.1min |  |
| ✅ SOL | $79.03 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,873.26 | consenso |  |
| ETH | $1,773.88 | consenso |  |
| SOL | $78.87 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:3 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*