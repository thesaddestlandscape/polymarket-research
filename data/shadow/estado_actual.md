# Estado del bot — 2026-07-10 04:26 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **31.38 $** |
| P&L real total | 🟢 **+5.94 $** |
| P&L real hoy | -1.09 $ |
| P&L real 7 días | +7.17 $ |
| Fees pagados (real) | 6.95 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +643.64 $ |
| P&L sim compuesto | 🟢 +983.30 $ (ficción Kelly: +3865% s/ operativo) |
| P&L sim hoy (2026-07-10) | 🟢 +71.37 $ |
| Operaciones resueltas | 7139 (3870 WIN / 3269 LOSS) — 54.2% |
| Señales abiertas | 168 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2742 | 61.5% | +0.115 | 📈 madura (+0.03) | +911.19$ | 1.15$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 229 | 65.5% | +0.154 | ➡️ estable | +72.20$ | 1.54$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 290 | 54.5% | +0.045 | 📈 madura (+0.11) | +28.77$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1568 | 51.3% | +0.013 | ➡️ estable | +16.61$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 111 | 58.6% | +0.084 | 📈 madura (+0.04) | +10.35$ | 0.84$ | ✅ activa |
| LATE_WINDOW_5MIN | 34 | 70.6% | +0.194 | 📉 agota (-0.11) | +9.39$ | 1.94$ | ✅ activa |
| GBM_LATE_60M | 208 | 37.5% | -0.124 | 📈 madura (+0.08) | +8.10$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| LEADLAG_BTC_XRP_15M | 14 | 50.0% | +0.000 | — | -0.16$ | 0.50$ | ✅ activa |
| UPDOWN_GBM | 1204 | 48.5% | -0.015 | ➡️ estable | -0.60$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 132 | 34.1% | -0.157 | 📉 agota (-0.10) | -0.77$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 159 | 55.3% | +0.053 | 📈 madura (+0.14) | -15.64$ | 0.53$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-10T04:21 | ORDER_FLOW_5M#SOL#5min | Solana Up or Down - July 10, 12:15AM-12:20AM ET… | ❌ LOSS | -0.61$ |
| 2026-07-10T04:20 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 10, 12:00AM-12:15AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-10T04:20 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 10, 12:00AM-12:15AM ET… | ✅ WIN | +1.76$ |
| 2026-07-10T04:18 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 10, 12:00AM-12:15AM ET… | ✅ WIN | +1.39$ |
| 2026-07-10T04:18 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 10, 12:00AM-12:15AM ET… | ✅ WIN | +0.32$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-10T04:26 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,911.25 | 0.1min |  |
| ✅ ETH | $1,774.88 | 0.1min |  |
| ✅ SOL | $78.96 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,911.25 | consenso |  |
| ETH | $1,774.88 | consenso |  |
| SOL | $78.93 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*