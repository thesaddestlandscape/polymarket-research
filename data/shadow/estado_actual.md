# Estado del bot — 2026-07-10 21:19 UTC

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
| P&L fiel (stake fijo 1$) | +809.38 $ |
| P&L sim compuesto | 🟢 +1239.12 $ (ficción Kelly: +4871% s/ operativo) |
| P&L sim hoy (2026-07-10) | 🟢 +327.19 $ |
| Operaciones resueltas | 8156 (4518 WIN / 3638 LOSS) — 55.4% |
| Señales abiertas | 178 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3001 | 61.4% | +0.114 | ➡️ estable | +967.06$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 439 | 67.2% | +0.171 | 📈 madura (+0.05) | +192.07$ | 1.71$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 546 | 57.0% | +0.069 | 📈 madura (+0.08) | +95.42$ | 0.69$ | ✅ activa |
| ORDER_FLOW_5M | 1570 | 51.3% | +0.013 | ➡️ estable | +17.57$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 120 | 61.7% | +0.115 | 📈 madura (+0.13) | +17.48$ | 1.15$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 241 | 38.6% | -0.113 | 📈 madura (+0.09) | +9.37$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 29 | 62.1% | +0.113 | — | +3.69$ | 1.13$ | ✅ activa |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| FAVORITO_CONFIRMADO | 182 | 70.3% | +0.201 | 📉 agota (-0.11) | +2.82$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| UPDOWN_GBM | 1236 | 48.4% | -0.016 | ➡️ estable | -6.70$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-10T21:19 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 10, 5:00PM-5:15PM ET… | ❌ LOSS | -1.84$ |
| 2026-07-10T21:16 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 10, 5:00PM-5:15PM ET… | ✅ WIN | +0.89$ |
| 2026-07-10T21:16 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 10, 5:00PM-5:15PM ET… | ✅ WIN | +0.45$ |
| 2026-07-10T21:16 | UPDOWN_GBM#ETH#15min | Ethereum Up or Down - July 10, 5:00PM-5:15PM ET… | ✅ WIN | +0.34$ |
| 2026-07-10T21:16 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 10, 5:00PM-5:15PM ET… | ❌ LOSS | -0.55$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-10T21:19 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,921.62 | 0.1min |  |
| ✅ ETH | $1,791.61 | 0.1min |  |
| ✅ SOL | $77.95 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,924.01 | consenso |  |
| ETH | $1,791.58 | consenso |  |
| SOL | $77.88 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*