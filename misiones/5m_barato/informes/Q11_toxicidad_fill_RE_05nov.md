# Q11: toxicidad del relleno y mecanismo de PG_O50 (05-Nov, reverse-engineer, caso RE-Q11). TODO EXPLORATORIO
**Estado de cierre: EVIDENCE_INSUFFICIENT.** Hay un mecanismo plausible, medido solo en días GASTADOS y sin prerregistro forward. No se toca producción ni ningún prerregistro.
**Base:** escalera G0 (rellenos de `barrido_corr/out/A_all.pkl`, sin `src=bloque`): n=2.922, 634 cierres, 10 días (26-Oct..04-Nov). EV = Σpnl/Σcoste con rebate. IC por bootstrap de cierres (4000) y de días. Placebo = permutación dentro de día×moneda.
- Diseño fijado ANTES de calcular: `experimentos/5m_barato/q11/toxicidad_re/DISENO_TOX.md`, sha 07bde82a8c3b7def… (14:01Z). Las partes 2-4 son post hoc y DESCRIPTIVAS.
- Código, logs y hashes: misma carpeta (`HASHES.txt`, `out/ana_tox*.log`).
- Recursos: nice 19, ionice 3, ulimit 3 GB, ~2 min de CPU. load5/nproc ≈0,8 (la regla absoluta load5<4 no se cumple nunca con 8 núcleos; mismo criterio que el alpha-miner).

**Descomposición usada en todo el informe.** m0 = mid del libro a tf−300 ms. EV = DESCUENTO (m0−L) + INFORMACIÓN (gana−m0), cada término dividido por el coste. Markouts mk = mid(tf+1/10/60 s)−m0.

## 1. Toxicidad del relleno: 4 contrastes fijados de antemano (familia de 4, promoción con alfa/4)
| contraste (grupo vs resto) | n | EV grupo vs resto | dif [IC90 cierre] [IC alfa/4] [IC90 día] | p placebo | sin 2 mejores días | días con dif<0 | qué componente pierde |
|---|---|---|---|---|---|---|---|
| K1 posición: nuestro L en o por encima del bid real a tf−300 | 2.240/682 | −0,112 / +0,043 | −0,155 [−0,34,+0,03] [−0,41,+0,09] [−0,37,+0,02] | 0,136 | −0,012 | 5/10 | **descuento** (−0,151 frente a +0,295); la información va al revés (+0,027 frente a −0,264) |
| K2 edad ≤3 s | 321/2.601 | −0,163 / −0,065 | −0,098 [−0,35,+0,18] | 0,481 | −0,008 | 5/10 | — |
| **K3 salto adverso de Binance hace ≤3 s** | 594/2.328 | **−0,289 / −0,021** | **−0,267 [−0,52,−0,001]** [−0,59,+0,10] [−0,46,−0,06] | **0,013** | −0,159 | 7/10 | **información** (−0,330 frente a +0,034) |
| K4 primera mitad del ciclo (T≥150 s) | 1.619/1.303 | +0,002 / −0,178 | +0,180 [−0,08,+0,42] | 0,054 | +0,034 | 4/10 | los tardíos pierden información (−0,117) |

Ningún contraste pasa alfa/4 por IC. K3 pasa el IC90 y el placebo a 0,025, pero:
- es la réplica de P-B en G0;
- usa los mismos días en que se encontró P-B, así que no es evidencia independiente.

**Lo que discrimina es la colocación, no el relleno** (descriptivo, post hoc; fuentes `ana_tox2.log` y `ana_tox3.log`):

| condición | n | EV | información | días positivos |
|---|---|---|---|---|
| armada con bid−L 1-5c | 620 | −0,31 / −0,47 | −0,21 / −0,39 | 2/10 |
| armada a ≥6c | 1.904 | +0,033 | — | — |
| armada a ≥6c y edad >35 s | 929 | +0,130 | — | 6/10 |
| sin salto ≤3 s y edad >35 s | 783 | +0,169 | — | 7/10 |
| primera colocación | 1.142 | +0,018 | — | — |
| re-armado | 1.780 | −0,137 | — | — |

