#!/bin/bash
# espera a load5<12 y lanza la evaluación de 17-18 Oct (A6). Salida en el scratchpad.
S=/tmp/claude-0/-root-polymarket-research/cbc315b0-0ee3-4fbb-b193-997ca0900993/scratchpad/a6
D=$S/d
while true; do
  L=$(awk '{print int($2)}' /proc/loadavg); [ "$L" -lt 12 ] && break; sleep 15
done
cd /root/polymarket-research/experimentos/5m_barato/a6_detector_vivo
ulimit -v 3000000
TG=$(ls $D/*.TG.gz | sort -t_ -k3,3 -k4,4 | tr '\n' ' ')
B=$(ls $D/*.B.gz | sort -t_ -k3,3 -k4,4 | tr '\n' ' ')
nice -n 19 ionice -c3 python3 -I r5k_eval.py --desde 2026-10-17T12:00:00Z --hasta 2026-10-18T23:55:00Z --tg $TG --b $B \
  --k $D/k_2026-10-16.csv $D/k_2026-10-17.csv $D/k_2026-10-18.csv \
  --onchain /mnt/HC_Volume_106538179/m5_onchain/m5_onchain_2026-10-17.csv.gz /mnt/HC_Volume_106538179/m5_onchain/m5_onchain_2026-10-18.csv.gz \
  --out $S/eval_17_18.json > $S/eval_17_18.out 2>&1
echo FIN >> $S/eval_17_18.out
