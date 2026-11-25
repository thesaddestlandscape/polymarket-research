---
name: project-qc2-delta-propio-brecha-b-16nov
description: Q-C2 (16-Nov) — δ por orden con la ida y vuelta propia del DELETE de B cierra 26 % de la brecha de nivel (techo por δ 41 %); MIX 80 % era artefacto; HI = retraso del feed WS, no del camino de órdenes; RTT ≥1 s endógena (DELETE sobre orden casada ~1,6 s)
metadata:
  type: project
---

Programa BF5-REPLAY-COLOC-v1, ADDENDUM2 sellado 2026-11-16 18:05Z (sha256 d3ea7183…), resultados en
`experimentos/5m_barato/replay_brecha_B_16nov/etapa0/QC2_delta_propio.json` (+ `QC2_posthoc_rtt_relleno.json`). Muestra: 3.796 órdenes reales de B, 20-23 Oct.

Hechos verificados (no autocertificados; pendiente validador/red-team):
- δ_i = (t_fuera − t_cancel_int) − 24 ms ⇔ cortar el segmento simulado (verif_v3 simula [t_ini, t_fuera]) en t_fuera − 24. tf ≤ t_fuera en 82/82, así que x ≤ rtt por construcción: toda prueba «rtt larga ⇒ sobrevive» es casi tautológica y los placebos deben condicionarse a rtt_j ≥ x_i.
- V0 anula 6 FP y 0 TP: cierra 26,2 % (ΔEV +0,042, IC90 por cierre [+0,0105, +0,082]). Techo de cualquier δ ≥ 0 sin tocar TP (C2) = 40,9 %; quitar los 12 FP (C1) = 72,5 %. El 100 % no se alcanza con δ: hay 4 FP con x ≤ 0 (cola/sello) y 132 FN (94 son prints propios excluidos).
- El 79,9 % de MIX anulaba 10 rellenos REALES perdedores. La fracción cerrada premia anular TP perdedores: hay que usar S = FP anulados − TP anulados y los techos.
- HI (20-22 Oct ~100 % hi): la ida y vuelta hi − lo dentro del 23-Oct es +1 ms, y V4 (δ − 20,5 en hi) da 11/36 rellenos reales imposibles (V0 2/36). Lo único compatible: el salto HI está en la ENTREGA del feed WS (~20 ms), no en el camino de órdenes ni en los relojes. La carrera no necesita corrección HI; la detección de B por WS sí llega ~20 ms tarde (hipótesis abierta).
- La ida y vuelta es endógena en el lado TP: 54 órdenes con ≥1 s, el 72 % con relleno real, y 38 con cancel_ya_terminal_ack. Un DELETE sobre una orden ya casada tarda ~1,6 s. La evidencia por orden limpia es la de los FP (rtt 56-63 ms).

**Why:** Javi pide cerrar el 100 % de la brecha sin forzar. Este resultado fija qué parte es latencia (≤41 %) y cuál no.
**How to apply:** no reutilizar MIX/13-Nov para B (era transferencia LO→HI y anulaba TP). Siguiente palanca: la cola y el sello (4 FP x ≤ 0, 38 FN multi-maker) y el retraso del tf simulado (4 de 7 TP con 300-900 ms de retraso). Véase [[reference-paridad-contra-json-original-no-md]].
