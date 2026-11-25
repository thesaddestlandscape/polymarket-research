# SPEC F5-V4 (17-Nov-2026) -- escrita ANTES de calcular ninguna cifra de T2/T3. Sin dinero real. Solo sensibilidad: todo «no validado».
Paso 1 de 6 «cerrar F5» (Javi). NO se tocan dryrun/*, cxb60dry, forward_v2.py, PREREG_FWD_V2.md, ADDENDUM1/3 ni caches de exp1/ (solo lectura).

## T1. passT_v4 sobre V2 y ADD3
Hecho verificable por codigo (no por resultado): la poblacion F5 (V2 forward = forward_a1/forward_v2; ADD3 = e2_dia_add3/e2_agrega_add3) se construye con PRINTS de m5_registro
(sello r_v3 = r_ex - c - 1, c=19 ms constante; F5 del libro q por RX <= t_dec) y NO importa engine/engine_v3/engine_v4/passT: engine_v4 solo cambia la cantidad/tf de NUESTROS rellenos simulados.
Comprobaciones: (a) grep de imports; (b) re-ejecucion de los agregadores (copias) sobre las MISMAS caches -> cifras identicas (V2 RESUMEN y ADD3 .txt, comparando sha de las lineas de cifras);
(c) CRUCE de los 33 tf distintos (G0 publicado CX_v3dd vs out_v4/RT_v3dd var G0, 26-Oct..09-Nov) mas los 5 rellenos-polvo: para cada uno, ¿la moneda/dia esta en ADD3 (ETH/SOL/XRP)?, ¿hay print de la poblacion
(banda q (0,10;0,30], ultimos 300 s) con mismo (fin, coin, lado, nivel L) y |r_ex - tf| <= 2000 ms para tf_v3 y para tf_v4?, y el tercil F5 (p35 y p60) de ese print. Cualquier delta de EV de celda es 0 por construccion; se reporta el peso (EUR) de esos prints en su celda.

## T2. Clasificador causal de clase de suelo (rx - ex de las filas q), funcion reutilizable `suelo_causal.py`
Filas: las de ADD2/ADD3 C3 (q de tokens de mercados 5min de las 6 monedas, bid en [0,03; 0,45]); d = rx - ex recortado a [-50, 400] ms (bins de 1 ms); tiempo en bins de 10 s por RX.
Instante de decision t. B = floor(t/10 s). Solo bins COMPLETOS anteriores a t: W2 = bins B-30..B-1 (5 min recientes), W1 = B-60..B-31 (5 min previos), W = W1+W2.
p5(X) = menor d con cum >= max(1, trunc(0,05*tot)) (identico a ADD2/ADD3); exige tot(W) >= 200 y tot(W1), tot(W2) >= 100, si no clase 'indet'.
clase(X) = lo si |p5-19,25| <= 5; hi si |p5-39,5| <= 5; si no indet (umbrales ADD2, sin tocar).
Clase final: PURA lo/hi si clase(W)=clase(W1)=clase(W2) in {lo,hi}; 'mixta' si {clase(W1), clase(W2)} = {lo,hi}; 'indet' en cualquier otro caso. Clases operables: SOLO pura lo / pura hi.
Instante de cada print de la poblacion ADD3: t = r_ex - 83 ms (= t_dec de p60 con c=19, l=60, d_proc=3; mas temprano que el de p35, causal para ambos). V2 forward: t = r - 100 ms (r = rx).
Control de integridad: con los histogramas de 10 s, la p5 de cada ventana ALINEADA de 10 min debe reproducir `perfil_p5_10min` de los manifiestos ADD3 (exp1/cache/pob_add3_D.json) -> 0 diferencias.
Validacion (no se usa para elegir nada): clase «de futuro» = clase de las filas con rx en [t, t+300 s) (bins B..B+29, tot >= 100). Matriz clase causal vs futura; CONTAMINACION = % prints (y EUR) con clase futura determinada distinta de la declarada. Se compara con la clase causal de ADD3 (ventana alineada previa, cl_c).
Comparador: celdas ADD3 (b) con cl_c (control: debe reproducir E2_clase_suelo_add3.txt) y con la clase causal v4 PURA (excluye indet y mixta).

## T2/T3. Celdas y metricas (identicas a ADD3 (b); no se anade ninguna)
Celdas: {p35, p60} x {lo, hi} sobre tipo B (bid >= q + 0,0099), segmento = dia x clase; unidad = (dia, mercado, lado, tercil); EV ponderado por EUR (sum pnl / sum coste) y por unidad; gradiente bajo-alto diario;
IC90 por dias (t, 1 cola); sin 2 mejores dias; placebo por unidad (B=1000, semilla 20261118, max-stat sobre las celdas del mismo grupo). Cortes de tercil del TRAIN SIN tocar (C0=3,526360511779785; C1=4,717426776885986).
Se reporta por celda: prints, unidades, dias, EUR excluidos por indet/mixta (prints, EUR, mercado-lado). ALL3 = ETH/SOL/XRP (caches ADD3 existentes + clase v4); BTC = poblacion nueva (misma definicion p35/p60 de ADD3, 35 dias, cobertura de desenlace >= 0,995 por dia o dia PENDING y excluido con su cobertura).
Criterio §4 de ADD3 sin cambios y solo informativo: robustez = media>0, IC90 dias inf>0, sin 2 mejores>0 en hi y lo, placebo max-stat <= 0,0125. Resultado maximo posible: EXPLORATORY. Nada es REJECTED por n bajo (INSUFFICIENT).
V2 forward (copia versionada de forward_v2.py, mismas 8 condiciones, sin Telegram, sin tocar RESUMEN_V2.md): (i) ALL3 reproduccion; (ii) ALL3 solo prints de clase pura (excluye indet/mixta); (iii) BTC (grupo = {BTC}), con y sin exclusion.
Dias V2: los 11 validos 04..14-Nov (prints_D.pkl existentes); 15 y 16-Nov no estan procesados por el cron (load5>=8): NO se fuerzan. Multiplicidad: BTC es 1 grupo nuevo x 2 fuentes (V2, ADD3) x 2 l_ef; todo exploratorio, sin correccion.
Limites declarados de antemano: poblacion CENSURADA (solo prints ajenos): gradiente poblacional, NO EV de regla ni capacidad de B; d_proc=3 ms supuesto; causa de la alternancia del suelo insuficiente; hi tiene pocos dias (11) -> hi solo INSUFFICIENT/EXPLORATORY.
