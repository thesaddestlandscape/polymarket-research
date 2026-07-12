# Estado del bot — 2026-07-12 05:51 UTC

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
| P&L fiel (stake fijo 1$) | +1127.08 $ |
| P&L sim compuesto | 🟢 +1750.48 $ (ficción Kelly: +6881% s/ operativo) |
| P&L sim hoy (2026-07-12) | 🟢 +145.77 $ |
| Operaciones resueltas | 10451 (5922 WIN / 4529 LOSS) — 56.7% |
| Señales abiertas | 144 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3482 | 61.2% | +0.112 | ➡️ estable | +1111.00$ | 1.12$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 848 | 65.3% | +0.153 | 📉 agota (-0.03) | +394.49$ | 1.53$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1024 | 57.8% | +0.078 | ➡️ estable | +227.63$ | 0.78$ | ✅ activa |
| STREAK_FADE_15M | 149 | 61.7% | +0.116 | 📈 madura (+0.17) | +19.64$ | 1.16$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 63 | 61.9% | +0.115 | ➡️ estable | +18.14$ | 1.15$ | ✅ activa |
| ORDER_FLOW_5M | 1584 | 51.3% | +0.013 | ➡️ estable | +17.50$ | 0.50$ | ✅ activa |
| UPDOWN_GBM | 1302 | 49.2% | -0.008 | 📈 madura (+0.05) | +16.20$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 305 | 38.7% | -0.112 | ➡️ estable | +8.14$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 9 | 100.0% | +0.184 | — | +3.91$ | 1.84$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| FAVORITO_CONFIRMADO | 766 | 67.9% | +0.178 | ➡️ estable | -0.13$ | 1.78$ | ✅ activa |
| PRICE_TARGET_GBM | 136 | 34.6% | -0.152 | 📉 agota (-0.13) | -0.14$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 114 | 50.9% | +0.009 | ➡️ estable | -1.99$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 192 | 57.8% | +0.077 | 📈 madura (+0.23) | -13.59$ | 0.77$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-12T05:50 | STREAK_FADE_5M#XRP#5min | XRP Up or Down - July 12, 1:40AM-1:45AM ET… | ✅ WIN | +0.49$ |
| 2026-07-12T05:49 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 12, 1:30AM-1:45AM ET… | ❌ LOSS | -0.95$ |
| 2026-07-12T05:49 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 12, 1:30AM-1:45AM ET… | ✅ WIN | +1.92$ |
| 2026-07-12T05:49 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 12, 1:30AM-1:45AM ET… | ✅ WIN | +0.38$ |
| 2026-07-12T05:49 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 12, 1:30AM-1:45AM ET… | ✅ WIN | +0.76$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-12T05:50 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,945.00 | 0.1min |  |
| ✅ ETH | $1,803.73 | 0.1min |  |
| ✅ SOL | $76.51 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,945.00 | consenso |  |
| ETH | $1,803.93 | consenso |  |
| SOL | $76.46 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*