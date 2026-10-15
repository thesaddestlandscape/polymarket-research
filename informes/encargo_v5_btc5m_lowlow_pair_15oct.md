# ENCARGO (Javi 15-Oct-2026) — PENDIENTE, "para ver después"
# DISEÑAR Y VALIDAR UNA ESTRATEGIA DE BTC 5M QUE COMPRE UP Y DOWN ENTRE 0,00 Y 0,10, CON 1 € POR LADO, BUSQUE PARES RENTABLES Y EVALÚE UNA META DE 200.000 € NETOS ANUALES

Copia íntegra del encargo (texto de Javi). Nombre provisional de la variante: **V5-BTC5M-LOWLOW-PAIR**. Todo en dry-run.

Fecha de referencia: 15 de octubre de 2026.
Objetivo principal: desarrollar, investigar y validar una nueva estrategia para los mercados Bitcoin Up/Down de 5 minutos de Polymarket. La estrategia debe comprar ambos lados cuando sus precios de entrada se encuentren en el rango de 0,00 a 0,10 dólares por acción, comprometiendo como máximo 1 € por lado y manteniendo las posiciones hasta la resolución.
La hipótesis económica consiste en comprar ambas patas a precios suficientemente bajos para que el pago de la pata ganadora pueda compensar la pérdida de la perdedora y generar beneficio neto.
La meta aspiracional es alcanzar 200.000 € netos anuales. No debes asumir que esa meta es posible ni manipular los criterios de evaluación para conseguirla. Tu misión consiste en determinar si el mecanismo tiene una ventaja real, desarrollar la mejor implementación técnicamente defendible y cuantificar su capacidad económica.
Trabaja como un equipo de investigación cuantitativa, microestructura, ejecución, análisis on-chain, gestión de inventario y auditoría financiera.
No entregues únicamente una propuesta conceptual o un backtest superficial. Inspecciona el repositorio, recupera datos, reconstruye operaciones, ejecuta simulaciones y proporciona artefactos reproducibles.
Todas las pruebas serán en dry-run. No envíes órdenes con dinero real, no muevas fondos ni contrates infraestructura.

## 1. ESPECIFICACIÓN INICIAL DE LA ESTRATEGIA
Desarrolla una estrategia específica para los mercados de BTC Up/Down de 5 minutos.
La regla inicial es deliberadamente simple.

### 1.1. Mercado
Opera únicamente en mercados de Bitcoin Up/Down a 5 minutos para la versión inicial. No mezcles ETH, SOL, DOGE, BNB u otros activos en la evaluación principal.
La estrategia debe identificar exactamente el mercado, sus dos contratos, sus reglas de resolución y el momento de cierre.
Comprueba las reglas efectivas de liquidación aplicables a cada mercado histórico.
No emparejes posiciones pertenecientes a ventanas distintas, aunque sean consecutivas, ni combines contratos de 5m y 15m como si garantizasen un pago conjunto.

### 1.2. Entrada en ambos lados
Para cada mercado de BTC 5m existen dos lados:
- Up: el contrato que paga si se cumple la condición de subida definida por el mercado.
- Down: el contrato que paga si se cumple la condición de bajada definida por el mercado.

La estrategia debe observar de forma continua los precios ejecutables de ambos contratos.
Regla de entrada para cada lado:
- Comprar Up si su precio de compra ejecutable está entre 0,00 y 0,10 dólares por acción.
- Comprar Down si su precio de compra ejecutable está entre 0,00 y 0,10 dólares por acción.
- Comprometer un máximo de 1 € de capital de entrada en Up por mercado.
- Comprometer un máximo de 1 € de capital de entrada en Down por mercado.
- Hacer como máximo una asignación inicial de 1 € por lado en cada mercado para la versión base.
- Mantener las posiciones adquiridas hasta la resolución oficial.
- No vender anticipadamente en la versión base.
- No aumentar automáticamente el stake después de una pérdida.
- No seguir comprando indefinidamente el mismo lado.
- No comprometer más de 2 € por mercado en las dos entradas iniciales, sin contar las variaciones derivadas de la conversión de moneda y los costes que deben contabilizarse por separado.

