# Expediente RE-THRU1: toxicidad del relleno «thru1» en la escalera G (06-Nov-2026, cheap5m-reverse-engineer)
**Estado de cierre: PARTIALLY_SOLVED (exploratorio).** Bloqueo dominante: F (selección adversa durante la vida de la orden). Secundarios: B (modelo de relleno BASE sin calibrar), G (días quemados, post hoc, multiplicidad) y E (latencia de cancelación). Validado: 0 €.
Código y datos: `experimentos/5m_barato/q11/toxicidad_thru1/`.
- Diseño escrito antes de calcular: `DISENO_T.md`, sha 36e49c0c…a404.
- Scripts: `passT.py`, `anaT.py` y `anaT2.py` (este último post-resultado, no prerregistrado).
- Logs: `out/passT.log`, `out/anaT.log`, `out/anaT2.log`; hashes en `HASHES.txt`.
- Corrió a partir de las 09:16Z con nice 19, ionice 3 y ulimit 3 GB: 10-21 s/día, pico de 1,0 GB.

Los addenda y prerregistros de RE-Q11 no se han tocado. Desviación respecto al diseño: CXJ, además de cancelar, no arma 3 s después de un salto (fijado antes de ejecutar y aplicado a CXJ150 y CXJ1000 por igual). El informe pedido en `misiones/5m_barato/informes/` queda fuera de mis rutas de escritura, así que el contenido va aquí.

## 1. Reproducción y relojes
- G0 sale exacto: 2.938 rellenos, −166,9 €, EV −0,076, 10 días (26-Oct..04-Nov).
- thru1: n 2.321, EV −0,125, −218 €. Reproduce el −0,123 (n 2.308) de Q11.
- GEO6 aquí usa el bid a t−300 ms (C5d usaba t): da −26,9 € frente a −2,7 €.
- Todos los rasgos se toman a t_dec−300 ms. Binance usa reloj de recepción c[7]. El rasgo NaN no predice nada: solo 1 relleno con r3 NaN.
- 31-Oct y 01-Nov tienen el ~80 % de los ticks de Binance perdidos, así que la detección de saltos esos días está degradada.
- Unidad: cierre (fin). EV ponderado por €, no relleno = 0, población completa con reposición.

## 2. Descomposición por segmento de G0 (10 días)

| bid−L en t−300 | segmentos | P(relleno) | EV\|relleno [IC90 del pnl por cierre] | €/segmento | EV\|thru1 |
|---|---|---|---|---|---|
| <2c | 1.703 | 0,295 | −0,321 (−195, −42 €) | −0,071 | −0,393 |
| 2-4c | 757 | 0,267 | −0,214 (−69, +9) | −0,042 | −0,143 |
| 4-6c | 857 | 0,235 | −0,414 (−91, −29) | −0,072 | −0,418 |
| 6-8c | 819 | 0,225 | −0,214 (−64, +8) | −0,035 | −0,253 |
| ≥8c | 26.662 | 0,069 | +0,055 (−175, +335) | +0,003 | −0,007 |

Por factor:
- Salto adverso de Binance ≥3 bps en los 3 s previos al armado: EV\|thru1 −0,331 (n 215 rellenos), frente a −0,111 en calma.
- Lado: NO −0,261, YES +0,123 (régimen, como ya vio el red-team).
- Monedas: SOL −0,172, XRP −0,085, ETH −0,008.

Hecho: thru1 solo es tóxico cuando L está a menos de 8c del bid. Con L a ≥8c, thru1 ≈ 0.

## 3. Hipótesis (familia primaria de 4, alfa/4)

