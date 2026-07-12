# Estado del bot — 2026-07-12 12:45 UTC

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
| P&L fiel (stake fijo 1$) | +1216.44 $ |
| P&L sim compuesto | 🟢 +1940.01 $ (ficción Kelly: +7626% s/ operativo) |
| P&L sim hoy (2026-07-12) | 🟢 +335.30 $ |
| Operaciones resueltas | 10916 (6217 WIN / 4699 LOSS) — 57.0% |
| Señales abiertas | 145 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3578 | 61.3% | +0.113 | ➡️ estable | +1159.11$ | 1.13$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 940 | 66.1% | +0.160 | ➡️ estable | +491.07$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1111 | 58.0% | +0.080 | ➡️ estable | +260.74$ | 0.80$ | ✅ activa |
| UPDOWN_GBM | 1318 | 49.4% | -0.006 | 📈 madura (+0.05) | +28.92$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 66 | 62.1% | +0.118 | ➡️ estable | +18.50$ | 1.18$ | ✅ activa |
| STREAK_FADE_15M | 150 | 61.3% | +0.112 | 📈 madura (+0.18) | +17.60$ | 1.12$ | ✅ activa |
| ORDER_FLOW_5M | 1584 | 51.3% | +0.013 | ➡️ estable | +17.50$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO | 885 | 68.6% | +0.185 | 📈 madura (+0.05) | +13.89$ | 1.85$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 310 | 38.4% | -0.115 | ➡️ estable | +4.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 9 | 100.0% | +0.184 | — | +3.91$ | 1.84$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 136 | 34.6% | -0.152 | 📉 agota (-0.13) | -0.14$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 159 | 45.3% | -0.047 | 📉 agota (-0.08) | -11.64$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 192 | 57.8% | +0.077 | 📈 madura (+0.23) | -13.59$ | 0.77$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-12T12:37 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 12, 8:15AM-8:30AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-12T12:37 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 12, 8:15AM-8:30AM ET… | ❌ LOSS | -1.83$ |
| 2026-07-12T12:37 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 12, 8:15AM-8:30AM ET… | ✅ WIN | +1.70$ |
| 2026-07-12T12:37 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 12, 8:15AM-8:30AM ET… | ✅ WIN | +1.82$ |
| 2026-07-12T12:32 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 12, 8:15AM-8:30AM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-12T12:44 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,983.76 | 0.1min |  |
| ✅ ETH | $1,804.82 | 0.1min |  |
| ✅ SOL | $77.17 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,978.58 | consenso |  |
| ETH | $1,804.78 | consenso |  |
| SOL | $77.09 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*