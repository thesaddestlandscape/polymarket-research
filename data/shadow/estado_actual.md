# Estado del bot — 2026-07-12 00:43 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **17.99 $** |
| P&L real total | 🔴 **-7.45 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | +10.01 $ |
| Fees pagados (real) | 7.61 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1058.16 $ |
| P&L sim compuesto | 🟢 +1635.50 $ (ficción Kelly: +6429% s/ operativo) |
| P&L sim hoy (2026-07-12) | 🟢 +30.79 $ |
| Operaciones resueltas | 10045 (5658 WIN / 4387 LOSS) — 56.3% |
| Señales abiertas | 154 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3399 | 61.1% | +0.111 | ➡️ estable | +1083.99$ | 1.11$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 777 | 64.6% | +0.146 | 📉 agota (-0.05) | +347.66$ | 1.46$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 942 | 57.9% | +0.078 | ➡️ estable | +209.52$ | 0.78$ | ✅ activa |
| ORDER_FLOW_5M | 1578 | 51.4% | +0.014 | ➡️ estable | +20.07$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 138 | 60.9% | +0.107 | 📈 madura (+0.14) | +18.19$ | 1.07$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 57 | 63.2% | +0.127 | 📈 madura (+0.05) | +16.63$ | 1.27$ | ✅ activa |
| UPDOWN_GBM | 1296 | 49.2% | -0.008 | 📈 madura (+0.05) | +15.61$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 300 | 38.7% | -0.113 | 📈 madura (+0.04) | +9.21$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| STREAK_FADE_5M | 65 | 52.3% | +0.022 | ➡️ estable | +0.79$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 136 | 34.6% | -0.152 | 📉 agota (-0.13) | -0.14$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 192 | 57.8% | +0.077 | 📈 madura (+0.23) | -13.59$ | 0.77$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 680 | 66.3% | +0.163 | ➡️ estable | -25.61$ | 1.63$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-12T00:41 | STREAK_FADE_5M#SOL#5min | Solana Up or Down - July 11, 8:35PM-8:40PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-12T00:41 | ORDER_FLOW_5M#BNB#5min | BNB Up or Down - July 11, 8:30PM-8:35PM ET… | ✅ WIN | +1.34$ |
| 2026-07-12T00:36 | STREAK_FADE_5M#ETH#5min | Ethereum Up or Down - July 11, 8:25PM-8:30PM ET… | ✅ WIN | +0.50$ |
| 2026-07-12T00:35 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 11, 8:15PM-8:30PM ET… | ✅ WIN | +1.65$ |
| 2026-07-12T00:35 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 11, 8:15PM-8:30PM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-12T00:42 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,686.03 | 0.1min |  |
| ✅ ETH | $1,782.72 | 0.1min |  |
| ✅ SOL | $75.88 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,724.30 | consenso |  |
| ETH | $1,784.47 | consenso |  |
| SOL | $75.88 | consenso |  |
| XRP | $1.09 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*