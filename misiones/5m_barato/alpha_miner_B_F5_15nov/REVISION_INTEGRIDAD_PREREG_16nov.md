# REVISION_INTEGRIDAD_PREREG_16nov (measurement_id BF5-REPLAY-COLOC-v1) - polymarket-data-integrity-authority
Solo lectura. Verificado: existen L2/paquete_l/paquete_l.py y los ledger.jsonl/cancel_evid de B3. Prereg sellado no editado: los cambios van como ADDENDUM con sha propio antes de computar.
Estado global: AMBER (exploratorio, techo PROMISING). Etapa 0 puede arrancar al aplicar los cambios; Etapas 2-3 BLOQUEADAS hasta ADDENDUM + ADD3 completo.

| Punto | Veredicto | Motivo / cambio exigido |
|---|---|---|
| B-1 | APROBADO CON CAMBIOS | >=50 % de mercados retenidos es razonable (la regla literal dejaria 4 dias). Exigir: lista de dias validos fijada en Etapa 0 ANTES de cualquier EV; misma regla en motor y poblacion; hole60 obligatorio como sensibilidad; cobertura y %retenido publicados por dia y moneda; la censura por hora mala es por reloj, no por resultado (declararlo). |
| B-2 | APROBADO CON CAMBIOS | Pool de 313 incluye BTC (126) y el universo es ETH/SOL/XRP: anadir sensibilidad con pool sin BTC (n=188). Reproduccion exacta de n/p10/p50/p90 de los 3 informe_final.json como puerta; si falla, l=46 fija y se declara. Etiquetar que son 1 dia y 2,2 h y solo LO; d_proc=3 es supuesto. |
| B-3 | APROBADO CON CAMBIOS | Aceptado el criterio LO-puro (0 hi, indet<=5 %) para variantes con A diario. Cambios: dia con indet>20 % sale de tablas por clase pero tambien del conteo de >=10 dias LO de G-INT (no se rellena); dias mixtos (hi/lo) solo por segmento, nunca fusionados; la clase se mide por ventana (no por fecha) y la primera ventana del dia es indet. |
| B-4 | APROBADO CON CAMBIOS | h_m (IC90 de la media por dias) es una vara demasiado estrecha para comparar UNA celda dia x moneda: infla P-NO. Usar el error propio de la celda: incompatible si |Delta| > 1,645*sqrt(se_mot^2+se_pob^2), con se por bootstrap por CIERRE dentro de la celda (B=10000). Mantener >=30 rellenos y >=100 prints, y publicar la tasa de incompatibilidad tambien con h_m como sensibilidad. Declarar que motor(5 acc., cola) y poblacion(prints) siguen siendo objetos distintos: P-NO no prueba nada sobre B real. |
| B-5 | APROBADO CON CAMBIOS (placebos) | Con 100 placebos p_min=0,0099: pasa Bonferroni 0,0125 pero NO puede pasar el primer rango de BH con 18 contrastes (umbral 0,10/18=0,0056). Exigir >=1000 placebos por variante en la pasada final (p_min 0,001); permitido cribar con 100 y re-ejecutar con 1000 placebos NUEVOS (semilla distinta) solo las que tengan p<=0,05, declarado de antemano. Familias y K quedan como estan; K de P=4 y 18 secundarios, sin anadir variantes. |
| B-6 | APROBADO | ulimit -v 6 GB (excepcion autorizada), guardia MemAvailable>=5,5 GB x3 lecturas, corte <2,5 GB o RSS>3,6 GB, un dia cada vez, ADD3 primero, fuera de 06:00-09:30Z, choom +500. Anadir: si el semaforo cron_pesado "corre igualmente" tras 10 min, la guardia propia prevalece (abortar, no esperar). |

## Pregunta de Javi: Etapa 1 (A=68, CX sin tiempo, 20 placebos)
Tiene razon en lo de fondo. Veredicto: SALTAR la Etapa 1 como evidencia y como criterio de prioridad.
- Latencia: CX/SEGT se generaron con A=68 y fin +60 ms (constantes congeladas, no vigentes). Para X (cancelacion) la latencia es el mecanismo mismo: medir CXB con l=60 supuesto no dice nada de l vigente. Para el reparto por distancia al bid (kt) el sesgo es menor pero sigue siendo un P(fill) calculado con cola y llegada no vigentes.
- Tiempo/clase: la tabla A de CX no lleva t_dec; solo existe G0 incondicional por dia. SEGT si trae t_dec (clase causal posible) pero solo de G0, no de X/F.
- Potencia: 20 placebos dan p_min=1/21=0,048 > 0,0125; no pueden dar ni un solo p significativo.
- Prioridad: §7.1 solo decide el ORDEN de P2 dentro de la Etapa 2, y la Etapa 2 calcula todo en una pasada por dia (§8.1). El orden no cambia coste ni decision: Etapa 1 no informa ninguna decision.
- Mantener lo que no depende de esas constantes: Etapa 0 (identidades, dias validos, clase) y Q-C (§7.3), que usa delta vigente MIX y las 3.796 ordenes reales. Etapa 1 reducida = Etapa 0 + Q-C.
Que hace falta para que las limitaciones desaparezcan: (1) copia paridad-exacta del motor (A=68, l=60, 26-29 Oct) y luego parametrizada A=38, l=MIX; (2) guardar CADA segmento con t_dec, t_arr, t_end, clase causal, rama de sello (ya en §8.1); (3) placebos >=1000 por variante (cribar 100, confirmar 1000 nuevos; p_min 0,001) frente a 20 de CX; con 1000 BH de 18 contrastes (rango 1 = 0,0056) y Bonferroni 0,0125 son alcanzables (>=79 minimo teorico para 0,0125, >=179 para 0,0056). Es decir: la Etapa 2 ES la regeneracion; no hay forma barata de arreglar los pkl existentes.
Reordenacion propuesta (ADDENDUM, no editar el sellado): Etapa 0 -> Q-C -> (ADD3 completo) -> paridad -> Etapa 2 -> 3. Eliminar §7.1/§8.4 como etapa previa (T1 sale de la pasada con SIZE parametrizado) y retirar "variantes ya calculadas (regresion)" de §8 excepto como control de paridad.

## Pendientes no resueltos
- Poblacion sin sesgo de censura: mantener P(fill) x rho x EV|fill en toda tabla (§5.2 OK; contrafactual no ocurrido = 0 declarado).
- Sin clase HI: sigue DATA_BLOCKED; anclas HI no usadas (decision de Javi).
- Siguiente prueba mas pequena: Etapa 0 (<5 min CPU) + reproduccion de n/p10/p50/p90 de paquete_l.
