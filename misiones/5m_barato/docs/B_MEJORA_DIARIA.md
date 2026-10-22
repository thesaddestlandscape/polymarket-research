# B — protocolo de mejora diaria (orden de Javi 22-Oct 11:35Z)
Objetivo: reducir la selección adversa de B y explotar más lo que funciona, cada día. Lo que sabemos hoy (b_postmortem, 22-Oct 11:30Z, 251 pujas, 152 rellenos, solo lectura): EV ponderado +0,104, IC90 (−0,177,+0,414), **sin las 2 mejores posiciones −0,002**; XRP −0,025 (sin 2 mejores −0,314), ETH +0,151, SOL +0,168; hb=8 UTC −0,248, hb=4 +0,713 (n=36); acierto relleno 23,7 % frente a 38,4 % de no rellenos (selección adversa visible).
**Claves ya identificadas** (`b_seleccion_adversa/INFORME.md`): R2 (bid15 mismo lado ≤3c sobre mi puja) y R3 (+≥26 acc casadas 30 s + hora ≥4 UTC) en ETH/SOL/XRP; H62 (XRP peor); rechazadas con libro real: confirmación previa, cancelar por bid15, cobertura con lado contrario, spread, tamaño del top, profundidad. Irreducible fuera del nicho R3: 0,26 €/€.
**Ciclo diario**
1. 10:40Z cron `r1_fwd_cron.sh`: forward R1/R2/R3 (población, D-1). 10:55Z cron `b_mejora_diaria_cron.sh`: postmortem de B real → Telegram.
2. Chief: leer ambos; ¿R3 acumula días? ¿alguna celda de B cruza n≥15 con IC90 por días no incluido en 0? Anotar en DECISION_LOG.
3. Agente de mejora de B (cuando haya hueco): una palanca por día, con split por días y placebo; entrega propuesta, nunca cambio directo.
4. Cambios a B: SOLO como variante (fichero nuevo) + `/code-review` + OK Javi + peldaño micro-real. `experimento_maker_h47.py` (sha c82f5dc5f304b8a6) intocable hasta 500 pujas (gate de H23).
5. Brazo shadow R3 en tiempo real (agente prioridad 1) = forward emparejado contra B real.
Límite honesto: la selección adversa es estructural; el objetivo es acotarla (R3 en el nicho) y mover capital a donde el EV es positivo, no eliminarla en BTC todavía (H63).

## DECISIÓN (Javi 22-Oct 11:45Z): B sigue COMPLETO hasta N=500; si XRP sigue perdiendo sistemáticamente → se quita de B y pasa a una línea aparte con agentes dedicados
Criterio fijado AHORA, antes de ver el resultado (propuesto por el chief; Javi puede corregirlo): al llegar a 500 pujas, XRP «palma sistemáticamente» si b_postmortem da para coin=XRP EV ponderado por € ≤ 0 **y** EV sin las 2 mejores posiciones ≤ 0 **y** ETH+SOL juntos no lo están (para que no sea un mal régimen general). Hoy (251 pujas): XRP −0,025 / −0,314; ETH +0,151; SOL +0,168. H62 (forward «B sin XRP», IC90 por días < 0) corre en paralelo como segunda evidencia.
Si se cumple: (1) variante de B sin XRP en fichero nuevo + `/code-review` + OK Javi (el fichero de B no se toca antes de 500); (2) XRP pasa a línea propia «XRP-5M» con agentes dedicados (por qué rinde menos que ETH/SOL; si hay palanca propia, p. ej. R2/R3 solo en XRP, otro rango de precio/hora; solo shadow hasta gate).
