# B (H47-B real): pérdidas vistas por cartera y por tanda (22-Oct-2026, ~15:10Z)
Estado: **EXPLORATORY / sin palanca validada**. Solo lectura. No se ha tocado nada de B, del supervisor, de los crons ni de los procesos.
Datos: `posiciones_snapshot.csv`, copia de `contabilidad_wallet_dedicada/posiciones.csv` de las 14:20Z. Son 175 posiciones H47-B liquidadas con desenlace oficial (cobertura 178/178), en 23 tandas, entre el 20-Oct a las 11:40Z y el 22-Oct a las 12:05Z. Coste total 193,60 $, PnL −2,32 $, EV ponderado −0,012/€, PnL sin las 2 mejores posiciones −20,12 $.
Reglas fijadas antes de mirar las posiciones: `PREREG.md` (sha256 8af1de13…, `sha256sum -c PREREG.sha256` = OK). Lo que se añadió después va marcado como POST-HOC.

## 0. Conclusión en 5 líneas
1. **Corrijo la premisa.** No son «20 tandas que pierden el stake entero». Son **15 perdedoras (−58,08 $) y 8 ganadoras (+55,76 $)**, y el 65 % de tandas perdedoras es exactamente lo que da la mecánica de la tanda con EV≈0. En la simulación con e=0 pierden el 64,8 % de las tandas, la perdedora media deja −4,26 $ y la ganadora media +8,28 $; en lo observado, −3,87 $ y +6,97 $. **Con un edge real de +10 % seguirían perdiendo el 59 % de las tandas.** La tanda no sirve como unidad para juzgar a B.
2. **Ninguna regla de tanda o cartera aporta información con el segundo instrumento.** En B real, las rachas y la hora walk-forward «ganan» +28/+30 $, pero ninguna pasa Bonferroni. En el pseudo-B de población (12 días) las posiciones que quitan no son peores que las que dejan, y la de rachas y la de stop diario las quitan **mejores**.
3. **El drawdown es casi todo varianza de pago.** El observado, 30,6 $, coincide con la mediana i.i.d. con e=0 (30,5; p=0,50). Con un edge real de +10 % la mediana seguiría en 25-29 $. Lo evitable por deriva negativa es unos 2 $.
4. **El riesgo que de verdad está en la mesa es el de capital.** Quedan 5,12 $ sobre el suelo duro de 12 $. **P(llegar a las 500 pujas del gate) = 10-13 % con EV=0 y 18-22 % con +10 %.** Lo más probable es que B se pare hacia las 320 pujas. Hoy el suelo duro ya «corta pérdidas», pero también actúa como un kill que salta en falso el ~80 % de las veces aunque el edge sea real.
5. Cortar pérdidas «como sea» solo es posible bajando volumen, y eso baja también el PnL si el edge es real: los filtros quitan entre el 21 % y el 49 % del coste y se llevan esa misma fracción del edge. Si se quiere cortar pérdidas de verdad, la palanca es el EV (R2/R3 en el nicho, XRP), no la tanda.

## 1. Perfil de tandas perdedoras frente a ganadoras (`resultados.json::perdedoras/ganadoras/perfil_tandas`)
| | perdedoras (15) | ganadoras (8) |
|---|---|---|
| posiciones / por tanda | 92 / 6,1 | 83 / 10,4 |
| PnL | −58,08 $ | +55,76 $ |
| acierto (implícito por precio) | 10,9 % (21,7 %) | 32,5 % (21,5 %) |
| precio medio | 0,210 | 0,207 |
| monedas ETH/SOL/XRP | 36/30/26 | 32/27/24 |
| coste abierto máximo (media) | 3,69 $ | 3,91 $ |
| % de posiciones en un cierre compartido | 80 % | 78 % |
| primer relleno ganador | 3/15 | 4/8 |
| duración mediana | 18 min | 25,5 min |
| bloque 04-08 / 08-12 UTC (posiciones) | 9 / 61 | 31 / 26 |
- Precio, moneda, concurrencia y concentración salen **iguales**. Lo que cambia (acierto, número de posiciones, duración, primer relleno) es en parte tautológico, porque una tanda deja de perder cuando acierta, y en parte se debe a la barrera de ruina. **8 de las 15 perdedoras tienen 0 aciertos y se gastan los 5 $ en 2-3 cierres**: 3, 8, 11, 17, 19, 21, 22 y 23.
- **La única diferencia no mecánica es la hora.** En B real, 04-08 UTC dio +28,5 $ (40 posiciones; 21 y 22-Oct, los dos días positivos) y 08-12 UTC dio −35,0 $ (84 posiciones, los dos días negativos). En la población (12 días, 110.600 unidades) no se repite: 08-12 UTC tiene EV +0,047 y 04-08 UTC +0,028, y la diferencia de 08-12 frente al resto cambia de signo según el día (7 de 12 días positiva). Es compatible con que la dirección del día domine 2 días (trampa del ranking dominado por la dirección del día).
- **Correlación dentro del cierre (la clave de por qué las tandas mueren de golpe).** Hay 56 cierres con ≥2 posiciones, que suman 137 de las 175. La concordancia de resultado es **0,774 (p de permutación 0,0055)**, 97 de 106 pares van al mismo lado, y en 34 cierres pierden todas. B compra el lado barato de ETH, SOL y XRP en el mismo cierre, así que es **una sola apuesta direccional**: el n efectivo se parece más a 94 cierres que a 175 posiciones. Un presupuesto de 5 $ da para unas 2 de esas apuestas. Entre cierres consecutivos no hay memoria: autocorrelación lag-1 del EV por cierre +0,006 (p 0,41).
- Pago: acierto 21,1 %, ganancia media +4,10 $, pérdida media −1,12 $. Por día: 20-Oct +3,01 $ (EV +0,07), 21-Oct +13,01 $ (+0,166), 22-Oct −18,33 $ (−0,254).

