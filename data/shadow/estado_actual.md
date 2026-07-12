# Estado del bot — 2026-07-12 22:44 UTC

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
| P&L fiel (stake fijo 1$) | +1350.84 $ |
| P&L sim compuesto | 🟢 +2211.92 $ (ficción Kelly: +8695% s/ operativo) |
| P&L sim hoy (2026-07-12) | 🟢 +607.21 $ |
| Operaciones resueltas | 11537 (6622 WIN / 4915 LOSS) — 57.4% |
| Señales abiertas | 147 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3718 | 61.3% | +0.113 | ➡️ estable | +1236.89$ | 1.13$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1066 | 66.4% | +0.164 | ➡️ estable | +621.94$ | 1.64$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1206 | 58.2% | +0.082 | 📈 madura (+0.03) | +303.79$ | 0.82$ | ✅ activa |
| UPDOWN_GBM | 1346 | 49.6% | -0.004 | 📈 madura (+0.07) | +28.66$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_15M | 157 | 62.4% | +0.123 | 📈 madura (+0.19) | +25.11$ | 1.23$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 71 | 63.4% | +0.130 | ➡️ estable | +21.20$ | 1.30$ | ✅ activa |
| FAVORITO_CONFIRMADO | 1067 | 68.6% | +0.186 | 📈 madura (+0.07) | +18.41$ | 1.85$ | ✅ activa |
| ORDER_FLOW_5M | 1586 | 51.3% | +0.013 | ➡️ estable | +16.48$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 317 | 38.8% | -0.111 | ➡️ estable | +7.10$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM | 138 | 34.8% | -0.150 | 📉 agota (-0.11) | +0.19$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 173 | 47.4% | -0.026 | ➡️ estable | -7.09$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 204 | 57.4% | +0.073 | 📈 madura (+0.24) | -13.93$ | 0.73$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-12T22:41 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 12, 6:30PM-6:35PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-12T22:38 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 12, 6:30PM-6:35PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-12T22:38 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 12, 6:15PM-6:30PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-12T22:38 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 12, 6:15PM-6:30PM ET… | ✅ WIN | +6.66$ |
| 2026-07-12T22:38 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 12, 6:15PM-6:30PM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-12T22:43 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,744.28 | 0.1min |  |
| ✅ ETH | $1,800.01 | 0.1min |  |
| ✅ SOL | $76.63 | 0.1min |  |
| ✅ XRP | $1.08 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,752.60 | consenso |  |
| ETH | $1,800.01 | consenso |  |
| SOL | $76.56 | consenso |  |
| XRP | $1.08 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*