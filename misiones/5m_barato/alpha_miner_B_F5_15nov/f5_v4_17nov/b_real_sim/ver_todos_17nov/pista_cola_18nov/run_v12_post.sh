#!/bin/bash
# run_v12_post.sh (ADENDA_12_19nov) -- NO lanzado por quien lo escribio. Cuando la cadena v11 marque COMPLETE re-corre SOLO p7 v12 (y p3 v12 DISENO) sobre los p1 ya hechos. No procesa p1 nuevos.
# Uso: ./run_v12_post.sh [--wait] [--veredicto]
#   --wait       espera (sondeo cada 300 s, sin pgrep/pkill) a out/verif_adenda11/chain.status = COMPLETE; sin --wait sale con WAITING_CHAIN (exit 3) si aun no lo esta.
#   --veredicto  ademas ejecuta p3 v12 de VEREDICTO sobre los p1 de dias de veredicto que ya existan (decision del chief/validador; por defecto NO).
# Un trabajo a la vez (scripts/cron_pesado.sh), nice 19, ionice -c3, ulimit -v 5 GB (ADENDA_06b, OK Javi 23-Nov; antes 3 GB), /usr/bin/time -v en los pasos p3 (pico en out/verif_adenda12/pico_<paso>.txt); ningun paso arranca en 06:00-09:00Z ni 22:15-22:30Z. Idempotente: p7 se salta si su JSON ya corresponde al codigo v12 y al pkl de p1 en disco.
# Contrato de job: out/verif_adenda12/run_manifest.json (job, hashes, parametros, dias, inicio/fin, estado), post.log con hora, post.status (RUNNING|COMPLETE_V12|FAILED_<paso>|BLOCKED_<motivo>|WAITING_CHAIN), post.pid (PID para parar), un .log por paso.
cd "$(dirname "$0")"; H=$(pwd); V=out/verif_adenda12; mkdir -p $V; LOG=$V/post.log; ST=$V/post.status; CHAIN=out/verif_adenda11/chain.status; CP=/root/polymarket-research/scripts/cron_pesado.sh
WAIT=0; VER=0; for a in "$@"; do [ "$a" = --wait ] && WAIT=1; [ "$a" = --veredicto ] && VER=1; done
say() { echo "$(date -u +%FT%TZ) $*" >> $LOG; }
manifest() { python3 -I - "$1" <<'PY'
import json, os, sys, hashlib, time
V = 'out/verif_adenda12'; mf = V + '/run_manifest.json'; st = sys.argv[1]
F = ['p3_agrega_v12.py', 'p7_ipw_balance_v12.py', 'cmp_p7_v11_v12.py', 'run_v12_post.sh', 'ADENDA_12_19nov.md', 'ADENDA_13_19nov.md', 'ADENDA_13b_19nov.md', 'p1_dia.py']
m = json.load(open(mf)) if os.path.exists(mf) else dict(job='pista_cola_v12_post', params=dict(chain_gate='out/verif_adenda11/chain.status=COMPLETE', veredicto=os.environ.get('V12_VER'), horas_prohibidas='06:00-09:00Z,22:15-22:30Z', ulimit_v_kb=5000000), start_utc=time.strftime('%FT%TZ', time.gmtime()))
m['codigo_sha256'] = {f: hashlib.sha256(open(f, 'rb').read()).hexdigest() for f in F if os.path.exists(f)}
m['dias_previstos'] = dict(fixture='2026-11-12_fxP1', DISENO=['2026-11-12', '2026-11-16'], veredicto_si_existe_p1=['2026-11-13', '2026-11-14', '2026-11-15', '2026-11-17', '2026-11-18', '2026-11-19'])
m['estado'] = st; m['ultima_actualizacion_utc'] = time.strftime('%FT%TZ', time.gmtime())
if st != 'RUNNING': m['end_utc'] = m['ultima_actualizacion_utc']
json.dump(m, open(mf, 'w'), indent=1)
PY
}
fail() { say "FALLO en $1"; echo "FAILED_$1 $(date -u +%FT%TZ)" > $ST; manifest FAILED_$1; exit 1; }
blocked() { say "BLOQUEADO: $1"; echo "BLOCKED_$1 $(date -u +%FT%TZ)" > $ST; manifest BLOCKED_$1; exit 2; }
ventana() { while true; do hm=$(date -u +%H%M); if { [ $hm -ge 0600 ] && [ $hm -lt 0900 ]; } || { [ $hm -ge 2215 ] && [ $hm -lt 2230 ]; }; then sleep 60; else break; fi; done; }
heavy() { local nm=$1; shift; ventana; say "inicio $nm"; $CP bash -c "ulimit -v 5000000; nice -n 19 ionice -c3 $*" >> $V/$nm.log 2>&1; local rc=$?; say "fin $nm rc=$rc"; return $rc; }
cs() { cut -d' ' -f1 $CHAIN 2>/dev/null; }
echo $$ > $V/post.pid
if [ "$(cs)" != COMPLETE ]; then
  if [ $WAIT = 0 ]; then echo "WAITING_CHAIN ($(cs))" ; echo "WAITING_CHAIN $(date -u +%FT%TZ)" > $ST; exit 3; fi
  say "esperando cadena v11 (estado $(cs)); tope 6 h"; t_w=$(date +%s)      # sin pgrep/pkill: se vigila el PID guardado en chain.pid
  while [ "$(cs)" != COMPLETE ]; do
    case "$(cs)" in FAILED_*) blocked cadena_v11_fallida;; esac
    cpid=$(cat out/verif_adenda11/chain.pid 2>/dev/null)
    if [ -z "$cpid" ] || ! kill -0 $cpid 2>/dev/null; then sleep 5; [ "$(cs)" = COMPLETE ] || blocked cadena_v11; fi
    [ $(( $(date +%s) - t_w )) -gt 21600 ] && blocked espera_6h
    sleep 300
  done