## 2. Reglas de tope por tanda o día: efecto, placebo y falso disparo (`analisis_tandas.py` → `resultados.json`)
Δ = PnL de la regla − PnL actual (−2,32 $). IC90 por bootstrap de tandas. «info» = EV de lo que se queda − EV de lo que se quita: si vale ≈0, la regla solo reduce tamaño. Falso disparo medido con resultados sintéticos Bernoulli q = p·(1+e), 500 simulaciones por cada e.
| Regla | Δ B real $ (IC90 tandas) | mitades 1-12 / 13-23 | p placebo (Bonf ×11) | info en B | info pob. «primero» (IC90 por días, días+) | si edge real +0,10: % de veces que salta / coste quitado / ΔPnL esperado |
|---|---|---|---|---|---|---|
| R1a racha 5 → pausa 60 min | +30,1 (+16,3,+45,0) | +13,0 / +17,2 | 0,016 (0,18) | +0,78 | −0,009 (−0,025,+0,010), 3/12 | 100 % / 41 % / −7,0 $ (−36 % del edge) |
| R1b racha 8 | +28,3 (+12,9,+45,0) | +12,8 / +15,5 | 0,005 (0,055) | +0,75 | **−0,021 (−0,039,−0,002)**, 2/12 | 99 % / 21 % / −4,7 $ (−24 %) |
| R2a coste abierto ≤2 $ | +18,4 (−7,4,+42,6) | +14,7 / +3,7 | 0,15 | +0,36 | n/m | 100 % / 49 % / −10,3 $ |
| R2b coste abierto ≤3 $ | +19,3 (+3,6,+32,6) | +12,7 / +6,5 | 0,074 (0,81) | +0,58 | −0,012 (−0,044,+0,019), 6/12 | 100 % / 22 % / −4,5 $ |
| R3 una por cierre | +13,0 (−14,2,+38,7) | +6,8 / +6,1 | 0,23 | +0,25 | +0,009 (−0,024,+0,041), 8/12 | 100 % / 45 % / −8,7 $ |
| R4a stop diario −5 $ | +10,1 (−6,2,+26,0) | 0 / +10,1 | 0,20 | +0,42 | **−0,070 (−0,152,−0,009)**, 4/12 | 94 % / 44 % / −7,8 $ |
| R4b stop diario −10 $ | +6,2 (0,+15,8) | 0 / +6,2 | 0,24 | — | n/m | 73 % / 22 % / −4,4 $ |
| R5 saltar tanda tras 2 perdedoras | **−6,4** (−43,0,+19,1) | −15,9 / +9,5 | 0,74 | −0,19 | n/m | 95 % / 10 % / −1,3 $ |
| R6a moneda walk-forward | **−13,7** (−34,2,+4,2) | −7,2 / −6,5 | 0,19 | −0,71 | n/m | 97 % / 31 % / −5,5 $ |
| R6b bloque de 4 h walk-forward | +30,3 (+4,8,+54,9) | +3,3 / +27,0 | 0,006 (0,066) | +0,64 | +0,020 (−0,022,+0,061), 7/12 | 96 % / 23 % / −4,8 $ |
| R7 5 acciones por posición | −1,8 | −9,5 / +7,7 | — | — | — | quita el 2 % del coste (B ya está en el mínimo de 5 acc del exchange) |
- **Criterio fijado de antemano** (Δ>0, p<0,05/11, IC90 de tandas >0, las dos mitades >0 y coste ≤10 % del edge si es real): **no lo cumple ninguna regla.** Las tres que mejor salen in-sample (R1a, R1b, R6b) fallan Bonferroni. Además, el 79 % de la Δ de R6b es del 22-Oct (+23,8 $), y en el segundo instrumento ninguna tiene info positiva.
- **Segundo instrumento (POST-HOC, `pob_reglas.py`).** Es un pseudo-B montado con rellenos de otros makers de ETH/SOL/XRP 5m, del 09 al 20-Oct (12 días), con 300 réplicas y ~230 posiciones por día, desenlace oficial. En el modo «primero» se toma el relleno más temprano de cada mercado; su EV base es −0,10 a +0,11 según el día, cerca del de B real. En el modo «azar», con un relleno al azar, el EV base cae a −0,16. Ahí R2b y R3 parecen informativas (+0,06/+0,08), pero solo porque los rellenos tardíos de un mismo cierre son barridos. Con el modo «primero», que es el parecido a B, ese efecto desaparece. Las reglas de racha y el stop diario quitan posiciones **mejores** que la media: después de malas rachas se recupera.
- Las mejoras in-sample de B (+28/+30 $) salen de una secuencia de 3 días con un día malo (el 22-Oct, periodo C negativo en la población), y no de memoria de corto plazo (lag-1 ≈0). Es la misma trampa que el kill secuencial que mata en falso con edge real (CLAUDE.md): **todas saltan en el 73-100 % de los escenarios con un edge real de +10 %.**

