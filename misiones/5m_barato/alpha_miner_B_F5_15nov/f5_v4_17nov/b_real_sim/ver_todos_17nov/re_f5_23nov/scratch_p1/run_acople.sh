#!/bin/bash
cd "$(dirname "$0")/.."; O=out_rf5_ciego; : > $O/acople_real_17nov.log
./lanza_pesado.sh $O/acople_real_17nov.log $O/pico_acople_17nov.txt python3 -I rf5_acople_real.py 2026-11-17 30
