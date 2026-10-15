# ENCARGO (Javi 15-Oct-2026) — SUBESTRATEGIA PENDIENTE DE 5m: BTC5M-FV-LONGSHOT
# CERRAR LA HIPÓTESIS DE PARES LOW-LOW Y DESARROLLAR UN FILTRO DE VALOR JUSTO QUE SELECCIONE LONGSHOTS CON VENTAJA REAL

Copia íntegra del encargo (texto de Javi). Todo en dry-run.

Fecha de corte: 15 de octubre de 2026.

Objetivo: determinar si podemos construir una estrategia rentable en los mercados BTC Up/Down de 5 minutos de Polymarket seleccionando únicamente contratos cuyo valor esperado sea positivo después de costes. La estrategia debe aprovechar la investigación previa de 5m barato, los cambios del mercado de 15m y los resultados de FV V4, sin comprar automáticamente ambos lados ni asumir que un precio de 0,10 es una oportunidad.

El objetivo económico de largo plazo continúa siendo investigar una estrategia que pueda contribuir a generar 200.000 € netos anuales. Debes calcular qué sería necesario para acercarse a esa meta, pero no forzarla en los resultados.

Actúa como un equipo de investigación cuantitativa, microestructura, modelización probabilística, ejecución y auditoría estadística. Inspecciona el repositorio, reproduce las cifras, prueba hipótesis y produce resultados verificables.

Todas las estrategias permanecen en dry-run. No envíes órdenes con dinero real, no muevas fondos y no contrates infraestructura.

## 1. VEREDICTO PROVISIONAL: LA REGLA LOW-LOW SIN FILTRO NO HA DEMOSTRADO ALPHA
Los siguientes resultados se han comunicado en una evaluación de mercados de 5 minutos. Debes reproducirlos desde los datos originales y verificar sus denominadores, pero constituyen el punto de partida de la nueva misión.
- 287 de 290 mercados presentaron algún lado a un precio de 0,10 o inferior.
- Se comunicaron aproximadamente 125 pares completados en unas 1.440 ventanas.
- La frecuencia de pares observada fue de aproximadamente el 8,7 %.
- Se comunicaron 1.314 posiciones sin emparejar, ninguna ganadora en esa muestra.
- La primera entrada en contratos de precio 0,10 o inferior presentó un resultado de aproximadamente −0,13 € por euro invertido.
- La política de acumulación de pares presentó un resultado cercano a −0,197 € por mercado, frente a una estimación de −0,217 € por mercado usando la aproximación de q=0,087.

Estas cifras no deben aceptarse sin auditoría. En particular, verifica que los números de mercados, pares, entradas iniciales y posiciones individuales pertenecen al mismo universo y periodo.
La interpretación provisional es que comprar automáticamente un lado cuando cae a 0,10 y comprar el contrario si también alcanza ese precio no constituye una estrategia rentable por sí misma.
La frecuencia con la que un contrato pierde y su precio se aproxima a cero puede explicar que aparezcan muchos precios bajos sin que exista una oportunidad de compra.
No sigas optimizando el número de pares completados sin contabilizar el resultado de todas las primeras patas. La política completa, no los pares seleccionados retrospectivamente, es la unidad correcta de evaluación.
Si la auditoría confirma estas conclusiones, documenta la estrategia indiscriminada LOWLOW-PAIR como rechazada para el universo probado. No la reabras sin nueva información predictiva, un mecanismo sustancialmente distinto o evidencia de un error en la prueba anterior.
Esto no significa que todo el 5m barato carezca de valor. Significa que el precio bajo, por sí solo, no ha demostrado ser un predictor suficiente.

