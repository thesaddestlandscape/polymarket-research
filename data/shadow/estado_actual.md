# Estado del bot — 2026-07-23 11:44 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **30.16 $** |
| P&L real total | 🔴 **-21.06 $** |
| P&L real hoy | +0.93 $ |
| P&L real 7 días | +0.02 $ |
| Fees pagados (real) | 9.81 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3627.06 $ |
| P&L sim compuesto | 🟢 +6886.43 $ (ficción Kelly: +27069% s/ operativo) |
| P&L sim hoy (2026-07-23) | 🟢 +174.57 $ |
| Operaciones resueltas | 30801 (18520 WIN / 12281 LOSS) — 60.1% |
| Señales abiertas | 147 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 7119 | 59.6% | +0.096 | 📉 agota (-0.03) | +2228.78$ | 0.96$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4315 | 62.7% | +0.127 | 📉 agota (-0.04) | +2194.44$ | 1.27$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4325 | 58.0% | +0.080 | ➡️ estable | +1302.22$ | 0.80$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1353 | 66.4% | +0.164 | ➡️ estable | +623.55$ | 1.64$ | ✅ activa |
| UPDOWN_GBM | 2317 | 53.1% | +0.031 | 📈 madura (+0.11) | +204.23$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 242 | 60.7% | +0.107 | 📉 agota (-0.06) | +110.40$ | 1.07$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5384 | 68.8% | +0.188 | ➡️ estable | +95.72$ | 1.88$ | ✅ activa |
| WEEKLY_PRICE | 336 | 68.2% | +0.180 | 📈 madura (+0.21) | +67.16$ | 1.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 856 | 62.9% | +0.128 | ➡️ estable | +45.69$ | 1.28$ | ✅ activa |
| STREAK_FADE_15M | 270 | 58.5% | +0.085 | 📉 agota (-0.06) | +34.12$ | 0.85$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 131 | 79.4% | +0.289 | ➡️ estable | +24.29$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 288 | 82.3% | +0.321 | ➡️ estable | +18.59$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1659 | 51.2% | +0.012 | ➡️ estable | +11.80$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 264 | 51.1% | +0.011 | 📉 agota (-0.16) | +10.21$ | 0.50$ | ✅ activa |
| GBM_LATE_5M | 363 | 47.9% | -0.021 | 📉 agota (-0.22) | +4.84$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 336 | 38.7% | -0.112 | ➡️ estable | +4.40$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 25 | 88.0% | +0.352 | — | +2.05$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 13 | 53.8% | +0.022 | — | +0.20$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| LATE_WINDOW_5MIN | 336 | 44.9% | -0.050 | 📉 agota (-0.16) | -4.47$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 319 | 44.2% | -0.058 | 📉 agota (-0.08) | -25.29$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-23T11:42 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 23, 7:30AM-7:35AM ET… | ❌ LOSS | -0.86$ |
| 2026-07-23T11:39 | GBM_LATE_5M#ETH#5min | Ethereum Up or Down - July 23, 7:25AM-7:30AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-23T11:39 | GBM_LATE_5M#SOL#5min | Solana Up or Down - July 23, 7:25AM-7:30AM ET… | ✅ WIN | +1.18$ |
| 2026-07-23T11:39 | GBM_LATE_5M#BTC#5min | Bitcoin Up or Down - July 23, 7:25AM-7:30AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-23T11:33 | UPDOWN_GBM_15M_TARDIO#SOL#15min | Solana Up or Down - July 23, 7:15AM-7:30AM ET… | ❌ LOSS | -1.08$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-23T11:42 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,538.00 | 0.0min |  |
| ✅ ETH | $1,925.06 | 0.0min |  |
| ✅ SOL | $77.64 | 0.0min |  |
| ✅ XRP | $1.13 | 0.0min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,531.70 | consenso |  |
| ETH | $1,925.15 | consenso |  |
| SOL | $77.66 | consenso |  |
| XRP | $1.13 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*