El precio mínimo ejecutable no debe darse por supuesto como cero. Determina el tick mínimo, la liquidez, las restricciones del mercado y los tamaños mínimos vigentes. Si el precio de 0,00 no es ejecutable, utiliza los precios reales permitidos y documenta el límite.
El rango 0,00–0,10 es la regla inicial que debes evaluar, no un resultado que debas modificar silenciosamente para mejorar el backtest.

### 1.3. Definición del stake
El stake de 1 € significa capital invertido, no una cantidad fija de acciones.
Si una asignación de 1 € se ejecuta a un precio de p, calcula el número de acciones a partir del importe realmente convertido a la moneda de negociación y del precio de ejecución: Q = S / p, donde S es el stake expresado en la moneda de negociación, p el precio realmente pagado por acción y Q el número de acciones adquiridas.
Si la operativa utiliza USDC u otra moneda, convierte el stake de euros usando el tipo de cambio pertinente y registra explícitamente ese cambio. No supongas que 1 € equivale siempre a 1 USDC.
Incluye las comisiones, el redondeo, la liquidez, las ejecuciones parciales y las restricciones de cantidad.
No intentes dividir por cero. Si el precio observado es cero o redondea a cero, comprueba si se trata de una cotización real ejecutable, un artefacto de representación o falta de liquidez.

### 1.4. Una pata puede ejecutarse sin que la otra llegue a hacerlo
El algoritmo debe tratar las compras de Up y Down como decisiones cronológicas independientes. No puede presuponer que, porque un lado haya cotizado por debajo de 0,10, el contrario también llegará a ese rango.
Si se compra una primera pata y la segunda nunca alcanza el intervalo de entrada, la posición inicial se mantiene hasta resolución en la versión base y su resultado se contabiliza íntegramente.
No elimines esos mercados de las estadísticas.
No contabilices únicamente los mercados en los que ambos lados llegaron a comprarse: hacerlo sin incluir el coste y el resultado de las primeras patas no emparejadas produciría un backtest sesgado.
Esta condición es esencial. La estrategia debe demostrar rentabilidad como política completa de entrada y mantenimiento, no únicamente como suma de pares seleccionados retrospectivamente.

## 2. LA HIPÓTESIS ECONÓMICA
Investiga si comprar las dos patas a precios de hasta 0,10 dólares por acción proporciona un beneficio neto suficientemente elevado para compensar: el coste de ambas compras; las comisiones; el riesgo de las patas que no llegan a emparejarse; la disponibilidad real de liquidez; las ejecuciones parciales; la latencia; la competencia por el nivel de precio; la dependencia de eventos excepcionales; los costes operativos.
Para una pareja formada por una acción Up y otra Down del mismo mercado binario, si ambas acciones están correctamente emparejadas, una de ellas paga un dólar a la resolución y la otra cero.
Si cada pata se adquirió con un stake S, a precios p_U y p_D, la cantidad de acciones de cada lado es, de forma simplificada: Q_U = S / p_U, Q_D = S / p_D.
Sin costes y suponiendo una resolución binaria normal, el pago final del par completo es Q_U si gana Up y Q_D si gana Down. El coste conjunto es 2S.
Si ambas compras se producen a precios no superiores a 0,10 dólares por acción, la pareja completa tiene, bajo esas condiciones, un pago bruto mínimo de diez veces el stake de la pata ganadora. Esto supone un margen bruto mínimo equivalente a ocho veces un stake de 1 € por par completo, antes de costes, moneda y diferencias de ejecución.
Debes verificar la aritmética, la unidad monetaria, los precios reales, los pagos y las comisiones. No conviertas este límite teórico del par completo en una previsión de rentabilidad de la estrategia.
La estrategia necesita explicar qué sucede con todos los mercados donde no logra construir ambas patas, cuánto tardan los pares en completarse y qué porcentaje de las entradas termina expuesto a resolución sin cobertura.

