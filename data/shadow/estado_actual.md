# Estado del bot — 2026-07-11 14:57 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **23.84 $** |
| P&L real total | 🔴 **-1.60 $** |
| P&L real hoy | -1.46 $ |
| P&L real 7 días | +15.85 $ |
| Fees pagados (real) | 7.30 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +970.67 $ |
| P&L sim compuesto | 🟢 +1496.65 $ (ficción Kelly: +5883% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +217.24 $ |
| Operaciones resueltas | 9316 (5219 WIN / 4097 LOSS) — 56.0% |
| Señales abiertas | 181 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3260 | 61.3% | +0.113 | ➡️ estable | +1061.25$ | 1.13$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 659 | 64.6% | +0.146 | ➡️ estable | +288.68$ | 1.46$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 803 | 58.2% | +0.081 | 📈 madura (+0.04) | +179.67$ | 0.81$ | ✅ activa |
| STREAK_FADE_15M | 131 | 61.8% | +0.117 | 📈 madura (+0.12) | +19.89$ | 1.17$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 49 | 63.3% | +0.127 | 📈 madura (+0.17) | +12.80$ | 1.27$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 281 | 39.1% | -0.108 | 📈 madura (+0.10) | +7.10$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM | 1268 | 48.7% | -0.013 | 📈 madura (+0.03) | +5.78$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 497 | 65.6% | +0.155 | ➡️ estable | -35.37$ | 1.55$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T14:50 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 11, 10:40AM-10:45AM ET… | ✅ WIN | +0.19$ |
| 2026-07-11T14:48 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 11, 10:30AM-10:45AM ET… | ❌ LOSS | -1.58$ |
| 2026-07-11T14:48 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 11, 10:30AM-10:45AM ET… | ❌ LOSS | -0.72$ |
| 2026-07-11T14:48 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 11, 10:30AM-10:45AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-11T14:48 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 11, 10:30AM-10:45AM ET… | ✅ WIN | +0.43$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T14:56 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,314.47 | 0.1min |  |
| ✅ ETH | $1,810.74 | 0.1min |  |
| ✅ SOL | $78.57 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,314.47 | consenso |  |
| ETH | $1,810.74 | consenso |  |
| SOL | $78.45 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*