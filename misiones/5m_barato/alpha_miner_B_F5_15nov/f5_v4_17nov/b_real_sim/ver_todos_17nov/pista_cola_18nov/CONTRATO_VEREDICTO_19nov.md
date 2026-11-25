# CONTRATO_VEREDICTO_19nov (auditoria de datos, solo lectura, sin f_*/tasas)
1. Completitud: RED para la regla dia_completo (p7 l.335) tal como esta; datos reales OK. `cover` = (primera,ultima) fila de libro5 filtrada por tokens del universo (`grep -F -f tokfile`, p1 l.496/547); el universo (comp/END, p1 l.17-31) sale de sonda1_fotos_l2 (Sonda1), que omite 9-13 mercados BTC 5m/dia (cierres 23:55, 00:00 del dia y xx:55/xx:00 en limites de 4 h) y acaba siempre en cierre 23:50. m5_registro (filas k) trae 286-287 de 288. libro5_ms_prot es continuo 24 h (huecos de rotacion ~45 s; cabeceras/colas: 12-Nov acaba 23:57:23 en el fichero 1124981, 16-Nov 23:59:59).
   Consecuencia: todo dia fallara por construccion (fin ~23:52 < t1-120 s; inicio 00:02:10 en 13..18).
2. Small: AMBER (mayormente estructural; datos/reloj sin defecto hallado).
3. Inputs: ver informe del chief.