## 3. EL OBJETIVO DE 200.000 € NETOS ANUALES
El objetivo de largo plazo es producir una estrategia con capacidad potencial para generar 200.000 € netos anuales.
Debes trabajar hacia ese objetivo, pero no puedes darlo por alcanzado ni utilizarlo como criterio para elegir parámetros retrospectivamente.
Como punto de partida, calcula: cuántos pares completos al año serían necesarios; cuántos pares completos al día exigiría cada escenario; qué margen neto medio debería aportar cada par; cuántas primeras patas quedarían sin emparejar; cuánto capital estaría comprometido simultáneamente; cuántas ventanas de BTC 5m existen y cuántas oportunidades reales aparecen; qué frecuencia de pares completos sería necesaria respecto al total de ventanas; cuál sería el efecto de comisiones y de la ejecución parcial; qué parte de los beneficios procedería de posiciones individuales ganadoras; qué parte procedería de pares realmente completados.
Haz los cálculos bajo varios supuestos de beneficio neto por par y de pérdidas en patas no emparejadas. No utilices únicamente el margen mínimo teórico.
Distingue tres magnitudes:
- Beneficio neto por par completo: resultado de las dos patas realmente ejecutadas, después de costes.
- Beneficio neto por mercado: resultado incluyendo todas las operaciones del mercado, las posiciones no emparejadas, las comisiones y los pagos oficiales.
- Beneficio neto de la estrategia: resultado agregado de todos los mercados, incluyendo los periodos sin oportunidades y la exposición total.

Calcula escenarios conservador, base y optimista, indicando qué evidencia respalda sus supuestos.
Para la meta anual, presenta tanto el equivalente sobre 365 días como el correspondiente a 260 días operativos. No extrapoles una muestra de pocos días como si representase un año completo.
Define el término «neto» de forma explícita: comisiones, pérdidas, deslizamiento y costes operativos deben estar incluidos; los gastos de infraestructura y la fiscalidad deben presentarse por separado cuando no puedan estimarse con fiabilidad.
Si el objetivo de 200.000 € anuales no resulta plausible con un stake de 1 € por lado y una frecuencia realista de oportunidades, dilo claramente. No aumentes el stake para forzar la meta.

## 4. RECONSTRUIR LA EVIDENCIA DISPONIBLE DE 5M
La nueva estrategia debe aprovechar todo lo aprendido en la investigación de 5m barato, sin asumir que los mecanismos son idénticos.

### 4.1. Estrategia existente V4
La referencia existente es V4, con hash comunicado: 77a75859ae5cf22e
Su objetivo es detectar valor relativo entre mercados de 5m y 15m con cierres coincidentes. La regla comunicada es: bid15(s) - ask5(s) - commission >= 0.05
La implementación real, la referencia de precios, la regla de señal y los costes deben comprobarse en el repositorio.
No sobrescribas V4. No cambies sus parámetros ni combines sus resultados con la nueva estrategia.

### 4.2. Hallazgo de los 82 ms
Se reconstruyeron 62 consumos con compradores identificados:
| Categoría | Casos comunicados |
|---|---|
| Solo 5m, sin actividad de caja identificada | 37 |
| Actividad de caja en el mismo bloque | 11 |
| Actividad de caja con el 15m después, hasta 60 s | 5 |
| Actividad de caja con el 15m antes, hasta 30 s | 3 |
| Otros | 6 |

El total comunicado es de 62. Verifica la clasificación original y sus definiciones.
La explicación prioritaria de la anomalía temporal es que el evento relevante puede ser un cambio del bid de 15m mientras el ask barato de 5m ya estaba publicado.
Las medianas comunicadas son: recepción de ese cambio por nuestro feed ≈ 42 ms desde el evento del exchange; operación ajena ≈ 97 ms después de nuestra recepción; desaparición o cambio del ask barato ≈ 174 ms después de nuestra recepción.
Estos datos deben reproducirse y sus bases temporales deben ser compatibles antes de utilizarse como parámetros de una estrategia.

