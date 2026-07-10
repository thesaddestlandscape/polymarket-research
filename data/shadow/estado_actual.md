# Estado del bot — 2026-07-10 07:04 UTC

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
| P&L fiel (stake fijo 1$) | +671.99 $ |
| P&L sim compuesto | 🟢 +1028.87 $ (ficción Kelly: +4044% s/ operativo) |
| P&L sim hoy (2026-07-10) | 🟢 +116.94 $ |
| Operaciones resueltas | 7271 (3953 WIN / 3318 LOSS) — 54.4% |
| Señales abiertas | 163 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2783 | 61.5% | +0.115 | 📈 madura (+0.03) | +921.85$ | 1.15$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 263 | 66.5% | +0.164 | 📈 madura (+0.03) | +95.71$ | 1.64$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 331 | 55.3% | +0.053 | 📈 madura (+0.13) | +41.21$ | 0.53$ | ✅ activa |
| ORDER_FLOW_5M | 1570 | 51.3% | +0.013 | ➡️ estable | +17.57$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 111 | 58.6% | +0.084 | 📈 madura (+0.04) | +10.35$ | 0.84$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 215 | 37.7% | -0.122 | 📈 madura (+0.10) | +7.12$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| LEADLAG_BTC_XRP_15M | 17 | 47.1% | -0.022 | — | -0.73$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 132 | 34.1% | -0.157 | 📉 agota (-0.10) | -0.77$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM | 1207 | 48.5% | -0.015 | ➡️ estable | -1.96$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 159 | 55.3% | +0.053 | 📈 madura (+0.14) | -15.64$ | 0.53$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-10T07:00 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 10, 2:45AM-3:00AM ET… | ✅ WIN | +1.08$ |
| 2026-07-10T07:00 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 10, 2:45AM-3:00AM ET… | ✅ WIN | +2.00$ |
| 2026-07-10T07:00 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 10, 2:45AM-3:00AM ET… | ✅ WIN | +1.78$ |
| 2026-07-10T07:00 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 10, 2:45AM-3:00AM ET… | ❌ LOSS | -0.56$ |
| 2026-07-10T07:00 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 10, 2:45AM-3:00AM ET… | ❌ LOSS | -1.59$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-10T07:04 UTC | rechazos 1h: 5 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,776.71 | 0.1min |  |
| ✅ ETH | $1,768.51 | 0.1min |  |
| ✅ SOL | $78.88 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,776.71 | consenso |  |
| ETH | $1,768.51 | consenso |  |
| SOL | $78.83 | consenso |  |
| XRP | $1.10 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:5 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*