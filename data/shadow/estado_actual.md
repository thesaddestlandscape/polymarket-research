# Estado del bot — 2026-07-22 05:44 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **24.46 $** |
| P&L real total | 🔴 **-26.76 $** |
| P&L real hoy | +1.95 $ |
| P&L real 7 días | -7.64 $ |
| Fees pagados (real) | 9.10 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3391.30 $ |
| P&L sim compuesto | 🟢 +6417.19 $ (ficción Kelly: +25225% s/ operativo) |
| P&L sim hoy (2026-07-22) | 🟢 +53.68 $ |
| Operaciones resueltas | 28321 (16999 WIN / 11322 LOSS) — 60.0% |
| Señales abiertas | 142 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6745 | 59.7% | +0.097 | ➡️ estable | +2144.74$ | 0.98$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3939 | 63.1% | +0.131 | 📉 agota (-0.04) | +2083.76$ | 1.31$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3912 | 58.5% | +0.085 | ➡️ estable | +1241.55$ | 0.85$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1121 | 66.2% | +0.162 | 📉 agota (-0.04) | +495.89$ | 1.62$ | ✅ activa |
| UPDOWN_GBM | 2142 | 52.7% | +0.027 | 📈 madura (+0.11) | +173.70$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 224 | 61.2% | +0.111 | 📉 agota (-0.06) | +107.55$ | 1.11$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4900 | 68.6% | +0.186 | ➡️ estable | +73.63$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| STREAK_FADE_15M | 261 | 58.2% | +0.082 | 📉 agota (-0.08) | +30.75$ | 0.82$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 696 | 62.4% | +0.123 | 📉 agota (-0.04) | +24.98$ | 1.23$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 117 | 78.6% | +0.282 | ➡️ estable | +19.54$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 247 | 81.8% | +0.315 | ➡️ estable | +12.39$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1653 | 51.1% | +0.011 | ➡️ estable | +11.85$ | 0.50$ | ✅ activa |
| GBM_LATE_5M | 275 | 49.5% | -0.005 | 📉 agota (-0.12) | +10.22$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 257 | 51.0% | +0.010 | 📉 agota (-0.15) | +9.66$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 330 | 38.8% | -0.111 | ➡️ estable | +6.19$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| LATE_WINDOW_5MIN | 295 | 45.8% | -0.042 | 📉 agota (-0.17) | +0.37$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 8 | 50.0% | +0.000 | — | -0.26$ | 0.50$ | ✅ activa |
| BALLENAS_TARDIAS | 13 | 76.9% | +0.152 | — | -1.30$ | 1.52$ | ✅ activa |
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
| 2026-07-22T05:40 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 22, 1:30AM-1:35AM ET… | ✅ WIN | +0.59$ |
| 2026-07-22T05:40 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 22, 1:25AM-1:30AM ET… | ✅ WIN | +2.72$ |
| 2026-07-22T05:40 | GBM_LATE_5M#BTC#5min | Bitcoin Up or Down - July 22, 1:25AM-1:30AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-22T05:34 | GBM_LATE_5M#ETH#5min | Ethereum Up or Down - July 22, 1:25AM-1:30AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-22T05:34 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 22, 1:15AM-1:30AM ET… | ✅ WIN | +0.12$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-22T05:42 UTC | rechazos 1h: 3 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,946.62 | 0.1min |  |
| ✅ ETH | $1,918.53 | 0.1min |  |
| ✅ SOL | $77.49 | 0.1min |  |
| ✅ XRP | $1.13 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,946.62 | consenso |  |
| ETH | $1,918.62 | consenso |  |
| SOL | $77.49 | consenso |  |
| XRP | $1.13 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:3 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*