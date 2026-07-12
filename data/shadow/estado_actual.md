# Estado del bot — 2026-07-12 16:17 UTC

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
| P&L fiel (stake fijo 1$) | +1270.36 $ |
| P&L sim compuesto | 🟢 +2063.18 $ (ficción Kelly: +8110% s/ operativo) |
| P&L sim hoy (2026-07-12) | 🟢 +458.47 $ |
| Operaciones resueltas | 11142 (6362 WIN / 4780 LOSS) — 57.1% |
| Señales abiertas | 141 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3626 | 61.4% | +0.114 | ➡️ estable | +1211.95$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 984 | 66.4% | +0.163 | ➡️ estable | +549.27$ | 1.63$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1142 | 58.1% | +0.080 | ➡️ estable | +280.72$ | 0.80$ | ✅ activa |
| UPDOWN_GBM | 1329 | 49.4% | -0.006 | 📈 madura (+0.06) | +29.35$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_15M | 154 | 62.3% | +0.122 | 📈 madura (+0.18) | +24.62$ | 1.22$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 68 | 63.2% | +0.129 | ➡️ estable | +20.94$ | 1.29$ | ✅ activa |
| ORDER_FLOW_5M | 1584 | 51.3% | +0.013 | ➡️ estable | +17.50$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 312 | 38.5% | -0.115 | ➡️ estable | +4.15$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM | 138 | 34.8% | -0.150 | 📉 agota (-0.11) | +0.19$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| FAVORITO_CONFIRMADO | 952 | 67.9% | +0.178 | 📈 madura (+0.04) | -2.91$ | 1.78$ | ✅ activa |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 161 | 45.3% | -0.046 | 📉 agota (-0.07) | -11.84$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 204 | 57.4% | +0.073 | 📈 madura (+0.24) | -13.93$ | 0.73$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-12T16:06 | FAVORITO_CONFIRMADO#ETH#60min | Ethereum Up or Down - July 12, 11AM ET… | ✅ WIN | +1.50$ |
| 2026-07-12T16:06 | WEEKLY_PRICE#SOL | Will the price of Solana be between $70 and $80 on… | ❌ LOSS | -0.51$ |
| 2026-07-12T16:05 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 12, 11:45AM-12:00PM ET… | ✅ WIN | +8.92$ |
| 2026-07-12T16:05 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 12, 11:45AM-12:00PM ET… | ✅ WIN | +2.52$ |
| 2026-07-12T16:05 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 12, 11:45AM-12:00PM ET… | ✅ WIN | +7.66$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-12T16:16 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,013.04 | 0.1min |  |
| ✅ ETH | $1,816.73 | 0.1min |  |
| ✅ SOL | $77.49 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,016.60 | consenso |  |
| ETH | $1,817.41 | consenso |  |
| SOL | $77.43 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*