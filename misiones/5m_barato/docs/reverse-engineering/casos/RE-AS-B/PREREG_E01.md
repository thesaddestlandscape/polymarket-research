# PREREG E-RE-AS-B-01 (26-Oct-2026 ~08:55Z) — escrito ANTES de abrir vpv_2026-10-24/25 (no vistos por este agente; detector_ex_ante solo vio una prueba en seco del 23-Oct)
Pregunta: ¿la «selección adversa −18 pp» (rellenas vs NO rellenas) es una propiedad del RELLENO frente a su precio (pérdida económica real, informada o por impacto) o sobre todo
el condicionamiento mecánico de la trayectoria (las no rellenas son, por construcción, las que el precio dejó atrás al subir) que predice la hipótesis nula martingala?
Ya visto (no ciego) en datos de B 20-23 Oct (r1_salida.txt, anatomia/pujas.csv): rellenas hit−p −0,017/−0,032; no rellenas +0,024 (orden) /+0,060 (unidad) /+0,131 (pujas.csv).
## Datos (independientes de B, días 24-25 Oct)
`/root/polymarket-research-datalogs/vida_puja_virtual/vpv_2026-10-2{4,5}.csv.gz`: pujas virtuales 5 acc al mejor bid b∈[0,10-0,30], cada 10 s por token, vida 60 s.
Filas con `gana` vacío = missing (se reporta cobertura, no se imputan). mid0=(b+ba)/2 con ba = mejor ask en t0; se descartan filas con ba<=b o ba vacío.
## Métricas (unidad = vida; inferencia por CIERRE = `cierre`, todas las monedas del mismo cierre una unidad; bootstrap 2000, semilla 2610)
Q1 M_f = media(gana − b | relleno), para relleno_opt y relleno_pes. Q2 M_nf = media(gana − b | no relleno). Q3 S = M_nf/(M_nf − M_f) (parte de la brecha que viene del lado NO rellenado).
Q4 calibración en t0: media(gana − mid0) sobre todas las vidas. Q5 (H2 techo/impacto): M_f(pes) − M_f(opt y no pes). Q6 exposición: por mercado-lado, nº de vidas k;
Spearman(k, gana−b) en unidades NUNCA rellenadas (opt) y en unidades con algún relleno. Robustez: solo primera vida por mercado-lado; por moneda; por día.
## Reglas de decisión (fijadas antes)
- «Brecha mayoritariamente mecánica (H0/H2): el −18 pp NO es el premio de una mitigación» si S(opt) ≥ 0,6 Y IC90 de Q4 contiene 0 Y |M_f(opt)| ≤ 0,03.
- «Componente informado material en el relleno (H1)» si el IC90 de M_f(opt) tiene cota superior < −0,03.
- «H2 (techo condicionado al fill por barrido)» apoyada si IC90 de Q5 < 0. Si nada de lo anterior: inconclusa.
- Predicción H0 de Q6: Spearman>0 en nunca-rellenadas; ≈0 en rellenadas. Solo descriptivo (no decide).
## Q7 (después de 09:30Z si load5<4): población on-chain 20-22 Oct (pickles b_vs_poblacion F_D.pkl, desenlace igual que x2): hit−pc por unidad mercado-lado de P y de B,
IC90 por cierre, barrido sí/no. Mismas reglas: |hit−pc|(P) ≤ 0,03 ⇒ el relleno real de la población no pierde más que ~3 pp frente a su precio.
