# H23 real: arreglos de los hallazgos 1-7 del /code-review (20-Oct-2026)

Ficheros: `experimento_maker_h23.py` (ronda 2: `sha=4346e3bddf542d67 regla=46eff95337902549 h47=439a70e9262ef38c pares=5e116f619887345d shadow=43373dd4affe3181`; CAMBIA con cualquier edicion posterior) y `test_experimento_maker_h23.py`.
`/root/polymarket-research-dev/experimento_maker_h47.py` NO se ha tocado (el diff contra H47 sigue siendo cero lineas; el B real que corre con el no se ve afectado).
Sin commits, sin lanzar nada. Tests: 50 pasados tras la ronda 2 (38 en la ronda 1) (`python3 -m pytest -q -p no:cacheprovider test_experimento_maker_h23.py`, nice 19, ulimit 3 GB).
Mutaciones (ronda 1: 7; ronda 2: otras 8, todas detectadas): roturas deliberadas del codigo (quitar reaccion en paso, top con nuestra orden, sin revalidar, sin edad de token, sin sha, sin `visto`,
verificar sin limite) hacen fallar al menos un test cada una.

## Por hallazgo

1. HECHO. `_marcar_visto` (copia del bloque de `Exp47.decidir`) se llama en `decidir()` y en la reaccion rapida, antes de cancelar. Tests con `X.cancelar`
   REAL y cliente falso (`not_canceled: already canceled or matched`, orden de 5 s): `test_hallazgo1_already_canceled_en_orden_joven_no_acaba_en_kill`
   (sin kill, `ya_terminal`), `..._control_sin_marcar_visto_el_mismo_escenario_mata_la_wallet` (el codigo anterior: kill), `..._via_paso_rapido_...`.
2. HECHO. `paso()` evalua la orden viva ANTES de `Exp47.paso` (que sale sin llegar a decidir si `fresco()` es False). `LibroH23` guarda la hora del
   ultimo mensaje por token; `_libro_fresco` exige conexion Y edad(5m s) y edad(15m s) <= `EDAD_TOKEN_MAX_S`=30 s; sin vista = cancelar y no pujar.
   Tests: `test_paso_cancela_con_libro_no_fresco_antes_de_salir`, `test_paso_cancela_si_el_libro_15m_esta_viejo_aunque_la_conexion_viva`,
   `test_libro_h23_registra_edad_por_token`. Coste medido en el extracto (10 y 16-Oct, 162 ventanas): el 15m tiene algun hueco >30 s en el 12 % de las
   ventanas (1,2 % del tiempo cotizable; el 5m: 2 % de ventanas, 0,7 % del tiempo, varios son huecos del propio extracto). Cancelar ahi es conservador:
   se pierde prioridad de cola, no EV por seleccion adversa. El umbral 30 s es mio, no esta congelado: Javi/chief pueden subirlo.
3. HECHO. `_top5` usa `mejor_bid_ajeno(tok, precio, resto, visto)` con orden viva (el replay no nos tiene en el libro). Tests:
   `test_equivalencia_con_el_replay_mismas_decisiones_sobre_el_mismo_libro` (600 libros aleatorios: misma decision que `R.querer` sobre el libro ajeno;
   la version ingenua discrepaba en algunos, asi que el test tiene potencia) y `test_solos_en_el_nivel_se_cancela_aunque_top_muestre_nuestra_orden`.
4. HECHO. `LibPost` se pasa como `lib` a `X.Exp.post`: tras `create_order`+`get_neg_risk` se recalcula `objetivo_h23` completo (cota bid15, margen,
   cruce, frescura 5m/15m, T) y si ya no es el precio firmado NO se envia (`h23_revalida_aborta`). Tests: `test_hallazgo4_*` (X.post real; 4 cambios
   parametrizados; control: sin cambio SI envia post-only; `post_order` no se llama).
