# Estado del bot — 2026-07-12 17:52 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **14.13 $** |
| P&L real total | 🔴 **-11.31 $** |
| P&L real hoy | -3.85 $ |
| P&L real 7 días | +6.15 $ |
| Fees pagados (real) | 7.67 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1291.51 $ |
| P&L sim compuesto | 🟢 +2099.51 $ (ficción Kelly: +8253% s/ operativo) |
| P&L sim hoy (2026-07-12) | 🟢 +494.80 $ |
| Operaciones resueltas | 11235 (6425 WIN / 4810 LOSS) — 57.2% |
| Señales abiertas | 144 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3650 | 61.3% | +0.113 | ➡️ estable | +1211.71$ | 1.13$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1003 | 66.4% | +0.164 | ➡️ estable | +565.16$ | 1.64$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1156 | 58.1% | +0.081 | ➡️ estable | +285.82$ | 0.81$ | ✅ activa |
| UPDOWN_GBM | 1333 | 49.4% | -0.006 | 📈 madura (+0.06) | +25.21$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_15M | 154 | 62.3% | +0.122 | 📈 madura (+0.18) | +24.62$ | 1.22$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 69 | 63.8% | +0.134 | 📈 madura (+0.04) | +21.47$ | 1.34$ | ✅ activa |
| ORDER_FLOW_5M | 1585 | 51.3% | +0.013 | ➡️ estable | +16.99$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO | 979 | 68.3% | +0.183 | 📈 madura (+0.07) | +11.98$ | 1.83$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 313 | 38.7% | -0.113 | ➡️ estable | +7.56$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM | 138 | 34.8% | -0.150 | 📉 agota (-0.11) | +0.19$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 163 | 46.0% | -0.039 | 📉 agota (-0.04) | -10.45$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 204 | 57.4% | +0.073 | 📈 madura (+0.24) | -13.93$ | 0.73$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-12T17:52 | ORDER_FLOW_5M#ETH#5min | Ethereum Up or Down - July 12, 1:45PM-1:50PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-12T17:52 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 12, 1:45PM-1:50PM ET… | ✅ WIN | +1.04$ |
| 2026-07-12T17:52 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 12, 1:30PM-1:45PM ET… | ✅ WIN | +1.16$ |
| 2026-07-12T17:45 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 12, 1:30PM-1:45PM ET… | ✅ WIN | +1.92$ |
| 2026-07-12T17:45 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 12, 1:30PM-1:45PM ET… | ✅ WIN | +0.72$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-12T17:51 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,109.42 | 0.1min |  |
| ✅ ETH | $1,820.08 | 0.1min |  |
| ✅ SOL | $77.41 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,109.60 | consenso |  |
| ETH | $1,820.08 | consenso |  |
| SOL | $77.48 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*