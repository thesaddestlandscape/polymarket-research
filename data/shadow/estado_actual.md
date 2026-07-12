# Estado del bot — 2026-07-12 11:37 UTC

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
| P&L fiel (stake fijo 1$) | +1184.95 $ |
| P&L sim compuesto | 🟢 +1880.89 $ (ficción Kelly: +7393% s/ operativo) |
| P&L sim hoy (2026-07-12) | 🟢 +276.18 $ |
| Operaciones resueltas | 10852 (6174 WIN / 4678 LOSS) — 56.9% |
| Señales abiertas | 145 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3562 | 61.3% | +0.113 | ➡️ estable | +1148.19$ | 1.12$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 926 | 65.9% | +0.158 | 📉 agota (-0.03) | +461.34$ | 1.58$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1101 | 57.9% | +0.079 | ➡️ estable | +247.77$ | 0.79$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 65 | 63.1% | +0.127 | ➡️ estable | +20.54$ | 1.27$ | ✅ activa |
| UPDOWN_GBM | 1314 | 49.2% | -0.008 | 📈 madura (+0.05) | +20.17$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_15M | 150 | 61.3% | +0.112 | 📈 madura (+0.18) | +17.60$ | 1.12$ | ✅ activa |
| ORDER_FLOW_5M | 1584 | 51.3% | +0.013 | ➡️ estable | +17.50$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO | 867 | 68.7% | +0.187 | 📈 madura (+0.04) | +15.71$ | 1.87$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 310 | 38.4% | -0.115 | ➡️ estable | +4.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 9 | 100.0% | +0.184 | — | +3.91$ | 1.84$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 136 | 34.6% | -0.152 | 📉 agota (-0.13) | -0.14$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 158 | 44.9% | -0.050 | 📉 agota (-0.09) | -12.25$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 192 | 57.8% | +0.077 | 📈 madura (+0.23) | -13.59$ | 0.77$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-12T11:31 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 12, 7:15AM-7:30AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-12T11:31 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 12, 7:20AM-7:25AM ET… | ✅ WIN | +0.46$ |
| 2026-07-12T11:31 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 12, 7:15AM-7:30AM ET… | ❌ LOSS | -1.95$ |
| 2026-07-12T11:31 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 12, 7:15AM-7:30AM ET… | ❌ LOSS | -1.60$ |
| 2026-07-12T11:31 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 12, 7:15AM-7:30AM ET… | ❌ LOSS | -2.02$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-12T11:36 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,880.29 | 0.1min |  |
| ✅ ETH | $1,800.60 | 0.1min |  |
| ✅ SOL | $76.99 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,899.90 | consenso |  |
| ETH | $1,800.60 | consenso |  |
| SOL | $76.84 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*