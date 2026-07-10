# Estado del bot — 2026-07-10 02:09 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **31.45 $** |
| P&L real total | 🟢 **+6.01 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | +8.26 $ |
| Fees pagados (real) | 6.95 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +590.25 $ |
| P&L sim compuesto | 🟢 +926.48 $ (ficción Kelly: +3642% s/ operativo) |
| P&L sim hoy (2026-07-10) | 🟢 +14.54 $ |
| Operaciones resueltas | 7033 (3794 WIN / 3239 LOSS) — 53.9% |
| Señales abiertas | 161 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2707 | 61.4% | +0.114 | ➡️ estable | +892.05$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 206 | 63.6% | +0.135 | 📉 agota (-0.07) | +49.16$ | 1.35$ | ✅ activa |
| ORDER_FLOW_5M | 1564 | 51.3% | +0.013 | ➡️ estable | +18.43$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 255 | 52.5% | +0.025 | 📈 madura (+0.07) | +18.34$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 111 | 58.6% | +0.084 | 📈 madura (+0.04) | +10.35$ | 0.84$ | ✅ activa |
| LATE_WINDOW_5MIN | 34 | 70.6% | +0.194 | 📉 agota (-0.11) | +9.39$ | 1.94$ | ✅ activa |
| GBM_LATE_60M | 202 | 36.6% | -0.132 | 📈 madura (+0.06) | +4.11$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 132 | 34.1% | -0.157 | 📉 agota (-0.10) | -0.77$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 12 | 41.7% | -0.043 | — | -1.12$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM | 1203 | 48.5% | -0.015 | ➡️ estable | -1.68$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 159 | 55.3% | +0.053 | 📈 madura (+0.14) | -15.64$ | 0.53$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-10T02:00 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 9, 9:45PM-10:00PM ET… | ✅ WIN | +0.26$ |
| 2026-07-10T02:00 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 9, 9:45PM-10:00PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-10T02:00 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 9, 9:45PM-10:00PM ET… | ✅ WIN | +0.15$ |
| 2026-07-10T02:00 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 9, 9:45PM-10:00PM ET… | ✅ WIN | +1.25$ |
| 2026-07-10T02:00 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 9, 9:45PM-10:00PM ET… | ❌ LOSS | -0.72$ |

## Calidad de datos

⚠️ **DEGRADED** — última verificación 2026-07-10T02:09 UTC | rechazos 1h: 11 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,697.08 | 0.0min |  |
| ✅ ETH | $1,763.85 | 0.0min |  |
| ✅ SOL | $78.92 | 0.0min |  |
| ✅ XRP | $1.10 | 0.0min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,704.70 | consenso |  |
| ETH | $1,764.17 | consenso |  |
| SOL | $78.84 | consenso |  |
| XRP | $1.10 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:11 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*