# Estado del bot — 2026-07-10 14:54 UTC

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
| P&L fiel (stake fijo 1$) | +745.18 $ |
| P&L sim compuesto | 🟢 +1135.68 $ (ficción Kelly: +4464% s/ operativo) |
| P&L sim hoy (2026-07-10) | 🟢 +223.74 $ |
| Operaciones resueltas | 7714 (4238 WIN / 3476 LOSS) — 54.9% |
| Señales abiertas | 187 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2901 | 61.4% | +0.114 | ➡️ estable | +939.94$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 360 | 66.1% | +0.160 | 📈 madura (+0.03) | +142.37$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 447 | 56.8% | +0.068 | 📈 madura (+0.09) | +70.93$ | 0.68$ | ✅ activa |
| ORDER_FLOW_5M | 1570 | 51.3% | +0.013 | ➡️ estable | +17.57$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 116 | 60.3% | +0.102 | 📈 madura (+0.13) | +13.28$ | 1.02$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 230 | 38.3% | -0.116 | 📈 madura (+0.09) | +6.90$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| UPDOWN_GBM | 1217 | 48.7% | -0.013 | ➡️ estable | +3.05$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 73 | 72.6% | +0.220 | ➡️ estable | +2.04$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 26 | 57.7% | +0.071 | — | +1.86$ | 0.71$ | ✅ activa |
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
| 2026-07-10T14:51 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 10, 10:30AM-10:45AM ET… | ❌ LOSS | -1.04$ |
| 2026-07-10T14:51 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 10, 10:30AM-10:45AM ET… | ✅ WIN | +0.32$ |
| 2026-07-10T14:51 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 10, 10:30AM-10:45AM ET… | ✅ WIN | +0.10$ |
| 2026-07-10T14:51 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 10, 10:30AM-10:45AM ET… | ✅ WIN | +1.87$ |
| 2026-07-10T14:51 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 10, 10:30AM-10:45AM ET… | ✅ WIN | +1.14$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-10T14:53 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,950.92 | 0.1min |  |
| ✅ ETH | $1,785.29 | 0.1min |  |
| ✅ SOL | $77.96 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,959.30 | consenso |  |
| ETH | $1,785.32 | consenso |  |
| SOL | $78.04 | consenso |  |
| XRP | $1.10 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*