5. HECHO con un limite declarado. Orden de cada vuelta: reaccion -> REST. `liquidar` y `verificar` re-evaluan antes de cada lectura, `verificar` va de una
   en una mientras haya orden viva, y `vigilar_saldo` (RPC bloqueante) se espacia a 10 s con orden viva. `h23_cancela` registra `t_evento`, `t_detecta`,
   `t_cancel`, `t_cancel_ret`, `ms_evento_a_cancel`, `ms_cancel_rtt`, `ult_poll_rest_ms`, `causa`, `origen`. Tests: `test_paso_cancela_antes_de_cualquier_lectura_rest`,
   `test_liquidar_y_verificar_reevaluan_...`, `test_vigilar_saldo_se_espacia_...`. LIMITE: una llamada REST ya en vuelo (get_order, hasta ~0,2-0,7 s con
   sus reintentos) no se interrumpe; si el evento llega justo dentro, la cancelacion espera a que termine. Quitarlo del todo exige un hilo de REST o
   cambiar `Exp47.liquidar_todo`/`X.consultar` (H47): NO aplicado. Al haber una sola puja activa a la vez (un 5m por cada 15m), no hay otros mercados
   a los que bloquear.
6. HECHO (etiquetas) y CUANTIFICADO (universo). `_log47` fuerza en `puja_fin/config/mercado_fin/puja_post/h23_*/kill_brazo/par_refs`:
   `variante=H23-<brazo>`, `brazo`, `umbral`, `hash_regla`; `config` lleva `codigo_sha_h23`. El brazo B usa escalon `H23B` (N_MAX['H23B']=40 desde el import).
   Tests: `test_hallazgo6_*`.
   Universo ejecutable: p en [0,10; 0,60] (tamano <=10 acc, <=3 USD/orden), T>=12 s, 5 acc/ceil(1 USD/p) en vez de 2 EUR. Replay 06..18-Oct (13 dias,
   BTC, cola base, alta 79 ms, cancel 60 ms, rebate 20 %, desenlace oficial; `analisis_h23.txt` + `universo_h23.py` en el scratchpad). Un relleno por cierre.
   | brazo/var | rellenos totales (n, EV pond) | fuera p<0,10 | fuera p>0,60 | fuera T<12 s | dentro, a 2 EUR | dentro, con tamano real | sin 2 mejores dias (tam. real) |
   |---|---|---|---|---|---|---|---|
   | A join_r (el que aplica) | 10; +0,595 | 0 | 0 | 0 | +0,595 | n=10, PnL +7,10 sobre 18,05 €; EV +0,393 | -0,001 (3 dias restantes) |
   | A join (sim-fiel) | 16; +0,992 | 0 | 2 (EV +0,48, acierto 100 %) | 0 | n=14; +1,120 | n=14, PnL +16,67 sobre 23,53 €; EV +0,708 | +0,425 (5 dias) |
   | B join_r | 9; +0,557 | 0 | 0 | 0 | +0,557 | n=9, PnL +6,15 sobre 13,97 €; EV +0,440 | -0,168 (1 dia) |
   | B join | 26; +0,737 | 0 | 4 (EV +0,35, acierto 100 %) | 0 | n=22; +0,870 | n=22, PnL +23,27 sobre 35,05 €; EV +0,664 | +0,439 (6 dias) |
   Lectura: el filtro de p y T apenas quita EV en join_r (0 rellenos fuera); lo que mas cambia el resultado es el TAMANO: pasar de 2 EUR a 5 acc baja el
   EV ponderado (A join_r +0,595 -> +0,393) porque los rellenos baratos (los mas grandes en el replay) pesan menos. Sin los 2 mejores dias el EV de join_r es
   ~0 (A) o negativo (B) con 1-3 dias restantes: n minimo, SIN significacion; es el limite del replay, no una prueba. Los fuera-de-universo (p>0,60) son
   solo `join`, todos ganadores a precio alto (poco rendimiento por €). Caveat: se filtra por el precio del relleno; no se simula que una cotizacion
   fuera de [0,10; 0,60] no se ponga (podria cambiar la secuencia de re-cotizaciones). Dias del replay hechos: 13 (06..18-Oct), 0 de `join_r` con n>=40.
