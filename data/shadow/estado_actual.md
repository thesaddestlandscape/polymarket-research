# Estado del bot — 2026-07-14 12:45 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **8.21 $** |
| P&L real total | 🔴 **-17.23 $** |
| P&L real hoy | -1.81 $ |
| P&L real 7 días | -7.29 $ |
| Fees pagados (real) | 8.15 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1564.33 $ |
| P&L sim compuesto | 🟢 +2704.15 $ (ficción Kelly: +10630% s/ operativo) |
| P&L sim hoy (2026-07-14) | 🟢 +149.94 $ |
| Operaciones resueltas | 13787 (7979 WIN / 5808 LOSS) — 57.9% |
| Señales abiertas | 69 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4252 | 60.4% | +0.104 | ➡️ estable | +1326.83$ | 1.04$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1555 | 65.4% | +0.154 | ➡️ estable | +931.59$ | 1.54$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1488 | 58.1% | +0.081 | ➡️ estable | +398.07$ | 0.81$ | ✅ activa |
| UPDOWN_GBM | 1468 | 50.6% | +0.006 | 📈 madura (+0.08) | +59.36$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 99 | 59.6% | +0.094 | 📉 agota (-0.07) | +27.72$ | 0.94$ | ✅ activa |
| STREAK_FADE_15M | 178 | 60.1% | +0.100 | 📈 madura (+0.12) | +18.42$ | 1.00$ | ✅ activa |
| LATE_WINDOW_5MIN | 39 | 71.8% | +0.207 | 📈 madura (+0.06) | +13.83$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1593 | 51.2% | +0.012 | ➡️ estable | +13.78$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 323 | 38.7% | -0.112 | ➡️ estable | +5.44$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 143 | 34.3% | -0.155 | 📉 agota (-0.13) | -1.21$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 219 | 59.4% | +0.093 | 📈 madura (+0.26) | -1.22$ | 0.93$ | ✅ activa |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 1731 | 68.1% | +0.181 | ➡️ estable | -6.38$ | 1.81$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-14T12:31 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 14, 8:15AM-8:30AM ET… | ❌ LOSS | -1.72$ |
| 2026-07-14T12:31 | UPDOWN_GBM#BTC#15min | Bitcoin Up or Down - July 14, 8:15AM-8:30AM ET… | ✅ WIN | +0.81$ |
| 2026-07-14T12:31 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 14, 8:15AM-8:30AM ET… | ✅ WIN | +0.65$ |
| 2026-07-14T12:31 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 14, 8:15AM-8:30AM ET… | ✅ WIN | +2.08$ |
| 2026-07-14T12:31 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 14, 8:15AM-8:30AM ET… | ✅ WIN | +0.97$ |

## Calidad de datos

⚠️ **DEGRADED** — última verificación 2026-07-14T12:44 UTC | rechazos 1h: 7 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,444.50 | 0.1min |  |
| ✅ ETH | $1,819.38 | 0.1min |  |
| ✅ SOL | $76.11 | 0.1min |  |
| ✅ XRP | $1.08 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,478.00 | consenso |  |
| ETH | $1,819.95 | consenso |  |
| SOL | $76.11 | consenso |  |
| XRP | $1.08 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:7 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*