# REANUDAR_V31 (24-Nov, corte 13:50Z) -- estado exacto de RF5E-COMB-23NOV-v1 v3.1 (NO FIRMADO)
Rol: cheap5m-execution-engineer. Directorio D = este. Nada de esto abre precintos, pkl ni manifiestos ciegos; 0 ordenes, 0 red.

## HECHO (en codigo, tests en verde, ver DIFF_V3_MOTIVOS.md seccion E, items 23-29)
- C1: eventos (saltos Calma, disparos V5/V6) calculados UNA vez sobre la serie original y solo sus TIEMPOS se rotan en [d0, d0+24h) (`rf5_nulo.desplaza_eventos`, via `construye_hook(ev_shift=...)`; compartida por SimK6.una y SimNulo.una; `desplaza_circular` eliminada). Bordes declarados en el docstring de rf5_nulo.py y en DIFF 23.
- KMAX: {'K':250,'K6':1100,'A':500}; solo K y K6 bloquean la mirada (`rf5_eval.BLOQUEAN_MIRADA`); A no bloquea.
- C2: FICH_REG += rf5_nulo_inc.py, run_nulo_inc.sh, cron_nulo_inc.txt; verifica_registro fail-closed (cola/dia/equiv/ident/corre); sello de codigo + K_max en cada replica y en el estado; rechazo de otro sello/K_max en lee_sellado/lee_replicas/agrega/lee_nulo; workers=1 fijo.
- C3: nulo K6 sobre `dias_k6` (`rf5_nulo_inc.mirada_k6`: 6.o/10.o dia valido de K6; pendientes esperan; >20 % no evaluables => K6_INSUFFICIENT).
- C4: Bretz persistente (`rf5_eval.k1_rechazada_persistente`, fichero `rf5_k1_mirada1.json` de escritura unica).
- C6: vs_azar 0,07085/0,06165; docstring rf5_eval l.6.
- Tests: 142 passed (todos salvo test_run_scripts) incl. test_rf5_v31.py (11 nuevos) y 2 nuevos en test_rf5_nulo.py. HASHES_rf5.txt v3.1 regenerado (83 entradas, sha256sum -c 0 fallos; .v2 intacto). NO FIRMADO.

## PRUEBAS REALES 17-Nov (pesadas, via lanza_pesado, una a la vez; cola en scratchpad cola8.sh; log out_rf5_ciego/v31_cola.log)
Todas VERDES, sello de codigo 801394fed66753c1 (= HASHES v3.1 vigente; el codigo no se toco tras las pruebas), un solo proceso, workers=1:
- (a)+(b)+(c) K: nulo_inc_ident_K_2026-11-17.json verde: identidad delta=0 PASANDO por desplaza_eventos == directa bit a bit K1/K2/K3/K4 (8.272/9.207/1.682/8.273 ordenes); 5 replicas (delta_perm j=0..4): rotacion_ok y numero de eventos V5 y V6 de la replica == observado EXACTO por moneda (V6: eth 476.899, sol 111.469, xrp 83.821).
- (a)+(b)+(c) K6: nulo_inc_ident_K6_2026-11-17.json verde: K6 con delta=0 por el desplazamiento == K6 directo bit a bit (5.291 ordenes = 5.291); 5 replicas: rotacion_ok y numero de saltos de Calma == observado exacto (eth 10.809, sol 33.878, xrp 28.257).
- (d) equiv repetidas: nulo_inc_equiv_K_2026-11-17.json y nulo_inc_equiv_K6_2026-11-17.json todo_igual=true (3 replicas, incremental == bloque, bit a bit). Logs: out_rf5_ciego/v31_*.log y v31_cola.log; picos de RAM v31_pico_*.txt.
- Familia A (repetida tras v3.1, mismo sello 801394fed66753c1): nulo_inc_equiv_A_2026-11-17.json todo_igual=true (3 replicas, incremental == bloque) y nulo_identidad_A_2026-11-17.json todo_igual=true (F1/F2/F3/U13: 19.542/2.956/17.600/17.493 ordenes, bit a bit).

## PENDIENTE (manana)
1. Si alguna prueba real de arriba no esta en verde o no corrio: relanzar `bash <scratchpad>/cola8.sh`-equivalente: `RF5_OUT=$D/out_rf5_ciego/ bash lanza_pesado.sh LOG PICO python3 -I rf5_nulo_inc.py ident K|K6 2026-11-17` y `... equiv K|K6 2026-11-17 --K 3` (uno a uno, nunca 06:00-09:15Z). NO editar codigo del nulo sin re-hashear (cualquier edicion invalida HASHES -> las ejecuciones escriben BLOCKED) y sin repetir las pruebas (cambia el sello).
2. Revision del validador de v3.1; luego firma de HASHES por el chief (python3 scratch mkhashes.py desde D regenera; no firmado).
3. Reprocesar 18-22 Nov con el codigo final: out_rf5_ciego_v3/ se genero con el codigo ANTERIOR a v3.1 (INCOMPLETE por cobertura de datos, no por codigo); ya_completo reprocesa si cambian los code_hashes. Las salidas v2 estan en out_rf5_ciego_v2_24nov/ (intactas). OJO: un cron a las 12:30Z con RF5_OUT por defecto puede reescribir out_rf5_ciego/ (v2).
4. Instalar el cron del nulo (el chief): cron_nulo_inc.txt (09:20Z y 22:35Z, `|| vigia --aviso-nulo`), sin RF5_NULO_WORKERS. Primer dia con replicas: dias COMPLETE >= 24-Nov (el primero valido posible es el 25-Nov).
5. Coste del nulo con K_max nuevo: ver ENMIENDA_RF5_NULO_KMAX_24nov.md (K ~6 h + K6 ~7 h + A solo con cola libre) por dia de datos; un solo proceso (RAM).
6. El backfill BTC sigue en marcha (btc_backfill.sh PID 2734050 en out_rf5_ciego/btc_backfill.pid, setsid, idempotente con su flock); `TAPES_SHA256_btc.txt` lo modifica: NO se ha commiteado.

## ESTADO EXACTO POR FICHERO (D)
- Modificados y COMMITEADOS: rf5_nulo.py, rf5_core.py, rf5_run.py, rf5_eval.py, rf5_fronteras.py, rf5_nulo_inc.py, rf5_nulo_run.py, rf5_acople_real.py, run_nulo_inc.sh, cron_nulo_inc.txt, test_rf5_nulo.py, test_rf5_nulo_inc.py, test_rf5_fronteras.py, test_rf5_v31.py (NUEVO), HASHES_rf5.txt (v3.1, no firmado), DIFF_V3_MOTIVOS.md, REANUDAR_V31.md.
- NO commiteados a proposito: TAPES_SHA256_btc.txt (lo escribe el backfill), out_rf5_ciego*/, scratch_p1/, suelo_sucesora/, hbgap.sha256.pre_fix_carga, ENMIENDA_RF5_NULO_KMAX_24nov.md (fichero del chief, sin sha registrado).
- rf5_cortes.json NO tocado (sha 4e88fb3c8da7). rf5_t_proc_ms.txt intacto.