## 2. LA ECONOMÍA QUE DEBE GUIAR LA NUEVA ESTRATEGIA
Si se invierte un importe fijo S en un contrato comprado a precio p, el número aproximado de acciones es Q = S / p.
Si el contrato paga un dólar por acción cuando gana y cero cuando pierde, el beneficio esperado bruto de esa compra es EV = S (q/p − 1), donde q es la probabilidad real de que el contrato gane.
La condición simplificada de equilibrio, sin comisiones, es q > p.
Con comisiones y otros costes, calcula el punto de equilibrio exacto a partir de la estructura de tarifas aplicable al contrato y al tipo de orden.
Esta fórmula no autoriza a sustituir la probabilidad real por el precio de mercado ni a suponer que una señal predictiva está calibrada. La pregunta de investigación es precisamente si podemos estimar q con suficiente precisión antes de comprar.

### 2.1. El ejemplo de 0,10
Si una acción cuesta 0,10 y se invierte 1 €, ignorando temporalmente el cambio entre euros y dólares, se adquieren aproximadamente diez acciones.
Si gana, produce 10 € de pago bruto y 9 € de beneficio antes de costes. Si pierde, se pierde el euro invertido.
Por tanto, si la probabilidad real de ganar es del 8,7 %, el valor esperado bruto aproximado de esa posición sería EV = 1 (0,087/0,10 − 1) = −0,13 €.
Esto coincide con el resultado comunicado de −0,13 € por euro, aunque debes verificarlo con la muestra original y los costes reales.
La conclusión es que un multiplicador potencial elevado no implica un valor esperado positivo. Un longshot necesita acertar con la frecuencia suficiente para compensar el coste de todas las pérdidas.

### 2.2. Por qué la pareja puede empeorar el resultado
Bajo el ejemplo simplificado comunicado, la estrategia gasta un euro en la primera pata a 0,10 y compra una segunda pata por otro euro cuando el mercado alcanza una condición que permite completar el par.
Si la primera pata gana y la segunda es efectivamente la perdedora, el resultado total será aproximadamente +8 € antes de costes. Si la primera pierde y no se compra la segunda pata, el resultado será −1 €.
Si q es la probabilidad de que la primera pata gane bajo esas condiciones concretas: EV = 8q − (1 − q) = 9q − 1. El equilibrio se obtiene con q > 1/9 ≈ 11,11 %.
Con q = 8,7 %, el EV aproximado sería −0,217 € por mercado.
Esta es una representación simplificada de la política descrita, no una identidad universal para todas las estrategias de pares. Reproduce el proceso real de entradas y salidas y calcula el EV a partir de los fills y las resoluciones observadas.
No afirmes que la segunda pata siempre es perdedora por definición matemática. Verifica cuántas veces sucede en la muestra y si esa relación depende de la regla de entrada, del momento en que se compra la segunda pata o de cómo se clasifica un mercado como emparejado.
La nueva estrategia debe seleccionar contratos por su valor esperado individual y evaluar el efecto incremental de cualquier segunda compra. No debe comprar la segunda pata simplemente porque su precio también haya caído.

## 3. MISIÓN CENTRAL: DESARROLLAR Y VALIDAR FV V4
La prioridad es investigar FV V4 y determinar si puede estimar el valor justo de los contratos baratos con suficiente precisión para seleccionar aquellos que tienen una probabilidad de ganar superior a la implícita en el precio.
La descripción actual indica que FV V4 trabaja con valor justo a escalas temporales pequeñas y busca una ventaja respecto al precio de mercado, pero debes recuperar del repositorio la definición exacta, el código, los datos y los resultados originales.
No inventes su mecanismo ni lo sustituyas por otra versión más favorable.
Debes responder: ¿Qué variable estima FV V4? ¿Estima la probabilidad de resolución, un valor de contrato, un movimiento de precio futuro o un diferencial entre mercados? ¿Qué información utiliza? ¿En qué momento está disponible esa información? ¿Qué horizonte temporal predice? ¿Cómo se convierte su salida en una decisión de compra? ¿Cuál es su rendimiento neto con precios y costes reales? ¿Se mantiene la ventaja fuera de muestra? ¿Puede identificar contratos baratos cuya probabilidad real de ganar supera la probabilidad de equilibrio? ¿Aporta información incremental sobre el precio del contrato y las referencias de mercado existentes?
Si FV V4 no produce directamente una probabilidad calibrada de resolución, determina qué transformación o modelo de calibración necesita y cómo validarlo sin utilizar información futura.
No supongas que batir al mid significa obtener beneficio. La referencia operativa debe ser el precio realmente ejecutable y el coste total de la operación.

