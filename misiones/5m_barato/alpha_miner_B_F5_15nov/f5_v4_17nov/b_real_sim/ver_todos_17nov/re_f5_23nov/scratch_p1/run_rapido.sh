#!/bin/bash
cd "$(dirname "$0")/.."; O=out_rf5_ciego; : > $O/rapido_17nov.log
for G in A K; do ./lanza_pesado.sh $O/rapido_17nov.log $O/pico_rapido_${G}_17nov.txt python3 -I rf5_rapido_prueba.py 2026-11-17 $G; done
