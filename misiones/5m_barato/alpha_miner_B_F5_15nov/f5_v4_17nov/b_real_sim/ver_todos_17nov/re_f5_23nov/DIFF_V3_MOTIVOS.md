# DIFF_V3_MOTIVOS -- HASHES_rf5 v3 (24-Nov-2026) -- ADENDA_RF5_INTERINA_24nov sec.4, condicion 2
Referencia: `git diff 19965ec6ef6 -- <fichero>` (v2 = HASHES_rf5.txt.v2, identico al commit 19965ec6ef6). Una linea de motivo por cambio. Nada de lo cambiado lee EV/PnL ni pkl/manifest de dias >=18-Nov; ninguna ruta nueva a precintos (`PRECINTO` en rf5_eval.py es de la linea base 19965ec6ef6, sin tocar). NO firmado: lo firma el chief tras el validador.
Parametros intactos (cond. 5): rf5_cortes.json (sha 4e88fb3c, tabla de suelo 18..23 firmada por el chief 24-Nov, no tocado por esta ronda), alfa, gates, unidad, L_cancel, t_proc (4355a46b), semilla. K_max, h y las fronteras Pocock NO viven en rf5_cortes.json: viven en `rf5_fronteras.py` (codigo hasheado).

## A. Cambios de la ronda 1 (ya en disco, 23-Nov 20:57-21:16Z) -- motivo
- rf5_core.py: politicas K6 (Calma como 3.er componente de HookRF5), `quien` por componente, tabla POLITICAS_NULO_*; (ESPEC_HOOK_CALMA_V4 sec.2/5).
- rf5_run.py: trabajo rf5K6 + `_replay` con simulador rapido (rf5_rapido), huecos del motor/Binance, desenlace con marcador (C3 peor caso); (ESPEC_ENGINEER E5/E3).
- rf5_eval.py: peor caso de desenlace, sensibilidad a huecos (E5), por_bloque_4h; (ESPEC_ENGINEER E5, ADENDA_CRITERIOS_v2 C1).
- rf5_nulo.py: Besag-Clifford h=20, nulo por re-simulacion con series Binance desplazadas, `rng_perm` determinista por (dia, j), checkpoint JSONL durable; (DICTAMEN test 3/4, firma chief 23-Nov).
- rf5_acople_real.py / cobertura_bruta.py / vigia_rf5.py / test_rf5_p1.py / test_rf5_nulo.py: acople real busy/MAXV medido en 17-Nov, cobertura sin filtrar horas, vigia R6/R7 de K6; (ADENDA_CRITERIOS_v2 C1, ESPEC E4).
- Ficheros nuevos de la ronda 1: rf5_rapido(_prueba).py (aceleracion memoizando run_segment + 3 sustituciones equivalentes), rf5_k6_dia.py (juez Calma v4), rf5_nulo_run.py (nulo por re-simulacion), calma_hook.py/calma_gate.py (sha c66ce9de), c4_btc.py, c4_equiv_lowmem.py, prep_day_btc.py, reconstructor_relleno.py, btc_backfill.sh, lanza_pesado.sh, run_k6.sh y sus test_*.

