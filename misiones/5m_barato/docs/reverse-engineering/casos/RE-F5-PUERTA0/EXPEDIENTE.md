# Expediente RE-F5-PUERTA0 — 23-Nov-2026 (reverse-engineer, encargo del chief)
Estado de cierre: PARTIALLY_SOLVED (diagnóstico reproducido; la solución es EXPLORATORIA sobre días vistos, sin OOS ni validación independiente) · Bloqueo dominante: **J/B** (la hipótesis se probó con una unidad equivocada: F5 por orden/repegado en vez de por entrada de mercado-lado, y con cortes de G0 no calibrados por moneda) · Secundarios: **G** (bloq0: 99 rellenos alto en 10 días), **B** (modelo de relleno: bloq0 670 vs bloq1 4.735 rellenos, ×7), **H** (aun con filtro EV<0).

## 1. Fenómeno
Puerta 0 (PREREG_R1v2 §4 + ADENDA_06/08): EV_€(bajo∪medio) − EV_€(alto) por tercil de F5_t de cada ORDEN B simulada (colocación Y cada repegado), C = 05-14 Nov (NO CIEGO). Oficial: NO_PASA (bloq0 −0,141 IC90 −0,494/+0,172; bloq1 −0,044).

## 2. Realidad observada
- Datos: misiones/5m_barato/alpha_miner_B_F5_15nov/f5_v4_17nov/b_real_sim/ver_todos_17nov/r1v2_eval/out_p0/p0_ordenes_2026-11-{03..14}.pkl (144.829 órdenes bloq0 / 62.855 bloq1 en 05-14), puerta0_resultado.json. Código: puerta0_core.py (leído), re_f5_23nov/*.py (sha en *.sha256).
- Reproducción: diff bloq0 −0,141 / bloq1 −0,0438, n órdenes 87.509/45.544/11.776 y rellenos 322/249/99 → **REPRODUCIDA** (re_f5_23nov/out/desagrega.json; 0 duplicados mercado-lado).
- Relojes: F5_t por rx<=t (decisión); tercil_ex por sello exchange (solo diagnóstico, mira ~20-40 ms al futuro). Fill = tf del motor passT_v4.
- Discrepancias: (a) el diseño dice «F5_t inválido si hueco de seq/antigüedad>30 s», pero n_inval = 0 en 207 k órdenes → el test de fuga es inevaluable por construcción (no hay inválidos), no por azar. (b) Los cortes C0/C1 vienen de prints ajenos en G0; en B real el «alto» es 8 % de órdenes (bloq0) y por moneda en la 1.ª colocación: ETH 21 %, SOL 5 %, **XRP 0,6 %** → el «alto» de la Puerta 0 es casi solo ETH.
- Límites: rellenos VISIBLES (sin NONE), motor simulado, días vistos; régimen de huecos viejo en todos los días (no hay días ≥16-Nov simulados).

## 3. Qué se sostiene / qué NO
SÍ (exploratorio, 05-14 Nov): (1) A nivel de ORDEN el gradiente está invertido o es nulo (bloq0 bajo −0,287 / medio −0,110 / alto −0,069; bloq1 −0,029/−0,068/+0,000): retirar órdenes «alto» quita los rellenos MENOS malos. (2) A nivel de MERCADO-LADO con F5 de la 1.ª colocación, el signo vuelve al del origen y es monótono (bloq0 EV bajo −0,12 / medio −0,25 / alto −0,39; bloq1 −0,003/−0,094/−0,121). (3) El repegado re-etiqueta: de los rellenos de lados que entraron «alto», el 81 % (bloq0) y 72 % (bloq1) llegan en órdenes etiquetadas bajo/medio. (4) Con cortes p80 DENTRO de moneda, «no entrar si F5 de entrada ≥ p80»: bloq0 diff +0,258 IC90 [+0,001; +0,489], 8/10 días, placebo día×moneda p=0,052, sin 2 mejores +0,245, ΔPnL −147→−84 €; bloq1 +0,101 [−0,047; +0,261], 5/10, p=0,035, ΔPnL −227→−79 €; q4 peor que resto en las 3 monedas (bloq0). 03-04 POST HOC mismo signo (+0,22/+0,28).
NO: que F5 haga a B rentable (EV restante −0,137 bloq0 / −0,017 bloq1); que el efecto del tercil original a nivel de lado sea más que composición por moneda (placebo día×moneda p=0,146/0,274); ninguna cifra es OOS (cortes p80 ajustados con los mismos días; formas probadas: tercil t0, quintiles, p80 → selección).

## 4. Diagnóstico
La Puerta 0 falla porque mide F5 en cada repegado: el repegado ocurre cuando el libro se mueve y F5 en ese instante es endógeno (ask del token recién refrescado), mientras la información útil de F5 está en el ESTADO del mercado-lado al entrar. Además los cortes de G0 no transfieren a B (alto ≈ ETH). Más filtros por orden o más días con la misma unidad NO resuelven esto (herramienta de G aplicada a un bloqueo J).

## 5. Hipótesis (HYPOTHESIS_LEDGER H-RF5-0..7)
H0 nula (ruido/día): no refutada a nivel de orden; a nivel de entrada p80 placebo p 0,035-0,052. H1 llega tarde (latencia): NO apoyada — el reloj exchange no mejora de forma consistente (orden bloq1 −0,044→+0,089; entrada bloq0 +0,229→−0,009); rellenos <0,5 s tras llegar bloq1 +0,147 [−0,05;+0,34] vs 0,5-2 s −0,298 [−0,51;−0,06]: mixto. H2 calibración G0≠B: APOYADA (alto 8 %, XRP 0,6 %; con cortes por moneda el signo aparece). H3 régimen/día: el fallo oficial es compatible con ruido (bloq0 99 rellenos alto; 11-Nov −1,84 a nivel de lado); mitades a nivel de entrada mismo signo en bloq0 (A +0,33 IC>0, B +0,12). H4 repegado: APOYADA descriptivamente (re-etiquetado 72-81 %). H5 umbral/lado: a nivel de orden el signo está invertido; a nivel de entrada YES y NO mismo signo. H6 huecos de stream (chief): con causas conocidas (restart 03:20/10:20/22:20 +50 s; XRP 08/12/16 h 115 s; 120 huecos) se marcan 0,2-0,8 % de órdenes, 0/670 rellenos bloq0 y 24/4.735 bloq1 (EV de los 24: −1,00), diff sin cambios (bloq0 −0,141→−0,141; bloq1 −0,044→−0,043; entrada +0,229→+0,223). XRP no puede explicar el fallo: 11-13 rellenos alto en 10 días. Marcado con TODOS los huecos >15 s: EN CURSO (run_hbgap.sh, puerta load5<4; out/gaps/).

## 6. Experimentos
E-RF5-1 desagrega.py c1c57ed9 · E-RF5-2 t0_refuta.py 466af151 · E-RF5-3 gap_mark.py e03ea71d (proxy hecho; real pendiente) · E-RF5-4 q4_entrada.py 97a1aaa5. Todos EXPLORATORIOS (días vistos; sha del código antes de ejecutar, sin prereg de resultado). Identidad: el diff por orden no es algebraicamente forzado; el contrafactual de entrada supone lados independientes (B una cara por lado).

## 7. Solución experimental propuesta
PREREG borrador re_f5_23nov/PREREG_RF5_ENTRADA_BORRADOR_23nov.md (sha be769431…): F5 como filtro de ENTRADA por mercado-lado, corte p80 por moneda congelado (ETH 4,7427 / SOL 4,1109 / XRP 3,3847), confirmación SOLO en días ≥18-Nov con cov_tx ≥0,90 (19-22 Nov fuera), ≥10 días, bloq0 y bloq1 mismo signo, placebo p<0,10. No duplica: los preregs R1v2/V5/V6 aplican F5 «al colocar» en cada colocación y repegado (DISENO 3c, ADENDA_02 §1); ninguno filtra la ENTRADA del lado.

## 8. Refutación intentada
Placebo día×moneda (tercil t0: p 0,146/0,274 → composición; p80 por moneda: 0,052/0,035); sin 2 mejores días (+0,245/+0,144); por moneda; por mitad; 03-04 post hoc; huecos (proxy). Pendiente: huecos reales; validación independiente (statistical-validator / red-team) — no la apruebo yo.

## 9. Economía (no sumar con E1b/V5)
Validada: 0 €. Exploratoria (contrafactual, rellenos visibles, 10 días vistos, unidades de stake del simulador): ΔPnL +63 € (bloq0) / +149 € (bloq1) en 10 días; EV de B tras el filtro sigue < 0 → contribución incremental potencial solo como componente de mitigación; capacidad no medida.

## 10. Siguiente paso exacto / reabrir
(1) Chief firma o corrige el prereg borrador; (2) generar órdenes B con puerta0_run en 18-Nov y ≥23-Nov (un día cada vez, cov_tx ≥0,90) y correr q4_entrada.py con esa lista; (3) terminar gap_mark.py real cuando run_hbgap.sh acabe (out/gaps/progreso.log). Reabre/refuta: diff ≤0 en bloq0 con ≥10 días ciegos ⇒ «F5 al entrar» REFUTADA para B real.
