# ADENDA 1 a PREREG_E01 (26-Oct ~09:05Z) — escrita DESPUÉS de la primera pasada (e01_salida.txt)
Defecto hallado: `gana` en vpv_2026-10-2{4,5} tiene cobertura 30,8 % (12.182/39.593 vidas; 1.082/3.456 mercados) porque el logger corre a las 04:41Z y
`maker_ms_desenlaces_cache.json` se actualiza a las 05:20Z. La falta es por mercado y no se asocia a relleno ni precio (P(fill opt) 0,871 vs 0,860; b 0,217 vs 0,217),
pero no se puede probar que sea aleatoria respecto al desenlace. Cambio ÚNICO: `gana` = (cache actual[str(mercado)] == lado), cache leída 26-Oct (cubre 3.454/3.456);
se comprueban 0 conflictos con las filas que ya tenían `gana`. Métricas, reglas, semilla y unidades del PREREG sin cambios. La pasada 0 se conserva como e01_salida_pasada0_cob31.txt.
