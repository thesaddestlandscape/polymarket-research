#!/bin/bash
# run_exp1.sh v4 (15-Nov 19:15Z; v3 + env de asignador glibc para bajar el pico de e2_dia + no reintentar dias con assert de integridad) [v3 18:40Z] -- EXP-1 (ADDENDUM1_B_F5, sha en ../ADDENDUM1_B_F5.sha256). UN solo job, idempotente; lo lanza supervisor_exp1.sh por la cola pesada:
#   /root/polymarket-research/scripts/cron_pesado.sh nice -n 19 ionice -c3 bash <este fichero>
# v1 (17:40Z) murio a las 18:24:43Z por el OOM-killer del kernel (swap 100 %; victima preferida adj +500; el orquestador bash cayo tambien). Directrices del chief (18:35Z): no rehacer E1/E3x/E7 (COMPLETE); esperar calma
# (load1<=8 y MemAvailable>=3500 MB) antes de CADA fase pesada; ulimit -v 2,2 GB; oom_score_adj +500 propio; un dia matado por OOM se reintenta UNA vez en una segunda pasada tras recuperar la calma (no de inmediato, no en bucle);
# un dia que no cabe (MemoryError) o cuyo assert de integridad C3/C5/C7 falla queda FAILED/INCOMPLETE y se lista, nunca se rellena.
# Orden: e3_reglas (si no COMPLETE; solo B real) -> E2 por dia (08-Oct..14-Nov, solo los no COMPLETE con el mismo hash) -> segunda pasada -> e2_agrega -> e5_regimen -> e6_brecha -> audit_final.
# Guardas: no arranca trabajo nuevo entre 06:00-09:15Z ni a partir de las 01:45Z (cron pesado 02:15Z y deploy v3 04:10Z del 16-Nov). Solo lectura de insumos; 0 ordenes; no toca v3/, dry-run, dev, libro_estado_ws.py.
H=/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/exp1; LOG=$H/run_exp1.log; cd $H || exit 9
[ -n "$DRYRUN" ] && LOG=/dev/stdout
echo 500 > /proc/$$/oom_score_adj 2>/dev/null
ulimit -v 2200000
export MALLOC_ARENA_MAX=2 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1
export MALLOC_MMAP_THRESHOLD_=262144 MALLOC_TRIM_THRESHOLD_=262144 MALLOC_TOP_PAD_=0   # arrays grandes por mmap y devueltos al SO al liberar (menos RSS/VSZ de pico; solo asignador, sin cambio numerico)
fuera_de_hora() { h=$(date -u +%H%M); { [ "$h" -ge 0600 ] && [ "$h" -lt 0915 ]; } || { [ "$h" -ge 0145 ] && [ "$h" -lt 0600 ]; }; }
calma() {  # hasta 45 min; 0 = maquina compartida en calma (load1<=8 y MemAvailable>=3500 MB), 1 = agotado u hora prohibida
  for i in $(seq 1 45); do
    fuera_de_hora && return 1
    l=$(awk '{print $1}' /proc/loadavg); a=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo)
    awk -v l="$l" 'BEGIN{exit !(l<=8.0)}' && [ "${a:-0}" -ge 3500 ] && return 0
    [ -n "$DRYRUN" ] && return 0
    sleep 60
  done; return 1
}
fase() { n=$1; shift; echo "$(date -u +%FT%TZ) INICIO $n load1 $(awk '{print $1}' /proc/loadavg) MemAvail_MB $(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo)" >> $LOG
  if [ -n "$DRYRUN" ]; then echo "   DRY: $*"; return 0; fi
  /usr/bin/time -v -o $H/time_$n.txt "$@" >> $H/out_$n.txt 2>&1; rc=$?
  echo "$(date -u +%FT%TZ) FIN $n rc=$rc maxrss_kB=$(awk -F: '/Maximum resident/{gsub(/ /,"",$2);print $2}' $H/time_$n.txt 2>/dev/null)" >> $LOG; return $rc; }
