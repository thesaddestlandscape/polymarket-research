# Estado del bot — 2026-07-11 19:41 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **21.30 $** |
| P&L real total | 🔴 **-4.14 $** |
| P&L real hoy | -4.00 $ |
| P&L real 7 días | +13.32 $ |
| Fees pagados (real) | 7.48 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +976.06 $ |
| P&L sim compuesto | 🟢 +1520.86 $ (ficción Kelly: +5978% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +241.45 $ |
| Operaciones resueltas | 9675 (5423 WIN / 4252 LOSS) — 56.1% |
| Señales abiertas | 184 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3331 | 61.1% | +0.111 | ➡️ estable | +1052.75$ | 1.11$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 716 | 64.2% | +0.142 | 📉 agota (-0.03) | +303.56$ | 1.42$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 874 | 57.4% | +0.074 | ➡️ estable | +179.08$ | 0.74$ | ✅ activa |
| STREAK_FADE_15M | 131 | 61.8% | +0.117 | 📈 madura (+0.12) | +19.89$ | 1.17$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 53 | 66.0% | +0.155 | 📈 madura (+0.15) | +19.18$ | 1.54$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 292 | 39.0% | -0.109 | 📈 madura (+0.05) | +10.33$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 1281 | 48.9% | -0.011 | 📈 madura (+0.03) | +9.23$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| STREAK_FADE_5M | 27 | 55.6% | +0.052 | — | +1.22$ | 0.52$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 136 | 34.6% | -0.152 | 📉 agota (-0.13) | -0.14$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 192 | 57.8% | +0.077 | 📈 madura (+0.23) | -13.59$ | 0.77$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 583 | 65.9% | +0.158 | 📉 agota (-0.06) | -31.33$ | 1.58$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T19:32 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 11, 3:15PM-3:30PM ET… | ❌ LOSS | -0.97$ |
| 2026-07-11T19:32 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 11, 3:15PM-3:30PM ET… | ❌ LOSS | -0.96$ |
| 2026-07-11T19:32 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 11, 3:15PM-3:30PM ET… | ✅ WIN | +1.92$ |
| 2026-07-11T19:32 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 11, 3:15PM-3:30PM ET… | ✅ WIN | +0.77$ |
| 2026-07-11T19:32 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 11, 3:15PM-3:30PM ET… | ✅ WIN | +1.92$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T19:40 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,199.44 | 0.1min |  |
| ✅ ETH | $1,818.69 | 0.1min |  |
| ✅ SOL | $77.99 | 0.1min |  |
| ✅ XRP | $1.12 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,199.44 | consenso |  |
| ETH | $1,818.71 | consenso |  |
| SOL | $77.88 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*