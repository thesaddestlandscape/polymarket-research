# Estado del bot — 2026-07-19 02:27 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **0.78 $** |
| P&L real total | 🔴 **-24.66 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -17.21 $ |
| Fees pagados (real) | 8.68 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +2888.15 $ |
| P&L sim compuesto | 🟢 +5210.48 $ (ficción Kelly: +20481% s/ operativo) |
| P&L sim hoy (2026-07-19) | 🟢 +48.71 $ |
| Operaciones resueltas | 21724 (13110 WIN / 8614 LOSS) — 60.3% |
| Señales abiertas | 134 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 5692 | 60.5% | +0.105 | ➡️ estable | +1890.45$ | 1.05$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 2924 | 65.2% | +0.152 | ➡️ estable | +1738.93$ | 1.52$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 2865 | 60.1% | +0.101 | 📈 madura (+0.04) | +1004.06$ | 1.01$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 556 | 68.2% | +0.181 | ➡️ estable | +242.52$ | 1.81$ | ✅ activa |
| UPDOWN_GBM | 1798 | 52.1% | +0.021 | 📈 madura (+0.13) | +129.41$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 166 | 66.3% | +0.161 | 📈 madura (+0.09) | +91.95$ | 1.61$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| FAVORITO_CONFIRMADO | 3635 | 68.4% | +0.184 | ➡️ estable | +39.35$ | 1.83$ | ✅ activa |
| STREAK_FADE_15M | 223 | 59.6% | +0.096 | ➡️ estable | +33.70$ | 0.96$ | ✅ activa |
| LATE_WINDOW_5MIN | 49 | 73.5% | +0.225 | ➡️ estable | +24.54$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1631 | 51.3% | +0.013 | ➡️ estable | +13.70$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 184 | 53.8% | +0.038 | 📉 agota (-0.12) | +13.05$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 258 | 63.6% | +0.135 | 📉 agota (-0.08) | +10.88$ | 1.35$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 57 | 78.9% | +0.280 | ➡️ estable | +10.24$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 133 | 82.0% | +0.315 | ➡️ estable | +5.53$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 326 | 38.3% | -0.116 | ➡️ estable | +3.81$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM_ETH_15M_HORA7 | 3 | 66.7% | +0.015 | — | +0.37$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_5M | 66 | 54.5% | +0.044 | ➡️ estable | -0.87$ | 0.50$ | ✅ activa |
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
| 2026-07-19T02:18 | GBM_LATE_5M#BTC#5min | Bitcoin Up or Down - July 18, 10:10PM-10:15PM ET… | ✅ WIN | +0.20$ |
| 2026-07-19T02:16 | GBM_LATE_5M#SOL#5min | Solana Up or Down - July 18, 10:10PM-10:15PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-19T02:16 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 18, 10:00PM-10:15PM ET… | ✅ WIN | +0.15$ |
| 2026-07-19T02:16 | UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | Bitcoin Up or Down - July 18, 10:00PM-10:15PM ET… | ✅ WIN | +0.10$ |
| 2026-07-19T02:16 | UPDOWN_GBM_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 18, 10:00PM-10:15PM ET… | ✅ WIN | +0.06$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-19T02:25 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,775.04 | 0.1min |  |
| ✅ ETH | $1,866.65 | 0.1min |  |
| ✅ SOL | $76.01 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,775.04 | consenso |  |
| ETH | $1,866.65 | consenso |  |
| SOL | $75.94 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*