# Estado del bot — 2026-07-18 15:14 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **0.78 $** |
| P&L real total | 🔴 **-24.66 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -24.52 $ |
| Fees pagados (real) | 8.68 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +2765.91 $ |
| P&L sim compuesto | 🟢 +4947.29 $ (ficción Kelly: +19447% s/ operativo) |
| P&L sim hoy (2026-07-18) | 🟢 +442.53 $ |
| Operaciones resueltas | 20807 (12539 WIN / 8268 LOSS) — 60.3% |
| Señales abiertas | 104 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 5548 | 60.5% | +0.105 | ➡️ estable | +1816.43$ | 1.04$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 2771 | 65.1% | +0.151 | ➡️ estable | +1623.39$ | 1.51$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 2710 | 60.2% | +0.102 | 📈 madura (+0.03) | +948.49$ | 1.02$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 470 | 68.9% | +0.189 | ➡️ estable | +207.62$ | 1.89$ | ✅ activa |
| UPDOWN_GBM | 1772 | 52.1% | +0.021 | 📈 madura (+0.13) | +132.78$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 162 | 66.7% | +0.165 | 📈 madura (+0.12) | +93.90$ | 1.65$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| STREAK_FADE_15M | 221 | 59.7% | +0.096 | 📈 madura (+0.03) | +33.83$ | 0.96$ | ✅ activa |
| FAVORITO_CONFIRMADO | 3442 | 68.4% | +0.184 | ➡️ estable | +32.74$ | 1.84$ | ✅ activa |
| LATE_WINDOW_5MIN | 49 | 73.5% | +0.225 | ➡️ estable | +24.54$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 176 | 56.2% | +0.062 | 📉 agota (-0.10) | +19.29$ | 0.62$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 179 | 65.4% | +0.152 | 📉 agota (-0.04) | +15.36$ | 1.52$ | ✅ activa |
| ORDER_FLOW_5M | 1630 | 51.3% | +0.013 | ➡️ estable | +14.21$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 48 | 83.3% | +0.320 | 📈 madura (+0.08) | +14.08$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 118 | 82.2% | +0.317 | ➡️ estable | +6.85$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 326 | 38.3% | -0.116 | ➡️ estable | +3.81$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_5M | 24 | 58.3% | +0.077 | — | +0.76$ | 0.77$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 3 | 66.7% | +0.015 | — | +0.37$ | 0.50$ | ⏳ acumulando |
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
| 2026-07-18T15:08 | BALLENAS_CONFIRMADAS_15M#ETH#15min | Ethereum Up or Down - July 18, 10:45AM-11:00AM ET… | ✅ WIN | +0.68$ |
| 2026-07-18T15:08 | FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | Solana Up or Down - July 18, 10:45AM-11:00AM ET… | ✅ WIN | +0.92$ |
| 2026-07-18T15:08 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 18, 10:45AM-11:00AM ET… | ✅ WIN | +1.77$ |
| 2026-07-18T15:08 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 18, 10:45AM-11:00AM ET… | ✅ WIN | +4.94$ |
| 2026-07-18T15:08 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 18, 10:45AM-11:00AM ET… | ✅ WIN | +5.05$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-18T15:13 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,090.88 | 0.1min |  |
| ✅ ETH | $1,844.34 | 0.1min |  |
| ✅ SOL | $74.91 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,090.88 | consenso |  |
| ETH | $1,844.40 | consenso |  |
| SOL | $74.92 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*