## 3. Drawdown irreducible frente a evitable y capital (`resultados.json::drawdown`, `ruina.py`)
- **Drawdown máximo observado: 30,6 $** (curva por orden de resolución; peor tramo de 24 h −19,9 $).
  - i.i.d. con e=0: mediana 30,5 (P90 51,6), p(≥ obs) = 0,50.
  - Con e=−0,012: 32,3.
  - Con e=+0,10: 25,2.
  - Añadiendo la correlación por cierre (ρ=0,333, calibrado a la concordancia 0,774): e=0 → 34,5 (P90 59,8) y e=+0,10 → 29,0.
  - Permutar el orden real: mediana 31,6 (p 0,55). El orden de B no fue especialmente malo.
- **Reparto.** Unos 29 de los 30,6 $ (~95 %) existirían igual con un edge real de +10 %: es varianza de pago (21 % de acierto, +4,1/−1,1). Unos 2 $ se deben a la deriva negativa observada, y entre 5 y 6 $ es lo que quitaría tener +10 % de edge. La correlación por cierre añade unos 4 $ de mediana. Una posición por cierre lo baja a 22,5 $, pero a cambio de la mitad del volumen, así que el EV baja en la misma proporción. Es reducir tamaño, no un edge.
- **Capital y gate** (POST-HOC, `ruina_resultados.json`, `ruina_colchon.json`). Datos de partida:
  - La tanda 24 arrancó a las 14:38:56Z con saldo_base 17,12 y suelo 12,12.
  - Una rotación exige un saldo ≥ 17 (ROTACION_SALDO_DURO 12 + 5).
  - Hay 305 pujas hechas y faltan unas 114 posiciones hasta 500.

  Con las reglas reales de capital y la correlación por cierre:
  - **P(llegar a 500): 0,10-0,13 con e=0, 0,18-0,22 con e=+0,10 y 0,06-0,07 con e=−0,10.** La parada mediana cae hacia las 319-326 pujas.
  - Con una posición por cierre (variante): 0,17 con e=0 y 0,23 con +0,10.
  - Para P ≥ 0,8 con e=0 harían falta unos 45-50 $ de saldo, es decir, unos +30 $ (palanca de capital = **decisión de Javi**; el calendario no tiene recargas planificadas).
  - **Potencia del gate:** aunque se llegara a 500 pujas (~290 posiciones), la desviación típica del EV/€ es ~0,14. Con un edge real de +10 %, el EV observado sale >0 solo en el 77 % de los casos, y el IC90 excluye el 0 en ~20 %. **500 pujas no bastan para separar +10 % de 0.**

