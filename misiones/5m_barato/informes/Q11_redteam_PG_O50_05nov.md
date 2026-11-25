# Q11 red-team de PG_O50 / GEO6 (05-Nov, cheap5m-red-team-auditor). TODO EXPLORATORIO, días ya gastados
**Veredicto global: INCONCLUSIVE, inclinado a desfavorable.** La ΔPnL de PG_O50 frente a G0 no la fabrica el fechado. Pero depende del modelo de relleno, que no está calibrado, y no sobrevive a la multiplicidad. La atribución del mecanismo («descuento frente a información», K1, K3, edad) sí es un artefacto del fechado del relleno. Validado: 0 €.

**Expediente:** `experimentos/5m_barato/q11/redteam/`
- Diseño fijado antes de calcular: `DISENO_RT.md`, sha 1b93653e….
- Scripts: `rt_sim.py`, `ana_r1.py`, `rt_b.py`, `rt_r3.py`. Logs en `out/*.log`; hashes en `HASHES.txt`.
- Recursos: nice 19, ionice 3, ulimit 3 GB, menos de 2 min de CPU en total, fuera de 06-09Z.
- Reproducción exacta de BASE contra barrido_corr:
  - PG_O50: 602 rellenos, +129,5 €;
  - G0: 2.938 rellenos, −166,9 €;
  - GEO6: 2.192 rellenos, −2,7 €.
- Libro espejado: ask(YES) = 1 − bid(NO) en el 100 % de la muestra, así que el cruce por el complementario es redundante.

## R1. Relleno «rancio» y fechado: FABRICATED para el mecanismo; INCONCLUSIVE para la ΔPnL
- **Fechado** (`out/ana_r1.log`):
  - G0: en el 96,5 % de los rellenos BASE el bid real ya había caído por debajo de L antes de rellenarse (mediana 3,0 s, p75 9,7 s, p90 20,6 s). En el 74,8 % el ask llegó antes a ≤L con el libro sin cruzar: la orden real habría sido cruzada una mediana de 3,2 s antes, con el mid 3c más alto.
  - PG_O50: 95,2 % y 67,6 %, con el mismo orden de magnitud de retraso.
  - Con la fecha temprana, la descomposición se invierte. En G0 pasa de «descuento −0,036 / información −0,036» a «descuento +0,172 / información −0,243». En PG pasa de «información +0,254» a «+0,090» (por acción).
  - K3 (salto ≤3 s) y K2 (edad ≤3 s) se miden en la misma escala que el error de fecha. **Las conclusiones de mecanismo de RE-Q11 no son interpretables.**
- **La PnL de un relleno no depende de la hora**: q·(gana−L) es igual para todo el par (k, L). La ΔPnL solo cambia si cambia el SÍ/NO del relleno. Cotas del modelo de relleno, con los mismos segmentos de cada política:

| ΔPnL [IC90 por cierre] | BASE | STRICT (solo travesía) | OPT (cola 0) | THIN (tamaño del print) | CROSS (rellena al tocar el ask L) |
|---|---|---|---|---|---|
| PG_O50−G0, 7 d | +201 [+54, +340] | +205 [+58, +346] | +192 [+44, +332] | +213 [+74, +348] | **+124 [−72, +313]**, sin 2 mejores días +57, 6/7 |
| GEO6−G0, 10 d | +164 [+64, +263] | +154 [+48, +255] | +158 [+57, +260] | +169 [+68, +263] | **+61 [−90, +201]**, sin 2 mejores días −0,2, 6/10 |
| PG_O50−GEO6, 7 d | +127 [+23, +227] | +144 [+41, +241] | +119 [+9, +223] | +132 [+29, +230] | **+81 [−51, +210]**, 5/7 |

- Con CROSS, G0 pasa de −166,9 € a +126,9 € en 10 días.
  - Los pares (k, L) que solo rellena CROSS dan EV +0,370 (n=1.026, +285 €). Son toques que rebotan.
  - El simulador BASE solo ve los rellenos en que el precio ATRAVIESA L, que pierden (EV −0,170 en los 2.211 pares adelantados). Es la misma brecha que R9-E4.
- **Regla prefijada:** GEO6−G0 pierde el 63 % con CROSS, así que da FABRICATED por la letra de la regla. PG−G0 (−38 %, IC que cruza 0) y PG−GEO6 (−36 %) dan INCONCLUSIVE.
  - CROSS es una cota alta: los makers post-only no cruzarían. Lo real está entre BASE y CROSS y no se ha medido.

## R2. Relleno simulado frente a real: INCONCLUSIVE (no hay datos reales en la celda de PG)
Fuente: 3.796 órdenes REALES de B (20-23 Oct, verdad on-chain por order_hash), pasadas por el mismo `fill_segment` con cinta WS (`out/rt_b.log`):
- P(relleno) por orden: real 5,3 %, BASE 2,3 %, STRICT 0,9 %.
- P(relleno) por puja: real 55,5 %, BASE 22,8 %.
- Recall de BASE 0,40 (81/202); precisión 0,94 (81/86).
- Por celda (real frente a BASE):