### 4.3. Vía de cancelación cerrada
La investigación anterior determinó que el exchange rechaza explícitamente cancelar determinadas órdenes retenidas por el retraso del tomador. Un caso excepcional de cancelación efectiva no proporcionó una solución útil.
Considera cerrada esa vía para el diseño inicial. No desarrolles una estrategia cuya rentabilidad dependa de cancelar con éxito esas órdenes.

### 4.4. Vía de anticipación del cambio de 15m
La vía de investigación abierta busca predecir el cambio del bid de 15m antes de su publicación para que una orden llegue al ask barato de 5m antes de su desaparición.
Esta hipótesis puede resultar relevante para mejorar la entrada en los mercados de 5m, pero no debe convertirse en una condición obligatoria de la estrategia nueva sin comprobar que aporta valor incremental.
La estrategia principal de este encargo es comprar ambos lados a precios bajos. Debes comparar si funciona: sin utilizar información de 15m; utilizando un precursor del cambio del bid de 15m; utilizando la señal original de valor relativo de V4 como filtro experimental.
Estas son variantes comparativas separadas. No combines sus resultados sin un análisis que permita atribuir el beneficio a cada componente.

## 5. EVALUAR DOS FORMAS DE EJECUTAR LAS COMPRAS
La regla de precio no determina por sí sola el método de ejecución. La investigación debe comparar distintas rutas, manteniendo la misma política de exposición de 1 € por lado.

### Variante A: compra reactiva al ask
El sistema detecta que el ask ejecutable de Up o Down ha entrado en el intervalo de 0,00–0,10 y envía una orden de compra.
Simula la ejecución después de la latencia realista, utilizando el precio y la cantidad disponibles al llegar.
Incluye: tiempo de recepción del feed; procesamiento; decisión; envío; retardo del tomador; precio y cantidad disponibles a la llegada; comisiones; ejecuciones parciales.
No supongas que una oportunidad detectada sigue disponible en el momento de la compra.

### Variante B: órdenes límite previamente colocadas
Investiga si tiene sentido mantener órdenes límite de compra preparadas para ambos lados a precios del intervalo 0,00–0,10, de modo que puedan ejecutarse cuando llegue flujo vendedor al nivel pertinente.
Esta variante es especialmente relevante porque la investigación anterior apunta a que algunos precios favorables desaparecen rápidamente. Una orden ya colocada podría reducir la dependencia de reaccionar después de observar el cambio.
No des por hecho que una orden pasiva será ejecutada simplemente porque el precio haya tocado su nivel.
Debes reconstruir o estimar, de forma conservadora: prioridad en cola; probabilidad de ejecución; cantidad ejecutable; tiempo de permanencia; cancelaciones y modificaciones; selección adversa; costes y posibles rebates; riesgo de que solo se ejecute una pata; diferencia entre el precio límite y el precio medio realmente ejecutado.
La asignación total por lado debe seguir limitada a 1 € por mercado en la comparación base. Si pruebas escalones de precios, distribuye ese presupuesto entre los niveles; no concedas un stake adicional de 1 € por cada nivel.

### Variante C: híbrida
Solo si las dos primeras variantes justifican una comparación adicional, estudia una solución que combine órdenes límite previas con compras reactivas.
La estrategia no debe aumentar automáticamente su exposición al detectar que la primera pata está abierta.
No utilices una orden reactiva para completar un par si el precio disponible hace que la operación deje de satisfacer los criterios de rentabilidad y riesgo.
Mantén las variantes separadas y documenta cuál ofrece el mejor resultado fuera de muestra.

