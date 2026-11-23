#!/bin/bash
cd "$(dirname "$0")/.."; ulimit -v 3500000
python3 -I t_proc_cronometro.py 2026-11-17 500000 > out_rf5_ciego/t_proc_medicion_17nov.json 2> out_rf5_ciego/t_proc_medicion_17nov.err
echo "FIN rc=$?" >> out_rf5_ciego/t_proc_medicion_17nov.err
