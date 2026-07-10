# Estado del bot — 2026-07-10 06:34 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **27.10 $** |
| P&L real total | 🟢 **+1.66 $** |
| P&L real hoy | -4.36 $ |
| P&L real 7 días | +3.91 $ |
| Fees pagados (real) | 7.11 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +685.34 $ |
| P&L sim compuesto | 🟢 +1042.89 $ (ficción Kelly: +4099% s/ operativo) |
| P&L sim hoy (2026-07-10) | 🟢 +130.95 $ |
| Operaciones resueltas | 7252 (3950 WIN / 3302 LOSS) — 54.5% |
| Señales abiertas | 160 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2777 | 61.6% | +0.116 | ➡️ estable | +927.00$ | 1.16$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 259 | 67.2% | +0.170 | 📈 madura (+0.06) | +99.77$ | 1.71$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 325 | 56.0% | +0.060 | 📈 madura (+0.15) | +43.64$ | 0.60$ | ✅ activa |
| ORDER_FLOW_5M | 1570 | 51.3% | +0.013 | ➡️ estable | +17.57$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 111 | 58.6% | +0.084 | 📈 madura (+0.04) | +10.35$ | 0.84$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 214 | 37.9% | -0.120 | 📈 madura (+0.10) | +7.63$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| LEADLAG_BTC_XRP_15M | 16 | 50.0% | +0.000 | — | -0.17$ | 0.50$ | ✅ activa |
| UPDOWN_GBM | 1206 | 48.5% | -0.015 | ➡️ estable | -0.67$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 132 | 34.1% | -0.157 | 📉 agota (-0.10) | -0.77$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 159 | 55.3% | +0.053 | 📈 madura (+0.14) | -15.64$ | 0.53$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-10T06:30 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 10, 2:15AM-2:30AM ET… | ✅ WIN | +0.48$ |
| 2026-07-10T06:30 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 10, 2:15AM-2:30AM ET… | ✅ WIN | +0.48$ |
| 2026-07-10T06:30 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 10, 2:15AM-2:30AM ET… | ✅ WIN | +1.81$ |
| 2026-07-10T06:30 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 10, 2:15AM-2:30AM ET… | ✅ WIN | +0.78$ |
| 2026-07-10T06:30 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 10, 2:15AM-2:30AM ET… | ✅ WIN | +1.20$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-10T06:33 UTC | rechazos 1h: 5 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,862.11 | 0.0min |  |
| ✅ ETH | $1,769.49 | 0.0min |  |
| ✅ SOL | $79.02 | 0.0min |  |
| ✅ XRP | $1.11 | 0.0min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,862.11 | consenso |  |
| ETH | $1,769.61 | consenso |  |
| SOL | $78.90 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:5 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*