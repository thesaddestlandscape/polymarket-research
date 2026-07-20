# Estado del bot — 2026-07-20 17:08 UTC

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
| P&L fiel (stake fijo 1$) | +3427.87 $ |
| P&L sim compuesto | 🟢 +6326.87 $ (ficción Kelly: +24870% s/ operativo) |
| P&L sim hoy (2026-07-20) | 🟢 +328.55 $ |
| Operaciones resueltas | 24909 (15143 WIN / 9766 LOSS) — 60.8% |
| Señales abiertas | 138 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6210 | 60.7% | +0.107 | ➡️ estable | +2160.44$ | 1.07$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3420 | 65.2% | +0.152 | ➡️ estable | +2113.51$ | 1.52$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3399 | 60.0% | +0.100 | 📈 madura (+0.04) | +1245.61$ | 1.00$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 819 | 66.8% | +0.167 | 📉 agota (-0.03) | +365.29$ | 1.68$ | ✅ activa |
| UPDOWN_GBM | 1963 | 52.1% | +0.021 | 📈 madura (+0.12) | +136.70$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 182 | 65.9% | +0.158 | 📈 madura (+0.09) | +97.69$ | 1.58$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4304 | 68.7% | +0.186 | ➡️ estable | +81.69$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 235 | 60.0% | +0.099 | ➡️ estable | +38.58$ | 0.99$ | ✅ activa |
| LATE_WINDOW_5MIN | 60 | 73.3% | +0.226 | 📈 madura (+0.12) | +32.92$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 212 | 56.6% | +0.065 | ➡️ estable | +21.42$ | 0.65$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 85 | 80.0% | +0.293 | 📉 agota (-0.11) | +16.42$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 226 | 52.7% | +0.026 | 📉 agota (-0.13) | +13.84$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1638 | 51.2% | +0.012 | ➡️ estable | +13.23$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 463 | 63.3% | +0.132 | ➡️ estable | +12.83$ | 1.32$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 188 | 82.4% | +0.321 | ➡️ estable | +10.70$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 6 | 66.7% | +0.037 | — | +0.87$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-20T17:07 | FAVORITO_CONFIRMADO#SOL#60min | Solana Up or Down - July 20, 12PM ET… | ✅ WIN | +0.94$ |
| 2026-07-20T17:04 | BALLENAS_CONFIRMADAS_15M#SOL#15min | Solana Up or Down - July 20, 12:45PM-1:00PM ET… | ✅ WIN | +0.49$ |
| 2026-07-20T17:04 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 20, 12:45PM-1:00PM ET… | ✅ WIN | +2.13$ |
| 2026-07-20T17:04 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 20, 12:45PM-1:00PM ET… | ❌ LOSS | -1.16$ |
| 2026-07-20T17:04 | UPDOWN_GBM_15M_TARDIO#BNB#15min | BNB Up or Down - July 20, 12:45PM-1:00PM ET… | ✅ WIN | +1.50$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-20T17:06 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,404.49 | 0.1min |  |
| ✅ ETH | $1,896.57 | 0.1min |  |
| ✅ SOL | $77.65 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,407.80 | consenso |  |
| ETH | $1,896.57 | consenso |  |
| SOL | $77.56 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*