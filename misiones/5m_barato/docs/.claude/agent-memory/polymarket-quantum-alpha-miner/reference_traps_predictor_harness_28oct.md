---
name: reference_traps_predictor_harness_28oct
description: Trampas técnicas y de proceso del predictor de B (sklearn 1.9, fugas te_age/nivel, registro sin libros 15m, tope de llamadas)
metadata:
  type: reference
---
- sklearn 1.9 HistGradientBoosting lanza ValueError ("window shape cannot be larger than input array shape") si una columna es toda NaN o constante: filtrar columnas sin variación y early_stopping=False (por defecto se activa con >10k filas).
- Fugas cazadas antes de mirar OOS: te_age (te posterior a tau) y el nivel de la puja del relleno (usar bb(tau−130)+0,01); v60 desde bn.sec con segundo <= floor(tau/1000)−1.
- m5_registro (05-Oct, 6 M primeras líneas): 708 tokens 15m con fila k y 0 filas q -> bid15 no sale de ahí; m15_registro sin verificar.
- Tiempos: sim+rasgos 36 s (05-Oct) a 140 s/día (41 M líneas); 22 días ≈ 45-50 min a nice 19 ionice idle; evaluación con 11 días ≈ 1 min.
- Proceso con tope de 20 llamadas: extracción 'anytime' (OOS primero, IS intercalado) y espera con bucle python time.sleep dentro de una llamada (el sleep de shell está bloqueado); parar el bucle antiguo por el PID del padre del python, no con pkill -f; la notificación de tarea en segundo plano no es un mensaje del usuario.