7. HECHO. (a) El OK ya no es solo texto: debe contener `sha=<sha256[:16] de ESTE fichero>` y `regla=<hash_config>`; `--imprimir-sha` los da; cualquier
   edicion lo invalida (`test_ok_ligado_al_sha_de_este_fichero`). (b) `exigir_puertas` LEE el ledger de H47-B (`experimento_h47_B_ledger.jsonl`): tras su
   ultimo `config` real exige `fin_ejecucion` con kill falso y sin ordenes abiertas sin verificar, sin kill pendiente y sin lineas ilegibles tras el
   `config`; falta/en curso/kill = no arranca (`test_puerta_h47b_exige_fin_ejecucion_sin_kill`, `test_puertas_del_modo_real`). (c) Kill por brazo
   IMPLEMENTADO: `evaluar_kill_brazo` (CONFIG kill_brazo: n>=20 posiciones con desenlace oficial y EV ponderado por € sin los 2 mejores dias < -0,15;
   missing no cuenta; <3 dias no dispara), vigilado cada 60 s solo sin orden viva, evento persistente `kill_brazo` en el ledger del brazo, cancela la
   viva, no repone y `parar`; el real no arranca con kill de brazo pendiente (`test_main_real_no_arranca_con_kill_brazo_pendiente`); rearme con
   `--rearmar-kill-brazo "motivo"` (lock). Tests: `test_kill_brazo_*`. Aviso: el falso disparo simulado (h23_analisis) es 13 % con el edge observado y 94 %
   sin edge con 60 rellenos: es un freno de perdida, no un test de edge.

## Pendiente / no hecho
- Ensayo en seco de extremo a extremo (necesita desplegar en la raiz de dev con red/WS): NO hecho; solo tests con fakes + `X.cancelar`/`X.post` reales.
- Medir `ms_evento_a_cancel` y `ult_poll_rest_ms` reales en seco/real antes de fiarse de la latencia de reaccion (hoy solo se registra).
- Cancelacion mientras hay un REST en vuelo (hallazgo 5): requiere cambio en H47 o hilo; descrito, no aplicado.
- `EDAD_TOKEN_MAX_S`=30 s y `VIGILAR_SALDO_VIVA_S`=10 s son decisiones mias: revisar en el re-review.
- El `/code-review` debe repetirse sobre el fichero nuevo (el OK anterior, si existiera, no vale: otro sha). El real sigue necesitando H47-B terminado, /code-review y OK final de Javi.

---
# RONDA 2 (2o /code-review) -- 50 tests pasados (`50 passed in 4.16s`)

1. HECHO. `h47b_terminado` exige `parada` vacia y `pujas >= n_max` del `config` de ESE run (un abortado/Ctrl-C/senal no llega a su N; `fin_ejecucion` no
   registra la senal, por eso se infiere del N). Test `test_r2_1_h47b_abortado_o_interrumpido_no_cuenta`.
2. [SUPERADO por KILL V2, seccion siguiente] DECLARADO (no se baja la regla: cambiar `h23_regla.CONFIG` = version nueva fuera de este paquete). Con N=40 y la fraccion de relleno del replay join_r (A 10/43,
   B 9/63) se esperan ~9,3 (A) / ~6 (B) posiciones frente a las 20 exigidas: el kill de brazo es INALCANZABLE. Figura en el docstring (INALCANZABLE), en el
   evento `config` (`kill_brazo_alcanzable`) y en un aviso al arrancar. La perdida maxima la acota el suelo dinamico/presupuesto util (5 USD). Si se quiere un
   freno efectivo hay que elegir n_rellenos/dias y recalcular el falso disparo con h23_analisis (pendiente, decision del chief). Tests `test_r2_2_*`.
