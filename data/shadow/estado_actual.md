# Estado del bot — 2026-07-18 15:04 UTC

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
| P&L fiel (stake fijo 1$) | +2759.93 $ |
| P&L sim compuesto | 🟢 +4935.88 $ (ficción Kelly: +19402% s/ operativo) |
| P&L sim hoy (2026-07-18) | 🟢 +431.11 $ |
| Operaciones resueltas | 20791 (12528 WIN / 8263 LOSS) — 60.3% |
| Señales abiertas | 110 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 5546 | 60.4% | +0.104 | ➡️ estable | +1809.61$ | 1.04$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 2769 | 65.1% | +0.151 | ➡️ estable | +1623.66$ | 1.51$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 2708 | 60.2% | +0.102 | 📈 madura (+0.03) | +941.78$ | 1.02$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 469 | 69.1% | +0.190 | ➡️ estable | +209.20$ | 1.90$ | ✅ activa |
| UPDOWN_GBM | 1771 | 52.1% | +0.021 | 📈 madura (+0.13) | +131.01$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 162 | 66.7% | +0.165 | 📈 madura (+0.12) | +93.90$ | 1.65$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| STREAK_FADE_15M | 220 | 60.0% | +0.099 | 📈 madura (+0.04) | +35.87$ | 0.99$ | ✅ activa |
| FAVORITO_CONFIRMADO | 3439 | 68.5% | +0.184 | ➡️ estable | +32.86$ | 1.84$ | ✅ activa |
| LATE_WINDOW_5MIN | 49 | 73.5% | +0.225 | ➡️ estable | +24.54$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 176 | 56.2% | +0.062 | 📉 agota (-0.10) | +19.29$ | 0.62$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 176 | 65.3% | +0.152 | 📉 agota (-0.03) | +16.15$ | 1.52$ | ✅ activa |
| ORDER_FLOW_5M | 1630 | 51.3% | +0.013 | ➡️ estable | +14.21$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 48 | 83.3% | +0.320 | 📈 madura (+0.08) | +14.08$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 117 | 82.1% | +0.315 | ➡️ estable | +5.93$ | 2.00$ | ✅ activa |
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
| 2026-07-18T15:03 | FAVORITO_CONFIRMADO#XRP#5min | XRP Up or Down - July 18, 10:50AM-10:55AM ET… | ✅ WIN | +1.17$ |
| 2026-07-18T15:03 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 18, 10:45AM-11:00AM ET… | ❌ LOSS | -1.10$ |
| 2026-07-18T15:03 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 18, 10:45AM-11:00AM ET… | ✅ WIN | +0.92$ |
| 2026-07-18T15:00 | FAVORITO_CONFIRMADO#SOL#60min | Solana Up or Down - July 18, 10AM ET… | ✅ WIN | +1.15$ |
| 2026-07-18T15:00 | FAVORITO_CONFIRMADO#ETH#60min | Ethereum Up or Down - July 18, 10AM ET… | ✅ WIN | +1.24$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-18T15:02 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,085.47 | 0.1min |  |
| ✅ ETH | $1,844.28 | 0.1min |  |
| ✅ SOL | $74.94 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,085.47 | consenso |  |
| ETH | $1,844.28 | consenso |  |
| SOL | $74.89 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*