## 4. CONVERTIR EL VALOR JUSTO EN UNA REGLA DE ENTRADA
Construye una regla basada en la diferencia entre la probabilidad estimada de resolución y el precio ejecutable.
Si q_FV es una estimación calibrada de la probabilidad de ganar y p_ask es el precio ejecutable de compra, la decisión debe tener en cuenta: valor esperado bruto; comisiones; coste de ejecución; latencia; incertidumbre del modelo; margen de seguridad; tamaño realmente disponible.
Una regla simplificada de compra podría expresarse como q_FV > p_ask + c, donde c representa el coste efectivo por acción cuando la estructura de tarifas pueda expresarse así.
No utilices esta forma simplificada si las comisiones dependen de otras variables. En ese caso, calcula el EV neto exacto para cada operación propuesta.
La condición de entrada no debe ser simplemente: Comprar cualquier contrato cuyo ask sea inferior o igual a 0,10.
Debe ser una condición económicamente justificada, por ejemplo: Considerar contratos baratos dentro del rango permitido cuando su probabilidad estimada y calibrada de ganar produzca un EV neto suficientemente positivo después de costes y de incorporar la incertidumbre de la predicción.
El intervalo de 0,00–0,10 debe mantenerse como universo inicial de investigación. Si encuentras que la ventaja existe en otros precios, documenta ese descubrimiento como una variante separada. No modifiques el umbral original retrospectivamente para mejorar sus resultados.

## 5. ESTIMAR LA PROBABILIDAD REAL DE LOS LONGSHOTS
El problema no es identificar cuándo un contrato vale 0,10 según el mercado. Es averiguar si algunos contratos que cotizan a 0,10 tienen una probabilidad real de ganar superior al 10 % más los costes aplicables.
Investiga qué variables disponibles antes de la compra pueden mejorar la estimación: distancia del precio actual de BTC al umbral de resolución; tiempo restante del mercado; movimiento y velocidad recientes de BTC; volatilidad y reversión; relación entre el precio de BTC y el valor de referencia utilizado para resolver; evolución del contrato Up y del contrato Down; edad del ask barato; spread y profundidad; cambios en el libro; diferenciales entre las referencias de 5m y 15m; cambio del bid de 15m y sus posibles precursores; otros indicadores que puedan justificarse a partir de los datos existentes.
No asumas que estas variables tienen poder predictivo. Contrástalas.
Separa tres tipos de información:
- Variables de estado: describen las condiciones actuales del mercado.
- Predictores de resolución: estiman la probabilidad de que el contrato elegido gane al vencimiento.
- Predictores de ejecución: estiman si el precio y la cantidad seguirán disponibles cuando nuestra orden llegue.

Una señal puede predecir correctamente un movimiento de precio sin mejorar la probabilidad de resolución del contrato que se va a comprar. También puede predecir una probabilidad favorable y, aun así, perder el precio de entrada por latencia.
Evalúa ambos problemas por separado.

