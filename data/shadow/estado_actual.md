# Estado del bot — 2026-07-12 14:57 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **15.24 $** |
| P&L real total | 🔴 **-10.20 $** |
| P&L real hoy | -2.75 $ |
| P&L real 7 días | +7.26 $ |
| Fees pagados (real) | 7.61 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1250.31 $ |
| P&L sim compuesto | 🟢 +2016.14 $ (ficción Kelly: +7925% s/ operativo) |
| P&L sim hoy (2026-07-12) | 🟢 +411.43 $ |
| Operaciones resueltas | 11045 (6302 WIN / 4743 LOSS) — 57.1% |
| Señales abiertas | 151 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3607 | 61.4% | +0.113 | ➡️ estable | +1190.09$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 968 | 66.4% | +0.164 | ➡️ estable | +530.45$ | 1.64$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1131 | 58.1% | +0.081 | ➡️ estable | +274.36$ | 0.81$ | ✅ activa |
| UPDOWN_GBM | 1326 | 49.3% | -0.007 | 📈 madura (+0.05) | +25.79$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_15M | 154 | 62.3% | +0.122 | 📈 madura (+0.18) | +24.62$ | 1.22$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 66 | 62.1% | +0.118 | ➡️ estable | +18.50$ | 1.18$ | ✅ activa |
| ORDER_FLOW_5M | 1584 | 51.3% | +0.013 | ➡️ estable | +17.50$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 310 | 38.4% | -0.115 | ➡️ estable | +4.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 9 | 100.0% | +0.184 | — | +3.91$ | 1.84$ | ✅ activa |
| FAVORITO_CONFIRMADO | 923 | 68.0% | +0.180 | 📈 madura (+0.03) | +2.36$ | 1.80$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 136 | 34.6% | -0.152 | 📉 agota (-0.13) | -0.14$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 161 | 45.3% | -0.046 | 📉 agota (-0.07) | -11.84$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 192 | 57.8% | +0.077 | 📈 madura (+0.23) | -13.59$ | 0.77$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-12T14:50 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 12, 10:30AM-10:45AM ET… | ✅ WIN | +2.00$ |
| 2026-07-12T14:50 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 12, 10:30AM-10:45AM ET… | ❌ LOSS | -2.03$ |
| 2026-07-12T14:50 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 12, 10:30AM-10:45AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-12T14:50 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 12, 10:30AM-10:45AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-12T14:50 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 12, 10:30AM-10:45AM ET… | ✅ WIN | +2.00$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-12T14:56 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,171.01 | 0.1min |  |
| ✅ ETH | $1,818.18 | 0.1min |  |
| ✅ SOL | $77.58 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,175.50 | consenso |  |
| ETH | $1,818.79 | consenso |  |
| SOL | $77.53 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*