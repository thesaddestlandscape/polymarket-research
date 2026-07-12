# Estado del bot — 2026-07-12 11:00 UTC

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
| P&L fiel (stake fijo 1$) | +1191.35 $ |
| P&L sim compuesto | 🟢 +1892.80 $ (ficción Kelly: +7440% s/ operativo) |
| P&L sim hoy (2026-07-12) | 🟢 +288.09 $ |
| Operaciones resueltas | 10809 (6152 WIN / 4657 LOSS) — 56.9% |
| Señales abiertas | 142 |

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
| FAVORITO_CONFIRMADO | 853 | 68.6% | +0.185 | 📈 madura (+0.03) | +11.34$ | 1.85$ | ✅ activa |
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
| 2026-07-12T11:00 | FAVORITO_CONFIRMADO#ETH#60min | Ethereum Up or Down - July 12, 6AM ET… | ✅ WIN | +0.71$ |
| 2026-07-12T11:00 | FAVORITO_CONFIRMADO#BTC#60min | Bitcoin Up or Down - July 12, 6AM ET… | ✅ WIN | +1.06$ |
| 2026-07-12T10:56 | STREAK_FADE_5M#XRP#5min | XRP Up or Down - July 12, 6:50AM-6:55AM ET… | ✅ WIN | +0.67$ |
| 2026-07-12T10:51 | STREAK_FADE_5M#XRP#5min | XRP Up or Down - July 12, 6:45AM-6:50AM ET… | ❌ LOSS | -0.68$ |
| 2026-07-12T10:51 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 12, 6:30AM-6:45AM ET… | ✅ WIN | +1.54$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-12T10:59 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,832.85 | 0.1min |  |
| ✅ ETH | $1,798.33 | 0.1min |  |
| ✅ SOL | $76.71 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,832.85 | consenso |  |
| ETH | $1,798.33 | consenso |  |
| SOL | $76.68 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*