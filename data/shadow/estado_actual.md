# Estado del bot — 2026-07-11 07:01 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **25.30 $** |
| P&L real total | 🔴 **-0.14 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | +17.32 $ |
| Fees pagados (real) | 7.27 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +909.42 $ |
| P&L sim compuesto | 🟢 +1398.84 $ (ficción Kelly: +5499% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +119.43 $ |
| Operaciones resueltas | 8795 (4909 WIN / 3886 LOSS) — 55.8% |
| Señales abiertas | 169 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3146 | 61.4% | +0.114 | ➡️ estable | +1027.40$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 555 | 65.9% | +0.159 | ➡️ estable | +252.54$ | 1.59$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 689 | 57.3% | +0.073 | 📈 madura (+0.03) | +140.22$ | 0.73$ | ✅ activa |
| STREAK_FADE_15M | 126 | 61.9% | +0.117 | 📈 madura (+0.12) | +19.78$ | 1.17$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 42 | 66.7% | +0.159 | 📈 madura (+0.26) | +11.49$ | 1.59$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 262 | 38.9% | -0.110 | 📈 madura (+0.11) | +10.13$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM | 1251 | 48.5% | -0.015 | ➡️ estable | -2.34$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 357 | 67.2% | +0.171 | 📉 agota (-0.05) | -17.74$ | 1.71$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 307 | 44.6% | -0.053 | 📉 agota (-0.05) | -22.65$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T07:00 | GBM_LATE_60M#SOL#60min | Solana Up or Down - July 11, 2AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-11T07:00 | FAVORITO_CONFIRMADO#SOL#60min | Solana Up or Down - July 11, 2AM ET… | ❌ LOSS | -1.51$ |
| 2026-07-11T06:56 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 11, 2:45AM-2:50AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-11T06:50 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 11, 2:40AM-2:45AM ET… | ✅ WIN | +0.64$ |
| 2026-07-11T06:48 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 11, 2:30AM-2:45AM ET… | ✅ WIN | +1.96$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T07:00 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,173.21 | 0.1min |  |
| ✅ ETH | $1,798.33 | 0.1min |  |
| ✅ SOL | $78.04 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,181.40 | consenso |  |
| ETH | $1,798.47 | consenso |  |
| SOL | $78.00 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*