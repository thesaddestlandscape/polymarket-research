# PREREG PSA v1 — «pata suelta activa» (idea Javi 25-Oct). Congelado ANTES de simular ningún día (25-Oct ~11:35Z)
## 0. Equivalencia que fija qué es nuevo (deducción, no dato)
En Polymarket el libro de YES y NO es espejo (CTF: YES+NO = 1 $; vender X a a ≡ pujar ¬X a 1−a; mismo nivel, misma cola; maker sin comisión, rebate 20 %).
Con X en inventario a coste c: (i) completar la pata con una puja ¬X a b ≤ 1−c−M, (ii) «salir vendiendo X a ≥ c+M» con un ask en reposo, son LA MISMA orden.
«Salir a coste» = M=0. «Salir por debajo» como tomador = vender al bid (REJECTED `salida/`, ≡ HT0/HTc `pares_huecos`). Valor de salir vs mantener en cada relleno
de la pata rezagada = PnL de ese relleno mantenido a resolución (1{¬X gana} − b). Por tanto completar → perseguir → salir ≥ coste es UNA familia: una puja en reposo
en la pata rezagada con margen M(t). Ya medido: M fijo 0,02/0,04/0,06 con escalera 4×50 acc (F7: −0,047/−0,038/−0,053), M 0-4c sobre rellenos de B (HM: −0,29..−0,36),
M≥2-10c tomador (HTc), cosechar v1/v2/v3 (todas <0). NUEVO aquí y nunca simulado: (a) clips de 5 acc con re-armado continuo en ambos lados (rotación, H39/H39b),
(b) tope de inventario |I|≤15 acc que retira el lado sobrante, (c) M que DECAE en el tiempo 0,02→0 (persecución hasta salir a coste), (d) congelar el lado sobrante en la fase de persecución.
## 1. Datos y universo
libro5 BTC 5m (`DL/rebate_ganadores_btc`, mismo muestreo 1/3 de mercados `fin//300 %3==0` y cargador que F7 f6_sim.py), días 18..23-Oct (los que existen). Desenlace oficial
`maker_ms_desenlaces_cache.json` + `des_23.json`. Libro y operaciones ordenados por hora de RECEPCIÓN (como F7). Días ≤21-Oct = EXPLORATORY; 22-23 = únicos >21-Oct.
Diseño y parámetros en BTC, fijados de antemano desde 0xf074/0x0ab0 (clip 5, |I| 14-17, banda 0,3-0,5→0,30-0,70) y F7 (M=0,02 = P2), SIN optimizar.
## 2. Política SM (máquina de estados por mercado; I = inv_lado − inv_contrario en acc)
Ventana: alta desde T=298 s; cancelación total en T=60 s; luego MANTENER a resolución. Latencias: alta 85 ms, cancelación 65 ms, re-armado 250 ms tras relleno.
- COTIZAR (|I|<5): clip 5 acc al touch del bid en cada lado si touch ∈ [0,30;0,70]; seguir el touch cada ≥1 s.
- COMPLETAR (pata rezagada, contrario ≥5 acc por delante): puja = min(touch, floor((1 − coste medio del contrario − M(t))·100)/100); reposición urgente ≥250 ms si el tope baja del touch; sin banda.
- TOPE: el lado sobrante deja de cotizar si I ≥ 15 acc.
- PERSEGUIR→SALIR A COSTE: M(t)=0,02 con T>150 s; lineal a 0 entre T=150 y 90 s; M=0 de T=90 a 60 s. Con T≤150 s el lado sobrante (I≥5) no añade.
- MANTENER: lo no emparejado a T=60 s se lleva a resolución.
Control C0 («mismas pujas sin gestión»): clips 5 acc ambos lados, misma banda/latencias, sin tope de precio, sin tope de inventario, sin decaimiento.
## 3. Instrumentos de relleno (no son variantes)
BASE = sim v2 de F7 (cola por proporción; trade-through rellena el resto). PES (pesimista, pedido) = solo rellena una operación que ATRAVIESA el nivel (p < precio).
OPT (cota optimista = cabeza de cola, como 0xf074) = al precio rellena sin cola delante.
## 4. Métricas
EV(+rebate)/€ ponderado por € (Σ(pnl+reb)/Σcoste), rebate 0,014·p(1−p)·acc; unidad = mercado (una vida por mercado; sin solapes); IC90 por día (t), bootstrap de
mercados, sin los 2 mejores días, días+, EV de días >21. Descomposición lock (AVG) / residuo / rebate; tasa de completado (acc emparejadas/acc), % mercados con residuo ≥5 acc;
EV de los rellenos de la pata rezagada por fase (M≥0,015 / 0<M<0,015 / M=0 = «salir a coste»), que es exactamente el valor de salir frente a mantener.
Señal ex ante SECUNDARIA (K=1, exploratoria): al entrar en desequilibrio, el touch del lado sobrante cayó ≥2c en los 5 s previos (barrido en contra) → EV y residuo por flag.
## 5. Criterio (fijado ahora)
Primaria: SM/BASE. ÉXITO solo si: EV>0 con IC90 por día inf>0, sin 2 mejores >0, SM−C0 por día IC90>0, PES ≥0, n≥40 mercados y ≥10 días de los que los >21-Oct
sostengan el signo; BH-FDR sobre {SM/BASE EV>0, SM−C0>0} a q=0,10. Con 6 días (4 EXPLORATORY) el éxito es IMPOSIBLE hoy: máximo PROMISING.
FALSADOR FUERTE: si SM/OPT (cabeza de cola) tiene EV ≤0 con IC90 por día sup <0 → REJECTED con independencia de la cola (si ni delante de todos gana, la cola no lo rescata).
Si OPT>0 y BASE/PES ≤0 → DATA_BLOCKED por cola (requiere F5 micro-órdenes, decisión de Javi).
## 6. Recursos
Un día por proceso, `nice -n 19 ionice -c3`, `ulimit -v 3000000`, fuera de 06-09Z, solo con load <16 y MemAvailable >2,5 GB y sin otro análisis pesado (regla misión §7).
Comando: `cd scripts && for d in 2026-10-18 … 2026-10-23; do (ulimit -v 3000000; nice -n 19 ionice -c3 python3 -I psa_sim.py $d SM,C0 > ../datos/log_$d.txt 2>&1); done; python3 -I psa_eval.py > ../datos/eval.txt`
