# PAUSA_RAM_27nov: piezas paradas / cambios de infraestructura (OK Javi 27-Nov 12:10Z, puntos 1-3)

Objetivo: bajar la presion de RAM/swap antes de P1b B (15:15Z, `at 89` -> `paquete_l/p1b_programado.sh B`). Ningun dato perdido.

## Paradas (PAUSADO-27NOV-RAM)
| Pieza | Como se lanzaba | Datos (se conservan, solo dejan de crecer) | Por que se puede parar |
|---|---|---|---|
| screen `freezeestado` (`resolution_sniper_freeze_estado_fase0.py`, ~350 MB RSS+swap) | screen, comando en `pipeline_watchdog.py::SCREEN_RESTART["freezeestado"]` | `data/shadow/resolution_sniper_freeze_estado_fase0.csv` (+ rotados), `logs/resolution_sniper_freeze_estado_fase0.log` | Fase 0 observacional del instante de cierre del exchange; ningun lector de datos (solo `buscador_grietas_polymarket.py` lo cita en un texto, y `comprimir_data_historica.sh` lo rota). PRECIERRE/NAIVE live (`resolution_sniper_precierre_executor.py`, screen `precierre`) no lo importa ni lo lee. No esta en BRIEFS_COLA_25nov ni MATRIZ_B_SUBVARIANTE_25nov. |
| screen `curvacierre` (`resolution_sniper_precierre_curva_cierre_fase0.py`, ~340 MB) | screen, `SCREEN_RESTART["curvacierre"]` | `data/shadow/resolution_sniper_precierre_curva_cierre_fase0.csv`, `logs/resolution_sniper_precierre_curva_cierre_fase0.log` | Idem (la validacion 9-24 Sep de la que parte NAIVE-TWAP ya esta hecha; el executor solo la cita en un comentario). |

Coherencia (todo para que ninguno se relance ni de falsos avisos):
- `pipeline_watchdog.py`: quitados de la lista de `check_screens()` (misma tecnica que walletmirror/sportsfase0 el 17-Nov); `SCREEN_RESTART` intacto para reactivar. Watchdog reiniciado a mano (screen `watchdog`, 12:07Z). Efecto colateral esperado: `vigiasfreq` pasa a STALE (importa pipeline_watchdog) y el watchdog lo reinicia solo (cooldown 10 min).
- `vigia_loggers_silenciosos.py`: conjunto `PAUSADOS_RAM_27NOV` (los 2 CSV) para no avisar de "logger silencioso".
- `verify_deploy.py`: SIN cambios. Mostrara `freezeestado`/`curvacierre` como CAIDO (igual que walletmirror/sportsfase0 desde el 17-Nov); no cuenta como STALE en `salud_sistema_diaria`. (Editarlo marcaba vigiasfreq STALE otra vez.)
- Sin cron propio. `inventario_sistema.py`: sin cambios (las clasifica como screen del watchdog).
- Backups pre-cambio: `/root/polymarket-research-datalogs/archivo_scratch_27nov/bak_pre_pausa/`.

## Reactivar
1. En `pipeline_watchdog.py::check_screens()` volver a anadir `"freezeestado"` y `"curvacierre"` a la lista; en `vigia_loggers_silenciosos.py` vaciar `PAUSADOS_RAM_27NOV`.
2. Reiniciar el watchdog: `screen -S watchdog -X quit; screen -dmS watchdog bash -c "cd /root/polymarket-research && python3 pipeline_watchdog.py"` (o esperar a que lo haga `watchdog_fast.sh`).
3. El watchdog las lanza solo (o a mano: `python3 verify_deploy.py --restart freezeestado` / `--restart curvacierre`). Los CSV siguen en append.

## NO parados (decision / dudoso)
- `f2_5m_barato_dryrun.py` x2 (Javi 27-Nov: se quedan; hay que medirlos con passT_v4). Pids 183634 (alt) y 1320711 (BTC); datos `datalogs/f2_5m_barato/f2_D.jsonl` + `f2_ledger_*.jsonl`.
- `h23_shadow.py` (v1) y `h23_shadow_v3.py`: NO parado. v3 emite un superset de variantes (join, join_150, join_r, nc) pero con tamano/universo distintos (acciones_real, p en [0,10-0,60], sin puja nueva con T<=12 s), y `v3/PREREGISTRO.md` linea 29 cita como forward «shadow `h23shadow` + ensayo en seco v3»; ademas `paquete_real/experimento_maker_h23.py` importa `h23_shadow.py` (el FICHERO, no el proceso). Dudoso -> se deja y se anota.

