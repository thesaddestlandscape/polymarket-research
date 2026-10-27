#!/bin/bash
# run_e1c.sh -- ejecuta E1C completo (senales + evaluacion) con manifiesto. Reanudable: senales salta mercados ya en el checkpoint.
# Uso: nice -n 19 ionice -c3 bash run_e1c.sh   (fuera de 06-09Z)
H=$(date -u +%H); if [ "$H" -ge 6 ] && [ "$H" -lt 9 ]; then echo "BLOQUEADO 06-09Z"; exit 2; fi
AQ=$(cd "$(dirname "$0")" && pwd); D=$AQ/../datos; OUT=/root/polymarket-research-datalogs/e1_cancelacion_ms
unset E1C_CK
INI=$(date -u +%FT%TZ)
man() { python3 - "$1" "$2" <<EOF
import json,hashlib,glob,sys
h=lambda p: hashlib.sha256(open(p,'rb').read()).hexdigest()[:16]
m=dict(job='E1C_cancelacion_ms', inicio='$INI', fin=sys.argv[2], estado=sys.argv[1],
 codigo={p.split('/')[-1]:h(p) for p in glob.glob('$AQ/*.py')+glob.glob('$AQ/*.sh')}, prereg=h('$AQ/../prereg/PREREG_E1C.md'),
 parametros=dict(lat_cancel_ms=60, lag_print_ms=30, paso_ms=10, train=['2026-10-20','2026-10-21'], test=['2026-10-22'], semilla=7),
 entradas={'ordenes_b.json':h('/root/polymarket-research-datalogs/cola_posicion/ordenes_b.json'),'b_l2.csv':h('$AQ/../../cola_posicion/datos/b_l2.csv'),'b_cola.csv':h('$AQ/../../cola_posicion/datos/b_cola.csv')},
 extraidos=sorted(p.split('/')[-1] for p in glob.glob('$OUT/maker_ms_*.gz')), salida=['$OUT/senales.csv.gz','datos/e1c_resultados.txt','datos/e1c_tabla.csv','datos/e1c_rellenos.csv'])
json.dump(m,open('$D/run_manifest.json','w'),indent=1)
EOF
}
man RUNNING ""
/usr/bin/time -v python3 $AQ/e1c_senales.py > $D/senales.stdout 2> $D/senales.time || { man FAILED "$(date -u +%FT%TZ)"; exit 1; }
python3 $AQ/e1c_eval.py > $D/eval.stdout 2>&1 || { man FAILED "$(date -u +%FT%TZ)"; exit 1; }
man COMPLETE "$(date -u +%FT%TZ)"
