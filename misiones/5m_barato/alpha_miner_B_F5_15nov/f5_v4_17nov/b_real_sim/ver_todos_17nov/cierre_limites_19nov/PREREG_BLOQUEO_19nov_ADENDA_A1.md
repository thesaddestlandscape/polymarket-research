# ADENDA A1 a PREREG_BLOQUEO_19nov.md (sha 8d51ffbd...), escrita 19-Nov ~09:32Z TRAS la 1a medicion (declarada post hoc).
Motivo (defecto mecanico del ancla, no del resultado): 89/170 casos sin ancla porque el print del relleno sale al precio del MAKER (1-L en el complementario, nuestro L en el propio), no al limite del tomador 1-tk_eq (difieren cuando eq_menos_L != 0). Visto en 8 casos sin ancla.
Cambio UNICO: ancla = primera fila T BUY del complementario con precio en {1-L, 1-tk_eq} (+-0,005) en [tm3-100, tm3+1500]; si no, T del propio con precio en {L, tk_eq} (+-0,005). Reglas R1-R3, acierto, placebos y criterio de aceptacion SIN CAMBIOS.
Informativo (no criterio): estratificar positivos por rem_sh >= 1 accion (restos de <1 accion no bloquean nada relevante).
La 1a medicion (out/u1b_prereg_bloqueo.csv) se conserva y se reporta junto a la A1.