## 6. INVESTIGAR EL EFECTO DEL PRECIO, EL TIEMPO Y LA SELECCIÓN ADVERSA
Los contratos que caen a 0,10 suelen representar resultados a los que el mercado asigna una probabilidad baja. El momento en que alcanzan ese precio puede ser una condición adversa para su compra.
Debes comprobar si la entrada inmediatamente después de una caída del precio sufre selección adversa, si la probabilidad de remontada cambia con el tiempo restante y si los precios baratos reflejan correctamente la información que acaba de aparecer.
Para cada contrato candidato, registra: precio y tamaño del ask; precio inmediatamente anterior; magnitud y velocidad de la caída; tiempo restante; movimiento reciente de BTC; estado del mercado emparejado cuando exista; probabilidad FV estimada en el momento de decisión; resultado de resolución; precio y cantidad realmente comprados; PnL neto.
Compara, en una muestra común:
- Comprar indiscriminadamente a un ask de 0,10 o menos.
- Comprar solo cuando FV V4 supera el umbral de EV.
- Comprar con FV V4 más un margen de seguridad.
- Comprar con la señal de FV V4 y un filtro de ejecución.
- Comprar únicamente cuando exista un precursor verificable del cambio relevante de 15m, si esa variable aporta valor adicional.

No presupongas que un periodo de espera mejora la selección. Evalúa si esperar permite obtener mejor información o solo hace que desaparezca la oportunidad.

## 7. DECIDIR SI TIENE SENTIDO COMPRAR LA SEGUNDA PATA
La estrategia de acumulación de ambos lados no queda prohibida para siempre, pero deja de ser la regla principal de compra.
Si el modelo estima que una pata tiene EV negativo, no la compres solo para formar un par.
Para cualquier segunda compra, evalúa por separado: el precio ejecutable; la probabilidad estimada de ganar; el EV incremental de esa compra; las cantidades que ya están en inventario; el efecto sobre la exposición; los costes; la probabilidad de que el par se complete; el PnL de la política total si la segunda compra se omite.
La segunda pata solo debe incorporarse si la decisión tiene una justificación económica verificable. La mera etiqueta de «cobertura» no basta.
Compara, manteniendo el mismo periodo y el mismo universo:
- Estrategia de una sola pata seleccionada por FV.
- Estrategia que añade una segunda pata solo si su propio EV es positivo.
- Estrategia low-low indiscriminada como control de referencia.
- Estrategia de pares simultáneos cuando el coste conjunto ejecutable lo permita.

El control low-low debe conservarse en la evaluación para demostrar si la nueva regla mejora el resultado; no debe utilizarse como una estrategia candidata predeterminada si ya ha sido refutada.

## 8. NO CONFUNDIR 5M Y 15M
La evidencia de 5m indica que el longshot indiscriminado puede perder dinero. No extrapoles automáticamente sus tasas de acierto, frecuencia de entradas, profundidad o EV a BTC 15m.
La investigación dedicada a 15m continúa siendo independiente.
Utiliza este encargo para desarrollar y validar la selección de longshots de BTC 5m. Si quieres evaluar si el mecanismo puede trasladarse a 15m, crea un análisis separado, con sus propios denominadores, precios, tiempos, calibración y validación cronológica.
No combines las muestras de ambos timeframes para aumentar el tamaño aparente de la muestra.

## 9. AUDITAR LOS DATOS Y LOS RESULTADOS PREVIOS
Antes de programar una nueva versión, recupera del repositorio: código y configuración de FV V4; hashes de los experimentos; datos de libro, trades y timestamps; reglas de resolución; resultados del longshot de primera compra; resultados de la estrategia low-low; resultados por mercado y por jornada; costes y comisiones; definiciones de EV y ROI; experimentos de anticipación del cambio de 15m; código y métricas de las puertas de validación anteriores.
Reproduce las cifras de 287/290 mercados, 125 pares, 1.314 posiciones sin emparejar, −0,13 €/€ de la primera compra y −0,197 € por mercado.
Verifica que: los periodos coinciden; las operaciones se clasifican de manera consistente; los denominadores son correctos; los mercados no se duplican; los pares pertenecen al mismo evento de resolución; el cálculo del PnL incluye todos los costes; no se ha utilizado información futura para seleccionar las entradas.
Si las cifras no se reproducen, documenta qué cambia y por qué.