| celda | n | real | BASE |
|---|---|---|---|
| 1c bajo el bid | 1.961 | 4,9 % | 2,0 % |
| 2c bajo el bid | 1.234 | 6,1 % | 2,4 % |
| ≥3c bajo el bid | 310 | 1,6 % | 0,0 % |

- **Los rellenos reales que el simulador no ve son PEORES**:
  - no vistos: EV −0,172 (n=121), frente a +0,065 en los vistos;
  - sin travesía: −0,122 (n=168), frente a +0,144 con travesía (n=34), diferencia con IC90 por cierre (−0,37, +0,91).
- En la celda de B, esto va en contra del signo de los «toques buenos» de CROSS.
- Límites:
  - B no tiene órdenes a ≥6c bajo el bid, que es donde arman PG/GEO6;
  - su vida es corta (mediana 0,6 s);
  - la cinta WS es incompleta (el 28 % de los rellenos reales no tiene print en L).

Conclusión: el simulador no está calibrado (coincide con `calibracion_etiqueta` del 26-Oct, NO_CALIBRADA) y el signo del sesgo en la celda de PG es desconocido.

## R3. Reposición, doble conteo, régimen y sobreajuste (`out/rt_r3.log`)
- **Reposición: SURVIVES** (no hay ventaja de cola al re-armar: BASE pone la cola en INF o en el tamaño visible).
  - El patrón por segmento es ruidoso. En PG: seg2 −0,483 (n=81) y seg3+ +0,923 (n=87, +60 € de los 129,5 €). Una parte material del EV absoluto sale de los re-armados.
- **Doble conteo por cierre: SURVIVES para la Δ.**
  - El IC es por cierre y hay 0-4 mercados con ambos lados rellenos.
  - Sin los 5 cierres que más aportan, Δ PG−G0 = +170 (CROSS +85).
  - Pero **el PnL absoluto de PG_O50 (+129,5) es el de sus 5 mejores cierres (+139)**: el EV>0 es frágil.
- **Régimen: INCONCLUSIVE.**
  - En G0, el lado NO pierde en los 7 días de PG; el único día con NO ≥0 es el 26-Oct, sin PG.
  - El 81 % de la Δ PG−G0 sale del lado NO (+162,6, 7/7 días); el YES aporta +38,5 (6/7).
  - Colocación y régimen no son separables.
- **Sobreajuste: INCONCLUSIVE.**
  - Max-t por cierre sobre las 14 políticas candidatas probadas en los mismos 7 días: PG_O50 p=0,090 (PG_A50 0,085).
  - Las dos reglas declaradas antes (AVO_B70, PG_B70) fallaron; c=0,5 se eligió a posteriori.
  - GEO4/6/8 se comportan de forma suave, sin filo de cuchillo.
- **Potencia de «supera a GEO6»:** Δ diaria +18,2 €, sd 14,7. Si se retiene el 28 % (histórico 11-28 %), hacen falta ≈23 días, no 10.

## Qué cambiar en el prerregistro forward (antes del 06-Nov)
1. **Cotas del relleno obligatorias:** calcular cada día BASE, STRICT, OPT, THIN y CROSS.
   - PASA solo si la Δ es >0 con IC90 por cierre >0 en BASE **y** tiene la estimación puntual >0 en CROSS.
   - Si falla en CROSS: «no identificado por el relleno».
2. **No atribuir mecanismo con el tf de BASE.** Registrar t_below y t_cross de cada relleno, y reportar descuento/información, markouts y K3 con ambas fechas.
3. **Régimen:** Δ por lado.
   - Exigir Δ_YES >0 por separado, o bien ≥3 días forward con G0-NO ≥0 y Δ_NO >0 en ellos.
   - Si no se cumple, aunque pase: «no separable del régimen».
4. **EV absoluto sin los 5 mejores cierres >0** (además de sin los 2 mejores días); IC solo por cierre, no por día.
5. **Duración:** mínimo 10 días con revisión a 20. El criterio «supera a GEO6» no se puede declarar fallido antes de ~20 días, ni aprobado con 10 si la Δ se encoge.
6. Declarar la familia de 14 políticas ya miradas y congelar el modelo OWN y el umbral con sha (ya previsto).
7. **Medición decisiva fuera del simulador:** P(relleno | el ask toca L con nuestra puja sola en L, armada a ≥6c).
   - Vía: micro-órdenes reales en la escalera (peldaño micro-real, OK Javi) o L2 desde el 05-Nov (≈16-17-Nov).
   - Sin ese dato, ninguna ΔPnL de la escalera G pasa de EXPLORATORY.
