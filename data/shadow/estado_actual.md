# Estado del bot — 2026-07-10 08:16 UTC

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
| P&L fiel (stake fijo 1$) | +684.29 $ |
| P&L sim compuesto | 🟢 +1039.46 $ (ficción Kelly: +4086% s/ operativo) |
| P&L sim hoy (2026-07-10) | 🟢 +127.53 $ |
| Operaciones resueltas | 7331 (3989 WIN / 3342 LOSS) — 54.4% |
| Señales abiertas | 155 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2802 | 61.3% | +0.113 | ➡️ estable | +914.33$ | 1.13$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 279 | 66.7% | +0.165 | ➡️ estable | +105.97$ | 1.66$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 348 | 55.7% | +0.057 | 📈 madura (+0.11) | +45.67$ | 0.57$ | ✅ activa |
| ORDER_FLOW_5M | 1570 | 51.3% | +0.013 | ➡️ estable | +17.57$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 112 | 58.9% | +0.088 | 📈 madura (+0.07) | +11.00$ | 0.88$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 218 | 38.1% | -0.118 | 📈 madura (+0.10) | +7.28$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| UPDOWN_GBM | 1210 | 48.5% | -0.015 | ➡️ estable | +0.09$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| LEADLAG_BTC_XRP_15M | 18 | 50.0% | +0.000 | — | -0.20$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 132 | 34.1% | -0.157 | 📉 agota (-0.10) | -0.77$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 159 | 55.3% | +0.053 | 📈 madura (+0.14) | -15.64$ | 0.53$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-10T08:16 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 10, 4:00AM-4:15AM ET… | ✅ WIN | +1.31$ |
| 2026-07-10T08:16 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 10, 4:00AM-4:15AM ET… | ✅ WIN | +1.52$ |
| 2026-07-10T08:16 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 10, 4:00AM-4:15AM ET… | ✅ WIN | +0.88$ |
| 2026-07-10T08:16 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 10, 4:00AM-4:15AM ET… | ✅ WIN | +0.99$ |
| 2026-07-10T08:16 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 10, 4:00AM-4:15AM ET… | ✅ WIN | +0.34$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-10T08:16 UTC | rechazos 1h: 4 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,992.00 | 0.0min |  |
| ✅ ETH | $1,774.77 | 0.0min |  |
| ✅ SOL | $78.91 | 0.0min |  |
| ✅ XRP | $1.11 | 0.0min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,026.20 | consenso |  |
| ETH | $1,776.33 | consenso |  |
| SOL | $78.98 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:4 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*