# Expediente RE-B-VER-TODOS — 17-Nov-2026 (reverse-engineer)
Código y datos: `misiones/5m_barato/alpha_miner_B_F5_15nov/f5_v4_17nov/b_real_sim/ver_todos_17nov/` (MANIFEST.sha256, STATUS.json).
Prereg: `PREREG_DEM_17nov.md` (sha final 37315ac12add5bda…; adendas 1 = COLA/C150 antes de calcular, 2 = arreglo de implementación sin métricas vistas, 3 = DEMr_COLA POST HOC).

## 1. Fenómeno
El simulador de la política real de B (contrato CONTRATO_MEDICION_F5_B_v2, base `r2_call00a35_intc33_v3d`) ve 84 de los 202 rellenos reales de B
(3.796 órdenes, 20-23 Oct; precisión 0,955, recall 0,416). Objetivo de Javi: verlos todos.

## 2. Realidad observada (reproducida)
| cifra previa | origen | estado |
|---|---|---|
| 88/84/4/118, prec 0,955, rec 0,416 | validacion_primaria_BASE.json / verif_v5 | REPRODUCIDA (v4_verif_dem, mismo motor) |
| 118 FN = 98/11/8/1 | valida_v5.evalua | REPRODUCIDA |
| 90/98 tomador del complementario | tomadores.pkl (FN_132) | REPRODUCIDA (calldata: 90 compra_comp, 8 vende_propio) |
| v3d_comp recupera ~8 | verif_fn.py | NO_REPRODUCIDA (no recalculado; otra base v3d legacy) |
- Base reproducida en la copia `v4_verif_dem.py`: 88 sim / 84 TP / 4 FP / 118 FN (idéntico a `validacion_primaria_BASE.json`).
- Calldata `matchOrders` (selector 0x3c2b4399, parse de cola_posicion/c7) de los 202 tx propios + 8.279 tx ajenos en ventanas de las órdenes ±31 s (RPC público vía polygon_rpc, 0 fallos).
- 98 FN clase 1 (sin print ajeno ≤L en el tx): 72 SOLO (nuestra orden fue el ÚNICO maker del tx), 24 SOLO_ARRIBA, 2 DEBAJO. Orden tomadora:
  límite en L exacto 49 / más allá 49; remanente >1 % en 60/98; la MISMA orden firmada no aparece antes en ningún tx 19-24 Oct (0/98);
  45 % firmada >5 s ANTES que nuestra orden (bots que prefirman; la demanda existía antes de nuestra cotización); 60/98 tomadores con otros tx tomadores en los 60 s previos (HFT, mediana ~9.000 tx/día).
- Clase 8 (11, cola): en 10/11 había puja > L a la llegada (motor: cola = INF y después TODO el tamaño en L del libro real, que incluye nuestra orden real y a quien llegó detrás); en 7/11 el operador nos casó ANTES que al otro maker en L.
- Clase 4 (8, tras cancelar): relleno real 1, 9, 18, 94, 164, 432, 679 y 868 ms después de t_end (3 dentro de la latencia p90 de cancelación de 74 ms).

## 3. Qué se puede sostener / qué NO
- SÍ: el print ajeno no puede ver los 72 SOLO: sin nuestra orden ese tx no existe; la orden tomadora es nueva en la cadena y los envíos no casados no son públicos. La información solo existe en NUESTRO tx (circular).
- SÍ (prerregistrado): COLA arregla 3 de cola sin FP. C150 (alargar la vida 150 ms por el retraso del tomador) queda REFUTADA: +6 TP y +18 FP.
- EXPLORATORIO (post hoc): la cinta de demanda residual (calldata) junto con COLA rescata +16 TP sin FP nuevos.
- NO: no se puede afirmar «ver todos». No se puede usar DEMall (+46 TP) porque lee nuestros propios tx.

## 4. Diagnóstico
Dominante: A (información). Los rellenos SOLO no dejan ninguna huella pública causal. Secundarios: B (medición), con el modelo de cola (INF y luego tamaño propio incluido), y E (la cola de delante se va por cancelaciones que el sa_ms de nivel 1 no ve; mismo hallazgo que R11 clase C).
Lo que NO resuelve el bloqueo: más filtros, otro sello de tiempo o una cancelación más larga (C150 refutada).

