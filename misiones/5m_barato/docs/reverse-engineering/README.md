# Ingeniería inversa 5m barato — agente `cheap5m-reverse-engineer`
Último recurso para problemas BLOQUEADOS. Invocación: la sesión principal lo lanza con un caso concreto (`subagent_type: cheap5m-reverse-engineer`; si la sesión no lo lista aún, reiniciar Claude Code o lanzar un general-purpose con el contenido de `.claude/agents/cheap5m-reverse-engineer.md` como prompt).
Ciclo: reconstruir → diagnosticar → hipótesis rivales → experimento mínimo → solución aislada → refutarla → persistir.
Ficheros (todos en este directorio): CASE_TEMPLATE.md, HYPOTHESIS_LEDGER.md, EXPERIMENT_LEDGER.md, FAILED_ATTEMPTS.md, DECISION_LOG.md, PROGRESS.md, `casos/<CASO>/EXPEDIENTE.md`, `tests/test_integridad_re.py` (`python3 -I tests/test_integridad_re.py`).
Ubicación: aquí y no en `docs/` raíz, para convivir con DECISION_LOG/MAPA de la misión (que ya existen).
Estados de cierre: SOLVED · PARTIALLY_SOLVED · EVIDENCE_INSUFFICIENT · HYPOTHESIS_REFUTED · BLOCKED · NO_ECONOMIC_EDGE_DETECTED. SOLVED requiere validación independiente de otro agente.
Seguridad: sin órdenes reales, sin secretos, sin tocar vivo/congelado, sin crons ni commits. Bash no es restringible por herramienta: se impone por instrucción + test + auditoría del chief.
Antes de abrir un caso: leer FAILED_ATTEMPTS (no repetir) y HYPOTHESIS_LEDGER (no duplicar).
