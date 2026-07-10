# Estado del bot — 2026-07-10 20:00 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **24.92 $** |
| P&L real total | 🔴 **-0.52 $** |
| P&L real hoy | -6.53 $ |
| P&L real 7 días | +1.73 $ |
| Fees pagados (real) | 7.19 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +784.02 $ |
| P&L sim compuesto | 🟢 +1209.55 $ (ficción Kelly: +4755% s/ operativo) |
| P&L sim hoy (2026-07-10) | 🟢 +297.61 $ |
| Operaciones resueltas | 8054 (4449 WIN / 3605 LOSS) — 55.2% |
| Señales abiertas | 188 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2978 | 61.4% | +0.114 | ➡️ estable | +962.37$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 423 | 67.1% | +0.171 | 📈 madura (+0.06) | +183.28$ | 1.71$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 524 | 56.7% | +0.067 | 📈 madura (+0.09) | +85.49$ | 0.67$ | ✅ activa |
| ORDER_FLOW_5M | 1570 | 51.3% | +0.013 | ➡️ estable | +17.57$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 118 | 61.0% | +0.108 | 📈 madura (+0.13) | +16.00$ | 1.08$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 238 | 38.2% | -0.117 | 📈 madura (+0.07) | +8.57$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 28 | 60.7% | +0.100 | — | +3.21$ | 1.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 151 | 69.5% | +0.193 | 📉 agota (-0.07) | -1.11$ | 1.93$ | ✅ activa |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| UPDOWN_GBM | 1232 | 48.4% | -0.016 | ➡️ estable | -6.18$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-10T19:46 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 10, 3:30PM-3:45PM ET… | ✅ WIN | +0.80$ |
| 2026-07-10T19:46 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 10, 3:30PM-3:45PM ET… | ✅ WIN | +1.77$ |
| 2026-07-10T19:46 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 10, 3:30PM-3:45PM ET… | ✅ WIN | +0.50$ |
| 2026-07-10T19:46 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 10, 3:30PM-3:45PM ET… | ✅ WIN | +0.36$ |
| 2026-07-10T19:46 | UPDOWN_GBM#BTC#15min | Bitcoin Up or Down - July 10, 3:30PM-3:45PM ET… | ✅ WIN | +1.22$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-10T19:59 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,893.15 | 0.1min |  |
| ✅ ETH | $1,791.37 | 0.1min |  |
| ✅ SOL | $77.95 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,893.15 | consenso |  |
| ETH | $1,791.50 | consenso |  |
| SOL | $77.95 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*