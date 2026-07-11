# Estado del bot — 2026-07-11 11:00 UTC

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
| P&L fiel (stake fijo 1$) | +936.81 $ |
| P&L sim compuesto | 🟢 +1443.98 $ (ficción Kelly: +5676% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +164.57 $ |
| Operaciones resueltas | 9051 (5060 WIN / 3991 LOSS) — 55.9% |
| Señales abiertas | 165 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3203 | 61.4% | +0.114 | ➡️ estable | +1042.16$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 604 | 65.1% | +0.150 | 📉 agota (-0.04) | +268.84$ | 1.50$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 746 | 57.8% | +0.078 | 📈 madura (+0.03) | +159.93$ | 0.78$ | ✅ activa |
| STREAK_FADE_15M | 128 | 62.5% | +0.123 | 📈 madura (+0.15) | +20.67$ | 1.23$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 47 | 61.7% | +0.112 | 📈 madura (+0.17) | +10.38$ | 1.12$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 273 | 39.2% | -0.107 | 📈 madura (+0.11) | +8.21$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM | 1255 | 48.4% | -0.016 | ➡️ estable | -2.42$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 427 | 67.0% | +0.169 | 📉 agota (-0.04) | -20.65$ | 1.69$ | ✅ activa |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T11:00 | GBM_LATE_60M#SOL#60min | Solana Up or Down - July 11, 6AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-11T11:00 | FAVORITO_CONFIRMADO#SOL#60min | Solana Up or Down - July 11, 6AM ET… | ✅ WIN | +0.64$ |
| 2026-07-11T11:00 | FAVORITO_CONFIRMADO#ETH#60min | Ethereum Up or Down - July 11, 6AM ET… | ✅ WIN | +1.18$ |
| 2026-07-11T10:51 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 11, 6:30AM-6:45AM ET… | ✅ WIN | +0.58$ |
| 2026-07-11T10:51 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 11, 6:30AM-6:45AM ET… | ✅ WIN | +0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T10:59 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,124.61 | 0.1min |  |
| ✅ ETH | $1,796.96 | 0.1min |  |
| ✅ SOL | $78.04 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,124.61 | consenso |  |
| ETH | $1,796.96 | consenso |  |
| SOL | $78.00 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*