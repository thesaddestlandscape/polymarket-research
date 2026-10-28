# PLAYBOOK — de un problema a una fórmula que gane dinero (documento vivo)

Pedido de Javi 28-Oct: documentar cómo el sistema se organiza para encontrar/derivar la fórmula, de modo que se replique en otras estrategias. Se actualiza al cierre de cada ronda. Caso 0: salida/escalera de B (5m barato, todas las monedas).

## 0. Principios de organización (reglas del proceso)
1. **Un agente a la vez**, sonnet, tope de llamadas por ronda (≤20; iteraciones ≤8). Coste en tokens medido por ronda (campo `subagent_tokens`).
2. **Ciclo por tarea**: informe → revisión (¿es bug?) → iteración mínima → veredicto → solo entonces la siguiente. Una tarea no se abandona por un resultado positivo implausible: primero se audita (ej. terminal D +0,409 → +0,117 al añadir profundidad de bid).
3. **Cola priorizada** en el checkpoint de memoria (`project_checkpoint_27oct_noche_mandato_AS_prediccion`), con lo pendiente y lo guardado; la prioridad la fijan los resultados de la ronda anterior y el mandato de Javi.
4. **Cada ronda lee el informe anterior y no repite lo REJECTED** (lista de callejones cerrados en el checkpoint).
5. **Entorno**: `nice -n 19 ionice -c3`, `ulimit -v 3 GB`, load5 vigilado, nada en producción ni `data/live`, sin commits del agente.

## 1. Embudo (qué se hace, en orden)
| Paso | Qué | Salida |
|---|---|---|
| A. Síntoma medible | Cuantificar el fallo con EV ponderado por € (Σpnl/Σcoste), IC90 por días, OOS | Cifra base y qué gate falla |
| B. Descomposición causal | Separar por qué pierde (p. ej. ganadores cortados, relleno = barrido final, dependencia negativa de pares) | Lista de mecanismos con cifra |
| C. Callejones cerrados | Lo ya REJECTED con su informe (no repetir) | Tabla de exclusiones |
| D. Teoría | Plantear como control/parada óptima con coste de selección adversa e inventario | Forma cerrada/paramétrica, ≤5 parámetros |
| E. Prerregistro | Fórmula + rejilla + hash ANTES de medir | `PREREG_*.md` + `HASHES.txt` |
| F. Calibrar solo IS, validar OOS | 22 días: IS 05-22, OOS 23-26 | EVw, IC90 por días, sin 2 mejores días |
| G. Controles | Placebo (hora/permutación aleatoria), inversión, max-statistic, desagregar moneda×bucket | Veredicto |
| H. Auditoría del resultado | Positivo espectacular = bug hasta probar lo contrario; relleno estricto, bids >2 s fuera, libros cruzados fuera, mín 5 acc | Cifra corregida |
| I. Veredicto | REJECTED / EXPLORATORY / CANDIDATE con lo que falta | Informe + fila en checkpoint |
| J. Siguiente ronda | Variable o hipótesis rival nueva (no ajustar el mismo modelo a posteriori) | Prompt de la ronda |

## 2. Plantilla de prompt de ronda (copiable)
Alcance + presupuesto (llamadas, nice/ulimit) → qué leer (solo resúmenes) → hechos establecidos y REJECTED → tarea con fórmula/rejilla prerregistrada → métricas obligatorias → entregable (ruta del informe) → formato de respuesta (≤15 líneas: veredicto, n, EVw, IC90, OOS, sin 2 mejores días, llamadas, siguiente).

## 3. Registro de rondas (caso 0)
| Ronda | Pregunta | Veredicto | Lección transferible |
|---|---|---|---|
| Predictor AS | ¿Se anticipa el relleno adverso? | REJECTED (dAUC +0,007 vs +0,03) | Predecir el movimiento del ask (AUC 0,71-0,75) no es predecir la selección adversa: son objetos distintos |
| Escalera de patas (6 monedas, 26.802 patas) | ¿Comprar ambos lados y vender en rebote? | REJECTED (EVw OOS −0,198 a +10c) | Objetivo fijo corta ganadores: si toca +10c gana 41,9 %, si no 0,5 %; P(toque) respeta la cota martingala |
| Entradas <0,10 (710k rellenos) | ¿Pujas pasivas 1-9c? | REJECTED (hold −0,30; AS: relleno acierta 0,2-6 %) | El relleno es el barrido final del token que muere; pares con dependencia negativa (P conjunta ≪ producto de marginales) |
| Iteración D | ¿Vender al bid T−30 s? | +0,409 → +0,117 con profundidad real; IC90 cruza 0 | Sin profundidad de bid un positivo es artefacto; 65 % sin bid |
| Fórmula R1 (22 d, 6 monedas, 5 params, prereg 116f5c42) | ¿Vender/cancelar con q̂ = σ(logit m + ΔC 15m + ΔQ cola + zBinance)? | REJECTED salida/cancelar (17/18 variantes Δ OOS<0; placebo p=0,71) | La AS ya está hecha ANTES del relleno (win−mid −2,0 pp a t1−250 ms): tras el relleno el mid está calibrado. Cota teórica G≈0,1 % del coste de salir: la información extra mueve q̂ ≈1,3 pp vs coste ≈2,2 pp. Una cota analítica de ganancia máxima ahorra rondas: calcularla ANTES de medir |
| Fórmula R2 | Curva AS(δ) de la puja pasiva de entrada (x*=R−1/k) | (en curso) | — |

## 4. Trampas del método (ya cazadas en este caso)
- Relleno optimista (10 acc supuestas, mismo relleno de entrada para 2 patas) → medir P conjunta real.
- Venta sin comprobar tamaño del bid ni antigüedad de la cotización.
- Unidad = fill en vez de mercado+lado+bucket; media de cocientes en vez de Σpnl/Σcoste.
- Elegir la mejor celda tras mirar todas sin max-statistic.
- 4 días de OOS no permiten «sin 2 mejores días»: pedir ≥10 días o declarar la limitación.

## 5. Cómo replicarlo en otra estrategia
1. Copiar §1 como checklist; abrir una carpeta `experimentos/<mision>/<ronda>/` con PREREG + HASHES.
2. Fijar IS/OOS por días, el presupuesto de llamadas y la lista de callejones cerrados.
3. Lanzar la ronda con la plantilla §2, un agente a la vez; al cierre añadir fila a §3 y trampas nuevas a §4.
4. Si falta un dato para calibrar un término: logger mínimo (gz, retención, fuera de git) antes de rendirse.
5. Parar solo con fórmula validada (gates de promoción del CLAUDE.md) o imposibilidad estructural documentada.

## 6. Lección de método (R1)
Calcular primero la **cota de ganancia máxima** de la familia de reglas (aquí G=σφ(h/σ)−h·Φ̄(h/σ)) y compararla con el objetivo (548 €/día exigiría σ 10× mayor): descarta familias enteras sin medirlas. Pasar entonces a la palanca que SÍ tiene margen (la entrada/cotización), no a más variantes de salida.
