#!/bin/bash
# Reaceptacion tras editar evaluadores Q11 (la guardia por sha de eval_thru1 invalida thru1_fwd/aceptacion.json con cada edicion). NO quita la guardia: la regenera.
# Corre: py_compile, tests unitarios puros, aceptacion sobre quemados (thru1 + SOL013), `eval_thru1.py --aceptacion` (escribe thru1_fwd/aceptacion.json) y verifica pass_ + sha.
# Solo lectura de pickles; 0 ordenes. nice 19, ionice 3, ulimit 3 GB; no corre en 06:00-09:15Z. Uso: bash reaceptar.sh   (codigo de salida 0 = todo OK)
set -u
Q=/root/polymarket-research/experimentos/5m_barato/q11; F=/root/polymarket-research/misiones/5m_barato/forward_sol013
H=$(date -u +%H%M); if [ "$H" -ge 0600 ] && [ "$H" -lt 0915 ]; then echo "BLOQUEADO 06:00-09:15Z"; exit 2; fi
ulimit -v 3000000; export OMP_NUM_THREADS=1; run() { nice -n 19 ionice -c3 "$@"; }
cd $Q || exit 1; rc=0
run python3 -m py_compile $F/q11_decision.py $F/filtro_sol013.py eval_pistas.py eval_giro.py eval_thru1.py redteam/rt_cxj150_cross.py placebo_cxj150.py || { echo "FALLO py_compile"; exit 1; }
for t in tests/test_q11_decision.py tests/test_q11_aceptacion.py; do run python3 -I $t || { echo "FALLO $t"; rc=1; }; done
run python3 -I eval_thru1.py --aceptacion > /tmp/reaceptar_thru1.$$.json || { echo "FALLO eval_thru1 --aceptacion (aceptacion.json con pass_=false: los dias se acumulan sin evaluarse)"; rc=1; }
python3 -I - <<PY || rc=1
import json, sys
sys.path.insert(0, '$F'); sys.path.insert(0, '$Q'); import eval_thru1 as E
d = json.load(open('$Q/thru1_fwd/aceptacion.json')); sha = E.eval_sha()   # sha256(sha(eval_thru1.py) + sha(q11_decision.py))
ok = d['pass_'] and d['eval_sha'] == sha; print('aceptacion.json pass_=%s eval_sha=%s coincide=%s' % (d['pass_'], d['eval_sha'][:16], d['eval_sha'] == sha)); sys.exit(0 if ok else 1)
PY
rm -f /tmp/reaceptar_thru1.$$.json
echo "--- sha16 de los ficheros del parche ---"
sha256sum $F/q11_decision.py $F/filtro_sol013.py eval_pistas.py eval_giro.py eval_thru1.py redteam/rt_cxj150_cross.py tests/test_q11_decision.py tests/test_q11_aceptacion.py reaceptar.sh | awk '{print substr($1,1,16), $2}'
[ $rc -eq 0 ] && echo "REACEPTACION OK" || echo "REACEPTACION FALLIDA"; exit $rc
