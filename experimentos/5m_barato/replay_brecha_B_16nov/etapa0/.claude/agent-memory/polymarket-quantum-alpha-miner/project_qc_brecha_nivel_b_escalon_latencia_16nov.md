---
name: project-qc-brecha-nivel-b-escalon-latencia-16nov
description: Q-C de BF5-REPLAY-COLOC-v1 (16-Nov): la carrera de cancelacion explica la brecha de nivel de B (sim -0,222 vs real -0,061) solo con latencia LO; es un escalon en delta 35-49 ms; en HI casi nada. EXPLORATORY.
metadata:
  type: project
---
Q-C (prereg PREREG_REPLAY_BRECHA_B_16nov s.7.3 + ADDENDUM1), ejecutado 16-Nov 16:42Z sobre 3.796 ordenes reales de B (20-23 Oct, 129 cierres, 82 rellenos sim = 70 TP / 12 FP). Reproduccion exacta previa de brecha_nivel_v3.json.
- MIX (l_pool_vigente_13nov, 3+v por oid): cierra 80 % (dEV +0,128, IC90 por cierre [+0,013; +0,255]); MIX_sinBTC 72 %; fijo 36/46/60: 89/79/50 %; HI +20,5: 50 % (anula 7 TP y 1 FP: no es el mecanismo).
- Fraccion cerrada SIN IC util: la propia brecha tiene IC90 [-0,13; +0,44]. Por dia 545/125/-46/0 %; LODO 63/16/130/92 %.
- Mecanismo (post-hoc): x = tf_sim - t_cancel_int; 7 de 12 FP en [35; 49] ms -> escalon: delta<35 los anula, delta>49 ninguno. 7 TP con x 127-866 ms (rellenos reales muy tarde tras la intencion de cancelar: sin explicar).
- Por clase (solo 22-23 Oct con ADD3): hi 2.127 ordenes, HI +20,5 cierra 7 %; lo sin potencia (2 rellenos sim).
**Why:** decide si la brecha de nivel motor-vs-real es "carrera de cancelacion" (arreglable en el motor) o no; la respuesta depende de la latencia de B en su epoca (HI), que esta DATA_BLOCKED.
**How to apply:** no citar el 80 % sin la condicion LO; siguiente prueba propuesta = delta por orden desde el RTT del propio DELETE de B (t_fuera - t_cancel_int, menos ack-ex 24 ms de 13-Nov), solo con ADDENDUM2 + OK chief/Javi (regla latencia vigente). Ficheros: experimentos/5m_barato/replay_brecha_B_16nov/etapa0/QC_brecha_nivel_mix.{json,tsv}, QC_desc_tf_menos_tcs.json. Ver [[reference-paridad-contra-json-original-no-md]].