3. HECHO. El OK debe contener tambien `h47=`, `pares=` (experimento_pares_cola_15m.py) y `shadow=` (h23_shadow.py); van en `config.dependencias` y en
   `--imprimir-sha`. Test `test_r2_3_el_ok_liga_h47_pares_y_shadow`. DESPLIEGUE en dev (hoy `experimentos/5m_barato/h23_maker/` NO existe en
   /root/polymarket-research-dev; el import de h23_regla fallaria): copiar `h23_regla.py` y `h23_shadow.py` (de /root/polymarket-research/experimentos/5m_barato/h23_maker/)
   a `/root/polymarket-research-dev/experimentos/5m_barato/h23_maker/`, y `experimento_maker_h23.py` a la raiz de dev junto a `experimento_maker_h47.py`;
   `AQUI_REGLA` se resuelve desde `h23_regla.__file__`. `h23_shadow` usa `PRICES=/root/polymarket-research/data/prices` (solo lectura). Los tres sha deben
   coincidir con los del OK: copiar con `cp -p` y ejecutar `--imprimir-sha` desde dev. (No desplegado: solo paquete_real.)
4. HECHO. `_libro_fresco` = conexion sana (`fresco()` del arnes: PING/PONG <= 5 s, hilo vivo, sin error) + respaldo de 120 s por token (antes 30 s, que cancelaba el
   12 % de las ventanas 15m por libro quieto). `LibroH23.conexion_sana()` distingue salud de actividad. Tests `test_r2_4_*` (60 s quieto: no cancela; conexion
   muerta: cancela; token mudo >120 s: cancela). Limite: un token mudo entre 30 y 120 s con conexion sana ya no se cancela (la perdida eventual es de selección adversa, no cuantificada).
5. HECHO. `_top5` resta SIEMPRE nuestro tamano restante. `test_r2_5_nunca_se_queda_donde_el_replay_cancelaria...` (800 libros, orden mostrada o no, vista o no, cola
   ajena pequena): si el WS muestra nuestra orden la decision es EXACTAMENTE la del replay; si no, solo puede ser mas conservadora (cancela de mas), nunca se queda
   donde el replay cancela. Coste: con cola ajena menor que nuestro tamano y orden aun no mostrada se cancela/re-cotiza de mas (breve, hasta que el WS la muestra).
6. HECHO. `Exp23.liquidar` tras `_reaccion_rapida` relee `h in self.vivas`: si paso a `canceladas` continua con `es_cancelada=True` y la orden de `canceladas`; si ya no esta en
   ninguna, no lee. Test `test_r2_6_*`.
7. HECHO. `h23_cancela` lleva `camino_ack` y `rtt_incluye_asentar_s` (X.cancelar duerme ASENTAR_S=1,5 s + get_order en el camino ack, commit 0b0eede035 de dev) y
   `edad_5m_s/edad_15m_s`; docstring actualizado. Test `test_r2_7_camino_ack_de_x_cancelar_desde_h23` (X.cancelar real, `time.sleep` capturado, sin kill, y camino normal
   con `camino_ack=False`). Nota: en el camino ack la reaccion queda bloqueada >=1,5 s; es lo que H47/pares hace y no se cambia aqui.
8. HECHO. `_vigilar_kill_brazo`: sin orden viva/cancelada, sin mercado activo, no a <20 s de la apertura del siguiente 5m cotizable ni dentro de la ventana, <= 2 consultas
   gamma por pasada, timeout 3 s (antes 10). `vigilar_saldo` se espacia tambien con cancelada pendiente. Tests `test_r2_8_*`. Pendiente: el RPC de saldo en si sigue
   siendo bloqueante cuando toca (cada 10 s con orden viva); acotarlo del todo exige cambiar `saldo()` de H47.

---
# KILL V2 DE BRAZO (Javi 20-Oct: que funcione con N=40) -- 56 tests pasados (`56 passed in 2.24s`)

