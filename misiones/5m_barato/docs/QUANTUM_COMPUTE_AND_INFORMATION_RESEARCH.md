# Protocolo de investigación cuántica, híbrida y de nuevas fuentes de información
(Origen: carpeta de Drive del agente cuántico, 29-Oct-2026. Adaptado al repo.)

## Principio
Cuántica real, híbridos, quantum-inspired y nuevas fuentes de datos son opciones activas si atacan el cuello de botella identificado; no son objetivos por sí mismos. Deben mejorar pronóstico, ejecución o EV neto.

## Distinciones obligatorias
- **QPU real**: hardware cuántico físico. **Simulador**: circuito emulado. **Quantum-inspired**: algoritmo clásico. **Clásico**: ML/estadística convencional.
- No reportar simulación como hardware ni afirmar ventaja sin benchmarks comparables y replicados.

| Cuello de botella | Vías | Control obligatorio |
|---|---|---|
| Predicción probabilística | Bayes/ML clásicos, quantum kernels, reservoir | Mid y baseline calibrada; walk-forward OOS |
| Estado oculto/no linealidad | State-space/HMM, secuencia, QRC exploratorio | Ablación y estabilidad por régimen |
| Optimización discreta (cotizaciones/inventario) | MILP/heurísticas, quantum-inspired, annealing/QAOA | Comparar solución, tiempo y coste vs solver clásico |
| Datos ausentes | APIs, WS, on-chain, conectores autorizados, proxies | Timestamps, licencias, cobertura, permisos |
| Latencia | Inferencia offline/clásica en memoria | Medir camino completo; QPU fuera de la ruta crítica |

## Protocolo
1. Decisión concreta y cuello de botella. 2. Datos y mejor baseline. 3. Por qué cuántica/nuevo dato podría mejorar. 4. Simulador/prototipo barato si es informativo. 5. Hardware real solo con proveedor/SDK/acceso/coste identificados y aprobación de Javi. 6. Benchmark con mismos datos/splits/tuning. 7. Revisión estadística y red-team independientes.

## Acceso a información
El cómputo no crea observaciones privadas. Documentar qué se observa, qué se infiere y qué es no identificable. No eludir autenticación ni leer/imprimir secretos.

## Regla de este repo
Aplican las trampas de `CLAUDE.md` (fugas de futuro, NaN por ventana, clave k15, ask real, gates). Agentes: `polymarket-quantum-alpha-miner` (mecanismo económico), `polymarket-quantum-researcher` (pruebas acotadas cuánticas/fuentes), `polymarket-predictive-alpha-engine` (calibración y EV). Ninguno valida por sí solo: validador estadístico + red-team.
