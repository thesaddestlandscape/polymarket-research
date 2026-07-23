# Estado del bot — 2026-07-23 03:44 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **29.23 $** |
| P&L real total | 🔴 **-21.99 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -0.91 $ |
| Fees pagados (real) | 9.69 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3591.80 $ |
| P&L sim compuesto | 🟢 +6771.96 $ (ficción Kelly: +26619% s/ operativo) |
| P&L sim hoy (2026-07-23) | 🟢 +60.10 $ |
| Operaciones resueltas | 30144 (18132 WIN / 12012 LOSS) — 60.2% |
| Señales abiertas | 145 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 7018 | 59.7% | +0.097 | 📉 agota (-0.03) | +2201.60$ | 0.97$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4218 | 62.8% | +0.128 | 📉 agota (-0.04) | +2173.74$ | 1.28$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4220 | 58.2% | +0.082 | ➡️ estable | +1289.56$ | 0.82$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1304 | 66.5% | +0.165 | ➡️ estable | +595.94$ | 1.65$ | ✅ activa |
| UPDOWN_GBM | 2275 | 52.9% | +0.029 | 📈 madura (+0.11) | +186.57$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 239 | 61.1% | +0.110 | 📉 agota (-0.07) | +110.98$ | 1.10$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5258 | 68.8% | +0.188 | ➡️ estable | +97.04$ | 1.88$ | ✅ activa |
| WEEKLY_PRICE | 336 | 68.2% | +0.180 | 📈 madura (+0.21) | +67.16$ | 1.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 817 | 62.9% | +0.129 | ➡️ estable | +36.41$ | 1.29$ | ✅ activa |
| STREAK_FADE_15M | 267 | 58.4% | +0.084 | 📉 agota (-0.08) | +32.81$ | 0.84$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 126 | 79.4% | +0.289 | 📈 madura (+0.03) | +22.84$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 279 | 81.7% | +0.315 | ➡️ estable | +13.42$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1656 | 51.2% | +0.012 | ➡️ estable | +13.33$ | 0.50$ | ✅ activa |
| GBM_LATE_5M | 303 | 48.5% | -0.015 | 📉 agota (-0.17) | +11.10$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 263 | 51.0% | +0.009 | 📉 agota (-0.17) | +9.67$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 336 | 38.7% | -0.112 | ➡️ estable | +4.40$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 19 | 84.2% | +0.294 | — | +0.40$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 11 | 45.5% | -0.021 | — | -0.76$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 331 | 45.6% | -0.044 | 📉 agota (-0.15) | -1.92$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 318 | 44.0% | -0.059 | 📉 agota (-0.09) | -25.84$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-23T03:43 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 22, 11:30PM-11:35PM ET… | ✅ WIN | +0.68$ |
| 2026-07-23T03:40 | GBM_LATE_5M#SOL#5min | Solana Up or Down - July 22, 11:30PM-11:35PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-23T03:37 | ORDER_FLOW_5M#ETH#5min | Ethereum Up or Down - July 22, 11:25PM-11:30PM ET… | ✅ WIN | +0.50$ |
| 2026-07-23T03:37 | BALLENAS_CONFIRMADAS_15M#ETH#15min | Ethereum Up or Down - July 22, 11:15PM-11:30PM ET… | ✅ WIN | +0.72$ |
| 2026-07-23T03:37 | GBM_LATE_15M_PYCONFIRMADO#ETH#15min | Ethereum Up or Down - July 22, 11:15PM-11:30PM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-23T03:43 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,644.99 | 0.1min |  |
| ✅ ETH | $1,922.05 | 0.1min |  |
| ✅ SOL | $77.61 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,645.20 | consenso |  |
| ETH | $1,922.07 | consenso |  |
| SOL | $77.58 | consenso |  |
| XRP | $1.14 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*