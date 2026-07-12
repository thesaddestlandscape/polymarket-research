# Estado del bot — 2026-07-12 17:15 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **14.13 $** |
| P&L real total | 🔴 **-11.31 $** |
| P&L real hoy | -3.85 $ |
| P&L real 7 días | +6.15 $ |
| Fees pagados (real) | 7.67 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1278.83 $ |
| P&L sim compuesto | 🟢 +2083.08 $ (ficción Kelly: +8188% s/ operativo) |
| P&L sim hoy (2026-07-12) | 🟢 +478.37 $ |
| Operaciones resueltas | 11193 (6395 WIN / 4798 LOSS) — 57.1% |
| Señales abiertas | 146 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3640 | 61.3% | +0.113 | ➡️ estable | +1211.14$ | 1.13$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 995 | 66.3% | +0.163 | ➡️ estable | +558.40$ | 1.63$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1148 | 58.0% | +0.080 | ➡️ estable | +281.52$ | 0.80$ | ✅ activa |
| UPDOWN_GBM | 1331 | 49.4% | -0.006 | 📈 madura (+0.06) | +25.76$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_15M | 154 | 62.3% | +0.122 | 📈 madura (+0.18) | +24.62$ | 1.22$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 68 | 63.2% | +0.129 | ➡️ estable | +20.94$ | 1.29$ | ✅ activa |
| ORDER_FLOW_5M | 1584 | 51.3% | +0.013 | ➡️ estable | +17.50$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO | 969 | 68.2% | +0.182 | 📈 madura (+0.06) | +8.04$ | 1.81$ | ✅ activa |
| GBM_LATE_60M | 313 | 38.7% | -0.113 | ➡️ estable | +7.56$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM | 138 | 34.8% | -0.150 | 📉 agota (-0.11) | +0.19$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 161 | 45.3% | -0.046 | 📉 agota (-0.07) | -11.84$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 204 | 57.4% | +0.073 | 📈 madura (+0.24) | -13.93$ | 0.73$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-12T17:15 | UPDOWN_GBM#BTC#15min | Bitcoin Up or Down - July 12, 1:00PM-1:15PM ET… | ❌ LOSS | -1.78$ |
| 2026-07-12T17:15 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 12, 1:00PM-1:15PM ET… | ✅ WIN | +0.80$ |
| 2026-07-12T17:15 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 12, 1:00PM-1:15PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-12T17:08 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 12, 12:45PM-1:00PM ET… | ✅ WIN | +0.54$ |
| 2026-07-12T17:08 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 12, 12:45PM-1:00PM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-12T17:14 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,128.89 | 0.1min |  |
| ✅ ETH | $1,820.58 | 0.1min |  |
| ✅ SOL | $77.48 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,128.89 | consenso |  |
| ETH | $1,820.58 | consenso |  |
| SOL | $77.51 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*