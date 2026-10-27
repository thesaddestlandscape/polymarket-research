# F7 — política de PRECIO DEL PAR (tope de la 2ª pata): INFORME (25-Oct ~10:55Z)

**Veredicto: REFUTADA (criterio PREREG_F7 no se cumple en ninguno de sus 4 puntos de éxito para la primaria P4).** Nada a real.

## Integridad
- Hashes de `datos/HASHES_PREREG.txt` verificados 25-Oct: PREREG_F7.md, scripts/f6_sim.py, f2_pares.py, f8_cohorte.py coinciden.
- La simulación ya la había completado el agente anterior (24-Oct 12:41-12:57Z, `scripts/f9_run.sh` + `f9b_run.sh` con ulimit 4,5 GB para 19-21): `datos/f6_sim_2026-10-{18..23}.csv.gz`, logs `datos/f6_log_*.txt`. No se ha re-simulado nada.
- `scripts/f10_eval.py` (12:39Z, anterior a los primeros resultados 12:41Z; no está en la lista de hashes) ejecutado hoy sin cambios → salida íntegra en `datos/f10_eval.txt`.
- Desenlace oficial (`maker_ms_desenlaces_cache.json` + `des_23.json`, etiquetas YES/NO 50/50). Rebate 20 % = 0,014·p(1−p)·acc. Fee de tomador no aplica (maker).

## Muestra
BTC 5m, libro5, 1/3 de mercados (`fin//300 %3==0`), ventana T(60,300], 6 días 18-23-Oct: 549 mercados válidos (70/96/95/96/96/96). Fills sim: B 8.725, P2 6.212, P4 5.976, P6 5.861.

## Resultados (EV(+reb)/€ ponderado por €)
| Var | pooled | media días | IC90 días (t, n=6) | bootstrap mercados IC90 | sin 2 mejores días | días + | sin rebate |
|---|---|---|---|---|---|---|---|
| B (control) | −0,0545 | −0,0522 | (−0,077, −0,028) | (−0,071, −0,040) | −0,067 | 1/6 | −0,060 |
| P2 | −0,0468 | −0,0485 | (−0,098, +0,001) | (−0,073, −0,019) | −0,085 | 2/6 | −0,054 |
| **P4 (primaria)** | **−0,0383** | −0,0407 | **(−0,080, −0,002)** | (−0,067, −0,010) | **−0,067** | 1/6 | −0,045 |
| P6 | −0,0529 | −0,0552 | (−0,085, −0,025) | (−0,083, −0,020) | −0,074 | 1/6 | −0,060 |

- P4 − B por día: +0,0115, IC90 (−0,034, +0,057), 4/6 días → no supera a B.
- Placebo (B remuestreado al coste por mercado de P4, 1000 sorteos): media −0,0515, IC90 (−0,063, −0,041); P4 queda fuera (p=0,026). Es decir, el tope SÍ mejora algo frente a "B más pequeño", pero sigue negativo.
- Criterio de éxito: EV>0 ✗ ; IC90 días inf>0 ✗ ; sin 2 mejores >0 ✗ ; >B con IC ✗ ; fuera de placebo ✓ (único que pasa).

## Por qué falla (descomposición por €)
| Var | lock AVG | lock FIFO | lock BEST | residuo suelta (AVG) | rebate | acc emparejadas | mercados con par |
|---|---|---|---|---|---|---|---|
| B | −0,038 | −0,037 | −0,015 | −0,022 | +0,006 | 0,77 | 548/549 |
| P4 | **+0,085** | +0,079 | +0,102 | **−0,130** | +0,007 | 0,67 | 438/549 |
| P6 | +0,097 | +0,093 | +0,113 | −0,157 | +0,007 | 0,65 | 424/549 |

El tope hace lo que promete (el par cerrado pasa de −3,8c a +8,5c por €), pero traslada la selección adversa a la pata suelta: la 2ª pata solo se rellena por debajo del tope cuando el mercado se mueve contra la 1ª, y cuando no se rellena queda una 1ª pata huérfana que es mayoritariamente la perdedora. Acierto por acción vs precio medio: B 0,496 vs 0,528 (−3,2 pp); P4 0,410 vs 0,430 (−2,0 pp); P6 0,397 vs 0,422 (−2,5 pp). Cuanto más margen (M), más lock y peor suelta: no hay M que cruce cero en esta rejilla. Mismo patrón que la trampa "pares con órdenes quietas: la pata suelta es casi siempre la perdedora".

## Limitaciones / qué falta
- 6 días, no ≥10 (requisito de misión): aun siendo positivo no habría bastado. n mercados (549) sí ≥40.
- Días 20-22 son los de construcción del sim v2 (contaminación declarada en el prereg; la política no se ajustó sobre ellos).
- Modelo de relleno del sim v2 algo optimista (trade-through rellena el resto completo; cola por proporción). El sesgo iría a favor de la política, no en contra: no rescata el veredicto.
- Rebate supuesto al 20 % de la comisión por acción rellenada (sin reparto del pool real).
- No reabrir por cambiar M (P2/P6 ya cubren la rejilla) ni por renombrado. Lo único distinto que queda en esta línea es atacar la SUELTA (salida/cobertura de la 1ª pata huérfana con señal ex-ante), que ya se tocó en X-SALIDA sin EV: cualquier reapertura exige mecanismo nuevo para predecir qué 1ª pata quedará huérfana.

Comando reproducible: `cd .../f7_precio_par && ulimit -v 3000000 && nice -n 19 ionice -c3 python3 scripts/f10_eval.py` (2 min).