echo "$(date -u +%FT%TZ) ===== run_exp1 v3 pid $$ load1 $(awk '{print $1}' /proc/loadavg) MemAvailable_MB $(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo)" >> $LOG
completa() { grep -A1 "\"$1\"" $H/STATUS.json 2>/dev/null | grep -q '"estado": "COMPLETE"'; }
limpia() { rm -f $H/cache/${1}_q.gz $H/cache/${1}_q.tmp.gz $H/cache/${1}_t.csv $H/cache/${1}_k.csv $H/cache/${1}_bn.csv $H/cache/${1}_ktokprev.txt; }
completo_d() {  # mismo criterio que e2_dia: COMPLETE + mismo hash de codigo + mismo addendum + pickle presente
  cs=$(sha256sum $H/e2_dia.py | cut -c1-16)+$(sha256sum $H/lib1.py | cut -c1-16); as=$(cut -c1-8 $H/../ADDENDUM1_B_F5.sha256)
  grep -q '"estado": "COMPLETE"' $H/cache/pob_$1.json 2>/dev/null && grep -q "\"code\": \"$cs\"" $H/cache/pob_$1.json 2>/dev/null && grep -q "\"addendum\": \"$as\"" $H/cache/pob_$1.json 2>/dev/null && [ -s $H/cache/${1}_pob.pkl.gz ]; }
completa E1 || { calma && fase E1 python3 -I $H/e1_b_real.py; }
completa E3x || { calma && fase E3x python3 -I $H/e3_extrae.py; }
if completa E3; then echo "$(date -u +%FT%TZ) e3_reglas ya COMPLETE (se salta)" >> $LOG; elif fuera_de_hora; then echo "$(date -u +%FT%TZ) e3_reglas OMITIDA (fuera de hora)" >> $LOG; else calma && fase e3_reglas python3 -I $H/e3_reglas.py; fi
FALLOS=""; PEND=""; FUERA=""; SINCALMA=""; MUERTOS=""; ASERT=""
dias=$(for i in $(seq 0 37); do date -u -d "2026-10-08 +$i day" +%F; done)
paso() { d=$1; fase E2_$d python3 -I $H/e2_dia.py $d; rc=$?
  case $rc in 0) return 0;; 3) PEND="$PEND $d"; return 3;; 137) limpia $d; MUERTOS="$MUERTOS $d"; return 137;; *) FALLOS="$FALLOS $d"; return 1;; esac; }
for d in $dias; do
  [ -z "$DRYRUN" ] && completo_d $d && continue
  if grep -q '"error": "ASSERT' $H/cache/pob_$d.json 2>/dev/null; then ASERT="$ASERT $d"; continue; fi   # FAILED por assert de integridad C3/C5/C7: no se reintenta, se lista
  if fuera_de_hora; then FUERA="$FUERA $d"; continue; fi
  if ! calma; then SINCALMA="$SINCALMA $d"; echo "$(date -u +%FT%TZ) E2_$d pospuesto: sin calma (45 min)" >> $LOG; continue; fi
  paso $d
done
for d in $SINCALMA $MUERTOS; do   # segunda y ultima pasada, tras recuperar la calma; un dia que vuelve a morir o no cabe queda INCOMPLETE
  [ -z "$DRYRUN" ] && completo_d $d && continue
  fuera_de_hora && break
  calma || continue
  paso $d
done
echo "$(date -u +%FT%TZ) E2 dias: FALLOS=[$FALLOS] PENDIENTES_DESENLACE=[$PEND] MUERTOS_OOM=[$MUERTOS] SIN_CALMA=[$SINCALMA] OMITIDOS_POR_HORA=[$FUERA] ASSERT_INTEGRIDAD=[$ASERT]" >> $LOG
for f in e2_agrega e5_regimen e6_brecha audit_final; do
  if fuera_de_hora; then echo "$(date -u +%FT%TZ) $f OMITIDA (fuera de hora)" >> $LOG; continue; fi
  calma || { echo "$(date -u +%FT%TZ) $f OMITIDA (sin calma)" >> $LOG; continue; }
  if [ -f $H/$f.py ]; then fase $f python3 -I $H/$f.py; else echo "$(date -u +%FT%TZ) $f.py NO EXISTE" >> $LOG; fi
done
echo "$(date -u +%FT%TZ) ===== FIN run_exp1 FALLOS=[$FALLOS] PEND=[$PEND] MUERTOS=[$MUERTOS] SIN_CALMA=[$SINCALMA] FUERA=[$FUERA] ASSERT=[$ASERT]" >> $LOG
