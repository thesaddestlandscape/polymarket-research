# BRIEF — Disección de los bots que operan donde nos afecta (B y su subvariante) — 09-Nov (Javi)
Mandato Javi: ir a por los bots que operan en el MISMO plano que B (mismos mercados 5m, mismos niveles de precio, misma ventana) y su subvariante. Diseccionarlos, ingeniería inversa, y usar todo a nuestro favor: generar EV y eliminar la selección adversa (AS). NO es el enjambre global (Q5 cerrado).
## Universo (acotado, no global)
Contrapartes que casan CONTRA nuestras órdenes de B (tomadores de nuestros bids) y competidores que cotizan en los mismos tokens/niveles/instantes. Fuentes: onchain_fills_*.csv.gz (maker/tomador explícitos; datalogs + keep_onchain_re_as_b en /mnt/HC_Volume_106538179/mover_09nov/ via symlink), registro ms `maker_ms_*`, libro5/libro5_ms, ledger de B (misiones/5m_barato/CLAUDE.md).
## Preguntas (por orden)
1. Quién nos rellena cuando perdemos (AS): clusters de wallets/tomadores en NUESTROS fills de B, frente a los fills que ganan. ¿Concentración por wallet (top ≤30 %)? ¿Persisten en días distintos?
2. Mecanismo de cada cluster: disparador (salto Binance, movimiento bid15, hora del ciclo, z), latencia relativa (usar reloj de RECEPCIÓN; onchain = bloque ~2,4 s tras casado), tamaño, lado.
3. Contra-política: qué regla de entrada/salida/cancelación evita ser su contraparte o los toma a ellos (p. ej. cancelar si firma del cluster). Medir en SIMULADOR con las MISMAS guardas del ejecutor, PnL ponderado por €, por cierre/día, sin los 2 mejores días, vs placebo e inversión.
## Reglas (CLAUDE.md trampas)
- Grupos y medida en días DISTINTOS (makers ganadoras 14-Oct). Desagregar moneda×marco×bucket 0,05. Unidad = cierre/mercado-lado, no fill. Desenlace oficial, cobertura declarada.
- Datos 26-Oct..06-Nov quemados para Q11; usar los 22 d de m5_registro solo para exploración; confirmar en forward desde 09-Nov. Prerregistrar regla antes de medir OOS.
- 0 órdenes reales, solo lectura. Análisis pesados nice 19/ionice 3, ulimit ≤3 GB, fuera de 06-09Z y de 22:20Z.
- Fail loud: n, IC90, periodo, comando reproducible. Veredicto: SOLUCIÓN / FALTA_INFO / NO_VIABLE.
## Entregable
informes/DISECCION_BOTS_B_<fecha>.md + tabla clusters (wallet, mecanismo, AS que nos causan, contra-política, EV simulado) + siguiente paso único. Cola posterior: validator independiente → alpha-miner (explotar a favor) → execution-engineer si hay regla.
