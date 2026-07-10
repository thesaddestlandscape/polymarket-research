# Estado del bot — 2026-07-10 03:38 UTC

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
| P&L fiel (stake fijo 1$) | +628.52 $ |
| P&L sim compuesto | 🟢 +970.10 $ (ficción Kelly: +3813% s/ operativo) |
| P&L sim hoy (2026-07-10) | 🟢 +58.16 $ |
| Operaciones resueltas | 7103 (3846 WIN / 3257 LOSS) — 54.1% |
| Señales abiertas | 166 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2730 | 61.5% | +0.115 | 📈 madura (+0.03) | +908.02$ | 1.15$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 223 | 65.0% | +0.149 | ➡️ estable | +66.22$ | 1.49$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 278 | 54.0% | +0.039 | 📈 madura (+0.09) | +26.54$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1566 | 51.3% | +0.013 | ➡️ estable | +18.63$ | 0.50$ | ✅ activa |
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
| 2026-07-10T03:38 | ORDER_FLOW_5M#BTC#5min | Bitcoin Up or Down - July 9, 11:30PM-11:35PM ET… | ✅ WIN | +1.77$ |
| 2026-07-10T03:36 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 9, 11:15PM-11:30PM ET… | ✅ WIN | +1.16$ |
| 2026-07-10T03:36 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 9, 11:15PM-11:30PM ET… | ✅ WIN | +0.48$ |
| 2026-07-10T03:36 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 9, 11:15PM-11:30PM ET… | ✅ WIN | +1.74$ |
| 2026-07-10T03:33 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 9, 11:15PM-11:30PM ET… | ❌ LOSS | -1.57$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-10T03:38 UTC | rechazos 1h: 4 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,825.64 | 0.0min |  |
| ✅ ETH | $1,770.74 | 0.0min |  |
| ✅ SOL | $78.96 | 0.0min |  |
| ✅ XRP | $1.11 | 0.0min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,825.64 | consenso |  |
| ETH | $1,770.74 | consenso |  |
| SOL | $78.87 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:4 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*