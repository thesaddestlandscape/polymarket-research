# Estado del bot — 2026-07-12 13:12 UTC

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
| P&L fiel (stake fijo 1$) | +1222.59 $ |
| P&L sim compuesto | 🟢 +1956.04 $ (ficción Kelly: +7689% s/ operativo) |
| P&L sim hoy (2026-07-12) | 🟢 +351.33 $ |
| Operaciones resueltas | 10947 (6239 WIN / 4708 LOSS) — 57.0% |
| Señales abiertas | 147 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3584 | 61.3% | +0.113 | ➡️ estable | +1166.08$ | 1.13$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 946 | 66.1% | +0.160 | ➡️ estable | +493.87$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1115 | 58.0% | +0.080 | ➡️ estable | +265.43$ | 0.80$ | ✅ activa |
| UPDOWN_GBM | 1320 | 49.4% | -0.006 | 📈 madura (+0.05) | +28.66$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 66 | 62.1% | +0.118 | ➡️ estable | +18.50$ | 1.18$ | ✅ activa |
| STREAK_FADE_15M | 150 | 61.3% | +0.112 | 📈 madura (+0.18) | +17.60$ | 1.12$ | ✅ activa |
| ORDER_FLOW_5M | 1584 | 51.3% | +0.013 | ➡️ estable | +17.50$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO | 898 | 68.6% | +0.186 | 📈 madura (+0.04) | +15.72$ | 1.85$ | ✅ activa |
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
| 2026-07-12T13:07 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 12, 8:45AM-9:00AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-12T13:07 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 12, 8:45AM-9:00AM ET… | ✅ WIN | +1.01$ |
| 2026-07-12T13:07 | FAVORITO_CONFIRMADO#BTC#60min | Bitcoin Up or Down - July 12, 8AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-12T13:04 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 12, 8:45AM-9:00AM ET… | ✅ WIN | +1.70$ |
| 2026-07-12T13:04 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 12, 8:45AM-9:00AM ET… | ✅ WIN | +1.27$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-12T13:10 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,995.35 | 0.1min |  |
| ✅ ETH | $1,806.01 | 0.1min |  |
| ✅ SOL | $77.32 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,995.35 | consenso |  |
| ETH | $1,806.07 | consenso |  |
| SOL | $77.31 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*