## 4. Palancas de cartera que propongo (ninguna es € validado; todas, como variante + /code-review + OK de Javi)
1. **Decidir ya qué pasa en el suelo duro (palanca de capital/gate, 0 $ de código).** B va a pararse por capital antes de 500 pujas con probabilidad 0,8-0,9, haya edge o no. El kill de capital que existe salta en falso ~80 % con +10 % real, así que el gate de 500 (H23, R3-en-B, XRP) no se va a evaluar con B real.
   - Opciones para Javi: (a) aceptar la parada hacia las 320 pujas y decidir con shadow/forward (R3 en el brazo shadow, población); (b) recargar ~30 $, aunque no está planificado; (c) bajar el gate a «lo que dé el capital» y declararlo como pérdida de potencia.
   - € netos: 0 en ganancia. Lo que se evita es una pérdida máxima adicional ≤5,12 $, que ya está acotada.
2. **Unidad de medida = cierre, no tanda (palanca de medición).** Los postmortems y gates de B deberían reportar el IC por cierre o por día. Con 175 posiciones el n efectivo ronda 94 cierres. Hay que dejar de leer «tandas perdidas» como señal: la mecánica las produce con cualquier EV entre −0,10 y +0,10. € netos: 0, pero evita decisiones malas como R5/R6a, que habrían costado −6,4 $ y −13,7 $.
3. **(Solo si se quiere menos riesgo a cambio de menos PnL) una posición por cierre o un coste abierto ≤3 $.** No mejora el EV (info en la población +0,009 y −0,012, IC90 incluye 0). Reduce la varianza: drawdown con e=0 de 34,5 a 22,5 $, P(llegar a 500) de 0,11 a 0,17. Con un edge real de +10 % cuesta ~45 % del PnL (−8,7 $ por cada 175 posiciones). € netos esperados: 0 si EV=0, negativo si el edge es real. Es una palanca de tamaño, no de edge.

## 5. Qué NO vale (con la medición)
- **Parar tras k pérdidas seguidas**, sea por posición (R1a/R1b) o por tanda (R5). Con k=5/8: in-sample +28/+30 $, pero Bonferroni 0,055-0,18, info en población −0,009/−0,021 (R1b con IC90 <0) y salta en el 99-100 % de los escenarios con edge real. R5 da −6,4 $.
- **Stop diario de −5/−10 $**: info en población −0,070 (IC90 −0,152,−0,009); quita días que luego se recuperan.
- **Pausar la moneda mala walk-forward** (−13,7 $ en B) y **la hora mala walk-forward** (+30 $ in-sample, 79 % de un solo día; población +0,020 sin significación; 08-12 UTC no es peor en la población).
- **Reducir tamaño por posición:** B ya está en el mínimo del exchange (5 acc, ~1,05 $); R7 no cambia nada (−1,8 $).
- Cualquier lectura de «pocas ganadoras grandes frente a muchas perdedoras de 5 $» como patrón: es la forma del pago con acierto del 21 %.

## 6. Límites y desviaciones declaradas
- 3 días y 23 tandas: ningún IC por días es posible en B real (por eso uso tandas y el segundo instrumento).
- Después del PREREG se añadieron, como POST-HOC: el placebo por bloques de cierre, Δ por día, autocorrelación, info, pseudo-B de población y ruina/capital. Las reglas no cambiaron. La familia real es de 11 reglas (el PREREG dice ×10; uso ×11, que es más conservador).
- `t_conocido = fin + 60 s` es conservador. R5 usa el resultado parcial que se conoce al empezar la tanda siguiente. R6 usa todas las posiciones conocidas (shadow) para no caer en un estado absorbente. En la población, R6b es intradía.
- El pseudo-B de población no reproduce la selección propia de B (cola, repegs) y sus días no se solapan con los de B salvo el 20-Oct. Sirve para efectos relativos (info), no para niveles. El fill por puja (0,585) y las pujas hechas (305) son aproximados, sacados del ledger.
- El simulador de ruina usa la plantilla temporal real de B en bucle y la regla de rotación de H47/supervisor tal como la leí (ROTACION_AUTOMATICA=False: la rotación la hace el chief, se modela como si siempre se rotara cuando se puede).

## 7. Reproducir (nice 19, ionice -c3, ulimit -v 2-2,5 GB; máx. ~4 min y <300 MB)
`python3 analisis_tandas.py --perm 2000 --sims 2000` → `resultados.json` · `python3 pob_reglas.py --rep 300 --modo primero|azar` → `pob_resultados_{modo}.json` · `python3 ruina.py` → `ruina_resultados.json` (el barrido de colchón → `ruina_colchon.json` se hizo en línea con `ruina.correr`). Hashes en `HASHES.txt` (`sha256sum -c HASHES.txt`).
