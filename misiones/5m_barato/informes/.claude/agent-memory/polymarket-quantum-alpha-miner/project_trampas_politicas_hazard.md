---
name: project-trampas-politicas-hazard
description: Trampas de método cazadas el 05-Nov al convertir un hazard/score en política maker (cancelación continua degenerada, control OWN-only, claves float32, BLAS bajo ulimit, carga del VPS)
metadata:
  type: project
---
1. Política «cancelar cuando el hazard sube» evaluada en continuo degenera en NO OPERAR: los rellenos se concentran en las ventanas de hazard alto (en la escalera G, el 30 % de tiempo con hazard más alto contiene ~90 % de los rellenos). Comparar siempre P(relleno) y horas en libro frente a G0 y probar la variante «puerta de colocación» (el score solo decide armar).
2. Un AUC alto de hazard en rejilla puede ser solo geometría: incluir SIEMPRE un modelo de control con solo (T, L, bid-L, moneda, lado) y comparar AUC dentro de estratos de bid-L; en Q11 libro+actividad no añadía nada (−0,014..−0,002).
3. Tercil/cuantil de score calculado con la distribución del propio día de prueba = mirada a la distribución; los umbrales salen de los días de entrenamiento.
4. Claves de merge con L en float32 (0,1 → 0,10000000149) frente a float64 dan 0 coincidencias en silencio: redondear L a 2 decimales en ambos lados.
5. Con `ulimit -v 3000000`, numpy/OpenBLAS con 8 hilos revienta por memoria virtual (RSS real 1,4 GB): exportar OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 y leer los x_*.csv.gz de Binance por trozos con ventana (día−3 h). HGB de sklearn también usa todos los núcleos si no se limita.
6. La regla «nunca con load5>4» es inalcanzable en este VPS (0/200 muestras de vigia_carga_sistema ≤4 en ~50 h, nproc=8): aplicar la regla por núcleo del CLAUDE.md raíz (load5/nproc>3) y la de misión (load<16), con nice 19/ionice 3/ulimit, y declararlo en el informe.
7. No editar un .sh que está corriendo (bash lo lee por desplazamiento); escribir uno nuevo.
**Why:** cada una costó una pasada o pudo fabricar una conclusión falsa en Q11.
**How to apply:** repasar antes de convertir cualquier predictor en política de colocación/cancelación. Relacionado: [[project-q11-barrido-corregido-05nov]].