Version nueva del kill; `h23_regla.py`, la regla H23 y el replay NO cambian (hash de la regla `46eff95337902549` intacto). Vive en el paquete: `KILL_BRAZO_V2`
(z 1,645; sigma1 2,0; margen_ev 0,05; n_min 3; tope_perdida 4,5 $; sin exigir dias) + `evaluar_kill_v2` + `hash_kill_v2()` (parametros + codigo de la funcion; entra en el OK como
`kill=` y en `config.kill_brazo_v2`). Regla: tras CADA posicion cerrada con desenlace oficial (orden por cierre), dispara si perdida acumulada >= z*sigma1*s*sqrt(n) - 0,05*s*n (n>=3)
o >= tope. Evento `kill_brazo` persistente, `--rearmar-kill-brazo` (tras el rearme solo cuentan ordenes posteriores). Quitado el aviso de «no alcanzable».
**Nuevo sha del OK:** `sha=b7d9b2aedbcbdf82 regla=46eff95337902549 h47=439a70e9262ef38c pares=5e116f619887345d shadow=43373dd4affe3181 kill=23bee24053e56b95`.

Estimacion (replay 06..18-Oct, cola base, alta 79/cancel 60): sigma1 empirica (std de pnl/coste por posicion) join_r 1,87 (n=19), join 1,79 (n=42), pool 2,07 -> se usa 2,0
(modelo binario a los precios del replay: 1,6 de media, p90 2,6). Tasa de relleno join_r por cierre cotizado: A 0,233, B 0,143 -> con N=40: 9,3 (A) y 5,7 (B) posiciones.
Precio medio de relleno 0,36; coste por posicion ~1,5-1,8 $. No use fills reales de B (no estan en este paquete y su n no ayudaria).

## Simulacion secuencial (`sim_kill_v2.py`, 20.000 trayectorias por celda, semilla fija, misma funcion que el ejecutor)
Trayectoria: n ~ Binomial(40, tasa); precio remuestreado del replay; tamano real (5 acc o ceil(1$/p)); gana ~ Bernoulli(q) con EV ponderado por euro = EV (rebate incluido).
Cifras = % de trayectorias en que el kill dispara alguna vez.
| EV real | A tope 3,0 | A tope 4,0 | **A tope 4,5** | A tope 5,0 | A solo sigma | B tope 3,0 | B tope 4,0 | **B tope 4,5** | B tope 5,0 |
|---|---|---|---|---|---|---|---|---|---|
| +0,40 | 26,3 | 18,2 | **14,8** | 12,1 | 0,0 | 21,9 | 14,0 | **10,7** | 8,3 |
| +0,20 | 41,0 | 31,4 | **27,1** | 23,4 | 0,1 | 31,7 | 22,1 | **18,1** | 14,7 |
| +0,10 | 48,9 | 39,1 | **34,8** | 30,6 | 0,2 | 38,5 | 28,1 | **23,8** | 20,0 |
| +0,05 | 52,2 | 42,8 | **38,2** | 33,9 | 0,2 | 41,8 | 31,2 | **26,3** | 22,7 |
| 0 (potencia) | 56,5 | 47,3 | **42,8** | 38,7 | 0,4 | 45,2 | 34,4 | **29,5** | 25,3 |
| -0,15 (potencia) | 67,8 | 59,1 | **54,8** | 50,7 | 0,7 | 56,1 | 45,2 | **40,1** | 35,1 |
| -0,30 (potencia) | 79,2 | 72,0 | **68,2** | 64,5 | 1,9 | 65,1 | 55,4 | **49,9** | 44,8 |
Posiciones medias por trayectoria: A 9,3, B 5,7. Perdida media al disparo (tope 4,5): ~5,3-5,5 $ (salto por posiciones de ~1,8 $; el suelo de presupuesto de 5 $ limita en la practica el gasto).

