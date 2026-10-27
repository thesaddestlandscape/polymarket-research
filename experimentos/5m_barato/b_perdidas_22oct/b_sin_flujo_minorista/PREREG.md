# PREREG b_sin_flujo_minorista (25-Oct-2026 ~12:25Z) — EXPLORATORY (<=21 dias). Escrito ANTES de calcular nada por clase de tomador ni ningun replay.
Visto antes de escribir (declarado): contrapunto_informado/INFORME.md (B: DES+NUEVO 9,9 % vs 26,2 % esperado; INF 24 rellenos), b_vs_poblacion/INFORME.md,
y estadistica descriptiva del ledger de B (3.796 ordenes armadas 20-23 Oct, vida mediana 0,58 s, p90 2,8 s; 202 con relleno). B NO opero el 24 ni el 25-Oct
(ledger: solo mercado_inicio/fin) y no existe antes del 20-Oct: no hay mas dias de B que los 20-23 (23 parcial, desde 06:30Z).
## Datos
- Poblacion on-chain: f6 M/T 17-23 Oct (+ 24-Oct extraido con la MISMA logica e1_extrae) ; clase ex ante del tomador = contrapunto s1 (walk-forward D-7..D-1; INF/DES/MIX/NUEVO). 5m, ETH/SOL/XRP para B.
- B: experimento_h47_B_ledger.jsonl (puja_post = ARMADO; fuera_libro/intencion_cancel = CANCELACION; lectura/puja_fin = relleno con espera_s y cola). Desenlace oficial (misma cadena DES de s1).
- Alineacion de reloj: offset = mediana(U.ts on-chain - hora de deteccion del ledger) sobre los rellenos de B emparejados (slug, lado, precio, acc, |dT|<10 s); se aplica a todo el flujo.
## Preguntas y reglas de decision (fijadas)
Q1 persistencia: (a) fill-level 20-23: cuota € DES+NUEVO de B vs esperada (coin x dia x banda 0,05 de la poblacion) con IC90 por cierre (misma funcion que s3); (b) NUEVO, nivel de ARMADO: cuota DES+NUEVO del flujo (rellenos de OTROS) que cruza el nivel EXACTO (mkt, lado, precio) de cada orden armada de B durante su vida [t_arm, t_out], vs cuota poblacion del mismo coin x dia x banda. Persiste si obs-esp IC90 cierre < -0,05 en (a) y (b).
 Dias: contar dias de B (4) y los que faltan hasta 10 (6).
Q2 por relleno de B: espera (armado->relleno), vida de la orden, cola, T restante, clase del tomador, tamano de la casacion (acc de la tx del tomador / acc de B) y si agota el nivel; distribucion por clase INF vs DES+NUEVO; emparejado contra rellenos de la poblacion en el mismo (mkt, lado, nivel) +-60 s.
Q3 quien barre y cuanto tarda: cuantiles de espera, T restante, precio y tamano por clase (B: espera real; poblacion: T restante, precio, tamano, hueco al relleno previo en el mismo nivel).
Q4 mecanismo (se dice SI cumple): (M1 "vida corta") la tasa de llegada por segundo armado de flujo DES+NUEVO al nivel NO cae en la ventana de vida de B respecto a la ventana [t_arm, t_arm+X] extendida (X=12 s), es decir, el flujo DES+NUEVO llega mas tarde que la vida de B: cuota DES+NUEVO del flujo en (vida, 12 s] > cuota en [0, vida] con IC90 cierre > +0,03. (M2 "cola") share DES+NUEVO entre los rellenos de B bajo replay FIFO de la cola `cola` vs share del flujo total.
## Replay FIFO (simulador de relleno de B)
Orden de B en (mkt, lado, p) con cola Q (ledger, acciones por delante al postear). Flujo = rellenos de OTROS makers en ese mkt-lado-p con ts_corr in [t_arm, t_fin]; B se rellena cuando el acumulado de acciones >= Q (+ parcial, tamano 5). Los makers de delante que cancelan solo ayudan: Q es cota conservadora; se declara. VALIDACION obligatoria antes de usarlo: recall/precision frente a los 202 rellenos reales con la vida real; si el recall < 60 % o la precision < 60 %, el replay NO se usa para politicas (BLOCKED) y se reporta como tal.
## Politicas (todas con el mismo replay; sin tope de precio; orden por recepcion; rasgos solo hasta t_arm, nada de look-ahead; la cancelacion contrafactual solo usa tiempo)
 P1 hold: sustituir la cancelacion por min(vida real... ) -> la orden vive hasta X = 3, 6, 12 s tras armar (o T restante 60 s, o fin de mercado). No cancelar por repega.
 P2 late: solo armar si T restante en armado <= 150 s (descarta ordenes antes) con la vida real.
 P3 nivel top-1c: mismo armado pero un tick por debajo, cola = tamano del nivel en libro de puja_post (libro.bids), vida real y vida X=6.
 P4 placebo: las mismas politicas sobre ordenes de B barajadas entre cierres (permutacion de T/armado entre ordenes del mismo coin x dia, 1000 veces).
 Unidad de EV: orden armada (rellenos a EV por EUR ponderado) agrupados por CIERRE; IC90 bootstrap por cierre y por dia (4 dias = informativo); sin 2 mejores dias; BH-FDR sobre las 7 politicas x 2 medidas (EV y delta vs base).
 Gate de "politica con senal": delta EV vs base > 0 con IC90 cierre > 0, placebo p<0,05, sin 2 mejores dias > 0, replay validado, >= 3 de 4 dias con delta >= 0. Si no, "sin senal".
 Etiquetas: todo EXPLORATORY; EUR/ano = cota (EV por EUR * volumen diario de B * 365), nunca validado.
