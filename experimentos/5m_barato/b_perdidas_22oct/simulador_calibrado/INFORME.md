# E1 — Calibración del simulador maker fiel a B (B_FIEL) contra anclas on-chain. 23-Oct-2026. EXPLORATORY, solo lectura (B, ejecutores, main intactos)
Prereg congelado ANTES de correr: `prereg/PREREG_E1_CALIBRACION.md` (sha256 001c130d…, `sha256sum -c prereg/PREREG_E1_CALIBRACION.sha256`). Declarado como ya visto: las cifras de AVANCE (B_FIEL 0,58 vs 0,61, acuerdo 0,74).
Simulador bajo prueba: `cola_vs_cruce/scripts/e1q_sim.py` importado sin modificar (B_FIEL = settle 0, repost 1500, cancelación efectiva 280 ms, alloc prop). Datos: libro5 MEDIR 20-22 Oct.

## Veredicto: **NO_REPRODUCE**
El simulador acierta los AGREGADOS (tasa de relleno, EV, mediana de edad, volumen del libro) pero NO reproduce puja a puja ni la dinámica de órdenes, y el acuerdo de agregados con las cifras actuales es compatible con compensación de errores. No sirve todavía para medir palancas marginales de ±0,05-0,10 €/€.

## Criterios (EVAL = pujas 21-22 Oct; n = 212 pujas con mercado en el sim, 196 con el mismo lado; TUNE = 20-Oct, 43)
| Criterio | Umbral | B_FIEL nominal (280/prop) | Celda elegida en TUNE (450/prop) | |
|---|---|---|---|---|
| B0 lado coincide | ≥0,90 | 0,925 | 0,925 | PASA |
| B1 tasa de relleno | \|Δ\|≤0,05 | sim 0,582 vs real 0,587 (Δ−0,005; IC90 −0,061,+0,051) | sim 0,704 (Δ+0,117; IC90 +0,061,+0,173) | nominal PASA, elegida FALLA |
| B2 acuerdo puja a puja | acc≥0,80, κ≥0,60, recall y precisión≥0,75 | acc 0,740, κ 0,464 (IC90 0,36-0,57), recall 0,774, precisión 0,781 | acc 0,740, κ 0,440, recall 0,878, precisión 0,732 | **FALLA** (acc y κ) |
| B3 edad al relleno | KS D≤0,15, \|Δmediana\|≤0,5 s, ≥70 % de pares a ≤1 s | KS D 0,120 (p 0,40), mediana sim 1,01 s vs real 1,06 s; pares a ≤1 s: **58 %** (n=77) | D 0,124, Δmed 0,07 s; pares **57 %** (n=86) | distribución PASA, pares **FALLA** |
| B4 EV (€/€, mismas pujas) | \|Δ\|≤0,10 y cuotas de clase a ≤0,10 | sim −0,060 vs real −0,048 (Δ−0,012; IC90 −0,24,+0,22). Cuotas X1/X2/X3 0,37/0,22/0,41 vs C1/C2/C3 0,20/0,29/0,51: **X1 Δ0,17, X3 Δ0,10** | −0,048 vs −0,048; cuotas 0,38/0,24/0,38 | EV PASA (sin potencia), clases **FALLA** |
| W1 relleno explicado por prints L2 | ≥0,75 cada wallet y a ≤0,10 de B | 0xf074 0,945 (n=346), 0x0ab0 0,955 (n=467), B 0,814 (n=183); placebo ±90 s ≈0,00-0,02 | | ≥0,75 PASA; "a ≤0,10 de B" FALLA por 0,03-0,04 (causa abajo) |
| W2 volumen L2 vs on-chain (banda 0,10-0,30, 4.507 mercados, 17-22 Oct) | razón [0,85-1,15], Spearman ≥0,70 | razón 0,995 (ETH 1,000, SOL 0,986, XRP 0,976); Spearman 0,989 | | PASA |
Rejilla TUNE (lat_can 65/150/280/450 × alloc prop/lo/hi): kappa 0,13-0,49; la elegida (450/prop, κ 0,49 con n=43) no generaliza (B1 falla en EVAL); en TUNE la tasa real era 0,72 y en EVAL 0,59 (la tasa real varía por día más que la diferencia entre celdas). Tabla completa en `datos/cal_eval_a.txt`. Unión de fuentes de relleno real (ledger / on-chain / tardío) = ledger (174/298): sin diferencia.

