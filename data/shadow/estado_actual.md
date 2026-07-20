# Estado del bot — 2026-07-20 02:30 UTC

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
| P&L fiel (stake fijo 1$) | +3295.43 $ |
| P&L sim compuesto | 🟢 +6029.57 $ (ficción Kelly: +23701% s/ operativo) |
| P&L sim hoy (2026-07-20) | 🟢 +31.25 $ |
| Operaciones resueltas | 23637 (14367 WIN / 9270 LOSS) — 60.8% |
| Señales abiertas | 133 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6008 | 60.8% | +0.108 | ➡️ estable | +2119.07$ | 1.08$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3225 | 65.5% | +0.154 | ➡️ estable | +2007.08$ | 1.54$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3188 | 60.4% | +0.103 | 📈 madura (+0.05) | +1187.41$ | 1.03$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 720 | 67.6% | +0.176 | ➡️ estable | +324.78$ | 1.76$ | ✅ activa |
| UPDOWN_GBM | 1893 | 52.2% | +0.022 | 📈 madura (+0.12) | +139.29$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 179 | 65.9% | +0.157 | 📈 madura (+0.06) | +96.84$ | 1.57$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4045 | 68.6% | +0.186 | ➡️ estable | +59.54$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| STREAK_FADE_15M | 229 | 59.8% | +0.097 | ➡️ estable | +35.37$ | 0.97$ | ✅ activa |
| LATE_WINDOW_5MIN | 54 | 70.4% | +0.196 | ➡️ estable | +22.40$ | 1.96$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 382 | 64.1% | +0.141 | ➡️ estable | +16.17$ | 1.41$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 81 | 79.0% | +0.283 | 📉 agota (-0.11) | +14.93$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1634 | 51.2% | +0.012 | ➡️ estable | +13.23$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 210 | 52.9% | +0.028 | 📉 agota (-0.12) | +12.78$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 167 | 82.0% | +0.317 | ➡️ estable | +9.37$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 130 | 55.4% | +0.053 | ➡️ estable | +6.17$ | 0.53$ | ✅ activa |
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
| 2026-07-20T02:29 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 19, 10:20PM-10:25PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-20T02:16 | UPDOWN_GBM_15M_TARDIO#SOL#15min | Solana Up or Down - July 19, 10:00PM-10:15PM ET… | ✅ WIN | +1.04$ |
| 2026-07-20T02:16 | UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | Ethereum Up or Down - July 19, 10:00PM-10:15PM ET… | ✅ WIN | +1.04$ |
| 2026-07-20T02:16 | UPDOWN_GBM_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 19, 10:00PM-10:15PM ET… | ✅ WIN | +0.64$ |
| 2026-07-20T02:16 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 19, 10:00PM-10:15PM ET… | ✅ WIN | +0.99$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-20T02:28 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,601.24 | 0.1min |  |
| ✅ ETH | $1,868.07 | 0.1min |  |
| ✅ SOL | $76.54 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,601.50 | consenso |  |
| ETH | $1,868.38 | consenso |  |
| SOL | $76.42 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*