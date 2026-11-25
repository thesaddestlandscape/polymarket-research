---
name: reference-harness-escalera-g
description: Arnés reutilizable (05-Nov) para la escalera G de 5m barato ETH/SOL/XRP: reproducción exacta de G0/dec2, etiquetas S_*, oráculos, rejilla de decisión 500 ms, walk-forward y simulación de políticas con reposición
metadata:
  type: reference
---
Carpeta experimentos/5m_barato/q11/barrido_corr/ (05-Nov-2026; scripts hasheados en HASHES.txt; out/*.pkl fuera de git por .gitignore):
- passA.py DIA: motor escalera_B/engine.py sin tocar + cinta on-chain re-sincronizada idéntica a esc_dec2.py; comprueba G0 contra dec2 (10/10 días exacto); etiquetas S_wallet/S_orden/S_nivel/S_thru, cruce vs fallback, rasgos g_* (feat_day.py) a tf−{rejilla,1,300,1000} ms, Binance/CL/fase a tf−300; oráculos ON*/ANTI*/OY60/OYD60. ~20 s/día, 1,3 GB.
- passC1.py DIA: rejilla de decisión 500 ms (k, L, t con puerta G) con rasgos causales y etiquetas futuras (~15 s/día, ~100 MB/día: se borró, regenerable).
- passC2.py / passC2o.py: HGB walk-forward por día (submuestra 12 %), umbrales de cobertura en entrenamiento.
- passC3.py (cancelación continua), passC5*.py (puerta de colocación, placebos de otro token, inversión, reglas geométricas), ana_c*.py (ΔPnL frente a G0 con IC90 pareado por cierre y por día, p bootstrap).
Fuentes de entrada: dev .../sonda1/p2/precursores_barrido/out/{tape,bad}_D, datalogs sa_ms/ms_D.npz, x_D.csv.gz (clave_cancelacion/out o A3_guarda/fwd), data/prices/chainlink_D.
**How to apply:** partir de aquí para cualquier política de la escalera G en lugar de reescribir el simulador; ver [[project-trampas-politicas-hazard]].