- Por lado: NO armada a <6c da −0,405 (0/10 días positivos); YES armada a ≥6c da +0,247 (7/10).
- Profundidad L1 (bsz): tercil bajo −0,269, tercil alto +0,078.
- Lectura: es tóxica la orden puesta cerca del precio (o re-armada) en mitad de un movimiento. Se rellena en segundos y pierde por información. La orden vieja, puesta lejos, cobra una pequeña prima.
- La posición en el instante del relleno no separa la selección adversa (AS). El tramo «≥6c bajo el bid a tf−300» (n=118) es un desplome informado: información −0,967.

## 2. Mecanismo de PG_O50 (y de GEO6): hipótesis rivales y experimento mínimo
**Experimento: descomponer ΔPnL en rellenos quitados (de G0), añadidos (efecto hueco) y conservados.**

| política | ΔPnL frente a G0 | quitados | añadidos | conservados | |
|---|---|---|---|---|---|
| GEO6, 10 días | +164,9 € [IC90 cierre +65,+264; alfa/4 +27,+299]; sin 2 mejores días +77,6; 9/10 días | 829, −203,8 €, EV −0,336 (descuento −0,124, información −0,225) | 83, −38,9 € | — | 87 % de los quitados estaban en/encima del bid |
| PG_O50, 7 días OOS | +199,3 € | 1.027, −206,3 €, EV −0,271 (información −0,203), positivos 1/7 días | 9, −7,0 € | 593, EV +0,302 (información +0,277) | — |

Lo que PG_O50 quita y GEO6 conserva son 600 rellenos:
- −112,8 €, EV −0,252, negativos en 6/7 días;
- 400 de ellos con T<150 (−80,4 €).

Por lado, la ΔPnL de PG_O50 es:
- NO: +161,5 €, positiva 7/7 días;
- YES: +44,9 €, positiva 6/7 días.

Tasa de rellenos quitados por lado: NO 66 % y YES 61 %. No es un veto al lado NO.

| H | mecanismo | resultado | estado |
|---|---|---|---|
| H-TOX-0 | nula: ruido / selección post hoc | la parte simple (GEO6) se sostiene 9/10 días con IC alfa/4 >0, pero la regla se eligió para resumir PG_O50 en los mismos días; el EV extra de PG_O50 (+0,28) depende de interacciones aprendidas en 7 días | abierta |
| H-TOX-1 | descuento de entrada (posición al rellenar) | K1: el descuento explica la diferencia, no la información | **refutada como filtro de AS** |
| H-TOX-2 | AS de colocación: armar cerca del precio, tarde o re-armar ⇒ relleno informado | ~75 % de lo que quitan PG/GEO es información (−0,20/−0,23) y ~25 % descuento | **sostenida (exploratoria)** |
| H-TOX-3 | artefacto de hueco | los añadidos restan (−38,9 / −7,0 €); toda la ΔPnL sale de quitar | **refutada** |
| H-TOX-4 | relleno BASE optimista en tamaño | capando q a min(q, sh_tx): G0 −0,063, armadas a <6c −0,311, armadas a ≥6c +0,066 | signo robusto; falta validar el realismo del relleno «rancio» |
| H-TOX-5 | régimen de dirección del periodo (el NO pierde 8/10 días en G0) | la ΔPnL es positiva en ambos lados y el 31-Oct (NO ≈0 en G0) da +36,9 en NO; pero 7 días no separan H-TOX-2 de H-TOX-5 en el EV extra | **no identificables** |

Para separar H-TOX-2 de H-TOX-5 hacen falta días forward en que el lado NO gane en G0: si la ΔPnL de PG sigue >0 en ellos, es colocación.

**Respuesta.** PG_O50 funciona, en días gastados, sobre todo como filtro de AS de colocación: no arma, o no re-arma, cuando el precio está a ≤5c de L o cuando quedan menos de ~150 s. No anticipa barridos: el S_nivel es positivo (+0,206) y no se evita. El rasgo «hazard de barrido» es solo un proxy de «el precio está cerca de mi nivel». La parte que supera a GEO6 no está identificada frente al régimen ni frente al sobreajuste.

