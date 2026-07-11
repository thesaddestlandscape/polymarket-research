# Estado del bot — 2026-07-11 07:07 UTC

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
| P&L fiel (stake fijo 1$) | +914.64 $ |
| P&L sim compuesto | 🟢 +1405.18 $ (ficción Kelly: +5524% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +125.77 $ |
| Operaciones resueltas | 8813 (4921 WIN / 3892 LOSS) — 55.8% |
| Señales abiertas | 157 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3150 | 61.4% | +0.114 | ➡️ estable | +1027.68$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 558 | 66.1% | +0.161 | ➡️ estable | +259.61$ | 1.61$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 693 | 57.4% | +0.074 | 📈 madura (+0.04) | +142.37$ | 0.74$ | ✅ activa |
| STREAK_FADE_15M | 127 | 62.2% | +0.120 | 📈 madura (+0.13) | +20.22$ | 1.20$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 43 | 65.1% | +0.144 | 📈 madura (+0.23) | +10.37$ | 1.44$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 263 | 39.2% | -0.108 | 📈 madura (+0.11) | +10.26$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM | 1251 | 48.5% | -0.015 | ➡️ estable | -2.34$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 361 | 67.0% | +0.169 | 📉 agota (-0.06) | -20.36$ | 1.69$ | ✅ activa |
| STREAK_MOM_5M | 307 | 44.6% | -0.053 | 📉 agota (-0.05) | -22.65$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T07:06 | GBM_LATE_60M#BTC#60min | Bitcoin Up or Down - July 11, 2AM ET… | ✅ WIN | +0.14$ |
| 2026-07-11T07:06 | FAVORITO_CONFIRMADO#BTC#60min | Bitcoin Up or Down - July 11, 2AM ET… | ✅ WIN | +1.12$ |
| 2026-07-11T07:03 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 11, 2:45AM-3:00AM ET… | ✅ WIN | +4.98$ |
| 2026-07-11T07:03 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 11, 2:45AM-3:00AM ET… | ✅ WIN | +0.24$ |
| 2026-07-11T07:03 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 11, 2:45AM-3:00AM ET… | ❌ LOSS | -1.95$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T07:06 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,176.00 | 0.1min |  |
| ✅ ETH | $1,798.41 | 0.1min |  |
| ✅ SOL | $77.98 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,176.00 | consenso |  |
| ETH | $1,798.41 | consenso |  |
| SOL | $78.03 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*