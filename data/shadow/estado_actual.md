# Estado del bot — 2026-07-11 10:17 UTC

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
| P&L fiel (stake fijo 1$) | +932.09 $ |
| P&L sim compuesto | 🟢 +1437.19 $ (ficción Kelly: +5649% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +157.79 $ |
| Operaciones resueltas | 9023 (5045 WIN / 3978 LOSS) — 55.9% |
| Señales abiertas | 152 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3197 | 61.4% | +0.114 | ➡️ estable | +1041.68$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 598 | 65.1% | +0.150 | 📉 agota (-0.04) | +261.42$ | 1.50$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 740 | 57.8% | +0.078 | 📈 madura (+0.04) | +158.73$ | 0.78$ | ✅ activa |
| STREAK_FADE_15M | 128 | 62.5% | +0.123 | 📈 madura (+0.15) | +20.67$ | 1.23$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 46 | 63.0% | +0.125 | 📈 madura (+0.20) | +10.89$ | 1.25$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 272 | 39.3% | -0.106 | 📈 madura (+0.11) | +8.72$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM | 1255 | 48.4% | -0.016 | ➡️ estable | -2.42$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 419 | 67.1% | +0.170 | 📉 agota (-0.04) | -19.34$ | 1.70$ | ✅ activa |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T10:15 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 11, 6:00AM-6:15AM ET… | ✅ WIN | +1.92$ |
| 2026-07-11T10:15 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 11, 6:00AM-6:15AM ET… | ✅ WIN | +1.64$ |
| 2026-07-11T10:15 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 11, 6:00AM-6:15AM ET… | ✅ WIN | +1.06$ |
| 2026-07-11T10:15 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 11, 6:00AM-6:15AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-11T10:15 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 11, 6:00AM-6:15AM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T10:17 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,113.88 | 0.1min |  |
| ✅ ETH | $1,794.90 | 0.1min |  |
| ✅ SOL | $77.84 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,115.20 | consenso |  |
| ETH | $1,794.97 | consenso |  |
| SOL | $77.82 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*