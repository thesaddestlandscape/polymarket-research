# Sonda1 — corte por tope y RTT de cancelación (05-Nov 14:50Z)
Fuente: /root/polymarket-research-datalogs/sonda1/real/sonda1_ordenes_*.csv(.gz) (30-Oct..04-Nov), estado.json, run_manifest.json.
- Parada limpia por tope_coste_total el 04-Nov 16:29Z: coste_total 2,7497/2,75; saldo 3,4124→0,6627 (cuadra con el coste); vivas=0, kill=null, envio_bloqueado=0.
- Regla de corte de Javi (≥15 cancelaciones con RTT en ≥3 mercados, 0 bloqueos): CUMPLIDA (n=44, 44 mercados). No se amplía el tope; reserva 0,66 $.
- RTT cancel (t_cancel_ack − t_cancel_envio): p50 61 ms, p75 73, p90 139, max 894. 4 de 44 >266 ms (30-Oct 887, 01-Nov 288, 02-Nov 615 y 894): días distintos, NO seguidos; 3 de ellas valido_gate=0 (ws_nivel_sin_evento).
- La regla «RTT>266 ms ×3» NO existe en sonda1.py (grep 266: 0 resultados; el kill-switch solo mira errores/transitorios/estado ilegible): era criterio de plan, no código. Por tanto kill=null es esperado; no hay parada que se haya dejado de disparar.
- 5 órdenes con estado_final=LIVE (30-Oct, 31-Oct, 02-Nov, 03-Nov ×2): todas size_matched=0, valido_gate=0, motivos libro_perdido_con_orden_viva / ws_nivel_sin_evento, cancelación con ack (RTT 58-143 ms); en 3 de 5 t_lectura_terminal vacío → el estado terminal no se leyó y el valor por defecto quedó LIVE. Artefacto de lectura, no orden viva: mercados 5m ya resueltos, vivas=0 y el saldo cuadra. NO verificado contra get_orders del CLOB (no se consultó).
- Consecuencia analítica: excluir esas 5 (y valido_gate=0) de cualquier cifra de RTT/cola; el RTT de cancel (n=44) sí es utilizable.