## Qué falla y por qué (diagnóstico, `datos/cal_diag.txt`, descriptivo)
1. **Dinámica de órdenes NO fiel**: el sim publica 20,9 órdenes por puja (mediana 16) frente a 10,8 (mediana 8) de B real, Spearman 0,40. El hazard de relleno por orden del sim es ~la mitad del real (≈2,8 % vs ≈5,4 %); la tasa por puja coincide por compensación (más órdenes, más cortas). Es la causa más probable del acuerdo 0,74: el sim aún no copia cuándo B repega/cancela, solo cuántos relleno acaba teniendo. Candidatos a revisar (no probados): fuente del top de B (`lib.top` de su WS) frente a libro5, MIN_ENTRE_ACCIONES 0,1 s y cadencia 0,1 s del bucle, límites reales (max_vivas 5, presupuesto, `tick_cambiado`).
2. **Desacuerdos**: 25 rellenos solo en el sim (EV −0,285) y 26 solo en el real (EV −0,386); ambos adversos, sin sesgo sistemático de signo, pero sí de mezcla de clases (el sim da demasiado C1/X1 «atraviesa»: 12 de los 25 solo-sim son X). Por moneda, el EV no reproduce: ETH sim +0,21 vs real −0,14, SOL −0,32 vs +0,04 (n≈65 por moneda, signos opuestos) — el EV agregado coincidente es suerte de compensación, no fidelidad.
3. **W1 (B 0,81 vs wallets 0,95)**: 20 de los 33 rellenos de B sin print en su nivel tienen un print MÁS HONDO en la ventana (barridos C1: el WS imprime a otro precio); el sim ya cuenta una operación a q<puja como relleno, así que no es un agujero del replay (con «print en nivel ≤ puja» B subiría a ~0,93, definición post hoc). Las wallets, sentadas en cola, casi no sufren barridos. W2 confirma que el replay de operaciones es completo (0,995 en volumen).
4. **Wallets 0xf074dc84 y 0x0ab01745 como ancla de EV: inútiles hoy.** Solo ETH en banda (398 y 508 unidades, 17-22 Oct). EV 0xf074 −0,098 (IC90 días −0,18,+0,03), 0x0ab0 +0,049 (−0,11,+0,20); 20-22 Oct: +0,015 y +0,224 (+0,06,+0,33, 3 días). Su política (órdenes, cancelaciones) NO es observable on-chain, así que solo anclan el replay del libro (W1/W2), no la política. Su mezcla C1/C2/C3 es 0,13/0,20/0,67 y 0,09/0,21/0,71 frente a B 0,27/0,36/0,37 en ETH (`datos/w3_desc.txt`): B está mucho más expuesta a barridos que ellas; hipótesis, no medida.

## Qué falta para poder reproducir (por orden)
1. Ancla a nivel de ORDEN, no de puja: B guarda t_dec/t_post/t_cancel de cada orden (`cola_posicion/datos/ordenes_b.json`, 3.272 órdenes); comparar instante de publicación y cancelación sim vs real antes de mirar rellenos y calibrar hasta igualar nº de órdenes y vida media.
2. Reproducir la decisión con el código real de B (`decidir()` de `experimento_maker_h47.py`, en modo mock sobre libro5 grabado) en vez de reimplementarla; sin enviar nada.
3. Unificar las clases X/C (definición X1 con la desviación D1 vs C1 on-chain) y repetir por moneda.
4. Más días reales de B (EVAL = 196 pujas: SE de la exactitud ≈0,03, SE de EV ≈0,12): con los 3 días actuales B4 no tiene potencia ni para descartar ni para confirmar EV.
5. Wallets: si se quiere ancla de política hace falta dato de órdenes (p. ej. las de B en un futuro con micro-órdenes), no fills.

## Límites
Pujas reales con desenlace y mercado en el sim: 257 de 298 (23 fuera de MEDIR >22-Oct 14:40Z, 16 hueco global, 2 hueco de token = missing, no cero). Rejilla de 12 celdas elegida con 43 pujas (ruido). Tasas e IC por mercado (2.000 réplicas, semilla 20261023); sin IC por día (2 días). Tiempo de relleno real = recepción WS del print (no hora on-chain). EV real = on-chain b_clase (sin comisión maker).

## Reproducir
`cd experimentos/5m_barato/b_perdidas_22oct/simulador_calibrado && nice -n 19 ionice -c3 python3 -I scripts/cal_run.py` (≈4 min) · `scripts/cal_eval.py a|u` · `scripts/cal_diag.py` · `scripts/w_anchors.py` (≈8 min) · `scripts/w_diag_b.py` · `scripts/w3_desc.py`. Salidas en `datos/` (888 KB, hashes en `datos/HASHES.txt`). Handoff: statistical-validator (S1) puede usar B2/B3/B4 como línea base; red-team: el «EV coincide» es compensación de errores.