## 5. Hipótesis (HYPOTHESIS_LEDGER H-VT-1..5)
H-VT-1 cinta de demanda residual (calldata) · H-VT-2 cola mal modelada · H-VT-3 relleno tras cancelar = retraso del tomador · H-VT-4 SOLO visibles por demanda reciente ajena (hazard) · H-VT-0 nula: los FN son información inexistente sin nuestro tx.

## 6. Experimentos (out/V5_DEM_*.pkl, v7_resumen.json)
| variante | sim | TP | FP | prec | recall | ΔTP/ΔFP | EV TP real | EV FP motor | EV FN real | veredicto |
|---|---|---|---|---|---|---|---|---|---|---|
| base v3d | 88 | 84 | 4 | 0,955 | 0,416 | — | −0,111 | −1,00 | −0,041 | — |
| DEMr (prim.) | 91 | 87 | 4 | 0,956 | 0,431 | +3/0 | +0,008 | −1,00 | −0,143 | INCONCLUSO (ΔTP<5; placebo ±30 s +2) |
| DEMe | 88 | 84 | 4 | — | 0,416 | 0/0 | | | | prueba de consistencia pasada (ninguna demanda residual ajena llega a L mientras estábamos en el libro) |
| DEMall (CIRCULAR) | 134 | 130 | 4 | 0,970 | 0,644 | +46/0 | | | +0,122 | solo cota |
| COLA | 91 | 87 | 4 | 0,956 | 0,431 | +3/0 | +0,011 | | −0,145 | ACEPTA (adenda 1) |
| C150 | 112 | 90 | 22 | 0,804 | 0,446 | +6/+18 | | −0,41 | | REFUTADA |
| COLA_C150 / DEMr_COLA_C150 | 120/135 | 93/107 | 27/28 | 0,78/0,79 | 0,46/0,53 | +9/+23, +23/+24 | | | | REFUTADAS (ΔFP>ΔTP) |
| **DEMr_COLA (post hoc)** | 104 | **100** | 4 | **0,962** | **0,495** | +16/0 | +0,076 | −1,00 | −0,235 | EXPLORATORY |
| DEMr_COLA_p30 / _m30 | 98/104 | 89/90 | 9/14 | | | +5/+5, +6/+10 | | | | placebo |
Por día (DEMr_COLA vs base): 19/16, 44/39, 34/27, 3/2. TP a ±50 ms del relleno real: 63 frente a 45. EV de la simulación (Σpnl/Σcoste): −0,167 → +0,057; EV real −0,072.
Placebo frente a la regla escrita: el máximo ΔTP de placebo (6) supera ΔTP/3 = 5,3 por muy poco, así que la regla literal NO pasa. Restando la parte COLA, que comparten los placebos, el efecto DEM es +13 TP y 0 FP frente a +2/+3 TP con +5/+10 FP del placebo.
Hazard post hoc (v8): con demanda ajena reciente que llega a L, P(relleno) 5,36 % frente a 5,29 % sin ella (n 1.904/1.892), y P(invisible) 2,9 % frente a 2,1 %. No anticipa.

## 7. Solución experimental
`dem_hook.py` + `v4_verif_dem.py`, copia generada de verif_v5 (passT_v4/v5/verif_v5 sin tocar). Se inyecta un print sintético en L de tamaño S_T − acciones casadas con makers ajenos, solo en tx con ≥1 maker ajeno, sello v3 del tx. COLA: cola inicial = `cola` de B en t_dec si hay puja > L, y las filas en L menos nuestro tamaño (esto último solo vale para replay de órdenes reales).

## 8. Refutación intentada
Placebos ±30 s; DEMe como prueba de consistencia (0 FP); circularidad acotada con DEMall. Pendiente: validación independiente (validador/red-team) y una réplica con otros días de B (si los hay) antes de usar DEMr_COLA en contrafactuales.

