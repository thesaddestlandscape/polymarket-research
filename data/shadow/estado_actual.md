# Estado del bot — 2026-07-20 03:01 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **0.78 $** |
| P&L real total | 🔴 **-24.66 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -13.66 $ |
| Fees pagados (real) | 8.68 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3318.54 $ |
| P&L sim compuesto | 🟢 +6076.98 $ (ficción Kelly: +23888% s/ operativo) |
| P&L sim hoy (2026-07-20) | 🟢 +78.66 $ |
| Operaciones resueltas | 23700 (14419 WIN / 9281 LOSS) — 60.8% |
| Señales abiertas | 120 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6017 | 60.9% | +0.109 | ➡️ estable | +2133.12$ | 1.09$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3235 | 65.6% | +0.156 | ➡️ estable | +2023.15$ | 1.55$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3197 | 60.4% | +0.104 | 📈 madura (+0.05) | +1194.92$ | 1.04$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 727 | 67.5% | +0.175 | ➡️ estable | +327.51$ | 1.75$ | ✅ activa |
| UPDOWN_GBM | 1895 | 52.1% | +0.021 | 📈 madura (+0.12) | +136.76$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 180 | 65.6% | +0.154 | 📈 madura (+0.07) | +96.33$ | 1.54$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4057 | 68.7% | +0.187 | ➡️ estable | +65.09$ | 1.87$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| STREAK_FADE_15M | 229 | 59.8% | +0.097 | ➡️ estable | +35.37$ | 0.97$ | ✅ activa |
| LATE_WINDOW_5MIN | 54 | 70.4% | +0.196 | ➡️ estable | +22.40$ | 1.96$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 388 | 64.4% | +0.144 | ➡️ estable | +17.92$ | 1.44$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 81 | 79.0% | +0.283 | 📉 agota (-0.11) | +14.93$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1634 | 51.2% | +0.012 | ➡️ estable | +13.23$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 211 | 52.6% | +0.026 | 📉 agota (-0.13) | +12.27$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 169 | 82.2% | +0.319 | ➡️ estable | +9.80$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 134 | 56.0% | +0.059 | ➡️ estable | +9.03$ | 0.59$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 5 | 60.0% | +0.018 | — | +0.32$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 149 | 32.9% | -0.169 | 📉 agota (-0.12) | -4.27$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-20T03:00 | GBM_LATE_15M_PYCONFIRMADO#ETH#15min | Ethereum Up or Down - July 19, 10:45PM-11:00PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-20T03:00 | BALLENAS_CONFIRMADAS_15M#ETH#15min | Ethereum Up or Down - July 19, 10:45PM-11:00PM ET… | ✅ WIN | +0.41$ |
| 2026-07-20T03:00 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 19, 10:45PM-11:00PM ET… | ✅ WIN | +0.41$ |
| 2026-07-20T03:00 | FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | Solana Up or Down - July 19, 10:45PM-11:00PM ET… | ✅ WIN | +0.21$ |
| 2026-07-20T03:00 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 19, 10:45PM-11:00PM ET… | ✅ WIN | +0.21$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-20T03:00 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,788.28 | 0.1min |  |
| ✅ ETH | $1,877.79 | 0.1min |  |
| ✅ SOL | $76.99 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,796.80 | consenso |  |
| ETH | $1,878.45 | consenso |  |
| SOL | $77.03 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*