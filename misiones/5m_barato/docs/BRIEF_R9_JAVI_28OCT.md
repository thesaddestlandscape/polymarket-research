# BRIEF R9 (28-Oct noche) — mandato de Javi tras R8 (ninguna política CANDIDATE)
Regla: si no pasa NO se cierra; todo el equipo (de uno en uno, tokens mínimos) hasta dar con las claves; gates sin relajar, pre-registro con hash antes de medir. Base: FORMULA_R8_B.md y FORMULA_R8_L1RETRASO.md. R9 técnica propuesta por R8: puja fija profunda bb−4..−6 respecto al bb previo al barrido, hazard alto y T_rem<120 s, cola del nivel desde L2 (maker_ms/onchain).
Comentarios de Javi (tal cual, por resultado de R8):
1. Prima +0,365 (D_now −3..−4, información disponible en el momento) existe: diseñar la estrategia que la capture sí o sí, si la información para ello está disponible.
2. Mecanismo (makers re-cotizan en ms; cobra quien ya está en reposo en el nivel que el barrido sobrepasa): explotarlo a nuestro favor; diseñar la estrategia que lo permita.
3. Tomador a t+215 ms REJECTED (ask a ~5 ticks del print, solo en 26 % de eventos): el problema está identificado, resolverlo y explotarlo.
4. Maker a bb corregido −0,314: identificar qué falla y convertirlo en estrategia explotable.
5. Clasificador del retraso (AUC 0,687): si predice el retraso evita pérdidas; explotarlo (filtro/evitar).
6. Política de cotizar −0,217, oráculo −0,281: saber que llega el barrido tiene que ser explotable; investigar TODAS las vías que sí den dinero.
7. Hazard bajo +0,695 en BTC (no reproduce con logit ni ETH): si es positivo en BTC, explotarlo; único OOS limpio = días desde 28-Oct.
8. Brecha real−sim +0,135/día: eliminar la brecha, simulador = realidad. Si el simulador es pesimista, ¿realmente estamos minando dinero?
9. Colocación 20–60 s no mejora v258: encontrar el tramo de segundos que sí mejore (tiene que haberlo).
10. ETH: celda T_rem 120-200 s, hazard bajo, m=3 OOS +1,018 8/10 (22 €/día): seguir la pista, tirar de la manta.
