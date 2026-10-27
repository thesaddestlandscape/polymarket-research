#!/bin/bash
cd "$(dirname "$0")/.."
ulimit -v 3000000
nice -n 19 ionice -c3 python3 -I scripts/build_set.py > logs/build_set_$(date -u +%Y%m%dT%H%M%SZ).log 2>&1
echo "exit $?" > logs/build_set.done
