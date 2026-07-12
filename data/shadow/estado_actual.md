# Estado del bot — 2026-07-12 10:09 UTC

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
| P&L fiel (stake fijo 1$) | +1177.69 $ |
| P&L sim compuesto | 🟢 +1863.67 $ (ficción Kelly: +7326% s/ operativo) |
| P&L sim hoy (2026-07-12) | 🟢 +258.96 $ |
| Operaciones resueltas | 10762 (6118 WIN / 4644 LOSS) — 56.8% |
| Señales abiertas | 148 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3544 | 61.3% | +0.113 | ➡️ estable | +1150.79$ | 1.13$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 906 | 65.9% | +0.159 | ➡️ estable | +448.84$ | 1.59$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1086 | 58.0% | +0.080 | ➡️ estable | +247.78$ | 0.80$ | ✅ activa |
| UPDOWN_GBM | 1313 | 49.3% | -0.007 | 📈 madura (+0.05) | +21.70$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_15M | 149 | 61.7% | +0.116 | 📈 madura (+0.17) | +19.64$ | 1.16$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 63 | 61.9% | +0.115 | ➡️ estable | +18.14$ | 1.15$ | ✅ activa |
| ORDER_FLOW_5M | 1584 | 51.3% | +0.013 | ➡️ estable | +17.50$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO | 838 | 68.5% | +0.185 | ➡️ estable | +6.95$ | 1.84$ | ✅ activa |
| GBM_LATE_60M | 310 | 38.4% | -0.115 | ➡️ estable | +4.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 9 | 100.0% | +0.184 | — | +3.91$ | 1.84$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 136 | 34.6% | -0.152 | 📉 agota (-0.13) | -0.14$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 154 | 44.8% | -0.051 | 📉 agota (-0.09) | -11.98$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 192 | 57.8% | +0.077 | 📈 madura (+0.23) | -13.59$ | 0.77$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-12T10:06 | STREAK_FADE_5M#XRP#5min | XRP Up or Down - July 12, 6:00AM-6:05AM ET… | ❌ LOSS | -0.95$ |
| 2026-07-12T10:06 | FAVORITO_CONFIRMADO#SOL#60min | Solana Up or Down - July 12, 5AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-12T10:05 | GBM_LATE_60M#BTC#60min | Bitcoin Up or Down - July 12, 5AM ET… | ❌ LOSS | -1.64$ |
| 2026-07-12T10:05 | FAVORITO_CONFIRMADO#ETH#60min | Ethereum Up or Down - July 12, 5AM ET… | ✅ WIN | +0.94$ |
| 2026-07-12T10:05 | FAVORITO_CONFIRMADO#BTC#60min | Bitcoin Up or Down - July 12, 5AM ET… | ✅ WIN | +1.38$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-12T10:08 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,875.18 | 0.1min |  |
| ✅ ETH | $1,799.48 | 0.1min |  |
| ✅ SOL | $76.70 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,880.10 | consenso |  |
| ETH | $1,800.13 | consenso |  |
| SOL | $76.64 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*