## 6. DISEÑAR LA REGLA OPERATIVA COMPLETA
La estrategia no puede quedarse en «compra cuando el precio baja a 0,10».
Debes diseñar una política explícita de decisiones que contemple los estados de cada mercado.
Como mínimo, registra y distingue: mercado sin compras; solo Up comprado; solo Down comprado; ambos lados comprados; una o ambas órdenes parcialmente ejecutadas; mercado resuelto; mercado invalidado o con un resultado que requiera tratamiento especial.
Para cada estado, especifica qué acciones permite la estrategia y qué acciones prohíbe.
La regla base debe respetar: BTC 5m exclusivamente; precio de entrada dentro del intervalo definido; stake inicial máximo de 1 € por lado; máximo de una asignación inicial por lado y mercado; no vender anticipadamente en la versión base; no aumentar el stake para recuperar una pérdida; no duplicar compras por mensajes repetidos; no mezclar inventario de mercados diferentes; no contar como ejecutada una orden que solo haya generado una señal; mantener un ledger completo de las posiciones abiertas.
Evita la lógica retrospectiva. La estrategia debe tomar decisiones usando solamente los datos disponibles en el momento correspondiente.

### 6.1. Comportamiento cuando se compra una sola pata
Esta condición debe modelarse de manera explícita.
Si la primera compra se ejecuta y el lado contrario nunca alcanza el rango de entrada, el sistema conserva la primera posición hasta la resolución, según la política base.
Si la primera pata pierde, su coste debe aparecer como pérdida. Si gana, contabiliza el pago y los costes reales.
No excluyas estas operaciones del cálculo de rentabilidad, ni supongas que podrás venderlas sin pérdidas.
Si propones una variante con una salida defensiva, preséntala como una estrategia diferente y evalúala con precios realmente disponibles, costes y las reglas vigentes. No cambies la política base para mejorar el resultado retrospectivo.

## 7. RECONSTRUIR LOS PARES Y EL PNL SIN SESGOS
Para cada mercado, crea un ledger cronológico con: timestamp de cada señal; timestamp de cada orden simulada; precio solicitado; precio y cantidad realmente ejecutables al llegar; precio medio y cantidad de cada fill; capital invertido en Up; capital invertido en Down; cantidad de acciones adquiridas en cada lado; comisiones; inventario residual; resolución oficial; pago final; PnL neto por mercado.
Calcula Q_par = min(Q_U, Q_D), donde Q_U y Q_D son las cantidades de acciones compradas en Up y Down del mismo mercado.
Esta cantidad representa la máxima cantidad emparejable. No significa que el resto de la cartera deje de tener exposición.
La contabilidad final debe reconciliar los costes de todas las compras, las cantidades que realmente pagan a la resolución y cualquier otro coste atribuible.
No calcules el beneficio de los pares por separado y luego vuelvas a sumar sus pagos completos en el PnL del mercado. Eso produciría doble contabilización.
Presenta por separado: PnL de mercados con ambas patas ejecutadas; PnL de mercados con una sola pata; PnL de pares completos, neto de costes atribuibles; PnL de la estrategia completa incluyendo todas las compras; capital máximo comprometido; exposición residual máxima; drawdown; cantidad de posiciones abiertas antes de resolver.
La cifra principal para determinar la viabilidad es el PnL neto de todas las operaciones de la política completa.

## 8. BACKTEST Y SIMULACIÓN REALISTA
Construye un backtest cronológico de BTC 5m. No reconstruyas parejas únicamente a partir de precios históricos que parecen favorables.
La simulación debe avanzar en orden temporal y decidir en cada momento: si el precio ejecutable de uno de los lados ha entrado en el rango definido; si ya existe una compra de ese lado en el mercado; si queda presupuesto disponible para ese lado; qué tipo de orden se enviaría; cuándo llegaría la orden; si se ejecutaría completa o parcialmente; qué precio medio pagaría; qué inventario quedaría después del fill; si posteriormente se ejecuta la otra pata; qué PnL produce la resolución final.
No utilices el precio mínimo de una vela de 5 minutos como si se pudiera comprar automáticamente a ese nivel. Los datos de OHLC no bastan para reconstruir la ejecución.
Prioriza, en este orden: datos de libro y operaciones con timestamps suficientes; reconstrucción basada en el libro y en el retraso realista; datos agregados como exploración preliminar, indicando expresamente sus limitaciones.
Si faltan datos de profundidad o de orden de los eventos, no inventes la ejecución.

