#!/bin/bash
S=/tmp/claude-0/-root-polymarket-research/2f7d1d71-0bf0-4d96-b184-d3524a239dfe/scratchpad
s=1
while [ $s -le 99 ]; do
  e=$((s+2)); [ $e -gt 99 ] && e=99
  /root/polymarket-research/scripts/cron_pesado.sh bash $S/placebo_lote.sh $s $e; rc=$?
  if [ $rc -eq 3 ]; then sleep 300; continue; fi
  if [ $rc -ne 0 ]; then echo "driver: lote $s..$e rc=$rc" >> $S/placebo.log; exit 1; fi
  s=$((e+1))
done
touch $S/placebo.done; echo "driver completo $(date -u +%FT%TZ)" >> $S/placebo.log
