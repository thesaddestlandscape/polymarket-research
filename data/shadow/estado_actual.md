# Estado del bot — 2026-07-18 14:03 UTC

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
| P&L fiel (stake fijo 1$) | +2741.02 $ |
| P&L sim compuesto | 🟢 +4909.12 $ (ficción Kelly: +19297% s/ operativo) |
| P&L sim hoy (2026-07-18) | 🟢 +404.36 $ |
| Operaciones resueltas | 20708 (12478 WIN / 8230 LOSS) — 60.3% |
| Señales abiertas | 98 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 5534 | 60.4% | +0.104 | ➡️ estable | +1802.23$ | 1.04$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 2755 | 65.1% | +0.151 | ➡️ estable | +1614.93$ | 1.51$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 2696 | 60.2% | +0.102 | 📈 madura (+0.03) | +933.30$ | 1.02$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 461 | 68.5% | +0.185 | ➡️ estable | +198.90$ | 1.85$ | ✅ activa |
| UPDOWN_GBM | 1766 | 51.9% | +0.019 | 📈 madura (+0.12) | +124.22$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 162 | 66.7% | +0.165 | 📈 madura (+0.12) | +93.90$ | 1.65$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| STREAK_FADE_15M | 218 | 60.6% | +0.105 | 📈 madura (+0.05) | +39.44$ | 1.04$ | ✅ activa |
| FAVORITO_CONFIRMADO | 3421 | 68.5% | +0.185 | ➡️ estable | +36.45$ | 1.85$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 169 | 68.0% | +0.178 | ➡️ estable | +26.69$ | 1.78$ | ✅ activa |
| LATE_WINDOW_5MIN | 49 | 73.5% | +0.225 | ➡️ estable | +24.54$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 175 | 56.0% | +0.059 | 📉 agota (-0.12) | +18.77$ | 0.59$ | ✅ activa |
| ORDER_FLOW_5M | 1630 | 51.3% | +0.013 | ➡️ estable | +14.21$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 47 | 83.0% | +0.316 | 📈 madura (+0.09) | +12.81$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 116 | 81.9% | +0.314 | ➡️ estable | +5.66$ | 2.00$ | ✅ activa |
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
| 2026-07-18T14:02 | GBM_LATE_5M#BTC#5min | Bitcoin Up or Down - July 18, 9:55AM-10:00AM ET… | ✅ WIN | +0.06$ |
| 2026-07-18T14:02 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 18, 9:50AM-9:55AM ET… | ❌ LOSS | -1.37$ |
| 2026-07-18T14:00 | GBM_LATE_5M#SOL#5min | Solana Up or Down - July 18, 9:55AM-10:00AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-18T14:00 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 18, 9:45AM-10:00AM ET… | ✅ WIN | +2.84$ |
| 2026-07-18T14:00 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 18, 9:45AM-10:00AM ET… | ✅ WIN | +2.67$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-18T14:02 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,086.56 | 0.1min |  |
| ✅ ETH | $1,840.14 | 0.1min |  |
| ✅ SOL | $74.69 | 0.1min |  |
| ✅ XRP | $1.08 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,086.56 | consenso |  |
| ETH | $1,840.14 | consenso |  |
| SOL | $74.69 | consenso |  |
| XRP | $1.08 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*