### 8.1. Tratamiento de órdenes y latencia
La variante reactiva debe simular el retraso real del tomador. La investigación previa estimó unos 150 ms de retraso, pero debes verificar su definición, distribución y aplicabilidad a la ruta concreta.
La simulación de órdenes límite debe tener en cuenta la permanencia, la competencia y la probabilidad realista de ejecución.
No asumas que la variante pasiva es automáticamente superior ni que la variante reactiva es inútil en todos los mercados.
Compara ambas utilizando el mismo conjunto de mercados y las mismas reglas de stake.

### 8.2. Validación temporal
Divide la muestra cronológicamente en: descubrimiento; ajuste de parámetros; validación; evaluación final fuera de muestra; posterior evaluación prospectiva en dry-run.
No utilices una partición aleatoria que permita que datos futuros influyan en las decisiones pasadas.
Congela la estrategia y sus parámetros antes del periodo confirmatorio.
Si modificas el umbral, el número de compras o la política de ejecución después de ver resultados, crea una nueva variante y evalúala en datos independientes.

## 9. PRUEBAS DE ROBUSTEZ Y COMPARACIONES OBLIGATORIAS
Evalúa la estrategia original con el intervalo 0,00–0,10 y stake de 1 € por lado.
Después, realiza un análisis de sensibilidad en rangos cercanos, sin sustituir la prueba original ni presentar el umbral que mejor resulte retrospectivamente como si hubiera sido la regla inicial.
Los controles deberán determinar: qué ocurre si solo se compra Up cuando está barato; qué ocurre si solo se compra Down cuando está barato; qué ocurre si se compran ambos lados cuando cada uno alcanza la condición; qué ocurre con las órdenes límite previamente colocadas; qué ocurre con la ejecución reactiva; qué valor incremental aporta una señal basada en el cambio del bid de 15m; qué valor incremental aporta la señal original de V4; si la estrategia funciona en mercados donde no se activa ninguna señal de V4; qué sucede cuando solo se ejecuta una pata; qué sucede cuando ambas patas se ejecutan a precios muy diferentes dentro del rango; cómo varía el resultado según la hora, la volatilidad, la profundidad y el spread.
No mezcles todas las variantes en un único resultado agregado.
Para cada candidata informa de número de mercados, compras, pares completados, posiciones no emparejadas, PnL neto, costes y capital comprometido.

### 9.1. Concentración
Presenta resultados: totales; por jornada; por ventana; excluyendo el mejor día; excluyendo las mejores operaciones; excluyendo el 5 % de mejores resultados, si la muestra lo permite; separando mercados con pares completos y mercados con una única pata; separando la versión reactiva y la pasiva.
Estas exclusiones son pruebas de sensibilidad. No reemplazan el resultado principal de la estrategia.
No presentes una estrategia como robusta si depende completamente de unos pocos episodios de volatilidad extrema.

