# Retrospectiva del proyecto — 2026-06-26

## Estado real del sistema

El bot lleva varias semanas en shadow mode con un pipeline completo funcionando. Esta retrospectiva documenta lo aprendido, lo que está calibrado, y lo que falta para el primer trade real.

---

## Análisis ya hecho (backfill 90d — Binance)

El análisis de validación masivo ya se ejecutó: **90 días × 6 pares = 125k predicciones GBM** usando klines de Binance. Esto calibró los parámetros principales antes de que siguiéramos acumulando shadow ops.

### Parámetros calibrados por backfill

```python
DRIFT_DAMPING = {5: 0.30, 15: 0.20, 60: 0.05, 240: 0.10}  # por ventana
REGIME_BUY_NO_THRESHOLD = 0.7   # solo 60min+, solo BUY_NO alcista
DELTA_MAX = 0.46                 # zona muerta ORDER_FLOW [0.46-0.65]
ORDER_FLOW_PAIR_BLACKLIST = {'ETH', 'BNB', 'XRP', 'DOGE'}  # IC negativo
ORDER_FLOW_BLACKLIST_HOURS = {2, 7, 9, 10, 11, 22}          # UTC, IC neg en BTC+SOL
```

### Hipótesis validadas por backfill

| Hipótesis | Resultado | Acción tomada |
|---|---|---|
| H-REGIMEN (filtro drift 15min) | ❌ REFUTADA — BUY_YES ≈ BUY_NO en 5/15min | Filtro eliminado en 15min, rediseñado solo para 60min+ BUY_NO |
| H-60MIN (GBM en ventanas 1h) | ✅ CONFIRMADA — IC positivo BTC+ETH | Acumulando shadow, ETA live dom-lun |
| H-ORDER_FLOW-DECAY (zona muerta) | ✅ RESUELTA — [0.46-0.65] IC=-0.079 | DELTA_MAX=0.46 implementado |
| ORDER_FLOW por par | ✅ — ETH/XRP/DOGE/BNB negativos | PAIR_BLACKLIST implementado |
| Rangos OF per-par | ✅ calibrado — BTC 0.42-0.44, SOL 0.36-0.40 | No aplicado aún (n<200 post-blacklist) |

### Estrategias descartadas por backfill (antes de más shadow ops)

| Estrategia | Motivo | Coste evitado |
|---|---|---|
| GBM #5min | No predecible — mercado revierte | El que tenemos (~-22€) habría sido mayor |
| GBM #240min | IC muy negativo en backfill | Desactivada tras n=11 (-5€) |
| ORDER_FLOW horas malas | IC negativo confirmado en 125k ops | +31€ retroactivo |

---

## Lo que el shadow ha añadido sobre el backfill

El backfill usa precios Binance pero no tiene acceso a las probabilidades reales de Polymarket. El shadow mode descubrió cosas que el backfill no ve:

| Hallazgo | Origen | Impacto |
|---|---|---|
| BUY_YES vs BUY_NO split #15min (IC +0.134 vs +0.016) | Shadow n=132 | Kelly overstaking BUY_YES → fix hoy |
| Kelly boost n=8 demasiado agresivo | Shadow (n=12 patrones) | Stakes a 2€ con IC=+0.016 → fix hoy |
| SMART_FLOW_1H sin señal real | Shadow n=17 | -8.95€ (no había backtest posible sin datos Polymarket) |
| OU_5M theta sin calibrar | Shadow n=57 | -13.76€ (requiere dataset Polymarket histórico) |
| Efecto horario ORDER_FLOW | Shadow n≈800 | +31€ retroactivo |

---

## Estado estrategias hoy (2026-06-26)

### Activas y en camino a live

| Estrategia | n | IC | Kelly/op | ETA live |
|---|---|---|---|---|
| **BUY_NO #15min (agg)** | **39** | **+0.134** | **1.34€** | **HOY — 1 op más** |
| ORDER_FLOW BTC+SOL | 269 filtrado | +0.058 | 0.50€ | ✅ activa |
| GBM ETH#60min | 18 | +0.090 | 0.90€ | Dom 28 Jun |
| GBM BTC#60min | 16 | +0.089 | 0.89€ | Lun 29 Jun |
| GBM SOL#15min | 30 | +0.062 | 0.62€ | Sáb 27 Jun |

### Señal débil / vigilancia

| Estrategia | n | IC | Estado |
|---|---|---|---|
| BUY_YES #15min (todos pares) | 93 | +0.005 | ⚠️ Ruido — stake mínimo (0.50€) |
| GBM SOL#60min | 9 | -0.021 | ⚠️ IC negativo con n pequeño |
| GBM XRP#15min | 9 | +0.021 | ⚠️ n insuficiente |

### Desactivadas

| Estrategia | IC final | n | PNL |
|---|---|---|---|
| UPDOWN_OU_5M | -0.229 | 57 | -13.76€ |
| SMART_FLOW_1H | -0.246 | 17 | -8.95€ |
| GBM #5min (todos pares) | ~-0.15 | ~80 | ~-22€ |
| GBM #240min | -0.318 | 11 | -5.04€ |

---

## Fixes aplicados en esta sesión (2026-06-26)

1. **N_BUCKET_MIN 8→15**: patrones causales requieren n≥15 — evita kelly_boost con muestras ruidosas
2. **Limpieza patrones_ganadores n<15**: BTC#15min (3→1 patrón), SOL#15min (1→0 patrones)
3. **Kelly por dirección**: postmortem calcula `apuesta_kelly_BUY_YES` y `apuesta_kelly_BUY_NO` por separado; shadow_predict aplica el específico tras determinar dirección
   - BTC#15min BUY_YES: 2.00€ → 0.50€
   - SOL#15min BUY_YES: 1.62€ → 0.50€
4. **Telegram horario**: shadow_resumen.py envía resumen cada 60 min + `/update` forzado
5. **Ventana live 15:00-16:00 Madrid** (UTC 13h): OF IC=+0.112 n=17 añadida
6. **UTC 20 revertido de blacklist**: el IC=-0.095 era de pares ya excluidos; BTC+SOL IC=+0.000

---

## Un bloqueante real — Polymarket API

Todo lo anterior está listo para operar. El único bloqueante para el primer trade real:

```
MetaMask → red Polygon → 30 USDC → cuenta Polymarket (VPS Helsinki)
Ver LIVE_PLAN.md para checklist completo.
```

Con BUY_NO #15min a 1 operación del umbral live (IC=+0.134, n=39/40), el bot está técnicamente listo. Solo falta la credencial.

---

## Para qué sirve Jon-Becker (en el futuro)

Jon-Becker (`s3.jbecker.dev/data.tar.zst`, 36GB) ya fue analizado online. **No es un bloqueante actual** — es para estrategias que aún no hemos implementado:

- **OU_5M con theta calibrado** (ahora desactivada, requiere datos de Polymarket histórico)
- **OBI — Orderbook Imbalance** (nueva estrategia, requiere book histórico)
- **Cross-Market Arb Polymarket vs Kalshi** (requiere precios Kalshi histórico)
- **Rangos OF per-par validados** (BTC 0.42-0.44 calibrado en backfill — validar cuando n≥200 post-blacklist)

El backfill de Binance ya resolvió lo que necesitábamos para GBM y ORDER_FLOW. Jon-Becker es el siguiente nivel, no el paso inmediato.
