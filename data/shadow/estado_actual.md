# Estado del bot — 2026-07-11 09:03 UTC

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
| P&L fiel (stake fijo 1$) | +938.82 $ |
| P&L sim compuesto | 🟢 +1434.97 $ (ficción Kelly: +5641% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +155.57 $ |
| Operaciones resueltas | 8934 (4999 WIN / 3935 LOSS) — 56.0% |
| Señales abiertas | 160 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3177 | 61.4% | +0.114 | ➡️ estable | +1034.32$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 578 | 65.9% | +0.159 | 📉 agota (-0.03) | +267.74$ | 1.59$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 720 | 58.1% | +0.080 | 📈 madura (+0.04) | +153.10$ | 0.80$ | ✅ activa |
| STREAK_FADE_15M | 127 | 62.2% | +0.120 | 📈 madura (+0.13) | +20.22$ | 1.20$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 268 | 39.6% | -0.104 | 📈 madura (+0.12) | +10.55$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 45 | 62.2% | +0.117 | 📈 madura (+0.14) | +8.93$ | 1.17$ | ✅ activa |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM | 1255 | 48.4% | -0.016 | ➡️ estable | -2.42$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 396 | 67.4% | +0.173 | 📉 agota (-0.04) | -14.31$ | 1.73$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T09:03 | GBM_LATE_60M#BTC#60min | Bitcoin Up or Down - July 11, 4AM ET… | ✅ WIN | +0.10$ |
| 2026-07-11T09:03 | FAVORITO_CONFIRMADO#BTC#60min | Bitcoin Up or Down - July 11, 4AM ET… | ✅ WIN | +0.42$ |
| 2026-07-11T09:01 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 11, 4:50AM-4:55AM ET… | ✅ WIN | +0.38$ |
| 2026-07-11T09:01 | GBM_LATE_60M#SOL#60min | Solana Up or Down - July 11, 4AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-11T09:01 | FAVORITO_CONFIRMADO#SOL#60min | Solana Up or Down - July 11, 4AM ET… | ✅ WIN | +0.44$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T09:02 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,207.29 | 0.1min |  |
| ✅ ETH | $1,800.05 | 0.1min |  |
| ✅ SOL | $78.24 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,213.90 | consenso |  |
| ETH | $1,800.05 | consenso |  |
| SOL | $78.10 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*