# Estado del bot — 2026-07-12 07:10 UTC

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
| P&L fiel (stake fijo 1$) | +1135.77 $ |
| P&L sim compuesto | 🟢 +1777.01 $ (ficción Kelly: +6985% s/ operativo) |
| P&L sim hoy (2026-07-12) | 🟢 +172.30 $ |
| Operaciones resueltas | 10555 (5979 WIN / 4576 LOSS) — 56.6% |
| Señales abiertas | 153 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3500 | 61.3% | +0.113 | ➡️ estable | +1122.32$ | 1.12$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 866 | 65.6% | +0.156 | ➡️ estable | +416.41$ | 1.55$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1042 | 58.0% | +0.080 | ➡️ estable | +236.59$ | 0.80$ | ✅ activa |
| STREAK_FADE_15M | 149 | 61.7% | +0.116 | 📈 madura (+0.17) | +19.64$ | 1.16$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 63 | 61.9% | +0.115 | ➡️ estable | +18.14$ | 1.15$ | ✅ activa |
| ORDER_FLOW_5M | 1584 | 51.3% | +0.013 | ➡️ estable | +17.50$ | 0.50$ | ✅ activa |
| UPDOWN_GBM | 1305 | 49.1% | -0.009 | 📈 madura (+0.05) | +15.68$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 308 | 38.3% | -0.116 | ➡️ estable | +6.35$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 9 | 100.0% | +0.184 | — | +3.91$ | 1.84$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 136 | 34.6% | -0.152 | 📉 agota (-0.13) | -0.14$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 788 | 67.8% | +0.177 | ➡️ estable | -4.89$ | 1.77$ | ✅ activa |
| STREAK_FADE_5M | 136 | 44.9% | -0.051 | 📉 agota (-0.16) | -10.58$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 192 | 57.8% | +0.077 | 📈 madura (+0.23) | -13.59$ | 0.77$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-12T07:09 | STREAK_FADE_5M#SOL#5min | Solana Up or Down - July 12, 3:00AM-3:05AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-12T07:09 | STREAK_FADE_5M#XRP#5min | XRP Up or Down - July 12, 3:00AM-3:05AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-12T07:08 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 12, 3:00AM-3:05AM ET… | ❌ LOSS | -0.88$ |
| 2026-07-12T07:08 | STREAK_FADE_5M#SOL#5min | Solana Up or Down - July 12, 2:55AM-3:00AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-12T07:06 | STREAK_FADE_5M#ETH#5min | Ethereum Up or Down - July 12, 2:55AM-3:00AM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-12T07:09 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,749.97 | 0.1min |  |
| ✅ ETH | $1,795.95 | 0.1min |  |
| ✅ SOL | $76.55 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,753.00 | consenso |  |
| ETH | $1,795.95 | consenso |  |
| SOL | $76.46 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*