# Estado del bot — 2026-07-11 12:26 UTC

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
| P&L fiel (stake fijo 1$) | +940.80 $ |
| P&L sim compuesto | 🟢 +1450.94 $ (ficción Kelly: +5703% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +171.53 $ |
| Operaciones resueltas | 9147 (5112 WIN / 4035 LOSS) — 55.9% |
| Señales abiertas | 166 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3223 | 61.3% | +0.113 | ➡️ estable | +1046.17$ | 1.13$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 622 | 64.8% | +0.147 | 📉 agota (-0.04) | +272.29$ | 1.47$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 766 | 57.6% | +0.076 | ➡️ estable | +162.34$ | 0.76$ | ✅ activa |
| STREAK_FADE_15M | 131 | 61.8% | +0.117 | 📈 madura (+0.12) | +19.89$ | 1.17$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 47 | 61.7% | +0.112 | 📈 madura (+0.17) | +10.38$ | 1.12$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 276 | 39.5% | -0.104 | 📈 madura (+0.12) | +9.15$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| UPDOWN_GBM | 1258 | 48.6% | -0.014 | 📈 madura (+0.03) | +1.30$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 456 | 66.2% | +0.162 | 📉 agota (-0.05) | -27.43$ | 1.62$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T12:23 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 11, 8:00AM-8:15AM ET… | ❌ LOSS | -1.96$ |
| 2026-07-11T12:23 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 11, 8:00AM-8:15AM ET… | ❌ LOSS | -1.74$ |
| 2026-07-11T12:23 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 11, 8:00AM-8:15AM ET… | ❌ LOSS | -0.69$ |
| 2026-07-11T12:23 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 11, 8:00AM-8:15AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-11T12:23 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 11, 8:00AM-8:15AM ET… | ✅ WIN | +1.44$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T12:25 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,125.89 | 0.1min |  |
| ✅ ETH | $1,797.49 | 0.1min |  |
| ✅ SOL | $78.05 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,129.80 | consenso |  |
| ETH | $1,797.53 | consenso |  |
| SOL | $77.98 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*