fi
echo "RUNNING $(date -u +%FT%TZ)" > $ST; export V12_VER=$VER; manifest RUNNING; say "cadena v11 COMPLETE; inicio post v12 (pid $$)"
# 0) hashes v12 congelados (ultimo bloque de HASHES_CODIGO.txt)
python3 -I - <<'PY' || blocked hashes_v12
import re, hashlib, sys
last = {}
for ln in open('HASHES_CODIGO.txt'):
    p = ln.split()
    if len(p) == 2 and re.fullmatch(r'[0-9a-f]{64}', p[0]): last[p[1]] = p[0]
bad = [n for n in ('p3_agrega_v12.py', 'p7_ipw_balance_v12.py', 'cmp_p7_v11_v12.py', 'run_v12_post.sh', 'ADENDA_12_19nov.md', 'ADENDA_13_19nov.md', 'ADENDA_13b_19nov.md', 'p1_dia.py') if last.get(n) != hashlib.sha256(open(n, 'rb').read()).hexdigest()]
print('discrepan', bad) if bad else None; sys.exit(1 if bad else 0)
PY
python3 -I tests_v12/test_v12.py >> $V/tests.log 2>&1 || fail tests_v12
# 1) p7 v12 sobre cada p1 existente: (nombre, pkl, sufijo). Salta si el JSON ya corresponde a este codigo y a este pkl.
ya_hecho() { python3 -I - "$1" "$2" "$3" <<'PY'
import json, sys, hashlib, os, pickle
j, pk, wp = sys.argv[1:4]
if not (os.path.exists(j) and os.path.exists(wp)): sys.exit(1)
h = lambda f: hashlib.sha256(open(f, 'rb').read()).hexdigest(); c, p = h('p7_ipw_balance_v12.py'), h(pk)
r = json.load(open(j)); w = pickle.load(open(wp, 'rb'))
ok = r.get('version') == 'p7_v12_ADENDA12' and r.get('SHA256_codigo') == c and r.get('SHA256_pkl_p1') == p and w.get('version') == 'p7w_v12' and w.get('SHA256_codigo') == c and w.get('SHA256_pkl_p1') == p
sys.exit(0 if ok else 1)
PY
}
WAITROT=""
sonda1_ok() { local D=$1 k fn; for k in -1 0 1; do fn=/root/polymarket-research-datalogs/sonda1/pasivo/sonda1_fotos_l2_$(date -u -d "$D $k day" +%F).csv.gz; [ -s $fn ] || { say "WAITING_ROTACION $D: falta $fn"; return 1; }; done; }
esperar_rot() { [ -z "$WAITROT" ] && return 0; say "WAITING_ROTACION:$WAITROT"; echo "WAITING_ROTACION$WAITROT $(date -u +%FT%TZ)" > $ST; manifest WAITING_ROTACION; exit 4; }
p7() { local D=$1 S=$2 NOTE=$3; local pk=out/p1_btc_${D}${S}.pkl j=out/p7v12_btc_${D}${S}.json w=out/p7wv12_btc_${D}${S}.pkl; [ -f $pk ] || { say "sin $pk: se omite"; return 0; }
  sonda1_ok $D || { WAITROT="$WAITROT $D$S"; return 0; }
  ya_hecho $j $pk $w && { say "p7 v12 $D$S ya hecho"; return 0; }
  rm -f $j $w; heavy p7v12_${D}${S} "env P7_NOTE=$NOTE python3 p7_ipw_balance_v12.py $pk $j $w"; ya_hecho $j $pk $w || fail p7v12_${D}${S}; }