## Otros cambios de esta tanda
- Scratchpads antiguos de `/tmp/claude-0/-root-polymarket-research/` (57 sesiones, 1,5 GB) movidos con `cp -a` + `diff -r` a `/root/polymarket-research-datalogs/archivo_scratch_27nov/` y borrados de tmpfs. NO tocados: 27e63a6d..., ef0f068e... y los ficheros sueltos de `/tmp/claude-0/` (cola_q_*.csv, etc.).
- `scripts/reinicio_limpio_shadows.sh`: BUG hallado. El cron `3,33` no hacia nada desde el 14-Nov 15:03 porque `f2 alt` (pid 183634) heredo el fd 8 (`/tmp/reinicio_limpio_shadows.lock`) al relanzarlo el propio script y retiene el flock (`flock -n 8 || exit 0`). Parche: los dos relanzamientos llevan `8>&-`. El lock sigue retenido por el pid 183634 hasta que ese proceso se reinicie o se retire el fichero de lock (ver informe).
- P1b: `paquete_l/p1b_lock.sh` + `p1b_programado.sh` (flock global de cron_pesado durante preflight+lanzamiento), umbral de swap-in del preflight recalibrado. Ver cabeceras.

## Calibracion del preflight de P1b (27-Nov 12:08-12:23Z, /proc a 1 Hz, host quieto, n=295 y n=355 ventanas de 5 s)
swap-in p50 37-84 | p90 425-431 | p95 864-904 | p99 2.161-3.228 | media 174-205 pag/s (antes del alivio ~1.300). Nuevo criterio: ventana <=1.000 y media de la racha <=450 (antes 400 por ventana).
PSI cpu some avg10 (mismo muestreo): p50 5,4 | p90 12,9 | p95 19,6; el umbral PSI_CPU_MAX=8 NO se ha tocado y es el que mas bloquea (pasa ~60 % de los instantes con host quieto; 4 % si hay trabajo mio en paralelo).
Sin dinero real: p1b_programado.sh NO se ha ejecutado; probado p1b_lock.sh (5 tests) y el preflight (11 tests) en `paquete_l/`.
Para parar el bug del flock de reinicio_limpio_shadows (reactivar el reinicio sin perdida de h23v3/h23/r3/F2): `rm /tmp/reinicio_limpio_shadows.lock` (el pid 183634 conserva el inodo viejo; el cron crea uno nuevo). No hecho: reiniciaria F2/r3.

## Reinicio limpio reactivado (27-Nov 12:31-12:35Z, OK Javi)
- Quitado `/tmp/reinicio_limpio_shadows.lock` (retenido por f2 alt 183634) y ejecutado `UMBRAL_MB=250 scripts/reinicio_limpio_shadows.sh` en la ventana tras el cierre de las 12:30 (h23v3, h23, f2 alt) y la ventana de r3 (12:34:22-28). F2 BTC no se tocó (185 MB < umbral). Script: `UMBRAL_MB` ahora sobreescribible por entorno (defecto 450) y `8>&-` en los relanzamientos. Cron :03/:33 operativo (12:33:01 abrió el lock nuevo y salió porque el manual lo tenía).
- Parada→proceso nuevo: h23v3 0,9 s, h23 0,8 s, f2 alt 3,9 s, r3 0,8 s; primera escritura posterior en <=15 s.

## RF5 25-Nov FAILED -> COMPLETE (27-Nov 12:36-13:10Z)
- Causa: MemoryError por `ulimit -v 5000000` con RSS solo ~3 GB: pandas 3.0.3 importa pyarrow y su pool de memoria (mimalloc) reserva 2 mapeos anonimos de 1 GiB (uno casi vacio, RSS 172 kB) => 5 GB virtuales. No era BLAS (Threads=2 con OMP=1 y seguia fallando) ni un insumo nuevo.
- Arreglo por entorno (sin tocar sellados ni el ulimit): `ARROW_DEFAULT_MEMORY_POOL=system`. A del 25-Nov: VmPeak 3,1 GB, COMPLETE (12:46:20Z). K en el mismo proceso que A vuelve a fallar (VmPeak 4,5-4,8 GB, RSS 4,4); en proceso nuevo K entra (VmPeak 3,4 GB) y queda COMPLETE (13:00:05Z); rf5dia COMPLETE, sha de las 3 salidas = manifest, codigo = HASHES_rf5.txt (83 OK).
- Crontab 12:30 (backup /root/crontab_backup_27nov_pre_rf5_env.txt): env anti-arena + `bash -c 'R=run_rf5.sh; "$R" || "$R"'` (2o intento en proceso nuevo). Evidencia del fallo: out_rf5_ciego/pico_dia_2026-11-25.txt.fail_MemoryError_27nov_1231Z (y .A_run_12h46Z...).
