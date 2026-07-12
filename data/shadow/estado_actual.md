# Estado del bot — 2026-07-12 10:55 UTC

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
| P&L fiel (stake fijo 1$) | +1189.50 $ |
| P&L sim compuesto | 🟢 +1890.36 $ (ficción Kelly: +7431% s/ operativo) |
| P&L sim hoy (2026-07-12) | 🟢 +285.65 $ |
| Operaciones resueltas | 10806 (6149 WIN / 4657 LOSS) — 56.9% |
| Señales abiertas | 144 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3553 | 61.3% | +0.113 | ➡️ estable | +1154.40$ | 1.13$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 916 | 66.0% | +0.160 | ➡️ estable | +461.68$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1094 | 58.1% | +0.081 | ➡️ estable | +254.42$ | 0.81$ | ✅ activa |
| UPDOWN_GBM | 1313 | 49.3% | -0.007 | 📈 madura (+0.05) | +21.70$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 64 | 62.5% | +0.121 | ➡️ estable | +20.06$ | 1.21$ | ✅ activa |
| STREAK_FADE_15M | 149 | 61.7% | +0.116 | 📈 madura (+0.17) | +19.64$ | 1.16$ | ✅ activa |
| ORDER_FLOW_5M | 1584 | 51.3% | +0.013 | ➡️ estable | +17.50$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO | 851 | 68.5% | +0.185 | 📈 madura (+0.03) | +9.56$ | 1.84$ | ✅ activa |
| GBM_LATE_60M | 310 | 38.4% | -0.115 | ➡️ estable | +4.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 9 | 100.0% | +0.184 | — | +3.91$ | 1.84$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 136 | 34.6% | -0.152 | 📉 agota (-0.13) | -0.14$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 157 | 44.6% | -0.053 | 📉 agota (-0.10) | -12.92$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 192 | 57.8% | +0.077 | 📈 madura (+0.23) | -13.59$ | 0.77$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-12T10:51 | STREAK_FADE_5M#XRP#5min | XRP Up or Down - July 12, 6:45AM-6:50AM ET… | ❌ LOSS | -0.68$ |
| 2026-07-12T10:51 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 12, 6:30AM-6:45AM ET… | ✅ WIN | +1.54$ |
| 2026-07-12T10:51 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 12, 6:30AM-6:45AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-12T10:51 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 12, 6:30AM-6:45AM ET… | ❌ LOSS | -1.99$ |
| 2026-07-12T10:51 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 12, 6:30AM-6:45AM ET… | ✅ WIN | +1.50$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-12T10:54 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,801.46 | 0.1min |  |
| ✅ ETH | $1,798.37 | 0.1min |  |
| ✅ SOL | $76.73 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,807.10 | consenso |  |
| ETH | $1,798.37 | consenso |  |
| SOL | $76.67 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*