## 3. P-C como filtro de AS y T1 con calma de 3 s (solo diseño; nada ejecutado, nada real)
**P-C en G0** (días gastados, descriptivo, `ana_tox4.log`):

| conjunto | n | EV | información | mk +1 s | mk +10 s | mk +60 s |
|---|---|---|---|---|---|---|
| H | 529 | −0,384 | −0,338 | −0,156 | −0,085 | +0,054 |
| C | 981 | −0,182 | −0,144 | −0,159 | −0,143 | +0,137 |

- La pérdida extra de H NO aparece en los markouts cortos: aparece al resolver. P-C es filtro de DIRECCIÓN, no de microestructura.
- Se apila con la geometría: H armada a <6c da −0,733 (n=186), H armada a ≥6c −0,196 (n=343).

**Diseño P-C** (añadido descriptivo al evaluador forward sin tocar PREREG_Q11_GIRO):
- reportar descuento, información y mk+1/+10/+60 s de H frente a C;
- etiqueta «filtro de AS» solo si mk+10 s(H) − mk+10 s(C) <0 con IC90 por cierre <0; si no, «filtro de dirección»;
- como filtro sigue haciendo falta /code-review + OK de Javi.

**T1 con calma de 3 s** = `esc_dec2` con `make_seg(lat_j=60, rearm=3000)`, variante `T1_r3000`.

Dosis-respuesta en días gastados (dec2, 10 días):

| variante | PnL | rellenos con salto ≤3 s que quedan |
|---|---|---|
| G0 | −166,9 € | 594, −128,9 € |
| T1_r0 | +53,1 € | — |
| T1 (1 s) | +75,9 € | 122, −19,1 € |
| T1_r2000 | +31,3 € | — |

- **El techo de la calma de 3 s sobre T1 es ≈ +19 € en 10 días a 5 acc.** La versión de 2 s ya pierde 44,6 € frente a T1.
- Prior: calma 3 s ≤ T1.

Prueba dry-run propuesta:
- variante extra en el forward de dec2 (lo implementa el execution-engineer si el chief lo aprueba; ~1 min de CPU al día);
- juez: ΔPnL pareada frente a T1 por cierre, ≥10 días desde la fecha de alta;
- acepta si ΔPnL >0 con IC90 por cierre >0, sin 2 mejores días >0, ≥6/10 días, y la misma variante con saltos desplazados (PLA) da Δ ≈0;
- refuta si Δ ≤0 a los 10 días.
- Valor de la información BAJO: recomiendo no priorizarla.

## 4. Economía (sin sumar solapes)
- **Validado:** 0 €.
- **Exploratorio** (días gastados, 5 acc por nivel):
  - GEO6 neutraliza la pérdida: −166,9 € → −2,7 € en 10 días, EV ≈0, no genera dinero;
  - PG_O50 da +129,5 € en 7 días (≈18 €/día). Es post hoc, no pasa alfa/8 y la retención histórica de estimaciones exploratorias al forward ha sido del 11-28 %.
- **Capacidad:** no medida (5 acc por token y nivel).
- **Contribución incremental:** sin estimar hasta el forward.

## 5. Siguiente paso y qué lo reabre
1. Forward de PG_O50 congelado frente a GEO6 y G0 (propuesta del alpha-miner). El RE pide añadir tres cosas al prerregistro, antes del 06-Nov y sin cambiar sus umbrales:
   - (a) descomposición quitados/añadidos: la ΔPnL debe venir de quitados con información <0;
   - (b) ΔPnL por lado y en los días en que el NO gana en G0 (control de régimen);
   - (c) markouts.
2. **Red-team:** atacar el realismo del relleno «rancio» (orden en L con el bid ya por debajo): ¿la orden real se habría rellenado ANTES, con el movimiento que bajó el bid? Si ese relleno temprano domina, la toxicidad de la colocación cercana podría estar mal fechada.
3. El caso se reabre con forward ≥10 días, con libro L2 (≈16-17-Nov) o con rellenos reales de una sonda.