**Lectura honesta:** con N=40, posiciones de ~1,8 $ y sigma1~2, la desviacion tipica de la PnL total es ~10 $, mayor que cualquier tope <= 5 $: NO existe un kill con falso
disparo <= 15 % (con edge conocido) Y potencia util. Con el tope 4,5 $ el falso disparo es <= 15 % solo con EV >= +0,40 (A) / +0,20 (B), y la potencia con EV 0 es 43 % (A) / 30 % (B),
con EV -0,15 55 % / 40 %. La rama sigma del PLAN (z 1,645 o 2,0) casi nunca dispara antes del tope (0,0-0,7 %: exige ~10 perdidas seguidas con sigma1=2): se mantiene por fidelidad y
para tamanos menores, pero el kill es en la practica un TOPE DE PERDIDA PERSISTENTE (con evento y rearme manual). El tope de 3,0 $ (60 % del presupuesto, sugerido) da 52 % de falso
disparo con EV +0,05 y 26 % con +0,40 (A): no es aceptable, por eso 4,5 $ (90 %). Decision de Javi/chief: si se prefiere menos falso disparo, 5,0 $ (= agotar el presupuesto: A +0,20 23 %, B 15 %).

---
# KILL V3 (Javi 20-Oct: tope 5,0 $ y acumulado entre tandas) -- 62 tests pasados (`62 passed in 1.48s`)

`KILL_BRAZO_V3` (z 1,645; sigma1 2,0; margen 0,05; n_min 3; tope_tanda 5,0 $) con hash propio (`hash_kill_v3`: `kill=` en el OK y `config.kill_brazo_v3`). h23_regla.py y el replay intactos.
- ACUMULADO: n = posiciones cerradas con desenlace oficial de TODOS los ledgers reales del brazo (`experimento_h47_H23_ledger*.jsonl` / `..._H23B_ledger*.jsonl`, sin mezclar brazos ni H47-B)
  desde el ultimo `kill_brazo_rearmado`. Un `suelo_reiniciado`/`suelo_fijado`/nueva tanda NO lo reinicia; solo `--rearmar-kill-brazo`. Fail-closed: un ledger hermano ilegible (linea cortada,
  JSON no objeto, fichero ilegible) = `LedgerBrazoIlegible` -> el real NO arranca y el rearme tampoco.
- FORMULA (kill PERSISTENTE): perdida acumulada >= 1,645*sigma1*s*sqrt(n) - 0,05*s*n sobre el n acumulado (el «tope duro acumulado» es esta formula), comprobada tras cada posicion.
- TOPE DE TANDA 5,0 $ (perdida de las posiciones de ESTA ejecucion): **PARA la tanda** (evento `tope_tanda`, cancela lo vivo) pero NO deja kill persistente. Interpretacion mia, razonada por la
  simulacion: como kill persistente seria un test repetido en cada tanda y daria 43-99 % de falso disparo (ver «solo tope de tanda»). Si se quiere persistente, es una linea (decision de Javi).
**Nuevo sha del OK:** `sha=sha=c394037e5e6656bd regla=46eff95337902549 h47=439a70e9262ef38c pares=5e116f619887345d shadow=43373dd4affe3181 kill=ffcf92552ead5dc1`.

