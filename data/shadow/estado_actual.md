# Estado del bot — 2026-07-10 14:42 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **26.01 $** |
| P&L real total | 🟢 **+0.57 $** |
| P&L real hoy | -5.44 $ |
| P&L real 7 días | +2.82 $ |
| Fees pagados (real) | 7.14 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +743.63 $ |
| P&L sim compuesto | 🟢 +1134.36 $ (ficción Kelly: +4459% s/ operativo) |
| P&L sim hoy (2026-07-10) | 🟢 +222.42 $ |
| Operaciones resueltas | 7695 (4227 WIN / 3468 LOSS) — 54.9% |
| Señales abiertas | 193 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2897 | 61.4% | +0.114 | ➡️ estable | +942.26$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 356 | 66.0% | +0.159 | 📈 madura (+0.04) | +137.54$ | 1.59$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 443 | 56.9% | +0.069 | 📈 madura (+0.08) | +71.45$ | 0.69$ | ✅ activa |
| ORDER_FLOW_5M | 1570 | 51.3% | +0.013 | ➡️ estable | +17.57$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 116 | 60.3% | +0.102 | 📈 madura (+0.13) | +13.28$ | 1.02$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 230 | 38.3% | -0.116 | 📈 madura (+0.09) | +6.90$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 68 | 75.0% | +0.243 | 📈 madura (+0.08) | +3.68$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| UPDOWN_GBM | 1216 | 48.7% | -0.013 | ➡️ estable | +2.55$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 25 | 56.0% | +0.056 | — | +1.38$ | 0.56$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 132 | 34.1% | -0.157 | 📉 agota (-0.10) | -0.77$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 159 | 55.3% | +0.053 | 📈 madura (+0.14) | -15.64$ | 0.53$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-10T14:41 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 10, 10:35AM-10:40AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-10T14:38 | FAVORITO_CONFIRMADO#BTC#5min | Bitcoin Up or Down - July 10, 10:30AM-10:35AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-10T14:37 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 10, 10:30AM-10:35AM ET… | ✅ WIN | +0.34$ |
| 2026-07-10T14:35 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 10, 10:15AM-10:30AM ET… | ❌ LOSS | -1.77$ |
| 2026-07-10T14:35 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 10, 10:15AM-10:30AM ET… | ✅ WIN | +0.31$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-10T14:41 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,029.77 | 0.1min |  |
| ✅ ETH | $1,784.82 | 0.1min |  |
| ✅ SOL | $77.53 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,029.77 | consenso |  |
| ETH | $1,785.14 | consenso |  |
| SOL | $77.53 | consenso |  |
| XRP | $1.10 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*