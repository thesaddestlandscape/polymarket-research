---
name: feedback_muestreo_negativos_fuga
description: Submuestrear negativos por t%10 filtra T mod 10 y da AUC .97 falso en el hazard de barridos 5m; usar muestreo aleatorio
metadata:
  type: feedback
---
Al submuestrear una rejilla 1 s para entrenar HGB, no muestrear negativos con t%10==0 (positivos en todos los segundos): T (=fin-t) queda multiplo de 10 solo en negativos, fuga. Resultado espectacular (AUC .97 vs .77 previo) = bug primero. **How to apply:** muestreo aleatorio con semilla; verificar reproduciendo la cifra previa (H-SURF .77). Contexto: Q11 barrido multivariable 05-Nov, experimentos/5m_barato/q11/barrido_multi/. Tambien: HGB sin OMP_NUM_THREADS=1 disparo el load a 17.