## B. Cambios de ESTA ronda (24-Nov)
1. rf5_core.py `construye_hook(..., bsrc_calma=None)`: CAUSA RAIZ del bloqueante K6. El ensayo «K6 con Calma vacia == K1» (rf5_rapido_prueba.py) pasaba la serie vacia como `bsrc`, que alimenta tambien a V5/V6 => V5/V6 ciegos => 17.600 ordenes (= F3 solo) frente a 8.272 de K1. Con `bsrc_calma` se anula SOLO a Calma; en produccion (K6) Calma y V5/V6 comparten la misma fuente (comportamiento sin cambio). Test que fallaba antes: test_calma_hook.py::test_K6_con_calma_vacia_no_ciega_V5_V6_causa_raiz_bloqueante_24nov.
2. rf5_rapido_prueba.py: usa `bsrc_calma=vac`; contadores del MOTOR por replica (antes la rapida acumulaba 2 pasadas frente a 1 de la lenta: el falso `cont_motor_igual=false`); `todo_igual` incluye fills/f5/cont/tau; caso K6_tq0 (sensibilidad tq = t).
3. rf5_fronteras.py (nuevo): fronteras Pocock-LD, IC t de Student por dias, regla de mirada (6.o dia valido / 10.o), K_max 1500 (K) y 2000 (A), h=20, semilla 20261124 (ADENDA INTERINA sec.6 D1/D3).
4. rf5_eval.py: MIN_DIAS 6, `decide_mirada`, umbrales por mirada (p_max, IC t por dias, IC por cierres con B>=5000 al nivel, dias>0 >=4/6 | >=6/10, vs azar 0,0709|0,0617), nunca REFUTADA en la mirada 1, final REFUTADA/NO_CONFIRMADA_A_10, p de la SIMULACION COMPLETA (lee nulo_{A,K}_resultado.json solo si coinciden dias y mirada), K_PERM=2000; notas de alcance (23-Nov INCOMPLETE, suelo no sustituye bad_D, hi sin datos); (ADENDA INTERINA sec.1,2,3,5,6).
5. rf5_nulo_run.py: motivo del nulo por simulacion completa (acople real busy/MAXV) escrito en el codigo; K_max por familia; `identidad DIA FAM` (replica con el par F5_0 observado y desplazamiento 0 == politica directa, bit a bit); `corre` toma los dias de decide_mirada (no por argumento) y comprueba K_max >= 5/umbral; (ADENDA INTERINA sec.1).
6. rf5_nulo.py: docstring + `permuta_asignacion` (permutacion de mercados dentro de dia x moneda, una sola por (dia,j) compartida por todas las politicas; `permuta_pares` la reutiliza, mismo resultado y mismo rng_perm). Motivo: la prueba de identidad del 24-Nov mostro que con acople busy/MAXV la F5_0 de un lado depende de la politica (K1 intenta lados que la base no: 8.272 vs 8.201 ordenes con el par de la base), asi que cada politica necesita SU tabla F5_0 observada.
7. rf5_run.py: `FICH_EXT` + `verifica_registro` y `code_hashes` cubren lo externo (b_policy_sim, eng_v5, ejecutor_puro, r1v2_eval/*, r1v2_sec7/*, engine_v3/v4/clock, passT_v4, relojes, stamp_v3, ms_extract(_v2/_lowmem), suelo_causal, cron_pesado.sh, y DEV prep_day.py + reconstructor); `rf5_fronteras.py` en FICH_REG; (ADENDA INTERINA sec.4 cond.1).
8. run_rf5.sh / run_k6.sh: si se agota la espera de RAM/ventana el dia se ABORTA (antes se ejecutaba igualmente), rc=1 (el `|| vigia --aviso-*` del cron avisa) y marcador abortado_<dia>.json; retencion 30 d en run_rf5.sh; (orden chief 24-Nov, minimo 6).
9. btc_backfill.sh: `c4_equiv_lowmem` sobre 17-Nov pasa a ser PUERTA previa (sha de scripts vigentes) antes de extraer cualquier btc_ms nuevo; si no pasa: BLOQUEADO_EQUIV, exit 1; (orden chief, 4).
10. desagrega.py, gap_mark.py, q4_entrada.py, t0_refuta.py (+ .sha256): glob `p0_ordenes_*` restringido a dias < 2026-11-15; (orden chief, 6; cond. 3).
11. test_rf5.py, test_rf5_p1.py: test de 5 dias en vez de 9 (mirada 1 = 6 dias); test de la tabla de suelo a la firmada 18..23 (sha 742ccfea).
12. Tests nuevos: test_rf5_fronteras.py (10), test_run_scripts.py (3; el camino feliz salta si la cola global cron_pesado esta ocupada), test_calma_hook.py (+1), test_rf5_nulo_run.py (+2: asignacion biyectiva por moneda y comparacion `igual` solo ignora la etiqueta `pol`), test_c4_equiv_lowmem.py (2, nuevo).
13. rf5_nulo_run.py (tras el hallazgo de identidad): `SimNulo.tablas` (F5_0 por politica: la de su replica directa y, para lados que esa no intenta, la de base/VETO_UP/VETO_DN), `_ctx/identidad/__call__/ensayo` reutilizan el E ya construido (2 x ~3 GB reventaba ulimit -v 5 GB), `difiere` (diagnostico por columna), `igual` ignora solo la etiqueta `pol` (`F1_SET` vs `F1`: era la UNICA columna distinta en las 19.542/2.956/17.600/17.493 filas de A y en K).
14. c4_equiv_lowmem.py: `iguales_bit` (bytes) en vez de `np.array_equal`: los float32 q_v0..q_v3 llevan 482.763 NaN y array_equal da False aun con patron identico (causa del DIFIERE del 24-Nov 10:01Z; q_k/q_t/t* ya eran iguales). Sin esto btc_backfill se bloqueaba para siempre.
## C. Fuera de D (reeval CXB60, experimentos/5m_barato/l2_carrera_10nov/reeval_cxb60_passT_v4/; NO lo importa ni lo lanza el runner RF5; sha informativos al final de este fichero)
- huecos_cxb60.py: declaracion de feed (filas q+t de todos los tokens de la moneda), reloj de recepcion (q c[7], t recv), UNA ventana PRE_S=332 (el 300 queda retirado; justificacion: 300 s de mercado + 32 s de calentamiento vol30/b300 del runner).
- huecos_real.py: lector real de maker_ms (union datalogs/crudo sin ficheros vacios ni enlaces rotos), ventana unica, ficheros usados en el JSON, ADAPTADOR de la reeval (huecos_mercados_D.json por mercado con `excluir`).
- tests: test_huecos_cxb60.py, test_huecos_real.py (+2).

## D. Evidencia (24-Nov, dia 2026-11-17, datos no ciegos; sin EV/PnL)
- K6==K1 bit a bit: out_rf5_ciego/rapido_2026-11-17_K.json todo_igual=true; k6_calma_vacia_vs_K1 ordenes 8272, distintas_de_K1=false (antes 17.600 vs 8.272); K6_tq0 igual_fria/caliente true.
- Aceleracion bit a bit: rapido_2026-11-17_A.json y _K.json: lenta == rapida (fria y caliente) en F3/base/bloq1 y K1,K6,CALMA,K6_tq0,bloq1_K1; contadores del motor iguales.
- Identidad del nulo: nulo_identidad_A_2026-11-17.json F1/F2/F3/U13 igual=true (19.542/2.956/17.600/17.493 ordenes); nulo_identidad_K_2026-11-17.json K1..K4 igual=true (8.272/9.207/1.682/8.273). Estado previo (hallazgo) en nulo_identidad_K_2026-11-17.json.hallazgo_par_de_la_base_24nov.
- BTC: rf5_btc/equiv_lowmem_2026-11-17.json igual=true con sha_lowmem da09d166.. / sha_orig e66559cc..; btc_backfill reanudado 10:16Z (log btc_backfill_20261124.log).
- huecos real 13..17-Nov: out_rf5_ciego/v3_huecos.log, 5/5 dias OK, vac_max_nuevo p50 = 1 s (frente a 57 s del runner), aceptacion p50<10 s true.
- Ensayo de coste del nulo (K, 2 permutaciones, 17-Nov): 24,7 s por dia-replica (incl. build de E; cola compartida), 4 politicas/permutacion.
### sha de los ficheros fuera de D (reeval CXB60)
- 6660f03e3801b69e2e1633b19984d0850a432b80d0b952a62aa736bb45732227  huecos_cxb60.py
- 7b200f20166201c9698b3fded57ef311db3aaeacaf6e357fb98cfa3df4503982  huecos_real.py
- fe548d1bee9ff9325c0b6d18704d7e4ad120969b001064b06524263320f76e70  test_huecos_cxb60.py
- f463c016429a27144d21e8ee04be5772d282b673f089ce2ac2b9893487e74f36  test_huecos_real.py
