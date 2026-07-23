# Estado del bot — 2026-07-23 05:32 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **29.17 $** |
| P&L real total | 🔴 **-22.05 $** |
| P&L real hoy | -0.06 $ |
| P&L real 7 días | -0.97 $ |
| Fees pagados (real) | 9.72 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3602.44 $ |
| P&L sim compuesto | 🟢 +6803.53 $ (ficción Kelly: +26743% s/ operativo) |
| P&L sim hoy (2026-07-23) | 🟢 +91.67 $ |
| Operaciones resueltas | 30277 (18214 WIN / 12063 LOSS) — 60.2% |
| Señales abiertas | 153 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 7038 | 59.7% | +0.097 | 📉 agota (-0.03) | +2210.19$ | 0.97$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4236 | 62.8% | +0.128 | 📉 agota (-0.04) | +2182.00$ | 1.28$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4238 | 58.2% | +0.082 | ➡️ estable | +1297.98$ | 0.82$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1317 | 66.5% | +0.165 | ➡️ estable | +605.69$ | 1.65$ | ✅ activa |
| UPDOWN_GBM | 2285 | 53.0% | +0.030 | 📈 madura (+0.11) | +190.78$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 239 | 61.1% | +0.110 | 📉 agota (-0.07) | +110.98$ | 1.10$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5289 | 68.7% | +0.187 | ➡️ estable | +88.51$ | 1.87$ | ✅ activa |
| WEEKLY_PRICE | 336 | 68.2% | +0.180 | 📈 madura (+0.21) | +67.16$ | 1.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 823 | 62.9% | +0.129 | ➡️ estable | +37.38$ | 1.29$ | ✅ activa |
| STREAK_FADE_15M | 267 | 58.4% | +0.084 | 📉 agota (-0.08) | +32.81$ | 0.84$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 127 | 79.5% | +0.291 | 📈 madura (+0.03) | +24.00$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 280 | 81.8% | +0.316 | ➡️ estable | +14.03$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1659 | 51.2% | +0.012 | ➡️ estable | +11.80$ | 0.50$ | ✅ activa |
| GBM_LATE_5M | 313 | 48.6% | -0.014 | 📉 agota (-0.17) | +10.27$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 263 | 51.0% | +0.009 | 📉 agota (-0.17) | +9.67$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 336 | 38.7% | -0.112 | ➡️ estable | +4.40$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 21 | 85.7% | +0.326 | — | +0.90$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 11 | 45.5% | -0.021 | — | -0.76$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 331 | 45.6% | -0.044 | 📉 agota (-0.15) | -1.92$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 318 | 44.0% | -0.059 | 📉 agota (-0.09) | -25.84$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-23T05:24 | BALLENAS_TARDIAS#BTC#15min | … | ✅ WIN | +0.33$ |
| 2026-07-23T05:24 | BALLENAS_CONFIRMADAS_15M#SOL#15min | Solana Up or Down - July 23, 1:00AM-1:15AM ET… | ✅ WIN | +0.47$ |
| 2026-07-23T05:24 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 23, 1:00AM-1:15AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-23T05:24 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 23, 1:00AM-1:15AM ET… | ✅ WIN | +2.05$ |
| 2026-07-23T05:24 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 23, 1:00AM-1:15AM ET… | ✅ WIN | +2.22$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-23T05:30 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,624.21 | 0.1min |  |
| ✅ ETH | $1,920.98 | 0.1min |  |
| ✅ SOL | $77.70 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,624.21 | consenso |  |
| ETH | $1,921.11 | consenso |  |
| SOL | $77.50 | consenso |  |
| XRP | $1.13 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*