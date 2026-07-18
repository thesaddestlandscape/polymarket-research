# Estado del bot — 2026-07-18 14:41 UTC

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
| P&L fiel (stake fijo 1$) | +2747.54 $ |
| P&L sim compuesto | 🟢 +4915.39 $ (ficción Kelly: +19321% s/ operativo) |
| P&L sim hoy (2026-07-18) | 🟢 +410.62 $ |
| Operaciones resueltas | 20758 (12503 WIN / 8255 LOSS) — 60.2% |
| Señales abiertas | 117 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 5542 | 60.4% | +0.104 | ➡️ estable | +1807.59$ | 1.04$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 2764 | 65.1% | +0.151 | ➡️ estable | +1622.41$ | 1.51$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 2704 | 60.2% | +0.102 | 📈 madura (+0.03) | +938.71$ | 1.02$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 465 | 68.8% | +0.187 | ➡️ estable | +203.11$ | 1.87$ | ✅ activa |
| UPDOWN_GBM | 1769 | 52.0% | +0.020 | 📈 madura (+0.13) | +128.41$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 162 | 66.7% | +0.165 | 📈 madura (+0.12) | +93.90$ | 1.65$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| STREAK_FADE_15M | 220 | 60.0% | +0.099 | 📈 madura (+0.04) | +35.87$ | 0.99$ | ✅ activa |
| FAVORITO_CONFIRMADO | 3430 | 68.4% | +0.184 | ➡️ estable | +27.86$ | 1.84$ | ✅ activa |
| LATE_WINDOW_5MIN | 49 | 73.5% | +0.225 | ➡️ estable | +24.54$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 175 | 56.0% | +0.059 | 📉 agota (-0.12) | +18.77$ | 0.59$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 175 | 65.7% | +0.155 | 📉 agota (-0.04) | +18.19$ | 1.55$ | ✅ activa |
| ORDER_FLOW_5M | 1630 | 51.3% | +0.013 | ➡️ estable | +14.21$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 47 | 83.0% | +0.316 | 📈 madura (+0.09) | +12.81$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 117 | 82.1% | +0.315 | ➡️ estable | +5.93$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 326 | 38.3% | -0.116 | ➡️ estable | +3.81$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM_ETH_15M_HORA7 | 3 | 66.7% | +0.015 | — | +0.37$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_5M | 22 | 59.1% | +0.083 | — | +0.02$ | 0.83$ | ✅ activa |
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
| 2026-07-18T14:40 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 18, 10:30AM-10:35AM ET… | ✅ WIN | +0.89$ |
| 2026-07-18T14:38 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 18, 10:15AM-10:30AM ET… | ✅ WIN | +2.80$ |
| 2026-07-18T14:38 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 18, 10:15AM-10:30AM ET… | ✅ WIN | +4.03$ |
| 2026-07-18T14:38 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 18, 10:15AM-10:30AM ET… | ✅ WIN | +3.77$ |
| 2026-07-18T14:38 | BALLENAS_CONFIRMADAS_15M#XRP#15min | XRP Up or Down - July 18, 10:15AM-10:30AM ET… | ❌ LOSS | -0.81$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-18T14:40 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,130.67 | 0.1min |  |
| ✅ ETH | $1,844.99 | 0.1min |  |
| ✅ SOL | $74.86 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,142.10 | consenso |  |
| ETH | $1,844.99 | consenso |  |
| SOL | $74.88 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*