| hipótesis | ΔPnL frente a G0, 10 d [IC90 por cierre] [IC97,5] | OOS 01-04 Nov | EV absoluto / sin 2 mejores días | veredicto |
|---|---|---|---|---|
| H-GEO (GEO6) | +140 (+44, +226) (+9, +253), 9/10 días | +31,5 (−16, +73), 3/4 | −0,016 / −0,116 | INSUFFICIENT: la Δ es robusta y pasa alfa/4, pero es post hoc y sin EV absoluto >0 |
| H-JUMP (NJ3A, solo no armar) | +2,5 (−16, +18); placebo p 0,65 | +6,5 (+2,7, +11,1); placebo p 0,05 | −0,076 | INSUFFICIENT con efecto ≈ nulo (quita el 1 % de los rellenos) |
| H-CALM (CALM3) | +40,9 (−58, +133) | +9,2 (−53, +56) | −0,069 | INSUFFICIENT |
| H-LAT (CXB300: cancelar al caer el bid bajo L) | +198,5 (−18, +408); placebo p 0,167 (es el mínimo con 5 semillas) | +19,9 (−85, +123) | +0,043 / −0,103 | INSUFFICIENT. Cancela el 97 %. El modelo BASE no simula la carrera contra el tomador cuando somos el mejor bid: no identificable sin L2 o micro-real |
| H0 (ruido / no explotable) | — | — | — | no refutada para EV absoluto |

Secundario, no prerregistrado como primario y sin placebo: **CXJ150** (cancelar 150 ms después de un salto adverso de Binance ≥3 bps en 1 s y no rearmar en 3 s).
- 10 d: ΔPnL +128 (+52, +203), IC97,5 (+20, +225), 9/10 días.
- TRAIN: +79, 6/6 días.
- OOS: +48,9 (+15, +81), 3/4 días.
- Por moneda: SOL +73 (+35, +110), XRP +46 (+0, +85), ETH +9 (−34, +45).
- Por lado: NO +95 (+37, +148), YES +33 (−22, +82).
- Los rellenos que quita tienen EV −0,281 (n 597; 463 son thru1).
- EV absoluto −0,020 en 10 d. **Latencia:** CXJ150 − CXJ1000 = +54 (+20, +85), 8/10 días.

Clasificación: EXPLORATORY, candidato para forward.

## 4. Respuesta a la pregunta
- **EVITAR (no colocar):** L a menos de 8c del bid en t−300 ms (−0,035 a −0,072 €/segmento).
- **PROTEGER (mantener):**
  - con L ≥8c y sin salto: EV ≈ 0;
  - durante la vida de la orden, cancelar al primer salto adverso de Binance: es lo que quita el thru1 tóxico; no armar después del salto no basta.
- **Reducir latencia:** sí, solo para la cancelación por Binance. A 150 ms frente a 1 s vale unos +54 € en 10 días con 5 acciones. La curva CXB baja de forma monótona en los 10 días (220/199/161/152), pero no OOS.

Ninguna variante tiene EV absoluto >0 robusto: lo que hay es reducción de pérdida.

## 5. Refutación pendiente (crítica)
1. **Cota CROSS de CXJ150:** si el ask toca L antes de salto+150 ms, la cancelación pierde la carrera. Esto no está medido.
2. Placebo de CXJ con las horas de salto desplazadas.
3. CXJ se eligió entre 12 variantes: corregir por multiplicidad.
4. El 81 % de la Δ viene del lado NO: posible régimen.
5. Fiabilidad del grabador de Binance (huecos 31-Oct y 01-Nov).

## 6. Siguiente paso y qué reabriría el caso
- Congelar `PREREG_Q11_THRU1_FWD_BORRADOR.md` tras revisión del validador. Brazos: PG_O50, GEO6, CXJ150, PC_AS frente a G0; cotas BASE/CROSS; días desde el 07-Nov.
- execution-engineer: evaluador forward más las cotas CROSS y el placebo de CXJ sobre los días quemados.
- L2 (16-17 Nov) o micro-real: medir P(relleno | ask toca L) para cerrar H-LAT.

Reabriría H-JUMP como filtro de colocación: un rasgo de L2 o del perp que anticipe saltos a ≥300 ms.
