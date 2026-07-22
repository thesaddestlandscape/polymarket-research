# Estado del bot — 2026-07-22 12:00 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **26.34 $** |
| P&L real total | 🔴 **-24.88 $** |
| P&L real hoy | +3.83 $ |
| P&L real 7 días | -5.76 $ |
| Fees pagados (real) | 9.24 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3387.69 $ |
| P&L sim compuesto | 🟢 +6426.43 $ (ficción Kelly: +25261% s/ operativo) |
| P&L sim hoy (2026-07-22) | 🟢 +62.92 $ |
| Operaciones resueltas | 28812 (17273 WIN / 11539 LOSS) — 60.0% |
| Señales abiertas | 142 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6816 | 59.6% | +0.096 | 📉 agota (-0.03) | +2136.04$ | 0.96$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4015 | 62.8% | +0.128 | 📉 agota (-0.04) | +2083.14$ | 1.28$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4001 | 58.2% | +0.082 | ➡️ estable | +1235.14$ | 0.82$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1161 | 66.1% | +0.161 | 📉 agota (-0.05) | +518.62$ | 1.61$ | ✅ activa |
| UPDOWN_GBM | 2171 | 52.8% | +0.028 | 📈 madura (+0.11) | +178.98$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 226 | 61.1% | +0.110 | 📉 agota (-0.05) | +107.72$ | 1.10$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5006 | 68.6% | +0.186 | ➡️ estable | +70.02$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 730 | 62.3% | +0.123 | ➡️ estable | +29.80$ | 1.23$ | ✅ activa |
| STREAK_FADE_15M | 262 | 58.0% | +0.080 | 📉 agota (-0.08) | +28.71$ | 0.80$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 119 | 79.0% | +0.285 | ➡️ estable | +20.13$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 256 | 82.0% | +0.318 | ➡️ estable | +14.70$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1653 | 51.1% | +0.011 | ➡️ estable | +11.85$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 257 | 51.0% | +0.010 | 📉 agota (-0.15) | +9.66$ | 0.50$ | ✅ activa |
| GBM_LATE_5M | 280 | 48.6% | -0.014 | 📉 agota (-0.14) | +7.67$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 332 | 38.9% | -0.111 | ➡️ estable | +5.44$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 11 | 45.5% | -0.021 | — | -0.76$ | 0.50$ | ⚠️ IC negativo |
| BALLENAS_TARDIAS | 13 | 76.9% | +0.152 | — | -1.30$ | 1.52$ | ✅ activa |
| LATE_WINDOW_5MIN | 316 | 45.3% | -0.047 | 📉 agota (-0.18) | -1.65$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 316 | 44.3% | -0.057 | 📉 agota (-0.09) | -24.82$ | 0.50$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-22T11:52 | UPDOWN_GBM_15M_TARDIO#BNB#15min | BNB Up or Down - July 22, 7:30AM-7:45AM ET… | ❌ LOSS | -1.30$ |
| 2026-07-22T11:52 | UPDOWN_GBM#BNB#15min | BNB Up or Down - July 22, 7:30AM-7:45AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-22T11:52 | FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | Solana Up or Down - July 22, 7:30AM-7:45AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-22T11:52 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 22, 7:30AM-7:45AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-22T11:52 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 22, 7:30AM-7:45AM ET… | ✅ WIN | +1.62$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-22T11:58 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,983.07 | 0.1min |  |
| ✅ ETH | $1,926.48 | 0.1min |  |
| ✅ SOL | $77.59 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,983.07 | consenso |  |
| ETH | $1,926.48 | consenso |  |
| SOL | $77.54 | consenso |  |
| XRP | $1.14 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*