## 10. INVESTIGACIÓN DE CARTERAS GANADORAS
Utiliza como referencias de investigación los participantes y resultados que ya hemos observado, sin asumir que conocemos con certeza sus estrategias.
Entre las carteras mencionadas en la investigación de 5m barato están: 0x9783f45c, con PnL comunicado de aproximadamente +18.600 dólares; 0x6515bf17, con PnL comunicado de aproximadamente +4.200 dólares.
También se ha comunicado una estrategia atribuida al perfil mo-money, que aparentemente acumula ambos lados de mercados de BTC 5m a lo largo del tiempo.
Debes comprobar si alguno de esos participantes utiliza un mecanismo compatible con la estrategia nueva. No asumas que operan igual ni que el PnL comunicado pertenece exclusivamente a BTC 5m.
Reconstruye, cuando las fuentes lo permitan: si compran ambos lados del mismo mercado; si lo hacen simultáneamente o de forma secuencial; los precios medios de entrada; las cantidades; la frecuencia con que completan pares; el inventario sin emparejar; el resultado de la resolución; su exposición direccional residual; las comisiones y otros ingresos identificables; la concentración del resultado en determinados mercados.
El propósito es comprender mecanismos públicos y patrones de mercado, no copiar operaciones a ciegas.
Utiliza cualquier información de carteras únicamente como evidencia descriptiva o predictiva. Una estrategia nuestra debe utilizar datos y decisiones disponibles antes de su propia entrada, no depender de observar una compra ajena después de que se haya ejecutado.

## 11. DETERMINAR SI ESTA ESTRATEGIA PERTENECE A 5M BARATO O A 5M GENERAL
La nueva familia de acumulación de ambos lados puede compartir parte del mecanismo de 5m barato o ser independiente.
No tomes esa decisión por similitud de nombres.
Compara:
- Versión A: BTC 5m general. Compra cada lado cuando el precio ejecutable entra en el rango definido, independientemente de que exista una señal de 15m o V4.
- Versión B: BTC 5m barato con filtro 15m. Utiliza el mismo stake y la misma regla de entrada, pero exige una condición identificada previamente en la relación entre 5m y 15m.
- Versión C: BTC 5m con anticipación del cambio del bid de 15m. Utiliza una señal precursora cuando haya evidencia de que puede mejorar el timing de la entrada.

Evalúa las tres variantes sobre un conjunto comparable de mercados.
Determina si el filtro de 15m: aumenta la proporción de oportunidades completadas; reduce las pérdidas de las primeras patas que quedan sin emparejar; mejora el precio medio; aumenta el EV neto por mercado; reduce las oportunidades, pero aumenta el beneficio por operación; no aporta valor incremental; introduce retraso o elimina oportunidades rentables.
El resultado determinará si debes clasificarla como: una extensión de 5m barato; una nueva estrategia independiente de BTC 5m; una hipótesis prometedora que todavía no se puede clasificar; una estrategia que debe descartarse.

## 12. IMPLEMENTACIÓN EXPERIMENTAL Y REGISTRO CONTABLE
Si la evidencia justifica una implementación, crea un proyecto o rama experimental independiente. Puedes utilizar provisionalmente el nombre: V5-BTC5M-LOWLOW-PAIR
No sobrescribas V4 ni utilices este nombre para una variante que no implemente realmente la regla descrita.
La implementación debe incorporar: identificación inequívoca de cada mercado; monitorización de los dos lados; validación de precio y tick; conversión explícita de moneda; stake máximo de 1 € por lado y mercado; prevención de compras duplicadas; gestión del inventario y de las posiciones no emparejadas; registro de la señal, decisión, orden virtual, ejecución simulada y resolución; cálculo de comisiones; PnL por mercado y total; capital comprometido y exposición residual; registro de errores de datos y de ejecución.
Incluye pruebas automáticas para comprobar que: una misma señal no genera varias compras accidentales; no se supera el presupuesto de 1 € por lado y mercado; los contratos emparejados corresponden al mismo mercado y resolución; los precios fuera del rango no generan entradas; un mercado sin segunda pata conserva el coste y el resultado de la primera; los pagos de resolución se contabilizan una sola vez; el PnL se reconcilia con el ledger de operaciones; las órdenes simuladas respetan la latencia y la profundidad disponible.
Todas las operaciones deben permanecer simuladas.

