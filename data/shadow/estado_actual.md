# Estado del bot — 2026-07-20 15:48 UTC

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
| P&L fiel (stake fijo 1$) | +3403.91 $ |
| P&L sim compuesto | 🟢 +6269.65 $ (ficción Kelly: +24645% s/ operativo) |
| P&L sim hoy (2026-07-20) | 🟢 +271.32 $ |
| Operaciones resueltas | 24781 (15062 WIN / 9719 LOSS) — 60.8% |
| Señales abiertas | 128 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6191 | 60.7% | +0.107 | ➡️ estable | +2151.75$ | 1.07$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3401 | 65.3% | +0.153 | ➡️ estable | +2096.94$ | 1.53$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3378 | 60.0% | +0.100 | 📈 madura (+0.04) | +1228.37$ | 1.00$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 810 | 66.8% | +0.167 | 📉 agota (-0.04) | +357.21$ | 1.68$ | ✅ activa |
| UPDOWN_GBM | 1959 | 52.1% | +0.021 | 📈 madura (+0.11) | +133.67$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 182 | 65.9% | +0.158 | 📈 madura (+0.09) | +97.69$ | 1.58$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4276 | 68.6% | +0.186 | ➡️ estable | +78.25$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| STREAK_FADE_15M | 235 | 60.0% | +0.099 | ➡️ estable | +38.58$ | 0.99$ | ✅ activa |
| LATE_WINDOW_5MIN | 60 | 73.3% | +0.226 | 📈 madura (+0.12) | +32.92$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 211 | 56.9% | +0.068 | ➡️ estable | +21.93$ | 0.68$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 85 | 80.0% | +0.293 | 📉 agota (-0.11) | +16.42$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 450 | 63.8% | +0.137 | ➡️ estable | +15.45$ | 1.37$ | ✅ activa |
| ORDER_FLOW_5M | 1638 | 51.2% | +0.012 | ➡️ estable | +13.23$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 224 | 52.2% | +0.022 | 📉 agota (-0.15) | +12.64$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 186 | 82.3% | +0.319 | ➡️ estable | +9.93$ | 2.00$ | ✅ activa |
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
| 2026-07-20T15:47 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 20, 11:40AM-11:45AM ET… | ✅ WIN | +1.92$ |
| 2026-07-20T15:47 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 20, 11:30AM-11:45AM ET… | ✅ WIN | +2.13$ |
| 2026-07-20T15:47 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 20, 11:30AM-11:45AM ET… | ✅ WIN | +2.13$ |
| 2026-07-20T15:47 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 20, 11:30AM-11:45AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-20T15:47 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 20, 11:30AM-11:45AM ET… | ❌ LOSS | -1.31$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-20T15:47 UTC | rechazos 1h: 3 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,164.53 | 0.1min |  |
| ✅ ETH | $1,888.60 | 0.1min |  |
| ✅ SOL | $77.58 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,164.53 | consenso |  |
| ETH | $1,888.60 | consenso |  |
| SOL | $77.22 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:3 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*