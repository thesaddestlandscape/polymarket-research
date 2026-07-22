# Estado del bot — 2026-07-22 16:03 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **28.95 $** |
| P&L real total | 🔴 **-22.27 $** |
| P&L real hoy | +6.44 $ |
| P&L real 7 días | -3.15 $ |
| Fees pagados (real) | 9.37 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3453.70 $ |
| P&L sim compuesto | 🟢 +6564.84 $ (ficción Kelly: +25805% s/ operativo) |
| P&L sim hoy (2026-07-22) | 🟢 +201.33 $ |
| Operaciones resueltas | 29145 (17505 WIN / 11640 LOSS) — 60.1% |
| Señales abiertas | 140 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6865 | 59.6% | +0.096 | 📉 agota (-0.03) | +2151.79$ | 0.96$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4064 | 62.9% | +0.129 | 📉 agota (-0.04) | +2116.36$ | 1.29$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4057 | 58.2% | +0.082 | ➡️ estable | +1251.96$ | 0.82$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1199 | 66.5% | +0.164 | 📉 agota (-0.04) | +550.79$ | 1.64$ | ✅ activa |
| UPDOWN_GBM | 2193 | 52.9% | +0.029 | 📈 madura (+0.11) | +186.45$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 229 | 61.6% | +0.115 | 📉 agota (-0.05) | +109.27$ | 1.15$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5070 | 68.8% | +0.188 | ➡️ estable | +95.19$ | 1.87$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 756 | 62.4% | +0.124 | ➡️ estable | +32.90$ | 1.24$ | ✅ activa |
| STREAK_FADE_15M | 263 | 58.2% | +0.081 | 📉 agota (-0.07) | +30.04$ | 0.81$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 119 | 79.0% | +0.285 | ➡️ estable | +20.13$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 263 | 82.5% | +0.323 | ➡️ estable | +18.78$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1653 | 51.1% | +0.011 | ➡️ estable | +11.85$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 260 | 51.2% | +0.011 | 📉 agota (-0.16) | +10.25$ | 0.50$ | ✅ activa |
| GBM_LATE_5M | 284 | 48.2% | -0.017 | 📉 agota (-0.13) | +5.25$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 335 | 38.8% | -0.111 | ➡️ estable | +4.91$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 11 | 45.5% | -0.021 | — | -0.76$ | 0.50$ | ⚠️ IC negativo |
| BALLENAS_TARDIAS | 15 | 80.0% | +0.199 | — | -0.90$ | 1.99$ | ✅ activa |
| LATE_WINDOW_5MIN | 322 | 45.3% | -0.046 | 📉 agota (-0.17) | -1.93$ | 0.50$ | ⚠️ IC negativo |
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
| 2026-07-22T15:55 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 22, 11:30AM-11:45AM ET… | ✅ WIN | +0.50$ |
| 2026-07-22T15:55 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 22, 11:30AM-11:45AM ET… | ✅ WIN | +0.59$ |
| 2026-07-22T15:55 | STREAK_FADE_15M#XRP#15min | XRP Up or Down - July 22, 11:30AM-11:45AM ET… | ✅ WIN | +1.33$ |
| 2026-07-22T15:55 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 22, 11:30AM-11:45AM ET… | ✅ WIN | +1.77$ |
| 2026-07-22T15:55 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 22, 11:30AM-11:45AM ET… | ✅ WIN | +1.77$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-22T16:01 UTC | rechazos 1h: 3 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,017.24 | 0.1min |  |
| ✅ ETH | $1,942.12 | 0.1min |  |
| ✅ SOL | $78.46 | 0.1min |  |
| ✅ XRP | $1.15 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,017.24 | consenso |  |
| ETH | $1,942.12 | consenso |  |
| SOL | $78.44 | consenso |  |
| XRP | $1.15 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:3 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*