p7 2026-11-12 _fxP1 fixture_fxP1 || exit 1      # misma nota que el fixture v11 (si no, `nota` difiere en cmp)
esperar_rot
python3 -I cmp_p7_v11_v12.py out/p7_btc_2026-11-12_fxP1.json out/p7v12_btc_2026-11-12_fxP1.json > $V/cmp_p7_v11_v12_fxP1.out 2>&1; rc=$?; say "cmp_p7_v11_v12 fixture rc=$rc"; [ $rc = 0 ] || fail cmp_p7_v11_v12
for D in 2026-11-16 2026-11-12; do p7 $D _DISENO DISENO_ADENDA12; done
for D in 2026-11-13 2026-11-14 2026-11-15 2026-11-17 2026-11-18 2026-11-19; do p7 $D "" VEREDICTO_ADENDA12_p7_solo_balance; done
esperar_rot
# 2) p3 v12: rc==0 obligatorio; rc 2 (BLOCKED de p3) -> BLOCKED_P3; otro rc -> FAILED_<paso>. Se borra la salida previa y se exige salida NUEVA (mtime >= inicio del paso, version p3_v7_ADENDA12): cron_pesado devuelve 0 aunque OMITA el job.
p3run() { local nm=$1 envs=$2 okj=$3; local bj=${okj%.json}_BLOCKED.json; rm -f $okj $bj; local t_ini=$(date +%s); heavy $nm "env $envs timeout 1500 /usr/bin/time -v -o $V/pico_$nm.txt python3 p3_agrega_v12.py btc act"; local rc=$?; say "$nm rc=$rc"
  [ $rc = 2 ] && blocked P3; [ $rc = 0 ] || fail $nm
  { [ -f $okj ] && [ $(stat -c %Y $okj) -ge $t_ini ]; } || fail ${nm}_sin_salida_nueva
  python3 -I -c "import json,sys; sys.exit(0 if json.load(open('$okj')).get('version') == 'p3_v7_ADENDA12' else 1)" || fail ${nm}_version; }
p3run p3v12_fxP1 "P3_DISENO=1 PISTA_SUF=_fxP1" out/p3v12_btc_act_fxP1_DISENO.json
p3run p3v12_DISENO "P3_DISENO=1 PISTA_SUF=_DISENO" out/p3v12_btc_act_DISENO.json
# 3) p3 v12 de veredicto: SOLO con --veredicto (decision del chief tras el validador); siempre se re-ejecuta
if [ $VER = 1 ]; then p3run p3v12_veredicto "" out/p3v12_btc_act.json; fi
echo "COMPLETE_V12 $(date -u +%FT%TZ)" > $ST; manifest COMPLETE_V12; say "post v12 COMPLETE"
