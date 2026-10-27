#!/bin/bash
cd "$(dirname "$0")"; ulimit -v 3000000; export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MALLOC_ARENA_MAX=1
nice -n 19 ionice -c3 python3 sim.py >> sim_stdout.txt 2>> sim_stderr.txt