## 10. RECONSTRUIR EL VALOR JUSTO Y SU CALIBRACIÓN
Si FV V4 genera estimaciones de probabilidad, mide si están calibradas.
Agrupa las operaciones por intervalos de probabilidad estimada y compara las probabilidades predichas con las frecuencias empíricas de resolución.
Utiliza suficientes observaciones por grupo y evita presentar como fiable un segmento con muy pocos casos.
Calcula, cuando los datos lo permitan: curvas de calibración; error de calibración; Brier score; log loss; discriminación entre ganadores y perdedores; EV neto por intervalos de probabilidad; resultados por precio de entrada; resultados por tiempo restante; sensibilidad al coste de ejecución.
No elijas el modelo únicamente por una métrica predictiva genérica. La cuestión relevante es si la calibración mejora la decisión de compra y el resultado neto.
Un modelo puede discriminar correctamente entre contratos y, aun así, estar mal calibrado. Para calcular el valor esperado necesitas una estimación de probabilidad fiable o límites conservadores que compensen su incertidumbre.
Si FV V4 no produce una probabilidad calibrada, propone el método más sencillo que pueda hacerlo y compáralo con la versión original.
No añadas complejidad si no mejora de manera reproducible la rentabilidad fuera de muestra.

## 11. VALIDACIÓN CRONOLÓGICA Y CONTROLES
Divide la muestra en periodos cronológicos de descubrimiento, calibración, validación y evaluación final fuera de muestra.
Congela las reglas antes del periodo confirmatorio.
Si una variable se descubre mirando los resultados, sus resultados históricos son exploratorios. No los presentes como evidencia de que predice la resolución.
Para cada variante compara: número de señales; número de compras ejecutables; precio medio; probabilidad estimada; frecuencia de acierto; EV neto; PnL total; drawdown; capital comprometido; concentración del beneficio; resultado excluyendo el mejor día y las mejores operaciones; resultado por activo o periodo, cuando exista suficiente información.
Utiliza inferencia compatible con la dependencia entre mercados y ventanas próximas. No asumas que todos los resultados de BTC son estadísticamente independientes.
Los datos deben permitir reproducir no solo los mercados ganadores, sino también los contratos comprados que terminaron perdiendo.

## 12. OBJETIVO ECONÓMICO: 200.000 € NETOS ANUALES
Mantén el objetivo aspiracional, pero cuantifica si puede alcanzarse.
Calcula cuántas compras con EV neto positivo serían necesarias, el margen neto medio requerido, la frecuencia de oportunidades, el capital comprometido y el coste de ejecución.
Distingue entre: EV por euro arriesgado; EV por operación; PnL diario; ROI sobre capital comprometido; capacidad de ejecución; rentabilidad anual proyectada.
No extrapoles unos pocos días a un año completo ni multipliques mecánicamente el EV para conseguir 200.000 €.
Presenta escenarios conservador, base y optimista con supuestos explícitos y sensibilidad a una caída de la tasa de acierto.
Si el objetivo no es viable con la frecuencia, el capital, la liquidez o la incertidumbre disponibles, dilo claramente.

## 13. IMPLEMENTACIÓN EXPERIMENTAL
Si FV V4 o un filtro alternativo justifica continuar, desarrolla una versión nueva e independiente de las estrategias existentes.
Puede denominarse provisionalmente BTC5M-FV-LONGSHOT.
Debe incluir: datos utilizados por la señal; probabilidad estimada o valor justo; precio ejecutable; cálculo de EV neto; margen de seguridad; condición de entrada; restricciones de exposición; registro de señales rechazadas y aceptadas; resultado de resolución; PnL neto; hash de versión; tests y reproducción de resultados.
No sobrescribas V4 ni cambies sus resultados originales.
La nueva implementación debe impedir: entradas basadas en información futura; compras duplicadas; ejecuciones simuladas a precios no disponibles; omisión de operaciones perdedoras; mezcla de mercados diferentes; alteraciones retrospectivas de los umbrales; contabilidad doble de las posiciones o sus pagos.
Todas las pruebas continúan en dry-run.