## 9. Veredicto
Estado de cierre: PARTIALLY_SOLVED
Recall honesto máximo: 0,495 (100/202, precisión 0,962, exploratorio); prerregistrado aceptado: 0,431 (COLA).
Quedan sin ver 102 rellenos (EV real −0,235 €/€, es decir, los invisibles son perdedores, igual que R11 C):
- 72 SOLO: sin nuestra orden el tx no existe. Solo los vería una fuente de órdenes tomadoras NO casadas, que no es pública, o estar en el libro (el dry-run no sirve).
- 16 SOLO_ARRIBA y 4 de cola: 15/16 tenían puja > L y una cola de B en t_dec con mediana 16,5. La cola de delante se fue por cancelaciones; haría falta L2 por nivel (price_change del WS en L, no sa_ms de nivel 1).
- 8 tras cancelar: 3 dentro de la latencia p90; 5 entre 94 y 868 ms (hipótesis: tomador retenido en el taker delay e incancelable, o t_cancel_int del ledger distinto del envío real; hace falta el acuse de cancelación del ledger).
- 1 sin prints y 1 DEBAJO.
Economía: validada 0 €. El simulador sobreestimaba la pérdida de B en los TP; incorporar DEMr_COLA cambia el EV simulado de −0,167 a +0,057. Esa cifra NO es beneficio de B, porque los invisibles (−0,235) siguen fuera.

## 10. Siguiente paso exacto
(1) Validación independiente de DEMr_COLA (statistical-validator + red-team) con la regla prerregistrada y el placebo neto de COLA.
(2) Si hay L2 por nivel archivado para 20-23 Oct (cola_posicion/l2_agregado_* cubre 20-22), medir la cola de delante consumida por cancelaciones en los 20 de cola/SOLO_ARRIBA.
(3) Auditar el ledger de cancelaciones (acuse) de las 5 órdenes de clase 4 >74 ms.
Reabriría el caso: un feed de órdenes tomadoras no casadas, más días con órdenes reales de B o L2 por nivel.

---
# CONTINUACIÓN 18-Nov-2026 (reverse-engineer) — tras CONTRATO_VALIDACION_18nov (f85b1bb4…, RED)
Prereg: `ver_todos_17nov/PREREG_VER_TODOS_v2_18nov.md` (sha b3374be38c2f12ce…, escrito antes de ejecutar). Código: `dem_hook_v2.py`, `v9_verif_v2.py` (copia generada de v4_verif_dem; motor/sello sin tocar), `v10_resumen_v2.py`, `v11_hazard.py`, `run_v2.sh`; `MANIFEST_v2.sha256`, `STATUS_v2.json`. Salidas: `out_v2/`, `v10_resumen_v2.json`, `v11_hazard.json`.
C8: lo que antes se llamaba «invisible» pasa a llamarse **«no identificable ex ante con las fuentes archivadas»**. Se retira «firmada >5 s antes = estaba antes en el libro».

## R1. Reproducción
Base v3d con EXA=35 y EXC=33: 88 simulados, igual que antes (17/39/28/4 por día). Con la regla nueva de TP (q_sim ≥ 0,5·q_real) salen 82 TP + 2 parciales + 4 FP.
EV real de B (desenlace oficial): −0,0724 €/€ (n=202, 1.er relleno por token-lado; 221,3 € de coste; −16,02 €); −0,0174 por unidad.

