# VALIDACIÓN INDEPENDIENTE de INFORME_V2 (26-Oct-2026 ~18:35Z, cheap5m-statistical-validator). Veredicto: **VALIDADO CON RESERVAS**. Validado: 0 €.
Método: reimplementación propia sin importar v2lib (scratchpad `val/{ext.sh,rep.py,met.py,capag.py}`), extracción en 2 pasadas desde `m5_registro_D`, verdad on-chain `ordenes_b.parquet`/`onchain_fills_D`. sha256 de PREREG_V2 y de los 11 ficheros de HASHES_V2.txt: OK.

## 1. Bug de extracción
- e0 actual correcto: q/t de los mercados de B, extracción independiente vs `mk_D` = 0 filas perdidas y 0 de más los 4 días (q 747.218/1.880.281/2.475.135/422.824; t 5.547/12.337/15.374/2.798; 20..23-Oct). 100 % de tokens de B con fila k y complementario (0 sin comp). La versión con el bug no se conserva: arreglo verificado, el bug no.
- Feed de prints vs on-chain (mercados de B): 15.374/15.598 casados (98,6 %) el 22-Oct y 2.798/2.802 el 23-Oct. Dedup del complementario: marca 2-13 prints/día; sin dedup no cambia nada (recall 0,839, precisión 0,757).

## 2. Contaminación TUNE/TEST
- Plantillas (177), rho y selección (e=250, f=0, g=0,5) se rederivan IDÉNTICAS solo con 20-21. diag_tune solo tiene 20-21. Orden por mtime: PREREG 16:15:25 → e2 16:15:43 → e3 16:16:14. No hay rastro de métricas sobre TEST previas al prereg (no se puede probar la ausencia de pruebas interactivas). El TEST no es virgen (ronda 1), y así se declara.
- Discrepancia: las horas de la cabecera («~16:25Z» en el prereg, «~16:50Z» en el informe) no cuadran con los mtime (16:15/16:18). El orden sí.

## 3. Cifras (todas se reproducen)
Capa 1: n=2.270, 93 rellenas, 4,54 % vs 4,10 %, Wilson95 3,36-4,99, recall 0,839 (78/93), precisión 0,757, AUC 0,9185, puja 49,7/49,7 (79/14/14), por día 4,41/4,64 y 3,05/4,20 %. Placebos +90/−90: recall 12,9/1,1 %, precisión 6,6/5,6 %, P_puja 40,1/7,0 %. Capa G: 29,27 % vs 49,73 % (−20,46 pp), AUC 0,633, P_orden_G 5,43 %, +90 35,1 % (AUC 0,625), −90 9,2 % (AUC 0,445). EV real TEST −0,321 €/€ (93 rellenos, 99,92 € de coste).
Discrepancias:
- (a) «IC90 por cierre» = bootstrap por slug, es decir por PUJA (187 clústeres), no por cierre. Por hora de cierre (64 cierres, ~3 monedas por cierre): −0,274..−0,138 (el informe da −0,266..−0,149). Mismo signo y misma conclusión.
- (b) «37 % de los rellenos 0-250 ms después»: en TUNE, el 33,9 % de los 109 tiene el print después de t_fin (el 36,6 % de los que tienen print a ±5 s). El tramo 0-250 ms es el 28,4 % (30,7 %).
- (c) El placebo −90 s está degenerado: el 81 % de las pujas empieza con T>210 s, así que el desplazamiento cae antes de que abra la ventana 5m. El placebo informativo es +90 s, y G (AUC 0,633) ≈ +90 (0,625): G no tiene especificidad temporal. K4 falla de todos modos.
- (d) v2lib descarta las filas q con lado «None» (71k el 22-Oct, 18k el 23-Oct) y usa la anterior (≤30 s). Con trato estricto P_G = 0,2927: sin efecto.

## 4. Holgura 250 ms y veredicto
- No hay filo de navaja. K1 pasa con (e,g) = (100; 0,5), (250; 1), (250; 0,5) y (500; 1), y falla con e=0, con 1000 y con (100; 1). Es un parámetro mecánico (cancelación ~60 ms y feed p50 26 ms). La selección es solo TUNE y obligada por precisión ≥0,80 (el mínimo libre de err era 500/1).
- PARCIAL es la etiqueta correcta según el prereg: K1 sí; K2, K3, K4 y K5 no.
- RESERVA DE ALCANCE (fuera del informe): K1 es un replay de las órdenes PROPIAS de B. No es una etiqueta contrafactual:
  - (i) La ventana es endógena al relleno. 21/93 rellenos no tienen cancelación y su ventana termina al detectar el relleno. Los otros 72/93 caen en órdenes que B ya estaba cancelando.
  - (ii) Auto-print: en el 57 % de las tx de relleno de B (57/98) B es el ÚNICO maker, y ahí el recall es 0,92 frente a 0,725 con otros makers (n=53/40). Parte del acierto es «el feed muestra el relleno propio». f=0 (sin cola) calibra por eso y no vale para órdenes que no están en el libro.
  - (iii) La deriva de B entre tramos: EV TUNE +0,132 frente a TEST −0,321.
- La lectura «vida endógena» no se refuta. La alternativa de plantillas truncadas por el desenlace NO explica el fallo de G: plantillas de pujas rellenas 27,5 % vs no rellenas 32,1 %.

## Implicaciones
- Frentes 2-3: sobre órdenes reales de B, usar la verdad on-chain directa (202 rellenos / 3.796 órdenes / 364 pujas, 20-23 Oct; 4 días, poco poder). La regla virtual no aporta nada ahí y no está calibrada para contrafactuales (otro precio, momento, población P o favoritos). Todo F8/A1 con etiqueta virtual sobre P sigue siendo EXPLORATORY.
- Modelo de cancelación de B:
  - Modelar la cancelación como función del libro MÁS la carrera de latencia: 62/202 rellenos llegan 0-250 ms tras la intención de cancelar.
  - Modelar la presencia propia y la cola, porque f=0 solo funciona por el auto-print.
  - Juzgar contra el placebo +90 s, no contra −90 s.
  - Post-hoc EXPLORATORY (3 grupos, sin prereg), EV/€ con IC90 por slug, n=202:
    - Rellenos sin print visible: −0,65 (−0,94..−0,27), n=36.
    - En carrera: +0,26 (−0,24..+0,81), n=62.
    - Dentro de la ventana: −0,13 (−0,41..+0,16), n=104.
    - Preregistrar antes de usarlo.
