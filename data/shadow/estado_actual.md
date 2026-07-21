# Estado del bot — 2026-07-21 15:27 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **26.19 $** |
| P&L real total | 🔴 **-25.03 $** |
| P&L real hoy | -0.64 $ |
| P&L real 7 días | -9.89 $ |
| Fees pagados (real) | 8.78 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3299.81 $ |
| P&L sim compuesto | 🟢 +6250.45 $ (ficción Kelly: +24569% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -165.03 $ |
| Operaciones resueltas | 27009 (16246 WIN / 10763 LOSS) — 60.2% |
| Señales abiertas | 129 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6548 | 59.9% | +0.099 | ➡️ estable | +2109.55$ | 0.99$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3744 | 63.5% | +0.135 | 📉 agota (-0.04) | +2035.09$ | 1.35$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3715 | 58.7% | +0.087 | ➡️ estable | +1207.62$ | 0.87$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 996 | 67.0% | +0.169 | 📉 agota (-0.03) | +457.81$ | 1.69$ | ✅ activa |
| UPDOWN_GBM | 2065 | 52.7% | +0.027 | 📈 madura (+0.11) | +173.55$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 213 | 62.0% | +0.119 | 📉 agota (-0.04) | +100.10$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4660 | 68.6% | +0.186 | ➡️ estable | +77.40$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 256 | 58.2% | +0.081 | 📉 agota (-0.08) | +29.43$ | 0.81$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 104 | 79.8% | +0.292 | ➡️ estable | +20.82$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 254 | 50.4% | +0.004 | 📉 agota (-0.12) | +17.30$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 606 | 62.4% | +0.123 | 📉 agota (-0.05) | +14.23$ | 1.23$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 252 | 51.6% | +0.016 | 📉 agota (-0.14) | +11.88$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 223 | 81.6% | +0.313 | ➡️ estable | +11.47$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 215 | 49.8% | -0.002 | 📉 agota (-0.21) | +6.83$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 7 | 100.0% | +0.136 | — | +1.20$ | 1.36$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 8 | 50.0% | +0.000 | — | -0.26$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-21T15:23 | BALLENAS_CONFIRMADAS_15M#SOL#15min | Solana Up or Down - July 21, 11:00AM-11:15AM ET… | ✅ WIN | +0.65$ |
| 2026-07-21T15:23 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 21, 11:00AM-11:15AM ET… | ❌ LOSS | -1.96$ |
| 2026-07-21T15:23 | UPDOWN_GBM_15M_TARDIO#SOL#15min | Solana Up or Down - July 21, 11:00AM-11:15AM ET… | ✅ WIN | +0.19$ |
| 2026-07-21T15:23 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 21, 11:00AM-11:15AM ET… | ✅ WIN | +0.57$ |
| 2026-07-21T15:23 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 21, 11:00AM-11:15AM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T15:26 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,670.57 | 0.1min |  |
| ✅ ETH | $1,928.37 | 0.1min |  |
| ✅ SOL | $78.04 | 0.1min |  |
| ✅ XRP | $1.15 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,670.57 | consenso |  |
| ETH | $1,928.37 | consenso |  |
| SOL | $78.03 | consenso |  |
| XRP | $1.15 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*