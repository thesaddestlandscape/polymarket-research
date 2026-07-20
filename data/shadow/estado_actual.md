# Estado del bot — 2026-07-20 02:14 UTC

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
| P&L fiel (stake fijo 1$) | +3290.46 $ |
| P&L sim compuesto | 🟢 +6019.12 $ (ficción Kelly: +23660% s/ operativo) |
| P&L sim hoy (2026-07-20) | 🟢 +20.79 $ |
| Operaciones resueltas | 23621 (14354 WIN / 9267 LOSS) — 60.8% |
| Señales abiertas | 128 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6006 | 60.8% | +0.108 | ➡️ estable | +2116.22$ | 1.08$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3223 | 65.4% | +0.154 | ➡️ estable | +2004.68$ | 1.54$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3186 | 60.3% | +0.103 | 📈 madura (+0.05) | +1184.65$ | 1.03$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 717 | 67.5% | +0.175 | ➡️ estable | +321.33$ | 1.74$ | ✅ activa |
| UPDOWN_GBM | 1891 | 52.2% | +0.022 | 📈 madura (+0.12) | +142.44$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 179 | 65.9% | +0.157 | 📈 madura (+0.06) | +96.84$ | 1.57$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4042 | 68.6% | +0.186 | ➡️ estable | +56.40$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| STREAK_FADE_15M | 229 | 59.8% | +0.097 | ➡️ estable | +35.37$ | 0.97$ | ✅ activa |
| LATE_WINDOW_5MIN | 54 | 70.4% | +0.196 | ➡️ estable | +22.40$ | 1.96$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 382 | 64.1% | +0.141 | ➡️ estable | +16.17$ | 1.41$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 80 | 78.8% | +0.280 | 📉 agota (-0.12) | +13.90$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1634 | 51.2% | +0.012 | ➡️ estable | +13.23$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 210 | 52.9% | +0.028 | 📉 agota (-0.12) | +12.78$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 167 | 82.0% | +0.317 | ➡️ estable | +9.37$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 129 | 55.8% | +0.057 | ➡️ estable | +8.21$ | 0.57$ | ✅ activa |
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
| 2026-07-20T02:13 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 19, 10:05PM-10:10PM ET… | ✅ WIN | +1.63$ |
| 2026-07-20T02:13 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 19, 10:05PM-10:10PM ET… | ❌ LOSS | -1.95$ |
| 2026-07-20T02:08 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 19, 10:00PM-10:05PM ET… | ✅ WIN | +0.88$ |
| 2026-07-20T02:08 | FAVORITO_CONFIRMADO#SOL#60min | Solana Up or Down - July 19, 9PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-20T02:08 | FAVORITO_CONFIRMADO#ETH#60min | Ethereum Up or Down - July 19, 9PM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-20T02:13 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,823.22 | 0.1min |  |
| ✅ ETH | $1,876.11 | 0.1min |  |
| ✅ SOL | $76.90 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,823.22 | consenso |  |
| ETH | $1,876.27 | consenso |  |
| SOL | $76.82 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*