## R2. Correcciones C1-C7 (configuración 35/33; incrementos medidos sobre COLA_viva; TP estricto)
| variante | sim | TP | FP | rec | rec_q | ΔTP | ΔFP | neto | neto por día 20/21/22/23 | veredicto |
|---|---|---|---|---|---|---|---|---|---|---|
| BASE | 88 | 82 | 4 | 0,406 | 0,431 | −3 | 0 | −3 | −1/−1/−1/0 | referencia |
| COLA (resta constante) | 91 | 85 | 4 | 0,421 | 0,451 | 0 | 0 | 0 | 0 | idéntica a COLA_viva |
| **COLA_viva** | 91 | 85 | 4 | 0,421 | 0,451 | — | — | — | — | referencia de los incrementos |
| DEMe_COLAv (S_T, sin tx propios) | 91 | 85 | 4 | | | 0 | 0 | 0 | 0 | 166 prints sintéticos y 0 efecto |
| **DEMt_COLAv** (tfill, C1+C2) | 91 | 85 | 4 | | | 0 | 0 | 0 | 0 | **REFUTADA**: 0 eventos con residual > 1e-3 |
| placebos DEMt ±30 s / rnd (20 semillas) | | | | | | 0 | 0 | 0 | | 0 eventos |
| **L2Q** (L2 por nivel, paso 2a) | 92 | 87 | 4 | 0,431 | 0,459 | +2 | 0 | +2 | 0/+2/0/— | **REFUTADA** (ΔTP 2 ≤ placebo máx. 3; los 2 con dt=0) |
| L2Q20 (reloj rx−20) | 93 | 87 | 5 | | | +2 | +1 | +1 | | |
| L2Q_opt (cota optimista) | 99 | 90 | 8 | 0,446 | 0,477 | +5 | +4 | +1 | 0/+2/−1/— | cota: ni así pasa |
| L2Q_p30 / L2Q_m30 (placebos) | 91/103 | 84/88 | 7/14 | | | −1/+3 | +3/+10 | −4/−7 | | |
Hechos que se pueden sostener:
- **C1/C2**: el residual calculado con takerFillAmount es exactamente 0 en todos los tx sin filas nuestras (4 días; DEMt elegibles 0 de 8.493 eventos). La cinta de calldata no aporta información pública ex ante. El +16 de DEMr_COLA era nuestro propio relleno reinyectado, como decía el contrato.
- **C3**: la sospecha 2c queda REFUTADA para COLA. COLA y COLA_viva dan resultados idénticos (0 diferencias). Sus 3 rescates sobre BASE (2 con dt=0 y uno con dt=+29,5 s) no salen de la resta constante: salen de la cola de B en t_dec y de un print ajeno en el mismo tx, que es público.
- **C4**: con COLA_viva, los placebos de DEMt valen 0 porque no hay eventos. En L2Q el placebo m30 da +3 TP y +10 FP.
- **C6 latencia** (TP/FP de COLA_viva): 35/33 → 85/4; 147/33 → 82/4; 35/74 → 89/13; 35/111 → 89/19; 147/111 → 85/19. Los FP pasan de 4 a 19 con la cancelación p90, y la precisión baja de 0,955 a 0,79 aprox. Clase de suelo de esos días: 94 % hi, y la latencia 35/33 viene del pool lo. La referencia hi pesimista (147/111) da 85 TP y 19 FP. Veredictos DEMt y L2Q: REFUTA en las 5 configuraciones.
- **C7** (sin sinev/amb: 3.642 órdenes y 110 reales): BASE 25 TP y 1 FP, COLA_viva 27/1, L2Q 29/1, DEMt 27/1. Se mantiene el mismo patrón.
- **C5 ventana endógena (HALLAZGO PRINCIPAL)**: con el tope de vida p90 de las no rellenadas (2.675 ms), COLA_viva baja de 85 a 48 TP y los FP se quedan en 4. Con el tope p50 (605 ms) quedan 20 TP. La causa, medida de forma descriptiva y post hoc (EXPLORATORY): **las 58 órdenes SIN cancelación son exactamente las 58 rellenadas por completo** (no se cancelaron porque se llenaron). El motor les da una vida hasta T_STOP (mediana 136 s después del relleno real) y aporta 52 de los 82 TP de BASE. 27 de ellos se rellenan en la simulación más de 178 ms DESPUÉS del relleno real, con otro estado del libro.
  Recall con ventana exógena (TP con tf ≤ real_tm3 + 178 ms): BASE 52/202 = 0,257, COLA_viva 56 = 0,277 y L2Q 59 = 0,292. En las órdenes con cancelación real, BASE ve 30 de 144 (0,21).
  **El 0,416 de recall estaba inflado por la ventana endógena.** EV real: TP con dt ≤ 178 ms −0,111 €/€ (n=52); TP de cola tardía −0,194 (n=30).

## R3. EV real por clase de FN (C8; 1.er relleno por token-lado; desenlace oficial; configuración 35/33)
| clase (FN de BASE / COLA_viva) | n | EV €/€ | EV por unidad | pnl € |
|---|---|---|---|---|
| 1 propio solo (no identificable ex ante) | 98 / 98 | **−0,176** | −0,061 | −17,52 |
| 8 cola no agotada | 11 / 10 | +0,956 / +0,634 | +0,873 / +0,534 | +10,92 / +6,59 |
| 4 relleno real tras la cancelación simulada | 8 / 8 | +0,313 | +0,302 | +2,86 |
| 6 sin prints | 1 | −1,00 | | −1,20 |
| TODOS los FN | 120 / 117 | −0,018 / −0,077 | +0,061 / +0,006 | −2,17 / −9,27 |
**Reconciliación del −0,235**: era el EV de los 102 FN de DEMr_COLA (v7_resumen.json), una variante circular. Al reinyectar nuestros propios rellenos, rescataba de forma preferente rellenos ganadores, y el resto quedaba más negativo. Es un artefacto. La cifra honesta del grupo no identificable ex ante es la clase 1: **−0,176 €/€ (n=98, 4 días, sin IC por días, INSUFFICIENT)**. Los FN de cola y de tras cancelar son GANADORES.