## Simulacion secuencial (`sim_kill_v3.py`, 20.000 trayectorias, misma funcion que el ejecutor; tandas de 9 posiciones = A con N=40; cada tanda con presupuesto fresco de 5 $)
Cifras = % de trayectorias en que dispara alguna vez, por N de posiciones ACUMULADAS.
| N acum. | EV | V3 completo (tanda+formula) | **solo formula acumulada (kill persistente)** | solo tope de tanda |
|---|---|---|---|---|
| 20 | +0,20 | 43,3 | **0,5** | 43,3 |
| 20 | +0,05 | 58,7 | **1,3** | 58,7 |
| 20 | 0 | 63,5 | **1,9** | 63,5 |
| 20 | -0,15 | 78,6 | **4,8** | 78,6 |
| 40 | +0,20 | 70,6 | **0,6** | 70,6 |
| 40 | +0,05 | 84,9 | **2,1** | 84,9 |
| 40 | 0 | 89,1 | **3,2** | 89,1 |
| 40 | -0,15 | 96,4 | **10,9** | 96,4 |
| 80 | +0,20 | 91,3 | **0,8** | 91,3 |
| 80 | +0,05 | 97,8 | **2,8** | 97,8 |
| 80 | 0 | 98,9 | **5,1** | 98,9 |
| 80 | -0,15 | 99,9 | **22,8** | 99,9 |
Lectura: la formula acumulada cumple el falso disparo (<= 3 % con EV >= +0,05 hasta 80 posiciones) pero tiene POCA potencia: con EV -0,15 solo dispara 4,8 % (20 pos.), 10,9 % (40), 22,8 % (80)
(posiciones de ~1,8 $ con sigma1 ~2: hace falta mucho n; con EV 0 casi nunca dispara, que es lo correcto). El tope de tanda dispara con frecuencia (43 % ya a +0,20 en una sola tanda, mucho mas en varias):
por eso es solo una parada de tanda. La proteccion real de dinero es el presupuesto de 5 $ por tanda y el suelo; el kill acumulado es el freno estadistico de largo plazo.

---
# RONDA 3 (3er /code-review; paquete CONGELADO hasta el gate de n>=40) -- 75 tests pasados (`75 passed in 7.95s`)

1. HECHO. `_resolver_pendientes` ROTA (menos intentos primero, luego mas antigua; <= 2 por pasada), cuenta cada fallo de gamma (`desenlace_error`) y NO deja el kill ciego: la evaluacion
   se hace SIEMPRE con los desenlaces cacheados (un fallo de gamma ya no deja `_ult_kb` puesto sin evaluar). FAIL-CLOSED: una posicion con >= 8 intentos o > 15 min desde el cierre sin
   desenlace (o con relleno incierto) pone `sin_desenlace` y `decidir` no postea (se levanta sola al resolverse). Tests `test_r3_1_*`.
2. HECHO. `_puerta`: antes de la primera orden de una tanda resuelve (hasta 20 consultas) y evalua las posiciones pendientes; si no puede (gamma, incierta, pendientes) no postea y reintenta cada
   15 s; si el kill dispara, no postea. Test `test_r3_2_*`.
3. HECHO. Dedupe por oid (sin nombre de fichero) entre ledgers hermanos y propio (lo propio manda) y una posicion por slug; patron ESTRICTO `experimento_h47_H23[B]_ledger[_tandaN].jsonl`
   (ni `.bak`, `_copia`, `~`, `_t1`). Test `test_r3_3_*` y `test_kv3_cada_brazo_acumula_solo_sus_ledgers`.
4. HECHO. `h47b_terminado(eventos, sha_h47)`: config.escalon == 'B', n_max >= 230, t_stop == 60 y config.codigo_sha == `h47=` del OK (exigir_puertas lo pasa siempre). Tests `test_r3_4_*`.
5. HECHO. `_libro_fresco` y `LibPost.fresco` usan `LibroH23.conexion_sana()` (PING/PONG) + respaldo 120 s por token; ya NO `X.Libro.fresco()`. Test con libro real quieto 200 s y conexion
   viva (`X.Libro.fresco()` daria False; el nuestro True), token mudo > 120 s (False) y conexion muerta (False). `test_r3_5_*`.
6. HECHO (documentado en docstring, `KILL_BRAZO_V3["nota"]` -> `config`, y aqui): con n acumulado < ~10 posiciones la formula sigma es INALCANZABLE (exige ~10 perdidas seguidas con sigma1=2);
   la proteccion real a n bajo es el SUELO DE SALDO / presupuesto util de H47 (5 USD) y el tope de tanda; el kill sigma solo actua con n acumulado grande. s_n es la MEDIA MOVIL DEL PREFIJO
   (coste medio de las n primeras posiciones), no de todas. `test_r3_6_*`.