## 13. SEGURIDAD Y LÍMITES DE LA INVESTIGACIÓN
No envíes órdenes reales. No firmes transacciones. No muevas fondos. No habilites ejecución en producción. No compres un VPS ni contrates servicios. No aumentes los stakes para alcanzar el objetivo anual. No utilices martingalas ni incrementos de tamaño tras las pérdidas. No confundas una compra simulada con una ejecución confirmada. No ocultes las posiciones que no se emparejan. No modifiques retrospectivamente los parámetros para mejorar las métricas. No presentes estimaciones teóricas como beneficios futuros garantizados.
Puedes inspeccionar el repositorio, reconstruir datos, programar simulaciones, ejecutar pruebas y crear una versión experimental separada.
Si falta información, explica qué no puede verificarse y qué conclusión queda limitada. Continúa con las pruebas que sí sean posibles.

## 14. FORMATO DEL INFORME FINAL
Empieza por una conclusión ejecutiva inequívoca.
- A. ¿Es matemáticamente consistente la estrategia? Explica cómo se forma el beneficio de una pareja completa comprada a precios no superiores a 0,10 dólares por acción. Distingue el margen teórico de pares completos del resultado real de toda la estrategia.
- B. ¿Cuántas oportunidades existen realmente? Presenta la frecuencia con la que ambos lados de un mercado llegan a comprarse dentro del rango, cuántas veces solo se ejecuta una pata y cuánto tiempo se tarda en completar pares.
- C. ¿Qué método de ejecución funciona mejor? Compara compra reactiva, órdenes límite previamente colocadas y, si está justificado, una versión híbrida. Incluye ejecuciones, costes, profundidad, latencia y PnL neto.
- D. ¿Cuál es el PnL completo? Incluye todos los mercados, las posiciones no emparejadas, las pérdidas y los costes. No filtres mercados por haber completado un par.
- E. ¿Qué estrategia proporciona el mejor resultado fuera de muestra? Compara la regla base 0,00–0,10 con las variantes experimentales, utilizando los mismos mercados y las mismas condiciones de validación.
- F. ¿Qué aporta 15m? Determina si el uso del bid de 15m, de V4 o de un precursor del cambio de 15m aporta valor incremental.
- G. ¿Es viable alcanzar 200.000 € netos anuales? Presenta los números necesarios, la capacidad real, la frecuencia de oportunidades, los costes, la exposición, el riesgo y la incertidumbre. Si no es viable con un stake fijo de 1 € por lado, dilo. No modifiques el stake para fabricar una respuesta favorable.
- H. ¿Cuál es la siguiente decisión? Elige una única prioridad: continuar en dry-run, rediseñar una regla concreta, abrir una estrategia independiente de 5m general o abandonar la hipótesis. Justifica la decisión con la evidencia.
- I. ¿Cómo se reproduce? Entrega las rutas exactas de los archivos, hashes, comandos, tests, tablas y datos derivados necesarios para reproducir el análisis.

## 15. CRITERIO FINAL DE ÉXITO
Esta misión no se considera completada por obtener un backtest positivo de los pares que llegaron a completarse.
Debe demostrar, con un proceso cronológico reproducible: que la regla compra ambos lados únicamente cuando el precio ejecutable se encuentra en el intervalo definido; que el stake total no supera 1 € por lado y mercado en la versión base; que los pares completos producen el margen esperado después de costes; que las posiciones no emparejadas se contabilizan íntegramente; que el método de ejecución es realista con las condiciones del mercado; que la rentabilidad total de la política completa es positiva fuera de muestra; que el resultado no depende de excluir pérdidas, de unas pocas operaciones excepcionales o de precios imposibles de ejecutar; que se conoce el volumen de pares completos y el capital necesario para alcanzar distintos objetivos; que existe o no una ruta cuantitativamente defendible hacia 200.000 € netos anuales.
Diseña la mejor estrategia posible para esta regla concreta, pero deja que los datos decidan si funciona y cuánto puede ganar. La prioridad es demostrar un alpha ejecutable, no prometer una rentabilidad anual.
