# Estado del bot — 2026-07-10 03:32 UTC

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
| P&L fiel (stake fijo 1$) | +621.94 $ |
| P&L sim compuesto | 🟢 +962.19 $ (ficción Kelly: +3782% s/ operativo) |
| P&L sim hoy (2026-07-10) | 🟢 +50.26 $ |
| Operaciones resueltas | 7094 (3838 WIN / 3256 LOSS) — 54.1% |
| Señales abiertas | 165 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2727 | 61.4% | +0.114 | ➡️ estable | +904.09$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 221 | 65.2% | +0.150 | ➡️ estable | +66.63$ | 1.50$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 275 | 53.5% | +0.034 | 📈 madura (+0.06) | +23.93$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1565 | 51.3% | +0.013 | ➡️ estable | +16.86$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 111 | 58.6% | +0.084 | 📈 madura (+0.04) | +10.35$ | 0.84$ | ✅ activa |
| LATE_WINDOW_5MIN | 34 | 70.6% | +0.194 | 📉 agota (-0.11) | +9.39$ | 1.94$ | ✅ activa |
| GBM_LATE_60M | 205 | 37.1% | -0.128 | 📈 madura (+0.07) | +4.73$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM | 1204 | 48.5% | -0.015 | ➡️ estable | -0.60$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 13 | 46.2% | -0.022 | — | -0.64$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 132 | 34.1% | -0.157 | 📉 agota (-0.10) | -0.77$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 159 | 55.3% | +0.053 | 📈 madura (+0.14) | -15.64$ | 0.53$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-10T03:32 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 9, 11:15PM-11:30PM ET… | ✅ WIN | +1.82$ |
| 2026-07-10T03:32 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 9, 11:15PM-11:30PM ET… | ✅ WIN | +0.51$ |
| 2026-07-10T03:32 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 9, 11:15PM-11:30PM ET… | ✅ WIN | +0.58$ |
| 2026-07-10T03:32 | UPDOWN_GBM#ETH#15min | Ethereum Up or Down - July 9, 11:15PM-11:30PM ET… | ✅ WIN | +1.08$ |
| 2026-07-10T03:26 | ORDER_FLOW_5M#SOL#5min | Solana Up or Down - July 9, 11:15PM-11:20PM ET… | ❌ LOSS | -1.57$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-10T03:32 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,808.00 | 0.0min |  |
| ✅ ETH | $1,769.23 | 0.0min |  |
| ✅ SOL | $78.79 | 0.0min |  |
| ✅ XRP | $1.11 | 0.0min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,808.00 | consenso |  |
| ETH | $1,769.23 | consenso |  |
| SOL | $78.78 | consenso |  |
| XRP | $1.10 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*