## R4. Paso 2a: L2 por nivel para la clase cola
Fuente: `datalogs/cola_vs_cruce/mk/` (libro5 por nivel con recepción en ms, ETH/SOL/XRP 5m, del 20-Oct al 22-Oct 16:15Z). Cubre 3.195 órdenes y 183 reales; el 23-Oct no tiene datos. Nuestra alta aparece en el L2 en el 93 % de los casos. Cola delante p50 = 41 acciones.
Con la semántica del motor (las cancelaciones salen primero de detrás), L2Q rescata 2 de la clase 8, los dos con dt=0, con 0 FP. La cota optimista rescata 5 a cambio de +4 FP. **Conclusión: las cancelaciones de quien iba delante, vistas en el L2 archivado, no explican los FN de cola.** Hay que tener en cuenta que esos FN son ganadores (+0,63/+0,96), así que no forman parte del problema de selección adversa.

## R5. Paso 2b: modelo de llegada de tomadores (hazard)
20.103 intervalos de 250 ms con 190 positivos. Logística L2, leave-one-day-out, rasgos solo con datos ≤ t, sin NaN. Brier skill por día: +0,016, +0,014, −0,069 y +0,032 (3 de 4 > 0). AUC por día: 0,69, 0,74, 0,80 y 0,86; total 0,739. Fiabilidad por decil: monótona en general (decil 9: p 0,045 frente a y 0,037). Según el criterio prerregistrado sale **ÚTIL**.
Coeficientes estables en los 4 días: distancia bid−L (−), tamaño en top (−), r5 a favor de nuestro token (−) (el relleno llega cuando el subyacente va en contra) y T a cierre (−).
Separación entre perdedores y ganadores en el intervalo del relleno: AUC 0,553 (por día 0,50/0,47/0,59/0,58). **NO separa la selección adversa** según el criterio (≥ 0,60). Exploratorio: EV de los rellenos por tercil de hazard: bajo +0,26 (n=64), medio −0,27 (n=63), alto −0,22 (n=63).
No distingue los rellenos visibles de los no identificables (AUC 0,502). Por eso puede servir para imputar en la fase 2 sin sesgo en esa dimensión, pero no para filtrar perdedores.
F5: en estos días el 94 % es hi, así que F5 cancelaría casi todo y no se puede medir aquí cuántos no identificables evitaría. Hace falta el estado del detector W12_C30 por orden en días lo con órdenes reales, y esos días no existen.

## R6. Veredicto 18-Nov
Prereg v2: **DEMt_COLAv REFUTADA** (residual con tfill = 0: no hay información pública ex ante en la cinta). **L2Q REFUTADA** (ΔTP 2 ≤ placebo 3) en las 5 latencias.
COLA_viva queda como motor de referencia, ya que la sospecha 2c no se sostuvo. Medición: el recall de referencia se recalcula con ventana exógena a 0,26-0,29 (EXPLORATORY: necesita prereg v3 y validador).
Estado de cierre: **HYPOTHESIS_REFUTED** (para «ver más rellenos con fuentes públicas archivadas»), con un hallazgo de medición (B) que corrige a la baja la cobertura del simulador. Los 98 de clase 1 (−0,176 €/€) son no identificables ex ante con las fuentes archivadas.
Economía: validado 0 €. Nada de esto es EV de B.
Siguiente paso exacto: (1) validador independiente con un contrato v3 que fije la métrica de recall con ventana exógena (tf ≤ real_tm3 + 178 o vida contrafactual de las órdenes sin cancelación) y repita C5. (2) Para fase 2, imputar con el hazard v11 los rellenos no identificables y medir su EV con el desenlace oficial; el tercil bajo +0,26 hay que verificarlo con prereg. (3) Reabriría el caso: un feed de órdenes tomadoras no casadas, días con órdenes reales en régimen lo o un L2 de ambos tokens del 23-Oct.