## 14. FORMATO DEL INFORME FINAL
Empieza con un veredicto ejecutivo.
- A. ¿Queda refutada la regla low-low sin filtro? Reproduce los resultados y especifica el universo y las condiciones bajo los que queda rechazada.
- B. ¿Qué aporta realmente FV V4? Explica el mecanismo, la variable estimada, su calibración y su rendimiento neto con precios ejecutables.
- C. ¿Podemos identificar longshots con EV positivo? Presenta las tasas de acierto por precio y probabilidad estimada, la incertidumbre y la diferencia respecto al precio de equilibrio.
- D. ¿Cuál es la regla de entrada propuesta? Define las condiciones necesarias para que la probabilidad estimada supere el coste total y exista suficiente margen de seguridad.
- E. ¿Merece la pena comprar una segunda pata? Demuestra si aporta valor incremental o si simplemente resta rentabilidad a una entrada de una sola pata con EV positivo.
- F. ¿El resultado sobrevive fuera de muestra? Muestra PnL neto, EV, drawdown, concentración, costes y comparaciones con la regla low-low original.
- G. ¿Es económicamente escalable? Presenta frecuencia, profundidad, capital comprometido y escenarios respecto al objetivo de 200.000 € anuales.
- H. ¿Qué debemos hacer a continuación? Elige una sola prioridad de investigación y justifícala con evidencia.
- I. ¿Cómo se reproduce el análisis? Entrega rutas exactas, código, hashes, comandos, tests, tablas y fuentes.

## 15. CRITERIO DE ÉXITO
La misión solo se considera completada cuando: la estrategia low-low indiscriminada ha sido auditada y su estado está documentado; FV V4 ha sido reproducido y evaluado con métricas económicas correctas; se ha probado si puede identificar longshots cuya probabilidad real de resolución supera su precio más los costes; la señal utiliza únicamente información disponible antes de la compra; el resultado neto es positivo en una evaluación cronológica independiente, o la hipótesis se rechaza por falta de evidencia; se sabe si una segunda pata aporta valor incremental; el riesgo y la capacidad económica están cuantificados; el objetivo anual de 200.000 € se ha evaluado honestamente, sin extrapolaciones injustificadas.
No compres el contrato porque sea barato. Cómpralo únicamente cuando exista evidencia de que su probabilidad real de ganar supera suficientemente el precio que pagas y todos los costes de ejecutarlo. La nueva estrategia debe convertir el valor justo en una decisión económicamente defendible.

---
## NOTAS DE AUDITORÍA YA CONOCIDAS (Claude, 15-Oct, antes de empezar)
- Universo de la exploración: BTC 5m, 10-14 Oct, registro ms (top del libro por recepción), desenlace oficial. Cuadran: 287+288+288+288+288 = 1.439 mercados con algún lado ≤0,10; pares 27+27+24+26+21 = 125; sueltas 260+261+264+262+267 = 1.314. 287/290 es SOLO el 14-Oct (un día), no los 5.
- El −0,13 €/€ de "primera compra" que cité NO es de este universo: es el longshot de primera compra de wallets del 30-Sep (otro estudio). En ESTE universo la política "solo 1ª pata" dio −255,6 € en 1.439 mercados = −0,178 €/mercado = −0,178 €/€ (1 € por mercado). Corregir en el informe.
- "La suelta siempre pierde por construcción" lo dije demasiado fuerte: vale si el perdedor siempre cae a ≤0,10 antes del cierre, lo que es casi siempre pero no una identidad (mercados que resuelven con el perdedor por encima de 0,10, ask vacío al final). Verificar con los datos, como pide §2.2.
- FV v4 (`analisis_5m_barato_fv_modelo_v4.py`, commit f7dfd42f67) predice el CAMBIO DEL MID a 0,5/1/3 s, no la probabilidad de resolución: para este encargo hay que añadir el puente FV → q calibrada.
