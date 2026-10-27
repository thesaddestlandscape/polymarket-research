#!/bin/bash
cd "$(dirname "$0")"; ulimit -v 3000000; export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MALLOC_ARENA_MAX=1
while [ "$(awk '{print ($2>8)}' /proc/loadavg)" = "1" ]; do sleep 30; done
nice -n 19 ionice -c3 python3 eval.py > eval_stdout.txt 2> eval_stderr.txt
