---
name: trampas-out-v3-motor-16nov
description: Límites verificados (16-Nov) al reutilizar out_v3/CX_v3dd y SEGT_v3dd del motor v3 de B (clase, placebos, tamaño, tf, cola) — leer antes de diseñar cualquier prueba CPU≈0 sobre ellos
metadata:
  type: project
---

Hechos verificados leyendo código/ficheros el 16-Nov (prereg `misiones/5m_barato/alpha_miner_B_F5_15nov/PREREG_REPLAY_BRECHA_B_16nov.md`, sha f1a7d766…):
- `CX_v3dd_<D>.pkl::A` agrega por var×moneda×L y día, SIN tiempo: no permite métricas incondicionales por clase de suelo salvo en G0 (SEGT trae todos los segmentos). Para el resto: «día LO-puro» o una réplica que guarde cada segmento.
- CX trae solo 20 placebos por variante (`S_PLC=20`, `passT_cxb_v3.py:96`): p mínimo 1/21 ≈ 0,048, nunca pasa Bonferroni 0,0125. Hacen falta ≥100.
- Tamaño s ≤ 5 sale EXACTO de SEGT: `Q_s = min(s, Q_5)` por cadena (k, L), porque los tiempos del segmento no dependen de `rem` y el relleno es min(rem, V). Más de 5 exige réplica.
- `SEGT_v3dd` (15 días, 11-Nov 11:47-12:09Z) es anterior al arreglo de `tf` del 12-Nov: `tf` no vale; q/pnl sí (MULTIVARIANTE_GOLD_RIESGOS_12nov.md §2).
- Cola BASE (`engine.py::fill_segment`): con L < bid la cola es INF hasta que el bid baja a L → el motor es conservador para colocaciones profundas (cota inferior de P(fill)).
- `brecha_nivel_v3.py` crea `out_replay/` al importarse: copiar `pnl_of`/`sim_con_delta`, no importar.
- `bidL` de SEGT = bid_rx(t_dec−300 ms) − L, no el bid en t_dec.

**Why:** cada uno habría invalidado en silencio una prueba «barata» sobre out_v3.
**How to apply:** comprobar estos puntos antes de prometer una cifra por clase, un p ajustado o un tamaño desde out_v3. Ver [[feedback_latencia_solo_datos_reales_vigentes_16nov]].