7. HECHO. El kill usa PnL = acc*gana - coste (el rebate teorico NO cuenta como ingreso; cota pesimista). Posiciones con alguna orden abierta (`hi > lo`: relleno sin verificar / fill desconocido)
   = `incierta` -> gana None (sin desenlace fiable, fail-closed). `test_r3_7_*`. (La tabla de simulacion se REHIZO sin rebate, abajo.)
8. HECHO. `kill_brazo`, `tope_tanda` (fsync, y si no llega a disco -> kill de la wallet) y `kill_brazo_rearmado` (fsync; si falla, el rearme no se da por hecho) y la linea ilegible del ledger
   PROPIO = fail-closed (`estado_acumulado` lee el propio en estricto; aceptable solo con la herramienta del punto 10). `test_r3_8_*`.
9. HECHO. `pares_contabilidad.py` en `sha_dependencias()` (`contabilidad=` en el OK, `--imprimir-sha` y `config.dependencias`); `hash_kill_v3` incluye el codigo de `evaluar_kill_v3`,
   `agrupar_posiciones`, `estado_acumulado`, `escanear_brazo`, `leer_ledger_brazo` y `ledgers_del_brazo`. `test_r3_9_*`.
10. HECHO. `--aceptar-linea-ilegible-brazo "motivo"` (`aceptar_lineas_brazo`): muestra cada linea, solo acepta las que parezcan JSON cortado (si hay otra, ninguna), exige motivo y la frase de
    confirmacion `ACEPTAR LINEA ILEGIBLE BRAZO <A|B>`, escribe `h23_linea_ilegible_aceptada` (fichero + sha + linea cruda base64) con fsync en el ledger propio. `test_r3_10_*`.

Mutaciones: 13 roturas del codigo de la ronda 3 (X.fresco, sin rotacion, puerta siempre abierta, sin fail-closed por intentos, dedupe por fichero, sin escalon B, sin sha de H47, con rebate,
incierta cuenta, sin fsync, propio ilegible ok, sin contabilidad, except que deja el kill sin evaluar) hacen fallar al menos un test cada una.

## Simulacion REHECHA sin rebate (`sim_kill_v3.py`, 20.000 trayectorias, tandas de 9 posiciones, presupuesto fresco 5 $ por tanda)
| N acum. | EV | V3 completo (tanda+formula) | **solo formula acumulada (kill persistente)** | solo tope de tanda |
|---|---|---|---|---|
| 20 | +0,20 | 44,4 | **0,5** | 44,4 |
| 20 | +0,05 | 59,7 | **1,5** | 59,7 |
| 20 | 0 | 64,5 | **2,1** | 64,5 |
| 20 | -0,15 | 79,3 | **5,2** | 79,3 |
| 40 | +0,20 | 71,8 | **0,7** | 71,8 |
| 40 | +0,05 | 85,5 | **2,3** | 85,5 |
| 40 | 0 | 89,7 | **3,4** | 89,7 |
| 40 | -0,15 | 96,6 | **11,6** | 96,6 |
| 80 | +0,20 | 91,9 | **0,9** | 91,9 |
| 80 | +0,05 | 98,0 | **3,2** | 98,0 |
| 80 | 0 | 99,0 | **5,6** | 99,0 |
| 80 | -0,15 | 99,9 | **24,5** | 99,9 |
(La rama sigma depende de EV real y de n; con n acumulado < 10 no puede dispararse. Potencia baja a n bajo: lo honesto, sin maquillar.)

**Nuevo sha del OK:** `sha=sha=602d5a2debb42cc0 regla=46eff95337902549 h47=439a70e9262ef38c pares=5e116f619887345d contabilidad=0a41bc39108cdf82 shadow=43373dd4affe3181 kill=59437e2037321aed`.
**Paquete CONGELADO** hasta el gate de n>=40: cualquier edicion cambia el sha y exige re-review + OK nuevo. Despliegue en dev (no hecho): ver ronda 2 punto 3.
